---
{
  "type": "technique",
  "id": "multi-repo-manifest",
  "title": "Track coordinated multi-repository changes in one revision-linked manifest",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-06-26T01:15:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "WE_Gnowy3uw",
      "resource": "https://www.youtube.com/watch?v=WE_Gnowy3uw",
      "title": "Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor",
      "author": "David Gomes, Cursor",
      "last_modified": "2026-04-30T12:00:06Z",
      "analysis_file": "analysis/WE_Gnowy3uw.json"
    },
    {
      "id": "jVjt-2g8NMY",
      "resource": "https://www.youtube.com/watch?v=jVjt-2g8NMY",
      "title": "A Genius With Amnesia - Victor Savkin, Nx",
      "author": "Victor Savkin, Nx",
      "last_modified": "2026-06-26T01:15:06Z",
      "analysis_file": "analysis/jVjt-2g8NMY.json"
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

# Track coordinated multi-repository changes in one revision-linked manifest

## What

Track coordinated multi-repository changes in one revision-linked manifest

Retain a shared intent and explicit repository/PR membership for one conceptual change, avoiding repeated lossy explanations.

## Evidence

Source analysis [^WE_Gnowy3uw]; no independently matched timestamped quote published.

> I explained the change once and I got it implemented in both repos and it's all
> — 12:46 [^jVjt-2g8NMY]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^WE_Gnowy3uw]: [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](https://www.youtube.com/watch?v=WE_Gnowy3uw); publication: 2026-04-30T12:00:06Z; analysis: `analysis/WE_Gnowy3uw.json`.
[^jVjt-2g8NMY]: [A Genius With Amnesia - Victor Savkin, Nx](https://www.youtube.com/watch?v=jVjt-2g8NMY); publication: 2026-06-26T01:15:06Z; analysis: `analysis/jVjt-2g8NMY.json`.
