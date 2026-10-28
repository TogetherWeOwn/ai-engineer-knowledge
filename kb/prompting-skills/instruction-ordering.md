---
{
  "type": "technique",
  "id": "instruction-ordering",
  "title": "Use stable high-information instruction ordering and verify its actual effect",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-06-29T18:53:10Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "UNzCG3lw6O0",
      "resource": "https://www.youtube.com/watch?v=UNzCG3lw6O0",
      "title": "Building Great Agent Skills: The Missing Manual",
      "author": null,
      "last_modified": "2026-06-29T18:53:10Z",
      "analysis_file": "analysis/UNzCG3lw6O0.json"
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

# Use stable high-information instruction ordering and verify its actual effect

## What

Use stable high-information instruction ordering and verify its actual effect

A consistent phrase such as vertical slice activates a known workflow more compactly than many inconsistent paraphrases.

## Evidence

> What we're doing is we're packing lots of meaning into a relatively short
> — 13:56 [^UNzCG3lw6O0]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^UNzCG3lw6O0]: [Building Great Agent Skills: The Missing Manual](https://www.youtube.com/watch?v=UNzCG3lw6O0); publication: 2026-06-29T18:53:10Z; analysis: `analysis/UNzCG3lw6O0.json`.
