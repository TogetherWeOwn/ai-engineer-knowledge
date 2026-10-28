---
{
  "type": "technique",
  "id": "deployment-placement",
  "title": "Choose approved execution placement from measured needs instead of defaulting every session to the cloud",
  "area": "sandbox-compute",
  "status": "stable",
  "valid_from": "2026-10-04T15:00:15Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "pyvRID_CZZU",
      "resource": "https://www.youtube.com/watch?v=pyvRID_CZZU",
      "title": "We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI",
      "author": "AssemblyAI",
      "last_modified": "2026-10-04T15:00:15Z",
      "analysis_file": "analysis/pyvRID_CZZU.json"
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

# Choose approved execution placement from measured needs instead of defaulting every session to the cloud

## What

Choose approved execution placement from measured needs instead of defaulting every session to the cloud

The agent is a Dockerfile deployed on Railway so every repo push auto-deploys with no manual instance management.

## Evidence

Source analysis [^pyvRID_CZZU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable idle and duplicated compute
- **Speed:** Reduce measured execution/queue bottlenecks
- **Quality:** Reproducible command and environment evidence
- **Reliability:** Isolation, cleanup and recovery guarantees
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^pyvRID_CZZU]: [We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](https://www.youtube.com/watch?v=pyvRID_CZZU); publication: 2026-10-04T15:00:15Z; analysis: `analysis/pyvRID_CZZU.json`.
