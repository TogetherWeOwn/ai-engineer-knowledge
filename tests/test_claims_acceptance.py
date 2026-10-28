"""Test-first acceptance of the corrected catalog/OKF contract.

No generator implementation or implementation diff was used to derive this
suite. Input projections come from import commit e355ad807ca6229ded4351b3451aa373927366b6:
context-composition and runnable-evidence, one real source each, and their
real vid/takeaways/string-confidence analyses. Dates and follow-up talks are
controlled fixtures, NOT real publication-date or real-corpus evidence.

The CLI seam specified here is deliberately offline:
  generate_claims.py --root ROOT                     # one-shot migration
  generate_claims.py --root ROOT --candidates        # read-only JSON
  generate_claims.py --root ROOT --relations FILE    # untrusted proposals
A candidate row is {vid, takeaway_index, candidate_ids}; a proposal file is
{schema_version: 1, proposals: [{vid, takeaway_index, catalog_id, relation}]}.
The code must derive candidates itself, never trust IDs supplied by a model.
No credentials or live LLM/caption requests are needed to implement this seam.

Breaks caught: slug/merge identities; zero claims on the real schema; dates
invented from retrieval; implicit/29-day/unknown-date supersession; trusting
out-of-candidate proposals; catalog/history loss; replay churn; broken OKF
provenance; private mapping or unverified quote publication.
"""

import copy
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import pytest

from okf_contract import assert_project_bundle, aware_datetime, claim_documents, read_frontmatter


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_claims.py"
FIXTURES = Path(__file__).parent / "fixtures" / "claims"
CONTEXT_ID = "context-composition"
CONTEXT_AREA = "context-engineering"
CONTEXT_VID = "0n3MKk7r60w"
DEMO_ID = "runnable-evidence"
DEMO_VID = "MGzymaYBiss"
NEW_VID = "NEWVID00001"
BASE_DATE = "2025-01-01T00:00:00Z"
NEW_QUOTE = "Smaller tool payloads retain decisive evidence."


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fixture_json(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def write_transcript(root: Path, analysis: dict, quote: str, timestamp="00:01",
                     speaker="Fixture Speaker") -> None:
    vid = analysis["vid"]
    body = f"[{timestamp}] {quote}\n"
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    retrieved = "2026-10-22T09:38:47Z"
    text = (f"# source: https://www.youtube.com/watch?v={vid}\n"
            f"# speaker: {speaker}\n# channel: AI Engineer\n"
            f"# retrieved_at: {retrieved}\n# sha256: {digest}\n"
            f"# auto/author captions, unverified\n{body}")
    path = root / "transcripts" / f"{vid}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    analysis.update(transcript_file=f"transcripts/{vid}.txt", transcript_sha256=digest,
                    retrieved_at=retrieved)


def seed_corpus(root: Path, *, date=BASE_DATE, reverse=False) -> dict:
    catalog = fixture_json("catalog.json")
    if reverse:
        catalog["techniques"].reverse()
    write_json(root / "data" / "catalog.json", catalog)
    rows = list(catalog["techniques"])
    for row in rows:
        vid = row["sources"][0]["vid"]
        analysis = fixture_json(f"{vid}.json")
        index = 1 if vid == CONTEXT_VID else 4
        analysis["takeaways"] = [analysis["takeaways"][index]]
        analysis["published_at"] = date
        source = row["sources"][0]
        write_transcript(root, analysis, source["quote"], source["timestamp"],
                         "Sam Morrow" if vid == CONTEXT_VID else "Dan Shipper")
        write_json(root / "analysis" / f"{vid}.json", analysis)
    return catalog


def add_followup(root: Path, published_at, *, title=None, quote=NEW_QUOTE) -> dict:
    analysis = fixture_json(f"{CONTEXT_VID}.json")
    catalog = fixture_json("catalog.json")
    context = next(row for row in catalog["techniques"] if row["id"] == CONTEXT_ID)
    takeaway = copy.deepcopy(analysis["takeaways"][1])
    takeaway.update(technique=title or context["title"],
                    what_they_do=context["mechanism"]["summary"], evidence_quote=quote,
                    evidence_quote_verification="normalized-exact", evidence_timestamp="00:01")
    analysis.update(vid=NEW_VID, title="Controlled follow-up talk",
                    source=f"https://www.youtube.com/watch?v={NEW_VID}",
                    takeaways=[takeaway], published_at=published_at)
    write_transcript(root, analysis, quote)
    write_json(root / "analysis" / f"{NEW_VID}.json", analysis)
    return analysis


def proposals(root: Path, relation="supports", catalog_id=CONTEXT_ID, **overrides) -> Path:
    proposal = {"vid": NEW_VID, "takeaway_index": 0, "catalog_id": catalog_id,
                "relation": relation}
    proposal.update(overrides)
    path = root / "relations.json"
    write_json(path, {"schema_version": 1, "proposals": [proposal]})
    return path


def run_generator(root: Path, *extra: str) -> subprocess.CompletedProcess:
    # The deterministic boundary must not inherit any provider/run credentials.
    env = {key: os.environ[key] for key in ("PATH", "PYTHONPATH", "LANG") if key in os.environ}
    env.update(PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, str(SCRIPT), "--root", str(root), *extra],
                          capture_output=True, text=True, env=env, timeout=30)


def json_report(result: subprocess.CompletedProcess) -> dict:
    assert result.stdout.strip(), "CLI must return a JSON report, not an empty/argparse-only error"
    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError:
        pytest.fail(f"CLI stdout is not one JSON report: {result.stdout!r}")
    assert isinstance(report, dict), "CLI report must be an object"
    return report


def current_claim(root: Path, id=CONTEXT_ID, area=CONTEXT_AREA):
    path = root / "kb" / area / f"{id}.md"
    assert path.is_file(), f"missing frozen catalog claim: kb/{area}/{id}.md"
    return read_frontmatter(path)


def snapshot(root: Path) -> dict[str, bytes]:
    return {str(path.relative_to(root)): path.read_bytes()
            for path in sorted(root.rglob("*")) if path.is_file()}


def generated_snapshot(root: Path) -> dict[str, bytes]:
    return {name: content for name, content in snapshot(root).items()
            if name.startswith("kb/") or name in {"llms.txt", "llms-full.txt"}}


def assert_rejected_without_writes(root: Path, *extra: str) -> dict:
    before = snapshot(root)
    result = run_generator(root, *extra)
    assert result.returncode != 0, "invalid input/proposal must not be silently accepted"
    assert snapshot(root) == before, "validate the complete request before any output or source writes"
    report = json_report(result)
    error = report.get("error", report)
    assert isinstance(error, dict) and (error.get("code") or error.get("type")), (
        "errors need a stable code/type, not raw exception text"
    )
    return report


def test_real_schema_migration_preserves_frozen_ids_and_source_bytes(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    before = snapshot(tmp_path)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stderr + result.stdout
    for name, content in before.items():
        assert (tmp_path / name).read_bytes() == content, f"migration changed an input: {name}"
    context, body = current_claim(tmp_path)
    demo, _ = current_claim(tmp_path, DEMO_ID, "product-ui-quality")
    assert context["id"] == "context-composition"
    assert demo["id"] == "runnable-evidence"
    assert context["status"] == demo["status"] == "stable"
    assert "Measure context composition" in body
    assert len(claim_documents(tmp_path)) == 2, "one initial claim per frozen cluster, not one per takeaway"


def test_generated_bundle_meets_okf_and_stricter_project_contract(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    result = run_generator(tmp_path)
    assert result.returncode == 0, result.stderr + result.stdout
    assert_project_bundle(tmp_path)


def test_same_title_clusters_keep_separate_frozen_identities(tmp_path: Path) -> None:
    catalog = seed_corpus(tmp_path)
    for row in catalog["techniques"]:
        row["title"] = "Same display title"
    write_json(tmp_path / "data" / "catalog.json", catalog)
    assert run_generator(tmp_path).returncode == 0
    assert current_claim(tmp_path)[0]["id"] == "context-composition"
    assert current_claim(tmp_path, DEMO_ID, "product-ui-quality")[0]["id"] == "runnable-evidence"
    assert len(claim_documents(tmp_path)) == 2


def test_title_change_cannot_rename_a_frozen_cluster(tmp_path: Path) -> None:
    catalog = seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    next(row for row in catalog["techniques"] if row["id"] == CONTEXT_ID)["title"] = "A renamed display title"
    write_json(tmp_path / "data" / "catalog.json", catalog)
    assert run_generator(tmp_path).returncode == 0
    assert current_claim(tmp_path)[0]["id"] == "context-composition"
    assert not (tmp_path / "kb" / CONTEXT_AREA / "a-renamed-display-title.md").exists()


def test_unknown_publication_time_is_not_retrieval_or_analysis_time(tmp_path: Path) -> None:
    seed_corpus(tmp_path, date=None)
    assert run_generator(tmp_path).returncode == 0
    metadata, _ = current_claim(tmp_path)
    assert metadata["valid_from"] is None
    assert metadata["valid_to"] is None
    assert all(source["last_modified"] is None for source in metadata["sources"])
    assert_project_bundle(tmp_path)


def test_sources_use_video_identity_and_publication_metadata(tmp_path: Path) -> None:
    seed_corpus(tmp_path, date="2025-01-01T01:00:00+01:00")
    assert run_generator(tmp_path).returncode == 0
    metadata, body = current_claim(tmp_path)
    source = next(source for source in metadata["sources"] if source["id"] == CONTEXT_VID)
    assert source["resource"].startswith(f"https://www.youtube.com/watch?v={CONTEXT_VID}")
    assert source["analysis_file"] == f"analysis/{CONTEXT_VID}.json"
    assert source["author"] == "Sam Morrow"
    assert aware_datetime(source["last_modified"]) == aware_datetime("2025-01-01T00:00:00Z")
    assert f"[^{CONTEXT_VID}]" in body
    assert not re.search(r"\[\^\d+\]", body), "positional footnotes are not stable source identities"


def test_verified_timestamped_quote_is_published_but_not_attested(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    metadata, body = current_claim(tmp_path)
    assert "more than 75%" in body
    assert "06:03" in body or "t=363" in body, "a quote must retain its source timestamp"
    assert "verified" not in metadata, "matching a quote is not human review of the generated claim"


def test_unverified_quote_is_not_published_as_evidence(tmp_path: Path) -> None:
    catalog = seed_corpus(tmp_path)
    fabricated = "A fabricated quote absent from every caption fixture."
    row = next(row for row in catalog["techniques"] if row["id"] == CONTEXT_ID)
    row["sources"][0].update(quote=fabricated, quote_verification="not-found-in-captions",
                              requires_confirmation=True, quote_is_verbatim_original=False)
    write_json(tmp_path / "data" / "catalog.json", catalog)
    analysis = json.loads((tmp_path / "analysis" / f"{CONTEXT_VID}.json").read_text())
    analysis["takeaways"][0].update(evidence_quote=fabricated,
                                     evidence_quote_verification="not-found-in-captions")
    write_json(tmp_path / "analysis" / f"{CONTEXT_VID}.json", analysis)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    assert all(fabricated.encode() not in content for content in generated_snapshot(tmp_path).values())


def test_private_mapping_fields_do_not_escape_into_generated_artifacts(tmp_path: Path) -> None:
    catalog = seed_corpus(tmp_path)
    marker = "PRIVATE-APPLICATION-MAPPING-SENTINEL"
    row = next(row for row in catalog["techniques"] if row["id"] == CONTEXT_ID)
    row.update(concrete_change_for_us=marker, our_status=marker, our_status_evidence=[marker])
    row["sources"][0]["origin_path"] = str(Path("/") / "home" / "fixture" / marker)
    write_json(tmp_path / "data" / "catalog.json", catalog)
    analysis_path = tmp_path / "analysis" / f"{CONTEXT_VID}.json"
    analysis = json.loads(analysis_path.read_text())
    analysis["takeaways"][0].update(apply_to_us=marker, expected_effect=marker)
    write_json(analysis_path, analysis)
    before = snapshot(tmp_path)
    result = run_generator(tmp_path)
    if result.returncode != 0:
        # Refusing contaminated input is also safe; silently publishing it is not.
        assert snapshot(tmp_path) == before
        json_report(result)
        return
    current_claim(tmp_path)
    output = b"\n".join(generated_snapshot(tmp_path).values())
    assert marker.encode() not in output
    assert b"our_status" not in output and b"apply_to_us" not in output


@pytest.mark.parametrize("relation,new_date", [
    ("supports", "2025-02-15T00:00:00Z"),
    ("refines", "2025-01-30T00:00:00Z"),
    ("contradicts", "2025-01-30T23:59:59Z"),
    ("refines", "2025-01-31T00:00:00+01:00"),
    ("contradicts", "2024-12-01T00:00:00Z"),
    ("refines", None),
])
def test_supports_or_insufficient_age_never_supersedes(tmp_path: Path, relation: str,
                                                       new_date) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    add_followup(tmp_path, new_date)
    path = proposals(tmp_path, relation)
    result = run_generator(tmp_path, "--relations", str(path))
    assert result.returncode == 0, result.stderr + result.stdout
    metadata, _ = current_claim(tmp_path)
    assert metadata["status"] == "stable"
    assert metadata["superseded_by"] is None and metadata["valid_to"] is None
    assert aware_datetime(metadata["valid_from"]) == aware_datetime(BASE_DATE)
    assert not any(meta["status"] == "deprecated" for _, meta, _ in claim_documents(tmp_path))
    if relation == "supports":
        assert {source["id"] for source in metadata["sources"]} == {CONTEXT_VID, NEW_VID}


@pytest.mark.parametrize("relation", ["refines", "contradicts"])
@pytest.mark.parametrize("old_date,new_date", [
    (BASE_DATE, "2025-01-31T00:00:00Z"),
    ("2025-01-01T00:30:00+01:00", "2025-01-30T23:30:00Z"),
])
def test_thirty_day_refinement_or_contradiction_retains_deprecated_revision(
        tmp_path: Path, relation: str, old_date: str, new_date: str) -> None:
    seed_corpus(tmp_path, date=old_date)
    assert run_generator(tmp_path).returncode == 0
    _, old_body = current_claim(tmp_path)
    add_followup(tmp_path, new_date)
    path = proposals(tmp_path, relation)
    result = run_generator(tmp_path, "--relations", str(path))
    assert result.returncode == 0, result.stderr + result.stdout
    current, _ = current_claim(tmp_path)
    assert current["id"] == "context-composition" and current["status"] == "stable"
    assert aware_datetime(current["valid_from"]) == aware_datetime(new_date)
    assert NEW_VID in {source["id"] for source in current["sources"]}
    deprecated = [(meta, body) for _, meta, body in claim_documents(tmp_path)
                  if meta["status"] == "deprecated"]
    assert len(deprecated) == 1, "the old evidence must be retained as a deprecated revision"
    old, body = deprecated[0]
    assert old["superseded_by"] == current["id"]
    assert aware_datetime(old["valid_from"]) == aware_datetime(old_date)
    assert aware_datetime(old["valid_to"]) == aware_datetime(new_date)
    assert CONTEXT_VID in {source["id"] for source in old["sources"]}
    assert "more than 75%" in old_body and "more than 75%" in body
    log = (tmp_path / "kb" / "log.md").read_text(encoding="utf-8")
    for stable_id in (CONTEXT_ID, CONTEXT_VID, NEW_VID):
        assert stable_id in log, f"supersession log must identify {stable_id}"
    assert_project_bundle(tmp_path)


@pytest.mark.parametrize("new_date", [None, "2025-04-01T00:00:00Z"])
def test_unknown_current_date_cannot_establish_a_thirty_day_delta(tmp_path: Path, new_date) -> None:
    seed_corpus(tmp_path, date=None)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    add_followup(tmp_path, new_date)
    path = proposals(tmp_path, "contradicts")
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    assert not any(meta["status"] == "deprecated" for _, meta, _ in claim_documents(tmp_path))


def test_a_newer_video_alone_is_not_authority_to_supersede(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    add_followup(tmp_path, "2025-04-01T00:00:00Z")
    assert run_generator(tmp_path).returncode == 0
    metadata, _ = current_claim(tmp_path)
    assert metadata["status"] == "stable" and metadata["superseded_by"] is None
    assert aware_datetime(metadata["valid_from"]) == aware_datetime(BASE_DATE)
    assert not any(meta["status"] == "deprecated" for _, meta, _ in claim_documents(tmp_path))


@pytest.mark.parametrize("bad_date", ["2025-04-01", "2025-04-01T00:00:00", "not-a-date"])
def test_invalid_publication_time_is_rejected_or_remains_unknown(tmp_path: Path, bad_date: str) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    add_followup(tmp_path, bad_date)
    path = proposals(tmp_path, "contradicts")
    before = snapshot(tmp_path)
    result = run_generator(tmp_path, "--relations", str(path))
    if result.returncode != 0:
        assert snapshot(tmp_path) == before
        json_report(result)
        return
    current, _ = current_claim(tmp_path)
    assert aware_datetime(current["valid_from"]) == aware_datetime(BASE_DATE)
    assert not any(meta["status"] == "deprecated" for _, meta, _ in claim_documents(tmp_path))
    for source in current["sources"]:
        if source["id"] == NEW_VID:
            assert source["last_modified"] is None
    assert_project_bundle(tmp_path)


def test_current_evidence_not_the_oldest_source_sets_the_thirty_day_threshold(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    add_followup(tmp_path, "2025-01-20T00:00:00Z")
    support = proposals(tmp_path, "supports")
    assert run_generator(tmp_path, "--relations", str(support)).returncode == 0
    # A second follow-up is 35 days after the original, but only 16 after support.
    second_vid = "FOLLOWUP002"
    second = add_followup(tmp_path, "2025-02-05T00:00:00Z")
    second.update(vid=second_vid, source=f"https://www.youtube.com/watch?v={second_vid}")
    write_transcript(tmp_path, second, NEW_QUOTE)
    write_json(tmp_path / "analysis" / f"{second_vid}.json", second)
    # Restore the first follow-up; the two evidence records have distinct dates.
    add_followup(tmp_path, "2025-01-20T00:00:00Z")
    path = proposals(tmp_path, "contradicts", vid=second_vid)
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    metadata, _ = current_claim(tmp_path)
    assert metadata["status"] == "stable" and metadata["superseded_by"] is None
    assert not any(meta["status"] == "deprecated" for _, meta, _ in claim_documents(tmp_path))


def test_read_only_candidates_are_deterministic_catalog_identities(tmp_path: Path) -> None:
    first, second = tmp_path / "first", tmp_path / "second"
    for root, reverse in ((first, False), (second, True)):
        seed_corpus(root, reverse=reverse)
        add_followup(root, "2025-04-01T00:00:00Z")
    reports = []
    for root in (first, second):
        before = snapshot(root)
        result = run_generator(root, "--candidates")
        assert result.returncode == 0, result.stderr + result.stdout
        reports.append(json_report(result))
        assert snapshot(root) == before, "candidate discovery must not mutate sources or publish"
    assert reports[0] == reports[1]
    rows = [row for row in reports[0]["candidates"]
            if row["vid"] == NEW_VID and row["takeaway_index"] == 0]
    assert len(rows) == 1
    assert CONTEXT_ID in rows[0]["candidate_ids"]
    assert set(rows[0]["candidate_ids"]) <= {CONTEXT_ID, DEMO_ID}
    assert DEMO_ID not in rows[0]["candidate_ids"], "an unrelated mechanism is not a candidate"


@pytest.mark.parametrize("mutation", [
    {"relation": "supersedes"},
    {"relation": "new", "catalog_id": "silently-minted-cluster"},
    {"catalog_id": "not-a-frozen-cluster"},
    {"catalog_id": DEMO_ID},
    {"catalog_id": "../../escape"},
    {"vid": "UNKNOWN0001"},
    {"takeaway_index": -1},
    {"takeaway_index": 99},
    {"takeaway_index": True},
])
def test_untrusted_invalid_or_out_of_candidate_relations_are_rejected_atomically(
        tmp_path: Path, mutation: dict) -> None:
    seed_corpus(tmp_path)
    add_followup(tmp_path, "2025-04-01T00:00:00Z")
    path = proposals(tmp_path, **mutation)
    assert_rejected_without_writes(tmp_path, "--relations", str(path))
    assert not (tmp_path.parent / "escape.md").exists()


def test_a_bad_late_proposal_prevents_all_publication(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    add_followup(tmp_path, "2025-04-01T00:00:00Z")
    path = proposals(tmp_path)
    value = json.loads(path.read_text())
    value["proposals"].append({"vid": NEW_VID, "takeaway_index": 0,
                               "catalog_id": "not-a-candidate", "relation": "contradicts"})
    write_json(path, value)
    assert_rejected_without_writes(tmp_path, "--relations", str(path))


@pytest.mark.parametrize("fault", ["duplicate_id", "unsafe_id", "unsafe_area", "missing_catalog"])
def test_catalog_validation_precedes_every_write(tmp_path: Path, fault: str) -> None:
    catalog = seed_corpus(tmp_path)
    path = tmp_path / "data" / "catalog.json"
    if fault == "duplicate_id":
        catalog["techniques"].append(copy.deepcopy(catalog["techniques"][0]))
    elif fault == "unsafe_id":
        catalog["techniques"][0]["id"] = "../../escape"
    elif fault == "unsafe_area":
        catalog["techniques"][0]["area"] = "../../escape"
    if fault == "missing_catalog":
        path.unlink()
    else:
        write_json(path, catalog)
    assert_rejected_without_writes(tmp_path)


def test_migration_is_independent_of_catalog_and_file_creation_order(tmp_path: Path) -> None:
    roots = (tmp_path / "first", tmp_path / "second")
    results = []
    for root, reverse in zip(roots, (False, True)):
        seed_corpus(root, reverse=reverse)
        assert run_generator(root).returncode == 0
        current_claim(root)
        result = []
        for path, metadata, body in claim_documents(root):
            # Fresh runs may have different creation clocks; identity/evidence may not differ.
            metadata = {key: value for key, value in metadata.items()
                        if key not in {"generated", "stale_after"}}
            result.append((str(path.relative_to(root)), metadata, body))
        results.append(result)
    assert results[0] == results[1]


def test_replay_does_not_churn_generated_at_stale_after_or_log(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    before = generated_snapshot(tmp_path)
    # This is a clock-boundary assertion, not a network/CI polling loop.
    time.sleep(1.1)
    assert run_generator(tmp_path).returncode == 0
    assert generated_snapshot(tmp_path) == before, "a check/replay is not a meaningful content change"


def test_replaying_a_supersession_never_duplicates_history_or_log(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    add_followup(tmp_path, "2025-01-31T00:00:00Z")
    path = proposals(tmp_path, "refines")
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    before = generated_snapshot(tmp_path)
    assert run_generator(tmp_path, "--relations", str(path)).returncode == 0
    assert generated_snapshot(tmp_path) == before
    assert len([meta for _, meta, _ in claim_documents(tmp_path) if meta["status"] == "deprecated"]) == 1


def test_preexisting_unreferenced_history_is_never_deleted(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    history = tmp_path / "kb" / "history" / "retained.md"
    history.parent.mkdir(parents=True)
    content = b"---\ntype: technique\nid: retained-history\nstatus: deprecated\n---\n\nRetained evidence.\n"
    history.write_bytes(content)
    result = run_generator(tmp_path)
    assert history.read_bytes() == content, "unreferenced evidence is not garbage to delete"
    if result.returncode != 0:
        # A strict validator may refuse this legacy orphan, but may not erase it.
        json_report(result)


def test_check_mode_is_offline_and_never_repairs_outputs(tmp_path: Path) -> None:
    seed_corpus(tmp_path)
    before = snapshot(tmp_path)
    stale = run_generator(tmp_path, "--check")
    assert stale.returncode != 0, "missing corrected bundle must fail its freshness check"
    assert snapshot(tmp_path) == before
    assert run_generator(tmp_path).returncode == 0
    current_claim(tmp_path)
    before = snapshot(tmp_path)
    fresh = run_generator(tmp_path, "--check")
    assert fresh.returncode == 0, fresh.stderr + fresh.stdout
    assert snapshot(tmp_path) == before
