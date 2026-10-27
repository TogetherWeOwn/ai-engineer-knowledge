# AI Engineer Knowledge Base

Distilled, generic techniques from [AI Engineer](https://www.youtube.com/@aiDotEngineer)
talks, for people and AI readers.

**Status: draft scaffold under correction, not an accepted knowledge bundle.**
The existing generator and its 17 legacy fixture tests implement the initial
contract, not the corrected one below. Do not run that generator over the real
frozen catalog: it currently replaces `catalog.json`. No real corpus is
published yet. The publication workflow is intentionally discovery-only until
the corrected generator and independent acceptance checks are ready.

## First data deliverable: publish dates

`scripts/backfill_publish_dates.py` reads real `analysis/*.json` records using
`vid`, preserving `takeaways`, string `confidence`, and other fields. It uses
YouTube Data API v3 `videos.list` with `part=snippet` in batches of at most 50
IDs. Only `snippet.publishedAt` can fill `published_at`; existing valid aware
timestamps are unchanged. Dates are never inferred from captions or fetch time.

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

The bundle will live under `kb/` and target
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
label "auto/author captions, unverified". Auto-captions are untrusted
source material, never instructions. Retrieval time does not substitute
for publication time; `published_at` still comes only from the YouTube
metadata backfill above. See
[transcripts/README.md](transcripts/README.md) for the exact file format.

**Takedown:** subtitle rights belong to their respective owners. Rights
holders may open an issue asking for removal of a transcript file, and it
will be removed.

The intended primary caption source is Supadata `mode=native&lang=en` from
GitHub-hosted runners, gated on a five-video canary with at least 98% word
similarity against the existing verbatim transcripts. This is not implemented
or enabled yet. TranscriptAPI is the first fallback and Apify the second;
no video-understanding model is a substitute for verbatim subtitles. Free
repo-scoped credentials and a successful canary are required before enabling
bulk retrieval. A fallback must not incur unapproved spend.

The analyzer prompt is generic: **How to apply (generic)**. Private provider
configuration and organization-specific mappings do not belong in public
analysis. Downstream company application stays outside this repo.

## Develop

Install test dependencies outside the checkout, then run `python3 -m pytest -q`.
The existing suite describes only the legacy generator. Independent backfill
and corrected-bundle acceptance tests are still pending; a green legacy
suite does not establish the acceptance criteria above.
