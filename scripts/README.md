# Pipeline scripts

- `check_rss.py` — polls the channel RSS feed and writes
  `state/missing_transcripts.json` listing videos with no transcript yet.
  Safe anywhere; it reads only the public feed.
- `generate_claims.py` — deterministic claims generator. Reads
  `analysis/*.json`, writes `claims/`, `areas/`, `catalog.json`, `llms.txt`
  and `llms-full.md`. See the recency rules in the repo README.

Two pipeline stages deliberately do **not** run from CI:

- **Transcript fetching** needs residential egress (caption hosts reject
  datacenter IPs). It runs from a home connection and commits
  `transcripts/<video_id>.txt` files. Never add caption fetching to a
  workflow in this repo.
- **Analysis** (transcript → `analysis/*.json`) runs against newly
  committed transcripts and must emit the contract in
  `docs/analysis-schema.md`, including each talk's publish date.

Both stages land here as scripts alongside the corpus they operate on.
