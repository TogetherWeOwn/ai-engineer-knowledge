"""Conformance tests for published transcripts.

Contract under test (from the repo docs, not from any implementation):

- One file per video: ``transcripts/<vid>.txt`` carrying a ``#``-comment
  header with the source video URL, the speaker/channel credit, an aware
  ``retrieved_at``, the ``sha256`` of the caption body below the header, and
  the label ``auto/author captions, unverified``. The body is verbatim
  captions. Retrieval time is provenance only, never a publication date.
- The root README carries a takedown note: rights holders open an issue and
  the file is removed.

These tests pin that contract so the upcoming corpus import can be checked
against it. No test uses real captions, keys or the network.
"""

import hashlib
import re
from datetime import datetime
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPTS = ROOT / "transcripts"

UNVERIFIED_LABEL = "auto/author captions, unverified"
WATCH_PREFIX = "https://www.youtube.com/watch?v="


# ---------------------------------------------------------------------------
# Contract validator (the conformance rule itself)
# ---------------------------------------------------------------------------

def split_header(text: str):
    """Split transcript text into (header_lines, body_text)."""
    lines = text.split("\n")
    index = 0
    while index < len(lines) and lines[index].startswith("#"):
        index += 1
    return lines[:index], "\n".join(lines[index:])


def parse_aware(value: str) -> datetime:
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        raise ValueError("timezone-naive datetime")
    return parsed


def validate_transcript(path: Path) -> list:
    """Return a list of contract problems; empty means the file conforms."""
    problems = []
    try:
        text = path.read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return [f"unreadable as utf-8 text: {exc}"]
    header_lines, body = split_header(text)
    header = "\n".join(header_lines)

    source = re.search(r"^#\s*source:\s*(\S+)\s*$", header, re.M)
    if not source:
        problems.append("header lacks a 'source:' line")
    else:
        url = source.group(1)
        if not url.startswith(WATCH_PREFIX):
            problems.append(f"source is not a watch URL: {url}")
        elif url[len(WATCH_PREFIX):] != path.stem:
            problems.append(f"source video {url} does not match filename {path.name}")

    credit = re.search(r"^#\s*(?:speaker|channel):\s*(\S.*)$", header, re.M)
    if not credit:
        problems.append("header lacks speaker/channel credit")

    retrieved = re.search(r"^#\s*retrieved_at:\s*(\S+)\s*$", header, re.M)
    if not retrieved:
        problems.append("header lacks 'retrieved_at:'")
    else:
        try:
            parse_aware(retrieved.group(1))
        except ValueError:
            problems.append(f"retrieved_at is not an aware ISO datetime: {retrieved.group(1)}")

    digest = re.search(r"^#\s*sha256:\s*([0-9a-fA-F]+)\s*$", header, re.M)
    if not digest:
        problems.append("header lacks 'sha256:'")
    elif len(digest.group(1)) != 64:
        problems.append("sha256 is not a 64-character hex digest")
    elif digest.group(1).lower() != hashlib.sha256(body.encode("utf-8")).hexdigest():
        problems.append("sha256 does not match the caption body")

    if UNVERIFIED_LABEL not in header:
        problems.append(f"header lacks the {UNVERIFIED_LABEL!r} label")

    if not body.strip():
        problems.append("caption body is empty")

    return problems


# ---------------------------------------------------------------------------
# Fixture builder
# ---------------------------------------------------------------------------

def transcript_text(vid="VIDDEMO01", body="00:00:01.000 first line\n00:00:02.000 second line",
                    retrieved_at="2026-10-26T12:00:00Z", speaker="Jane Doe",
                    source=None, label=True, digest=None, extra=()):
    header = [
        f"# source: {source or WATCH_PREFIX + vid}",
        f"# speaker: {speaker}",
        f"# retrieved_at: {retrieved_at}",
        "# sha256: PLACEHOLDER",
    ]
    if label:
        header.append(f"# {UNVERIFIED_LABEL}")
    header.extend(extra)
    text = "\n".join(header) + "\n" + body
    _, body_text = split_header(text)
    actual = digest or hashlib.sha256(body_text.encode("utf-8")).hexdigest()
    return text.replace("PLACEHOLDER", actual)


def write_transcript(directory: Path, vid: str, text: str) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{vid}.txt"
    path.write_text(text, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Validator behavior on fixtures
# ---------------------------------------------------------------------------

def test_valid_transcript_conforms(tmp_path: Path) -> None:
    path = write_transcript(tmp_path, "VIDDEMO01", transcript_text())
    assert validate_transcript(path) == []


def test_channel_credit_is_accepted(tmp_path: Path) -> None:
    text = transcript_text().replace("# speaker:", "# channel:")
    path = write_transcript(tmp_path, "VIDDEMO01", text)
    assert validate_transcript(path) == []


BAD_VARIANTS = {
    "missing_source": lambda t: "\n".join(
        line for line in t.split("\n") if not line.startswith("# source:")),
    "non_watch_source": lambda t: t.replace(WATCH_PREFIX, "https://example.com/v/"),
    "source_filename_mismatch": lambda t: t.replace("VIDDEMO01", "VIDOTHER02"),
    "missing_credit": lambda t: "\n".join(
        line for line in t.split("\n") if not line.startswith("# speaker:")),
    "missing_retrieved_at": lambda t: "\n".join(
        line for line in t.split("\n") if not line.startswith("# retrieved_at:")),
    "naive_retrieved_at": lambda t: t.replace("2026-10-26T12:00:00Z", "2026-10-26T12:00:00"),
    "wrong_sha256": lambda t: re.sub(r"# sha256: [0-9a-f]+", "# sha256: " + "0" * 64, t),
    "missing_label": lambda t: "\n".join(
        line for line in t.split("\n") if UNVERIFIED_LABEL not in line),
    "tampered_body": lambda t: t + "\n00:00:03.000 injected line",
    "empty_body": lambda t: t.split("\n00:")[0] + "\n",
}


@pytest.mark.parametrize("case", sorted(BAD_VARIANTS))
def test_broken_transcripts_do_not_conform(tmp_path: Path, case: str) -> None:
    text = BAD_VARIANTS[case](transcript_text())
    path = write_transcript(tmp_path, "VIDDEMO01", text)
    assert validate_transcript(path), f"{case} must be rejected"


# ---------------------------------------------------------------------------
# Repository state
# ---------------------------------------------------------------------------

def test_existing_repo_transcripts_meet_contract() -> None:
    files = sorted(p for p in TRANSCRIPTS.glob("*.txt") if p.is_file())
    failures = {str(p): validate_transcript(p) for p in files}
    failures = {name: problems for name, problems in failures.items() if problems}
    assert not failures, f"non-conforming transcripts: {failures}"


def test_root_readme_has_takedown_note() -> None:
    raw = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    readme = re.sub(r"\s+", " ", raw)
    assert "takedown" in readme, "README must carry a takedown note"
    assert "rights holder" in readme, "takedown note must address rights holders"
    assert "issue" in readme, "takedown note must name opening an issue"


def test_transcripts_readme_documents_format() -> None:
    readme = (TRANSCRIPTS / "README.md").read_text(encoding="utf-8").lower()
    for token in ("source:", "retrieved_at", "sha256", "unverified"):
        assert token in readme, f"transcripts/README.md must document {token}"
