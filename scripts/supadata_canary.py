#!/usr/bin/env python3
"""Five-video Supadata canary gate for verbatim caption ingestion.

Compares Supadata mode=native&lang=en captions fetched from a GitHub-hosted
runner against the conforming reference transcripts/*.txt files. Every video
must fetch with HTTP 200 (a 206 or any other status/shape fails that video)
and reach >= 0.98 word similarity. A passing canary authorizes bulk caption
retrieval; anything else keeps it disabled. JSON output never contains keys,
request URLs, captions or raw API bodies. Standard library only.
"""
from __future__ import annotations

import argparse
from datetime import datetime
from difflib import SequenceMatcher
import hashlib
from http.client import HTTPException
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener

ENDPOINT = "https://api.supadata.ai/v1/youtube/transcript"
KEY_NAME = "SUPADATA_API_KEY"
CANARY_SIZE = 5
GATE = 0.98
MAX_RESPONSE_BYTES = 4 * 1024 * 1024
VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{1,64}")
WATCH_PREFIX = "https://www.youtube.com/watch?v="
UNVERIFIED_LABEL = "auto/author captions, unverified"
MACHINE_LABEL = "machine transcript (Whisper; no YouTube captions)"
TIMESTAMP_TOKEN = re.compile(r"^\[?\(?<?\d{1,2}:\d{2}(:\d{2})?([.,]\d+)?\]?\)?>?$")
ARROW_TOKEN = re.compile(r"^-->$")
NORMALIZATION = (
    "drop #-header lines; drop timestamp/--> tokens; lowercase; "
    "strip punctuation; split on whitespace"
)


class NoRedirect(HTTPRedirectHandler):
    """Never forward the authenticated request, even to another HTTPS host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class CanaryError(Exception):
    def __init__(self, code: str, next_action: str):
        self.code = code
        self.next_action = next_action


def split_reference(text: str) -> tuple[list[str], str]:
    """Split transcript text into (header_lines, body_text)."""
    lines = text.split("\n")
    index = 0
    while index < len(lines) and lines[index].startswith("#"):
        index += 1
    return lines[:index], "\n".join(lines[index:])


def reference_problems(path: Path, vid: str, text: str) -> tuple[list[str], str]:
    """Mirror the transcript conformance contract; return (problems, body)."""
    problems = []
    header_lines, body = split_reference(text)
    header = "\n".join(header_lines)
    fields = []
    for line in header_lines:
        key, separator, _ = line[1:].strip().partition(":")
        if separator:
            fields.append(key.strip())
    if len(fields) != len(set(fields)):
        problems.append("header fields must not be duplicated")
    source = re.search(r"^#\s*source:\s*(\S+)\s*$", header, re.M)
    if not source:
        problems.append("header lacks a 'source:' line")
    else:
        url = source.group(1)
        if not url.startswith(WATCH_PREFIX):
            problems.append("source is not a watch URL")
        elif url[len(WATCH_PREFIX):] != vid:
            problems.append("source video does not match filename")
    if not re.search(r"^#\s*(?:speaker|channel):\s*(\S.*)$", header, re.M):
        problems.append("header lacks speaker/channel credit")
    retrieved = re.search(r"^#\s*retrieved_at:\s*(\S+)\s*$", header, re.M)
    if not retrieved:
        problems.append("header lacks 'retrieved_at:'")
    else:
        stamp = retrieved.group(1).strip()
        try:
            parsed = datetime.fromisoformat(stamp[:-1] + "+00:00" if stamp.endswith("Z") else stamp)
            if parsed.tzinfo is None:
                raise ValueError("naive")
        except ValueError:
            problems.append("retrieved_at is not an aware ISO datetime")
    digest = re.search(r"^#\s*sha256:\s*([0-9a-fA-F]+)\s*$", header, re.M)
    if not digest:
        problems.append("header lacks 'sha256:'")
    elif len(digest.group(1)) != 64:
        problems.append("sha256 is not a 64-character hex digest")
    elif digest.group(1).lower() != hashlib.sha256(body.encode("utf-8")).hexdigest():
        problems.append("sha256 does not match the caption body")
    comments = [line[1:].strip() for line in header_lines]
    if (comments.count(UNVERIFIED_LABEL) != 1
            or any(comment.casefold().startswith("machine transcript") for comment in comments)):
        problems.append("canary reference requires exactly one caption label and no machine marker")
    if not body.strip():
        problems.append("caption body is empty")
    _ = path
    return problems, body


def normalize_words(body: str) -> list[str]:
    words = []
    for token in body.split():
        if TIMESTAMP_TOKEN.match(token) or ARROW_TOKEN.match(token):
            continue
        cleaned = re.sub(r"[^\w\s]", "", token.lower(), flags=re.UNICODE)
        if cleaned:
            words.append(cleaned)
    return words


def word_similarity(reference: list[str], fetched: list[str]) -> float:
    if not reference or not fetched:
        return 0.0
    return SequenceMatcher(None, reference, fetched, autojunk=False).ratio()


def fetch_caption(vid: str, key: str) -> tuple[int | None, str | None, str]:
    """Fetch one native caption. Returns (http_status, content, detail)."""
    query = urlencode({"videoId": vid, "lang": "en", "mode": "native", "text": "true"})
    request = Request(ENDPOINT + "?" + query,
                      headers={"x-api-key": key, "Accept": "application/json"})
    try:
        with build_opener(NoRedirect()).open(request, timeout=30) as response:
            status = getattr(response, "status", 200)
            raw = response.read(MAX_RESPONSE_BYTES + 1)
    except HTTPError as exc:
        return exc.code, None, "caption_http_error"
    except (URLError, TimeoutError, OSError, HTTPException):
        raise CanaryError("supadata_transport_error",
                          "Check runner network access to the Supadata API; no gate result was recorded.") from None
    if status != 200:
        # Partial (206), async (202) or any other status is not a native caption.
        return status, None, "unexpected_http_status"
    if len(raw) > MAX_RESPONSE_BYTES:
        return status, None, "response_too_large"
    try:
        payload = json.loads(raw)
    except (ValueError, UnicodeError):
        return status, None, "invalid_response_shape"
    content = payload.get("content") if isinstance(payload, dict) else None
    if not isinstance(content, str) or not content.strip():
        return status, None, "invalid_response_shape"
    return status, content, "ok"


def evaluate(root: Path, vids: list[str], key: str) -> dict:
    directory = root / "transcripts"
    if directory.is_symlink():
        raise CanaryError("unsafe_transcripts_path",
                          "Use a real transcripts directory, not a symlink.")
    entries = []
    for vid in vids:
        entry: dict = {"vid": vid, "reference_ok": False, "fetch_ok": False,
                       "http_status": None, "words_ref": None, "words_got": None,
                       "similarity": None, "pass": False, "detail": "invalid_reference"}
        path = directory / f"{vid}.txt"
        if path.is_symlink():
            entries.append(entry)
            continue
        try:
            text = path.read_bytes().decode("utf-8")
        except (OSError, UnicodeDecodeError):
            entries.append(entry)
            continue
        problems, body = reference_problems(path, vid, text)
        if problems:
            entries.append(entry)
            continue
        ref_words = normalize_words(body)
        if not ref_words:
            entries.append(entry)
            continue
        entry["reference_ok"] = True
        entry["words_ref"] = len(ref_words)
        status, content, detail = fetch_caption(vid, key)
        entry["http_status"] = status
        if content is None:
            entry["detail"] = detail
            entries.append(entry)
            continue
        got_words = normalize_words(content)
        score = word_similarity(ref_words, got_words)
        entry.update(fetch_ok=True, words_got=len(got_words),
                     similarity=round(score, 4),
                     detail="below_gate" if score < GATE else "ok")
        entry["pass"] = score >= GATE
        entries.append(entry)
    failures = sorted(entry["vid"] for entry in entries if not entry["pass"])
    return {
        "schema": "supadata-canary.v1",
        "metric": "word_sequence_ratio.v1",
        "normalization": NORMALIZATION,
        "gate": GATE,
        "required_http_status": 200,
        "videos": entries,
        "overall": "pass" if not failures else "fail",
        "failures": failures,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--vids", required=True, help="comma-separated video IDs (exactly 5)")
    parser.add_argument("--out", type=Path, default=None, help="write the JSON report to this file too")
    args = parser.parse_args(argv)
    try:
        vids = [item.strip() for item in args.vids.split(",") if item.strip()]
        if len(vids) != CANARY_SIZE or len(set(vids)) != CANARY_SIZE:
            raise CanaryError("invalid_canary_set",
                              f"Provide exactly {CANARY_SIZE} distinct video IDs.")
        for vid in vids:
            if not VIDEO_ID.fullmatch(vid):
                raise CanaryError("invalid_canary_set", "Video IDs must match [A-Za-z0-9_-]{1,64}.")
        key = os.environ.get(KEY_NAME, "").strip()
        if not key:
            raise CanaryError("missing_api_key",
                              "Set the repo-scoped SUPADATA_API_KEY through the approved secret channel; never paste it into logs or cards.")
        report = evaluate(args.root, vids, key)
        if args.out is not None:
            try:
                args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            except OSError:
                raise CanaryError("report_write_failed",
                                  "Inspect the --out path permissions; the gate result was not recorded.") from None
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0 if report["overall"] == "pass" else 1
    except CanaryError as exc:
        report = {"schema": "supadata-canary.v1", "status": "error",
                  "code": exc.code, "next_action": exc.next_action}
        if args.out is not None and exc.code != "report_write_failed":
            try:
                args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            except OSError:
                report = {"schema": "supadata-canary.v1", "status": "error",
                          "code": "report_write_failed",
                          "next_action": "Inspect the --out path permissions; the gate result was not recorded."}
        print(json.dumps(report, sort_keys=True))
        return 2


if __name__ == "__main__":
    sys.exit(main())
