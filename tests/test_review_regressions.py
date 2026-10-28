"""Regressions for review findings at the frozen-generator publication boundary."""

import hashlib
import io
import json
import os
import re
import runpy
import subprocess
import sys
import urllib.error
import urllib.request
import urllib.response
from email.message import Message
from pathlib import Path

import pytest

from test_backfill_acceptance import (
    KEY_NAME as BACKFILL_KEY, SENTINEL_KEY as BACKFILL_SENTINEL,
    FakeUrlopen as BackfillUrlopen, requested_ids, run_cli as run_backfill_cli,
    videos_list_payload,
)
from test_claims_acceptance import (
    CONTEXT_ID, CONTEXT_VID, NEW_VID, add_followup, current_claim,
    generated_snapshot, proposals, run_generator, seed_corpus, write_json,
)
from test_supadata_canary import (
    KEY_NAME, SENTINEL_KEY, SCRIPT as CANARY_SCRIPT, FakeResponse, FakeUrlopen,
    corpus, result_json, run_cli, transcript_payload, transcript_text as canary_text,
)
from test_transcript_conformance import validate_transcript
from test_workflow_safety import workflow


def apply_relation(root, date="2025-02-15T00:00:00Z", relation="refines"):
    seed_corpus(root)
    add_followup(root, date)
    path = proposals(root, relation)
    result = run_generator(root, "--relations", str(path))
    assert result.returncode == 0, result.stdout + result.stderr
    return path


@pytest.mark.parametrize("changed_vid,date", [
    (CONTEXT_VID, "2025-02-01T00:00:00Z"),
    (NEW_VID, "2025-01-15T00:00:00Z"),
    (NEW_VID, None),
])
def test_date_correction_does_not_reverse_a_committed_supersession(tmp_path, changed_vid, date):
    path = apply_relation(tmp_path)
    history = {p.name: p.read_bytes() for p in (tmp_path / "kb/history").glob("*.md")}
    log = (tmp_path / "kb/log.md").read_bytes()
    analysis_path = tmp_path / "analysis" / f"{changed_vid}.json"
    analysis = json.loads(analysis_path.read_text())
    analysis["published_at"] = date
    write_json(analysis_path, analysis)
    for extra in [(), ("--relations", str(path))]:
        result = run_generator(tmp_path, *extra)
        assert result.returncode == 0, result.stdout + result.stderr
        current, _ = current_claim(tmp_path)
        assert {s["id"] for s in current["sources"]} == {NEW_VID}
        assert current["valid_from"] == "2025-02-15T00:00:00Z"
        assert {p.name: p.read_bytes() for p in (tmp_path / "kb/history").glob("*.md")} == history
        assert (tmp_path / "kb/log.md").read_bytes() == log
    assert run_generator(tmp_path, "--check").returncode == 0


def test_date_backfill_does_not_reclassify_an_already_appended_relation(tmp_path):
    apply_relation(tmp_path, date=None)
    analysis_path = tmp_path / "analysis" / f"{NEW_VID}.json"
    analysis = json.loads(analysis_path.read_text())
    analysis["published_at"] = "2025-05-01T00:00:00Z"
    write_json(analysis_path, analysis)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    current, _ = current_claim(tmp_path)
    assert {s["id"] for s in current["sources"]} == {CONTEXT_VID, NEW_VID}
    assert not list((tmp_path / "kb/history").glob("*.md"))


def test_prior_decision_survives_complete_candidate_text_edit(tmp_path):
    apply_relation(tmp_path)
    history = {p.name: p.read_bytes() for p in (tmp_path / "kb/history").glob("*.md")}
    catalog_path = tmp_path / "data/catalog.json"
    catalog = json.loads(catalog_path.read_text())
    row = next(r for r in catalog["techniques"] if r["id"] == CONTEXT_ID)
    row["title"] = "Zebra nebula"
    row["mechanism"] = {"summary": "Zebra nebula", "variants": []}
    for source in row["sources"]:
        source["input_technique"] = "Zebra nebula"
    write_json(catalog_path, catalog)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    assert current_claim(tmp_path)[0]["title"] == "Zebra nebula"
    assert {p.name: p.read_bytes() for p in (tmp_path / "kb/history").glob("*.md")} == history
    assert run_generator(tmp_path, "--check").returncode == 0
    # A fresh incoming proposal still needs the candidate gate.
    path = proposals(tmp_path, "supports")
    before = generated_snapshot(tmp_path)
    assert run_generator(tmp_path, "--relations", str(path)).returncode != 0
    assert generated_snapshot(tmp_path) == before


@pytest.mark.parametrize("date", ["0001-01-01T00:00:00+14:00", "9999-12-31T23:59:59-14:00"])
def test_extreme_aware_source_date_becomes_unknown_without_traceback(tmp_path, date):
    seed_corpus(tmp_path, date=date)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    metadata, _ = current_claim(tmp_path)
    assert metadata["valid_from"] is None
    assert all(s["last_modified"] is None for s in metadata["sources"])


def replace_context_caption(root, catalog, body, quote):
    digest = hashlib.sha256(body.encode()).hexdigest()
    path = root / "transcripts" / f"{CONTEXT_VID}.txt"
    text = path.read_text()
    header = text.split("# auto/author captions, unverified\n")[0]
    header = re.sub(r"# sha256: [0-9a-f]+", f"# sha256: {digest}", header)
    path.write_text(header + "# auto/author captions, unverified\n" + body)
    analysis_path = root / "analysis" / f"{CONTEXT_VID}.json"
    analysis = json.loads(analysis_path.read_text())
    analysis["transcript_sha256"] = digest
    write_json(analysis_path, analysis)
    row = next(r for r in catalog["techniques"] if r["id"] == CONTEXT_ID)
    row["sources"][0].update(quote=quote, timestamp="00:01", quote_verification="normalized-exact")
    write_json(root / "data/catalog.json", catalog)


def test_quote_cannot_run_past_its_declared_timestamp_segment(tmp_path):
    catalog = seed_corpus(tmp_path)
    quote = "First segment finishes much later with unrelated evidence"
    replace_context_caption(tmp_path, catalog,
                            "[00:01] First segment\n[10:00] finishes much later with unrelated evidence\n", quote)
    assert run_generator(tmp_path).returncode == 0
    assert quote.encode() not in b"\n".join(generated_snapshot(tmp_path).values())


@pytest.mark.parametrize("quote", [" ".join(f"word{i}" for i in range(100)), "x" * 600])
def test_verified_quote_cannot_publish_an_unbounded_caption_body(tmp_path, quote):
    catalog = seed_corpus(tmp_path)
    replace_context_caption(tmp_path, catalog, f"[00:01] {quote}\n", quote)
    assert run_generator(tmp_path).returncode == 0
    assert quote.encode() not in b"\n".join(generated_snapshot(tmp_path).values())


def test_long_near_identical_repeated_vocabulary_passes_canary(tmp_path, monkeypatch):
    body = " ".join(["hello", "world", "caption", "system"] * 150)
    fetched = "hello inserted " + body[len("hello "):]
    vids = corpus(tmp_path, body=body)
    fake = FakeUrlopen(lambda *_: FakeResponse(200, transcript_payload(fetched)))
    code, stdout, stderr = run_cli(monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
                                    env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 0, stdout + stderr
    assert all(v["similarity"] >= 0.98 for v in result_json(stdout, stderr)["videos"])


@pytest.mark.parametrize("field,value", [("source", "https://www.youtube.com/watch?v=OTHER"),
                                          ("sha256", "0" * 64),
                                          ("retrieved_at", "2025-01-01T00:00:00Z")])
def test_duplicate_reference_fields_fail_before_fetch(tmp_path, monkeypatch, field, value):
    vids = corpus(tmp_path)
    path = tmp_path / "transcripts" / f"{vids[0]}.txt"
    text = path.read_text().replace("# auto/author", f"# {field}: {value}\n# auto/author")
    path.write_text(text)
    fake = FakeUrlopen(lambda *_: FakeResponse(200, transcript_payload("unused")))
    code, stdout, stderr = run_cli(monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
                                    env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    report = result_json(stdout, stderr)
    assert code == 1
    assert report["videos"][0]["reference_ok"] is False
    assert len(fake.calls) == 4
    assert validate_transcript(path), "conformance must also reject ambiguous headers"


@pytest.mark.parametrize("marker", ["machine transcript", "machine transcript (other engine)",
                                     "machine transcript (Whisper; no YouTube captions), unverified"])
def test_unrecognized_or_mixed_machine_reference_is_rejected(tmp_path, monkeypatch, marker):
    vids = corpus(tmp_path)
    path = tmp_path / "transcripts" / f"{vids[0]}.txt"
    path.write_text(path.read_text().replace("# auto/author", f"# {marker}\n# auto/author"))
    assert validate_transcript(path), "native label must not conceal any machine marker"
    fake = FakeUrlopen(lambda *_: FakeResponse(200, transcript_payload("unused")))
    _, stdout, stderr = run_cli(monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
                               env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert result_json(stdout, stderr)["videos"][0]["reference_ok"] is False
    assert len(fake.calls) == 4


@pytest.mark.parametrize("error", ["missing_api_key", "supadata_transport_error"])
def test_canary_errors_are_written_to_requested_report(tmp_path, monkeypatch, error):
    vids = corpus(tmp_path)
    out = tmp_path / "canary-report.json"
    def fail(*_):
        raise urllib.error.URLError("synthetic transport failure")
    fake = FakeUrlopen(fail)
    code, stdout, stderr = run_cli(monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
                                    "--out", str(out), env={KEY_NAME: None if error == "missing_api_key" else SENTINEL_KEY},
                                    urlopen=fake)
    assert code == 2
    report = result_json(stdout, stderr)
    assert report["code"] == error
    assert out.is_file(), "failure artifact is needed as much as a success artifact"
    assert json.loads(out.read_text()) == report


@pytest.mark.parametrize("location", ["http://api.supadata.ai/insecure", "https://other.invalid/captions"])
def test_canary_rejects_redirect_without_forwarding_api_key(monkeypatch, location):
    calls = []
    def respond(_self, request):
        calls.append(request)
        if len(calls) > 1:
            return FakeResponse(200, transcript_payload("caption"))
        headers = Message()
        headers["Location"] = location
        response = urllib.response.addinfourl(io.BytesIO(b""), headers, request.full_url, 302)
        response.msg = "Found"
        return response
    monkeypatch.setattr(urllib.request.HTTPSHandler, "https_open", respond)
    monkeypatch.setattr(urllib.request.HTTPHandler, "http_open", respond)
    module = runpy.run_path(str(CANARY_SCRIPT))
    status, content, detail = module["fetch_caption"]("VIDCAN01", SENTINEL_KEY)
    assert status == 302 and content is None and detail == "caption_http_error"
    assert len(calls) == 1, "a redirect must never receive the authenticated request"


def test_backfill_verifies_changed_checkout_before_commit():
    steps = workflow("backfill")["jobs"]["backfill"]["steps"]
    commit_index = next(i for i, s in enumerate(steps) if s.get("name") == "Commit analysis dates")
    verification = "\n".join(s.get("run", "") for s in steps[:commit_index])
    assert "pytest -q" in verification
    assert "scripts/generate_claims.py --check" in verification
    install = "\n".join(s.get("run", "") for s in steps[:commit_index])
    assert "pytest pyyaml" in install


@pytest.mark.parametrize("unresolved,expected_code", [(set(), 0), ({CONTEXT_VID}, 1)])
def test_backfill_workflow_pushes_dates_with_fresh_generated_bundle(tmp_path, monkeypatch,
                                                                  unresolved, expected_code):
    """A real date update must not be blocked by, or pushed with, stale claims."""
    root = tmp_path / "checkout"
    root.mkdir()
    seed_corpus(root, date=None)
    # Execute the actual generator from the workflow shell in this fixture repo.
    scripts = Path(__file__).resolve().parents[1] / "scripts"
    (root / "scripts").symlink_to(scripts, target_is_directory=True)
    assert run_generator(root).returncode == 0
    assert run_generator(root, "--check").returncode == 0
    before_bundle = generated_snapshot(root)
    before_transcripts = {p.name: p.read_bytes() for p in (root / "transcripts").glob("*.txt")}
    before_analyses = {p.name: json.loads(p.read_text()) for p in (root / "analysis").glob("*.json")}

    def git(*args, cwd=root):
        result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                                timeout=30)
        assert result.returncode == 0, result.stdout + result.stderr
        return result.stdout.strip()

    git("init", "--initial-branch=main")
    git("config", "user.name", "Workflow Test")
    git("config", "user.email", "workflow-test@example.invalid")
    git("config", "commit.gpgsign", "false")
    git("add", ".")
    git("commit", "-m", "fixture: undated generated bundle")
    baseline = git("rev-parse", "HEAD")
    remote = tmp_path / "remote.git"
    git("init", "--bare", str(remote))
    git("remote", "add", "origin", str(remote))
    git("push", "--set-upstream", "origin", "main")

    fetched_date = "2025-01-01T00:00:00Z"
    fake = BackfillUrlopen(lambda url, _: videos_list_payload(
        {vid: fetched_date for vid in requested_ids(url) if vid not in unresolved}))
    code, stdout, stderr = run_backfill_cli(
        monkeypatch, "--root", str(root), env={BACKFILL_KEY: BACKFILL_SENTINEL}, urlopen=fake)
    assert code == expected_code, stdout + stderr
    assert json.loads(stdout)["updated_files"] == 2 - len(unresolved)
    stale = run_generator(root, "--check")
    assert stale.returncode == 1, "the fixture must reproduce the stale-tree backfill failure"
    assert "llms-full.txt" in json.loads(stale.stdout)["stale"]

    # These unrelated local outputs must never enter the backfill commit.
    (root / "canary-report.json").write_text('{"status": "unrelated"}\n')
    (root / "state").mkdir()
    (root / "state/missing_transcripts.json").write_text('[]\n')
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (bin_dir / "python3").symlink_to(sys.executable)
    # Avoid recursively running this entire suite from inside its own test.
    # The generator, backfill, Git index, commit and local push remain real;
    # separate regressions verify pytest/generator failures prevent commits.
    pytest_stub = bin_dir / "pytest"
    pytest_stub.write_text('#!/bin/sh\ntest "$#" = 1 && test "$1" = -q\n')
    pytest_stub.chmod(0o755)
    env = {k: os.environ[k] for k in ("PATH", "HOME", "LANG") if k in os.environ}
    env["PATH"] = f"{bin_dir}:{env['PATH']}"
    steps = workflow("backfill")["jobs"]["backfill"]["steps"]
    validation = next(s for s in steps if s.get("name") == "Validate backfilled checkout")
    commit = next(s for s in steps if s.get("name") == "Commit analysis dates")
    for step in (validation, commit):
        assert step["if"] == (
            "steps.backfill.outputs.exit_code == '0' || steps.backfill.outputs.exit_code == '1'")
    shell = validation["run"] + "\n" + commit["run"]
    result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", shell], cwd=root,
                            env=env, capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stdout + result.stderr
    assert run_generator(root, "--check").returncode == 0
    metadata, _ = current_claim(root)
    expected_date = None if CONTEXT_VID in unresolved else fetched_date
    assert metadata["valid_from"] == expected_date
    assert {s["last_modified"] for s in metadata["sources"]} == {expected_date}
    after_bundle = generated_snapshot(root)
    changed_bundle = {name for name in after_bundle if after_bundle[name] != before_bundle.get(name)}
    assert "llms-full.txt" in changed_bundle
    changed_analyses = {f"analysis/{filename}" for filename, original in before_analyses.items()
                        if original["vid"] not in unresolved}
    committed = set(git("diff", "--name-only", baseline, "HEAD").splitlines())
    assert committed == changed_analyses | changed_bundle
    assert git("rev-parse", "main", cwd=remote) == git("rev-parse", "HEAD")
    assert git("diff", "HEAD") == "", "all tracked date and generated changes must be committed"
    assert git("ls-files", "canary-report.json", "state/missing_transcripts.json") == ""
    assert {p.name: p.read_bytes() for p in (root / "transcripts").glob("*.txt")} == before_transcripts
    for filename, original in before_analyses.items():
        updated = json.loads((root / "analysis" / filename).read_text())
        expected = dict(original)
        if original["vid"] not in unresolved:
            expected["published_at"] = fetched_date
        assert updated == expected
    # A second run must not create a redundant commit or churn output timestamps.
    published_head = git("rev-parse", "HEAD")
    replay = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", shell], cwd=root,
                            env=env, capture_output=True, text=True, timeout=30)
    assert replay.returncode == 0, replay.stdout + replay.stderr
    assert git("rev-parse", "HEAD") == published_head
    assert generated_snapshot(root) == after_bundle


def test_refresh_preserves_read_only_discovery_as_artifact():
    document = workflow("refresh")
    steps = document["jobs"]["discovery"]["steps"]
    upload = next((s for s in steps if s.get("uses", "").startswith("actions/upload-artifact@")), None)
    assert upload is not None
    assert upload["with"]["path"] == "state/missing_transcripts.json"
    assert upload["with"]["if-no-files-found"] == "error"
    assert document["permissions"] == {"contents": "read"}
    assert not any("git push" in s.get("run", "") for s in steps)


def test_machine_transcript_documented_format_conforms(tmp_path):
    readme = (Path(__file__).resolve().parents[1] / "transcripts/README.md").read_text()
    # A producer following the exact documented labels can build a conforming
    # header; it must not need an undocumented unverified marker.
    labels = re.findall(r"`(# (?:machine transcript[^`]+|unverified))`", readme)
    text = canary_text("VIDCAN01").replace("# auto/author captions, unverified", "\n".join(labels))
    path = tmp_path / "VIDCAN01.txt"
    path.write_text(text)
    assert validate_transcript(path) == []


@pytest.mark.parametrize("failing_command,failing_args", [
    ("pytest", "-q"),
    ("python3", "scripts/generate_claims.py"),
    ("python3", "scripts/generate_claims.py --check"),
])
def test_backfill_validation_failure_stops_before_commit_or_push(tmp_path, failing_command,
                                                               failing_args):
    steps = workflow("backfill")["jobs"]["backfill"]["steps"]
    validation = next(s for s in steps if s.get("name") == "Validate backfilled checkout")
    commit = next(s for s in steps if s.get("name") == "Commit analysis dates")
    for executable in ("pytest", "python3", "git"):
        path = tmp_path / executable
        path.write_text('#!/bin/sh\nprintf "%s\\n" "' + executable + ' $*" >> "$CALLS"\n'
                        + (f'if [ "$*" = "{failing_args}" ]; then exit 1; fi\n'
                           if executable == failing_command else "") + "exit 0\n")
        path.chmod(0o755)
    calls = tmp_path / "calls"
    env = dict(os.environ, PATH=f"{tmp_path}:{os.environ['PATH']}", CALLS=str(calls))
    shell = validation["run"] + "\n" + commit["run"]
    result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", shell], env=env,
                            cwd=tmp_path, capture_output=True, text=True)
    assert result.returncode == 1
    assert "git " not in calls.read_text(), "failed verification must prevent all commit actions"


@pytest.mark.parametrize("field,change", [("vid", "missing"), ("takeaway_index", 99),
                                           ("catalog_id", "missing")])
def test_prior_relations_still_require_valid_references(tmp_path, field, change):
    apply_relation(tmp_path)
    path = tmp_path / "kb/context-engineering/context-composition.md"
    block, body = path.read_text()[4:].split("\n---\n", 1)
    metadata = json.loads(block)
    metadata["relations"][0][field] = change
    path.write_text("---\n" + json.dumps(metadata) + "\n---\n" + body)
    before = generated_snapshot(tmp_path)
    result = run_generator(tmp_path)
    assert result.returncode == 2
    assert "error" in json.loads(result.stdout)
    assert generated_snapshot(tmp_path) == before


def test_legacy_persisted_supersession_is_migrated_without_date_redecision(tmp_path):
    apply_relation(tmp_path)
    path = tmp_path / "kb/context-engineering/context-composition.md"
    block, body = path.read_text()[4:].split("\n---\n", 1)
    metadata = json.loads(block)
    metadata.pop("relation_transitions", None)
    path.write_text("---\n" + json.dumps(metadata) + "\n---\n" + body)
    analysis_path = tmp_path / "analysis" / f"{NEW_VID}.json"
    analysis = json.loads(analysis_path.read_text())
    analysis["published_at"] = None
    write_json(analysis_path, analysis)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    current, _ = current_claim(tmp_path)
    assert current["valid_from"] == "2025-02-15T00:00:00Z"
    assert {s["id"] for s in current["sources"]} == {NEW_VID}


@pytest.mark.parametrize("body,quote", [
    ("[00:01] First segment\nfinishes right here\n", "First segment finishes right here"),
    ("[00:01] First segment has some intervening words and finishes here\n", "First segment … finishes here"),
])
def test_short_quote_can_span_continuation_lines_at_same_timestamp(tmp_path, body, quote):
    catalog = seed_corpus(tmp_path)
    replace_context_caption(tmp_path, catalog, body, quote)
    catalog_path = tmp_path / "data/catalog.json"
    catalog = json.loads(catalog_path.read_text())
    row = next(r for r in catalog["techniques"] if r["id"] == CONTEXT_ID)
    row["sources"][0]["quote_verification"] = "ordered-ellipsis-pieces" if "…" in quote else "normalized-exact"
    write_json(catalog_path, catalog)
    assert run_generator(tmp_path).returncode == 0
    assert quote in current_claim(tmp_path)[1]


@pytest.mark.parametrize("marker", ["#  machine transcript (Whisper; no YouTube captions)",
                                    "#\tmachine transcript (Whisper; no YouTube captions)",
                                    "# Machine transcript (Whisper; no YouTube captions)"])
def test_machine_marker_variants_withhold_quote_from_generated_claim(tmp_path, marker):
    catalog = seed_corpus(tmp_path)
    quote = "Distinctive evidence for this claim"
    replace_context_caption(tmp_path, catalog, f"[00:01] {quote}\n", quote)
    path = tmp_path / "transcripts" / f"{CONTEXT_VID}.txt"
    path.write_text(path.read_text().replace("# auto/author captions, unverified", marker + "\n# auto/author captions, unverified"))
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    assert quote.encode() not in b"\n".join(generated_snapshot(tmp_path).values())


@pytest.mark.parametrize("quote,allowed", [
    (" ".join(["word"] * 50), True),
    (" ".join(["word"] * 51), False),
    ("x" * 500, True),
    ("x" * 501, False),
])
def test_quote_length_exact_boundaries(tmp_path, quote, allowed):
    catalog = seed_corpus(tmp_path)
    replace_context_caption(tmp_path, catalog, f"[00:01] {quote}\n", quote)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    assert (quote.encode() in b"\n".join(generated_snapshot(tmp_path).values())) is allowed
