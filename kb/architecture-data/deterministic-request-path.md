---
{
  "type": "technique",
  "id": "deterministic-request-path",
  "title": "Keep LLM reasoning out of latency-critical paths when deterministic execution suffices",
  "area": "architecture-data",
  "status": "stable",
  "valid_from": "2025-03-19T17:09:54Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-rsTkYgnNzM",
      "resource": "https://www.youtube.com/watch?v=-rsTkYgnNzM",
      "title": "Rethinking how we Scaffold AI Agents - Rahul Sengottuvelu, Ramp",
      "author": "Rahul Sengottuvelu, Ramp",
      "last_modified": "2025-03-19T17:09:54Z",
      "analysis_file": "analysis/-rsTkYgnNzM.json"
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

# Keep LLM reasoning out of latency-critical paths when deterministic execution suffices

## What

Keep LLM reasoning out of latency-critical paths when deterministic execution suffices

Their demo makes the LLM simulate a Gmail UI per click; it is very slow and barely works.

## Evidence

Source analysis [^-rsTkYgnNzM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Lower future change and maintenance cost
- **Speed:** Faster localized reasoning and edits
- **Quality:** Explicit domain/query semantics
- **Reliability:** Narrow testable boundaries and preserved invariants
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-rsTkYgnNzM]: [Rethinking how we Scaffold AI Agents - Rahul Sengottuvelu, Ramp](https://www.youtube.com/watch?v=-rsTkYgnNzM); publication: 2025-03-19T17:09:54Z; analysis: `analysis/-rsTkYgnNzM.json`.
