---
{
  "type": "technique",
  "id": "dataset-difficulty-refresh",
  "title": "Refresh saturated or too-easy evaluation cases while preserving regression coverage",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-08-12T14:00:19Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "AQv3qRCG6Gw",
      "resource": "https://www.youtube.com/watch?v=AQv3qRCG6Gw",
      "title": "Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect",
      "author": "Will Brown, Prime Intellect",
      "last_modified": "2026-07-31T15:00:06Z",
      "analysis_file": "analysis/AQv3qRCG6Gw.json"
    },
    {
      "id": "W3khHzajE04",
      "resource": "https://www.youtube.com/watch?v=W3khHzajE04",
      "title": "Benchmarks Are Memes: How What We Measure Shapes AI—and Us - Alex Duffy, Every.to",
      "author": "Alex Duffy, Every.to",
      "last_modified": "2025-07-15T17:05:49Z",
      "analysis_file": "analysis/W3khHzajE04.json"
    },
    {
      "id": "iqloyWCGYQQ",
      "resource": "https://www.youtube.com/watch?v=iqloyWCGYQQ",
      "title": "Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley",
      "author": "Parth Asawa, UC Berkeley",
      "last_modified": "2026-08-12T14:00:19Z",
      "analysis_file": "analysis/iqloyWCGYQQ.json"
    },
    {
      "id": "q4Tr-DknG2M",
      "resource": "https://www.youtube.com/watch?v=q4Tr-DknG2M",
      "title": "Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI",
      "author": "Lee Robinson, Cursor, SpaceXAI",
      "last_modified": "2026-07-15T20:13:51Z",
      "analysis_file": "analysis/q4Tr-DknG2M.json"
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

# Refresh saturated or too-easy evaluation cases while preserving regression coverage

## What

Refresh saturated or too-easy evaluation cases while preserving regression coverage

They retire evals when all models hit ~90%, and auto-generate hard tasks by taking a working app, deleting a feature/files so tests fail, and asking the model to reimplement until tests pass.

## Evidence

Source analysis [^AQv3qRCG6Gw]; no independently matched timestamped quote published.

Source analysis [^W3khHzajE04]; no independently matched timestamped quote published.

Source analysis [^iqloyWCGYQQ]; no independently matched timestamped quote published.

Source analysis [^q4Tr-DknG2M]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^AQv3qRCG6Gw]: [Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect](https://www.youtube.com/watch?v=AQv3qRCG6Gw); publication: 2026-07-31T15:00:06Z; analysis: `analysis/AQv3qRCG6Gw.json`.
[^W3khHzajE04]: [Benchmarks Are Memes: How What We Measure Shapes AI—and Us - Alex Duffy, Every.to](https://www.youtube.com/watch?v=W3khHzajE04); publication: 2025-07-15T17:05:49Z; analysis: `analysis/W3khHzajE04.json`.
[^iqloyWCGYQQ]: [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](https://www.youtube.com/watch?v=iqloyWCGYQQ); publication: 2026-08-12T14:00:19Z; analysis: `analysis/iqloyWCGYQQ.json`.
[^q4Tr-DknG2M]: [Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](https://www.youtube.com/watch?v=q4Tr-DknG2M); publication: 2026-07-15T20:13:51Z; analysis: `analysis/q4Tr-DknG2M.json`.
