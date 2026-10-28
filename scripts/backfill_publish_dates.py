#!/usr/bin/env python3
"""Backfill analysis published_at from YouTube Data API v3 videos.list.

Reads analysis/*.json using the corpus's vid field. Existing aware timestamps
and all other analysis fields are preserved. --check is offline/read-only;
--dry-run fetches metadata but does not write. JSON output never contains keys,
request URLs, API error bodies or raw exception messages. Standard library only.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from http.client import HTTPException
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ENDPOINT = "https://www.googleapis.com/youtube/v3/videos"
BATCH_SIZE = 50
MAX_RESPONSE_BYTES = 4 * 1024 * 1024
VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{1,64}")


class BackfillError(Exception):
    def __init__(self, code: str, next_action: str, retryable: bool = False):
        self.code = code
        self.next_action = next_action
        self.retryable = retryable


def timestamp(value: object) -> str | None:
    """Accept full timezone-aware ISO datetimes, never date-only values."""
    if not isinstance(value, str) or "T" not in value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            return None
        return parsed.astimezone(timezone.utc).isoformat()
    except (ValueError, OverflowError):
        return None


def load_analyses(root: Path) -> list[tuple[Path, dict, bytes]]:
    directory = root / "analysis"
    if directory.is_symlink():
        raise BackfillError("unsafe_analysis_path", "Use a real analysis directory, not a symlink.")
    records = []
    for path in sorted(directory.glob("*.json")):
        if path.is_symlink():
            raise BackfillError("unsafe_analysis_path", "Remove symlinked analysis inputs.")
        try:
            original = path.read_bytes()
            payload = json.loads(original)
        except (OSError, ValueError, UnicodeError):
            raise BackfillError("invalid_analysis", "Repair unreadable or malformed analysis JSON before retrying.") from None
        if not isinstance(payload, dict) or not isinstance(payload.get("vid"), str) or not VIDEO_ID.fullmatch(payload["vid"]):
            raise BackfillError("invalid_analysis", "Every analysis must be an object with a safe string vid; adapt legacy inputs explicitly.")
        records.append((path, payload, original))
    return records


def report(records: list[tuple[Path, dict, bytes]], dates: dict[str, str] | None = None) -> dict:
    # A video counts as covered only when every record for that ID has a date.
    by_video: dict[str, bool] = {}
    values: dict[str, set[str]] = {}
    dates = dates or {}
    for _, payload, _ in records:
        vid = payload["vid"]
        # Fetched dates are raw API strings; normalize for comparison so that
        # equivalent instants with different UTC offsets do not conflict.
        published = timestamp(payload.get("published_at")) or timestamp(dates.get(vid))
        by_video[vid] = by_video.get(vid, True) and published is not None
        if published is not None:
            values.setdefault(vid, set()).add(published)
    conflicts = sorted(vid for vid, seen in values.items() if len(seen) > 1)
    total = len(by_video)
    known = sum(by_video.values())
    passes = total > 0 and known * 100 >= total * 95 and not conflicts
    return {
        "schema": "publish-date-backfill.v1",
        "status": "ok" if passes else "incomplete",
        "analysis_files": len(records),
        "videos": total,
        "dated_videos": known,
        "coverage": known / total if total else 0,
        "required_coverage": 0.95,
        "unresolved_ids": sorted(vid for vid, dated in by_video.items() if not dated),
        "conflicting_ids": conflicts,
    }


def fetch_dates(ids: list[str], key: str) -> dict[str, str]:
    """Validate all batches before returning any data eligible for persistence.

    Returned values are the exact API publishedAt strings; callers normalize
    only for coverage/conflict comparison, never for storage."""
    dates = {}
    for start in range(0, len(ids), BATCH_SIZE):
        batch = ids[start : start + BATCH_SIZE]
        query = urlencode({"part": "snippet", "id": ",".join(batch), "key": key,
                           "fields": "items(id,snippet(publishedAt))"})
        request = Request(ENDPOINT + "?" + query, headers={"Accept": "application/json"})
        try:
            with urlopen(request, timeout=30) as response:
                raw = response.read(MAX_RESPONSE_BYTES + 1)
            if len(raw) > MAX_RESPONSE_BYTES:
                raise BackfillError("invalid_api_response", "Inspect the metadata response size; no files were changed.")
            payload = json.loads(raw)
        except HTTPError as exc:
            # HTTPError includes the key-bearing URL: never serialize it.
            raise BackfillError("youtube_http_error", "Check the repo secret, API enablement and quota; retry with the same authorized key only.", exc.code == 429 or exc.code >= 500) from None
        except (URLError, TimeoutError, OSError, HTTPException):
            raise BackfillError("youtube_transport_error", "Check network access to YouTube Data API; no files were changed.", True) from None
        except (ValueError, UnicodeError):
            raise BackfillError("invalid_api_response", "Inspect the metadata response format; no files were changed.") from None
        if not isinstance(payload, dict) or not isinstance(payload.get("items"), list) or "error" in payload:
            raise BackfillError("invalid_api_response", "Expected a videos.list items array; no files were changed.")
        seen = set()
        for item in payload["items"]:
            if not isinstance(item, dict):
                raise BackfillError("invalid_api_response", "Expected video metadata objects; no files were changed.")
            vid = item.get("id")
            if not isinstance(vid, str) or vid not in batch or vid in seen:
                raise BackfillError("invalid_api_response", "Unexpected or duplicate response video ID; no files were changed.")
            seen.add(vid)
            snippet = item.get("snippet")
            raw = snippet.get("publishedAt") if isinstance(snippet, dict) else None
            if timestamp(raw) is None:
                raise BackfillError("invalid_api_response", "Expected an aware snippet.publishedAt timestamp; no files were changed.")
            assert isinstance(raw, str)
            dates[vid] = raw
        # Omitted IDs may be private/deleted. Leave them unresolved, never guess.
    return dates


def persist(records: list[tuple[Path, dict, bytes]], dates: dict[str, str]) -> int:
    changes = []
    for path, payload, original in records:
        if timestamp(payload.get("published_at")) is None and payload["vid"] in dates:
            updated = dict(payload, published_at=dates[payload["vid"]])
            changes.append((path, original, (json.dumps(updated, indent=2, ensure_ascii=False) + "\n").encode()))
    staged = []
    try:
        # Check for concurrent writes and stage everything before replacing files.
        for path, original, content in changes:
            if path.is_symlink() or path.read_bytes() != original:
                raise BackfillError("analysis_changed", "Another writer changed the corpus; retry from a fresh snapshot.")
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".published-at-", delete=False) as f:
                temp = Path(f.name)
                staged.append((temp, path, original))
                f.write(content)
                os.fchmod(f.fileno(), path.stat().st_mode & 0o777)
                f.flush()
                os.fsync(f.fileno())
        for _, path, original in staged:
            if path.is_symlink() or path.read_bytes() != original:
                raise BackfillError("analysis_changed", "Another writer changed the corpus; retry from a fresh snapshot.")
        for temp, path, _ in staged:
            temp.replace(path)
    except OSError:
        raise BackfillError("write_failed", "Inspect filesystem permissions and rerun coverage; replacement is atomic per file, not across the corpus.") from None
    finally:
        for temp, _, _ in staged:
            temp.unlink(missing_ok=True)
    return len(changes)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true", help="offline coverage check; exit 1 below 95%% or on empty corpus")
    modes.add_argument("--dry-run", action="store_true", help="fetch metadata and report projected coverage without writing")
    args = parser.parse_args(argv)
    try:
        records = load_analyses(args.root)
        before = report(records)
        dates: dict[str, str] = {}
        if not args.check and before["unresolved_ids"]:
            key = os.environ.get("YOUTUBE_API_KEY", "").strip()
            if not key:
                raise BackfillError("missing_api_key", "Set the repo-scoped YOUTUBE_API_KEY through the approved secret channel; never paste it into logs or cards.")
            dates = fetch_dates(before["unresolved_ids"], key)
        conflicts = report(records, dates)["conflicting_ids"]
        # Do not introduce an API date that conflicts with retained metadata.
        dates = {vid: value for vid, value in dates.items() if vid not in conflicts}
        result = report(records, dates)
        result["conflicting_ids"] = conflicts
        if conflicts:
            result["status"] = "incomplete"
        updates = sum(timestamp(p.get("published_at")) is None and p["vid"] in dates for _, p, _ in records)
        written = persist(records, dates) if not args.check and not args.dry_run else 0
        result.update(mode="check" if args.check else "dry_run" if args.dry_run else "write", updated_files=written, proposed_updates=updates)
        if result["status"] != "ok":
            result.update(code="conflicting_publish_dates" if result["conflicting_ids"] else "insufficient_publish_dates", retryable=False,
                          next_action="Backfill missing public videos and resolve conflicting dates using source provenance; never guess. Empty corpus cannot pass.")
        print(json.dumps(result, sort_keys=True))
        return 0 if result["status"] == "ok" else 1
    except BackfillError as exc:
        print(json.dumps({"schema":"publish-date-backfill.v1", "status":"error", "code":exc.code,
                          "retryable":exc.retryable, "next_action":exc.next_action}, sort_keys=True))
        return 2


if __name__ == "__main__":
    sys.exit(main())
