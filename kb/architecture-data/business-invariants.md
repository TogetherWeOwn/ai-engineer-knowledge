---
{
  "type": "technique",
  "id": "business-invariants",
  "title": "Separate product invariants from architecture choices and encode objective rules in code",
  "area": "architecture-data",
  "status": "stable",
  "valid_from": "2026-09-27T17:30:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "hkhDdcM5V94",
      "resource": "https://www.youtube.com/watch?v=hkhDdcM5V94",
      "title": "Building with Anthropic Claude: Prompt Workshop with Zack Witten",
      "author": null,
      "last_modified": "2024-08-17T15:24:49Z",
      "analysis_file": "analysis/hkhDdcM5V94.json"
    },
    {
      "id": "tUPPVhBBcoM",
      "resource": "https://www.youtube.com/watch?v=tUPPVhBBcoM",
      "title": "Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp",
      "author": "Zach Lloyd, Warp",
      "last_modified": "2026-09-27T17:30:36Z",
      "analysis_file": "analysis/tUPPVhBBcoM.json"
    },
    {
      "id": "yj-wSRJwrrc",
      "resource": "https://www.youtube.com/watch?v=yj-wSRJwrrc",
      "title": "Pydantic is all you need: Jason Liu",
      "author": null,
      "last_modified": "2023-11-01T16:27:08Z",
      "analysis_file": "analysis/yj-wSRJwrrc.json"
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

# Separate product invariants from architecture choices and encode objective rules in code

## What

Separate product invariants from architecture choices and encode objective rules in code

Product specification defines observable invariants; technical specification defines interfaces, architecture and code shape.

## Evidence

> ideally I think for the ideal prompt you would find a native speaker of the
> — 20:03 [^hkhDdcM5V94]

> describes the product invariance that you're building towards. Techsp spec
> — 10:45 [^tUPPVhBBcoM]

Source analysis [^yj-wSRJwrrc]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Lower future change and maintenance cost
- **Speed:** Faster localized reasoning and edits
- **Quality:** Explicit domain/query semantics
- **Reliability:** Narrow testable boundaries and preserved invariants
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^hkhDdcM5V94]: [Building with Anthropic Claude: Prompt Workshop with Zack Witten](https://www.youtube.com/watch?v=hkhDdcM5V94); publication: 2024-08-17T15:24:49Z; analysis: `analysis/hkhDdcM5V94.json`.
[^tUPPVhBBcoM]: [Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp](https://www.youtube.com/watch?v=tUPPVhBBcoM); publication: 2026-09-27T17:30:36Z; analysis: `analysis/tUPPVhBBcoM.json`.
[^yj-wSRJwrrc]: [Pydantic is all you need: Jason Liu](https://www.youtube.com/watch?v=yj-wSRJwrrc); publication: 2023-11-01T16:27:08Z; analysis: `analysis/yj-wSRJwrrc.json`.
