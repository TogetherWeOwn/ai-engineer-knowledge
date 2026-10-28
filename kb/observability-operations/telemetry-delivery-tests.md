---
{
  "type": "technique",
  "id": "telemetry-delivery-tests",
  "title": "Verify that instrumentation reaches the intended collector and can be queried",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-10-11T15:00:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "YXiLj4tJt5A",
      "resource": "https://www.youtube.com/watch?v=YXiLj4tJt5A",
      "title": "Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS",
      "author": "Elizabeth Fuentes Leone & Sandhya Subramani, AWS",
      "last_modified": "2026-10-11T15:00:05Z",
      "analysis_file": "analysis/YXiLj4tJt5A.json"
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

# Verify that instrumentation reaches the intended collector and can be queried

## What

Verify that instrumentation reaches the intended collector and can be queried

Observability requires both instrumentation and enabled collection; a deployed runtime can appear healthy while missing agent traces.

## Evidence

> you need to enable transaction search so this thing allows you to have the
> — 50:34 [^YXiLj4tJt5A]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^YXiLj4tJt5A]: [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](https://www.youtube.com/watch?v=YXiLj4tJt5A); publication: 2026-10-11T15:00:05Z; analysis: `analysis/YXiLj4tJt5A.json`.
