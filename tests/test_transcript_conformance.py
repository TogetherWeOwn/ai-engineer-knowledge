"""Conformance tests for published transcripts.

Contract under test (from the repo docs, not from any implementation):

- One file per video: ``transcripts/<vid>.txt`` carrying a ``#``-comment
  header with the source video URL, the speaker/channel credit, an aware
  ``retrieved_at``, the ``sha256`` of the caption body below the header, and
  the label ``auto/author captions, unverified``. The body is verbatim
  captions. When YouTube has no captions, the explicit
  ``machine transcript (Whisper; no YouTube captions)`` exception is allowed,
  still unverified and never presented as a native-caption reference.
  Retrieval time is provenance only, never a publication date.
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
MACHINE_LABEL = "machine transcript (Whisper; no YouTube captions)"


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
    fields = []
    for line in header_lines:
        key, separator, _ = line[1:].strip().partition(":")
        if separator:
            fields.append(key.strip())
    if len(fields) != len(set(fields)):
        problems.append("header fields must not be duplicated")

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

    native_labels = list(re.finditer(rf"^#[ \t]*{re.escape(UNVERIFIED_LABEL)}[ \t]*$", header, re.M))
    machine_labels = list(re.finditer(
        rf"^#[ \t]*{re.escape(MACHINE_LABEL)}(?P<unverified>,[ \t]*unverified)?[ \t]*$",
        header, re.M,
    ))
    recognized_machine_lines = {match.group(0) for match in machine_labels}
    if any(line[1:].strip().casefold().startswith("machine transcript")
           and line not in recognized_machine_lines for line in header_lines):
        problems.append("unrecognized machine transcript marker")
    native = native_labels[0] if native_labels else None
    machine = machine_labels[0] if machine_labels else None
    if len(native_labels) + len(machine_labels) > 1:
        problems.append("header must contain exactly one provenance label")
    if machine:
        if native:
            problems.append("machine transcript must not also claim to be native captions")
        if not machine.group("unverified") and not re.search(
                r"^#\s*unverified\s*$", header, re.M):
            problems.append("machine transcript must remain explicitly unverified")
        track = re.search(r"^#\s*caption_track:\s*(\S.*)$", header, re.M)
        if track and track.group(1).strip().lower() != "none":
            problems.append("machine transcript must not claim a YouTube caption track")
    elif not native:
        problems.append(f"header lacks the {UNVERIFIED_LABEL!r} label or no-captions exception")

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


def machine_transcript_text(*, inline_unverified=True):
    label = f"# {MACHINE_LABEL}"
    extra = [label + ", unverified"] if inline_unverified else [label, "# unverified"]
    return transcript_text(vid="ySYLsoAhXmg", label=False,
                           extra=(*extra, "# caption_track: none"))


@pytest.mark.parametrize("inline_unverified", [True, False])
def test_no_captions_machine_transcript_conforms(tmp_path: Path,
                                                inline_unverified: bool) -> None:
    text = machine_transcript_text(inline_unverified=inline_unverified)
    path = write_transcript(tmp_path, "ySYLsoAhXmg", text)
    assert validate_transcript(path) == []


def test_machine_transcript_must_still_be_unverified(tmp_path: Path) -> None:
    text = machine_transcript_text().replace(", unverified", "")
    path = write_transcript(tmp_path, "ySYLsoAhXmg", text)
    assert validate_transcript(path), "machine output is not verified evidence"


@pytest.mark.parametrize("track", ["auto", "native", "manual"])
def test_machine_transcript_must_not_claim_a_caption_track(tmp_path: Path,
                                                          track: str) -> None:
    text = machine_transcript_text().replace("caption_track: none", f"caption_track: {track}")
    path = write_transcript(tmp_path, "ySYLsoAhXmg", text)
    assert validate_transcript(path), "machine output must not masquerade as captions"


def test_machine_and_native_caption_labels_are_mutually_exclusive(tmp_path: Path) -> None:
    text = machine_transcript_text().replace(
        "# caption_track: none", f"# {UNVERIFIED_LABEL}\n# caption_track: none")
    path = write_transcript(tmp_path, "ySYLsoAhXmg", text)
    assert validate_transcript(path), "a machine transcript is not a native-caption reference"


@pytest.mark.parametrize("field", ["source", "speaker", "retrieved_at", "sha256"])
def test_machine_exception_keeps_provenance_required(tmp_path: Path, field: str) -> None:
    text = "\n".join(line for line in machine_transcript_text().split("\n")
                     if not line.startswith(f"# {field}:"))
    path = write_transcript(tmp_path, "ySYLsoAhXmg", text)
    assert validate_transcript(path), f"machine exception must not drop {field}"


def test_machine_transcript_body_hash_is_checked(tmp_path: Path) -> None:
    text = machine_transcript_text() + "\n00:00:03.000 tampered text"
    path = write_transcript(tmp_path, "ySYLsoAhXmg", text)
    assert validate_transcript(path)


def test_generic_machine_label_is_not_the_no_captions_exception(tmp_path: Path) -> None:
    text = machine_transcript_text().replace(MACHINE_LABEL, "machine transcript")
    path = write_transcript(tmp_path, "ySYLsoAhXmg", text)
    assert validate_transcript(path)


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


@pytest.mark.parametrize('machine', [False, True])
def test_duplicate_provenance_labels_are_rejected(tmp_path, machine):
    if machine:
        text = machine_transcript_text().replace(
            f'# {MACHINE_LABEL}, unverified',
            f'# {MACHINE_LABEL}, unverified\n# {MACHINE_LABEL}, unverified')
        vid = 'ySYLsoAhXmg'
    else:
        text = transcript_text(extra=(f'# {UNVERIFIED_LABEL}',))
        vid = 'VIDDEMO01'
    assert validate_transcript(write_transcript(tmp_path, vid, text))
