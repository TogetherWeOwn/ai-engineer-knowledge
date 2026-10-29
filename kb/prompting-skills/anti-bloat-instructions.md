---
{
  "type": "technique",
  "id": "anti-bloat-instructions",
  "title": "Consolidate verified lessons instead of appending every failure to one ever-growing rules file",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-10-04T15:00:15Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "OrtBEBLMXdM",
      "resource": "https://www.youtube.com/watch?v=OrtBEBLMXdM",
      "title": "Iterating on LLM apps at scale  Learnings from Discord: Ian Webster",
      "author": null,
      "last_modified": "2024-11-22T20:27:24Z",
      "analysis_file": "analysis/OrtBEBLMXdM.json"
    },
    {
      "id": "pyvRID_CZZU",
      "resource": "https://www.youtube.com/watch?v=pyvRID_CZZU",
      "title": "We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI",
      "author": "AssemblyAI",
      "last_modified": "2026-10-04T15:00:15Z",
      "analysis_file": "analysis/pyvRID_CZZU.json"
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

# Consolidate verified lessons instead of appending every failure to one ever-growing rules file

## What

Consolidate verified lessons instead of appending every failure to one ever-growing rules file

Adding a special instruction for every failure can reach diminishing and negative returns; move enforceable cases into tests/code and simplify the prompt.

## Evidence

Source analysis [^OrtBEBLMXdM]; no independently matched timestamped quote published.

Source analysis [^pyvRID_CZZU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^OrtBEBLMXdM]: [Iterating on LLM apps at scale  Learnings from Discord: Ian Webster](https://www.youtube.com/watch?v=OrtBEBLMXdM); publication: 2024-11-22T20:27:24Z; analysis: `analysis/OrtBEBLMXdM.json`.
[^pyvRID_CZZU]: [We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](https://www.youtube.com/watch?v=pyvRID_CZZU); publication: 2026-10-04T15:00:15Z; analysis: `analysis/pyvRID_CZZU.json`.
