"""Tests for scripts/import_corpus.py and the imported corpus it produced.

The first group builds a synthetic raw corpus in a temp dir, so no real
captions, keys or network are used. The second group checks the committed
import: transcript headers, analysis provenance links and the frozen
catalog identities.
"""

import hashlib
import json
import os
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import import_corpus as ic  # noqa: E402

FROZEN_TECHNIQUE_COUNT = 475
FROZEN_ID_LIST_SHA256 = "72caeca5055237e6dbd261a741f23aaf01476a9f0093f5340940be981ed920b5"
REQUIRED_HEADER = ("title", "source", "channel", "caption_track", "retrieved_at", "sha256", "takedown")
GENERIC_LEAKS = re.compile(r"/home/|/Users/|/srv/private|\.ts\.net\b|\b192\.168\.\d|"
                           r"\bsynthetic/[a-z]+-v?\d", re.I)
CAPTION_HEADER = "# auto/author captions, unverified"
MACHINE_HEADER = "# machine transcript (Whisper; no YouTube captions)"


def has_one_provenance_label(lines):
    return sum(line in (CAPTION_HEADER, MACHINE_HEADER) for line in lines) == 1


@pytest.mark.parametrize("lines, valid", [
    ([CAPTION_HEADER], True),
    ([MACHINE_HEADER], True),
    ([], False),
    ([CAPTION_HEADER, MACHINE_HEADER], False),
    ([CAPTION_HEADER, CAPTION_HEADER], False),
])
def test_provenance_label_contract(lines, valid):
    assert has_one_provenance_label(lines) is valid


def split_header(text: str):
    lines = text.split("\n")
    index = 0
    while index < len(lines) and lines[index].startswith("#"):
        index += 1
    return lines[:index], "\n".join(lines[index:])


def header_fields(lines):
    fields = {}
    for line in lines:
        match = re.match(r"^#\s*([a-z0-9_]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2)
    return fields


# ---------------------------------------------------------------------------
# Synthetic corpus
# ---------------------------------------------------------------------------

BODY_A = ("[00:01] Welcome everyone to the talk.\n"
          "[00:05] We cut the tool output so it only keeps fields agents use.\n"
          "[00:09] That saved more than seventy five percent of output tokens.\n"
          "[01:02] Then we added evals for every tool description.\n")
BODY_B = "[00:00] Hola a todos y bienvenidos a esta charla sobre agentes.\n"


def raw_transcript(vid, title, track, body, source="direct-v4"):
    return (f"# {title}\n# url: {ic.WATCH_PREFIX}{vid}\n"
            f"# duration_s: 60 | views: 10 | source: {source} | track: {track}\n\n{body}")


def make_corpus(tmp_path: Path) -> Path:
    src = tmp_path / "corpus"
    (src / "transcripts").mkdir(parents=True)
    (src / "analysis").mkdir()
    (src / "synthesis").mkdir()
    files = {
        "VIDAAAA0001": raw_transcript("VIDAAAA0001", "Tool Diets — Jane Doe, ExampleCo", "auto", BODY_A),
        "-VIDBBBB002": raw_transcript("-VIDBBBB002", "Charla sin orador", "dub-auto:es", BODY_B),
        "VIDWHSP0003": raw_transcript("VIDWHSP0003", "Machine Talk - Sam Roe", "machine", BODY_B,
                                      source="whisper"),
    }
    for vid, text in files.items():
        path = src / "transcripts" / f"{vid}.txt"
        path.write_text(text, encoding="utf-8")
        os.utime(path, (1761200000, 1761200000))
    (src / "transcripts" / "run.log").write_text(
        "2025-10-23T06:13:20Z ok 1 VIDAAAA0001 (40w, direct-v4/auto) Tool Diets\n"
        "2025-10-20T00:00:00Z ok 1 VIDAAAA0001 (40w, direct-v4/auto) older unrelated fetch\n",
        encoding="utf-8")
    analysis = {
        "vid": "VIDAAAA0001", "title": "Tool Diets — Jane Doe, ExampleCo",
        "talk_summary": "Jane explains output trimming for tools. This maps directly onto our setup.",
        "takeaways": [
            {"area": "cost-tokens", "technique": "Trim tool outputs",
             "what_they_do": "Return only fields agents use. We should copy this.",
             "evidence_quote": "only keeps fields agents use",
             "numbers": ">75% fewer output tokens", "private_mapping": "internal note",
             "expected_effect": "per run", "confidence": "high"},
            {"area": "evaluation", "technique": "Eval tool descriptions",
             "what_they_do": "Evaluate each description.",
             "evidence_quote": "they evaluated descriptions nightly with a judge",
             "numbers": "", "private_mapping": "x", "expected_effect": "y", "confidence": "medium"},
            {"area": "evaluation", "technique": "Ellipsis quote",
             "what_they_do": "Pieces in order.",
             "evidence_quote": "welcome everyone to the talk ... saved more than seventy five percent",
             "numbers": "", "private_mapping": "x", "expected_effect": "y", "confidence": "low"},
        ],
        "relevance": 5, "model": "provider/model-x-1.0-0101", "served_model": "m", "usage": {"t": 1},
        "truncated": False, "analyzed_at": "2025-10-24T00:00:00Z", "note": "private note",
    }
    (src / "analysis" / "VIDAAAA0001.json").write_text(json.dumps(analysis), encoding="utf-8")
    (src / "analysis" / "VIDWHSP0003.json").write_text(
        json.dumps(dict(analysis, vid="VIDWHSP0003")), encoding="utf-8")
    techniques = []
    for index, tid in enumerate(["zeta-tool-diet", "alpha-evals", "alpha-evals-2"]):
        techniques.append({
            "id": tid, "title": f"Technique {index}", "area": "context-engineering",
            "mechanism": {"summary": "Trim payloads.", "representative_explanation": "Noise costs tokens.",
                          "representative_record_id": "R:1", "variants": [
                              {"title": "Apply it to our cards", "source_record_ids": ["R:1"]}]},
            "concrete_change_for_us": "private", "internal_status": "doing", "effort_hours": [1, 2],
            "source_count": 1, "source_record_count": 1, "deep_read_source_count": 1,
            "triage_only_source_count": 0, "source": "deep-read", "evidence_level": "deep-read",
            "quote_evidence": {"normalized-exact": 1},
            "expected_benefit": {"cost": "Less input", "certainty": "Directional."},
            "reported_measurements": [{"text": "75% fewer tokens.", "source_record_ids": ["R:1"],
                                       "attribution": "not our expected gain"}],
            "risk": {"level": "low", "failure_modes": ["Wrong scope."], "mitigation": "Stage first."},
            "how_to_measure_success": {"metrics": ["tokens per task"], "acceptance": "Compare cohorts.",
                                       "baseline_paths": ["/srv/private/notes.md"],
                                       "no_new_model_compare": True},
            "sources": [{"record_id": "R:1", "vid": "VIDAAAA0001", "talk": "Tool Diets",
                         "url": ic.WATCH_PREFIX + "VIDAAAA0001&t=5s", "source": "deep-read",
                         "origin_path": "/srv/private/reads.json", "transcript_path": "/srv/private/x.txt",
                         "quote": "We cut the tool output so it\nonly keeps fields agents use.",
                         "timestamp": "00:05", "timestamp_end": "00:05", "quote_verification": "normalized-exact",
                         "quote_match_score": 1.0, "matching_occurrences": 1, "requires_confirmation": False,
                         "quote_is_verbatim_original": True, "input_technique": "Trim outputs",
                         "input_area": "cost-tokens", "mechanism_in_source": "Trim at the source.",
                         "reader_status": "doing", "deepseek_correction": "x", "clustering": {}}],
        })
    catalog = {"schema_version": "1.0", "title": "Catalog", "generated_at": "2025-10-24T00:00:00Z",
               "catalog_path": "/srv/private/catalog.json", "areas": ["context-engineering"],
               "counts": {"raw_input_records": 3, "validated_already_do_clusters": 1},
               "scope": {"source_scope": "Every deep-read technique.", "owner_todos": ["x"]},
               "methodology": {"loading": "Loaded all files.", "status": "private status rule"},
               "techniques": techniques, "validated_already_do": [{"id": "private"}],
               "validation": {"validated_at": "2025-10-24T00:00:00Z", "independent_checks": 9,
                              "failures": 0, "verified": ["IDs consistent"]}}
    (src / "synthesis" / "catalog.json").write_text(json.dumps(catalog), encoding="utf-8")
    return src


def run_import(src: Path, out: Path, **kwargs) -> dict:
    out.mkdir(exist_ok=True)
    return ic.run(src, out, "2025-10-25T00:00:00Z", kwargs.get("private", {}),
                  kwargs.get("include_machine", False))


def tree_bytes(root: Path) -> dict:
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


def test_transcript_header_contract(tmp_path: Path) -> None:
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    report = run_import(src, out)
    assert report["transcripts"] == 2
    assert report["held"]["VIDWHSP0003"].startswith("machine transcript")
    text = (out / "transcripts" / "VIDAAAA0001.txt").read_text(encoding="utf-8")
    lines, body = split_header(text)
    fields = header_fields(lines)
    for key in REQUIRED_HEADER:
        assert key in fields, key
    assert fields["source"] == ic.WATCH_PREFIX + "VIDAAAA0001"
    assert fields["speaker"] == "Jane Doe, ExampleCo"
    assert fields["retrieved_at"] == "2025-10-23T06:13:20Z"  # run.log time next to the file mtime
    assert fields["sha256"] == hashlib.sha256(body.encode("utf-8")).hexdigest()
    assert body == BODY_A
    assert "# " + ic.CAPTION_LABEL in lines
    assert "duration_s" not in text and "direct-v4" not in text


def test_dub_track_labelled_and_speakerless_title(tmp_path: Path) -> None:
    out = tmp_path / "out"
    run_import(make_corpus(tmp_path), out)
    lines, _ = split_header((out / "transcripts" / "-VIDBBBB002.txt").read_text(encoding="utf-8"))
    fields = header_fields(lines)
    assert "speaker" not in fields and fields["channel"] == ic.CHANNEL_CREDIT
    assert fields["caption_track"].startswith("dub-auto:es (YouTube auto-dubbed Spanish")


def test_machine_transcript_needs_flag_and_never_claims_captions(tmp_path: Path) -> None:
    out = tmp_path / "out"
    report = run_import(make_corpus(tmp_path), out, include_machine=True)
    assert "VIDWHSP0003" not in report["held"]
    text = (out / "transcripts" / "VIDWHSP0003.txt").read_text(encoding="utf-8")
    lines, _ = split_header(text)
    assert "# machine transcript (Whisper; no YouTube captions)" in lines
    assert "# auto/author captions, unverified" not in lines


def test_analysis_projection_is_allowlisted_and_verified(tmp_path: Path) -> None:
    out = tmp_path / "out"
    run_import(make_corpus(tmp_path), out)
    assert not (out / "analysis" / "VIDWHSP0003.json").exists()
    data = json.loads((out / "analysis" / "VIDAAAA0001.json").read_text(encoding="utf-8"))
    assert set(data) == {"vid", "title", "source", "talk_summary", "takeaways", "truncated", "analyzed_at",
                         "analyzer", "transcript_file", "transcript_sha256", "retrieved_at"}
    assert data["talk_summary"] == "Jane explains output trimming for tools."
    assert data["analyzer"] == "model-x-1.0"
    first, second, third = data["takeaways"]
    assert "private_mapping" not in first and "expected_effect" not in first
    assert first["what_they_do"] == "Return only fields agents use."
    assert first["evidence_quote_verification"] == "normalized-exact"
    assert first["evidence_timestamp"] == "00:05"
    assert first["confidence"] == "high"
    assert second["evidence_quote"] is None
    assert second["evidence_quote_verification"] == "not-found-in-captions"
    assert third["evidence_quote_verification"] == "ordered-ellipsis-pieces"
    assert third["evidence_timestamp"] == "00:01"
    header = header_fields(split_header((out / data["transcript_file"]).read_text(encoding="utf-8"))[0])
    assert data["transcript_sha256"] == header["sha256"]
    assert data["retrieved_at"] == header["retrieved_at"]


def test_existing_published_at_is_preserved(tmp_path: Path) -> None:
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    path = out / "analysis" / "VIDAAAA0001.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(json.dumps(dict(data, published_at="2025-06-01T12:00:00Z")), encoding="utf-8")
    run_import(src, out)
    assert json.loads(path.read_text(encoding="utf-8"))["published_at"] == "2025-06-01T12:00:00Z"


def test_catalog_keeps_identities_and_drops_private_fields(tmp_path: Path) -> None:
    out = tmp_path / "out"
    run_import(make_corpus(tmp_path), out)
    catalog = json.loads((out / "data" / "catalog.json").read_text(encoding="utf-8"))
    ids = [t["id"] for t in catalog["techniques"]]
    assert ids == ["zeta-tool-diet", "alpha-evals", "alpha-evals-2"]
    assert catalog["technique_count"] == 3 and catalog["frozen"] is True
    assert catalog["id_list_sha256"] == hashlib.sha256(("\n".join(sorted(ids)) + "\n").encode()).hexdigest()
    assert "validated_already_do" not in catalog and "catalog_path" not in catalog
    assert set(catalog["methodology"]) == {"loading"}
    tech = catalog["techniques"][0]
    for key in ("concrete_change_for_us", "internal_status", "effort_hours"):
        assert key not in tech
    assert set(tech["how_to_measure_success"]) == {"metrics", "acceptance"}
    assert tech["mechanism"]["variants"][0]["title"] is None
    assert tech["reported_measurements"] == [{"text": "75% fewer tokens.", "source_record_ids": ["R:1"]}]
    source = tech["sources"][0]
    assert "origin_path" not in source and "reader_status" not in source
    assert source["transcript_file"] == "transcripts/VIDAAAA0001.txt"
    assert source["quote_verification"] == "normalized-exact"
    assert not GENERIC_LEAKS.search(json.dumps(catalog))


def test_private_terms_scrub_and_gate(tmp_path: Path) -> None:
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    report = run_import(src, out, private={"sentence_terms": ["exampleco"], "deny_literals": ["seventy five"]})
    # The transcript containing the literal is held, never edited.
    assert "leak gate" in report["held"]["VIDAAAA0001"]
    assert not (out / "transcripts" / "VIDAAAA0001.txt").exists()
    path = src / "analysis" / "VIDAAAA0001.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["takeaways"][0]["numbers"] = "see /Users/someone/notes.txt"
    path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ic.ImportError_):
        run_import(src, tmp_path / "out2")


def test_rerun_is_byte_identical(tmp_path: Path) -> None:
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    first = tree_bytes(out)
    run_import(src, out)
    assert tree_bytes(out) == first


# ---------------------------------------------------------------------------
# Committed import
# ---------------------------------------------------------------------------

REPO_TRANSCRIPTS = sorted((ROOT / "transcripts").glob("*.txt"))
REPO_ANALYSES = sorted((ROOT / "analysis").glob("*.json"))
REPO_CATALOG = ROOT / "data" / "catalog.json"


@pytest.mark.skipif(not REPO_TRANSCRIPTS, reason="no imported transcripts")
def test_repo_transcripts_have_required_header() -> None:
    failures = []
    for path in REPO_TRANSCRIPTS:
        text = path.read_text(encoding="utf-8")
        lines, body = split_header(text)
        fields = header_fields(lines)
        missing = [k for k in REQUIRED_HEADER if k not in fields]
        if missing or fields.get("source") != ic.WATCH_PREFIX + path.stem:
            failures.append((path.name, missing))
        elif fields["sha256"] != hashlib.sha256(body.encode("utf-8")).hexdigest():
            failures.append((path.name, "sha256"))
        elif not has_one_provenance_label(lines):
            failures.append((path.name, "label"))
        elif body.startswith("#") or not body.strip() or GENERIC_LEAKS.search(text):
            failures.append((path.name, "body"))
    assert not failures, failures[:10]


@pytest.mark.skipif(not REPO_ANALYSES, reason="no imported analysis")
def test_repo_analysis_links_to_transcripts() -> None:
    failures = []
    for path in REPO_ANALYSES:
        raw = path.read_text(encoding="utf-8")
        data = json.loads(raw)
        transcript = ROOT / data["transcript_file"]
        if data["vid"] != path.stem or not transcript.is_file() or GENERIC_LEAKS.search(raw):
            failures.append(path.name)
            continue
        fields = header_fields(split_header(transcript.read_text(encoding="utf-8"))[0])
        if (fields["sha256"], fields["retrieved_at"]) != (data["transcript_sha256"], data["retrieved_at"]):
            failures.append(path.name)
        if any(not isinstance(t.get("confidence"), str) for t in data["takeaways"]):
            failures.append(path.name)
    assert not failures, failures[:10]


@pytest.mark.skipif(not REPO_CATALOG.exists(), reason="no frozen catalog")
def test_repo_catalog_preserves_frozen_identities() -> None:
    raw = REPO_CATALOG.read_text(encoding="utf-8")
    catalog = json.loads(raw)
    ids = [t["id"] for t in catalog["techniques"]]
    assert len(ids) == len(set(ids)) == FROZEN_TECHNIQUE_COUNT == catalog["technique_count"]
    digest = hashlib.sha256(("\n".join(sorted(ids)) + "\n").encode()).hexdigest()
    assert digest == catalog["id_list_sha256"] == FROZEN_ID_LIST_SHA256
    assert catalog["frozen"] is True
    assert not GENERIC_LEAKS.search(raw)


def test_cli_refuses_to_export_without_private_policy(tmp_path: Path) -> None:
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    with pytest.raises(SystemExit) as exc:
        ic.main(["--src", str(src), "--out", str(out), "--exported-at", "2026-10-28T00:00:00Z"])
    assert exc.value.code == 2
    assert not out.exists() or not any(out.rglob("*.json"))
    empty = tmp_path / "policy.json"
    empty.write_text(json.dumps({"sentence_terms": [], "deny_regexes": [], "deny_literals": []}), encoding="utf-8")
    assert ic.main(["--src", str(src), "--out", str(out), "--exported-at", "2026-10-28T00:00:00Z",
                    "--private-terms", str(empty)]) == 2
    assert not out.exists() or not any(out.rglob("*.json"))
