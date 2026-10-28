---
{
  "type": "technique",
  "id": "policy-conflict-audit",
  "title": "Detect contradictory or obsolete instructions while preserving real enforced policy",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-07-15T15:05:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "avWhreBUYF0",
      "resource": "https://www.youtube.com/watch?v=avWhreBUYF0",
      "title": "#define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)",
      "author": "Greg Brockman, OpenAI (ft. Jensen Huang)",
      "last_modified": "2025-08-10T16:00:06Z",
      "analysis_file": "analysis/avWhreBUYF0.json"
    },
    {
      "id": "uU5Gv2h8-9g",
      "resource": "https://www.youtube.com/watch?v=uU5Gv2h8-9g",
      "title": "Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison",
      "author": "Cat Wu & Thariq Shihipar ft Simon Willison",
      "last_modified": "2026-07-15T15:05:06Z",
      "analysis_file": "analysis/uU5Gv2h8-9g.json"
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

# Detect contradictory or obsolete instructions while preserving real enforced policy

## What

Detect contradictory or obsolete instructions while preserving real enforced policy

Rules that are only usually correct can confuse agents when presented as unconditional constraints; supply context and remove conflicting soft guidance.

## Evidence

Source analysis [^avWhreBUYF0]; no independently matched timestamped quote published.

> this statement is like 90% true, but there's like a real 10% of cases where
> — 23:21 [^uU5Gv2h8-9g]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^avWhreBUYF0]: [#define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)](https://www.youtube.com/watch?v=avWhreBUYF0); publication: 2025-08-10T16:00:06Z; analysis: `analysis/avWhreBUYF0.json`.
[^uU5Gv2h8-9g]: [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](https://www.youtube.com/watch?v=uU5Gv2h8-9g); publication: 2026-07-15T15:05:06Z; analysis: `analysis/uU5Gv2h8-9g.json`.
