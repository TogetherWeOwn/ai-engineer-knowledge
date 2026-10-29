---
{
  "type": "technique",
  "id": "scope-reminders",
  "title": "Refresh concise goals and constraints at meaningful boundaries",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-04-30T12:00:06Z",
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
      "id": "am_oeAoUhew",
      "resource": "https://www.youtube.com/watch?v=am_oeAoUhew",
      "title": "Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI",
      "author": "Ryan Lopopolo, OpenAI",
      "last_modified": "2026-04-17T00:29:28Z",
      "analysis_file": "analysis/am_oeAoUhew.json"
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

# Refresh concise goals and constraints at meaningful boundaries

## What

Refresh concise goals and constraints at meaningful boundaries

Restating canonical task ID, repo, worktree and forbidden actions after resume/compaction can reduce instruction drift without repeatedly injecting an entire policy bundle.

## Evidence

Source analysis [^WE_Gnowy3uw]; no independently matched timestamped quote published.

Source analysis [^am_oeAoUhew]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^WE_Gnowy3uw]: [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](https://www.youtube.com/watch?v=WE_Gnowy3uw); publication: 2026-04-30T12:00:06Z; analysis: `analysis/WE_Gnowy3uw.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
