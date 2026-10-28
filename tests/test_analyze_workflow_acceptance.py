"""Offline acceptance for the manual, single-video analyzer workflow.

YAML checks cover permissions, secret/data flow and the public-runner boundary.
Shell checks execute the workflow's real run blocks with an isolated environment
and recording CLI stubs: no GitHub, caption or model requests are possible.
They are not evidence of a live Actions run or of a secret's repository scope;
those require the separately approved provider and live acceptance.

The small shell harness resolves simple input/env/validated-output expressions,
not arbitrary GitHub expression code. It does not emulate checkout/artifact
Actions. Publication must have an inspectable git-add run block, and analysis
must invoke the existing scripts/backfill_publish_dates.py --check gate before
scripts/analyze_transcript.py. The gate's >=95% behavior belongs to its existing
tests, not this file. No provider, model, or repository-secret name is selected.
"""

import json
import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "analyze.yml"
VID = "VIDAAAA0001"
EXPR = re.compile(r"\$\{\{\s*(.*?)\s*\}\}")
SECRET = re.compile(r"\bsecrets\.([A-Za-z_][A-Za-z0-9_]*)\b")
INPUT = re.compile(r"\b(?:inputs\.|github\.event\.inputs\.)")
GATE = "scripts/backfill_publish_dates.py"
ANALYZER = "scripts/analyze_transcript.py"


def workflow():
    # Ordinary assertion failures, not collection/setup errors, while absent.
    assert WORKFLOW.is_file(), "Missing feature workflow: .github/workflows/analyze.yml"
    # BaseLoader preserves YAML's 'on' key rather than treating it as a boolean.
    data = yaml.load(WORKFLOW.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    assert isinstance(data, dict) and isinstance(data.get("jobs"), dict)
    return data


def steps(job):
    return job.get("steps", [])


def run_steps(job):
    return [step for step in steps(job) if "run" in step]


def input_name(data):
    triggers = data.get("on")
    assert isinstance(triggers, dict) and set(triggers) == {"workflow_dispatch"}, "Analysis is manual only"
    dispatch = triggers["workflow_dispatch"]
    assert isinstance(dispatch, dict)
    inputs = dispatch.get("inputs", {})
    assert len(inputs) == 1, "Exactly one video, never a bulk list/path/provider selector"
    name, spec = next(iter(inputs.items()))
    assert spec.get("type") == "string" and spec.get("required", "").lower() == "true"
    return name


def analysis_job(data):
    found = [(name, job) for name, job in data["jobs"].items()
             if any(ANALYZER in step.get("run", "") for step in steps(job))]
    assert len(found) == 1, "One inspectable single-video analyzer job is required"
    return found[0]


def publication_jobs(data):
    found = [(name, job) for name, job in data["jobs"].items()
             if any(re.search(r"\bgit\s+(?:-[^\n]+\s+)?add\b", step.get("run", "")) for step in steps(job))]
    assert found, "Publication must stage the one validated analysis path explicitly"
    return found


def permission_map(data, job):
    permissions = job.get("permissions", data.get("permissions", {}))
    if permissions == "read-all":
        return {"contents": "read"}
    assert isinstance(permissions, dict), "No write-all or implicit broad token permissions"
    return permissions


def dependencies(data, name, visited=None):
    visited = set() if visited is None else visited
    assert name not in visited, "Workflow job dependencies must be acyclic"
    needs = data["jobs"][name].get("needs", [])
    needs = [needs] if isinstance(needs, str) else needs
    result = set(needs)
    for parent in needs:
        assert parent in data["jobs"]
        result.update(dependencies(data, parent, visited | {name}))
    return result


def test_workflow_is_manual_one_video_on_public_runners():
    data = workflow()
    input_name(data)
    for job in data["jobs"].values():
        assert job.get("runs-on") == "ubuntu-latest"
        assert "strategy" not in job, "No video matrices/bulk fan-out"
        assert "uses" not in job, "Keep this bounded analyzer's permission/secret flow inspectable"


def test_analysis_checkout_and_token_are_read_only():
    data = workflow()
    _, job = analysis_job(data)
    permissions = permission_map(data, job)
    assert permissions.get("contents") == "read"
    assert all(value in ("read", "none") for value in permissions.values())
    checkouts = [step for step in steps(job) if step.get("uses", "").startswith("actions/checkout@")]
    assert checkouts
    assert all(step.get("with", {}).get("persist-credentials", "").lower() == "false" for step in checkouts)
    assert "environment" not in job, "Do not borrow an environment's runtime credentials"


def test_llm_secret_is_env_only_and_absent_from_publication_scope():
    data = workflow()
    _, analysis = analysis_job(data)
    analysis_secrets = set(SECRET.findall(json.dumps(analysis))) - {"GITHUB_TOKEN"}
    assert len(analysis_secrets) == 1, "Exactly one explicitly named model secret, with no fallback credentials"
    assert not SECRET.search(json.dumps(data.get("env", {}))), "Do not expose the model key globally"
    exposed_env = dict(analysis.get("env", {}))
    for step in steps(analysis):
        exposed_env.update(step.get("env", {}))
        assert not SECRET.search(step.get("run", "")), "Secrets enter shell through env, not expression interpolation"
    assert analysis_secrets <= set(SECRET.findall(json.dumps(exposed_env)))
    for _, job in publication_jobs(data):
        assert not analysis_secrets.intersection(SECRET.findall(json.dumps(job)))
        assert job.get("secrets") != "inherit"


def test_untrusted_input_is_never_interpolated_into_shell_source():
    data = workflow()
    input_name(data)
    for job in data["jobs"].values():
        for step in run_steps(job):
            for expression in EXPR.findall(step["run"]):
                assert not INPUT.search(expression), "Use env-to-shell input, never executable expression text"
            assert "eval " not in step["run"], "Never re-evaluate video input as shell source"


def live_analyzer(step):
    source = step["run"].replace("\\\n", " ")
    arguments = re.findall(re.escape(ANALYZER) + r"([^\n;&|]*)", source)
    return any("--check" not in value for value in arguments)


def test_date_coverage_gate_is_mandatory_before_live_analysis():
    data = workflow()
    _, job = analysis_job(data)
    runs = run_steps(job)
    gates = [i for i, step in enumerate(runs) if GATE in step["run"] and "--check" in step["run"]]
    analyzers = [i for i, step in enumerate(runs) if live_analyzer(step)]
    assert gates and analyzers and min(gates) <= min(analyzers)
    for index in gates:
        step = runs[index]
        assert step.get("continue-on-error", "false").lower() == "false"
        assert step.get("if", "success()").strip("${{ }}") in ("success()", "true")
        overrides = re.findall(r"--(?:min-coverage|coverage-threshold|coverage)(?:=|\s+)([\d.]+)", step["run"])
        assert all(float(value) >= 0.95 for value in overrides), "Publication-date coverage must not be relaxed"
    for index in analyzers:
        assert "always()" not in runs[index].get("if", "")
        assert runs[index].get("continue-on-error", "false").lower() == "false"


def test_publication_has_no_model_authority_and_depends_on_successful_analysis():
    data = workflow()
    analysis_name, _ = analysis_job(data)
    for name, job in publication_jobs(data):
        assert name != analysis_name, "A write-scoped job must not run the model"
        assert analysis_name in dependencies(data, name)
        assert permission_map(data, job).get("contents") == "write"
        assert "always()" not in job.get("if", "") and "failure()" not in job.get("if", "")
        assert not any(ANALYZER in step["run"] for step in run_steps(job))


def test_workflow_has_no_caption_fetch_bulk_or_private_host_path():
    data = workflow()
    serialized = json.dumps(data).lower()
    for forbidden in ("self-hosted", "/home/", "/srv/private", ".ts.net", "127.0.0.1", "169.254.",
                      "paperclip_api_key", "ssh_private_key", "supadata_api_key", "youtube_api_key"):
        assert forbidden not in serialized
    for job in data["jobs"].values():
        for step in run_steps(job):
            run = step["run"]
            assert not re.search(r"\b(?:ssh|scp|rsync|curl|wget)\b", run)
            assert not re.search(r"(?:supadata_canary|import_corpus|check_rss)\.py|--vids\b|--all\b", run)
            assert not re.search(r"\bgit\s+add\s+(?:-A|--all|\.\s*$)", run, re.M)


def render(value, name, video, env):
    """Only synthetic input, env and validated path outputs; no live service state."""
    def replace(match):
        expression = match.group(1).strip()
        if expression in (f"inputs.{name}", f"github.event.inputs.{name}"):
            return video
        if expression.startswith("secrets."):
            return "TESTONLY_FAKE_WORKFLOW_KEY"
        if expression.startswith("env."):
            key = expression[4:]
            assert key in env, f"Declare env dependency before using it: {key}"
            return env[key]
        if re.fullmatch(r"(?:needs|steps)\.[\w-]+\.outputs\.[\w-]+", expression):
            key = expression.rsplit(".", 1)[1].lower()
            if key in ("vid", "video_id"):
                return video
            if key in ("path", "analysis_path", "analysis_file", "output_path"):
                return f"analysis/{video}.json"
        if expression == "github.repository":
            return "example/knowledge"
        if expression == "github.sha":
            return "a" * 40
        if expression in ("github.ref_name", "github.event.repository.default_branch"):
            return "main"
        pytest.fail(f"Shell fixture needs an explicit synthetic value for expression: {expression}")
    return EXPR.sub(replace, str(value))


CLI_STUB = r'''#!/usr/bin/python3
import json, os, re, socket, sys
from pathlib import Path
name = Path(sys.argv[0]).name
args = sys.argv[1:]
log = Path(os.environ["TEST_CALL_LOG"])
def record(kind):
    with log.open("a") as stream:
        stream.write(json.dumps({"kind": kind, "args": args}) + "\n")
def no_network(*args, **kwargs):
    raise RuntimeError("Offline workflow fixture forbids network")
socket.socket.connect = no_network
socket.create_connection = no_network
if name == "git":
    record("git")
    if "diff" in args and "--quiet" in args:
        sys.exit(1)
    sys.exit(0)
if name in ("python", "python3"):
    if args and args[0].endswith("backfill_publish_dates.py"):
        record("coverage")
        assert "--check" in args
        print(json.dumps({"ok": os.environ["TEST_GATE_EXIT"] == "0", "coverage": 0.95}))
        sys.exit(int(os.environ["TEST_GATE_EXIT"]))
    if args and args[0].endswith("analyze_transcript.py"):
        record("analysis")
        vids = [a.split("=", 1)[1] for a in args if a.startswith("--vid=")]
        if "--vid" in args:
            vids.append(args[args.index("--vid") + 1])
        if len(vids) != 1:
            sys.exit(2)
        video = vids[0]
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video):
            sys.exit(2)
        root = Path(args[args.index("--root") + 1]) if "--root" in args else Path.cwd()
        path = root / "analysis" / (video + ".json")
        if "--check" not in args:
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps({"vid": video, "takeaways": [], "truncated": False}))
        print(json.dumps({"ok": True, "vid": video, "path": "analysis/" + video + ".json"}))
        sys.exit(0)
    if args and args[0] in ("-", "-c"):
        source = sys.stdin.read() if args[0] == "-" else args[1]
        sys.argv = args if args[0] == "-" else ["-c"] + args[2:]
        exec(compile(source, "<workflow-inline>", "exec"), {"__name__": "__main__"})
        sys.exit(0)
    # Installation is not the behavior under test and must not contact PyPI.
    if args[:2] == ["-m", "pip"]:
        record("install")
        sys.exit(0)
if name in ("pip", "pip3"):
    record("install")
    sys.exit(0)
record("forbidden-command")
sys.exit(97)
'''


def exercise(data, job, tmp_path, *, video=VID, gate_exit=0, publication=False):
    name = input_name(data)
    workspace = tmp_path / "checkout"
    workspace.mkdir(exist_ok=True)
    for directory in ("analysis", "data", "kb", "transcripts", "home", "bin"):
        (workspace / directory).mkdir(exist_ok=True)
    (workspace / "unrelated.txt").write_text("Must never be staged.\n")
    (workspace / "analysis" / "OTHER000001.json").write_text("{}\n")
    (workspace / "data" / "catalog.json").write_text('{"frozen":true}\n')
    (workspace / "kb" / "index.md").write_text("Generator-owned.\n")
    (workspace / "analysis" / f"{VID}.json").write_text('{"vid":"VIDAAAA0001"}\n')
    for command in ("python", "python3", "git", "pip", "pip3", "curl", "wget", "gh", "ssh", "scp", "rsync"):
        path = workspace / "bin" / command
        path.write_text(CLI_STUB)
        path.chmod(0o700)
    log = tmp_path / "calls.jsonl"
    log.write_text("")
    env = {
        "PATH": str(workspace / "bin") + os.pathsep + os.defpath,
        "HOME": str(workspace / "home"),
        "LANG": "C.UTF-8",
        "GITHUB_WORKSPACE": str(workspace),
        "GITHUB_ENV": str(tmp_path / "github-env"),
        "GITHUB_OUTPUT": str(tmp_path / "github-output"),
        "GITHUB_STEP_SUMMARY": str(tmp_path / "summary"),
        "TEST_CALL_LOG": str(log),
        "TEST_GATE_EXIT": str(gate_exit),
    }
    for context in (data, job):
        for key, value in context.get("env", {}).items():
            env[key] = render(value, name, video, env)
    results = []
    selected = run_steps(job)
    if publication:
        selected = [step for step in selected if re.search(r"\bgit\s+(?:-[^\n]+\s+)?add\b", step["run"])]
    assert selected, "The workflow must expose executable analysis/publication run blocks"
    for step in selected:
        local_env = env.copy()
        for key, value in step.get("env", {}).items():
            local_env[key] = render(value, name, video, local_env)
        shell = render(step["run"], name, video, local_env)
        result = subprocess.run(["/bin/bash", "--noprofile", "--norc", "-e", "-o", "pipefail", "-c", shell],
                                cwd=workspace, env=local_env, text=True, capture_output=True, timeout=10)
        results.append(result)
        if result.returncode:
            break
        # GitHub's supported simple NAME=value export format is enough for VID
        # and a validated analysis path. No arbitrary expression evaluation.
        env_file = Path(env["GITHUB_ENV"])
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                assert "=" in line, "Use a simple validated env-to-shell value"
                key, value = line.split("=", 1)
                env[key] = value
    calls = [json.loads(line) for line in log.read_text().splitlines()]
    assert not any(call["kind"] == "forbidden-command" for call in calls), "No network/host CLI may run"
    return workspace, calls, results


def test_real_analysis_shell_runs_coverage_before_one_video(tmp_path):
    data = workflow()
    _, job = analysis_job(data)
    _, calls, results = exercise(data, job, tmp_path)
    assert all(result.returncode == 0 for result in results), "\n".join(result.stderr for result in results)
    sequence = [call["kind"] for call in calls if call["kind"] == "coverage"
                or (call["kind"] == "analysis" and "--check" not in call["args"])]
    assert sequence and sequence[0] == "coverage"
    live = [call for call in calls if call["kind"] == "analysis" and "--check" not in call["args"]]
    assert len(live) == 1
    assert f"--vid={VID}" in live[0]["args"]


def test_failed_coverage_cannot_reach_analysis_or_publication(tmp_path):
    data = workflow()
    _, job = analysis_job(data)
    workspace, calls, results = exercise(data, job, tmp_path, gate_exit=1)
    assert any(call["kind"] == "coverage" for call in calls)
    assert not any(call["kind"] == "git" or (call["kind"] == "analysis" and "--check" not in call["args"])
                   for call in calls)
    assert any(result.returncode != 0 for result in results), "A failed prerequisite must fail the job"
    assert (workspace / "analysis" / f"{VID}.json").read_text() == '{"vid":"VIDAAAA0001"}\n'


@pytest.mark.parametrize("attack", ["$(touch injected-marker)", '`touch injected-marker`',
                                    '"; touch injected-marker; #', "VIDAAAA0001\ntouch injected-marker"])
def test_input_shell_syntax_is_inert_and_cannot_publish(tmp_path, attack):
    data = workflow()
    _, job = analysis_job(data)
    workspace, calls, results = exercise(data, job, tmp_path, video=attack)
    assert not (workspace / "injected-marker").exists(), "Video input executed as shell code"
    assert any(result.returncode != 0 for result in results), "Invalid IDs must stop the job"
    assert not any(call["kind"] == "git" for call in calls)
    assert (workspace / "analysis" / f"{VID}.json").read_text() == '{"vid":"VIDAAAA0001"}\n'


def test_publication_shell_stages_only_the_selected_analysis_despite_decoys(tmp_path):
    data = workflow()
    jobs = publication_jobs(data)
    staged = []
    for number, (_, job) in enumerate(jobs):
        location = tmp_path / str(number)
        location.mkdir()
        _, calls, results = exercise(data, job, location, publication=True)
        assert all(result.returncode == 0 for result in results), "\n".join(result.stderr for result in results)
        for call in calls:
            if call["kind"] == "git" and "add" in call["args"]:
                args = call["args"][call["args"].index("add") + 1:]
                assert not any(arg in ("-A", "--all", "-u", "--update") for arg in args)
                paths = [arg for arg in args if not arg.startswith("-")]
                assert paths == [f"analysis/{VID}.json"], "Never stage a directory, glob, catalog/kb or unrelated files"
                staged.extend(paths)
    assert staged, "A no-op publication stub must not make the allowlist test pass"


def test_all_actions_are_pinned_to_full_commit_shas():
    data = workflow()
    for job in data['jobs'].values():
        for step in steps(job):
            if 'uses' in step:
                assert re.fullmatch(r'[^@]+@[0-9a-f]{40}', step['uses'])


def test_dash_leading_video_ids_reach_the_analyzer_as_one_argument():
    # 21 of the published IDs start with '-'; `--vid "$X"` makes argparse read them as a flag.
    text = WORKFLOW.read_text()
    assert '--vid "$VIDEO_ID"' not in text
    assert text.count('--vid="$VIDEO_ID"') == 2
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--vid")
    assert parser.parse_args(['--vid=-561cZmir5Q']).vid == "-561cZmir5Q"
