"""Offline acceptance checks for the documented publish-date CLI contract.

Exercise real JSON files and the public CLI; only the HTTP boundary is faked.
No credentials, live metadata, or generator-derived expectations are used.
"""

from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import runpy
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlsplit
import urllib.request

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "backfill_publish_dates.py"
STAMP = "2026-10-27T12:34:56Z"
KEY = "TEST_ONLY_METADATA_KEY_DO_NOT_LOG"


def analysis(root, vid, published_at=None, name=None):
    """Create a real-envelope record, including fields the backfill must preserve."""
    directory = root / "analysis"
    directory.mkdir(exist_ok=True)
    payload = {"vid": vid, "takeaways": [{"text": "Keep verbatim", "score": 3}],
               "confidence": "high", "unrelated": {"nested": [1, False, None]}}
    if published_at is not None:
        payload["published_at"] = published_at
    path = directory / (name or f"{vid}.json")
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=4) + "\n")
    return path


def snapshot(root):
    """Capture every input byte, not merely its parsed fields."""
    return {p.name: p.read_bytes() for p in (root / "analysis").glob("*.json")}


class Response:
    """Context-managed JSON response implementing the urllib read boundary."""

    def __init__(self, payload):
        self.raw = payload if isinstance(payload, bytes) else json.dumps(payload).encode()

    def read(self, size):
        return self.raw[:size]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def metadata(ids, stamp=STAMP):
    """Build videos.list data without referring to production parsing helpers."""
    return {"items": [{"id": vid, "snippet": {"publishedAt": stamp}} for vid in ids]}


def cli(monkeypatch, root, *args, http=None, key=KEY):
    """Run the CLI in-process with a hermetic HTTP boundary and captured output."""
    if key is None:
        monkeypatch.delenv("YOUTUBE_API_KEY", raising=False)
    else:
        monkeypatch.setenv("YOUTUBE_API_KEY", key)

    def no_network(*args, **kwargs):
        pytest.fail("this operation must not call the network")

    monkeypatch.setattr(urllib.request, "urlopen", http or no_network)
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), "--root", str(root), *args])
    stdout, stderr = io.StringIO(), io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        with pytest.raises(SystemExit) as exit_info:
            runpy.run_path(str(SCRIPT), run_name="__main__")
    assert stderr.getvalue() == ""
    output = stdout.getvalue()
    assert KEY not in output
    assert "googleapis.com" not in output
    assert "Traceback" not in output
    return exit_info.value.code, json.loads(output)


@pytest.mark.parametrize("known, expected", [(18, 1), (19, 0), (20, 0)])
def test_offline_95_percent_boundary_counts_distinct_videos(tmp_path, monkeypatch, known, expected):
    """Duplicate files cannot inflate the distinct-video coverage denominator."""
    for i in range(20):
        analysis(tmp_path, f"VIDEO{i:02d}", STAMP if i < known else None)
    for i in range(3):
        analysis(tmp_path, "VIDEO00", STAMP, name=f"duplicate-{i}.json")
    before = snapshot(tmp_path)
    code, report = cli(monkeypatch, tmp_path, "--check", key=None)
    assert code == expected
    assert report["videos"] == 20
    assert report["analysis_files"] == 23
    assert report["dated_videos"] == known
    assert report["coverage"] == known / 20
    assert report["required_coverage"] == 0.95
    assert report["updated_files"] == 0
    assert snapshot(tmp_path) == before


def test_empty_corpus_cannot_pass(tmp_path, monkeypatch):
    """An empty scaffold is not evidence of real-corpus date coverage."""
    code, report = cli(monkeypatch, tmp_path, "--check", key=None)
    assert code == 1
    assert report["code"] == "insufficient_publish_dates"
    assert report["videos"] == report["dated_videos"] == 0
    assert report["coverage"] == 0


@pytest.mark.parametrize("other, conflict", [
    ("2026-10-27T14:34:56+02:00", False),
    ("2026-10-27T12:34:57Z", True),
])
def test_duplicates_compare_instants_not_offset_strings(tmp_path, monkeypatch, other, conflict):
    """Equivalent offsets are not conflicts; different instants are."""
    analysis(tmp_path, "VIDEO00", STAMP)
    analysis(tmp_path, "VIDEO00", other, name="duplicate.json")
    before = snapshot(tmp_path)
    code, report = cli(monkeypatch, tmp_path, "--check")
    assert code == int(conflict)
    assert report["conflicting_ids"] == (["VIDEO00"] if conflict else [])
    assert snapshot(tmp_path) == before


def test_every_duplicate_record_requires_a_date(tmp_path, monkeypatch):
    """One known record must not conceal an undated record for the same video."""
    analysis(tmp_path, "VIDEO00", STAMP)
    analysis(tmp_path, "VIDEO00", name="duplicate.json")
    code, report = cli(monkeypatch, tmp_path, "--check")
    assert code == 1
    assert report["videos"] == 1
    assert report["dated_videos"] == 0
    assert report["unresolved_ids"] == ["VIDEO00"]


@pytest.mark.parametrize("dry_run", [False, True])
def test_batches_metadata_only_preserves_fields_and_exact_timestamps(tmp_path, monkeypatch, dry_run):
    """A 53-video lookup batches 50+3; existing valid records stay byte-identical."""
    for i in range(53):
        analysis(tmp_path, f"VIDEO{i:02d}")
    retained = analysis(tmp_path, "KNOWN00", "2025-01-02T03:04:05+03:00")
    before = snapshot(tmp_path)
    calls = []
    api_stamp = "2026-10-27T14:34:56.123+02:00"

    def http(request, timeout):
        parts = urlsplit(request.full_url)
        query = parse_qs(parts.query)
        assert parts.scheme == "https"
        assert parts.netloc == "www.googleapis.com"
        assert parts.path == "/youtube/v3/videos"
        assert query["part"] == ["snippet"]
        assert query["key"] == [KEY]
        assert query["fields"] == ["items(id,snippet(publishedAt))"]
        assert timeout == 30
        ids = query["id"][0].split(",")
        assert "KNOWN00" not in ids
        calls.append(ids)
        return Response(metadata(ids, api_stamp))

    code, report = cli(monkeypatch, tmp_path, *( ["--dry-run"] if dry_run else []), http=http)
    assert code == 0
    assert list(map(len, calls)) == [50, 3]
    assert len(set(sum(calls, []))) == 53
    assert report["proposed_updates"] == 53
    assert report["updated_files"] == (0 if dry_run else 53)
    assert report["dated_videos"] == report["videos"] == 54
    assert retained.read_bytes() == before[retained.name]
    if dry_run:
        assert snapshot(tmp_path) == before
    else:
        for name, original in before.items():
            expected = json.loads(original)
            if name != retained.name:
                expected["published_at"] = api_stamp
            assert json.loads((tmp_path / "analysis" / name).read_bytes()) == expected
        after = snapshot(tmp_path)
        replay_code, replay = cli(monkeypatch, tmp_path)
        assert replay_code == 0
        assert replay["updated_files"] == replay["proposed_updates"] == 0
        assert snapshot(tmp_path) == after
    assert not list((tmp_path / "analysis").glob(".published-at-*"))


@pytest.mark.parametrize("bad", [
    b"not JSON", [], {}, {"items": None}, {"items": [], "error": {"message": KEY}},
    {"items": [None]}, metadata(["UNREQUESTED"]), metadata(["VIDEO00", "VIDEO00"]),
    metadata(["VIDEO00"], "2026-10-27"),
    metadata(["VIDEO00"], "2026-10-27T12:34:56"),
    {"items": [{"id": "VIDEO00", "snippet": {}}]},
])
def test_malformed_api_response_never_writes(tmp_path, monkeypatch, bad):
    """Malformed or foreign metadata fails closed, without exposing raw data."""
    analysis(tmp_path, "VIDEO00")
    before = snapshot(tmp_path)
    code, report = cli(monkeypatch, tmp_path, http=lambda *a, **k: Response(bad))
    assert code == 2
    assert report["code"] == "invalid_api_response"
    assert report["retryable"] is False
    assert snapshot(tmp_path) == before


def test_later_batch_error_does_not_persist_earlier_batch(tmp_path, monkeypatch):
    """All network batches must validate before any analysis replacement."""
    for i in range(51):
        analysis(tmp_path, f"VIDEO{i:02d}")
    before = snapshot(tmp_path)
    calls = []

    def http(request, timeout):
        ids = parse_qs(urlsplit(request.full_url).query)["id"][0].split(",")
        calls.append(ids)
        if len(calls) == 2:
            raise URLError(f"private diagnostic {KEY}")
        return Response(metadata(ids))

    code, report = cli(monkeypatch, tmp_path, http=http)
    assert list(map(len, calls)) == [50, 1]
    assert code == 2
    assert report["code"] == "youtube_transport_error"
    assert report["retryable"] is True
    assert snapshot(tmp_path) == before


@pytest.mark.parametrize("status, retryable", [(403, False), (429, True), (500, True)])
def test_http_failures_are_sanitized(tmp_path, monkeypatch, status, retryable):
    """Key-bearing URLs and response diagnostics must not reach CLI output."""
    analysis(tmp_path, "VIDEO00")
    before = snapshot(tmp_path)

    def http(request, timeout):
        raise HTTPError(request.full_url, status, f"private error {KEY}", {}, None)

    code, report = cli(monkeypatch, tmp_path, http=http)
    assert code == 2
    assert report["code"] == "youtube_http_error"
    assert report["retryable"] is retryable
    assert snapshot(tmp_path) == before


def test_omitted_video_stays_unresolved_and_partial_progress_is_real(tmp_path, monkeypatch):
    """Unavailable videos get no fabricated date while successful metadata persists."""
    missing = analysis(tmp_path, "MISSING00")
    found = analysis(tmp_path, "FOUND00")
    original = missing.read_bytes()
    code, report = cli(monkeypatch, tmp_path, http=lambda *a, **k: Response(metadata(["FOUND00"])))
    assert code == 1
    assert report["unresolved_ids"] == ["MISSING00"]
    assert report["updated_files"] == 1
    assert report["coverage"] == 0.5
    assert missing.read_bytes() == original
    assert json.loads(found.read_text())["published_at"] == STAMP


def test_conflicting_api_date_is_not_written_to_duplicate(tmp_path, monkeypatch):
    """Fetched metadata must not overwrite or conflict with retained provenance."""
    analysis(tmp_path, "VIDEO00", STAMP)
    analysis(tmp_path, "VIDEO00", name="duplicate.json")
    before = snapshot(tmp_path)
    code, report = cli(monkeypatch, tmp_path, http=lambda *a, **k: Response(
        metadata(["VIDEO00"], "2025-01-01T00:00:00Z")))
    assert code == 1
    assert report["code"] == "conflicting_publish_dates"
    assert report["conflicting_ids"] == ["VIDEO00"]
    assert report["updated_files"] == 0
    assert snapshot(tmp_path) == before


@pytest.mark.parametrize("payload", [[], {}, {"vid": "../escape"}, {"video_id": "LEGACY00"}])
def test_invalid_analysis_fails_before_network_or_writes(tmp_path, monkeypatch, payload):
    """Legacy or malformed inputs need an explicit adapter, not a guessed ID."""
    path = analysis(tmp_path, "VIDEO00")
    path.write_text(json.dumps(payload))
    before = snapshot(tmp_path)
    code, report = cli(monkeypatch, tmp_path)
    assert code == 2
    assert report["code"] == "invalid_analysis"
    assert snapshot(tmp_path) == before


def test_symlinked_analysis_is_rejected_without_touching_target(tmp_path, monkeypatch):
    """Backfill cannot replace or mutate an out-of-corpus symlink target."""
    outside = tmp_path / "outside.json"
    outside.write_text(json.dumps({"vid": "VIDEO00"}))
    (tmp_path / "analysis").mkdir()
    (tmp_path / "analysis" / "link.json").symlink_to(outside)
    before = outside.read_bytes()
    code, report = cli(monkeypatch, tmp_path)
    assert code == 2
    assert report["code"] == "unsafe_analysis_path"
    assert outside.read_bytes() == before


def test_missing_key_fails_before_network(tmp_path, monkeypatch):
    """Metadata mode requires an explicit credential; offline check does not."""
    analysis(tmp_path, "VIDEO00")
    code, report = cli(monkeypatch, tmp_path, key=None)
    assert code == 2
    assert report["code"] == "missing_api_key"


def test_filesystem_failure_reports_partial_write_without_leaking_error(tmp_path, monkeypatch):
    """Per-file atomicity is not a corpus transaction; error status must survive."""
    first = analysis(tmp_path, "VIDEO00")
    second = analysis(tmp_path, "VIDEO01")
    retained_second = second.read_bytes()
    replace = Path.replace
    calls = []

    def fail_second(path, target):
        calls.append(target)
        if len(calls) == 2:
            raise OSError(f"private filesystem diagnostic {KEY}")
        return replace(path, target)

    monkeypatch.setattr(Path, "replace", fail_second)
    code, report = cli(monkeypatch, tmp_path, http=lambda *a, **k: Response(
        metadata(["VIDEO00", "VIDEO01"])))
    assert code == 2
    assert report["code"] == "write_failed"
    assert json.loads(first.read_text())["published_at"] == STAMP
    assert second.read_bytes() == retained_second
    assert not list((tmp_path / "analysis").glob(".published-at-*"))
