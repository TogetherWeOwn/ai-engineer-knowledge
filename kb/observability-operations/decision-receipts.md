---
{
  "type": "technique",
  "id": "decision-receipts",
  "title": "Record accountable version-bound decisions with evidence and a rollback path",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-07-30T02:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "tJFjeMBKbIY",
      "resource": "https://www.youtube.com/watch?v=tJFjeMBKbIY",
      "title": "Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings",
      "author": "Shawn Chan, China Resources Holdings",
      "last_modified": "2026-07-30T02:00:06Z",
      "analysis_file": "analysis/tJFjeMBKbIY.json"
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

# Record accountable version-bound decisions with evidence and a rollback path

## What

Record accountable version-bound decisions with evidence and a rollback path

Record the responsible actor, exact artifact version, decision and time; accountability must not disappear behind an agent.

## Evidence

> and is logged. Who's Who reviewed what change when they signed. That log is
> — 22:23 [^tJFjeMBKbIY]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^tJFjeMBKbIY]: [Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings](https://www.youtube.com/watch?v=tJFjeMBKbIY); publication: 2026-07-30T02:00:06Z; analysis: `analysis/tJFjeMBKbIY.json`.
