# Pipeline scripts

- `backfill_publish_dates.py` — first data deliverable: reads real
  `analysis/*.json` with `vid`, preserves other fields, backfills aware
  `published_at` from YouTube `videos.list` metadata, storing the exact API
  string verbatim. `--check` is offline; `--dry-run` fetches without
  writing. All output is JSON. See root README for exits, the >=95%
  coverage gate and the repo-scoped key requirement. Live runs go through
  the manual `backfill` workflow (single writer, stages `analysis/*.json`
  only).
- `supadata_canary.py` — five-video canary gate: fetches
  `mode=native&lang=en` captions and compares each against its conforming
  `transcripts/<vid>.txt` reference (>=0.98 word similarity, HTTP 200, no
  206). `--vids` takes exactly 5 IDs; `--out` writes the JSON report.
  Dispatch from the manual `canary` workflow on `ubuntu-latest` only.
  Procedure: `docs/canary.md`.
- `check_rss.py` — legacy RSS discovery. It currently checks public caption
  filenames; its missing-file list is not an ingestion queue. It fetches no
  captions. Provenance-based discovery is pending.
- `generate_claims.py` — initial scaffold only, **not the corrected generator**.
  It uses slug identities and overwrites `catalog.json`; do not run it over
  the frozen 475-cluster catalog or on real imported data.

The next migration is one-shot from the actual catalog, not a nonexistent
synthesis builder. Public analysis prompts must be generic. The planned
caption source is Supadata native/en, canary-gated on five videos with >=98%
word similarity; TranscriptAPI then Apify are fallbacks subject to authorized
access and no new spend. Full transcripts are published under
`transcripts/` per the format in `transcripts/README.md`; bulk retrieval
stays canary-gated.

Independent acceptance tests and actual corpus import precede resuming
publication. The target bundle contract is in `docs/analysis-schema.md`.
