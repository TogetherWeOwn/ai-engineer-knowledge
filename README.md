# AI Engineer Knowledge Base

Distilled techniques from [AI Engineer](https://www.youtube.com/@aiDotEngineer)
talks, in a form both people and AI tools can read. Everything here is
generated from verbatim caption transcripts, and it is **recency-aware**:
when a newer talk covers the same technique, the newer claim supersedes the
older one. Superseded claims are never deleted — they stay in the tree,
marked, with a pointer to what replaced them.

## Read it

- [`llms.txt`](llms.txt) — short router for AI readers (start here)
- [`llms-full.md`](llms-full.md) — every active technique, full text
- [`catalog.json`](catalog.json) — every claim's metadata, for machines
- [`claims/`](claims) — one Markdown file per technique claim, by area
- [`areas/`](areas) — one index page per area

Each claim file carries YAML frontmatter (`type`, `id`, `title`, `area`,
`status`, `valid_from`, `valid_to`, `superseded_by`, `confidence`,
`relevance`, `sources`) and four body sections: **What**, **Evidence**,
**Apply to us**, **Expected effect**.

## Recency rules

1. Claims are ordered by the talk's publish date.
2. A newer talk on the same technique supersedes the older claim
   (`status: superseded`, `superseded_by`, `valid_to`).
3. A talk with an unknown date never supersedes a dated claim.
4. Nothing is ever deleted.

These rules live in [`scripts/generate_claims.py`](scripts/generate_claims.py)
and are covered by tests in [`tests/`](tests).

## How it is built

```
caption transcripts ─► per-talk analysis ─► claims generator ─► this tree
transcripts/*.txt      analysis/*.json      scripts/generate_claims.py
```

- **Transcripts** are untrusted auto-captions, fetched from a residential
  connection (caption hosts reject datacenter IPs) and committed here.
  Automation in this repo never fetches captions.
- **Analysis** files follow [`docs/analysis-schema.md`](docs/analysis-schema.md)
  and record each talk's publish date, source URL and retrieval time.
- **Generation** is deterministic: same inputs, same bytes. A weekly
  GitHub Actions workflow polls the channel RSS feed
  ([`scripts/check_rss.py`](scripts/check_rss.py) lists videos still missing
  a transcript), regenerates the tree from committed analyses, and commits
  the result.

## Develop

```sh
pip install pytest pyyaml
pytest -q
python3 scripts/generate_claims.py            # regenerate the tree
python3 scripts/generate_claims.py --check    # fail if the tree is stale
```

Claim files, `areas/`, `catalog.json`, `llms.txt` and `llms-full.md` are
generated. Do not edit them by hand; change the analysis or the generator.
