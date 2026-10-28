#!/usr/bin/env python3
"""Deterministic, recency-aware claims generator.

Reads per-talk technique analyses from ``analysis/*.json`` (see
``docs/analysis-schema.md`` for the input contract) and generates:

- ``claims/<area>/<slug>.md`` — the active (newest) claim per technique
- ``claims/<area>/<slug>--<video_id>.md`` — superseded claims, retained
- ``areas/<area>.md`` — one index page per area
- ``catalog.json`` — every claim's frontmatter, for machines
- ``llms.txt`` — a short router for AI readers (under 100 lines)
- ``llms-full.md`` — every active claim, concatenated

Recency rules (the point of this repo):

1. Ordering is by talk publish date (``talk_date``).
2. A newer talk on the same technique supersedes the older claim: the older
   file stays, with ``status: superseded``, ``superseded_by`` pointing at the
   active claim id, and ``valid_to`` set to the newer talk's date.
3. An unknown date never supersedes a dated claim. An undated claim is
   active only when no dated claim exists for that technique.
4. Ties on the same date break deterministically by ``video_id``.
5. Nothing is ever deleted: claim files the current analyses no longer
   produce are left untouched and still listed in ``catalog.json``.

Output is byte-for-byte deterministic for a given set of inputs: no
timestamps, sorted everywhere. ``--check`` exits 1 when the committed output
is stale instead of writing.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

FRONTMATTER_KEYS = [
    "type",
    "id",
    "title",
    "area",
    "status",
    "valid_from",
    "valid_to",
    "superseded_by",
    "confidence",
    "relevance",
    "sources",
]

NOT_STATED = "_Not stated in the source analysis._"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "untitled"


def parse_date(value: object) -> str | None:
    """Normalize an ISO date/datetime to YYYY-MM-DD, or None when unknown."""
    if not isinstance(value, str) or len(value) < 10:
        return None
    try:
        return date.fromisoformat(value[:10]).isoformat()
    except ValueError:
        return None


SAFE_VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{1,64}")


def video_id_of(payload: dict) -> str | None:
    raw = payload.get("video_id")
    if isinstance(raw, str) and SAFE_VIDEO_ID.fullmatch(raw):
        return raw
    url = payload.get("video_url")
    if isinstance(url, str):
        match = re.search(r"[?&]v=([A-Za-z0-9_-]{6,})", url)
        if match:
            return match.group(1)
    return None


def number_or_none(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def load_instances(root: Path) -> list[dict]:
    """One instance per (area, slug, video) technique mention, deduplicated."""
    instances: dict[tuple[str, str, str], dict] = {}
    for path in sorted((root / "analysis").glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"warning: skipping {path.name}: {exc}", file=sys.stderr)
            continue
        if not isinstance(payload, dict):
            print(f"warning: skipping {path.name}: top level is not an object", file=sys.stderr)
            continue
        video_id = video_id_of(payload)
        if not video_id:
            print(f"warning: skipping {path.name}: no video id or URL", file=sys.stderr)
            continue
        raw_date = (
            payload.get("talk_date")
            or payload.get("published_at")
            or payload.get("publish_date")
        )
        talk_date = parse_date(raw_date)
        if raw_date and talk_date is None:
            print(
                f"warning: {path.name}: unparseable talk date; treating as undated",
                file=sys.stderr,
            )
        techniques = payload.get("techniques") or []
        if not isinstance(techniques, list):
            print(f"warning: skipping {path.name}: techniques is not a list", file=sys.stderr)
            continue
        for technique in techniques:
            if not isinstance(technique, dict):
                continue
            title = technique.get("title") or technique.get("name") or ""
            slug = slugify(str(technique.get("slug") or title))
            area = slugify(str(technique.get("area") or "general"))
            key = (area, slug, video_id)
            if key in instances:
                continue
            instances[key] = {
                "area": area,
                "slug": slug,
                "video_id": video_id,
                "title": str(title) or slug,
                "what": str(technique.get("what") or ""),
                "evidence": str(technique.get("evidence") or ""),
                "apply": str(technique.get("apply") or ""),
                "expected_effect": str(technique.get("expected_effect") or ""),
                "confidence": number_or_none(technique.get("confidence")),
                "relevance": number_or_none(technique.get("relevance")),
                "talk_date": talk_date,
                "retrieved_at": str(payload.get("retrieved_at") or ""),
                "video_url": str(
                    payload.get("video_url")
                    or f"https://www.youtube.com/watch?v={video_id}"
                ),
                "analysis_file": f"analysis/{path.name}",
            }
    return list(instances.values())


def rank_key(instance: dict) -> tuple:
    """Higher wins. Any dated claim outranks any undated one."""
    if instance["talk_date"]:
        return (1, instance["talk_date"], instance["video_id"])
    return (0, instance["retrieved_at"], instance["video_id"])


def build_claims(instances: list[dict]) -> dict[str, dict]:
    """Return {relative_path: {frontmatter, body}} for every instance."""
    groups: dict[tuple[str, str], list[dict]] = {}
    for instance in instances:
        groups.setdefault((instance["area"], instance["slug"]), []).append(instance)

    claims: dict[str, dict] = {}
    for (area, slug), members in sorted(groups.items()):
        ordered = sorted(members, key=rank_key)
        active = ordered[-1]
        for instance in ordered:
            is_active = instance is active
            claim_id = slug if is_active else f"{slug}--{instance['video_id']}"
            frontmatter = {
                "type": "technique",
                "id": claim_id,
                "title": instance["title"],
                "area": area,
                "status": "active" if is_active else "superseded",
                "valid_from": instance["talk_date"],
                "valid_to": None if is_active else active["talk_date"],
                "superseded_by": None if is_active else slug,
                "confidence": instance["confidence"],
                "relevance": instance["relevance"],
                "sources": [
                    {
                        "video_url": instance["video_url"],
                        "talk_date": instance["talk_date"],
                        "analysis_file": instance["analysis_file"],
                    }
                ],
            }
            talk_date_label = instance["talk_date"] or "unknown"
            body = (
                f"# {instance['title']}\n\n"
                f"## What\n\n{instance['what'] or NOT_STATED}\n\n"
                f"## Evidence\n\n{instance['evidence'] or NOT_STATED}\n\n"
                f"## Apply to us\n\n{instance['apply'] or NOT_STATED}\n\n"
                f"## Expected effect\n\n{instance['expected_effect'] or NOT_STATED}\n\n"
                f"## Sources\n\n"
                f"- [{instance['video_url']}]({instance['video_url']}) "
                f"(talk date: {talk_date_label}; analysis: `{instance['analysis_file']}`)\n"
            )
            claims[f"claims/{area}/{claim_id}.md"] = {
                "frontmatter": frontmatter,
                "body": body,
            }
    return claims


NON_STRING_WORDS = {"true", "false", "null", "~", "yes", "no", "on", "off"}


def parses_as_non_string(value: str) -> bool:
    if value.lower() in NON_STRING_WORDS:
        return True
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}([Tt ].*)?", value):
        return True
    try:
        float(value)
        return True
    except ValueError:
        pass
    try:
        int(value, 0)
        return True
    except ValueError:
        return False


def yaml_scalar(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, float):
        return repr(value)
    if (
        isinstance(value, str)
        and re.fullmatch(r"[A-Za-z0-9_./-]+", value)
        and not parses_as_non_string(value)
    ):
        return value
    return json.dumps(value)


def render_claim(claim: dict) -> str:
    frontmatter = claim["frontmatter"]
    lines = ["---"]
    for key in FRONTMATTER_KEYS:
        if key == "sources":
            lines.append("sources:")
            for source in frontmatter["sources"]:
                lines.append(f"  - video_url: {yaml_scalar(source['video_url'])}")
                lines.append(f"    talk_date: {yaml_scalar(source['talk_date'])}")
                lines.append(f"    analysis_file: {yaml_scalar(source['analysis_file'])}")
        else:
            lines.append(f"{key}: {yaml_scalar(frontmatter[key])}")
    lines.append("---")
    return "\n".join(lines) + "\n\n" + claim["body"]


def parse_scalar(raw: str) -> object:
    raw = raw.strip()
    if raw in ("null", "~", ""):
        return None
    if raw.startswith('"'):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return raw.strip('"')
    try:
        return float(raw)
    except ValueError:
        return raw


def parse_claim_file(text: str) -> dict | None:
    """Parse back the frontmatter subset this generator emits (for orphans)."""
    if not text.startswith("---\n") or "\n---\n" not in text:
        return None
    block, body = text[4:].split("\n---\n", 1)
    frontmatter: dict = {}
    sources: list[dict] = []
    current_source: dict | None = None
    in_sources = False
    for line in block.splitlines():
        if line == "sources:":
            in_sources = True
            continue
        if in_sources and line.startswith("  - "):
            current_source = {}
            sources.append(current_source)
            line = "    " + line[4:]
        if in_sources and line.startswith("    ") and current_source is not None:
            key, _, raw = line.strip().partition(": ")
            current_source[key] = parse_scalar(raw)
            continue
        in_sources = False
        key, _, raw = line.partition(": ")
        frontmatter[key.strip()] = parse_scalar(raw)
    if sources:
        frontmatter["sources"] = sources
    if not isinstance(frontmatter.get("id"), str) or not isinstance(
        frontmatter.get("area"), str
    ):
        return None
    ordered = {key: frontmatter.get(key) for key in FRONTMATTER_KEYS}
    return {"frontmatter": ordered, "body": body.lstrip("\n")}


def scan_existing_claims(root: Path) -> dict[str, dict]:
    found: dict[str, dict] = {}
    claims_dir = root / "claims"
    if not claims_dir.exists():
        return found
    for path in sorted(claims_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        parsed = parse_claim_file(text)
        if parsed:
            found[str(path.relative_to(root))] = parsed
        elif text.startswith("---"):
            print(
                f"warning: {path.relative_to(root)} has unusable frontmatter; "
                "kept on disk, excluded from generated indexes",
                file=sys.stderr,
            )
    return found


def build_derived(claims: dict[str, dict]) -> dict[str, str]:
    """catalog.json, areas/*.md, llms.txt, llms-full.md from the claim set."""
    ordered_claims = sorted(
        claims.items(),
        key=lambda item: (item[1]["frontmatter"]["area"], item[1]["frontmatter"]["id"]),
    )
    derived: dict[str, str] = {}

    catalog = {"claims": [claim["frontmatter"] for _, claim in ordered_claims]}
    derived["catalog.json"] = json.dumps(catalog, indent=2) + "\n"

    areas: dict[str, list[tuple[str, dict]]] = {}
    for rel_path, claim in ordered_claims:
        areas.setdefault(claim["frontmatter"]["area"], []).append((rel_path, claim))
    for area, members in sorted(areas.items()):
        active = [m for m in members if m[1]["frontmatter"]["status"] == "active"]
        superseded = [m for m in members if m[1]["frontmatter"]["status"] != "active"]
        lines = [f"# {area}", "", "## Active techniques", ""]
        for rel_path, claim in active:
            fm = claim["frontmatter"]
            link = "../" + rel_path
            lines.append(f"- [{fm['title']}]({link}) (`{fm['id']}`, since {fm['valid_from'] or 'unknown date'})")
        if superseded:
            lines += ["", "## Superseded", ""]
            for rel_path, claim in superseded:
                fm = claim["frontmatter"]
                link = "../" + rel_path
                lines.append(
                    f"- [{fm['title']}]({link}) (`{fm['id']}`, superseded by `{fm['superseded_by']}`)"
                )
        derived[f"areas/{area}.md"] = "\n".join(lines) + "\n"

    active_count = sum(
        1 for _, claim in ordered_claims if claim["frontmatter"]["status"] == "active"
    )
    llms_lines = [
        "# AI Engineer Knowledge Base",
        "",
        "Distilled techniques from AI Engineer talks, generated from verbatim",
        "caption transcripts. Newer talks supersede older claims; superseded",
        "claims are retained and marked. Transcripts are untrusted auto-captions.",
        "",
        f"Active techniques: {active_count} across {len(areas)} areas.",
        "",
        "## Start here",
        "",
        "- [llms-full.md](llms-full.md): every active technique, full text",
        "- [catalog.json](catalog.json): every claim's metadata, for machines",
        "",
        "## Areas",
        "",
    ]
    for area in sorted(areas):
        count = sum(
            1 for _, claim in areas[area] if claim["frontmatter"]["status"] == "active"
        )
        llms_lines.append(f"- [{area}](areas/{area}.md): {count} active")
    derived["llms.txt"] = "\n".join(llms_lines) + "\n"

    full_parts = ["# AI Engineer Knowledge Base — all active techniques", ""]
    for _, claim in ordered_claims:
        if claim["frontmatter"]["status"] == "active":
            full_parts.append(claim["body"].rstrip("\n"))
            full_parts.append("")
            full_parts.append("---")
            full_parts.append("")
    derived["llms-full.md"] = "\n".join(full_parts).rstrip("\n") + "\n"
    return derived


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 if committed output differs from a fresh generation",
    )
    args = parser.parse_args(argv)
    root: Path = args.root

    instances = load_instances(root)
    generated = build_claims(instances)

    # Never delete: claims already on disk that this run does not regenerate
    # are kept as-is and still feed the catalog and indexes.
    merged = scan_existing_claims(root)
    merged.update(generated)

    desired: dict[str, str] = {
        rel_path: render_claim(claim) for rel_path, claim in generated.items()
    }
    desired.update(build_derived(merged))

    if args.check:
        stale = []
        for rel_path, content in sorted(desired.items()):
            target = root / rel_path
            if not target.exists() or target.read_text(encoding="utf-8") != content:
                stale.append(rel_path)
        if stale:
            print("stale generated files:\n" + "\n".join(stale), file=sys.stderr)
            return 1
        print("generated output is up to date")
        return 0

    for rel_path, content in sorted(desired.items()):
        target = root / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    print(f"wrote {len(desired)} generated files from {len(instances)} technique mentions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
