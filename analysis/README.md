# Analysis

The real corpus envelope uses `vid`, `takeaways` and string `confidence`.
`scripts/backfill_publish_dates.py` preserves those fields and fills only
`published_at` from YouTube Data API v3 metadata. See the full
[input/publication contract](../docs/analysis-schema.md).

Only sanitized, generic analysis belongs here. Full captions live in
`transcripts/*.txt` with the required provenance header (source URL, credit,
`retrieved_at`, SHA256, unverified label); do not duplicate caption bodies
into analysis files, and do not commit private configuration,
organization-specific mappings, internal identifiers, paths or status
fields. Public provenance includes transcript SHA256 and `retrieved_at`,
plus short timestamped quotes verified against actual captions.

The legacy generator is not the migration adapter. Do not run it over the
real frozen source catalog; it currently overwrites `catalog.json`.
