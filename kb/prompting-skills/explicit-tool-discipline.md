---
{
  "type": "technique",
  "id": "explicit-tool-discipline",
  "title": "Declare required tool-use behavior and verify it in runtime evidence",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-06-11T18:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "TNwJ1LMiENk",
      "resource": "https://www.youtube.com/watch?v=TNwJ1LMiENk",
      "title": "Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel",
      "author": "Kobie Crawford, Snorkel",
      "last_modified": "2026-06-10T17:00:25Z",
      "analysis_file": "analysis/TNwJ1LMiENk.json"
    },
    {
      "id": "iUWwcG-C8OU",
      "resource": "https://www.youtube.com/watch?v=iUWwcG-C8OU",
      "title": "Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS",
      "author": "Garrett Galow, WorkOS",
      "last_modified": "2026-06-11T18:00:06Z",
      "analysis_file": "analysis/iUWwcG-C8OU.json"
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

# Declare required tool-use behavior and verify it in runtime evidence

## What

Declare required tool-use behavior and verify it in runtime evidence

Conventional package managers, languages and workflows match the examples agents know and reduce environment-discovery errors.

## Evidence

Source analysis [^TNwJ1LMiENk]; no independently matched timestamped quote published.

Source analysis [^iUWwcG-C8OU]; no independently matched timestamped quote published.

> things. You want to use the industry standard tools in the same way the
> — 02:59 [^rT2Del5pwg4]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^TNwJ1LMiENk]: [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](https://www.youtube.com/watch?v=TNwJ1LMiENk); publication: 2026-06-10T17:00:25Z; analysis: `analysis/TNwJ1LMiENk.json`.
[^iUWwcG-C8OU]: [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](https://www.youtube.com/watch?v=iUWwcG-C8OU); publication: 2026-06-11T18:00:06Z; analysis: `analysis/iUWwcG-C8OU.json`.
[^rT2Del5pwg4]: [Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One](https://www.youtube.com/watch?v=rT2Del5pwg4); publication: 2025-12-23T17:30:28Z; analysis: `analysis/rT2Del5pwg4.json`.
