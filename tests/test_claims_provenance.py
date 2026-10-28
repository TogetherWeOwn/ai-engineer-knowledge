"""Source-identity and body-hash joins must fail closed before publication."""

import json
from pathlib import Path

import pytest

from test_claims_acceptance import (
    CONTEXT_VID, DEMO_VID, NEW_VID, add_followup,
    assert_rejected_without_writes, current_claim, proposals,
    run_generator, seed_corpus, write_json,
)


@pytest.mark.parametrize("mode", [(), ("--candidates",), ("--check",)])
@pytest.mark.parametrize("fault,code", [
    ("other_video", "transcript_source_mismatch"),
    ("source_header", "transcript_source_mismatch"),
    ("analysis_hash", "transcript_hash_mismatch"),
    ("header_hash", "transcript_hash_mismatch"),
    ("changed_body", "transcript_hash_mismatch"),
    ("changed_newlines", "transcript_hash_mismatch"),
    ("missing_analysis_hash", "transcript_hash_mismatch"),
    ("missing_file", "missing_transcript"),
    ("duplicate_source", "ambiguous_transcript_header"),
    ("duplicate_hash", "ambiguous_transcript_header"),
])
def test_unbound_transcript_is_rejected_before_any_write(tmp_path: Path, mode, fault, code) -> None:
    catalog = seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    analysis_path = tmp_path / "analysis" / f"{CONTEXT_VID}.json"
    analysis = json.loads(analysis_path.read_text())
    transcript_path = tmp_path / analysis["transcript_file"]
    text = transcript_path.read_text()
    if fault == "other_video":
        # A fully conforming other video's caption and matching hash still
        # cannot supply this video's speaker or quote/footnote attribution.
        other = json.loads((tmp_path / "analysis" / f"{DEMO_VID}.json").read_text())
        analysis.update(transcript_file=other["transcript_file"],
                        transcript_sha256=other["transcript_sha256"])
        context = next(row for row in catalog["techniques"]
                       if row["sources"][0]["vid"] == CONTEXT_VID)
        demo = next(row for row in catalog["techniques"]
                    if row["sources"][0]["vid"] == DEMO_VID)
        context["sources"][0].update(quote=demo["sources"][0]["quote"],
                                      timestamp=demo["sources"][0]["timestamp"])
        write_json(tmp_path / "data" / "catalog.json", catalog)
    elif fault == "source_header":
        transcript_path.write_text(text.replace(f"watch?v={CONTEXT_VID}", f"watch?v={DEMO_VID}"))
    elif fault == "analysis_hash":
        analysis["transcript_sha256"] = "0" * 64
    elif fault == "header_hash":
        transcript_path.write_text(text.replace(analysis["transcript_sha256"], "0" * 64))
    elif fault == "changed_body":
        transcript_path.write_text(text + "Unrecorded caption edit.\n")
    elif fault == "changed_newlines":
        transcript_path.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))
    elif fault == "missing_analysis_hash":
        del analysis["transcript_sha256"]
    elif fault == "missing_file":
        transcript_path.unlink()
    elif fault == "duplicate_source":
        transcript_path.write_text(f"# source: https://www.youtube.com/watch?v={DEMO_VID}\n" + text)
    elif fault == "duplicate_hash":
        transcript_path.write_text("# sha256: " + "0" * 64 + "\n" + text)
    write_json(analysis_path, analysis)
    report = assert_rejected_without_writes(tmp_path, *mode)
    assert report["error"]["code"] == code


def test_relation_cannot_introduce_a_misbound_transcript(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    followup = add_followup(tmp_path, "2025-02-15T00:00:00Z")
    other = json.loads((tmp_path / "analysis" / f"{CONTEXT_VID}.json").read_text())
    followup.update(transcript_file=other["transcript_file"],
                    transcript_sha256=other["transcript_sha256"])
    write_json(tmp_path / "analysis" / f"{NEW_VID}.json", followup)
    path = proposals(tmp_path, "refines")
    report = assert_rejected_without_writes(tmp_path, "--relations", str(path))
    assert report["error"]["code"] == "transcript_source_mismatch"


def test_correctly_bound_transcript_still_publishes_its_quote_and_speaker(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    metadata, body = current_claim(tmp_path)
    assert metadata["sources"][0]["id"] == CONTEXT_VID
    assert metadata["sources"][0]["author"] == "Sam Morrow"
    assert "more than 75%" in body
    assert run_generator(tmp_path, "--check").returncode == 0
