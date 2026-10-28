---
{
  "type": "technique",
  "id": "prompt-cost-ceiling",
  "title": "Move repeatable prompt instructions into executable interfaces when prose stops improving outcomes",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2025-07-19T19:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "C13jiFWNuo8",
      "resource": "https://www.youtube.com/watch?v=C13jiFWNuo8",
      "title": "Google Photos Magic Editor: GenAI Under the Hood of a Billion-User App - Kelvin Ma, Google Photos",
      "author": "Kelvin Ma, Google Photos",
      "last_modified": "2025-07-19T19:00:06Z",
      "analysis_file": "analysis/C13jiFWNuo8.json"
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

# Move repeatable prompt instructions into executable interfaces when prose stops improving outcomes

## What

Move repeatable prompt instructions into executable interfaces when prose stops improving outcomes

They extract user intent and guide users through constrained UX rather than making users write detailed prompts for every edit.

## Evidence

Source analysis [^C13jiFWNuo8]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^C13jiFWNuo8]: [Google Photos Magic Editor: GenAI Under the Hood of a Billion-User App - Kelvin Ma, Google Photos](https://www.youtube.com/watch?v=C13jiFWNuo8); publication: 2025-07-19T19:00:06Z; analysis: `analysis/C13jiFWNuo8.json`.
