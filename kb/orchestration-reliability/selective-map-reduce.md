---
{
  "type": "technique",
  "id": "selective-map-reduce",
  "title": "Map exhaustively with cheap code and apply semantic reduction only where needed",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-08-19T18:00:17Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "XAsb7MIAzm8",
      "resource": "https://www.youtube.com/watch?v=XAsb7MIAzm8",
      "title": "Don’t be data poor — Anuj Iravane, Anterior",
      "author": "Anuj Iravane, Anterior",
      "last_modified": "2026-08-19T18:00:17Z",
      "analysis_file": "analysis/XAsb7MIAzm8.json"
    },
    {
      "id": "jRCpXUjz4CI",
      "resource": "https://www.youtube.com/watch?v=jRCpXUjz4CI",
      "title": "Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute",
      "author": "Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute",
      "last_modified": "2026-07-24T16:00:06Z",
      "analysis_file": "analysis/jRCpXUjz4CI.json"
    },
    {
      "id": "xIt_mTQp6mY",
      "resource": "https://www.youtube.com/watch?v=xIt_mTQp6mY",
      "title": "Loop Engineering from First Principles — Kyle Mistele, HumanLayer",
      "author": "Kyle Mistele, HumanLayer",
      "last_modified": "2026-07-25T20:41:40Z",
      "analysis_file": "analysis/xIt_mTQp6mY.json"
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

# Map exhaustively with cheap code and apply semantic reduction only where needed

## What

Map exhaustively with cheap code and apply semantic reduction only where needed

Spend low cost per independent extraction and reserve more capable synthesis only where aggregation actually needs semantic judgment.

## Evidence

Source analysis [^XAsb7MIAzm8]; no independently matched timestamped quote published.

> it's cheap and fast. And then I do the reduce step with fable 5 because I
> — 17:32 [^jRCpXUjz4CI]

> will be both cheaper and more reliable since each migration gets its own
> — 16:45 [^xIt_mTQp6mY]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^XAsb7MIAzm8]: [Don’t be data poor — Anuj Iravane, Anterior](https://www.youtube.com/watch?v=XAsb7MIAzm8); publication: 2026-08-19T18:00:17Z; analysis: `analysis/XAsb7MIAzm8.json`.
[^jRCpXUjz4CI]: [Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](https://www.youtube.com/watch?v=jRCpXUjz4CI); publication: 2026-07-24T16:00:06Z; analysis: `analysis/jRCpXUjz4CI.json`.
[^xIt_mTQp6mY]: [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](https://www.youtube.com/watch?v=xIt_mTQp6mY); publication: 2026-07-25T20:41:40Z; analysis: `analysis/xIt_mTQp6mY.json`.
