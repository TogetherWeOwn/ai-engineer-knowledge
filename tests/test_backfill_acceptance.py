"""Independent acceptance tests for the publish-date backfill.

Contract under test (from the repo docs, not from any implementation):

- CLI: ``scripts/backfill_publish_dates.py [--root PATH] [--check] [--dry-run]``
- Reads ``analysis/*.json`` records keyed by ``vid``; preserves ``takeaways``,
  string ``confidence`` and every other field; only ``published_at`` is filled.
- Source of dates is YouTube Data API v3 ``videos.list`` with ``part=snippet``
  in batches of at most 50 IDs. Only ``snippet.publishedAt`` may fill
  ``published_at``; existing valid aware timestamps stay verbatim.
- Exits: 0 means at least 95% of distinct video IDs have dates, 1 means
  incomplete coverage, 2 means an input/API/write error.
- ``--check`` is offline and read-only, needs no key, and fails on an empty
  corpus or below 95%. ``--dry-run`` fetches metadata but writes nothing.
- Every batch response must validate before any writes. Omitted videos stay
  unresolved. No secret value, request URL or raw API error may be printed.

These tests were written against that contract alone. Network behavior is
exercised in-process with a stubbed ``urlopen``; no test uses a real key or
touches the network.
"""

import io
import json
import runpy
import subprocess
import sys
import urllib.error
import urllib.request
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "backfill_publish_dates.py"

API_SCHEME = "https"
API_HOST = "www.googleapis.com"
API_PATH = "/youtube/v3/videos"

# Deliberately fake credential. It must never appear in any test output.
SENTINEL_KEY = "TESTONLY_FAKE_KEY_9f8e7d6c5b4a"
KEY_NAME = "YOUTUBE_API_KEY"

_MISSING = object()


# ---------------------------------------------------------------------------
# Fixture builders
# ---------------------------------------------------------------------------

def record(vid, takeaways=None, confidence="high", published_at=_MISSING, **extra):
    """One analysis record in the documented real envelope."""
    payload = {
        "vid": vid,
        "takeaways": takeaways if takeaways is not None else [f"Takeaway for {vid}"],
        "confidence": confidence,
        "video_url": f"https://www.youtube.com/watch?v={vid}",
        "title": f"Talk {vid}",
    }
    if published_at is not _MISSING:
        payload["published_at"] = published_at
    payload.update(extra)
    return payload


def write_analysis(root: Path, name: str, payload: dict) -> Path:
    target = root / "analysis"
    target.mkdir(parents=True, exist_ok=True)
    path = target / name
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def dated_corpus(root: Path, count: int, prefix="vid") -> list:
    """Write ``count`` dated single-record files; return their vids."""
    vids = []
    for i in range(count):
        vid = f"{prefix}{i:04d}ok"
        write_analysis(
            root,
            f"{vid}.json",
            record(vid, published_at=f"2025-06-{(i % 28) + 1:02d}T12:30:00Z"),
        )
        vids.append(vid)
    return vids


def undated_corpus(root: Path, count: int, prefix="vid") -> list:
    """Write ``count`` undated single-record files; return their vids."""
    vids = []
    for i in range(count):
        vid = f"{prefix}{i:04d}new"
        write_analysis(root, f"{vid}.json", record(vid))
        vids.append(vid)
    return vids


def snapshot(root: Path) -> dict:
    analysis = root / "analysis"
    if not analysis.is_dir():
        return {}
    return {p.name: p.read_bytes() for p in sorted(analysis.glob("*.json"))}


# ---------------------------------------------------------------------------
# CLI runners
# ---------------------------------------------------------------------------

def run_cli(monkeypatch, *args, env=None, urlopen=None):
    """Run the backfill CLI in-process so ``urlopen`` can be stubbed.

    Returns ``(returncode, stdout, stderr)``. The script is executed fresh on
    every call, exactly as ``__main__``, so ``from urllib.request import
    urlopen`` style imports also bind the stub.
    """
    assert SCRIPT.exists(), f"backfill script missing: {SCRIPT}"
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), *args])
    monkeypatch.syspath_prepend(str(SCRIPT.parent))
    for name, value in (env or {}).items():
        if value is None:
            monkeypatch.delenv(name, raising=False)
        else:
            monkeypatch.setenv(name, value)
    if urlopen is not None:
        monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        try:
            runpy.run_path(str(SCRIPT), run_name="__main__")
        except SystemExit as exc:
            code = exc.code
            code = code if isinstance(code, int) else (0 if code is None else 1)
        else:
            code = 0
    return code, out.getvalue(), err.getvalue()


def run_cli_subprocess(root: Path, *args):
    """Run the backfill CLI as a real subprocess (offline ``--check`` only)."""
    assert SCRIPT.exists(), f"backfill script missing: {SCRIPT}"
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root), *args],
        capture_output=True,
        text=True,
    )


def fail_if_network(url_or_request, *args, **kwargs):
    raise AssertionError(f"unexpected network request: {url_or_request!r}")


# ---------------------------------------------------------------------------
# Output assertions
# ---------------------------------------------------------------------------

def result_json(stdout: str, stderr: str):
    """All CLI output is JSON; results on stdout, remediation on either stream."""
    for text in (stdout, stderr):
        if text.strip():
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                continue
    pytest.fail(f"no JSON output produced: stdout={stdout!r} stderr={stderr!r}")


def assert_no_leak(stdout: str, stderr: str, urls=()):
    blob = stdout + "\n" + stderr
    assert SENTINEL_KEY not in blob, "secret value leaked into output"
    assert "key=" not in blob, "request URL query leaked into output"
    for url in urls:
        assert url not in blob, "request URL leaked into output"


def json_has_string(node, needle: str) -> bool:
    if isinstance(node, str):
        return node == needle
    if isinstance(node, list):
        return any(json_has_string(v, needle) for v in node)
    if isinstance(node, dict):
        return any(json_has_string(v, needle) for v in node.values())
    return False


def json_has_substring(node, needle: str) -> bool:
    if isinstance(node, str):
        return needle in node
    if isinstance(node, list):
        return any(json_has_substring(v, needle) for v in node)
    if isinstance(node, dict):
        return any(json_has_substring(v, needle) for v in node.values())
    return False


# ---------------------------------------------------------------------------
# API stubbing
# ---------------------------------------------------------------------------

class FakeResponse:
    def __init__(self, payload):
        self._body = json.dumps(payload).encode("utf-8")
        self.status = 200
        self.headers = {}

    def read(self, *args, **kwargs):
        return self._body

    def getcode(self):
        return 200

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class FakeUrlopen:
    """Stub for ``urllib.request.urlopen`` recording every request URL."""

    def __init__(self, handler):
        self.handler = handler
        self.urls: list = []

    def __call__(self, url_or_request, *args, **kwargs):
        if isinstance(url_or_request, urllib.request.Request):
            url = url_or_request.get_full_url()
        else:
            url = str(url_or_request)
        self.urls.append(url)
        payload = self.handler(url, len(self.urls) - 1)
        return FakeResponse(payload)


def requested_ids(url: str) -> list:
    qs = parse_qs(urlparse(url).query)
    ids = []
    for chunk in qs.get("id", []):
        ids.extend(part for part in chunk.split(",") if part)
    return ids


def assert_api_url(url: str, key: str = SENTINEL_KEY) -> list:
    """Assert the fixed videos.list request shape; return the requested IDs."""
    parts = urlparse(url)
    assert parts.scheme == API_SCHEME, url
    assert parts.netloc == API_HOST, url
    assert parts.path == API_PATH, url
    qs = parse_qs(parts.query)
    assert qs.get("part") == ["snippet"], url
    assert qs.get("key") == [key], "request must carry the configured key"
    ids = requested_ids(url)
    assert 1 <= len(ids) <= 50, f"batch of {len(ids)} IDs violates the <=50 limit"
    return ids


def videos_list_payload(dates_by_id: dict) -> dict:
    return {
        "kind": "youtube#videoListResponse",
        "items": [
            {
                "kind": "youtube#video",
                "id": vid,
                "snippet": {
                    "publishedAt": published_at,
                    "title": f"Talk {vid}",
                    "channelTitle": "AI Engineer",
                },
            }
            for vid, published_at in dates_by_id.items()
        ],
    }


def api_date(index: int) -> str:
    return f"2026-01-{(index % 28) + 1:02d}T10:00:00Z"


# ---------------------------------------------------------------------------
# --check: offline coverage gate
# ---------------------------------------------------------------------------

def test_check_all_dated_exits_zero(tmp_path: Path) -> None:
    dated_corpus(tmp_path, 3)
    result = run_cli_subprocess(tmp_path, "--check")
    assert result.returncode == 0, result.stderr
    result_json(result.stdout, result.stderr)


@pytest.mark.parametrize("layout", ["missing_dir", "empty_dir"])
def test_check_empty_corpus_fails(tmp_path: Path, layout: str) -> None:
    if layout == "empty_dir":
        (tmp_path / "analysis").mkdir()
    result = run_cli_subprocess(tmp_path, "--check")
    assert result.returncode != 0, "empty corpus must fail the coverage gate"


def test_check_empty_analysis_dir_exits_one(tmp_path: Path) -> None:
    (tmp_path / "analysis").mkdir()
    result = run_cli_subprocess(tmp_path, "--check")
    assert result.returncode == 1, result.stderr


def test_check_threshold_boundary(tmp_path: Path) -> None:
    dated_corpus(tmp_path, 19)
    undated_corpus(tmp_path, 1)
    result = run_cli_subprocess(tmp_path, "--check")
    assert result.returncode == 0, f"19/20 is exactly 95%: {result.stdout}"


def test_check_below_threshold_exits_one(tmp_path: Path) -> None:
    dated_corpus(tmp_path, 18)
    undated_corpus(tmp_path, 2)
    result = run_cli_subprocess(tmp_path, "--check")
    assert result.returncode == 1, result.stderr


def test_check_counts_distinct_ids_not_files(tmp_path: Path, monkeypatch) -> None:
    # 100 dated files for one video plus 5 undated videos: file counting would
    # report ~95% while distinct-ID counting reports 1/6. The gate is distinct.
    for i in range(100):
        write_analysis(tmp_path, f"dup{i:03d}.json",
                       record("VIDDUP", published_at="2025-05-05T05:05:05Z"))
    undated_corpus(tmp_path, 5)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--check", urlopen=fail_if_network)
    assert code == 1, stdout


def test_check_duplicate_requires_every_record_dated(tmp_path: Path, monkeypatch) -> None:
    # One dated + one undated record for the same video: the video is unknown.
    # 18 dated + this split video + 1 undated = 18/20 -> must fail.
    write_analysis(tmp_path, "split-a.json",
                   record("VIDSPLIT", published_at="2025-05-05T05:05:05Z"))
    write_analysis(tmp_path, "split-b.json", record("VIDSPLIT"))
    dated_corpus(tmp_path, 18)
    undated_corpus(tmp_path, 1)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--check", urlopen=fail_if_network)
    assert code == 1, stdout


def test_check_conflicting_dates_fail_and_report(tmp_path: Path, monkeypatch) -> None:
    write_analysis(tmp_path, "conflict-a.json",
                   record("VIDCONF", published_at="2025-01-10T10:00:00Z"))
    write_analysis(tmp_path, "conflict-b.json",
                   record("VIDCONF", published_at="2026-03-01T10:00:00Z"))
    dated_corpus(tmp_path, 3)
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--check", urlopen=fail_if_network)
    assert code == 1, stdout
    obj = result_json(stdout, stderr)
    assert "VIDCONF" in obj.get("conflicting_ids", []), stdout
    assert snapshot(tmp_path) == before, "--check must not modify anything"


def test_check_equivalent_instants_are_not_conflicts(tmp_path: Path, monkeypatch) -> None:
    write_analysis(tmp_path, "same-a.json",
                   record("VIDSAME", published_at="2026-03-01T17:00:00Z"))
    write_analysis(tmp_path, "same-b.json",
                   record("VIDSAME", published_at="2026-03-01T18:00:00+01:00"))
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--check", urlopen=fail_if_network)
    assert code == 0, stdout


def test_check_rejects_naive_and_date_only(tmp_path: Path, monkeypatch) -> None:
    write_analysis(tmp_path, "naive.json",
                   record("VIDNAIVE", published_at="2026-03-01T17:00:00"))
    write_analysis(tmp_path, "dateonly.json",
                   record("VIDDATE", published_at="2026-03-01"))
    write_analysis(tmp_path, "valid.json",
                   record("VIDOK", published_at="2026-03-01T17:00:00Z"))
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--check", urlopen=fail_if_network)
    assert code == 1, stdout


def test_check_ignores_non_json_files(tmp_path: Path, monkeypatch) -> None:
    dated_corpus(tmp_path, 2)
    (tmp_path / "analysis" / "README.md").write_text("notes\n", encoding="utf-8")
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--check", urlopen=fail_if_network)
    assert code == 0, stdout


def test_check_is_offline_and_read_only(tmp_path: Path, monkeypatch) -> None:
    dated_corpus(tmp_path, 3)
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--check", urlopen=fail_if_network)
    assert code == 0, stdout
    result_json(stdout, stderr)
    assert snapshot(tmp_path) == before, "--check must be read-only"


def test_check_needs_no_key(tmp_path: Path, monkeypatch) -> None:
    dated_corpus(tmp_path, 3)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--check",
        env={KEY_NAME: None}, urlopen=fail_if_network)
    assert code == 0, stdout


# ---------------------------------------------------------------------------
# Backfill: happy path and batching
# ---------------------------------------------------------------------------

def test_backfill_writes_exact_published_at_and_preserves_fields(
    tmp_path: Path, monkeypatch
) -> None:
    vids = undated_corpus(tmp_path, 3)
    before = {name: json.loads(data) for name, data in snapshot(tmp_path).items()}

    def handler(url, _index):
        ids = requested_ids(url)
        return videos_list_payload({vid: api_date(i) for i, vid in enumerate(ids)})

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 0, stderr
    result_json(stdout, stderr)
    assert_no_leak(stdout, stderr, fake.urls)

    assert len(fake.urls) == 1, f"3 IDs must go in one batch: {fake.urls}"
    requested = assert_api_url(fake.urls[0])
    assert sorted(requested) == sorted(vids)

    for name, original in before.items():
        updated = json.loads((tmp_path / "analysis" / name).read_text(encoding="utf-8"))
        assert updated["published_at"] == api_date(vids.index(original["vid"])), name
        for field, value in original.items():
            assert updated[field] == value, f"{name}: {field} must be preserved"


def test_backfill_batches_hold_at_most_50_ids(tmp_path: Path, monkeypatch) -> None:
    vids = undated_corpus(tmp_path, 53)

    def handler(url, _index):
        ids = requested_ids(url)
        return videos_list_payload({vid: api_date(i) for i, vid in enumerate(ids)})

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 0, stderr
    assert_no_leak(stdout, stderr, fake.urls)

    batches = [assert_api_url(url) for url in fake.urls]
    assert len(batches) == 2, f"53 IDs must take 2 batches: {len(batches)}"
    assert sorted(len(b) for b in batches) == [3, 50]
    flat = [vid for batch in batches for vid in batch]
    assert len(set(flat)) == len(flat), "IDs must be deduplicated across batches"
    assert sorted(flat) == sorted(vids)

    for name in snapshot(tmp_path):
        updated = json.loads((tmp_path / "analysis" / name).read_text(encoding="utf-8"))
        assert "published_at" in updated, name


def test_backfill_preserves_existing_valid_dates_verbatim(
    tmp_path: Path, monkeypatch
) -> None:
    original_date = "2020-05-05T05:05:05+00:00"
    write_analysis(tmp_path, "old.json", record("VIDOLD", published_at=original_date))
    write_analysis(tmp_path, "new.json", record("VIDNEW"))
    before_old = (tmp_path / "analysis" / "old.json").read_bytes()

    def handler(url, _index):
        ids = requested_ids(url)
        # Even if the dated video is (re-)requested, its stored date must win.
        return videos_list_payload({vid: "2030-01-01T00:00:00Z" for vid in ids})

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 0, stderr
    for url in fake.urls:
        assert_api_url(url)
    assert_no_leak(stdout, stderr, fake.urls)
    assert (tmp_path / "analysis" / "old.json").read_bytes() == before_old
    updated_new = json.loads((tmp_path / "analysis" / "new.json").read_text(encoding="utf-8"))
    assert updated_new["published_at"] == "2030-01-01T00:00:00Z"


def test_backfill_duplicate_records_share_one_lookup(tmp_path: Path, monkeypatch) -> None:
    write_analysis(tmp_path, "dup-a.json", record("VIDDUP"))
    write_analysis(tmp_path, "dup-b.json", record("VIDDUP"))
    write_analysis(tmp_path, "other.json", record("VIDOTHER"))

    def handler(url, _index):
        ids = requested_ids(url)
        return videos_list_payload({vid: api_date(i) for i, vid in enumerate(ids)})

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 0, stderr
    flat = [vid for url in fake.urls for vid in assert_api_url(url)]
    assert len(set(flat)) == len(flat), "duplicate IDs must be requested once"
    for name in ("dup-a.json", "dup-b.json", "other.json"):
        updated = json.loads((tmp_path / "analysis" / name).read_text(encoding="utf-8"))
        assert "published_at" in updated, name


# ---------------------------------------------------------------------------
# Backfill: omitted IDs stay unresolved
# ---------------------------------------------------------------------------

def test_backfill_omitted_id_stays_unresolved(tmp_path: Path, monkeypatch) -> None:
    vids = undated_corpus(tmp_path, 20)
    omitted = vids[-1]

    def handler(url, _index):
        ids = [vid for vid in requested_ids(url) if vid != omitted]
        return videos_list_payload({vid: api_date(i) for i, vid in enumerate(ids)})

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    # 19/20 resolves to exactly 95%: success, with the omission reported.
    assert code == 0, stderr
    for url in fake.urls:
        assert_api_url(url)
    assert_no_leak(stdout, stderr, fake.urls)
    obj = result_json(stdout, stderr)
    assert json_has_string(obj, omitted), f"omitted ID must be reported: {stdout}"
    untouched = json.loads(
        (tmp_path / "analysis" / f"{omitted}.json").read_text(encoding="utf-8"))
    assert "published_at" not in untouched, "omitted ID must not gain a date"


def test_backfill_many_omitted_fails_coverage(tmp_path: Path, monkeypatch) -> None:
    vids = undated_corpus(tmp_path, 3)

    def handler(url, _index):
        ids = requested_ids(url)
        return videos_list_payload({ids[0]: api_date(0)})

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stdout
    assert_no_leak(stdout, stderr, fake.urls)
    resolved = json.loads(
        (tmp_path / "analysis" / f"{vids[0]}.json").read_text(encoding="utf-8"))
    assert resolved.get("published_at") == api_date(0)


# ---------------------------------------------------------------------------
# Backfill: invalid responses and transport failures write nothing
# ---------------------------------------------------------------------------

MALFORMED_PAYLOADS = {
    "missing_items": {"kind": "youtube#videoListResponse"},
    "null_items": {"kind": "youtube#videoListResponse", "items": None},
    "items_not_list": {"kind": "youtube#videoListResponse", "items": {}},
    "item_missing_id": {"items": [{"snippet": {"publishedAt": api_date(0)}}]},
    "unknown_id": videos_list_payload({"NOTREQUESTED": api_date(0)}),
    "date_only": videos_list_payload({"PLACEHOLDER": "2026-03-01"}),
    "naive_date": videos_list_payload({"PLACEHOLDER": "2026-03-01T17:00:00"}),
    "null_date": {"items": [{"id": "PLACEHOLDER", "snippet": {"publishedAt": None}}]},
    "missing_snippet": {"items": [{"id": "PLACEHOLDER"}]},
}


@pytest.mark.parametrize("case", sorted(MALFORMED_PAYLOADS))
def test_backfill_malformed_response_writes_nothing(
    tmp_path: Path, monkeypatch, case: str
) -> None:
    vids = undated_corpus(tmp_path, 2)
    template = json.dumps(MALFORMED_PAYLOADS[case]).replace("PLACEHOLDER", vids[0])
    payload = json.loads(template)

    def handler(url, _index):
        # Serve the malformed payload once; any batch shape is invalid here.
        requested_ids(url)
        return payload

    fake = FakeUrlopen(handler)
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 2, f"{case}: invalid response must be an API error: {stdout} {stderr}"
    assert snapshot(tmp_path) == before, f"{case}: no file may change"
    assert_no_leak(stdout, stderr, fake.urls)
    result_json(stdout, stderr)


def test_backfill_later_batch_failure_writes_nothing(
    tmp_path: Path, monkeypatch
) -> None:
    undated_corpus(tmp_path, 53)

    def handler(url, index):
        ids = requested_ids(url)
        if index == 0:
            return videos_list_payload({vid: api_date(i) for i, vid in enumerate(ids)})
        return {"kind": "youtube#videoListResponse"}  # malformed second batch

    fake = FakeUrlopen(handler)
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert len(fake.urls) == 2, "both batches must be attempted before any write"
    assert code == 2, f"{stdout} {stderr}"
    assert snapshot(tmp_path) == before, "a failed batch must void the whole run"
    assert_no_leak(stdout, stderr, fake.urls)


def test_backfill_transport_error_writes_nothing(
    tmp_path: Path, monkeypatch
) -> None:
    undated_corpus(tmp_path, 2)

    def handler(url, _index):
        raise urllib.error.URLError("simulated outage")

    fake = FakeUrlopen(handler)
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 2, f"{stdout} {stderr}"
    assert snapshot(tmp_path) == before
    assert_no_leak(stdout, stderr, fake.urls)
    result_json(stdout, stderr)


def test_backfill_http_error_is_sanitized(tmp_path: Path, monkeypatch) -> None:
    undated_corpus(tmp_path, 2)
    raw_body = "quotaExceeded-symulated-raw-detail"

    def handler(url, _index):
        raise urllib.error.HTTPError(
            url, 403, "Forbidden", {}, io.BytesIO(raw_body.encode("utf-8")))

    fake = FakeUrlopen(handler)
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 2, f"{stdout} {stderr}"
    assert snapshot(tmp_path) == before
    assert_no_leak(stdout, stderr, fake.urls)
    assert raw_body not in (stdout + stderr), "raw API error must not be printed"
    result_json(stdout, stderr)


# ---------------------------------------------------------------------------
# Backfill: credentials
# ---------------------------------------------------------------------------

def test_backfill_missing_key_names_variable_not_value(
    tmp_path: Path, monkeypatch
) -> None:
    undated_corpus(tmp_path, 2)
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: None}, urlopen=fail_if_network)
    assert code == 2, f"{stdout} {stderr}"
    assert snapshot(tmp_path) == before
    obj = result_json(stdout, stderr)
    assert json_has_substring(obj, KEY_NAME), f"remediation must name {KEY_NAME}: {stdout}"


def test_backfill_empty_key_is_rejected(tmp_path: Path, monkeypatch) -> None:
    undated_corpus(tmp_path, 2)

    def handler(url, _index):
        raise urllib.error.HTTPError(
            url, 400, "Bad Request", {}, io.BytesIO(b"keyInvalid"))

    fake = FakeUrlopen(handler)
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: ""}, urlopen=fake)
    assert code != 0, "empty key must not succeed"
    assert snapshot(tmp_path) == before
    assert_no_leak(stdout, stderr, fake.urls)
    result_json(stdout, stderr)


# ---------------------------------------------------------------------------
# --dry-run: fetch without writing
# ---------------------------------------------------------------------------

def test_dry_run_fetches_but_writes_nothing(tmp_path: Path, monkeypatch) -> None:
    undated_corpus(tmp_path, 3)

    def handler(url, _index):
        ids = requested_ids(url)
        return videos_list_payload({vid: api_date(i) for i, vid in enumerate(ids)})

    fake = FakeUrlopen(handler)
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--dry-run",
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 0, stderr
    assert fake.urls, "--dry-run must still fetch metadata"
    for url in fake.urls:
        assert_api_url(url)
    assert snapshot(tmp_path) == before, "--dry-run must never write"
    assert_no_leak(stdout, stderr, fake.urls)
    result_json(stdout, stderr)


def test_dry_run_missing_key_fails_without_network(
    tmp_path: Path, monkeypatch
) -> None:
    undated_corpus(tmp_path, 2)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--dry-run",
        env={KEY_NAME: None}, urlopen=fail_if_network)
    assert code == 2, f"{stdout} {stderr}"
    result_json(stdout, stderr)


# ---------------------------------------------------------------------------
# Input validation fails before network or writes
# ---------------------------------------------------------------------------

def test_malformed_analysis_fails_before_network(
    tmp_path: Path, monkeypatch
) -> None:
    write_analysis(tmp_path, "good.json", record("VIDGOOD"))
    (tmp_path / "analysis" / "bad.json").write_text("{not json", encoding="utf-8")
    before = snapshot(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fail_if_network)
    assert code == 2, f"{stdout} {stderr}"
    remaining = snapshot(tmp_path)
    assert remaining.get("good.json") == before.get("good.json")
    result_json(stdout, stderr)


def test_missing_vid_fails_before_network(tmp_path: Path, monkeypatch) -> None:
    payload = record("VIDGOOD")
    del payload["vid"]
    write_analysis(tmp_path, "novid.json", payload)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fail_if_network)
    assert code == 2, f"{stdout} {stderr}"
    result_json(stdout, stderr)


def test_symlinked_input_fails_before_network(
    tmp_path: Path, monkeypatch
) -> None:
    target = write_analysis(tmp_path, "real.json", record("VIDREAL"))
    (tmp_path / "analysis" / "link.json").symlink_to(target)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fail_if_network)
    assert code == 2, f"{stdout} {stderr}"
    result_json(stdout, stderr)
