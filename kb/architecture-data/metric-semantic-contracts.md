---
{
  "type": "technique",
  "id": "metric-semantic-contracts",
  "title": "Define row grain, units and business metric semantics as versioned contracts",
  "area": "architecture-data",
  "status": "stable",
  "valid_from": "2026-10-11T12:30:23Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KhRjivBSwiw",
      "resource": "https://www.youtube.com/watch?v=KhRjivBSwiw",
      "title": "The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef",
      "author": "Yoni Michael & Brandon Callender, Typedef",
      "last_modified": "2026-10-11T12:30:23Z",
      "analysis_file": "analysis/KhRjivBSwiw.json"
    },
    {
      "id": "tJFjeMBKbIY",
      "resource": "https://www.youtube.com/watch?v=tJFjeMBKbIY",
      "title": "Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings",
      "author": "Shawn Chan, China Resources Holdings",
      "last_modified": "2026-07-30T02:00:06Z",
      "analysis_file": "analysis/tJFjeMBKbIY.json"
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

# Define row grain, units and business metric semantics as versioned contracts

## What

Define row grain, units and business metric semantics as versioned contracts

Valid SQL can silently change row meaning and multiply downstream metrics; explicit grain contracts expose semantic changes.

## Evidence

> mean? What does each row actually represent? Um and so if the grain is
> — 06:14 [^KhRjivBSwiw]

Source analysis [^tJFjeMBKbIY]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Lower future change and maintenance cost
- **Speed:** Faster localized reasoning and edits
- **Quality:** Explicit domain/query semantics
- **Reliability:** Narrow testable boundaries and preserved invariants
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KhRjivBSwiw]: [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](https://www.youtube.com/watch?v=KhRjivBSwiw); publication: 2026-10-11T12:30:23Z; analysis: `analysis/KhRjivBSwiw.json`.
[^tJFjeMBKbIY]: [Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings](https://www.youtube.com/watch?v=tJFjeMBKbIY); publication: 2026-07-30T02:00:06Z; analysis: `analysis/tJFjeMBKbIY.json`.
