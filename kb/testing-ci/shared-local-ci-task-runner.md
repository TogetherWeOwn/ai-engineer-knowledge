---
{
  "type": "technique",
  "id": "shared-local-ci-task-runner",
  "title": "Run the same authoritative checks locally and in CI with rationale-linked failures",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-07-29T22:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "504PvfXou5Y",
      "resource": "https://www.youtube.com/watch?v=504PvfXou5Y",
      "title": "BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence",
      "author": "Michal Cichra, Safe Intelligence",
      "last_modified": "2026-06-03T13:00:08Z",
      "analysis_file": "analysis/504PvfXou5Y.json"
    },
    {
      "id": "UXOLprPvr-0",
      "resource": "https://www.youtube.com/watch?v=UXOLprPvr-0",
      "title": "Building AI Agents with Real ROI in the Enterprise SDLC: Bruno (Booking.com) & Beyang (Sourcegraph)",
      "author": null,
      "last_modified": "2025-04-08T17:00:06Z",
      "analysis_file": "analysis/UXOLprPvr-0.json"
    },
    {
      "id": "iKQ78wyJEXU",
      "resource": "https://www.youtube.com/watch?v=iKQ78wyJEXU",
      "title": "We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank",
      "author": "Lucas Palma, Nubank",
      "last_modified": "2026-07-29T22:00:06Z",
      "analysis_file": "analysis/iKQ78wyJEXU.json"
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

# Run the same authoritative checks locally and in CI with rationale-linked failures

## What

Run the same authoritative checks locally and in CI with rationale-linked failures

A shared constraint implementation catches violations before PR review and avoids a separate contradictory rule set in the editor or agent prompt.

## Evidence

Source analysis [^504PvfXou5Y]; no independently matched timestamped quote published.

Source analysis [^UXOLprPvr-0]; no independently matched timestamped quote published.

Source analysis [^iKQ78wyJEXU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^504PvfXou5Y]: [BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence](https://www.youtube.com/watch?v=504PvfXou5Y); publication: 2026-06-03T13:00:08Z; analysis: `analysis/504PvfXou5Y.json`.
[^UXOLprPvr-0]: [Building AI Agents with Real ROI in the Enterprise SDLC: Bruno (Booking.com) & Beyang (Sourcegraph)](https://www.youtube.com/watch?v=UXOLprPvr-0); publication: 2025-04-08T17:00:06Z; analysis: `analysis/UXOLprPvr-0.json`.
[^iKQ78wyJEXU]: [We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](https://www.youtube.com/watch?v=iKQ78wyJEXU); publication: 2026-07-29T22:00:06Z; analysis: `analysis/iKQ78wyJEXU.json`.
