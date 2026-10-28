"""Offline acceptance for the publication artifact, independent of its builder.

Run with pytest, or without extra packages:
    python3 -m unittest discover -s tests -p 'test_site_publication*.py' -v

--check validates an existing artifact against its source without changing
source/output bytes, modes or modification times. A missing output must not be
created. This suite does not test a deployed renderer, browser navigation,
transcript conformance, claim generation, or real-corpus acceptance thresholds.
"""

import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import re
import tempfile
import unittest
from urllib.parse import urljoin, urlsplit

from site_publication_fixtures import (
    EXCLUDED_FILES,
    GENERATED_PATHS,
    OTHER_SHA,
    PAYLOAD_PATHS,
    SITE_URL,
    SOURCE_FILES,
    SOURCE_SHA,
    STAGE_SCRIPT,
    VIDEO,
    git_commit,
    make_source,
    run_stage,
    tree_snapshot,
    write_files,
)


class LandingLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.redirects = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.redirects.append(attrs.get("content", ""))


class SitePublicationAcceptance(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="publication-acceptance-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "source"
        self.out = self.base / "artifact"
        make_source(self.root)
        self.assertTrue(
            STAGE_SCRIPT.is_file(),
            "Missing publication CLI: scripts/stage_site.py must implement the offline artifact contract",
        )

    def stage(self, *, out=None, source_sha=SOURCE_SHA, check=False):
        return run_stage(self.root, out or self.out, source_sha=source_sha, check=check)

    def stage_ok(self, **kwargs):
        result = self.stage(**kwargs)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def manifest(self):
        path = self.out / "manifest.json"
        self.assertTrue(path.is_file(), "Successful staging must emit manifest.json")
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as error:
            self.fail(f"Manifest must be UTF-8 JSON: {error}")
        self.assertIsInstance(manifest, dict)
        self.assertIn("files", manifest)
        self.assertIsInstance(manifest["files"], list)
        return manifest

    def manifest_rows(self):
        rows = self.manifest()["files"]
        for row in rows:
            self.assertIsInstance(row, dict)
            self.assertEqual(set(row), {"path", "sha256", "size", "content_type"})
            self.assertIsInstance(row["path"], str)
        return rows

    def assert_read_only_check_rejects(self):
        before = tree_snapshot(self.base)
        result = self.stage(check=True)
        self.assertNotEqual(result.returncode, 0, "--check accepted an invalid artifact")
        self.assertEqual(tree_snapshot(self.base), before, "--check modified the source or artifact")

    def rewrite_manifest(self, transform):
        manifest = self.manifest()
        transform(manifest)
        (self.out / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    def test_exact_positive_allowlist_excludes_checkout_and_hidden_inputs(self):
        write_files(self.root, EXCLUDED_FILES)
        self.stage_ok()
        actual = {p.relative_to(self.out).as_posix() for p in self.out.rglob("*") if p.is_file()}
        self.assertEqual(actual, PAYLOAD_PATHS | {"manifest.json"})
        self.assertEqual({row["path"] for row in self.manifest_rows()}, PAYLOAD_PATHS)
        staged = b"\n".join(path.read_bytes() for path in self.out.rglob("*") if path.is_file())
        self.assertNotIn(b"EXCLUDED_", staged)

    def test_every_public_source_file_is_preserved_byte_for_byte(self):
        self.stage_ok()
        for relative, expected in SOURCE_FILES.items():
            with self.subTest(path=relative):
                self.assertTrue((self.out / relative).is_file())
                self.assertEqual((self.out / relative).read_bytes(), expected)

    def test_manifest_is_the_exact_payload_inventory_with_hash_size_and_mime(self):
        self.stage_ok()
        rows = self.manifest_rows()
        expected_bytes = dict(SOURCE_FILES)
        for path in GENERATED_PATHS:
            self.assertTrue((self.out / path).is_file())
            expected_bytes[path] = (self.out / path).read_bytes()
        mime_types = {
            ".md": "text/markdown; charset=utf-8",
            ".json": "application/json; charset=utf-8",
            ".html": "text/html; charset=utf-8",
            ".txt": "text/plain; charset=utf-8",
        }
        expected = [{
            "path": path,
            "sha256": hashlib.sha256(content).hexdigest(),
            "size": len(content),
            "content_type": mime_types[PurePosixPath(path).suffix],
        } for path, content in sorted(expected_bytes.items())]
        self.assertEqual(sorted(rows, key=lambda row: row["path"]), expected)
        self.assertEqual(len(rows), len(PAYLOAD_PATHS), "Duplicate manifest entries are forbidden")

    def test_retained_history_and_all_directory_indexes_are_in_the_manifest(self):
        self.stage_ok()
        paths = {row["path"] for row in self.manifest_rows()}
        self.assertTrue({
            "kb/index.md", "kb/log.md", "kb/techniques/index.md",
            "kb/techniques/context-composition/index.md",
            "kb/techniques/context-composition/revisions/index.md",
            "kb/techniques/context-composition/revisions/context-composition-v1.md",
            "kb/techniques/context-composition/revisions/context-composition-v2.md",
        }.issubset(paths))
        self.assertIn(b"status: deprecated", (self.out / "kb/techniques/context-composition/revisions/context-composition-v1.md").read_bytes())
        self.assertEqual((self.out / "kb/log.md").read_bytes(), SOURCE_FILES["kb/log.md"])

    def test_landing_shell_explicitly_routes_to_kb_not_an_assumed_nested_index(self):
        self.stage_ok()
        landing = self.out / "index.html"
        self.assertTrue(landing.is_file(), "Root requires its own HTML landing shell")
        parser = LandingLinks()
        parser.feed(landing.read_text(encoding="utf-8"))
        targets = {urljoin(SITE_URL + "/", link) for link in parser.links}
        redirect_targets = {
            urljoin(SITE_URL + "/", match.group(1).strip(" \"'"))
            for value in parser.redirects
            if (match := re.search(r"url\s*=\s*(.+)", value, re.IGNORECASE))
        }
        self.assertIn(SITE_URL + "/kb/", targets | redirect_targets)
        self.assertTrue((self.out / "kb/index.md").is_file())
        for shadow in ["index.htm", "index.md", "README.md", "readme.md"]:
            self.assertFalse((self.out / shadow).exists(), f"{shadow} must not shadow root routing")

    def test_relative_bundle_links_resolve_inside_the_staged_inventory(self):
        self.stage_ok()
        manifest_paths = {row["path"] for row in self.manifest_rows()}
        for relative, original in SOURCE_FILES.items():
            if not relative.startswith("kb/") or not relative.endswith(".md"):
                continue
            content = (self.out / relative).read_bytes()
            self.assertEqual(content, original, "Publication must not rewrite bundle-relative links")
            for target in re.findall(r"\]\(([^\s)]+)\)", content.decode("utf-8")):
                resolved = urlsplit(urljoin(SITE_URL + "/" + relative, target))
                if resolved.netloc == urlsplit(SITE_URL).netloc:
                    with self.subTest(page=relative, target=target):
                        self.assertIn(resolved.path.lstrip("/"), manifest_paths)

    def test_llms_index_uses_absolute_canonical_urls_and_exact_full_text_path(self):
        self.stage_ok()
        content = (self.out / "llms.txt").read_text(encoding="utf-8")
        urls = re.findall(r"https?://[^\s<>\])\"']+", content)
        self.assertIn(SITE_URL + "/llms-full.txt", urls)
        self.assertNotIn("llms-full.md", content)
        for target in re.findall(r"\]\(([^\s)]+)\)", content):
            with self.subTest(target=target):
                self.assertTrue(target.startswith(SITE_URL + "/"), "llms resource links must be absolute")
        self.assertIn(SITE_URL + "/kb/index.md", urls)
        self.assertIn(SITE_URL + f"/analysis/{VIDEO}.json", urls)
        self.assertIn(SITE_URL + f"/transcripts/{VIDEO}.txt", urls)
        paths = {row["path"] for row in self.manifest_rows()}
        for target in urls:
            parsed = urlsplit(target)
            if parsed.netloc == urlsplit(SITE_URL).netloc:
                self.assertIn(parsed.path.lstrip("/"), paths)

    def test_both_root_llms_files_have_exact_plain_text_content_types(self):
        self.stage_ok()
        rows = {row["path"]: row for row in self.manifest_rows()}
        for path in ["llms.txt", "llms-full.txt"]:
            with self.subTest(path=path):
                self.assertIn(path, rows)
                self.assertEqual(rows[path]["content_type"], "text/plain; charset=utf-8")
                self.assertFalse((self.out / "llms-full.md").exists())

    def test_generated_llms_bytes_and_hashes_ignore_separately_authored_root_text(self):
        self.stage_ok()
        paths = ["llms.txt", "llms-full.txt"]
        original = {path: (self.out / path).read_bytes() for path in paths}
        original_rows = {row["path"]: row for row in self.manifest_rows() if row["path"] in paths}
        write_files(self.root, {
            "llms.txt": b"EXCLUDED_SEPARATELY_AUTHORED_INDEX\n",
            "llms-full.txt": b"EXCLUDED_SEPARATELY_AUTHORED_CORPUS\n",
        })
        second = self.base / "second-artifact"
        self.stage_ok(out=second)
        for path in paths:
            with self.subTest(path=path):
                self.assertEqual((second / path).read_bytes(), original[path])
                self.assertEqual(hashlib.sha256((second / path).read_bytes()).hexdigest(), original_rows[path]["sha256"])
                self.assertNotIn(b"EXCLUDED_", (second / path).read_bytes())

    def test_llms_full_tracks_bundle_content_not_an_independent_corpus(self):
        self.stage_ok()
        first = (self.out / "llms-full.txt").read_bytes()
        for relative, content in SOURCE_FILES.items():
            if relative.startswith("kb/") and relative.endswith(".md"):
                with self.subTest(path=relative):
                    self.assertIn(content.rstrip(b"\n"), first, "Full text must retain the exact staged bundle content, including history")
        changed_claim = self.root / "kb/techniques/context-composition/revisions/context-composition-v2.md"
        changed_claim.write_bytes(changed_claim.read_bytes() + b"\nPUBLICATION_CONTENT_CHANGE_123\n")
        second = self.base / "second-artifact"
        self.stage_ok(out=second)
        second_full = (second / "llms-full.txt").read_bytes()
        self.assertNotEqual(second_full, first)
        self.assertIn(b"PUBLICATION_CONTENT_CHANGE_123", second_full)
        second_manifest = json.loads((second / "manifest.json").read_text(encoding="utf-8"))
        row = next(row for row in second_manifest["files"] if row["path"] == "llms-full.txt")
        self.assertEqual(row["sha256"], hashlib.sha256(second_full).hexdigest())
        self.assertEqual(row["size"], len(second_full))

    def test_llms_index_tracks_new_staged_bundle_paths(self):
        self.stage_ok()
        first = (self.out / "llms.txt").read_bytes()
        write_files(self.root, {"kb/addendum/index.md": b"# Publication addendum\n"})
        second = self.base / "second-artifact"
        self.stage_ok(out=second)
        content = (second / "llms.txt").read_text(encoding="utf-8")
        self.assertNotEqual(content.encode("utf-8"), first)
        self.assertIn(SITE_URL + "/kb/addendum/index.md", content)

    def test_txt_artifacts_are_stored_bytes_not_html_viewer_documents(self):
        self.stage_ok()
        for path in self.out.rglob("*.txt"):
            with self.subTest(path=path.relative_to(self.out).as_posix()):
                content = path.read_bytes().lower()
                self.assertNotRegex(content, rb"<!doctype\s+html|<html(?:\s|>)|<body(?:\s|>)|<iframe(?:\s|>)")
        self.assertEqual((self.out / f"transcripts/{VIDEO}.txt").read_bytes(), SOURCE_FILES[f"transcripts/{VIDEO}.txt"])

    def test_viewer_html_in_a_txt_source_is_rejected_without_publishing_it(self):
        write_files(self.root, {f"transcripts/{VIDEO}.txt": b"<!doctype html><html><body>Rendered Source Raw Download Files</body></html>"})
        result = self.stage()
        self.assertNotEqual(result.returncode, 0, "An HTML response saved as a transcript must fail closed")
        self.assertFalse((self.out / "manifest.json").exists(), "Invalid text must not yield a publishable manifest")

    def test_manifest_binds_explicit_source_commit_and_versioned_digests(self):
        self.stage_ok()
        manifest = self.manifest()
        self.assertEqual(manifest.get("source_commit"), SOURCE_SHA)
        for field in ["allowlist_digest", "artifact_digest"]:
            self.assertRegex(manifest.get(field, ""), r"^[0-9a-f]{64}$", field)
        self.assertIsInstance(manifest.get("tool_version"), str)
        self.assertTrue(manifest["tool_version"].strip())
        self.assertNotIn(manifest["tool_version"].lower(), {"unknown", "latest", "unversioned"})

    def test_source_commit_can_be_resolved_from_a_real_local_git_head(self):
        expected_sha = git_commit(self.root)
        self.stage_ok(source_sha=None)
        self.assertEqual(self.manifest().get("source_commit"), expected_sha)

    def test_explicit_full_source_commit_overrides_local_git_head(self):
        local_sha = git_commit(self.root)
        self.assertNotEqual(local_sha, SOURCE_SHA)
        self.stage_ok()
        self.assertEqual(self.manifest().get("source_commit"), SOURCE_SHA)

    def test_source_without_git_or_an_explicit_commit_fails_closed(self):
        before = tree_snapshot(self.root)
        result = self.stage(source_sha=None)
        self.assertNotEqual(result.returncode, 0, "Unknown source provenance must not be published")
        self.assertEqual(tree_snapshot(self.root), before)
        self.assertFalse((self.out / "manifest.json").exists())

    def test_unborn_git_head_without_override_fails_closed(self):
        (self.root / ".git").mkdir()
        (self.root / ".git/HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")
        result = self.stage(source_sha=None)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.out / "manifest.json").exists())

    def test_symbolic_short_or_malformed_source_overrides_fail_closed(self):
        for index, source in enumerate(["", "main", "HEAD", "0123456", "0" * 39, "g" * 40, "0" * 41, SOURCE_SHA + "\n"]):
            with self.subTest(source=repr(source)):
                out = self.base / f"invalid-source-{index}"
                result = self.stage(out=out, source_sha=source)
                self.assertNotEqual(result.returncode, 0, "Only an unambiguous full commit is accepted")
                self.assertFalse((out / "manifest.json").exists())

    def test_identical_inputs_produce_byte_identical_artifacts(self):
        self.stage_ok()
        second = self.base / "second-artifact"
        self.stage_ok(out=second)
        first_files = {p.relative_to(self.out).as_posix(): p.read_bytes() for p in self.out.rglob("*") if p.is_file()}
        second_files = {p.relative_to(second).as_posix(): p.read_bytes() for p in second.rglob("*") if p.is_file()}
        self.assertEqual(second_files, first_files)

    def test_excluded_file_changes_cannot_change_the_publication_digest(self):
        self.stage_ok()
        before = self.manifest()
        write_files(self.root, EXCLUDED_FILES)
        second = self.base / "second-artifact"
        self.stage_ok(out=second)
        after = json.loads((second / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(after, before)

    def test_allowed_byte_changes_change_artifact_but_not_allowlist_digest(self):
        self.stage_ok()
        before = self.manifest()
        (self.root / "kb/log.md").write_bytes(SOURCE_FILES["kb/log.md"] + b"\nA retained history amendment.\n")
        second = self.base / "second-artifact"
        self.stage_ok(out=second)
        after = json.loads((second / "manifest.json").read_text(encoding="utf-8"))
        self.assertNotEqual(after.get("artifact_digest"), before.get("artifact_digest"))
        self.assertEqual(after.get("allowlist_digest"), before.get("allowlist_digest"))

    def test_check_is_successful_offline_and_completely_read_only(self):
        self.stage_ok()
        before = tree_snapshot(self.base)
        self.stage_ok(check=True)
        self.assertEqual(tree_snapshot(self.base), before)

    def test_check_never_creates_a_missing_output_directory(self):
        before = tree_snapshot(self.base)
        result = self.stage(check=True)
        self.assertNotEqual(result.returncode, 2, "--check must be a supported CLI option")
        self.assertEqual(tree_snapshot(self.base), before)
        self.assertFalse(self.out.exists())

    def test_check_rejects_tampered_payload_without_repairing_it(self):
        self.stage_ok()
        (self.out / "kb/log.md").write_bytes(b"tampered history\n")
        self.assert_read_only_check_rejects()

    def test_check_rejects_an_extra_unmanifested_file(self):
        self.stage_ok()
        (self.out / "unexpected.txt").write_bytes(b"not in the allowlist\n")
        self.assert_read_only_check_rejects()

    def test_check_rejects_an_omitted_or_duplicated_manifest_entry(self):
        self.stage_ok()
        original = (self.out / "manifest.json").read_bytes()
        for mutation in [lambda value: value["files"].pop(), lambda value: value["files"].append(value["files"][0].copy())]:
            (self.out / "manifest.json").write_bytes(original)
            self.rewrite_manifest(mutation)
            self.assert_read_only_check_rejects()

    def test_check_rejects_wrong_hash_size_or_content_type(self):
        self.stage_ok()
        original = (self.out / "manifest.json").read_bytes()
        for key, value in [("sha256", "0" * 64), ("size", 999999), ("content_type", "text/html")]:
            with self.subTest(field=key):
                (self.out / "manifest.json").write_bytes(original)
                self.rewrite_manifest(lambda manifest: manifest["files"][0].__setitem__(key, value))
                self.assert_read_only_check_rejects()

    def test_check_rejects_forged_provenance_digests_and_tool_version(self):
        self.stage_ok()
        original = (self.out / "manifest.json").read_bytes()
        for field, value in [
            ("source_commit", OTHER_SHA), ("allowlist_digest", "0" * 64),
            ("artifact_digest", "0" * 64), ("tool_version", "forged-tool-version"),
        ]:
            with self.subTest(field=field):
                (self.out / "manifest.json").write_bytes(original)
                self.rewrite_manifest(lambda manifest: manifest.__setitem__(field, value))
                self.assert_read_only_check_rejects()

    def test_check_rejects_an_artifact_built_from_stale_source_bytes(self):
        self.stage_ok()
        (self.root / "kb/log.md").write_bytes(SOURCE_FILES["kb/log.md"] + b"\nNew source history.\n")
        self.assert_read_only_check_rejects()

    def test_external_symlink_is_never_followed_into_the_artifact(self):
        outside = self.base / "outside.txt"
        outside.write_bytes(b"EXCLUDED_EXTERNAL_SYMLINK\n")
        (self.root / "kb/linked.txt").symlink_to(outside)
        result = self.stage()
        if result.returncode == 0:
            self.assertFalse((self.out / "kb/linked.txt").exists())
            self.assertNotIn("kb/linked.txt", {row["path"] for row in self.manifest_rows()})
        else:
            self.assertFalse((self.out / "manifest.json").exists(), "Unsafe symlinks must not leave a publishable manifest")
        self.assertEqual(outside.read_bytes(), b"EXCLUDED_EXTERNAL_SYMLINK\n")

    def test_root_or_ancestor_output_paths_cannot_overwrite_the_source(self):
        before = tree_snapshot(self.root)
        for out in [self.root, self.base]:
            with self.subTest(out=out.name):
                result = self.stage(out=out)
                self.assertNotEqual(result.returncode, 0, "Output must not replace its source or an ancestor")
                self.assertEqual(tree_snapshot(self.root), before)


if __name__ == "__main__":
    unittest.main()
