# Frozen technique catalog

`data/catalog.json` is the frozen source catalog that the knowledge base is
built from. It holds 475 technique clusters, each consolidated from talks on
the AI Engineer channel. `scripts/import_corpus.py` exported it once from
the research catalog. That was a one-shot migration with no LLM re-read, and
it does not reproduce the clustering.

**Frozen identities.** Every technique `id` is kept unchanged and in its
original order. A generator may read this file but must never write it.
New videos attach to existing IDs, and any new identity needs an explicit,
validated extension path (see `docs/analysis-schema.md`). The root
`catalog.json` belongs to the legacy generator. It is a different file.

Integrity:

| Field | Value |
|---|---|
| `technique_count` | 475 |
| `id_list_sha256` | `72caeca5055237e6dbd261a741f23aaf01476a9f0093f5340940be981ed920b5` |
| `source_catalog_sha256` | `1ffb5ee38cfb7d91e0eeb62044c57a20a06684e27b3a75697399f53691afcd81` |

`id_list_sha256` is the SHA-256 of the IDs, sorted, joined with `\n` and
ending with a trailing `\n`. `source_catalog_sha256` identifies the
unpublished input that was exported.

## Root fields

- `schema_version`, `title`, `generated_at`: from the source catalog.
- `export_version` (`public-1`), `exported_at`, `frozen` (`true`), `note`.
- `areas`: the 18 technique areas.
- `counts`: input record and talk counts for the whole source catalog,
  `techniques` (475), and `techniques_per_area`. The record counts include
  a small number of clusters that were not exported.
- `source_scope`, `methodology`, `validation`: how the catalog was built and
  checked. `validation.independent_checks` and `failures` describe the
  source catalog build.

## Technique fields

- `id`, `title`, `area`.
- `source`: `deep-read`, `triage-only` or `mixed`. `evidence_level` is
  `deep-read` when at least one full-talk reading supports the cluster.
  Triage-only clusters remain provisional.
- `source_count` (distinct talks), `source_record_count`,
  `deep_read_source_count`, `triage_only_source_count`.
- `quote_evidence`: the number of sources per `quote_verification` label.
- `mechanism`: `summary`, `representative_explanation`,
  `representative_record_id`, and `variants[]` (`title`,
  `source_record_ids`).
- `expected_benefit`: directional `cost`, `speed`, `quality`,
  `reliability` and `certainty`. These are expected directions, not
  measured gains, and gains across clusters overlap.
- `risk`: `level`, `failure_modes[]` and `mitigation`.
- `how_to_measure_success`: `metrics[]` and `acceptance`.
- `reported_measurements[]`: `text` and `source_record_ids`. These are
  speaker or reader reports. They have not been independently reproduced.
- `sources[]`: one entry per supporting record (see below).

Three display titles were generalized because they were phrased for a single
organization's tracker: `structured-observability`, `work-deduplication` and
`retrieval-evaluation`. Their IDs did not change.

## Source fields

- `record_id`, `vid`, `talk` (the video title), `url` (a watch URL with a
  time offset), `source` (`deep-read` or `triage-only`).
- `quote`, `timestamp`, `timestamp_end`: a verbatim excerpt of
  `transcript_file`, with timestamp labels removed and line breaks kept.
  The import re-checked every quote against the published transcript. A
  quote that is not found there is set to `null`, with
  `quote_verification: not-found-in-published-transcript`.
- `quote_verification`, `quote_match_score`, `matching_occurrences`,
  `requires_confirmation`, `quote_is_verbatim_original`: describe how the
  quote location was matched to what the reader reported.
- `additional_original_excerpts[]`: extra verbatim excerpts, for example
  the original-script text on a mis-detected caption track.
- `input_technique`, `input_area`, `mechanism_in_source`: the reader's
  description of the technique in that talk.
- `triage_interpretation_requires_confirmation`: present on triage-only
  records.
- `transcript_file`: `transcripts/<vid>.txt`.

**Which quotes count as verified.** Only `normalized-exact` and
`manual-original-excerpt` locate the reported quote verbatim.
`ordered-ellipsis-pieces` and `fuzzy-location-needs-confirmation` are not
"verified". A generator must render only the first two as verified quotes,
and must label the others for confirmation.

## Imported per-video analysis (`analysis/<vid>.json`)

The same import writes one analysis file per video. It contains:

- `vid`, `title`, `source` (the watch URL), and `talk_summary` (scrubbed).
- `takeaways[]`, each with:
  - `area`, `technique`, `what_they_do`, `numbers`;
  - `confidence`, kept as the original string (`low`, `medium` or `high`);
  - `evidence_quote` and `evidence_quote_verification`, which is one of
    `normalized-exact`, `ordered-ellipsis-pieces` or `not-found-in-captions`.
    A quote that is not found is set to `null`;
  - `evidence_timestamp`: the `[mm:ss]` of the first caption line the quote
    matched.
- `confidence`, on a few files only (a string).
- `truncated`, `analyzed_at`, and `analyzer` (the model family).
- `transcript_file`, `transcript_sha256` and `retrieved_at`. These equal the
  header of the transcript file.
- `published_at`: filled later by `scripts/backfill_publish_dates.py` from
  YouTube `videos.list`. It is absent until then. A rerun of the import
  keeps any existing value.

## Privacy boundary

The export copies allowlisted fields only. Organization-specific
application notes, status, effort and priority fields, and local file paths
are not exported. Generated prose was scrubbed one sentence at a time: any
sentence written relative to the analyst's own organization was dropped, and
a field with nothing left became `null`. Verbatim caption excerpts are never
edited.
