---
{
  "type": "technique",
  "id": "transport-choice",
  "title": "Choose supported local or remote transport by actual lifecycle and trust requirements",
  "area": "tools-agent-interfaces",
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

# Choose supported local or remote transport by actual lifecycle and trust requirements

## What

Choose supported local or remote transport by actual lifecycle and trust requirements

MCP stdio can simplify local tool lifecycle without deploying another HTTP service, but it provides no filesystem or credential sandbox by itself.

## Evidence

> effectively a subprocess over standard in and standard out is extremely useful
> — 03:51 [^bmWZk9vTze0]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^bmWZk9vTze0]: [MCP is all you need — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=bmWZk9vTze0); publication: 2025-07-18T18:52:25Z; analysis: `analysis/bmWZk9vTze0.json`.
