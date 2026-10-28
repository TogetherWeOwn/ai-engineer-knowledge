---
{
  "type": "technique",
  "id": "nonblocking-hardening",
  "title": "Move noncritical cleanup off the delivery critical path without weakening required gates",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2024-11-27T19:56:40Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "prttz9_1XDc",
      "resource": "https://www.youtube.com/watch?v=prttz9_1XDc",
      "title": "Enhancing Quality and Security in CI: Gunjan Patel",
      "author": null,
      "last_modified": "2024-11-27T19:56:40Z",
      "analysis_file": "analysis/prttz9_1XDc.json"
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

# Move noncritical cleanup off the delivery critical path without weakening required gates

## What

Move noncritical cleanup off the delivery critical path without weakening required gates

Deliberate background test/security work can use iterations that would be too slow for inline completion, while still proposing rather than silently applying fixes.

## Evidence

> um code review code Reviewer is made to have a deliberate thinking right when
> — 04:06 [^prttz9_1XDc]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^prttz9_1XDc]: [Enhancing Quality and Security in CI: Gunjan Patel](https://www.youtube.com/watch?v=prttz9_1XDc); publication: 2024-11-27T19:56:40Z; analysis: `analysis/prttz9_1XDc.json`.
