---
{
  "type": "technique",
  "id": "pareto-tradeoffs",
  "title": "Retain non-dominated candidates when quality, cost and latency objectives conflict",
  "area": "evaluation-measurement",
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
    },
    {
      "id": "bMjlRrWjdT0",
      "resource": "https://www.youtube.com/watch?v=bMjlRrWjdT0",
      "title": "AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "author": "Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "last_modified": "2026-08-28T15:00:03Z",
      "analysis_file": "analysis/bMjlRrWjdT0.json"
    },
    {
      "id": "hqHC6Z_lXyo",
      "resource": "https://www.youtube.com/watch?v=hqHC6Z_lXyo",
      "title": "20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna",
      "author": "Bertrand Charpentier, Pruna",
      "last_modified": "2026-06-01T17:00:06Z",
      "analysis_file": "analysis/hqHC6Z_lXyo.json"
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

# Retain non-dominated candidates when quality, cost and latency objectives conflict

## What

Retain non-dominated candidates when quality, cost and latency objectives conflict

Discard dominated options, then choose among non-dominated choices according to the actual task quality threshold and efficiency constraints.

## Evidence

> that wins on even one training example and not just the top scorer. The
> — 08:56 [^OA-Mc60Rboo]

Source analysis [^bMjlRrWjdT0]; no independently matched timestamped quote published.

> single state of the art model, but there are actually multiple of them and there
> — 14:59 [^hqHC6Z_lXyo]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^OA-Mc60Rboo]: [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](https://www.youtube.com/watch?v=OA-Mc60Rboo); publication: 2026-09-26T17:00:06Z; analysis: `analysis/OA-Mc60Rboo.json`.
[^bMjlRrWjdT0]: [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](https://www.youtube.com/watch?v=bMjlRrWjdT0); publication: 2026-08-28T15:00:03Z; analysis: `analysis/bMjlRrWjdT0.json`.
[^hqHC6Z_lXyo]: [20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna](https://www.youtube.com/watch?v=hqHC6Z_lXyo); publication: 2026-06-01T17:00:06Z; analysis: `analysis/hqHC6Z_lXyo.json`.
