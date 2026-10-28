---
{
  "type": "technique",
  "id": "reusable-context-operations",
  "title": "Turn repeated context assembly and cleanup chores into deterministic reusable operations",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2025-04-10T19:47:37Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "kPL-6-9MVyA",
      "resource": "https://www.youtube.com/watch?v=kPL-6-9MVyA",
      "title": "RAG Agents in Prod: 10 Lessons We Learned — Douwe Kiela, creator of RAG",
      "author": "Douwe Kiela, creator of RAG",
      "last_modified": "2025-04-10T19:47:37Z",
      "analysis_file": "analysis/kPL-6-9MVyA.json"
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

# Turn repeated context assembly and cleanup chores into deterministic reusable operations

## What

Turn repeated context assembly and cleanup chores into deterministic reusable operations

They abstract repetitive RAG chores like chunking and prompting so engineers focus on business value.

## Evidence

Source analysis [^kPL-6-9MVyA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^kPL-6-9MVyA]: [RAG Agents in Prod: 10 Lessons We Learned — Douwe Kiela, creator of RAG](https://www.youtube.com/watch?v=kPL-6-9MVyA); publication: 2025-04-10T19:47:37Z; analysis: `analysis/kPL-6-9MVyA.json`.
