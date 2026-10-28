---
{
  "type": "technique",
  "id": "unsafe-generated-code",
  "title": "Reject unrestricted eval and execute generated programs only inside a constrained sandbox",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2025-04-23T16:00:26Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KUEmEb71vzQ",
      "resource": "https://www.youtube.com/watch?v=KUEmEb71vzQ",
      "title": "Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI",
      "author": "Full Workshop, with Ilan Bigio of OpenAI",
      "last_modified": "2025-04-23T16:00:26Z",
      "analysis_file": "analysis/KUEmEb71vzQ.json"
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

# Reject unrestricted eval and execute generated programs only inside a constrained sandbox

## What

Reject unrestricted eval and execute generated programs only inside a constrained sandbox

Agent generates Python source for a new tool, evals it, and appends it to its own tool list; speaker repeatedly flags it as dangerous.

## Evidence

Source analysis [^KUEmEb71vzQ]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KUEmEb71vzQ]: [Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI](https://www.youtube.com/watch?v=KUEmEb71vzQ); publication: 2025-04-23T16:00:26Z; analysis: `analysis/KUEmEb71vzQ.json`.
