---
{
  "type": "technique",
  "id": "offline-scheduling-policy",
  "title": "Optimize scheduling heuristics on existing traces and execute the selected policy deterministically",
  "area": "model-routing-capacity",
  "status": "stable",
  "valid_from": "2026-09-26T17:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "OA-Mc60Rboo",
      "resource": "https://www.youtube.com/watch?v=OA-Mc60Rboo",
      "title": "Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA",
      "author": "Lakshya A. Agrawal, GEPA",
      "last_modified": "2026-09-26T17:00:06Z",
      "analysis_file": "analysis/OA-Mc60Rboo.json"
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

# Optimize scheduling heuristics on existing traces and execute the selected policy deterministically

## What

Optimize scheduling heuristics on existing traces and execute the selected policy deterministically

A scheduling policy can be scored on recorded job traces and SLA violations; improved code can then run without an LLM making live decisions.

## Evidence

> or heristic algorithm can be expressed as a piece of text and the evaluator can
> — 11:53 [^OA-Mc60Rboo]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Use the cheapest evidenced capable mechanism
- **Speed:** Admit work within real quota and resource limits
- **Quality:** Preserve the role quality floor
- **Reliability:** Avoid exhaustion, unsafe fallback and policy bypass
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^OA-Mc60Rboo]: [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](https://www.youtube.com/watch?v=OA-Mc60Rboo); publication: 2026-09-26T17:00:06Z; analysis: `analysis/OA-Mc60Rboo.json`.
