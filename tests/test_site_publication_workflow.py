"""Offline policy tests for the site publisher's actual workflow configuration.

For auditable race gates, the publishing job consumes one preflight job's
outputs: source_commit, main_commit, artifact_digest, verified_artifact_digest,
base_version_id, current_version_id. Its job/credential-step conditions must
permit matched inputs and reject stale inputs. The job ID is not prescribed.

These tests interpret the configured GitHub expressions, not a mock publisher.
They do not dispatch Actions, contact Kofra, or prove remote compare-and-swap,
credential availability, review approval, canonical navigation, or deployment.
PyYAML is already used by this repository's test suite.
"""

import ast
import copy
import json
from pathlib import PurePosixPath
import re
import unittest

from site_publication_fixtures import REPO, SOURCE_SHA, OTHER_SHA


WORKFLOW = REPO / ".github/workflows/site-publish.yml"
GATE_OUTPUTS = {
    "source_commit", "main_commit", "artifact_digest", "verified_artifact_digest",
    "base_version_id", "current_version_id",
}
CREDENTIAL_NAME = re.compile(r"(?:KOFRA|DROPWAY).*(?:TOKEN|KEY|SECRET|CREDENTIAL|AUTH)", re.IGNORECASE)
SECRET_VALUE = re.compile(r"^\$\{\{\s*secrets\.[A-Za-z_][A-Za-z0-9_]*\s*\}\}$")


def condition_value(expression, context, *, step=False):
    """Evaluate the small declarative GHA condition language, fail on unknowns."""
    # A job's status depends on needs; a step's default success() concerns
    # preceding steps in that job, not the result of an upstream job.
    status_results = [] if step else [
        job.get("result", "success") for job in context.get("needs", {}).values()
    ]
    if expression is None:
        expression = "success()"
    if not isinstance(expression, str):
        raise ValueError("Workflow conditions must be expressions")
    expression = expression.strip()
    if expression.startswith("${{") and expression.endswith("}}"):
        expression = expression[3:-2].strip()
    expression = expression.replace("&&", " and ").replace("||", " or ")
    expression = re.sub(r"!(?!=)", " not ", expression).strip()
    # GHA allows hyphens in job IDs accessed with dotted context syntax.
    expression = re.sub(
        r"\b(?:needs|github|env|steps|inputs)(?:\.[A-Za-z_][A-Za-z0-9_-]*)+",
        lambda match: match.group(0).split(".")[0] + "".join(
            "[" + repr(part) + "]" for part in match.group(0).split(".")[1:]
        ),
        expression,
    )
    tree = ast.parse(expression, mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            return {"true": True, "false": False, "null": None}.get(node.id, context.get(node.id, ""))
        if isinstance(node, ast.Attribute):
            parent = evaluate(node.value)
            return parent.get(node.attr, "") if isinstance(parent, dict) else ""
        if isinstance(node, ast.Subscript):
            parent = evaluate(node.value)
            key = evaluate(node.slice)
            return parent.get(key, "") if isinstance(parent, dict) else ""
        if isinstance(node, ast.BoolOp):
            values = [bool(evaluate(value)) for value in node.values]
            return all(values) if isinstance(node.op, ast.And) else any(values)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            return not evaluate(node.operand)
        if isinstance(node, ast.Compare):
            left = evaluate(node.left)
            for operator, comparator in zip(node.ops, node.comparators):
                right = evaluate(comparator)
                if isinstance(operator, ast.Eq):
                    matched = left == right
                elif isinstance(operator, ast.NotEq):
                    matched = left != right
                else:
                    raise ValueError("Unsupported workflow comparison")
                if not matched:
                    return False
                left = right
            return True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            arguments = [evaluate(value) for value in node.args]
            functions = {
                "success": lambda: all(value == "success" for value in status_results),
                "always": lambda: True,
                "cancelled": lambda: "cancelled" in status_results,
                "failure": lambda: "failure" in status_results,
                "contains": lambda collection, value: value in collection,
                "startsWith": lambda value, prefix: value.startswith(prefix),
                "endsWith": lambda value, suffix: value.endswith(suffix),
                "fromJSON": json.loads,
            }
            if node.func.id in functions:
                return functions[node.func.id](*arguments)
        raise ValueError(f"Unsupported workflow condition node: {type(node).__name__}")

    explicit_status = any(
        isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        and node.func.id in {"success", "always", "failure", "cancelled"}
        for node in ast.walk(tree)
    )
    if not explicit_status and any(result != "success" for result in status_results):
        return False
    return bool(evaluate(tree.body))


class SitePublicationWorkflowAcceptance(unittest.TestCase):
    def setUp(self):
        self.assertTrue(WORKFLOW.is_file(), "Missing main-to-site workflow: .github/workflows/site-publish.yml")
        try:
            import yaml
        except ImportError:
            self.fail("The repository's workflow policy tests require its existing PyYAML test dependency")
        try:
            # BaseLoader preserves `on` as a string instead of YAML 1.1 boolean.
            self.workflow = yaml.load(WORKFLOW.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        except yaml.YAMLError as error:
            self.fail(f"Publisher workflow is not valid YAML: {error}")
        self.assertIsInstance(self.workflow, dict)
        self.assertIsInstance(self.workflow.get("jobs"), dict)
        self.jobs = self.workflow["jobs"]

    def credential_steps(self, job):
        return [step for step in job.get("steps", []) if any(
            CREDENTIAL_NAME.search(name) for name in step.get("env", {})
        )]

    def publication_gate(self):
        candidates = []
        for job_id, job in self.jobs.items():
            needs = job.get("needs", [])
            if isinstance(needs, str):
                needs = [needs]
            for dependency in needs:
                producer = self.jobs.get(dependency, {})
                if GATE_OUTPUTS.issubset(producer.get("outputs", {})) and self.credential_steps(job):
                    candidates.append((job_id, job, dependency))
        self.assertEqual(
            len(candidates), 1,
            "One credential-bearing publishing job must consume preflight source/main, artifact-digest and base/current-version outputs",
        )
        return candidates[0]

    def gate_context(self, job, dependency):
        needs = job.get("needs", [])
        if isinstance(needs, str):
            needs = [needs]
        context = {
            "github": {
                "ref": "refs/heads/main", "ref_name": "main", "sha": SOURCE_SHA,
                "event_name": "push", "repository": "TogetherWeOwn/ai-engineer-knowledge",
            },
            "needs": {name: {"result": "success", "outputs": {}} for name in needs},
            "env": {**self.workflow.get("env", {}), **job.get("env", {})},
        }
        context["needs"][dependency]["outputs"] = {
            "source_commit": SOURCE_SHA, "main_commit": SOURCE_SHA,
            "artifact_digest": "a" * 64, "verified_artifact_digest": "a" * 64,
            "base_version_id": "version-fixture-7", "current_version_id": "version-fixture-7",
        }
        return context

    def publishing_is_allowed(self, job, context):
        try:
            if not condition_value(job.get("if"), context):
                return False
            return any(condition_value(step.get("if"), context, step=True) for step in self.credential_steps(job))
        except (SyntaxError, ValueError, TypeError) as error:
            self.fail(f"Cannot verify publisher's declarative safety condition: {error}")

    def assert_gate_rejects(self, **changed_outputs):
        _, job, dependency = self.publication_gate()
        healthy = self.gate_context(job, dependency)
        self.assertTrue(self.publishing_is_allowed(job, healthy), "A matching approved-main artifact must have a usable publishing path")
        stale = copy.deepcopy(healthy)
        stale["needs"][dependency]["outputs"].update(changed_outputs)
        self.assertFalse(self.publishing_is_allowed(job, stale), f"Unsafe publication allowed for {changed_outputs}")

    def test_main_updates_trigger_the_workflow_without_untrusted_pr_events(self):
        triggers = self.workflow.get("on")
        self.assertIsInstance(triggers, dict)
        self.assertIn("push", triggers)
        self.assertIsInstance(triggers["push"], dict)
        self.assertEqual(triggers["push"].get("branches"), ["main"])
        self.assertNotIn("pull_request", triggers)
        self.assertNotIn("pull_request_target", triggers)

    def test_all_effective_repository_permissions_are_read_only(self):
        self.assertIn("permissions", self.workflow, "Default repository permissions must be explicit")
        for scope, permissions in [("workflow", self.workflow["permissions"])] + [
            (job_id, job.get("permissions", self.workflow["permissions"]))
            for job_id, job in self.jobs.items()
        ]:
            with self.subTest(scope=scope):
                self.assertIsInstance(permissions, dict, "Use explicit least-privilege scopes, not read-all/write-all")
                self.assertTrue(set(permissions.values()).issubset({"read", "none"}), "Publisher must not have repository write authority")
        _, publisher, _ = self.publication_gate()
        permissions = publisher.get("permissions", self.workflow["permissions"])
        self.assertEqual(permissions.get("contents"), "read")

    def test_remote_actions_are_immutable_sha_pins(self):
        uses = []
        for job in self.jobs.values():
            if "uses" in job:
                uses.append(job["uses"])
            uses.extend(step["uses"] for step in job.get("steps", []) if "uses" in step)
        for action in uses:
            with self.subTest(action=action):
                if action.startswith("./"):
                    self.assertNotIn("..", PurePosixPath(action).parts)
                elif action.startswith("docker://"):
                    self.assertRegex(action, r"@sha256:[0-9a-f]{64}$")
                else:
                    self.assertRegex(action, r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+@[0-9a-f]{40}$")

    def test_publications_serialize_per_site_across_commits_and_branches(self):
        _, publisher, _ = self.publication_gate()
        concurrency = publisher.get("concurrency", self.workflow.get("concurrency"))
        if isinstance(concurrency, str):
            group, cancel = concurrency, "false"
        else:
            self.assertIsInstance(concurrency, dict)
            group, cancel = concurrency.get("group", ""), concurrency.get("cancel-in-progress", "false")
        env = {**self.workflow.get("env", {}), **publisher.get("env", {})}
        group = re.sub(r"\$\{\{\s*env\.([A-Za-z_][A-Za-z0-9_]*)\s*\}\}", lambda match: env.get(match.group(1), ""), group)
        self.assertIn("ai-engineer-research", group, "Concurrency must bind the target site")
        self.assertNotRegex(group, r"github\.(?:sha|ref|ref_name|run_id|run_number)|artifact_digest")
        self.assertEqual(cancel, "false", "Do not interrupt a publisher between version capture and finalization")

    def test_stale_main_or_wrong_artifact_source_cannot_reach_publication(self):
        self.assert_gate_rejects(main_commit=OTHER_SHA)
        self.assert_gate_rejects(source_commit=OTHER_SHA)

    def test_unverified_or_replaced_artifact_digest_cannot_reach_publication(self):
        self.assert_gate_rejects(artifact_digest="b" * 64)
        self.assert_gate_rejects(verified_artifact_digest="b" * 64)
        self.assert_gate_rejects(artifact_digest="", verified_artifact_digest="")

    def test_stale_or_missing_base_version_cannot_reach_publication(self):
        self.assert_gate_rejects(current_version_id="version-fixture-8")
        self.assert_gate_rejects(base_version_id="", current_version_id="")

    def test_non_main_refs_and_failed_preflight_cannot_reach_publication(self):
        _, publisher, dependency = self.publication_gate()
        healthy = self.gate_context(publisher, dependency)
        self.assertTrue(self.publishing_is_allowed(publisher, healthy))
        for change in ["non-main", "failed-preflight"]:
            with self.subTest(change=change):
                context = copy.deepcopy(healthy)
                if change == "non-main":
                    context["github"]["ref"] = "refs/heads/feature-fixture"
                    context["github"]["ref_name"] = "feature-fixture"
                else:
                    context["needs"][dependency]["result"] = "failure"
                self.assertFalse(self.publishing_is_allowed(publisher, context))

    def test_kofra_credentials_are_step_scoped_secret_references_never_inline(self):
        for scope in [self.workflow, *self.jobs.values()]:
            self.assertFalse(any(CREDENTIAL_NAME.search(name) for name in scope.get("env", {})), "Kofra credentials must not be inherited by staging or artifact-upload steps")
        credentials = []
        for job in self.jobs.values():
            for step in job.get("steps", []):
                for name, value in step.get("env", {}).items():
                    if CREDENTIAL_NAME.search(name):
                        credentials.append(name)
                        self.assertRegex(value, SECRET_VALUE, "Publishing credentials must come only from GitHub secrets")
                # Passing secret expressions inside shell text can expose values or
                # inject shell syntax before execution. Secrets belong in env.
                self.assertNotIn("secrets.", step.get("run", ""))
                self.assertNotRegex(step.get("run", ""), r"(?m)^\s*set\s+-[A-Za-z]*x|(?m:^\s*(?:env|printenv)\s*$)")
                if step.get("uses", "").startswith("actions/upload-artifact@"):
                    self.assertFalse(any(CREDENTIAL_NAME.search(name) for name in step.get("env", {})))
                    self.assertNotIn("secrets.", json.dumps(step.get("with", {})))
        self.assertTrue(credentials, "The publisher must reference its existing Kofra credential through secrets")

    def test_artifact_uploads_cannot_capture_the_checkout_or_credentials(self):
        for job in self.jobs.values():
            for step in job.get("steps", []):
                if not step.get("uses", "").startswith("actions/upload-artifact@"):
                    continue
                self.assertEqual(step.get("with", {}).get("include-hidden-files", "false"), "false")
                paths = step.get("with", {}).get("path", "").splitlines()
                self.assertTrue(paths)
                for path in paths:
                    with self.subTest(path=path):
                        path = path.strip()
                        self.assertNotIn(path, {"", ".", "./", "*", "**", "./**", "**/*"})
                        self.assertFalse(PurePosixPath(path).is_absolute())
                        self.assertFalse({"..", ".git", ".github", ".env", "scripts", "policies"}.intersection(PurePosixPath(path).parts))

    def test_publisher_carries_verified_provenance_and_the_captured_base_version(self):
        _, publisher, dependency = self.publication_gate()
        reference_prefix = f"needs.{dependency}.outputs."
        publisher_envs = [step.get("env", {}) for step in self.credential_steps(publisher)]
        for field in ["source_commit", "artifact_digest", "base_version_id"]:
            self.assertTrue(
                any(any(reference_prefix + field in value for value in env.values()) for env in publisher_envs),
                f"The publishing step must receive its verified {field}; never reselect latest at publish time",
            )


if __name__ == "__main__":
    unittest.main()
