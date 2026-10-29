---
{
  "type": "technique",
  "id": "prompt-placement",
  "title": "Place task-local instructions at deliberate boundaries around long source documents",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2024-08-17T15:24:49Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "hkhDdcM5V94",
      "resource": "https://www.youtube.com/watch?v=hkhDdcM5V94",
      "title": "Building with Anthropic Claude: Prompt Workshop with Zack Witten",
      "author": null,
      "last_modified": "2024-08-17T15:24:49Z",
      "analysis_file": "analysis/hkhDdcM5V94.json"
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

# Place task-local instructions at deliberate boundaries around long source documents

## What

Place task-local instructions at deliberate boundaries around long source documents

Recency can improve following task-local instructions; the speaker explicitly qualifies this as model/context dependent.

## Evidence

> instructions okay we've sort of found that instructions are more tightly
> — 17:39 [^hkhDdcM5V94]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^hkhDdcM5V94]: [Building with Anthropic Claude: Prompt Workshop with Zack Witten](https://www.youtube.com/watch?v=hkhDdcM5V94); publication: 2024-08-17T15:24:49Z; analysis: `analysis/hkhDdcM5V94.json`.
