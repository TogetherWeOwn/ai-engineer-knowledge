---
{
  "type": "technique",
  "id": "condition-waits",
  "title": "Wait on explicit conditions with deadlines instead of blind sleeps or repeated model polls",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-07-08T13:45:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "iRcX54EO5g8",
      "resource": "https://www.youtube.com/watch?v=iRcX54EO5g8",
      "title": "Your agent is blindfolded — Johan Lajili, Poolside AI",
      "author": "Johan Lajili, Poolside AI",
      "last_modified": "2026-07-08T13:45:06Z",
      "analysis_file": "analysis/iRcX54EO5g8.json"
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

# Wait on explicit conditions with deadlines instead of blind sleeps or repeated model polls

## What

Wait on explicit conditions with deadlines instead of blind sleeps or repeated model polls

Repeated sleep calls indicate missing synchronization primitives; wait for a concrete event or readiness condition instead.

## Evidence

> everywhere is a stink that like there is something that should be wait for
> — 09:05 [^iRcX54EO5g8]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^iRcX54EO5g8]: [Your agent is blindfolded — Johan Lajili, Poolside AI](https://www.youtube.com/watch?v=iRcX54EO5g8); publication: 2026-07-08T13:45:06Z; analysis: `analysis/iRcX54EO5g8.json`.
