---
{
  "type": "technique",
  "id": "file-collision-analysis",
  "title": "Measure file-level collision hot spots before assigning concurrent changes",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-04-25T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "kR64LOqBBCU",
      "resource": "https://www.youtube.com/watch?v=kR64LOqBBCU",
      "title": "AgentCraft: Putting the Orc in Orchestration — Ido Salomon",
      "author": "Ido Salomon",
      "last_modified": "2026-04-25T16:00:06Z",
      "analysis_file": "analysis/kR64LOqBBCU.json"
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

# Measure file-level collision hot spots before assigning concurrent changes

## What

Measure file-level collision hot spots before assigning concurrent changes

Maps the filesystem to visible rooms, tracks which agent is editing which file, and uses a heatmap to spot and proactively prevent collisions.

## Evidence

Source analysis [^kR64LOqBBCU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^kR64LOqBBCU]: [AgentCraft: Putting the Orc in Orchestration — Ido Salomon](https://www.youtube.com/watch?v=kR64LOqBBCU); publication: 2026-04-25T16:00:06Z; analysis: `analysis/kR64LOqBBCU.json`.
