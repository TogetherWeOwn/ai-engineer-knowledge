---
{
  "type": "technique",
  "id": "prefetch-watermarks",
  "title": "Prefetch proven next work with bounded low-watermark queues",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-10-10T01:30:14Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "_KFbT6eph5A",
      "resource": "https://www.youtube.com/watch?v=_KFbT6eph5A",
      "title": "Using AI to Build an Infinite Game: Jeff Schomay",
      "author": null,
      "last_modified": "2024-02-01T17:41:28Z",
      "analysis_file": "analysis/_KFbT6eph5A.json"
    },
    {
      "id": "tNAV259UhCM",
      "resource": "https://www.youtube.com/watch?v=tNAV259UhCM",
      "title": "From 15% to 90% GPU Utilization: Fix the Data Pipeline, Not the Model",
      "author": null,
      "last_modified": "2026-10-10T01:30:14Z",
      "analysis_file": "analysis/tNAV259UhCM.json"
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

# Prefetch proven next work with bounded low-watermark queues

## What

Prefetch proven next work with bounded low-watermark queues

Because generation took 10-30s, he pre-generated a pool of scenes and refilled it whenever it dropped below a threshold, so a ready item was always available.

## Evidence

Source analysis [^_KFbT6eph5A]; no independently matched timestamped quote published.

Source analysis [^tNAV259UhCM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^_KFbT6eph5A]: [Using AI to Build an Infinite Game: Jeff Schomay](https://www.youtube.com/watch?v=_KFbT6eph5A); publication: 2024-02-01T17:41:28Z; analysis: `analysis/_KFbT6eph5A.json`.
[^tNAV259UhCM]: [From 15% to 90% GPU Utilization: Fix the Data Pipeline, Not the Model](https://www.youtube.com/watch?v=tNAV259UhCM); publication: 2026-10-10T01:30:14Z; analysis: `analysis/tNAV259UhCM.json`.
