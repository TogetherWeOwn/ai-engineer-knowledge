---
{
  "type": "technique",
  "id": "syntax-bounded-edits",
  "title": "Expand edit matches to full syntax boundaries and verify indentation changes",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2025-06-27T09:22:37Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "WXy8Yy9xGss",
      "resource": "https://www.youtube.com/watch?v=WXy8Yy9xGss",
      "title": "CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed",
      "author": "Nathan Sobo, Zed",
      "last_modified": "2025-06-27T09:22:37Z",
      "analysis_file": "analysis/WXy8Yy9xGss.json"
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

# Expand edit matches to full syntax boundaries and verify indentation changes

## What

Expand edit matches to full syntax boundaries and verify indentation changes

A single matching line may omit the signature or surrounding construct needed for a correct edit. AST-aware expansion returns the smallest useful complete code unit.

## Evidence

> actually expand out the match to the syntactic boundaries. Um and so that was
> — 04:43 [^WXy8Yy9xGss]

> delta. So we figure out basically we sort of renormalize the indent if
> — 10:28 [^WXy8Yy9xGss]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^WXy8Yy9xGss]: [CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed](https://www.youtube.com/watch?v=WXy8Yy9xGss); publication: 2025-06-27T09:22:37Z; analysis: `analysis/WXy8Yy9xGss.json`.
