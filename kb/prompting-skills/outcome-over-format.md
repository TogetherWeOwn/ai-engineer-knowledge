---
{
  "type": "technique",
  "id": "outcome-over-format",
  "title": "Specify qualitative intent before imposing cosmetic numerical output constraints",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-08-09T16:30:28Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Kz4QJmNrVXU",
      "resource": "https://www.youtube.com/watch?v=Kz4QJmNrVXU",
      "title": "Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.",
      "author": "Matt Dailey, Ref.",
      "last_modified": "2026-08-09T16:30:28Z",
      "analysis_file": "analysis/Kz4QJmNrVXU.json"
    },
    {
      "id": "ij-AU9dpJjc",
      "resource": "https://www.youtube.com/watch?v=ij-AU9dpJjc",
      "title": "Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co",
      "author": "Isadora Martin-Dye, Isadora & Co",
      "last_modified": "2026-06-26T20:00:35Z",
      "analysis_file": "analysis/ij-AU9dpJjc.json"
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

# Specify qualitative intent before imposing cosmetic numerical output constraints

## What

Specify qualitative intent before imposing cosmetic numerical output constraints

The speaker places human situation before numeric guard blocks so prose is framed around intent, not mechanically around numbers.

## Evidence

> in terms of planning and polish. So, recognizing that there are two gears
> — 18:50 [^Kz4QJmNrVXU]

> before the numbers. Tone is set by human context first, then numeric constraints.
> — 10:25 [^ij-AU9dpJjc]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Kz4QJmNrVXU]: [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](https://www.youtube.com/watch?v=Kz4QJmNrVXU); publication: 2026-08-09T16:30:28Z; analysis: `analysis/Kz4QJmNrVXU.json`.
[^ij-AU9dpJjc]: [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](https://www.youtube.com/watch?v=ij-AU9dpJjc); publication: 2026-06-26T20:00:35Z; analysis: `analysis/ij-AU9dpJjc.json`.
