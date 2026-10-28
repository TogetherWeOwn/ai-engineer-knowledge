"""Independent output oracle, not an import of the generator's own validators.

Upstream: OKF 0.2 SPEC.md at ad30107c31c06aec8a7d5636e0d1058118604e6f
(blob c06e3eede0c910d0ecf12524c34204156f8795ac).

OKF requires parseable concept frontmatter and a nonempty type; reserved
indexes/logs have their own structure. The required lifecycle, provenance,
per-directory indexes, body sections and router below are THIS PROJECT'S
stricter publication contract, not claims about OKF's minimum requirements.
Unknown source dates are nullable project extensions. No content is verified
merely because this structural conformance check passes.
"""

import json
import re
from datetime import date, datetime
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import yaml


RESERVED = {"index.md", "log.md"}
REQUIRED_HEADINGS = ("What", "Evidence", "How to apply (generic)", "Expected effect")


def aware_datetime(value) -> datetime:
    assert value is not None, "expected an aware datetime, not an unknown value"
    if isinstance(value, datetime):
        parsed = value
    else:
        assert isinstance(value, str), f"not an ISO datetime string: {value!r}"
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None and parsed.utcoffset() is not None, (
        f"timezone-naive timestamp: {value!r}"
    )
    return parsed


def read_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
    assert match, f"{path}: missing YAML frontmatter"
    metadata = yaml.safe_load(match.group(1))
    assert isinstance(metadata, dict), f"{path}: frontmatter must be a mapping"
    return metadata, text[match.end():]


def claim_documents(root: Path) -> list[tuple[Path, dict, str]]:
    return [(path, *read_frontmatter(path)) for path in sorted((root / "kb").rglob("*.md"))
            if path.name not in RESERVED]


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", text)


def assert_project_bundle(root: Path) -> None:
    kb = root / "kb"
    assert kb.is_dir(), "corrected generator must produce an OKF bundle under kb/"
    root_index = kb / "index.md"
    assert root_index.is_file(), "project requires the bundle-root index"
    root_metadata, _ = read_frontmatter(root_index)
    assert str(root_metadata.get("okf_version")) == "0.2"

    for directory in [kb, *(p for p in sorted(kb.rglob("*")) if p.is_dir())]:
        index = directory / "index.md"
        assert index.is_file(), f"project requires an index for {directory}"
        index_text = index.read_text(encoding="utf-8")
        if directory != kb:
            assert not index_text.startswith("---"), f"{index}: child indexes have no frontmatter"
        assert re.search(r"^#+\s+\S", index_text, re.M), f"{index}: missing section heading"

    documents = claim_documents(root)
    assert documents, "an empty kb/ does not establish conformance or migration acceptance"
    for path, metadata, body in documents:
        prefix = f"{path.relative_to(root)}: "
        assert isinstance(metadata.get("type"), str) and metadata["type"].strip(), prefix + "missing type"
        assert metadata["type"] == "technique", prefix + "wrong project concept type"
        for key in ("id", "title", "area", "status", "valid_from", "valid_to", "superseded_by",
                    "sources", "generated", "stale_after"):
            assert key in metadata, prefix + f"missing project field {key}"
        assert metadata["status"] in {"stable", "deprecated"}, prefix + "obsolete lifecycle status"
        assert "verified" not in metadata, prefix + "generation is not independent verification"
        for key in ("valid_from", "valid_to"):
            if metadata[key] is not None:
                aware_datetime(metadata[key])
        if metadata["status"] == "stable":
            assert metadata["valid_to"] is None, prefix + "current claim has an end date"
            assert metadata["superseded_by"] is None, prefix + "current claim is superseded"
        else:
            assert metadata["superseded_by"], prefix + "deprecated revision lacks its successor"
        generated = metadata["generated"]
        assert isinstance(generated, dict) and generated.get("by"), prefix + "missing generator attribution"
        aware_datetime(generated.get("at"))
        aware_datetime(metadata["stale_after"])
        for heading in REQUIRED_HEADINGS:
            assert f"## {heading}" in body, prefix + f"missing {heading} section"
        assert "## Apply to us" not in body, prefix + "private application mapping"

        sources = metadata["sources"]
        assert isinstance(sources, list) and sources, prefix + "missing evidence sources"
        ids = []
        for source in sources:
            assert isinstance(source, dict), prefix + "source is not a mapping"
            for key in ("id", "resource", "title", "author", "last_modified", "analysis_file"):
                assert key in source, prefix + f"source missing project field {key}"
            assert isinstance(source["id"], str) and source["id"], prefix + "missing source join key"
            ids.append(source["id"])
            url = urlsplit(source["resource"])
            assert url.scheme == "https" and url.hostname in {"www.youtube.com", "youtube.com"}, prefix + "not a video source"
            assert parse_qs(url.query).get("v") == [source["id"]], prefix + "resource/source ID mismatch"
            analysis_path = root / source["analysis_file"]
            assert analysis_path.is_file(), prefix + "analysis_file is not followable"
            analysis = json.loads(analysis_path.read_text(encoding="utf-8"))
            assert analysis["vid"] == source["id"], prefix + "wrong per-video analysis"
            if source["last_modified"] is not None:
                assert aware_datetime(source["last_modified"]) == aware_datetime(analysis.get("published_at")), (
                    prefix + "source modification time is not its publication date"
                )
            else:
                try:
                    aware_datetime(analysis.get("published_at"))
                except (AssertionError, TypeError, ValueError):
                    pass  # Invalid/naive publication times are unresolved, not known instants.
                else:
                    raise AssertionError(prefix + "known publication date was lost")
        assert len(ids) == len(set(ids)), prefix + "ambiguous duplicate source footnote IDs"
        cited_ids = set(re.findall(r"\[\^([^\]]+)\]", body))
        assert cited_ids == set(ids), prefix + "use source IDs, not positional footnotes"
        assert path.name in (path.parent / "index.md").read_text(encoding="utf-8"), (
            prefix + "concept is missing from its directory index"
        )

    log = kb / "log.md"
    assert log.is_file(), "project requires the supersession log"
    headings = re.findall(r"^##\s+(.+)$", log.read_text(encoding="utf-8"), re.M)
    assert all(re.fullmatch(r"\d{4}-\d{2}-\d{2}", heading) for heading in headings), (
        "OKF log entries are grouped by ISO calendar date"
    )
    dates = [date.fromisoformat(heading) for heading in headings]
    assert dates == sorted(dates, reverse=True), "project requires newest-first log date groups"

    router = root / "llms.txt"
    assert router.is_file(), "site-root router is missing"
    text = router.read_text(encoding="utf-8")
    assert len(text.splitlines()) < 100, "router must remain small"
    links = markdown_links(text)
    assert links and all(urlsplit(link).scheme in {"https", "http"} for link in links), (
        "router links must be absolute URLs"
    )
    assert any(urlsplit(link).path.endswith("/llms-full.txt") for link in links), "router lacks the full text bundle"
    assert any("/kb/" in urlsplit(link).path for link in links), "router lacks bundle indexes"
    assert (root / "llms-full.txt").is_file(), "full bundle must use .txt, not the legacy .md name"
