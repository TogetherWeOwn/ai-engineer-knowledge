---
{
  "type": "technique",
  "id": "exception-focused-review",
  "title": "Present exception-focused tables and decisive evidence instead of repetitive prose",
  "area": "review-quality",
  "status": "stable",
  "valid_from": "2026-04-22T15:15:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "XNtkiQJ49Ps",
      "resource": "https://www.youtube.com/watch?v=XNtkiQJ49Ps",
      "title": "Agents need more than a chat - Jacob Lauritzen, CTO Legora",
      "author": "Jacob Lauritzen, CTO Legora",
      "last_modified": "2026-04-22T15:15:06Z",
      "analysis_file": "analysis/XNtkiQJ49Ps.json"
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

# Present exception-focused tables and decisive evidence instead of repetitive prose

## What

Present exception-focused tables and decisive evidence instead of repetitive prose

Show one row per work unit with status, evidence and unresolved choice, so oversight sees exceptions without reading every trace.

## Evidence

> flag a few items for you that I want your take on." And then I can go in
> — 12:36 [^XNtkiQJ49Ps]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer redundant or low-value review rounds
- **Speed:** Shorter evidence-backed review/repair cycles
- **Quality:** Better focus on actionable defects rather than cosmetic scores
- **Reliability:** Independent, revision-bound verification
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^XNtkiQJ49Ps]: [Agents need more than a chat - Jacob Lauritzen, CTO Legora](https://www.youtube.com/watch?v=XNtkiQJ49Ps); publication: 2026-04-22T15:15:06Z; analysis: `analysis/XNtkiQJ49Ps.json`.
