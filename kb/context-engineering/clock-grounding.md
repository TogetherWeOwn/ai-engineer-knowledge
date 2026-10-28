---
{
  "type": "technique",
  "id": "clock-grounding",
  "title": "Inject the host clock and explicit time windows instead of relying on model time knowledge",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2025-07-18T18:52:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "bmWZk9vTze0",
      "resource": "https://www.youtube.com/watch?v=bmWZk9vTze0",
      "title": "MCP is all you need — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-07-18T18:52:25Z",
      "analysis_file": "analysis/bmWZk9vTze0.json"
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

# Inject the host clock and explicit time windows instead of relying on model time knowledge

## What

Inject the host clock and explicit time windows instead of relying on model time knowledge

Explicit time context prevents queries or reports from using a stale training-era year.

## Evidence

> it doesn't uh assume it's 20 2023 as they often do. Um and now we can go and
> — 12:51 [^bmWZk9vTze0]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^bmWZk9vTze0]: [MCP is all you need — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=bmWZk9vTze0); publication: 2025-07-18T18:52:25Z; analysis: `analysis/bmWZk9vTze0.json`.
