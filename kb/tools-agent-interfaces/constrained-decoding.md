---
{
  "type": "technique",
  "id": "constrained-decoding",
  "title": "Use grammar or constrained decoding for syntax only when the selected endpoint supports it",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2024-10-14T18:51:58Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "aNmfvN6S_n4",
      "resource": "https://www.youtube.com/watch?v=aNmfvN6S_n4",
      "title": "No more bad outputs with structured generation: Remi Louf",
      "author": null,
      "last_modified": "2024-10-14T18:51:58Z",
      "analysis_file": "analysis/aNmfvN6S_n4.json"
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

# Use grammar or constrained decoding for syntax only when the selected endpoint supports it

## What

Use grammar or constrained decoding for syntax only when the selected endpoint supports it

Mask tokens that violate the output grammar before sampling, rather than repairing malformed text afterward.

## Evidence

Source analysis [^aNmfvN6S_n4]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^aNmfvN6S_n4]: [No more bad outputs with structured generation: Remi Louf](https://www.youtube.com/watch?v=aNmfvN6S_n4); publication: 2024-10-14T18:51:58Z; analysis: `analysis/aNmfvN6S_n4.json`.
