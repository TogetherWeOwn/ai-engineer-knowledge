---
{
  "type": "technique",
  "id": "explicit-anti-goals",
  "title": "State explicit anti-goals and prohibited outcomes alongside acceptance criteria",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-09-26T15:00:32Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "vrDvatGtIxs",
      "resource": "https://www.youtube.com/watch?v=vrDvatGtIxs",
      "title": "Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph",
      "author": "Tejas Bhakta, Morph",
      "last_modified": "2026-09-26T15:00:32Z",
      "analysis_file": "analysis/vrDvatGtIxs.json"
    }
  ],
  "relations": [],
  "relation_transitions": {},
  "generated": {
    "by": "scripts/generate_claims.py",
    "at": "2026-10-28T21:30:11.661690Z"
  },
  "stale_after": "2027-01-26T21:30:11.661690Z"
}
---

# State explicit anti-goals and prohibited outcomes alongside acceptance criteria

## What

State explicit anti-goals and prohibited outcomes alongside acceptance criteria

Give the agent a written list of forbidden shortcuts (e.g. don't disable CUDA graphs, don't only test small contexts) because agents optimize the metric by cheating.

## Evidence

Source analysis [^vrDvatGtIxs]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^vrDvatGtIxs]: [Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph](https://www.youtube.com/watch?v=vrDvatGtIxs); publication: 2026-09-26T15:00:32Z; analysis: `analysis/vrDvatGtIxs.json`.
