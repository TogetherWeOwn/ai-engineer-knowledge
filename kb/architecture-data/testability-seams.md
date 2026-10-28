---
{
  "type": "technique",
  "id": "testability-seams",
  "title": "Refactor narrow seams and isolate effects to improve testability without broad rewrites",
  "area": "architecture-data",
  "status": "stable",
  "valid_from": "2026-09-11T20:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "3E7VAZaTG9M",
      "resource": "https://www.youtube.com/watch?v=3E7VAZaTG9M",
      "title": "Scaling AI in Education: A Khanmigo case study: Shawn Jansepar",
      "author": null,
      "last_modified": "2025-02-05T02:56:08Z",
      "analysis_file": "analysis/3E7VAZaTG9M.json"
    },
    {
      "id": "H7vFrcNWXzs",
      "resource": "https://www.youtube.com/watch?v=H7vFrcNWXzs",
      "title": "Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition",
      "author": "Jonathan Kelley, Dioxus Labs & Cognition",
      "last_modified": "2026-09-11T20:00:06Z",
      "analysis_file": "analysis/H7vFrcNWXzs.json"
    },
    {
      "id": "UNzCG3lw6O0",
      "resource": "https://www.youtube.com/watch?v=UNzCG3lw6O0",
      "title": "Building Great Agent Skills: The Missing Manual",
      "author": null,
      "last_modified": "2026-06-29T18:53:10Z",
      "analysis_file": "analysis/UNzCG3lw6O0.json"
    },
    {
      "id": "rT2Del5pwg4",
      "resource": "https://www.youtube.com/watch?v=rT2Del5pwg4",
      "title": "Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One",
      "author": "Max Kanat-Alexander, Capital One",
      "last_modified": "2025-12-23T17:30:28Z",
      "analysis_file": "analysis/rT2Del5pwg4.json"
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

# Refactor narrow seams and isolate effects to improve testability without broad rewrites

## What

Refactor narrow seams and isolate effects to improve testability without broad rewrites

Code that exposes observable outcomes and isolated units supports meaningful tests; an untestable codebase induces vacuous button-click assertions.

## Evidence

Source analysis [^3E7VAZaTG9M]; no independently matched timestamped quote published.

Source analysis [^H7vFrcNWXzs]; no independently matched timestamped quote published.

Source analysis [^UNzCG3lw6O0]; no independently matched timestamped quote published.

> structure of your systems and structure of your code bases. Agents work better
> — 06:47 [^rT2Del5pwg4]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Lower future change and maintenance cost
- **Speed:** Faster localized reasoning and edits
- **Quality:** Explicit domain/query semantics
- **Reliability:** Narrow testable boundaries and preserved invariants
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^3E7VAZaTG9M]: [Scaling AI in Education: A Khanmigo case study: Shawn Jansepar](https://www.youtube.com/watch?v=3E7VAZaTG9M); publication: 2025-02-05T02:56:08Z; analysis: `analysis/3E7VAZaTG9M.json`.
[^H7vFrcNWXzs]: [Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition](https://www.youtube.com/watch?v=H7vFrcNWXzs); publication: 2026-09-11T20:00:06Z; analysis: `analysis/H7vFrcNWXzs.json`.
[^UNzCG3lw6O0]: [Building Great Agent Skills: The Missing Manual](https://www.youtube.com/watch?v=UNzCG3lw6O0); publication: 2026-06-29T18:53:10Z; analysis: `analysis/UNzCG3lw6O0.json`.
[^rT2Del5pwg4]: [Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One](https://www.youtube.com/watch?v=rT2Del5pwg4); publication: 2025-12-23T17:30:28Z; analysis: `analysis/rT2Del5pwg4.json`.
