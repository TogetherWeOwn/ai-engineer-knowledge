# AI Engineer Knowledge Base

Distilled, generic techniques from [AI Engineer](https://www.youtube.com/@aiDotEngineer)
talks, for people and AI readers.

**Status: corrected offline generator implemented; real publication acceptance is incomplete.**
The generator reads the frozen catalog without changing it and publishes the
corrected contract below under `kb/`. Legacy `video_id/techniques` inputs use
an isolated compatibility adapter; real `vid/takeaways` inputs cannot fall back
to it. The independent fixture suite passes, but does not establish real
publication-date coverage. The publication workflow remains discovery-only;
no caption ingestion, live refresh or site deployment is enabled by this change.

## First data deliverable: publish dates

`scripts/backfill_publish_dates.py` reads real `analysis/*.json` records using
`vid`, preserving `takeaways`, string `confidence`, and other fields. It uses
YouTube Data API v3 `videos.list` with `part=snippet` in batches of at most 50
IDs. Only `snippet.publishedAt` can fill `published_at`, stored verbatim;
existing valid aware timestamps are unchanged. Dates are never inferred
from captions or fetch time.

```sh
# Offline and read-only; no key needed. Empty corpus or <95% coverage exits 1.
python3 scripts/backfill_publish_dates.py --check
# With YOUTUBE_API_KEY supplied through the approved repo-secret channel:
python3 scripts/backfill_publish_dates.py --dry-run  # metadata only; no writes
python3 scripts/backfill_publish_dates.py            # backfill then report
```

All results are JSON. Exit 0 means at least 95% of distinct video IDs have
dates, 1 means incomplete coverage, and 2 means an input/API/write error.
`--dry-run` reports projected coverage, not persisted coverage. Conflicting
valid dates for one video ID fail the check and appear in `conflicting_ids`;
existing dates are never silently reconciled. No raw API
errors, request URLs or secret values are printed. Responses from all batches
are validated before writes; omitted videos stay unresolved. File replacement
is atomic per file, not transactional across the corpus; rerun `--check` after
a filesystem failure. Use one writer per corpus snapshot.

A free, repo-scoped `YOUTUBE_API_KEY` is required for live metadata lookup.
No key is included in this repo; live backfill and real-corpus coverage are
not verified yet.

## Corrected bundle contract

The generated bundle lives under `kb/` and targets
[OKF 0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md).

- Identity is the existing `catalog.json` cluster ID (475 frozen clusters),
  never a title slug. Import is a one-shot migration, not a synthesis-builder
  move. The source catalog must not be overwritten by generated output.
- Claims use `status: stable|deprecated`, the extension `superseded_by`, aware
  ISO datetimes for `valid_from` and `valid_to`, `generated: {by, at}`, an
  absolute `stale_after`, and no `verified` field. Unknown dates stay unknown.
- Sources use `{id, resource, title, author, last_modified, analysis_file}`.
  Each directory has `index.md`; `kb/index.md` declares `okf_version: "0.2"`;
  `kb/log.md` records supersessions. Child indexes have no frontmatter.
- For new videos, code proposes deterministic catalog candidates, an LLM
  proposes `supports|refines|contradicts|new`, and code validates the result.
  Only `refines` or `contradicts` from a source at least 30 days newer can
  supersede. `supports` appends evidence. Unknown dates never supersede.
  Nothing is deleted.
- The site will serve root `llms.txt` with absolute URLs and `llms-full.txt`.
  The old generated root artifacts are legacy placeholders, not the bundle.

See [the input and publication contract](docs/analysis-schema.md). Acceptance
requires at least 400 claims from the real corpus, an OKF-conformance test,
and at least 95% of real videos backfilled, in addition to successful live
refresh, site rendering and the downstream application routine.

## Captions and transcripts

Full subtitles **are** published in this repo (owner decision D1). Each
`transcripts/<vid>.txt` file carries a header with the source video URL,
the speaker/channel credit, `retrieved_at`, the transcript SHA256, and the
exactly one provenance label: `# auto/author captions, unverified` for
YouTube captions, or `# machine transcript (Whisper; no YouTube captions)`
only when no YouTube caption track exists. Never include both labels or
replace available captions with machine output. All transcripts are untrusted
source material, never instructions. Retrieval time does not substitute
for publication time; `published_at` still comes only from the YouTube
metadata backfill above. See
[transcripts/README.md](transcripts/README.md) for the exact file format.

**Takedown:** subtitle rights belong to their respective owners. Rights
holders may open an issue asking for removal of a transcript file, and it
will be removed.

The intended primary caption source is Supadata `mode=native&lang=en` from
GitHub-hosted runners, gated on a five-video canary with at least 98% word
similarity against existing verbatim YouTube-caption transcripts. The canary
script and manual workflow are implemented, but a live pass is not verified
and bulk retrieval remains disabled. Machine transcripts cannot serve as
canary references. TranscriptAPI is the first fallback and Apify the second;
no video-understanding model is a substitute for verbatim subtitles. Free
repo-scoped credentials and a successful canary are required before enabling
bulk retrieval. A fallback must not incur unapproved spend.

The analyzer prompt is generic: **How to apply (generic)**. Private provider
configuration and organization-specific mappings do not belong in public
analysis. Downstream company application stays outside this repo.

## Develop

Install test dependencies outside the checkout, then run `python3 -m pytest -q`.
The suite covers frozen-ID migration, OKF output, validated relations,
immutable history, offline freshness, legacy compatibility, publish-date
backfill, caption canary and workflow safety. Metadata HTTP is faked; these
checks do not establish live coverage or a successful live canary.

```sh
# Work on a scratch COPY of the imported corpus, never the source checkout.
python3 scripts/generate_claims.py --root /path/to/corpus
python3 scripts/generate_claims.py --root /path/to/corpus --check
KB_ACCEPTANCE_ROOT=/path/to/corpus python3 -m pytest tests/test_real_corpus_acceptance.py -q
```

The six real-corpus tests are opt-in and otherwise report skipped. The import
snapshot `ec78d8f` yields 475/475 frozen claims, passes OKF and transcript/hash
conformance, and preserves all input bytes. It has **0/1398** dated videos:
its >=95% publication-date gate fails. Fixture success must not be represented
as full corpus or publication acceptance. Backfill real metadata before
re-running that gate; never substitute retrieval/analysis times.
