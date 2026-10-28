---
{
  "type": "technique",
  "id": "artifact-corrections",
  "title": "Continue from an explicitly corrected artifact while preserving the original trace and provenance",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2024-08-21T16:36:00Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "zwItokY087U",
      "resource": "https://www.youtube.com/watch?v=zwItokY087U",
      "title": "10x Development: LLMs For the working Programmer - Manuel Odendahl",
      "author": "Manuel Odendahl",
      "last_modified": "2024-08-21T16:36:00Z",
      "analysis_file": "analysis/zwItokY087U.json"
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

# Continue from an explicitly corrected artifact while preserving the original trace and provenance

## What

Continue from an explicitly corrected artifact while preserving the original trace and provenance

When output is wrong, he edits the assistant message to the correct code and continues, so the model believes it produced the right thing; also uses 'time travel' (summarize the fixed result, rewind, paste as a message from the future) to avoid 25 correction turns poisoning context.

## Evidence

Source analysis [^zwItokY087U]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^zwItokY087U]: [10x Development: LLMs For the working Programmer - Manuel Odendahl](https://www.youtube.com/watch?v=zwItokY087U); publication: 2024-08-21T16:36:00Z; analysis: `analysis/zwItokY087U.json`.
