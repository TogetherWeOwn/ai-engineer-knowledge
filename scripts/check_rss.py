#!/usr/bin/env python3
"""RSS discovery check: list channel videos that have no transcript yet.

Writes ``state/missing_transcripts.json`` with one entry per video in the
feed whose ``transcripts/<video_id>.txt`` does not exist.

This script must NEVER fetch captions. Caption hosts reject datacenter
egress, so transcripts are fetched from a residential connection and
committed to this repo; automation here only compares the public RSS feed
against what is already committed.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ATOM = "{http://www.w3.org/2005/Atom}"
YT = "{http://www.youtube.com/xml/schemas/2015}"
DEFAULT_FEED_URL = (
    "https://www.youtube.com/feeds/videos.xml?channel_id=UCLKPca3kwwd-B59HNr-_lvA"
)


def parse_feed(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    videos = []
    for entry in root.findall(f"{ATOM}entry"):
        video_id = entry.findtext(f"{YT}videoId")
        if not video_id:
            continue
        published = entry.findtext(f"{ATOM}published") or ""
        videos.append(
            {
                "video_id": video_id,
                "video_url": f"https://www.youtube.com/watch?v={video_id}",
                "title": entry.findtext(f"{ATOM}title") or "",
                "published": published[:10],
            }
        )
    return videos


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--feed-url", default=DEFAULT_FEED_URL)
    parser.add_argument("--feed-file", type=Path, help="read the feed from a file instead")
    parser.add_argument("--transcripts-dir", type=Path, default=Path("transcripts"))
    parser.add_argument(
        "--out", type=Path, default=Path("state/missing_transcripts.json")
    )
    args = parser.parse_args(argv)

    if args.feed_file:
        xml_text = args.feed_file.read_text(encoding="utf-8")
    else:
        request = urllib.request.Request(
            args.feed_url, headers={"User-Agent": "ai-engineer-knowledge/rss-check"}
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            xml_text = response.read().decode("utf-8")

    videos = parse_feed(xml_text)
    missing = [
        video
        for video in videos
        if not (args.transcripts_dir / f"{video['video_id']}.txt").exists()
    ]
    missing.sort(key=lambda v: (v["published"], v["video_id"]), reverse=True)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(missing, indent=2) + "\n", encoding="utf-8")
    print(f"{len(missing)} of {len(videos)} feed videos have no transcript yet")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
