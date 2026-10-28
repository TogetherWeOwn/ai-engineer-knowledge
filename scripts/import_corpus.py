#!/usr/bin/env python3
"""One-shot, deterministic import of the research corpus into this repository.

Reads a local corpus directory (raw transcripts, per-video analysis and the
frozen technique catalog) and writes the public layout:

- ``transcripts/<vid>.txt``: verbatim caption body under the provenance
  header pinned by ``transcripts/README.md``;
- ``analysis/<vid>.json``: a field-by-field allowlisted projection of the
  per-video analysis, with each ``evidence_quote`` checked against the
  caption body;
- ``data/catalog.json``: the frozen technique catalog. All technique IDs are
  kept unchanged and in their original order. The legacy generator owns the
  root ``catalog.json``, so this file lives under ``data/``.

Privacy model: only allowlisted fields are copied. Generated prose
(summaries, techniques, mechanisms) is scrubbed sentence by sentence; any
sentence written relative to the reader's own organization is dropped.
Before anything is written, every output is scanned by a fail-closed gate.
A required ``--private-terms`` JSON file, kept outside the repository, adds
local sentence terms, deny regexes and deny literals. A transcript that hits
the gate is held back for manual review; captions are never edited. Any other
hit aborts the import without writing.

Rerunning with the same inputs and ``--exported-at`` gives a byte-identical
tree. A ``published_at`` that is already present in an analysis file (filled
by ``backfill_publish_dates.py``) is carried over.

Usage:
  uv run --no-project --python 3.12 -- python -I scripts/import_corpus.py \\
      --src <corpus dir> --out <checkout> --exported-at 2026-10-28T03:00:00Z \\
      --private-terms <local policy.json>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

WATCH_PREFIX = "https://www.youtube.com/watch?v="
CHANNEL_CREDIT = "AI Engineer (https://www.youtube.com/@aiDotEngineer)"
CAPTION_LABEL = "auto/author captions, unverified"
MACHINE_LABEL = "machine transcript (Whisper; no YouTube captions)"
TAKEDOWN = "rights holders may open an issue on this repository to have this file removed"
EXPORT_VERSION = "public-1"
VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{6,64}")
LANGUAGES = {"en": "English", "es": "Spanish", "nl": "Dutch", "hi": "Hindi", "ar": "Arabic",
             "de": "German", "fr": "French", "pt": "Portuguese", "ja": "Japanese"}

# Sentences written relative to the analyst's own organization, not the talk.
COMPANY_RELATIVE = (
    r"our|ours|we|us|maps?\s+(?:directly\s+)?onto|agent\s+company"
    r"|relevan(?:t|ce)\s+(?:to|for)\s+(?:us|our|this\s+company|the\s+company|running)"
    r"|brief|cards?|fork(?:s|ed)?|heartbeats?"
    r"|agent[\s-]+(?:orchestration[\s-]+)?compan(?:y|ies)|orchestration[\s-]+compan(?:y|ies)"
    r"|a\s+company\s+that|out\s+of\s+scope|tangentially|indirect\s+lessons"
)
# Generic leak patterns; deployment-specific ones come from --private-terms.
GENERIC_DENY = [r"/home/", r"/Users/", r"[a-z0-9-]+\.ts\.net\b",
                r"\b192\.168\.\d{1,3}\.\d{1,3}", r"\bsynthetic/[a-z]+-v?\d"]

# Three cluster titles were phrased relative to the analyst's own tracker.
# IDs are frozen; only the display title is generalized.
TITLE_OVERRIDES = {
    "structured-observability": "Use structured correlated traces across tasks, runs, tools, heads and deployments",
    "work-deduplication": "Deduplicate new tasks and investigations against existing work and outcomes",
    "retrieval-evaluation": "Measure retrieval coverage, relevance, grounding and cost on real file-finding tasks",
}
CATALOG_NOTE = ("Identities are frozen; the generator must never write this file. "
                "reported_measurements are speaker/reader reports, not independently reproduced. "
                "Record counts describe the whole source catalog, including clusters not exported here.")
COUNT_KEYS = ("raw_input_records", "deep_read_records", "triage_only_records", "deep_read_talks",
              "triage_only_talks", "unique_source_talks", "excluded_records")
METHODOLOGY_KEYS = ("loading", "deduplication", "mechanism_granularity", "classification_review",
                    "source_levels", "quotation", "numbers")
SOURCE_KEEP = ("record_id", "vid", "talk", "url", "source", "quote", "timestamp", "timestamp_end",
               "quote_verification", "quote_match_score", "matching_occurrences",
               "requires_confirmation", "quote_is_verbatim_original")
SOURCE_FLAGS = ("triage_interpretation_requires_confirmation",)
TS_TOKEN = re.compile(r"\[(\d{1,2}:)?\d{1,2}:\d{2}\]")
LINE_TS = re.compile(r"^\[((?:\d{1,2}:)?\d{1,2}:\d{2})\]\s?(.*)$")
RUN_OK = re.compile(r"^(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ) ok \d+ (\S+) \(")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
MIN_QUOTE_WORDS = 4
# Ellipsis pieces must each be substantive and sit close together.
MIN_PIECE_WORDS = 3
MAX_ELLIPSIS_SPAN_FACTOR = 3
MAX_ELLIPSIS_GAP_CHARS = 600


class ImportError_(Exception):
    pass


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def iso_z(ts: float) -> str:
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_z(value: str) -> float:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    text = TS_TOKEN.sub(" ", text)
    text = re.sub(r"['\u2019`]", "", text)
    text = re.sub(r"[^\w\s]|_", " ", text)
    return " ".join(text.split())


def speaker_from_title(title: str) -> str | None:
    matches = list(re.finditer(r"\s(?:\u2014|\u2013|-|\|)\s", title))
    if not matches:
        return None
    speaker = title[matches[-1].end():].strip()
    return speaker or None


class Scrubber:
    def __init__(self, private_terms: list[str]):
        words = COMPANY_RELATIVE
        if private_terms:
            words += "|" + "|".join(re.escape(t) for t in private_terms)
        self.pattern = re.compile(r"(?i)\b(?:" + words + r")\b")
        self.counts: dict[str, int] = {}

    def hits(self, text: str) -> bool:
        return bool(self.pattern.search(text))

    def text(self, value, field: str):
        """Drop company-relative sentences; None when nothing remains."""
        if value is None:
            return None
        if not isinstance(value, str):
            raise ImportError_(f"{field}: expected a string or null")
        kept, dropped = [], 0
        for sentence in SENTENCE_SPLIT.split(value.strip()):
            if not sentence:
                continue
            if self.pattern.search(sentence):
                dropped += 1
            else:
                kept.append(sentence)
        if dropped:
            self.counts[field] = self.counts.get(field, 0) + dropped
        return " ".join(kept) if kept else None

    def texts(self, values, field: str) -> list:
        if values is not None and not isinstance(values, list):
            raise ImportError_(f"{field}: expected a list of strings")
        out = []
        for value in values or []:
            cleaned = self.text(value, field)
            if cleaned:
                out.append(cleaned)
        return out


class Gate:
    def __init__(self, regexes: list[str], literals: list[str]):
        self.regexes = [re.compile(r, re.I) for r in GENERIC_DENY + list(regexes)]
        self.literals = [lit.lower() for lit in literals if lit]

    def problems(self, text: str) -> list[str]:
        low = text.lower()
        found = [f"regex#{i}" for i, rx in enumerate(self.regexes) if rx.search(text)]
        found += [f"literal#{i}" for i, lit in enumerate(self.literals) if lit in low]
        return found


# ---------------------------------------------------------------------------
# Transcripts
# ---------------------------------------------------------------------------

class Caption:
    """Normalized caption body with a word -> line timestamp map."""

    def __init__(self, body: str):
        words, stamps = [], []
        stamp = None
        for line in body.split("\n"):
            match = LINE_TS.match(line)
            if match:
                stamp, line = match.group(1), match.group(2)
            for word in normalize(line).split():
                words.append(word)
                stamps.append(stamp)
        self.text = " ".join(words)
        offsets, pos = [], 0
        for word in words:
            offsets.append(pos)
            pos += len(word) + 1
        self.offsets = offsets
        self.stamps = stamps

    def stamp_at(self, char_pos: int):
        lo, hi = 0, len(self.offsets) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.offsets[mid] <= char_pos:
                lo = mid
            else:
                hi = mid - 1
        return self.stamps[lo] if self.stamps else None

    def find(self, normalized: str, start: int = 0) -> int:
        """Locate a normalized phrase without matching only part of a word."""
        pattern = re.compile(r"(?<!\w)" + re.escape(normalized) + r"(?!\w)")
        match = pattern.search(self.text, start)
        return match.start() if match else -1

    def verify(self, quote):
        """Return (method, timestamp) or (None, None)."""
        if not isinstance(quote, str):
            return None, None
        whole = normalize(quote)
        if len(whole.split()) < MIN_QUOTE_WORDS:
            return None, None
        pos = self.find(whole)
        if pos >= 0:
            return "normalized-exact", self.stamp_at(pos)
        pieces = [normalize(p) for p in re.split(r"\.\.\.|\u2026", quote)]
        pieces = [p for p in pieces if p]
        if len(pieces) < 2 or any(len(p.split()) < MIN_PIECE_WORDS for p in pieces):
            return None, None
        start, first = 0, None
        for piece in pieces:
            pos = self.find(piece, start)
            if pos < 0:
                return None, None
            first = pos if first is None else first
            start = pos + len(piece)
        if start - first > MAX_ELLIPSIS_SPAN_FACTOR * sum(len(p) for p in pieces) + MAX_ELLIPSIS_GAP_CHARS:
            return None, None
        return "ordered-ellipsis-pieces", self.stamp_at(first)


def caption_track(track: str) -> str:
    if track == "auto":
        return "auto (YouTube automatic captions, en)"
    if track in ("manual", "author", "en"):
        return "author (YouTube author-provided captions)"
    match = re.fullmatch(r"dub-auto:([a-z]{2,3})", track)
    if match:
        lang = LANGUAGES.get(match.group(1), match.group(1))
        return f"{track} (YouTube auto-dubbed {lang} captions; not the original English)"
    match = re.fullmatch(r"auto:([a-z]{2,3})", track)
    if match:
        lang = LANGUAGES.get(match.group(1), match.group(1))
        return f"{track} (YouTube automatic captions mis-detected as {lang})"
    raise ImportError_(f"unknown caption track kind: {track!r}")


def parse_raw_transcript(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    index = 0
    while index < len(lines) and lines[index].startswith("#"):
        index += 1
    header, rest = lines[:index], lines[index:]
    if not header or not rest or rest[0] != "":
        raise ImportError_(f"{path.name}: unexpected raw header layout")
    body = "\n".join(rest[1:])
    if not body.strip() or body.startswith("#"):
        raise ImportError_(f"{path.name}: empty body or body starts with '#'")
    fields = {"title": header[0][1:].strip()}
    for line in header[1:]:
        for part in line[1:].split(" | "):
            if ":" in part:
                key, value = part.split(":", 1)
                fields[key.strip()] = value.strip()
    fields["body"] = body
    return fields


def load_run_log(path: Path) -> dict[str, list[float]]:
    times: dict[str, list[float]] = {}
    if not path.is_file():
        return times
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = RUN_OK.match(line)
        if match:
            times.setdefault(match.group(2), []).append(parse_z(match.group(1)))
    return times


def load_manifest_models(path: Path) -> dict[str, str]:
    models = {}
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                record = json.loads(line)
            except ValueError:
                continue
            if record.get("ok") and record.get("model"):
                models[record["id"]] = record["model"]
    return models


def build_transcript(vid: str, raw: dict, retrieved_at: str, machine_model: str | None) -> str:
    url = raw.get("url", "")
    if url != WATCH_PREFIX + vid:
        raise ImportError_(f"{vid}: raw url does not match filename")
    header = [f"# title: {raw['title']}", f"# source: {WATCH_PREFIX}{vid}"]
    speaker = speaker_from_title(raw["title"])
    if speaker:
        header.append(f"# speaker: {speaker}")
    header.append(f"# channel: {CHANNEL_CREDIT}")
    machine = raw.get("source") == "whisper"
    if machine:
        header.append("# caption_track: none")
        header.append(f"# transcriber: {machine_model or 'faster-whisper'}")
    else:
        header.append(f"# caption_track: {caption_track(raw.get('track', ''))}")
    header.append(f"# retrieved_at: {retrieved_at}")
    header.append(f"# sha256: {sha256_text(raw['body'])}")
    header.append(f"# {MACHINE_LABEL if machine else CAPTION_LABEL}")
    if machine:
        header.append("# unverified")
    header.append(f"# takedown: {TAKEDOWN}")
    return "\n".join(header) + "\n" + raw["body"]


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyzer_name(model) -> str | None:
    if not isinstance(model, str) or not model:
        return None
    return re.sub(r"-\d{4}$", "", model.rsplit("/", 1)[-1])


def project_fields(value, shape, field: str, *, nullable=True):
    """Validate complete exported shapes and recursively discard unlisted keys.

    A field allowlist is not a privacy boundary if a scalar can contain an
    arbitrary object. Lists describe their element shape; dictionaries enumerate
    public keys. Unknown research-only keys are deliberately never traversed.
    """
    if value is None and nullable:
        return None
    if isinstance(shape, dict):
        if not isinstance(value, dict):
            raise ImportError_(f"{field}: expected an object")
        return {key: project_fields(value[key], child, f"{field}.{key}")
                for key, child in shape.items() if key in value}
    if isinstance(shape, list):
        if not isinstance(value, list):
            raise ImportError_(f"{field}: expected a list")
        return [project_fields(item, shape[0], field + "[]", nullable=False) for item in value]
    types = shape if isinstance(shape, tuple) else (shape,)
    if type(value) not in types:
        raise ImportError_(f"{field}: unexpected field type")
    return value


TAKEAWAY_FIELDS = {key: str for key in
                  ("area", "technique", "what_they_do", "evidence_quote", "numbers", "confidence")}
ANALYSIS_FIELDS = {**{key: str for key in ("vid", "title", "talk_summary", "confidence", "analyzed_at", "model")},
                   "truncated": bool, "takeaways": [TAKEAWAY_FIELDS]}
SOURCE_FIELDS = {
    **{key: str for key in ("record_id", "vid", "talk", "url", "source", "quote", "timestamp", "timestamp_end",
                           "quote_verification", "input_technique", "input_area", "mechanism_in_source")},
    "quote_match_score": (int, float), "matching_occurrences": int,
    **{key: bool for key in ("requires_confirmation", "quote_is_verbatim_original", *SOURCE_FLAGS)},
    "additional_original_excerpts": [{key: str for key in ("quote", "timestamp", "timestamp_end")}],
}
TECHNIQUE_FIELDS = {
    **{key: str for key in ("id", "title", "area", "source", "evidence_level")},
    **{key: int for key in ("source_count", "source_record_count", "deep_read_source_count", "triage_only_source_count")},
    "quote_evidence": {key: int for key in ("normalized-exact", "ordered-ellipsis-pieces",
                                            "fuzzy-location-needs-confirmation", "manual-original-excerpt")},
    "mechanism": {"summary": str, "representative_explanation": str, "representative_record_id": str,
                  "variants": [{"title": str, "source_record_ids": [str]}]},
    "expected_benefit": {key: str for key in ("cost", "speed", "quality", "reliability", "certainty")},
    "risk": {"level": str, "failure_modes": [str], "mitigation": str},
    "how_to_measure_success": {"metrics": [str], "acceptance": str},
    "reported_measurements": [{"text": str, "source_record_ids": [str]}],
    "sources": [SOURCE_FIELDS],
}
CATALOG_FIELDS = {
    **{key: str for key in ("schema_version", "title", "generated_at")},
    "areas": [str], "counts": {key: int for key in COUNT_KEYS}, "scope": {"source_scope": str},
    "methodology": {
        **{key: str for key in METHODOLOGY_KEYS if key != "classification_review"},
        "classification_review": {
            "assignment_methods": {key: int for key in ("curated-name-rule", "manual-semantic-review",
                                                         "curated-mechanism-rule", "tfidf-nearest-same-area")},
            "manual_assignment_changes": int, "manual_conflict_resolution": str,
        },
    },
    "validation": {"validated_at": str, "independent_checks": int, "failures": int,
                   "verified": [str], "remaining_limits": [str]},
    "techniques": [TECHNIQUE_FIELDS],
}


def project_analysis(raw: dict, transcript: dict, caption: Caption, scrub: Scrubber,
                     stats: dict, published_at) -> dict:
    raw = project_fields(raw, ANALYSIS_FIELDS, "analysis", nullable=False)
    vid = raw["vid"]
    takeaways = []
    for item in raw.get("takeaways") or []:
        if not isinstance(item, dict):
            raise ImportError_(f"{vid}: takeaway must be an object")
        quote = item.get("evidence_quote")
        method, stamp = caption.verify(quote)
        stats[method or "not-found-in-captions"] = stats.get(method or "not-found-in-captions", 0) + 1
        out = {
            "area": item.get("area"),
            "technique": scrub.text(item.get("technique"), "analysis.technique"),
            "what_they_do": scrub.text(item.get("what_they_do"), "analysis.what_they_do"),
            "evidence_quote": quote if method else None,
            "evidence_quote_verification": method or "not-found-in-captions",
        }
        if method:
            out["evidence_timestamp"] = stamp
        out["numbers"] = scrub.text(item.get("numbers"), "analysis.numbers")
        out["confidence"] = item.get("confidence")
        takeaways.append(out)
    result = {
        "vid": vid,
        "title": raw.get("title"),
        "source": WATCH_PREFIX + vid,
        "talk_summary": scrub.text(raw.get("talk_summary"), "analysis.talk_summary"),
        "takeaways": takeaways,
    }
    if isinstance(raw.get("confidence"), str):
        result["confidence"] = raw["confidence"]
    result["truncated"] = raw.get("truncated")
    result["analyzed_at"] = raw.get("analyzed_at")
    result["analyzer"] = analyzer_name(raw.get("model"))
    result["transcript_file"] = f"transcripts/{vid}.txt"
    result["transcript_sha256"] = transcript["sha256"]
    result["retrieved_at"] = transcript["retrieved_at"]
    if published_at:
        result["published_at"] = published_at
    return result


# ---------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------

def id_digest(ids: list[str]) -> str:
    return sha256_text("\n".join(sorted(ids)) + "\n")


def scrub_tree(value, scrub: Scrubber, field: str):
    if isinstance(value, str):
        return scrub.text(value, field)
    if isinstance(value, list):
        return [v for v in (scrub_tree(x, scrub, field) for x in value) if v is not None]
    if isinstance(value, dict):
        return {k: scrub_tree(v, scrub, field) for k, v in value.items()}
    return value


def project_source(src: dict, scrub: Scrubber, captions: dict, stats: dict) -> dict:
    src = project_fields(src, SOURCE_FIELDS, "catalog.source", nullable=False)
    out = {k: src[k] for k in SOURCE_KEEP if k in src}
    caption = captions.get(src.get("vid"))
    quote = src.get("quote")
    if isinstance(quote, str) and caption is not None and normalize(quote):
        found = caption.find(normalize(quote)) >= 0
    else:
        found = False
    stats["source_quote_found" if found else "source_quote_not_found"] = \
        stats.get("source_quote_found" if found else "source_quote_not_found", 0) + 1
    if not found:
        out["quote"] = None
        out["quote_verification"] = "not-found-in-published-transcript"
    excerpts = []
    for excerpt in src.get("additional_original_excerpts") or []:
        q = excerpt.get("quote")
        if isinstance(q, str) and caption is not None and normalize(q) and caption.find(normalize(q)) >= 0:
            excerpts.append({k: excerpt[k] for k in ("quote", "timestamp", "timestamp_end") if k in excerpt})
    if excerpts:
        out["additional_original_excerpts"] = excerpts
    out["input_technique"] = scrub.text(src.get("input_technique"), "catalog.source.input_technique")
    out["input_area"] = src.get("input_area")
    out["mechanism_in_source"] = scrub.text(src.get("mechanism_in_source"), "catalog.source.mechanism_in_source")
    for flag in SOURCE_FLAGS:
        if flag in src:
            out[flag] = src[flag]
    out["transcript_file"] = f"transcripts/{src['vid']}.txt" if caption is not None else None
    return out


def project_technique(tech: dict, scrub: Scrubber, captions: dict, stats: dict) -> dict:
    mech = tech.get("mechanism") or {}
    title = TITLE_OVERRIDES.get(tech["id"], tech["title"])
    if scrub.hits(title):
        raise ImportError_(f"technique {tech['id']}: title is company-relative; add an override")
    measurements = []
    for item in tech.get("reported_measurements") or []:
        text = scrub.text(item.get("text"), "catalog.reported_measurements")
        if text:
            measurements.append({"text": text, "source_record_ids": item.get("source_record_ids", [])})
    hms = tech.get("how_to_measure_success") or {}
    risk = tech.get("risk") or {}
    benefit = tech.get("expected_benefit") or {}
    return {
        "id": tech["id"],
        "title": title,
        "area": tech.get("area"),
        "source": tech.get("source"),
        "evidence_level": tech.get("evidence_level"),
        "source_count": tech.get("source_count"),
        "source_record_count": tech.get("source_record_count"),
        "deep_read_source_count": tech.get("deep_read_source_count"),
        "triage_only_source_count": tech.get("triage_only_source_count"),
        "quote_evidence": tech.get("quote_evidence"),
        "mechanism": {
            "summary": scrub.text(mech.get("summary"), "catalog.mechanism"),
            "representative_explanation": scrub.text(mech.get("representative_explanation"), "catalog.mechanism"),
            "representative_record_id": mech.get("representative_record_id"),
            "variants": [{"title": scrub.text(v.get("title"), "catalog.mechanism.variants"),
                          "source_record_ids": v.get("source_record_ids", [])}
                         for v in mech.get("variants") or []],
        },
        "expected_benefit": {k: scrub.text(benefit.get(k), "catalog.expected_benefit")
                             for k in ("cost", "speed", "quality", "reliability", "certainty") if k in benefit},
        "risk": {"level": risk.get("level"),
                 "failure_modes": scrub.texts(risk.get("failure_modes"), "catalog.risk"),
                 "mitigation": scrub.text(risk.get("mitigation"), "catalog.risk")},
        "how_to_measure_success": {"metrics": scrub.texts(hms.get("metrics"), "catalog.how_to_measure_success"),
                                   "acceptance": scrub.text(hms.get("acceptance"), "catalog.how_to_measure_success")},
        "reported_measurements": measurements,
        "sources": [project_source(s, scrub, captions, stats) for s in tech.get("sources") or []],
    }


def project_catalog(raw: dict, raw_bytes: bytes, exported_at: str, scrub: Scrubber,
                    captions: dict, stats: dict) -> dict:
    raw = project_fields(raw, CATALOG_FIELDS, "catalog", nullable=False)
    techniques = raw.get("techniques")
    if not isinstance(techniques, list) or not techniques:
        raise ImportError_("catalog techniques must be a non-empty list")
    for technique in techniques:
        if not isinstance(technique, dict) or any(
            not isinstance(technique.get(key), str) or not technique[key].strip()
            for key in ("id", "title", "area")
        ):
            raise ImportError_("catalog techniques require non-empty id, title and area")
    ids = [t["id"] for t in techniques]
    if len(ids) != len(set(ids)):
        raise ImportError_("catalog technique IDs are not unique")
    projected = [project_technique(t, scrub, captions, stats) for t in techniques]
    per_area: dict[str, int] = {}
    for tech in projected:
        per_area[tech["area"]] = per_area.get(tech["area"], 0) + 1
    counts = {k: raw.get("counts", {})[k] for k in COUNT_KEYS if k in raw.get("counts", {})}
    counts["techniques"] = len(projected)
    counts["techniques_per_area"] = dict(sorted(per_area.items()))
    validation = raw.get("validation") or {}
    scope = raw.get("scope") or {}
    methodology = raw.get("methodology") or {}
    return {
        "schema_version": raw.get("schema_version"),
        "export_version": EXPORT_VERSION,
        "title": raw.get("title"),
        "generated_at": raw.get("generated_at"),
        "exported_at": exported_at,
        "source_catalog_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "technique_count": len(projected),
        "id_list_sha256": id_digest(ids),
        "frozen": True,
        "areas": raw.get("areas"),
        "counts": counts,
        "source_scope": scrub.text(scope.get("source_scope"), "catalog.scope"),
        "methodology": {k: scrub_tree(methodology[k], scrub, "catalog.methodology")
                        for k in METHODOLOGY_KEYS if k in methodology},
        "validation": {
            "validated_at": validation.get("validated_at"),
            "independent_checks": validation.get("independent_checks"),
            "failures": validation.get("failures"),
            "verified": scrub.texts(validation.get("verified"), "catalog.validation"),
            "remaining_limits": scrub.texts(validation.get("remaining_limits"), "catalog.validation"),
        },
        "note": CATALOG_NOTE,
        "techniques": projected,
    }


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def dump_json(payload, indent: int) -> str:
    return json.dumps(payload, indent=indent, ensure_ascii=False) + "\n"


def existing_published_at(path: Path):
    try:
        existing = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, ValueError) as exc:
        raise ImportError_(f"{path.name}: unreadable existing analysis metadata") from exc
    if not isinstance(existing, dict):
        raise ImportError_(f"{path.name}: existing analysis metadata must be an object")
    value = existing.get("published_at")
    if value is not None and (not isinstance(value, str) or not value):
        raise ImportError_(f"{path.name}: invalid existing published_at")
    return value


def validate_private_policy(private):
    if not isinstance(private, dict):
        raise ImportError_("--private-terms must be an object")
    for field in ("sentence_terms", "deny_regexes", "deny_literals"):
        values = private.get(field, [])
        if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
            raise ImportError_(f"--private-terms {field} must be a list of nonempty strings")
    try:
        for pattern in private.get("deny_regexes", []):
            re.compile(pattern, re.I)
    except re.error as exc:
        raise ImportError_("--private-terms deny_regexes contains an invalid regex") from exc


def atomic_write(target: Path, text: str):
    """A failed write must leave the previously published file intact."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=target.parent, prefix=f".{target.name}.",
                                         suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            if handle.write(text) != len(text):
                raise OSError("incomplete output write")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def run(src: Path, out: Path, exported_at: str, private: dict, include_machine: bool) -> dict:
    parse_z(exported_at)
    validate_private_policy(private)
    scrub = Scrubber(private.get("sentence_terms", []))
    gate = Gate(private.get("deny_regexes", []), private.get("deny_literals", []))
    tdir = src / "transcripts"
    adir = src / "analysis"
    source_paths = {}
    for directory, pattern in ((tdir, "*.txt"), (adir, "*.json")):
        if not directory.is_dir():
            raise ImportError_(f"missing source directory: {directory}")
        paths = sorted(directory.glob(pattern))
        if not paths:
            raise ImportError_(f"empty source directory: {directory}")
        source_paths[directory.name] = paths
        source_names = {path.name for path in paths}
        missing = sorted(path.name for path in (out / directory.name).glob(pattern)
                         if path.name not in source_names)
        if missing:
            raise ImportError_(f"incomplete {directory.name} source: missing {len(missing)} existing files")
    run_log = load_run_log(tdir / "run.log")
    models = load_manifest_models(tdir / "manifest.jsonl")
    report = {"retrieved_at": {"run_log": 0, "mtime": 0, "header": 0}, "held": {}, "quotes": {},
              "source_quotes": {}}

    files: dict[str, str] = {}
    transcripts: dict[str, dict] = {}
    captions: dict[str, Caption] = {}
    for path in source_paths["transcripts"]:
        vid = path.stem
        if not VIDEO_ID.fullmatch(vid) or path.is_symlink():
            raise ImportError_(f"unsafe transcript name: {path.name}")
        raw = parse_raw_transcript(path)
        if raw.get("source") == "whisper" and not include_machine:
            report["held"][vid] = "machine transcript (use --include-machine-transcripts)"
            continue
        if raw.get("retrieved_at"):
            retrieved_at = iso_z(parse_z(raw["retrieved_at"]))
            report["retrieved_at"]["header"] += 1
        else:
            mtime = path.stat().st_mtime
            near = [t for t in run_log.get(vid, []) if abs(t - mtime) <= 2]
            if near:
                retrieved_at = iso_z(min(near, key=lambda t: abs(t - mtime)))
                report["retrieved_at"]["run_log"] += 1
            else:
                retrieved_at = iso_z(mtime)
                report["retrieved_at"]["mtime"] += 1
        text = build_transcript(vid, raw, retrieved_at, models.get(vid))
        problems = gate.problems(text)
        if problems:
            report["held"][vid] = "leak gate: " + ",".join(problems)
            continue
        files[f"transcripts/{vid}.txt"] = text
        transcripts[vid] = {"sha256": sha256_text(raw["body"]), "retrieved_at": retrieved_at}
        captions[vid] = Caption(raw["body"])

    if not transcripts:
        raise ImportError_("no transcripts eligible for export")

    analyses = 0
    for path in source_paths["analysis"]:
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ImportError_(f"{path.name}: analysis must be an object")
        vid = raw.get("vid")
        if not isinstance(vid, str) or vid != path.stem:
            raise ImportError_(f"{path.name}: vid does not match filename")
        if vid not in transcripts:
            report["held"].setdefault(vid, "analysis without published transcript")
            continue
        rel = f"analysis/{vid}.json"
        projected = project_analysis(raw, transcripts[vid], captions[vid], scrub, report["quotes"],
                                     existing_published_at(out / rel))
        files[rel] = dump_json(projected, 2)
        analyses += 1

    catalog_path = src / "synthesis" / "catalog.json"
    raw_bytes = catalog_path.read_bytes()
    catalog = project_catalog(json.loads(raw_bytes), raw_bytes, exported_at, scrub, captions,
                              report["source_quotes"])
    published_catalog = out / "data" / "catalog.json"
    if published_catalog.exists():
        published = json.loads(published_catalog.read_text(encoding="utf-8"))
        if not isinstance(published, dict) or published.get("frozen") is not True:
            raise ImportError_("existing catalog is not a frozen catalog")
        existing = published.get("techniques")
        if not isinstance(existing, list) or not existing or any(
            not isinstance(item, dict) or not isinstance(item.get("id"), str)
            for item in existing
        ):
            raise ImportError_("existing frozen catalog has invalid technique IDs")
        if [item["id"] for item in existing] != [item["id"] for item in catalog["techniques"]]:
            raise ImportError_("source catalog does not preserve frozen technique ID sequence")
    files["data/catalog.json"] = dump_json(catalog, 1)

    for rel, text in files.items():
        if rel.startswith("transcripts/"):
            continue
        # Scan decoded keys and values as well as serialized output. JSON escaping
        # can otherwise hide whitespace or punctuation from policy patterns.
        def strings(value):
            if isinstance(value, str):
                yield value
            elif isinstance(value, dict):
                for key, child in value.items():
                    yield key
                    yield from strings(child)
            elif isinstance(value, list):
                for child in value:
                    yield from strings(child)

        problems = set(gate.problems(text))
        for value in strings(json.loads(text)):
            problems.update(gate.problems(value))
        if problems:
            raise ImportError_(f"leak gate blocked {rel}: {','.join(sorted(problems))}")

    for pattern in ("transcripts/*.txt", "analysis/*.json"):
        for stale in out.glob(pattern):
            if stale.relative_to(out).as_posix() not in files:
                stale.unlink()
    for rel, text in sorted(files.items()):
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        atomic_write(target, text)

    report.update({
        "status": "ok",
        "transcripts": len(transcripts),
        "analyses": analyses,
        "techniques": catalog["technique_count"],
        "id_list_sha256": catalog["id_list_sha256"],
        "source_catalog_sha256": catalog["source_catalog_sha256"],
        "redactions": dict(sorted(scrub.counts.items())),
    })
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--src", required=True, type=Path, help="local corpus directory")
    parser.add_argument("--out", required=True, type=Path, help="repository checkout to write into")
    parser.add_argument("--exported-at", required=True, help="UTC timestamp, YYYY-MM-DDTHH:MM:SSZ")
    parser.add_argument("--private-terms", required=True, type=Path,
                        help="local JSON {sentence_terms, deny_regexes, deny_literals}; never commit it")
    parser.add_argument("--include-machine-transcripts", action="store_true",
                        help="also publish Whisper transcripts (needs the machine-transcript label contract)")
    args = parser.parse_args(argv)
    try:
        private = json.loads(args.private_terms.read_text(encoding="utf-8"))
        validate_private_policy(private)
        if not any(private.get(k) for k in ("sentence_terms", "deny_regexes", "deny_literals")):
            raise ValueError("--private-terms must define at least one sentence term, deny regex or deny literal")
        report = run(args.src, args.out, args.exported_at, private, args.include_machine_transcripts)
    except (ImportError_, OSError, ValueError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(report, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
