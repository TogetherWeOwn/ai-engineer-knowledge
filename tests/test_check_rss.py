"""Tests for the RSS discovery check.

The checker only lists videos that have no transcript yet. It must never
fetch captions; that step needs residential egress and runs elsewhere.
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_rss.py"

FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns:yt="http://www.youtube.com/xml/schemas/2015" xmlns="http://www.w3.org/2005/Atom">
 <title>AI Engineer</title>
 <entry>
  <id>yt:video:NEWVIDEO1</id>
  <yt:videoId>NEWVIDEO1</yt:videoId>
  <title>New talk</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=NEWVIDEO1"/>
  <published>2026-10-26T09:00:23+00:00</published>
 </entry>
 <entry>
  <id>yt:video:OLDVIDEO1</id>
  <yt:videoId>OLDVIDEO1</yt:videoId>
  <title>Old talk</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=OLDVIDEO1"/>
  <published>2025-01-10T17:00:00+00:00</published>
 </entry>
</feed>
"""


def run_checker(root: Path) -> subprocess.CompletedProcess:
    feed = root / "feed.xml"
    feed.write_text(FEED, encoding="utf-8")
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--feed-file",
            str(feed),
            "--transcripts-dir",
            str(root / "transcripts"),
            "--out",
            str(root / "state" / "missing_transcripts.json"),
        ],
        capture_output=True,
        text=True,
    )


def test_lists_only_videos_without_transcripts(tmp_path: Path) -> None:
    (tmp_path / "transcripts").mkdir()
    (tmp_path / "transcripts" / "OLDVIDEO1.txt").write_text("captions", encoding="utf-8")

    result = run_checker(tmp_path)
    assert result.returncode == 0, result.stderr

    missing = json.loads(
        (tmp_path / "state" / "missing_transcripts.json").read_text(encoding="utf-8")
    )
    assert [m["video_id"] for m in missing] == ["NEWVIDEO1"]
    assert missing[0]["video_url"] == "https://www.youtube.com/watch?v=NEWVIDEO1"
    assert missing[0]["published"] == "2026-10-26"
    assert missing[0]["title"] == "New talk"


def test_empty_when_all_transcripts_present(tmp_path: Path) -> None:
    (tmp_path / "transcripts").mkdir()
    for video_id in ("NEWVIDEO1", "OLDVIDEO1"):
        (tmp_path / "transcripts" / f"{video_id}.txt").write_text("x", encoding="utf-8")

    result = run_checker(tmp_path)
    assert result.returncode == 0, result.stderr
    missing = json.loads(
        (tmp_path / "state" / "missing_transcripts.json").read_text(encoding="utf-8")
    )
    assert missing == []
