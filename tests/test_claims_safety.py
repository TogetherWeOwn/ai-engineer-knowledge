"""Additional publication-boundary regressions; the pinned oracle stays untouched."""

import copy
import json
from pathlib import Path

import pytest

from test_claims_acceptance import (
    CONTEXT_ID, CONTEXT_VID, NEW_VID, add_followup,
    assert_rejected_without_writes, current_claim, generated_snapshot,
    proposals, run_generator, seed_corpus, snapshot, write_json,
)


def test_source_catalog_at_root_is_not_a_generated_catalog(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    source = tmp_path / "data" / "catalog.json"
    target = tmp_path / "catalog.json"
    source.rename(target)
    before = snapshot(tmp_path)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    for name, content in before.items():
        assert (tmp_path / name).read_bytes() == content
    assert current_claim(tmp_path)[0]["id"] == CONTEXT_ID


def test_successful_relation_is_retained_without_resubmitting_proposals(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    add_followup(tmp_path, "2025-02-15T00:00:00Z")
    path = proposals(tmp_path, "contradicts")
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    before = generated_snapshot(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    assert generated_snapshot(tmp_path) == before
    assert run_generator(tmp_path, "--check").returncode == 0


@pytest.mark.parametrize("value", [None, [], {}, {"schema_version": True, "proposals": []},
                                    {"schema_version": 2, "proposals": []},
                                    {"schema_version": 1, "proposals": "not a list"},
                                    {"schema_version": 1, "proposals": [None]}])
def test_invalid_relation_envelope_is_rejected_before_writes(tmp_path: Path, value) -> None:
    seed_corpus(tmp_path)
    path = tmp_path / "relations.json"
    write_json(path, value)
    assert_rejected_without_writes(tmp_path, "--relations", str(path))


@pytest.mark.parametrize("kind", ["catalog", "analysis", "transcript", "output"])
def test_symlink_escape_is_rejected_without_following_writes(tmp_path: Path, kind: str) -> None:
    root = tmp_path / "corpus"
    seed_corpus(root)
    outside = tmp_path / "outside"
    outside.mkdir()
    if kind == "output":
        (root / "kb").symlink_to(outside, target_is_directory=True)
    else:
        path = {"catalog": root / "data" / "catalog.json",
                "analysis": root / "analysis" / f"{CONTEXT_VID}.json",
                "transcript": root / "transcripts" / f"{CONTEXT_VID}.txt"}[kind]
        target = outside / path.name
        path.rename(target)
        path.symlink_to(target)
    before = snapshot(tmp_path)
    result = run_generator(root)
    assert result.returncode != 0
    assert snapshot(tmp_path) == before
    assert isinstance(json.loads(result.stdout)["error"]["code"], str)


def test_quote_verification_label_without_caption_match_is_not_evidence(tmp_path: Path) -> None:
    catalog = seed_corpus(tmp_path)
    forged = "Claimed verified words which are not in the caption body."
    catalog["techniques"][0]["sources"][0]["quote"] = forged
    write_json(tmp_path / "data" / "catalog.json", catalog)
    assert run_generator(tmp_path).returncode == 0
    assert forged.encode() not in b"\n".join(generated_snapshot(tmp_path).values())


def test_duplicate_analysis_identity_is_rejected_not_chosen_by_filename(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    data = json.loads((tmp_path / "analysis" / f"{CONTEXT_VID}.json").read_text())
    data["published_at"] = "2025-03-01T00:00:00Z"
    write_json(tmp_path / "analysis" / "conflicting.json", data)
    assert_rejected_without_writes(tmp_path)


def test_conflicting_relations_for_one_pair_are_rejected_before_writes(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    add_followup(tmp_path, "2025-02-15T00:00:00Z")
    path = proposals(tmp_path)
    data = json.loads(path.read_text())
    other = copy.deepcopy(data["proposals"][0])
    other["relation"] = "contradicts"
    data["proposals"].append(other)
    write_json(path, data)
    assert_rejected_without_writes(tmp_path, "--relations", str(path))


def test_old_unknown_evidence_prevents_age_proof_even_after_dated_support(tmp_path: Path) -> None:
    seed_corpus(tmp_path, date=None)
    assert run_generator(tmp_path).returncode == 0
    add_followup(tmp_path, "2025-01-15T00:00:00Z")
    path = proposals(tmp_path, "supports")
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    second = add_followup(tmp_path, "2025-04-15T00:00:00Z")
    second_vid = "FOLLOWUP002"
    second.update(vid=second_vid, source=f"https://www.youtube.com/watch?v={second_vid}")
    write_json(tmp_path / "analysis" / f"{second_vid}.json", second)
    add_followup(tmp_path, "2025-01-15T00:00:00Z")
    path = proposals(tmp_path, "contradicts", vid=second_vid)
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    assert current_claim(tmp_path)[0]["valid_from"] is None
    assert not list((tmp_path / "kb" / "history").glob("*.md"))


def test_late_support_cannot_rewrite_previously_archived_evidence(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    add_followup(tmp_path, "2025-02-01T00:00:00Z")
    path = proposals(tmp_path, "refines")
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    history_before = {p.name: p.read_bytes() for p in (tmp_path / "kb" / "history").glob("*.md")}
    log_before = (tmp_path / "kb" / "log.md").read_bytes()
    # Backdated support arrives after supersession was already recorded.
    late = add_followup(tmp_path, "2025-01-20T00:00:00Z")
    second_vid = "FOLLOWUP002"
    late.update(vid=second_vid, source=f"https://www.youtube.com/watch?v={second_vid}")
    write_json(tmp_path / "analysis" / f"{second_vid}.json", late)
    add_followup(tmp_path, "2025-02-01T00:00:00Z")
    path = proposals(tmp_path, "supports", vid=second_vid)
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    current, _ = current_claim(tmp_path)
    assert current["valid_from"] == "2025-02-01T00:00:00Z"
    assert {p.name: p.read_bytes() for p in (tmp_path / "kb" / "history").glob("*.md")} == history_before
    assert (tmp_path / "kb" / "log.md").read_bytes() == log_before


def test_display_title_edit_does_not_rewrite_or_duplicate_history(tmp_path: Path) -> None:
    catalog = seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    add_followup(tmp_path, "2025-02-01T00:00:00Z")
    path = proposals(tmp_path, "refines")
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    history_before = {p.name: p.read_bytes() for p in (tmp_path / "kb" / "history").glob("*.md")}
    log_before = (tmp_path / "kb" / "log.md").read_bytes()
    catalog["techniques"][0]["title"] = "A clearer display title"
    write_json(tmp_path / "data" / "catalog.json", catalog)
    assert run_generator(tmp_path).returncode == 0
    assert current_claim(tmp_path)[0]["title"] == "A clearer display title"
    assert {p.name: p.read_bytes() for p in (tmp_path / "kb" / "history").glob("*.md")} == history_before
    assert (tmp_path / "kb" / "log.md").read_bytes() == log_before


@pytest.mark.parametrize("mutation", [{"mechanism": []},
                                       {"mechanism": {"variants": 7}},
                                       {"mechanism": {"variants": {"title": "not a list"}}}])
def test_malformed_catalog_mechanism_has_a_structured_atomic_error(tmp_path: Path, mutation) -> None:
    catalog = seed_corpus(tmp_path)
    catalog["techniques"][0].update(mutation)
    write_json(tmp_path / "data" / "catalog.json", catalog)
    assert_rejected_without_writes(tmp_path, "--candidates")


def test_quote_at_a_different_timestamp_is_not_attested_by_a_label(tmp_path: Path) -> None:
    catalog = seed_corpus(tmp_path)
    catalog["techniques"][0]["sources"][0]["timestamp"] = "59:59"
    write_json(tmp_path / "data" / "catalog.json", catalog)
    assert run_generator(tmp_path).returncode == 0
    _, body = current_claim(tmp_path)
    assert "more than 75%" not in body


@pytest.mark.parametrize("mutation", [{"sources": []}, {"sources": [None]},
                                       {"status": "active"}, {"title": None}])
def test_corrupted_history_fails_closed_with_a_structured_error(tmp_path: Path, mutation) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    add_followup(tmp_path, "2025-02-01T00:00:00Z")
    path = proposals(tmp_path, "refines")
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    history = next(p for p in (tmp_path / "kb" / "history").glob("*.md") if p.name != "index.md")
    block, body = history.read_text()[4:].split("\n---\n", 1)
    metadata = json.loads(block)
    metadata.update(mutation)
    history.write_text("---\n" + json.dumps(metadata) + "\n---\n" + body)
    assert_rejected_without_writes(tmp_path, "--check")


def test_ambiguous_corrupt_inputs_do_not_fall_back_to_legacy_publication(tmp_path: Path) -> None:
    analysis = tmp_path / "analysis"
    analysis.mkdir()
    (analysis / "broken.json").write_text('{"vid":')
    assert_rejected_without_writes(tmp_path)
