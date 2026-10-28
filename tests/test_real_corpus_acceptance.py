"""Read-only C13 acceptance gate; fixture-suite green is NOT this gate.

Explicit invocation after generating/backfilling a SCRATCH COPY of the import:
  KB_ACCEPTANCE_ROOT=/path/to/scratch/corpus python3 -m pytest \
      tests/test_real_corpus_acceptance.py -q

Without that opt-in these checks report SKIPPED, not real-corpus acceptance.
They never fetch metadata, run a generator, rewrite the frozen catalog, or
contact any service. The builder owns producing the corrected real bundle.
"""

import hashlib
import json
import os
from pathlib import Path

import pytest

from okf_contract import assert_project_bundle, aware_datetime, claim_documents, read_frontmatter
from test_transcript_conformance import split_header, validate_transcript


FROZEN_ID_DIGEST = "72caeca5055237e6dbd261a741f23aaf01476a9f0093f5340940be981ed920b5"
SOURCE_CATALOG_DIGEST = "1ffb5ee38cfb7d91e0eeb62044c57a20a06684e27b3a75697399f53691afcd81"


@pytest.fixture(scope="module")
def corpus_root() -> Path:
    value = os.environ.get("KB_ACCEPTANCE_ROOT")
    if not value:
        pytest.skip("C13 not run: set KB_ACCEPTANCE_ROOT to a generated/backfilled scratch corpus")
    root = Path(value).resolve()
    assert root.is_dir(), f"acceptance root does not exist: {root}"
    return root


def catalog(root: Path) -> dict:
    path = root / "data" / "catalog.json"
    assert path.is_file(), "real frozen catalog is missing; fixtures cannot establish C13"
    return json.loads(path.read_text(encoding="utf-8"))


def test_real_catalog_retains_all_475_frozen_identities(corpus_root: Path) -> None:
    data = catalog(corpus_root)
    ids = sorted(row["id"] for row in data["techniques"])
    assert len(ids) == len(set(ids)) == 475
    digest = hashlib.sha256(("\n".join(ids) + "\n").encode()).hexdigest()
    assert digest == FROZEN_ID_DIGEST
    assert data["id_list_sha256"] == FROZEN_ID_DIGEST
    # This is the original host-catalog digest, NOT a digest of the public projection.
    assert data["source_catalog_sha256"] == SOURCE_CATALOG_DIGEST
    assert data["frozen"] is True


def test_real_migration_produces_at_least_400_claims_without_losing_catalog_ids(corpus_root: Path) -> None:
    rows = catalog(corpus_root)["techniques"]
    documents = claim_documents(corpus_root)
    assert len(documents) >= 400, f"C13 requires >=400 real claims, found {len(documents)}"
    missing = []
    for row in rows:
        path = corpus_root / "kb" / row["area"] / f"{row['id']}.md"
        if not path.is_file():
            missing.append(row["id"])
            continue
        metadata, _ = read_frontmatter(path)
        assert metadata["id"] == row["id"], f"frozen ID changed in {path}"
    assert not missing, f"real catalog identities missing from migration: {missing}"


def test_real_generated_bundle_meets_identified_okf_and_project_contract(corpus_root: Path) -> None:
    assert_project_bundle(corpus_root)


def test_real_video_publication_coverage_is_at_least_95_percent(corpus_root: Path) -> None:
    by_vid = {}
    for path in sorted((corpus_root / "analysis").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        assert isinstance(data, dict) and isinstance(data.get("vid"), str), f"wrong analysis schema: {path}"
        by_vid.setdefault(data["vid"], []).append(data.get("published_at"))
    assert by_vid, "empty corpus must not pass the publication-date gate"
    dated = 0
    unresolved = []
    for vid, values in sorted(by_vid.items()):
        try:
            instants = [aware_datetime(value) for value in values]
        except (AssertionError, TypeError, ValueError):
            unresolved.append(vid)
            continue
        if len(set(instants)) != 1:
            unresolved.append(vid)
            continue
        dated += 1
    assert dated * 100 >= len(by_vid) * 95, (
        f"dated {dated}/{len(by_vid)} distinct videos; unresolved={unresolved}"
    )


def test_every_real_transcript_keeps_native_or_explicit_machine_provenance(corpus_root: Path) -> None:
    files = sorted((corpus_root / "transcripts").glob("*.txt"))
    assert files, "an empty transcript directory does not establish publication conformance"
    failures = {path.name: problems for path in files if (problems := validate_transcript(path))}
    assert not failures, f"non-conforming real transcripts: {failures}"


def test_real_analysis_transcript_hashes_are_followable_and_match(corpus_root: Path) -> None:
    files = sorted((corpus_root / "analysis").glob("*.json"))
    assert len(files) >= 400, "small fixtures cannot establish real provenance"
    failures = []
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        transcript = corpus_root / data["transcript_file"]
        if not transcript.is_file():
            failures.append(f"{data['vid']}: missing transcript")
            continue
        _, body = split_header(transcript.read_bytes().decode("utf-8"))
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if actual != data["transcript_sha256"]:
            failures.append(f"{data['vid']}: body hash mismatch")
    assert not failures, failures
