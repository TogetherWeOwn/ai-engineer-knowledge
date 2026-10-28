"""Frozen-catalog migration, deterministic candidates, and validated publication.

All inputs, persisted relation decisions and output paths are validated before
writing anything. Rejected requests have no side effects. Successful publication
replaces individual files atomically, not the entire directory transactionally;
use one writer and rerun --check after an interrupted filesystem operation.

Only allowlisted generic content is projected. Quotes require both a permitted
verification label and an independent match against the actual caption body.
"""

from __future__ import annotations

import copy
import hashlib
import json
import math
import os
import re
import tempfile
import unicodedata
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

SAFE_COMPONENT = re.compile(r"[a-z0-9][a-z0-9-]{0,127}")
SAFE_VID = re.compile(r"[A-Za-z0-9_-]{1,64}")
RELATIONS = {"supports", "refines", "contradicts"}
PROPOSAL_KEYS = {"vid", "takeaway_index", "catalog_id", "relation"}
GENERATOR = "scripts/generate_claims.py"
BASE_URL = "https://togetherweown.github.io/ai-engineer-knowledge"
NOT_STATED = "_Not stated in the source analysis._"
STOP_WORDS = set("a an and are as at be by for from how in into is it its of on or the their this to use using with without".split())
PRIVATE_TEXT = re.compile(r"/home/|/root/|\bTOG-\d+\b|\bour_status\b|\bapply_to_us\b")


class PublicationError(Exception):
    """A safe, stable validation error; never include arbitrary source text."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


def require(condition: bool, code: str, message: str) -> None:
    if not condition:
        raise PublicationError(code, message)


def safe_path(root: Path, relative: str) -> Path:
    """No traversal or symlinked inputs/output ancestors, including leaf files."""
    path = Path(relative)
    require(not path.is_absolute() and bool(path.parts) and
            all(part not in {".", ".."} for part in path.parts),
            "unsafe_path", "Bundle paths must be relative and contained.")
    current = root
    for part in path.parts:
        current = current / part
        require(not current.is_symlink(), "unsafe_path", "Symlinks are not publication inputs or targets.")
    return current


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError):
        raise PublicationError("invalid_json", "Input must be valid UTF-8 JSON.") from None


def instant(value) -> datetime | None:
    """Only aware publication instants; never infer from retrieval or dates."""
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            return None
        return parsed.astimezone(timezone.utc)
    except (ValueError, OverflowError):
        return None


def iso(value: datetime | None) -> str | None:
    return value.isoformat().replace("+00:00", "Z") if value else None


def public_text(value, default: str = "") -> str:
    """Project only selected generic fields; fail closed on obvious private prose."""
    if not isinstance(value, str):
        return default
    require(not PRIVATE_TEXT.search(value), "private_content", "Selected prose contains private application data.")
    return value.strip()


def normalized(value: str) -> str:
    return " ".join(re.findall(r"[^\W_]+", unicodedata.normalize("NFKC", value).casefold()))


def tokens(value: str) -> set[str]:
    return set(normalized(value).split()) - STOP_WORDS


def timestamp_seconds(value: str) -> int:
    seconds = 0
    for component in value.split(":"):
        seconds = seconds * 60 + int(component)
    return seconds


def load_catalog(root: Path, payloads: list[tuple[str, object]]) -> list[dict] | None:
    data_path = safe_path(root, "data/catalog.json")
    root_path = safe_path(root, "catalog.json")
    if data_path.is_file():
        payload = load_json(data_path)
    elif root_path.is_file():
        payload = load_json(root_path)
        if isinstance(payload, dict) and "techniques" not in payload:
            payload = None
    else:
        payload = None
    real_input = any(isinstance(data, dict) and ("vid" in data or "takeaways" in data)
                     for _, data in payloads)
    if payload is None:
        require(not real_input, "missing_catalog", "Real analyses require a frozen source catalog.")
        identified_legacy = any(isinstance(data, dict) and
                                ("video_id" in data or "video_url" in data) for _, data in payloads)
        require(not payloads or identified_legacy, "unidentified_analysis_schema",
                "Unidentified or corrupt analyses cannot select the legacy publication adapter.")
        return None
    require(isinstance(payload, dict) and isinstance(payload.get("techniques"), list)
            and bool(payload["techniques"]), "invalid_catalog", "Catalog requires nonempty technique rows.")
    rows, seen = [], set()
    for row in payload["techniques"]:
        require(isinstance(row, dict), "invalid_catalog", "Each catalog row must be an object.")
        identity, area = row.get("id"), row.get("area")
        require(isinstance(identity, str) and SAFE_COMPONENT.fullmatch(identity) is not None
                and isinstance(area, str) and SAFE_COMPONENT.fullmatch(area) is not None,
                "unsafe_catalog_identity", "Catalog IDs and areas must be safe path components.")
        require(identity not in seen, "duplicate_catalog_id", "Catalog IDs must be unique.")
        require(identity not in {"index", "log"} and area != "history", "reserved_catalog_identity",
                "Catalog identities may not collide with reserved bundle paths.")
        seen.add(identity)
        require(isinstance(row.get("title"), str) and bool(row["title"].strip()),
                "invalid_catalog", "Catalog rows need display titles.")
        require(isinstance(row.get("sources"), list) and bool(row["sources"]),
                "invalid_catalog", "Catalog rows need evidence sources.")
        mechanism = row.get("mechanism", {})
        require(isinstance(mechanism, dict), "invalid_catalog", "Mechanism must be an object.")
        variants = mechanism.get("variants", [])
        require(isinstance(variants, list) and all(isinstance(variant, dict) for variant in variants),
                "invalid_catalog", "Mechanism variants must be a list of objects.")
        for source in row["sources"]:
            require(isinstance(source, dict) and isinstance(source.get("vid"), str)
                    and SAFE_VID.fullmatch(source["vid"]) is not None
                    and isinstance(source.get("record_id", ""), str),
                    "invalid_catalog_source", "Catalog sources need safe video and record identities.")
        rows.append(row)
    return sorted(rows, key=lambda row: row["id"])


def load_analyses(payloads: list[tuple[str, object]]) -> dict[str, dict]:
    result = {}
    for relative, payload in payloads:
        require(isinstance(payload, dict) and isinstance(payload.get("vid"), str)
                and SAFE_VID.fullmatch(payload["vid"]) is not None,
                "invalid_analysis", "Real analyses require a safe vid field.")
        vid = payload["vid"]
        require(vid not in result, "duplicate_analysis_id", "One analysis per video identity is required.")
        require(isinstance(payload.get("takeaways"), list) and
                all(isinstance(row, dict) for row in payload["takeaways"]),
                "invalid_analysis", "Analysis takeaways must be a list of objects.")
        result[vid] = {"payload": payload, "file": relative}
    return result


class Evidence:
    """Read-only analysis/transcript join and independently checked quote projection."""

    def __init__(self, root: Path, analyses: dict[str, dict]):
        self.root = root
        self.analyses = analyses
        self.transcripts: dict[str, tuple[dict, str]] = {}

    def transcript(self, vid: str) -> tuple[dict, str]:
        if vid not in self.transcripts:
            analysis = self.analyses[vid]["payload"]
            relative = analysis.get("transcript_file", f"transcripts/{vid}.txt")
            require(isinstance(relative, str) and relative.startswith("transcripts/"),
                    "invalid_transcript_path", "Transcript references must stay under transcripts/.")
            path = safe_path(self.root, relative)
            require(path.is_file(), "missing_transcript", "Every evidence source needs its referenced transcript.")
            # Hash the exact UTF-8 body, including newlines, before normalization.
            # read_text() would silently translate CRLF and hide byte changes.
            lines = path.read_bytes().decode("utf-8").split("\n")
            header, body, spans = {}, [], defaultdict(list)
            index = 0
            while index < len(lines) and lines[index].startswith("#"):
                line = lines[index].rstrip("\r")
                key, sep, value = line[1:].strip().partition(":")
                if sep:
                    key = key.strip()
                    require(key not in header, "ambiguous_transcript_header",
                            "Transcript header fields must not be duplicated.")
                    header[key] = value.strip()
                if line == "# auto/author captions, unverified":
                    header["native_labels"] = header.get("native_labels", 0) + 1
                if line[1:].strip().casefold().startswith("machine transcript"):
                    header["machine"] = True
                index += 1
            require(header.get("source") == f"https://www.youtube.com/watch?v={vid}",
                    "transcript_source_mismatch", "Transcript source must match its analysis video identity.")
            digest = hashlib.sha256("\n".join(lines[index:]).encode("utf-8")).hexdigest()
            for recorded in (header.get("sha256"), analysis.get("transcript_sha256")):
                require(isinstance(recorded, str) and re.fullmatch(r"[0-9a-fA-F]{64}", recorded) is not None
                        and recorded.lower() == digest, "transcript_hash_mismatch",
                        "Transcript body must match both header and analysis SHA256 values.")
            offset, current_time = 0, None
            for line in lines[index:]:
                match = re.match(r"^\[(\d+(?::[0-5]\d){1,2})\]\s*", line)
                if match:
                    current_time = timestamp_seconds(match.group(1))
                    line = line[match.end():]
                text = normalized(line)
                if text:
                    if body:
                        offset += 1  # Normalized lines are joined with one space.
                    spans[current_time].append((offset, offset + len(text)))
                    body.append(text)
                    offset += len(text)
            header["timestamp_spans"] = spans
            self.transcripts[vid] = header, " ".join(body)
        return self.transcripts[vid]

    def source(self, vid: str) -> dict:
        require(vid in self.analyses, "missing_source_analysis", "Every source must join a real analysis.")
        record = self.analyses[vid]
        payload = record["payload"]
        header, _ = self.transcript(vid)
        return {"id": vid, "resource": f"https://www.youtube.com/watch?v={vid}",
                "title": public_text(payload.get("title")) or None,
                "author": public_text(header.get("speaker") or payload.get("speaker") or payload.get("author")) or None,
                "last_modified": iso(instant(payload.get("published_at"))),
                "analysis_file": record["file"]}

    def quote(self, vid: str, record: dict, *, takeaway=False) -> str | None:
        quote_key, verification_key, timestamp_key = (
            ("evidence_quote", "evidence_quote_verification", "evidence_timestamp") if takeaway
            else ("quote", "quote_verification", "timestamp"))
        label = record.get(verification_key)
        if (not isinstance(label, str) or label not in {"normalized-exact", "ordered-ellipsis-pieces", "manual-original-excerpt"}
                or record.get("requires_confirmation") or record.get("quote_is_verbatim_original") is False):
            return None
        quote = record.get(quote_key)
        timestamp = record.get(timestamp_key)
        # Short excerpts only: a verification label does not authorize copying
        # an entire talk into a claim. Withhold, never truncate or paraphrase.
        if (not isinstance(quote, str) or not quote.strip() or len(quote) > 500
                or len(quote.split()) > 50 or not isinstance(timestamp, str)):
            return None
        if not re.fullmatch(r"\d+(?::[0-5]\d){1,2}", timestamp):
            return None
        header, body = self.transcript(vid)
        # A hash or a machine transcript is not independent verification of audio.
        if header.get("native_labels") != 1 or header.get("machine"):
            return None
        pieces = re.split(r"\.{3}|…", quote) if label == "ordered-ellipsis-pieces" else [quote]
        pieces = [normalized(piece) for piece in pieces if normalized(piece)]
        if not pieces:
            return None
        # Every piece must fit inside the declared timestamp's segment, not
        # merely start there. Adjacent continuation lines share that segment;
        # repeated timestamp values separated by another segment do not.
        spans = []
        for lower, upper in header["timestamp_spans"].get(timestamp_seconds(timestamp), []):
            if spans and lower == spans[-1][1] + 1:
                spans[-1] = (spans[-1][0], upper)
            else:
                spans.append((lower, upper))
        padded = " " + body + " "
        for lower, upper in spans:
            start = lower
            for piece in pieces:
                location = padded.find(" " + piece + " ", start)
                if location < lower or location + len(piece) > upper:
                    break
                start = location + len(piece) + 1
            else:
                return f"> {public_text(quote).replace(chr(10), chr(10) + '> ')}\n> — {timestamp} [^{vid}]"
        return None


def candidate_report(rows: list[dict], analyses: dict[str, dict]) -> dict:
    """Inverted lexical mechanism index: deterministic and deliberately conservative.

    Exact normalized mechanism/variant titles qualify directly. Other matches
    need at least two shared non-stopword tokens and cosine overlap >= 0.30.
    Area alone, title slugs, model IDs and mere source membership do not qualify.
    This stage suggests candidates only; it never makes relation decisions.
    """
    postings: dict[str, set[str]] = defaultdict(set)
    profiles = {}
    for row in rows:
        mechanism = row.get("mechanism") or {}
        names = [row["title"], mechanism.get("summary", "")]
        names += [variant.get("title", "") for variant in mechanism.get("variants", [])
                  if isinstance(variant, dict)]
        names += [source.get("input_technique", "") for source in row["sources"]]
        names = [name for name in names if isinstance(name, str) and name.strip()]
        fragments = [tokens(name) for name in names]
        profiles[row["id"]] = ({normalized(name) for name in names}, fragments)
        for word in set().union(*fragments):
            postings[word].add(row["id"])
    candidates = []
    for vid, record in sorted(analyses.items()):
        for index, takeaway in enumerate(record["payload"]["takeaways"]):
            name = takeaway.get("technique") or ""
            explanation = takeaway.get("what_they_do") or ""
            name = name if isinstance(name, str) else ""
            explanation = explanation if isinstance(explanation, str) else ""
            query = tokens(name + " " + explanation)
            possible = set().union(*(postings.get(word, set()) for word in query))
            matching = []
            for identity in sorted(possible):
                exact_names, fragments = profiles[identity]
                exact = normalized(name) in exact_names or normalized(explanation) in exact_names
                overlap = any(len(query & fragment) >= 2 and
                              len(query & fragment) / math.sqrt(len(query) * len(fragment)) >= 0.30
                              for fragment in fragments if fragment)
                if exact or overlap:
                    matching.append(identity)
            candidates.append({"vid": vid, "takeaway_index": index, "candidate_ids": matching})
    return {"schema_version": 1, "candidates": candidates}


def validate_proposals(value, candidates: dict[tuple[str, int], set[str]]) -> list[dict]:
    require(isinstance(value, dict) and type(value.get("schema_version")) is int
            and value["schema_version"] == 1 and isinstance(value.get("proposals"), list),
            "invalid_relations", "Relations need schema_version 1 and a proposals list.")
    result, seen = [], {}
    for proposal in value["proposals"]:
        require(isinstance(proposal, dict) and set(proposal) == PROPOSAL_KEYS,
                "invalid_proposal", "Relation proposals have four required fields only.")
        vid, index, identity, relation = (proposal.get(key) for key in
                                             ("vid", "takeaway_index", "catalog_id", "relation"))
        require(isinstance(vid, str) and type(index) is int and index >= 0
                and isinstance(identity, str) and isinstance(relation, str),
                "invalid_proposal", "Relation fields have invalid types or indices.")
        require(relation in RELATIONS, "unsupported_relation",
                "Only supports, refines and contradicts are supported; new IDs need an explicit catalog extension.")
        require(identity in candidates.get((vid, index), set()), "out_of_candidate_relation",
                "Proposed identity is not a deterministic catalog candidate for this takeaway.")
        key = vid, index, identity
        require(key not in seen or seen[key] == relation, "conflicting_relations",
                "A source/claim pair cannot have conflicting relations.")
        if key not in seen:
            result.append(dict(proposal))
        seen[key] = relation
    return result


def parse_document(text: str) -> dict:
    require(text.startswith("---\n") and "\n---\n" in text, "invalid_existing_claim",
            "Existing claim frontmatter must be preserved and inspected before migration.")
    block, body = text[4:].split("\n---\n", 1)
    try:
        metadata = json.loads(block)
    except ValueError:
        raise PublicationError("invalid_existing_claim", "Existing claims need the generated JSON-compatible YAML format.") from None
    require(isinstance(metadata, dict) and isinstance(metadata.get("id"), str)
            and isinstance(metadata.get("title"), str) and bool(metadata["title"].strip())
            and isinstance(metadata.get("area"), str) and metadata.get("type") == "technique"
            and isinstance(metadata.get("status"), str) and metadata["status"] in {"stable", "deprecated"}
            and isinstance(metadata.get("generated"), dict) and bool(metadata["generated"].get("by"))
            and instant(metadata["generated"].get("at")) is not None
            and instant(metadata.get("stale_after")) is not None,
            "invalid_existing_claim", "Existing claim lifecycle metadata is not usable.")
    for key in ("valid_from", "valid_to"):
        require(key in metadata and (metadata[key] is None or instant(metadata[key]) is not None),
                "invalid_existing_claim", "Existing claim dates must be aware instants or null.")
    require("superseded_by" in metadata and
            ((metadata["status"] == "stable" and metadata["valid_to"] is None and metadata["superseded_by"] is None)
             or (metadata["status"] == "deprecated" and isinstance(metadata["superseded_by"], str)
                 and bool(metadata["superseded_by"]))),
            "invalid_existing_claim", "Existing claim lifecycle is inconsistent.")
    sources = metadata.get("sources")
    require(isinstance(sources, list) and bool(sources), "invalid_existing_claim", "Retained claims need evidence sources.")
    ids = set()
    for source in sources:
        require(isinstance(source, dict) and isinstance(source.get("id"), str)
                and SAFE_VID.fullmatch(source["id"]) is not None and source["id"] not in ids
                and source.get("resource") == f"https://www.youtube.com/watch?v={source['id']}"
                and isinstance(source.get("analysis_file"), str)
                and source["analysis_file"].startswith("analysis/")
                and all(key in source for key in ("title", "author", "last_modified"))
                and (source["last_modified"] is None or instant(source["last_modified"]) is not None),
                "invalid_existing_claim", "Retained source metadata is invalid or ambiguous.")
        ids.add(source["id"])
    return {"frontmatter": metadata, "body": body.lstrip("\n")}


def render_document(claim: dict) -> str:
    # JSON objects are a YAML 1.2 subset, preserving strings, nulls and nesting
    # without adding a parser dependency to this offline CLI.
    return "---\n" + json.dumps(claim["frontmatter"], ensure_ascii=False, indent=2) + "\n---\n\n" + claim["body"]


def semantic(claim: dict) -> dict:
    metadata = {key: value for key, value in claim["frontmatter"].items()
                if key not in {"generated", "stale_after", "relations"}}
    return {"frontmatter": metadata, "body": claim["body"]}


def relation_event_id(proposal: dict) -> str:
    """A supersession event is its validated decision, not mutable display prose."""
    return hashlib.sha256(json.dumps(proposal, sort_keys=True).encode("utf-8")).hexdigest()[:20]


def stamp(claim: dict, at: datetime, existing: dict | None) -> None:
    metadata = claim["frontmatter"]
    if existing and semantic(claim) == semantic(existing) and metadata.get("relations") == existing["frontmatter"].get("relations"):
        metadata["generated"] = copy.deepcopy(existing["frontmatter"]["generated"])
        metadata["stale_after"] = existing["frontmatter"]["stale_after"]
    else:
        metadata["generated"] = {"by": GENERATOR, "at": iso(at)}
        metadata["stale_after"] = iso(at + timedelta(days=90))


def generic_effect(row: dict) -> str:
    benefit = row.get("expected_benefit") or {}
    if not isinstance(benefit, dict):
        return NOT_STATED
    lines = [f"- **{key.capitalize()}:** {public_text(benefit[key])}"
             for key in ("cost", "speed", "quality", "reliability", "certainty")
             if isinstance(benefit.get(key), str) and benefit[key].strip()]
    return "\n".join(lines) or NOT_STATED


def claim_body(row: dict, what: str, sources: list[dict], quotes: dict[str, list[str]]) -> str:
    evidence_lines = []
    footnotes = []
    for source in sources:
        vid = source["id"]
        evidence_lines.extend(sorted(set(quotes.get(vid, []))))
        if not quotes.get(vid):
            evidence_lines.append(f"Source analysis [^{vid}]; no independently matched timestamped quote published.")
        footnotes.append(f"[^{vid}]: [{source['title'] or vid}]({source['resource']})"
                         f"; publication: {source['last_modified'] or 'unknown'}; analysis: `{source['analysis_file']}`.")
    return (f"# {public_text(row['title'])}\n\n## What\n\n{what or NOT_STATED}\n\n"
            f"## Evidence\n\n" + "\n\n".join(evidence_lines) +
            "\n\n## How to apply (generic)\n\n"
            "Test the smallest supported intervention on representative tasks. Compare against a baseline, "
            "check correctness and failure cases, and retain a rollback before wider use.\n\n"
            f"## Expected effect\n\n{generic_effect(row)}\n\n" + "\n".join(footnotes) + "\n")


def initial_claim(row: dict, evidence: Evidence) -> tuple[dict, dict[str, list[str]], str]:
    quotes: dict[str, list[str]] = defaultdict(list)
    sources = {}
    for source in sorted(row["sources"], key=lambda value: (value["vid"], value.get("record_id", ""))):
        vid = source["vid"]
        sources[vid] = evidence.source(vid)
        quote = evidence.quote(vid, source)
        if quote:
            quotes[vid].append(quote)
    ordered = [source for _, source in sorted(sources.items())]
    times = [instant(source["last_modified"]) for source in ordered]
    # An unresolved source never becomes "known" through another source's clock.
    valid_from = iso(max(times)) if all(times) else None
    mechanism = row.get("mechanism") or {}
    require(isinstance(mechanism, dict), "invalid_catalog", "Mechanism must be an object.")
    what = "\n\n".join(public_text(mechanism.get(key)) for key in
                          ("summary", "representative_explanation") if mechanism.get(key))
    claim = {"frontmatter": {"type": "technique", "id": row["id"], "title": public_text(row["title"]),
                             "area": row["area"], "status": "stable", "valid_from": valid_from,
                             "valid_to": None, "superseded_by": None, "sources": ordered},
             "body": claim_body(row, what, ordered, quotes)}
    return claim, quotes, what


def add_relation(claim: dict, row: dict, proposal: dict, evidence: Evidence,
                 quotes: dict[str, list[str]], what: str, *,
                 transition: dict | None = None) -> tuple[dict | None, str]:
    """Prove a new transition once; replay its persisted outcome thereafter."""
    metadata = claim["frontmatter"]
    vid, index = proposal["vid"], proposal["takeaway_index"]
    source = evidence.source(vid)
    takeaway = evidence.analyses[vid]["payload"]["takeaways"][index]
    old_times = [instant(value["last_modified"]) for value in metadata["sources"]]
    new_time = instant(source["last_modified"])
    if transition is not None:
        # Dates may be corrected later. They must update source metadata, not
        # undo a committed lifecycle transition or create a retroactive one.
        new_time = instant(transition["superseded_at"])
        eligible = new_time is not None
    else:
        eligible = (proposal["relation"] in {"refines", "contradicts"}
                    and new_time is not None and all(old_times)
                    and new_time - max(old_times) >= timedelta(days=30))
    archived = None
    if eligible:
        archived = copy.deepcopy(claim)
        old = archived["frontmatter"]
        revision = relation_event_id(proposal)
        old.update(id=f"{row['id']}--{revision}", status="deprecated", valid_to=iso(new_time),
                   superseded_by=row["id"])
        metadata.update(valid_from=iso(new_time), sources=[source])
        quotes.clear()
        what = public_text(takeaway.get("what_they_do")) or what
    else:
        by_id = {value["id"]: value for value in metadata["sources"]}
        by_id[vid] = source
        metadata["sources"] = [value for _, value in sorted(by_id.items())]
    quote = evidence.quote(vid, takeaway, takeaway=True)
    if quote:
        quotes.setdefault(vid, []).append(quote)
    claim["body"] = claim_body(row, what, metadata["sources"], quotes)
    return archived, what


def read_existing(root: Path) -> tuple[dict[str, dict], list[dict]]:
    documents, decisions = {}, []
    kb = safe_path(root, "kb")
    if not kb.exists():
        return documents, decisions
    for path in sorted(kb.rglob("*")):
        safe_path(root, str(path.relative_to(root)))
        if path.is_file() and path.suffix == ".md" and path.name not in {"index.md", "log.md"}:
            relative = str(path.relative_to(root))
            document = parse_document(path.read_text(encoding="utf-8"))
            documents[relative] = document
            relations = document["frontmatter"].get("relations", [])
            require(isinstance(relations, list), "invalid_existing_relations", "Persisted relations must be a list.")
            if document["frontmatter"].get("status") == "stable":
                decisions.extend(relations)
    return documents, decisions


def persisted_transitions(documents: dict[str, dict]) -> dict[str, dict]:
    """Read immutable outcomes; migrate older bundles from retained revisions.

    An accepted relation without a retained revision was an append, even if
    corrected source dates would make it eligible for supersession today.
    """
    result = {}
    for document in documents.values():
        metadata = document["frontmatter"]
        if metadata["status"] != "stable":
            continue
        proposals = metadata.get("relations", [])
        recorded = metadata.get("relation_transitions")
        ids = {relation_event_id(proposal) for proposal in proposals}
        require(recorded is None or (isinstance(recorded, dict) and set(recorded) == ids),
                "invalid_existing_relations", "Persisted outcomes must match accepted relations.")
        for proposal in proposals:
            event_id = relation_event_id(proposal)
            history = documents.get(f"kb/history/{proposal['catalog_id']}--{event_id}.md")
            archived_at = history["frontmatter"]["valid_to"] if history else None
            at = recorded[event_id] if recorded is not None else archived_at
            require((at is None or (isinstance(at, str) and instant(at) is not None))
                    and (at is None) == (history is None)
                    and (not history or (at == archived_at
                         and history["frontmatter"]["superseded_by"] == proposal["catalog_id"]
                         and proposal["relation"] in {"refines", "contradicts"})),
                    "invalid_existing_relations", "Persisted outcomes and retained revisions must agree.")
            result[event_id] = {"superseded_at": at}
    return result


def update_log(existing: str, events: list[tuple[str, str]]) -> str:
    groups: dict[str, list[str]] = defaultdict(list)
    current = None
    for line in existing.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", current) is not None,
                    "invalid_log", "Existing log date headings must be ISO dates.")
        elif current and line.strip():
            groups[current].append(line)
    recorded = {line.split("`", 2)[1] for lines in groups.values() for line in lines
                if line.startswith("- `") and line.count("`") >= 2}
    for day, entry in events:
        event_id = entry.split("`", 2)[1]
        if event_id not in recorded:
            groups[day].append(entry)
            recorded.add(event_id)
    lines = ["# Supersession log", ""]
    for day, entries in sorted(groups.items(), reverse=True):
        lines += [f"## {day}", "", *sorted(set(entries)), ""]
    return "\n".join(lines).rstrip() + "\n"


def derived_files(root: Path, documents: dict[str, dict], log: str) -> dict[str, str]:
    directories = {"kb"}
    for relative in documents:
        directory = Path(relative).parent
        while str(directory) != ".":
            directories.add(str(directory))
            directory = directory.parent
    for path in safe_path(root, "kb").rglob("*"):
        if path.is_dir():
            directories.add(str(path.relative_to(root)))
    desired = {"kb/log.md": log}
    for directory in sorted(directories):
        lines = ["# AI Engineer knowledge" if directory == "kb" else f"# {Path(directory).name}", ""]
        if directory == "kb":
            lines = ["---", 'okf_version: "0.2"', "---", "", *lines]
        lines += ["## Techniques and revisions", ""]
        for relative, claim in sorted(documents.items()):
            if str(Path(relative).parent) == directory:
                fm = claim["frontmatter"]
                lines.append(f"- [{fm['title']}]({Path(relative).name}) — `{fm['id']}` ({fm['status']})")
        children = sorted(child for child in directories if str(Path(child).parent) == directory)
        if children:
            lines += ["", "## Directories", ""]
            lines += [f"- [{Path(child).name}]({Path(child).name}/index.md)" for child in children]
        desired[f"{directory}/index.md"] = "\n".join(lines).rstrip() + "\n"
    stable = [(path, claim) for path, claim in sorted(documents.items())
              if claim["frontmatter"]["status"] == "stable"]
    desired["llms.txt"] = ("# AI Engineer Knowledge Base\n\n"
                           "Generic techniques, unverified source interpretations. Frozen identities; "
                           "relation-gated supersession retains evidence history.\n\n"
                           f"Stable techniques: {len(stable)}.\n\n## Start here\n\n"
                           f"- [Knowledge indexes]({BASE_URL}/kb/index.md)\n"
                           f"- [Full text]({BASE_URL}/llms-full.txt)\n"
                           f"- [Supersession log]({BASE_URL}/kb/log.md)\n")
    desired["llms-full.txt"] = ("# AI Engineer Knowledge Base — stable techniques\n\n" +
                                "\n---\n\n".join(claim["body"] for _, claim in stable))
    return desired


def publish(root: Path, desired: dict[str, str], check: bool) -> tuple[dict, int]:
    # Preflight EVERY target before directory creation or any replacement.
    stale = []
    for relative, content in sorted(desired.items()):
        target = safe_path(root, relative)
        require(not target.exists() or target.is_file(), "invalid_output_target", "Output targets must be files.")
        for parent in target.parents:
            if parent == root:
                break
            require(not parent.exists() or parent.is_dir(), "invalid_output_target", "Output ancestors must be directories.")
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            stale.append(relative)
    if check:
        return {"status": "stale" if stale else "current", "stale": stale}, int(bool(stale))
    for relative in stale:
        target = safe_path(root, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                             dir=target.parent, prefix=".claims-", delete=False) as handle:
                temporary = Path(handle.name)
                handle.write(desired[relative])
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, target)
        finally:
            if temporary and temporary.exists():
                temporary.unlink()
    return {"status": "generated", "files_changed": len(stale), "files_checked": len(desired)}, 0


def generate(root: Path, *, candidates=False, check=False, relations: Path | None = None) -> tuple[dict | None, int]:
    root = root.absolute()
    require(root.is_dir() and not root.is_symlink(), "invalid_root", "Root must be a real corpus directory.")
    payloads = []
    for path in sorted(safe_path(root, "analysis").glob("*.json")):
        relative = str(path.relative_to(root))
        safe_path(root, relative)
        # Malformed legacy fixtures are handled by their original adapter.
        try:
            payload = load_json(path)
        except PublicationError:
            payload = None
        payloads.append((relative, payload))
    rows = load_catalog(root, payloads)
    if rows is None:
        require(not candidates and relations is None, "missing_catalog", "Candidate and relation stages require a source catalog.")
        return None, 0
    analyses = load_analyses(payloads)
    evidence = Evidence(root, analyses)
    # Validate every frozen source join and referenced transcript before writes.
    for row in rows:
        for source in row["sources"]:
            evidence.source(source["vid"])
    existing, prior = read_existing(root)
    report = candidate_report(rows, analyses) if candidates or relations is not None else None
    if candidates:
        require(relations is None, "invalid_mode", "Candidate discovery cannot apply relations.")
        return report, 0
    candidate_ids = {(row["vid"], row["takeaway_index"]): set(row["candidate_ids"])
                     for row in report["candidates"]} if report else {}
    # Previously accepted decisions need valid references, not a new lexical
    # match against editable display prose. New proposals still use candidates.
    catalog_ids = {row["id"] for row in rows}
    references = {(vid, index): catalog_ids for vid, record in analyses.items()
                  for index in range(len(record["payload"]["takeaways"]))}
    accepted = validate_proposals({"schema_version": 1, "proposals": prior}, references)
    transitions = persisted_transitions(existing)
    def order(proposal: dict):
        timestamp = instant(analyses[proposal["vid"]]["payload"].get("published_at"))
        return (timestamp or datetime.min.replace(tzinfo=timezone.utc), proposal["vid"],
                proposal["takeaway_index"], proposal["catalog_id"], proposal["relation"])
    if relations is not None:
        require(not relations.is_symlink(), "unsafe_path", "Relation inputs cannot be symlinks.")
        incoming = validate_proposals(load_json(relations), candidate_ids)
        # Persist application order. Backdated evidence arriving later must not
        # reorder decisions that already produced an immutable history revision.
        incoming.sort(key=order)
        accepted = validate_proposals({"schema_version": 1, "proposals": accepted + incoming}, references)
    by_identity = defaultdict(list)
    for proposal in accepted:
        by_identity[proposal["catalog_id"]].append(proposal)
    now = datetime.now(timezone.utc)
    documents = dict(existing)  # Never delete unreferenced evidence or history.
    events = []
    for row in rows:
        claim, quotes, what = initial_claim(row, evidence)
        outcomes = {}
        for proposal in by_identity[row["id"]]:
            event_id = relation_event_id(proposal)
            archived, what = add_relation(claim, row, proposal, evidence, quotes, what,
                                           transition=transitions.get(event_id))
            outcomes[event_id] = archived["frontmatter"]["valid_to"] if archived else None
            if archived:
                old = archived["frontmatter"]
                relative = f"kb/history/{old['id']}.md"
                if relative in existing:
                    # Frozen revisions are evidence, not a cache to regenerate
                    # after a title edit or a later source metadata backfill.
                    archived = existing[relative]
                    old = archived["frontmatter"]
                else:
                    stamp(archived, now, None)
                documents[relative] = archived
                old_vids = ", ".join(source["id"] for source in old["sources"])
                events.append((old["valid_to"][:10],
                               f"- `{old['id']}` [{row['id']}]({row['area']}/{row['id']}.md): "
                               f"{proposal['relation']}; {old_vids} → {proposal['vid']}; "
                               f"[retained revision](history/{old['id']}.md)."))
        claim["frontmatter"]["relations"] = by_identity[row["id"]]
        claim["frontmatter"]["relation_transitions"] = outcomes
        relative = f"kb/{row['area']}/{row['id']}.md"
        stamp(claim, now, existing.get(relative))
        documents[relative] = claim
    log_path = safe_path(root, "kb/log.md")
    old_log = log_path.read_text(encoding="utf-8") if log_path.is_file() else ""
    desired = {relative: render_document(claim) for relative, claim in documents.items()}
    desired.update(derived_files(root, documents, update_log(old_log, events)))
    return publish(root, desired, check)
