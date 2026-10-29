---
{
  "type": "technique",
  "id": "safe-edit-strategies",
  "title": "Select exact patches, structural transforms or full rewrites according to bounded file semantics",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2025-02-06T09:24:01Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "R3hTescenDw",
      "resource": "https://www.youtube.com/watch?v=R3hTescenDw",
      "title": "Which Jobs Can Be Replaced Today:  Fryderyk Wiatrowski and Peter Albert",
      "author": null,
      "last_modified": "2025-02-06T09:24:01Z",
      "analysis_file": "analysis/R3hTescenDw.json"
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

# Select exact patches, structural transforms or full rewrites according to bounded file semantics

## What

Select exact patches, structural transforms or full rewrites according to bounded file semantics

They design tool calls as key-value updates (mimicking Python dict updates) or full rewrites rather than small diffs, because models are weak at generating small diffs and this splits the reasoning into two simpler steps.

## Evidence

> diffs um also you should try to avoid any recursive n structures if you can um
> — 15:53 [^R3hTescenDw]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^R3hTescenDw]: [Which Jobs Can Be Replaced Today:  Fryderyk Wiatrowski and Peter Albert](https://www.youtube.com/watch?v=R3hTescenDw); publication: 2025-02-06T09:24:01Z; analysis: `analysis/R3hTescenDw.json`.
