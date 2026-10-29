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


@pytest.mark.parametrize("body, quote", [
    ("[00:01] Improving reliability with these tools.\n",
     "reliability with these tool"),
    ("[00:01] Improving unreliability with these tools.\n",
     "reliability with these tools"),
    ("[00:01] Improving reliability with careful evaluation of all these tools.\n",
     "improving reliability with ... all these tool"),
])
def test_quote_verification_rejects_partial_words(body, quote):
    assert ic.Caption(body).verify(quote) == (None, None)


def test_quote_verification_finds_complete_match_after_partial_match():
    caption = ic.Caption(
        "[00:01] Improving unreliability with these tools.\n"
        "[00:09] Improving reliability with these tools.\n"
    )
    assert caption.verify("reliability with these tools") == ("normalized-exact", "00:09")


def test_catalog_quote_verification_rejects_partial_words():
    captions = {"VIDAAAA0001": ic.Caption("[00:01] Improving unreliability with these tools.\n")}
    source = {"vid": "VIDAAAA0001", "quote": "reliability with these tools",
              "quote_verification": "normalized-exact", "additional_original_excerpts": [
                  {"quote": "reliability with these tools", "timestamp": "00:01"}]}
    projected = ic.project_source(source, ic.Scrubber([]), captions, {})
    assert projected["quote"] is None
    assert projected["quote_verification"] == "not-found-in-published-transcript"
    assert "additional_original_excerpts" not in projected


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


def test_repo_evidence_quotes_match_complete_transcript_words():
    captions = {p.stem: ic.normalize(split_header(p.read_text(encoding="utf-8"))[1])
                for p in REPO_TRANSCRIPTS}
    failures = []

    def check(vid, quote, location, ellipsis=False):
        pieces = re.split(r"\.\.\.|…", quote) if ellipsis else [quote]
        start = 0
        for piece in pieces:
            normalized = ic.normalize(piece)
            if not normalized:
                continue
            match = re.search(r"(?<!\w)" + re.escape(normalized) + r"(?!\w)",
                              captions.get(vid, "")[start:])
            if not match:
                failures.append(location)
                return
            start += match.end()

    for path in REPO_ANALYSES:
        analysis = json.loads(path.read_text(encoding="utf-8"))
        for index, takeaway in enumerate(analysis["takeaways"]):
            quote = takeaway["evidence_quote"]
            method = takeaway["evidence_quote_verification"]
            if method == "not-found-in-captions":
                assert quote is None, (path.name, index)
            else:
                assert method in ("normalized-exact", "ordered-ellipsis-pieces")
                assert isinstance(quote, str) and ic.normalize(quote), (path.name, index)
                check(analysis["vid"], quote, (path.name, index),
                      ellipsis=method == "ordered-ellipsis-pieces")
    if REPO_CATALOG.exists():
        catalog = json.loads(REPO_CATALOG.read_text(encoding="utf-8"))
        for technique in catalog["techniques"]:
            for source in technique["sources"]:
                location = (technique["id"], source["record_id"])
                if source.get("quote") is not None:
                    check(source["vid"], source["quote"], location)
                for excerpt in source.get("additional_original_excerpts", []):
                    check(source["vid"], excerpt["quote"], location)
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


def test_decoded_json_strings_are_scanned_before_any_write(tmp_path):
    src = make_corpus(tmp_path)
    path = src / 'analysis' / 'VIDAAAA0001.json'
    data = json.loads(path.read_text())
    data['talk_summary'] = 'A confidential\nproject was discussed.'
    path.write_text(json.dumps(data))
    out = tmp_path / 'out'
    out.mkdir()
    (out / 'existing.txt').write_text('unchanged')
    before = tree_bytes(out)
    with pytest.raises(ic.ImportError_, match='leak gate'):
        run_import(src, out, private={'deny_regexes': [r'confidential\s+project']})
    assert tree_bytes(out) == before


@pytest.mark.parametrize('damage', ['missing_transcripts', 'missing_analysis', 'empty_transcripts', 'empty_analysis', 'partial_transcripts', 'partial_analysis'])
def test_incomplete_source_never_changes_existing_output(tmp_path, damage):
    src = make_corpus(tmp_path)
    out = tmp_path / 'out'
    run_import(src, out)
    before = tree_bytes(out)
    import shutil
    if damage.startswith('missing_'):
        shutil.rmtree(src / damage.removeprefix('missing_'))
    elif damage.startswith('empty_'):
        directory = src / damage.removeprefix('empty_')
        for path in directory.glob('*.txt' if directory.name == 'transcripts' else '*.json'):
            path.unlink()
    elif damage == 'partial_transcripts':
        (src / 'transcripts' / 'VIDAAAA0001.txt').unlink()
    else:
        (src / 'analysis' / 'VIDAAAA0001.json').unlink()
    with pytest.raises(ic.ImportError_):
        run_import(src, out)
    assert tree_bytes(out) == before


def test_all_held_transcripts_preserve_existing_publication(tmp_path):
    src = make_corpus(tmp_path)
    out = tmp_path / 'out'
    run_import(src, out)
    before = tree_bytes(out)
    with pytest.raises(ic.ImportError_, match='no transcripts eligible for export'):
        run_import(src, out, private={'deny_literals': ['# takedown: rights holders']})
    assert tree_bytes(out) == before


def test_malformed_takeaway_is_reported_without_changing_publication(tmp_path, capsys):
    src = make_corpus(tmp_path)
    out = tmp_path / 'out'
    run_import(src, out)
    before = tree_bytes(out)
    path = src / 'analysis' / 'VIDAAAA0001.json'
    data = json.loads(path.read_text())
    data['takeaways'] = ['not an object']
    path.write_text(json.dumps(data))
    policy = tmp_path / 'policy.json'
    policy.write_text(json.dumps({'deny_literals': ['unrelated forbidden marker']}))
    code = ic.main(['--src', str(src), '--out', str(out), '--exported-at', '2025-10-25T00:00:00Z',
                    '--private-terms', str(policy)])
    error = json.loads(capsys.readouterr().err)
    assert code == 2
    assert error['status'] == 'error'
    assert 'takeaway' in error['error']
    assert tree_bytes(out) == before

@pytest.mark.parametrize("techniques", [[], None, "missing", "truncated", "reordered"])
def test_invalid_source_catalog_preserves_published_tree(tmp_path, techniques):
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    before = tree_bytes(out)
    path = src / "synthesis" / "catalog.json"
    catalog = json.loads(path.read_text(encoding="utf-8"))
    if techniques == "missing":
        del catalog["techniques"]
    elif techniques == "truncated":
        catalog["techniques"] = catalog["techniques"][:1]
    elif techniques == "reordered":
        catalog["techniques"].reverse()
    else:
        catalog["techniques"] = techniques
    path.write_text(json.dumps(catalog), encoding="utf-8")
    with pytest.raises(ic.ImportError_):
        run_import(src, out)
    assert tree_bytes(out) == before

@pytest.mark.parametrize("techniques", [[], None, [{}], [{"id": "", "title": "x", "area": "x"}]])
def test_invalid_catalog_cannot_create_initial_publication(tmp_path, techniques):
    src = make_corpus(tmp_path)
    path = src / "synthesis" / "catalog.json"
    catalog = json.loads(path.read_text(encoding="utf-8"))
    catalog["techniques"] = techniques
    path.write_text(json.dumps(catalog), encoding="utf-8")
    out = tmp_path / "out"
    with pytest.raises(ic.ImportError_):
        run_import(src, out)
    assert tree_bytes(out) == {}


def change_json(path, keys, value):
    data = json.loads(path.read_text(encoding="utf-8"))
    parent = data
    for key in keys[:-1]:
        parent = parent[key]
    parent[keys[-1]] = value
    path.write_text(json.dumps(data), encoding="utf-8")


@pytest.mark.parametrize("keys", [
    ("talk_summary",), ("title",), ("confidence",), ("analyzed_at",),
    ("takeaways", 0, "area"), ("takeaways", 0, "technique"),
    ("takeaways", 0, "what_they_do"), ("takeaways", 0, "numbers"),
    ("takeaways", 0, "confidence"), ("takeaways", 0, "evidence_quote"),
])
@pytest.mark.parametrize("value", [
    {"private_mapping": "The zebracorn initiative advances quietly."},
    ["The zebracorn initiative advances quietly."], 7, True,
])
def test_analysis_field_shapes_cannot_bypass_privacy(tmp_path, capsys, keys, value):
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    before = tree_bytes(out)
    change_json(src / "analysis" / "VIDAAAA0001.json", keys, value)
    policy = tmp_path / "policy.json"
    policy.write_text(json.dumps({"sentence_terms": ["zebracorn"]}))
    assert ic.main(["--src", str(src), "--out", str(out), "--exported-at", "2025-10-25T00:00:00Z",
                    "--private-terms", str(policy)]) == 2
    assert json.loads(capsys.readouterr().err)["status"] == "error"
    assert tree_bytes(out) == before


@pytest.mark.parametrize("keys", [
    ("techniques", 0, "mechanism", "summary"),
    ("techniques", 0, "mechanism", "representative_explanation"),
    ("techniques", 0, "mechanism", "variants", 0, "title"),
    ("techniques", 0, "reported_measurements", 0, "text"),
    ("techniques", 0, "expected_benefit", "cost"),
    ("techniques", 0, "risk", "mitigation"),
    ("techniques", 0, "risk", "failure_modes"),
    ("techniques", 0, "how_to_measure_success", "metrics"),
    ("techniques", 0, "how_to_measure_success", "acceptance"),
    ("techniques", 0, "sources", 0, "input_technique"),
    ("techniques", 0, "sources", 0, "mechanism_in_source"),
    ("scope", "source_scope"), ("validation", "verified"),
])
def test_catalog_prose_field_shapes_cannot_bypass_privacy(tmp_path, keys):
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    before = tree_bytes(out)
    change_json(src / "synthesis" / "catalog.json", keys,
                {"private_mapping": "The zebracorn initiative advances quietly."})
    with pytest.raises(ic.ImportError_):
        run_import(src, out, private={"sentence_terms": ["zebracorn"]})
    assert tree_bytes(out) == before


def test_string_private_sentence_is_still_scrubbed(tmp_path):
    src = make_corpus(tmp_path)
    change_json(src / "analysis" / "VIDAAAA0001.json", ("talk_summary",),
                "The zebracorn initiative advances quietly.")
    out = tmp_path / "out"
    run_import(src, out, private={"sentence_terms": ["zebracorn"]})
    assert json.loads((out / "analysis" / "VIDAAAA0001.json").read_text())["talk_summary"] is None


@pytest.mark.parametrize("field", ["sentence_terms", "deny_regexes", "deny_literals"])
@pytest.mark.parametrize("value", ["zebracorn", {"zebracorn": True}, 9, True, None,
                                  [""], ["   "], [7], [None], [False], [[]], [{}],
                                  ["valid", ""]])
def test_malformed_policy_is_rejected_before_any_write(tmp_path, capsys, field, value):
    src = make_corpus(tmp_path)
    change_json(src / "analysis" / "VIDAAAA0001.json", ("talk_summary",),
                "The zebracorn initiative advances quietly.")
    out = tmp_path / "out"
    run_import(src, out)
    before = tree_bytes(out)
    policy = tmp_path / "policy.json"
    # A valid second field must not mask a malformed/empty entry in this one.
    data = {"deny_literals": ["unrelated forbidden marker"]}
    data[field] = value
    policy.write_text(json.dumps(data))
    assert ic.main(["--src", str(src), "--out", str(out), "--exported-at", "2025-10-25T00:00:00Z",
                    "--private-terms", str(policy)]) == 2
    error = json.loads(capsys.readouterr().err)
    assert error["status"] == "error"
    assert "--private-terms" in error["error"] and field in error["error"]
    assert tree_bytes(out) == before


@pytest.mark.parametrize("key", ["sentence_term", "Sentence_terms", "deny_literal", "extra"])
def test_unknown_policy_key_is_rejected_before_any_write(tmp_path, capsys, key):
    # A misspelled rule must not be silently ignored while a valid sibling satisfies the check.
    src = make_corpus(tmp_path)
    change_json(src / "analysis" / "VIDAAAA0001.json", ("talk_summary",),
                "The zebracorn initiative advances quietly.")
    out = tmp_path / "out"
    run_import(src, out)
    before = tree_bytes(out)
    policy = tmp_path / "policy.json"
    policy.write_text(json.dumps({"deny_literals": ["unrelated forbidden marker"], key: ["zebracorn"]}))
    assert ic.main(["--src", str(src), "--out", str(out), "--exported-at", "2025-10-25T00:00:00Z",
                    "--private-terms", str(policy)]) == 2
    error = json.loads(capsys.readouterr().err)
    assert error["status"] == "error"
    assert "--private-terms" in error["error"] and key in error["error"]
    assert tree_bytes(out) == before


def test_non_string_manifest_model_is_ignored(tmp_path):
    manifest = tmp_path / "manifest.jsonl"
    manifest.write_text("\n".join([
        json.dumps({"id": "a", "ok": True, "model": {"name": "large"}}),
        json.dumps({"id": "b", "ok": True, "model": "large-v3"}),
        json.dumps(["not", "an", "object"]),
    ]))
    assert ic.load_manifest_models(manifest) == {"b": "large-v3"}


def test_invalid_policy_regex_is_a_clean_cli_error(tmp_path, capsys):
    src = make_corpus(tmp_path)
    policy = tmp_path / "policy.json"
    policy.write_text(json.dumps({"deny_regexes": ["["]}))
    out = tmp_path / "out"
    assert ic.main(["--src", str(src), "--out", str(out), "--exported-at", "2025-10-25T00:00:00Z",
                    "--private-terms", str(policy)]) == 2
    assert json.loads(capsys.readouterr().err)["status"] == "error"
    assert tree_bytes(out) == {}


@pytest.mark.parametrize("damage", ["truncated", "not-object", "unreadable", "invalid-date-type"])
def test_unreadable_existing_metadata_is_not_treated_as_absent(tmp_path, monkeypatch, capsys, damage):
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    path = out / "analysis" / "VIDAAAA0001.json"
    if damage == "truncated":
        path.write_text('{"published_at":')
    elif damage == "not-object":
        path.write_text('[]')
    elif damage == "invalid-date-type":
        change_json(path, ("published_at",), {"date": "2025-06-01T12:00:00Z"})
    before = tree_bytes(out)
    original_read = Path.read_text

    def fail_read(self, *args, **kwargs):
        if damage == "unreadable" and self == path:
            raise PermissionError("injected unreadable existing analysis")
        return original_read(self, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", fail_read)
    policy = tmp_path / "policy.json"
    policy.write_text(json.dumps({"deny_literals": ["unrelated forbidden marker"]}))
    assert ic.main(["--src", str(src), "--out", str(out), "--exported-at", "2025-10-25T00:00:00Z",
                    "--private-terms", str(policy)]) == 2
    assert json.loads(capsys.readouterr().err)["status"] == "error"
    assert tree_bytes(out) == before


@pytest.mark.parametrize("failure", ["raise", "short-count"])
def test_partial_write_preserves_backfilled_metadata_and_cleans_temp(tmp_path, monkeypatch, capsys, failure):
    import builtins
    import io

    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    path = out / "analysis" / "VIDAAAA0001.json"
    change_json(path, ("published_at",), "2025-06-01T12:00:00Z")
    before = tree_bytes(out)
    original_open = builtins.open
    original_io_open = io.open
    failed = False

    class ShortWrite:
        def __init__(self, handle):
            self.handle = handle

        def __enter__(self):
            self.handle.__enter__()
            return self

        def __exit__(self, *args):
            return self.handle.__exit__(*args)

        def __getattr__(self, name):
            return getattr(self.handle, name)

        def write(self, text):
            nonlocal failed
            if not failed:
                failed = True
                self.handle.write(text[:12])
                self.handle.flush()
                if failure == "raise":
                    raise OSError("injected short write")
                return 12
            return self.handle.write(text)

    def intercepted(opener):
        def open_file(file, mode="r", *args, **kwargs):
            handle = opener(file, mode, *args, **kwargs)
            # Match the sibling temp too, rather than prescribing its name.
            destination = Path(os.readlink(f"/proc/self/fd/{handle.fileno()}"))
            if destination.parent == path.parent and any(c in mode for c in "wax"):
                return ShortWrite(handle)
            return handle
        return open_file

    policy = tmp_path / "policy.json"
    policy.write_text(json.dumps({"deny_literals": ["unrelated forbidden marker"]}))
    with monkeypatch.context() as patch:
        patch.setattr(builtins, "open", intercepted(original_open))
        patch.setattr(io, "open", intercepted(original_io_open))
        code = ic.main(["--src", str(src), "--out", str(out), "--exported-at", "2025-10-25T00:00:00Z",
                        "--private-terms", str(policy)])
    assert failed, "Fault must reach a real output write"
    assert code == 2
    assert json.loads(capsys.readouterr().err)["status"] == "error"
    assert tree_bytes(out) == before, "A failed file write must not truncate an existing publication or leave temp files"
    run_import(src, out)
    assert json.loads(path.read_text())["published_at"] == "2025-06-01T12:00:00Z"


def test_selective_hold_rerun_removes_both_previously_public_files(tmp_path):
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    held_transcript = out / "transcripts" / "VIDAAAA0001.txt"
    held_analysis = out / "analysis" / "VIDAAAA0001.json"
    assert held_transcript.is_file() and held_analysis.is_file()
    retained = out / "transcripts" / "-VIDBBBB002.txt"
    retained_bytes = retained.read_bytes()
    report = run_import(src, out, private={"deny_literals": ["seventy five"]})
    assert report["status"] == "ok" and report["transcripts"] == 1
    assert "leak gate" in report["held"]["VIDAAAA0001"]
    assert not held_transcript.exists()
    assert not held_analysis.exists()
    assert retained.read_bytes() == retained_bytes
    catalog = json.loads((out / "data" / "catalog.json").read_text())
    assert all(s["transcript_file"] is None for t in catalog["techniques"] for s in t["sources"])


def test_source_publication_date_cannot_override_backfilled_date(tmp_path):
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    target = out / "analysis" / "VIDAAAA0001.json"
    change_json(target, ("published_at",), "2025-06-01T12:00:00Z")
    change_json(src / "analysis" / "VIDAAAA0001.json", ("published_at",), "2099-01-01T00:00:00Z")
    run_import(src, out)
    assert json.loads(target.read_text())["published_at"] == "2025-06-01T12:00:00Z"


def test_source_publication_date_cannot_inject_fresh_import_date(tmp_path):
    src = make_corpus(tmp_path)
    change_json(src / "analysis" / "VIDAAAA0001.json", ("published_at",), "2099-01-01T00:00:00Z")
    out = tmp_path / "out"
    run_import(src, out)
    assert "published_at" not in json.loads((out / "analysis" / "VIDAAAA0001.json").read_text())


def test_imported_machine_transcript_conforms_to_documented_provenance(tmp_path):
    from test_transcript_conformance import validate_transcript

    out = tmp_path / "out"
    run_import(make_corpus(tmp_path), out, include_machine=True)
    path = out / "transcripts" / "VIDWHSP0003.txt"
    assert validate_transcript(path) == []
    fields = header_fields(split_header(path.read_text())[0])
    assert fields["caption_track"] == "none"


@pytest.mark.parametrize("keys, value", [
    (("truncated",), {"private_mapping": "zebracorn"}),
    (("takeaways",), {"private_mapping": "zebracorn"}),
])
def test_analysis_container_shapes_are_validated(tmp_path, keys, value):
    src = make_corpus(tmp_path)
    change_json(src / "analysis" / "VIDAAAA0001.json", keys, value)
    out = tmp_path / "out"
    with pytest.raises(ic.ImportError_):
        run_import(src, out)
    assert tree_bytes(out) == {}


@pytest.mark.parametrize("keys", [
    ("title",), ("schema_version",), ("generated_at",), ("areas",),
    ("counts", "raw_input_records"), ("validation", "independent_checks"),
    ("techniques", 0, "source"), ("techniques", 0, "source_count"),
    ("techniques", 0, "quote_evidence", "normalized-exact"),
    ("techniques", 0, "mechanism", "representative_record_id"),
    ("techniques", 0, "mechanism", "variants", 0, "source_record_ids"),
    ("techniques", 0, "risk", "level"),
    ("techniques", 0, "reported_measurements", 0, "source_record_ids"),
    ("techniques", 0, "sources", 0, "record_id"),
    ("techniques", 0, "sources", 0, "talk"),
    ("techniques", 0, "sources", 0, "input_area"),
    ("techniques", 0, "sources", 0, "matching_occurrences"),
    ("techniques", 0, "sources", 0, "requires_confirmation"),
    ("methodology", "loading"),
])
def test_catalog_metadata_shapes_cannot_smuggle_nested_prose(tmp_path, keys):
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    before = tree_bytes(out)
    change_json(src / "synthesis" / "catalog.json", keys,
                {"private_mapping": "The zebracorn initiative advances quietly."})
    with pytest.raises(ic.ImportError_):
        run_import(src, out, private={"sentence_terms": ["zebracorn"]})
    assert tree_bytes(out) == before


def test_structured_methodology_is_allowlisted_recursively(tmp_path):
    src = make_corpus(tmp_path)
    change_json(src / "synthesis" / "catalog.json", ("methodology", "classification_review"),
                {"manual_assignment_changes": 2, "private_mapping": "A sensitive mapping.",
                 "assignment_methods": {"manual-semantic-review": 3, "private_mapping": 99}})
    out = tmp_path / "out"
    run_import(src, out)
    review = json.loads((out / "data" / "catalog.json").read_text())["methodology"]["classification_review"]
    assert review == {"manual_assignment_changes": 2, "assignment_methods": {"manual-semantic-review": 3}}



def test_failed_atomic_replace_preserves_backfilled_analysis(tmp_path, monkeypatch):
    src = make_corpus(tmp_path)
    out = tmp_path / "out"
    run_import(src, out)
    target = out / "analysis" / "VIDAAAA0001.json"
    change_json(target, ("published_at",), "2025-06-01T12:00:00Z")
    before = tree_bytes(out)
    attempted = []
    replace = os.replace

    def fail_replace(source, destination):
        if Path(destination) == target:
            attempted.append(Path(source))
            assert Path(source).parent == target.parent
            # The complete serialized document exists before replacement.
            assert json.loads(Path(source).read_text())["published_at"] == "2025-06-01T12:00:00Z"
            raise OSError("injected replace failure")
        return replace(source, destination)

    with monkeypatch.context() as patch:
        patch.setattr(os, "replace", fail_replace)
        with pytest.raises(OSError, match="injected replace failure"):
            run_import(src, out)
    assert len(attempted) == 1
    assert not attempted[0].exists()
    assert tree_bytes(out) == before
    run_import(src, out)
    assert json.loads(target.read_text())["published_at"] == "2025-06-01T12:00:00Z"


@pytest.mark.parametrize("raw", [[], "not an object", None])
def test_non_object_analysis_is_a_clean_error_before_writes(tmp_path, capsys, raw):
    src = make_corpus(tmp_path)
    (src / "analysis" / "VIDAAAA0001.json").write_text(json.dumps(raw))
    policy = tmp_path / "policy.json"
    policy.write_text(json.dumps({"sentence_terms": ["zebracorn"]}))
    out = tmp_path / "out"
    assert ic.main(["--src", str(src), "--out", str(out), "--exported-at", "2025-10-25T00:00:00Z",
                    "--private-terms", str(policy)]) == 2
    assert json.loads(capsys.readouterr().err)["status"] == "error"
    assert tree_bytes(out) == {}
