"""Tests for the deterministic, recency-aware claims generator.

Core rule under test: ordering is by talk publish date. A newer talk on the
same technique supersedes the older claim. An unknown date never supersedes
a dated claim. Nothing is ever deleted.
"""

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_claims.py"


def write_analysis(root: Path, name: str, payload: dict) -> None:
    (root / "analysis").mkdir(parents=True, exist_ok=True)
    (root / "analysis" / name).write_text(json.dumps(payload), encoding="utf-8")


def technique(what: str, **overrides) -> dict:
    base = {
        "slug": "trace-first-debugging",
        "title": "Trace-first debugging",
        "area": "observability",
        "what": what,
        "evidence": "Speaker walks through a failing run via its trace.",
        "apply": "Open the trace before re-running anything.",
        "expected_effect": "Less guesswork, faster root cause.",
        "confidence": 0.8,
        "relevance": 0.9,
    }
    base.update(overrides)
    return base


def analysis(video_id: str, talk_date, what: str) -> dict:
    payload = {
        "video_id": video_id,
        "video_url": f"https://www.youtube.com/watch?v={video_id}",
        "title": f"Talk {video_id}",
        "retrieved_at": "2026-10-26T12:00:00Z",
        "techniques": [technique(what)],
    }
    if talk_date is not None:
        payload["talk_date"] = talk_date
    return payload


def run_generator(root: Path, *extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root), *extra],
        capture_output=True,
        text=True,
    )


def read_claim(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path} has no frontmatter"
    frontmatter, body = text[4:].split("\n---\n", 1)
    return yaml.safe_load(frontmatter), body


def test_newer_talk_supersedes_older_claim(tmp_path: Path) -> None:
    write_analysis(tmp_path, "old.json", analysis("OLDVIDEO1", "2025-01-10", "Old way."))
    write_analysis(tmp_path, "new.json", analysis("NEWVIDEO1", "2026-03-01", "New way."))

    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stderr

    active_path = tmp_path / "claims" / "observability" / "trace-first-debugging.md"
    old_path = tmp_path / "claims" / "observability" / "trace-first-debugging--OLDVIDEO1.md"
    assert active_path.exists()
    assert old_path.exists(), "superseded claim must be retained, never deleted"

    active, active_body = read_claim(active_path)
    assert active["status"] == "active"
    assert active["id"] == "trace-first-debugging"
    assert str(active["valid_from"]) == "2026-03-01"
    assert active["valid_to"] is None
    assert active["superseded_by"] is None
    assert active["sources"][0]["video_url"].endswith("NEWVIDEO1")
    assert "New way." in active_body

    old, _ = read_claim(old_path)
    assert old["status"] == "superseded"
    assert old["superseded_by"] == "trace-first-debugging"
    assert str(old["valid_from"]) == "2025-01-10"
    assert str(old["valid_to"]) == "2026-03-01"


def test_unknown_date_never_supersedes_dated_claim(tmp_path: Path) -> None:
    write_analysis(tmp_path, "dated.json", analysis("DATED0001", "2025-06-01", "Dated way."))
    write_analysis(tmp_path, "undated.json", analysis("UNDATED01", None, "Undated way."))

    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stderr

    active, active_body = read_claim(
        tmp_path / "claims" / "observability" / "trace-first-debugging.md"
    )
    assert active["status"] == "active"
    assert active["sources"][0]["video_url"].endswith("DATED0001")
    assert "Dated way." in active_body

    undated, _ = read_claim(
        tmp_path / "claims" / "observability" / "trace-first-debugging--UNDATED01.md"
    )
    assert undated["status"] == "superseded"
    assert undated["superseded_by"] == "trace-first-debugging"
    assert undated["valid_from"] is None


def test_undated_only_claim_is_active(tmp_path: Path) -> None:
    write_analysis(tmp_path, "undated.json", analysis("UNDATED01", None, "Only way."))

    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stderr

    active, _ = read_claim(tmp_path / "claims" / "observability" / "trace-first-debugging.md")
    assert active["status"] == "active"
    assert active["valid_from"] is None
    assert active["superseded_by"] is None


def test_output_is_deterministic_regardless_of_input_order(tmp_path: Path) -> None:
    first = tmp_path / "a"
    second = tmp_path / "b"
    for root, order in ((first, ["1", "2", "3"]), (second, ["3", "1", "2"])):
        dates = {"1": "2024-05-01", "2": "2026-01-01", "3": "2025-05-01"}
        for key in order:
            write_analysis(
                root, f"{key}.json", analysis(f"VIDEO000{key}", dates[key], f"Way {key}.")
            )
        assert run_generator(root).returncode == 0

    def snapshot(root: Path) -> dict[str, str]:
        return {
            str(p.relative_to(root)): p.read_text(encoding="utf-8")
            for p in sorted(root.rglob("*"))
            if p.is_file() and "analysis" not in p.parts
        }

    assert snapshot(first) == snapshot(second)

    active, _ = read_claim(first / "claims" / "observability" / "trace-first-debugging.md")
    assert active["sources"][0]["video_url"].endswith("VIDEO0002")


def test_same_date_tie_break_is_deterministic(tmp_path: Path) -> None:
    write_analysis(tmp_path, "b.json", analysis("BBBVIDEO1", "2026-01-01", "B way."))
    write_analysis(tmp_path, "a.json", analysis("AAAVIDEO1", "2026-01-01", "A way."))

    assert run_generator(tmp_path).returncode == 0
    active, _ = read_claim(tmp_path / "claims" / "observability" / "trace-first-debugging.md")
    # Documented tie-break: (talk_date, video_id) descending.
    assert active["sources"][0]["video_url"].endswith("BBBVIDEO1")


def test_preexisting_claim_file_is_never_deleted(tmp_path: Path) -> None:
    orphan_dir = tmp_path / "claims" / "agents"
    orphan_dir.mkdir(parents=True)
    orphan = orphan_dir / "orphan-technique.md"
    orphan.write_text(
        "---\n"
        "type: technique\n"
        "id: orphan-technique\n"
        'title: "Orphan technique"\n'
        "area: agents\n"
        "status: active\n"
        "valid_from: 2024-01-01\n"
        "valid_to: null\n"
        "superseded_by: null\n"
        "confidence: 0.5\n"
        "relevance: 0.5\n"
        "sources:\n"
        '  - video_url: "https://www.youtube.com/watch?v=ORPHAN001"\n'
        "    talk_date: 2024-01-01\n"
        '    analysis_file: "analysis/orphan.json"\n'
        "---\n\n# Orphan technique\n",
        encoding="utf-8",
    )
    write_analysis(tmp_path, "new.json", analysis("NEWVIDEO1", "2026-03-01", "New way."))

    assert run_generator(tmp_path).returncode == 0
    assert orphan.exists(), "generator must never delete an existing claim"

    catalog = json.loads((tmp_path / "catalog.json").read_text(encoding="utf-8"))
    ids = [c["id"] for c in catalog["claims"]]
    assert "orphan-technique" in ids


def test_frontmatter_matches_the_documented_contract(tmp_path: Path) -> None:
    write_analysis(tmp_path, "one.json", analysis("VIDEO0001", "2026-01-15", "Way."))

    assert run_generator(tmp_path).returncode == 0
    claim, body = read_claim(tmp_path / "claims" / "observability" / "trace-first-debugging.md")

    assert claim["type"] == "technique"
    assert set(claim) == {
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
    }
    assert claim["sources"][0]["analysis_file"] == "analysis/one.json"
    assert str(claim["sources"][0]["talk_date"]) == "2026-01-15"
    for heading in ("## What", "## Evidence", "## Apply to us", "## Expected effect"):
        assert heading in body


def test_catalog_areas_and_llms_outputs(tmp_path: Path) -> None:
    write_analysis(tmp_path, "old.json", analysis("OLDVIDEO1", "2025-01-10", "Old way."))
    write_analysis(tmp_path, "new.json", analysis("NEWVIDEO1", "2026-03-01", "New way."))

    assert run_generator(tmp_path).returncode == 0

    catalog = json.loads((tmp_path / "catalog.json").read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in catalog["claims"]}
    assert by_id["trace-first-debugging"]["status"] == "active"
    assert by_id["trace-first-debugging--OLDVIDEO1"]["superseded_by"] == "trace-first-debugging"

    area_page = (tmp_path / "areas" / "observability.md").read_text(encoding="utf-8")
    assert "trace-first-debugging" in area_page

    llms = (tmp_path / "llms.txt").read_text(encoding="utf-8")
    assert len(llms.splitlines()) < 100
    assert "llms-full.md" in llms

    full = (tmp_path / "llms-full.md").read_text(encoding="utf-8")
    assert "New way." in full
    assert "Old way." not in full, "llms-full carries active claims only"


def test_check_mode_detects_stale_output(tmp_path: Path) -> None:
    write_analysis(tmp_path, "one.json", analysis("VIDEO0001", "2026-01-15", "Way."))

    stale = run_generator(tmp_path, "--check")
    assert stale.returncode == 1, "check must fail before generation"

    assert run_generator(tmp_path).returncode == 0
    fresh = run_generator(tmp_path, "--check")
    assert fresh.returncode == 0, fresh.stderr + fresh.stdout
