"""Keep the contextual soak annotation durable without changing its evidence."""

import json
import shutil
from pathlib import Path

import pytest

from okf_contract import read_frontmatter
from test_claims_acceptance import generated_snapshot, run_generator, write_json


ROOT = Path(__file__).resolve().parents[1]
CLAIM = "kb/testing-ci/staging-soak-tests.md"
VID = "Sjfz1TqxzEs"
ORIGINAL = (
    "Validate with repeated 24-hour continuous runs (four distinct trials) rather than "
    "single demos, exposing environment drift like lighting changes."
)
QUOTE = "uh in the office, you know, so these are four distinct trials of 24-hour runs."
SOURCE = {
    "id": VID,
    "resource": f"https://www.youtube.com/watch?v={VID}",
    "title": "Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics",
    "author": "Jason Ma, Dyna Robotics",
    "last_modified": "2026-09-24T14:30:12Z",
    "analysis_file": f"analysis/{VID}.json",
}


def assert_applicability(text: str) -> None:
    for required in (
        "**Applicability (non-binding):**",
        "not a universal minimum calendar hold for software staging",
        "A quotation is neither company policy nor release authorization",
        "representative evidence and signals, sufficient thresholds",
        "required temporal, environmental and endurance coverage",
        "earliest safe exit, accountable owner, maximum UTC timeout and fail-closed timeout action",
        "End when sufficient evidence is available and required coverage is complete",
        "an immediate green check does not replace delayed-failure, lighting-change or endurance coverage",
        "never automatic acceptance",
        "no new numeric threshold or empirical claim that a shorter observation is equivalent",
        "does not weaken any applicable test, review, security, rollback or release gate",
    ):
        assert required in text, f"missing applicability safeguard: {required}"


def test_soak_applicability_survives_generation_with_original_evidence(tmp_path: Path) -> None:
    catalog = json.loads((ROOT / "data/catalog.json").read_text(encoding="utf-8"))
    row = next(row for row in catalog["techniques"] if row["id"] == "staging-soak-tests")
    explanation = row["mechanism"]["representative_explanation"]
    assert explanation.startswith(ORIGINAL + "\n\n")
    assert_applicability(explanation)
    assert row["sources"][0]["mechanism_in_source"] == ORIGINAL
    assert row["sources"][0]["quote"] == QUOTE
    assert row["sources"][0]["timestamp"] == "09:50"

    # Exercise the public CLI on one real catalog row and its unchanged source joins.
    catalog["techniques"] = [row]
    write_json(tmp_path / "data/catalog.json", catalog)
    inputs = {}
    for relative in (SOURCE["analysis_file"], f"transcripts/{VID}.txt"):
        destination = tmp_path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, destination)
        inputs[relative] = destination.read_bytes()
    inputs["data/catalog.json"] = (tmp_path / "data/catalog.json").read_bytes()

    def assert_fidelity(root: Path) -> str:
        metadata, body = read_frontmatter(root / CLAIM)
        assert metadata["sources"] == [SOURCE]
        assert metadata["valid_from"] == SOURCE["last_modified"]
        for text in (body, (root / "llms-full.txt").read_text(encoding="utf-8")):
            assert ORIGINAL in text
            assert f"> {QUOTE}\n> — 09:50 [^{VID}]" in text
            assert f"publication: {SOURCE['last_modified']}; analysis: `{SOURCE['analysis_file']}`" in text
        return body

    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    body = assert_fidelity(tmp_path)
    assert explanation in body
    assert_applicability(body)
    assert body in (tmp_path / "llms-full.txt").read_text(encoding="utf-8")
    assert assert_fidelity(ROOT) == body
    assert body in (ROOT / "llms-full.txt").read_text(encoding="utf-8")
    before = generated_snapshot(tmp_path)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    assert json.loads(result.stdout)["files_changed"] == 0
    assert generated_snapshot(tmp_path) == before
    result = run_generator(tmp_path, "--check")
    assert result.returncode == 0, result.stdout + result.stderr
    assert all((tmp_path / name).read_bytes() == content for name, content in inputs.items())

    # The pre-correction explanation still renders valid evidence, but must fail
    # the same applicability oracle in BOTH outputs, not just a fixture equality.
    row["mechanism"]["representative_explanation"] = ORIGINAL
    write_json(tmp_path / "data/catalog.json", catalog)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    control_body = assert_fidelity(tmp_path)
    for text in (control_body, (tmp_path / "llms-full.txt").read_text(encoding="utf-8")):
        with pytest.raises(AssertionError, match="missing applicability safeguard"):
            assert_applicability(text)
