"""Implementation unit tests for the Supadata canary (not Test Author acceptance).

Contract under test (from the owner gates, not from any implementation):

- CLI: ``scripts/supadata_canary.py --root PATH --vids V1,..,V5 [--out PATH]``
- Exactly 5 distinct video IDs. Each must have a conforming reference
  ``transcripts/<vid>.txt`` (D1 header rules mirrored from the transcript
  conformance contract: watch-URL source matching the filename, speaker or
  channel credit, aware ``retrieved_at``, body-matching ``sha256``, the
  unverified label, non-empty body).
- Fetch per video is ``GET /v1/youtube/transcript`` with
  ``videoId``/``lang=en``/``mode=native``/``text=true`` and the repo-scoped
  ``SUPADATA_API_KEY`` in the ``x-api-key`` header. Only HTTP 200 with a JSON
  string ``content`` counts; 206 or any other status/shape fails that video.
- Word similarity is the SequenceMatcher ratio over normalized word sequences
  (header lines dropped, timestamp tokens dropped, lowercase, punctuation
  stripped). Gate: every video >= 0.98.
- Exits: 0 means all 5 pass, 1 means the gate fails, 2 means a usage/key/
  transport error. No secret value, request URL or response body is printed.

Network behavior is exercised in-process with a stubbed ``urlopen``; no test
uses a real key or touches the network.
"""

import hashlib
import io
import json
import re
import runpy
import sys
import urllib.error
import urllib.request
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "supadata_canary.py"

API_HOST = "api.supadata.ai"
API_PATH = "/v1/youtube/transcript"
KEY_NAME = "SUPADATA_API_KEY"
SENTINEL_KEY = "TESTONLY_FAKE_SUPADATA_7c3b9a1e5f"

WATCH_PREFIX = "https://www.youtube.com/watch?v="
UNVERIFIED_LABEL = "auto/author captions, unverified"

BODY_WORDS = (
    "hello world this is a test of the caption comparison system "
    "with enough words to make similarity meaningful across segments"
)


# ---------------------------------------------------------------------------
# Fixture builders
# ---------------------------------------------------------------------------

def transcript_text(vid, body=None, retrieved_at="2026-10-26T12:00:00Z",
                    speaker="Jane Doe", digest=None):
    body = BODY_WORDS if body is None else body
    header = [
        f"# source: {WATCH_PREFIX}{vid}",
        f"# speaker: {speaker}",
        f"# retrieved_at: {retrieved_at}",
        "# sha256: PLACEHOLDER",
        f"# {UNVERIFIED_LABEL}",
    ]
    text = "\n".join(header) + "\n" + body
    lines = text.split("\n")
    index = 0
    while index < len(lines) and lines[index].startswith("#"):
        index += 1
    actual = digest or hashlib.sha256("\n".join(lines[index:]).encode("utf-8")).hexdigest()
    return text.replace("PLACEHOLDER", actual)


def write_transcript(root: Path, vid: str, text: str) -> Path:
    directory = root / "transcripts"
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{vid}.txt"
    path.write_text(text, encoding="utf-8")
    return path


def five_vids():
    return [f"VIDCAN{i:02d}" for i in range(1, 6)]


def corpus(root: Path, vids=None, body=None):
    vids = five_vids() if vids is None else vids
    for vid in vids:
        write_transcript(root, vid, transcript_text(vid, body=body))
    return vids


class FakeResponse:
    def __init__(self, status=200, payload=b"{}"):
        self.status = status
        self._payload = payload

    def read(self, size=-1):
        data = self._payload if size is None or size < 0 else self._payload[:size]
        self._payload = self._payload[len(data):]
        return data

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class FakeUrlopen:
    """Stub for urllib.request.urlopen recording requests."""

    def __init__(self, handler):
        self._handler = handler
        self.calls = []

    def __call__(self, request, timeout=None):
        url = request.full_url if hasattr(request, "full_url") else request
        self.calls.append({
            "url": url,
            "key": request.get_header("X-api-key") if hasattr(request, "get_header") else None,
        })
        return self._handler(url, len(self.calls) - 1)


def transcript_payload(content):
    return json.dumps({"content": content, "lang": "en",
                       "availableLangs": ["en"]}).encode("utf-8")


def run_cli(monkeypatch, *argv, env=None, urlopen=None):
    if env:
        for name, value in env.items():
            if value is None:
                monkeypatch.delenv(name, raising=False)
            else:
                monkeypatch.setenv(name, value)
    if urlopen is not None:
        # The dedicated opener disables redirects. Stub only its transport seam;
        # redirect-handler behavior has a separate offline HTTP-handler test.
        monkeypatch.setattr(urllib.request.OpenerDirector, "open",
                            lambda self, request, timeout=None: urlopen(request, timeout=timeout))
    monkeypatch.setattr(sys, "argv", ["supadata_canary.py", *argv])
    stdout, stderr = io.StringIO(), io.StringIO()
    try:
        with redirect_stdout(stdout), redirect_stderr(stderr):
            runpy.run_path(str(SCRIPT), run_name="__main__")
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else 1
    else:
        code = 0
    return code, stdout.getvalue(), stderr.getvalue()


def result_json(stdout, stderr):
    try:
        return json.loads(stdout)
    except ValueError:
        pytest.fail(f"stdout is not JSON: {stdout!r} / {stderr!r}")


def assert_no_leak(stdout, stderr, calls):
    blob = stdout + stderr
    assert SENTINEL_KEY not in blob, "key material leaked into output"
    for call in calls:
        assert call["url"] not in blob, "request URL leaked into output"
        assert "x-api-key" not in blob.lower(), "auth header name leaked"


def assert_api_call(call):
    parsed = urlparse(call["url"])
    assert parsed.scheme == "https", call["url"]
    assert parsed.hostname == API_HOST, call["url"]
    assert parsed.path == API_PATH, call["url"]
    query = parse_qs(parsed.query)
    assert query.get("lang") == ["en"], call["url"]
    assert query.get("mode") == ["native"], call["url"]
    assert query.get("text") == ["true"], call["url"]
    assert len(query.get("videoId", [])) == 1, call["url"]
    assert call["key"] == SENTINEL_KEY, "key must travel in the x-api-key header"
    return query["videoId"][0]


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------

def test_all_five_pass_reports_scores_and_metric(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)

    def handler(url, _index):
        return FakeResponse(200, transcript_payload(BODY_WORDS))

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 0, stderr
    report = result_json(stdout, stderr)
    assert_no_leak(stdout, stderr, fake.calls)

    assert report["schema"] == "supadata-canary.v1"
    assert report["metric"] == "word_sequence_ratio.v1"
    assert report["gate"] == 0.98
    assert report["required_http_status"] == 200
    assert "normalization" in report and report["normalization"]
    assert report["overall"] == "pass"
    assert report["failures"] == []

    assert len(fake.calls) == 5
    seen = [assert_api_call(call) for call in fake.calls]
    assert sorted(seen) == sorted(vids)

    assert len(report["videos"]) == 5
    for entry in report["videos"]:
        assert entry["fetch_ok"] is True, entry
        assert entry["http_status"] == 200, entry
        assert entry["words_ref"] > 0 and entry["words_got"] > 0, entry
        assert entry["similarity"] >= 0.98, entry
        assert entry["pass"] is True, entry


def test_timestamps_and_header_ignored_by_metric(tmp_path: Path, monkeypatch) -> None:
    body = ("00:00:01.000 --> 00:00:03.500\n" + BODY_WORDS + "\n"
            "[00:00:04.000] " + BODY_WORDS)
    vids = corpus(tmp_path, body=body)

    def handler(url, _index):
        return FakeResponse(200, transcript_payload(BODY_WORDS + " " + BODY_WORDS))

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 0, stderr
    report = result_json(stdout, stderr)
    for entry in report["videos"]:
        assert entry["similarity"] == 1.0, entry


def test_report_written_to_out_file(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)

    def handler(url, _index):
        return FakeResponse(200, transcript_payload(BODY_WORDS))

    fake = FakeUrlopen(handler)
    out = tmp_path / "canary-report.json"
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        "--out", str(out), env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 0, stderr
    assert json.loads(out.read_text(encoding="utf-8")) == result_json(stdout, stderr)


# ---------------------------------------------------------------------------
# Gate failures (exit 1)
# ---------------------------------------------------------------------------

def test_below_gate_similarity_fails(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)

    def handler(url, _index):
        parsed = urlparse(url)
        vid = parse_qs(parsed.query)["videoId"][0]
        if vid == vids[0]:
            return FakeResponse(200, transcript_payload(
                "completely unrelated vocabulary about cooking recipes and garden tools"))
        return FakeResponse(200, transcript_payload(BODY_WORDS))

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    report = result_json(stdout, stderr)
    assert_no_leak(stdout, stderr, fake.calls)
    assert report["overall"] == "fail"
    assert report["failures"] == [vids[0]]
    entry = next(v for v in report["videos"] if v["vid"] == vids[0])
    assert entry["fetch_ok"] is True
    assert entry["similarity"] < 0.98
    assert entry["pass"] is False


def test_206_partial_content_fails(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)

    def handler(url, _index):
        return FakeResponse(206, transcript_payload(BODY_WORDS))

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    report = result_json(stdout, stderr)
    assert report["overall"] == "fail"
    assert sorted(report["failures"]) == sorted(vids)
    for entry in report["videos"]:
        assert entry["fetch_ok"] is False, entry
        assert entry["http_status"] == 206, entry
        assert entry["similarity"] is None, entry
        assert entry["pass"] is False, entry


def test_http_error_status_fails_video(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)

    def handler(url, _index):
        raise urllib.error.HTTPError(url, 500, "Internal Error", {}, None)

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    report = result_json(stdout, stderr)
    assert report["overall"] == "fail"
    for entry in report["videos"]:
        assert entry["fetch_ok"] is False, entry
        assert entry["http_status"] == 500, entry


def test_async_202_fails_video(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)

    def handler(url, _index):
        return FakeResponse(202, b'{"jobId": "job-1", "status": "processing"}')

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    report = result_json(stdout, stderr)
    assert report["overall"] == "fail"
    for entry in report["videos"]:
        assert entry["fetch_ok"] is False, entry
        assert entry["http_status"] == 202, entry


def test_chunk_content_shape_fails_video(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)

    def handler(url, _index):
        return FakeResponse(200, json.dumps(
            {"content": [{"text": "hi", "offset": 0}], "lang": "en"}).encode())

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    report = result_json(stdout, stderr)
    assert report["overall"] == "fail"
    for entry in report["videos"]:
        assert entry["fetch_ok"] is False, entry
        assert entry["http_status"] == 200, entry


def test_malformed_json_fails_video(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)

    def handler(url, _index):
        return FakeResponse(200, b"not json{")

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    report = result_json(stdout, stderr)
    assert report["overall"] == "fail"


def test_missing_reference_fails_gate(tmp_path: Path, monkeypatch) -> None:
    vids = five_vids()
    corpus(tmp_path, vids=vids[:4])

    def handler(url, _index):
        return FakeResponse(200, transcript_payload(BODY_WORDS))

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    report = result_json(stdout, stderr)
    assert report["failures"] == [vids[4]]
    entry = next(v for v in report["videos"] if v["vid"] == vids[4])
    assert entry["reference_ok"] is False
    assert entry["pass"] is False


def test_tampered_reference_fails_gate(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)
    target = tmp_path / "transcripts" / f"{vids[2]}.txt"
    target.write_text(target.read_text(encoding="utf-8") + "\ninjected line",
                      encoding="utf-8")

    def handler(url, _index):
        return FakeResponse(200, transcript_payload(BODY_WORDS))

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    report = result_json(stdout, stderr)
    assert report["failures"] == [vids[2]]


# ---------------------------------------------------------------------------
# Usage errors (exit 2)
# ---------------------------------------------------------------------------

def test_missing_key_is_usage_error(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: None}, urlopen=FakeUrlopen(lambda u, i: None))
    assert code == 2, stderr
    payload = result_json(stdout, stderr)
    assert payload["status"] == "error"
    assert KEY_NAME in payload["next_action"]
    assert SENTINEL_KEY not in stdout + stderr


def test_transport_error_is_usage_error(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)

    def handler(url, _index):
        raise urllib.error.URLError("network down")

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 2, stderr
    payload = result_json(stdout, stderr)
    assert payload["status"] == "error"
    assert_no_leak(stdout, stderr, fake.calls)


@pytest.mark.parametrize("count", [1, 4, 6])
def test_vid_count_must_be_exactly_five(tmp_path: Path, monkeypatch, count: int) -> None:
    corpus(tmp_path)
    vids = ",".join(five_vids()[:count] if count <= 5 else five_vids() + ["VIDEXTRA"])
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", vids,
        env={KEY_NAME: SENTINEL_KEY},
        urlopen=FakeUrlopen(lambda u, i: FakeResponse(200, b"{}")))
    assert code == 2, stderr
    assert result_json(stdout, stderr)["status"] == "error"


def test_duplicate_vids_rejected(tmp_path: Path, monkeypatch) -> None:
    corpus(tmp_path)
    vids = five_vids()
    vids[4] = vids[0]
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY},
        urlopen=FakeUrlopen(lambda u, i: FakeResponse(200, b"{}")))
    assert code == 2, stderr


def test_symlinked_reference_fails_gate(tmp_path: Path, monkeypatch) -> None:
    vids = corpus(tmp_path)
    target = tmp_path / "transcripts" / f"{vids[1]}.txt"
    real = tmp_path / "real.txt"
    real.write_text(target.read_text(encoding="utf-8"), encoding="utf-8")
    target.unlink()
    target.symlink_to(real)

    def handler(url, _index):
        return FakeResponse(200, transcript_payload(BODY_WORDS))

    fake = FakeUrlopen(handler)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    assert result_json(stdout, stderr)["failures"] == [vids[1]]


def test_symlinked_transcripts_dir_is_usage_error(tmp_path: Path, monkeypatch) -> None:
    vids = five_vids()
    real = tmp_path / "real-transcripts"
    corpus(tmp_path, vids=vids)
    (tmp_path / "transcripts").rename(real)
    (tmp_path / "transcripts").symlink_to(real, target_is_directory=True)
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY},
        urlopen=FakeUrlopen(lambda u, i: FakeResponse(200, b"{}")))
    assert code == 2, stderr
    assert result_json(stdout, stderr)["status"] == "error"


def test_unsafe_vid_rejected(tmp_path: Path, monkeypatch) -> None:
    corpus(tmp_path)
    vids = five_vids()
    vids[0] = "../evil"
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY},
        urlopen=FakeUrlopen(lambda u, i: FakeResponse(200, b"{}")))
    assert code == 2, stderr


@pytest.mark.parametrize("labels", [
    ["machine transcript (Whisper; no YouTube captions)"],
    [UNVERIFIED_LABEL, "machine transcript (Whisper; no YouTube captions)"],
    [UNVERIFIED_LABEL, "  machine transcript (Whisper; no YouTube captions)  "],
    [UNVERIFIED_LABEL, UNVERIFIED_LABEL],
    ["not " + UNVERIFIED_LABEL],
])
def test_only_one_exact_caption_label_is_a_canary_reference(tmp_path, monkeypatch, labels):
    """Machine or ambiguous provenance cannot authorize native-caption ingestion."""
    vids = corpus(tmp_path)
    path = tmp_path / "transcripts" / f"{vids[0]}.txt"
    text = path.read_text().replace(
        f"# {UNVERIFIED_LABEL}", "\n".join(f"# {label}" for label in labels))
    path.write_text(text)
    fake = FakeUrlopen(lambda _url, _index: FakeResponse(200, transcript_payload(BODY_WORDS)))
    code, stdout, stderr = run_cli(
        monkeypatch, "--root", str(tmp_path), "--vids", ",".join(vids),
        env={KEY_NAME: SENTINEL_KEY}, urlopen=fake)
    assert code == 1, stderr
    report = result_json(stdout, stderr)
    assert report["overall"] == "fail"
    assert report["failures"] == [vids[0]]
    entry = next(v for v in report["videos"] if v["vid"] == vids[0])
    assert entry["reference_ok"] is False
    assert entry["fetch_ok"] is False
    assert entry["detail"] == "invalid_reference"
    assert len(fake.calls) == 4, "a machine/ambiguous reference must not be fetched"
