---
{
  "type": "technique",
  "id": "planning-depth-routing",
  "title": "Vary planning depth by task coupling, uncertainty and risk",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-07-23T02:00:03Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "W76woOYHlvY",
      "resource": "https://www.youtube.com/watch?v=W76woOYHlvY",
      "title": "Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban",
      "author": "Louis Knight-Webb, Vibe Kanban",
      "last_modified": "2026-05-02T21:00:06Z",
      "analysis_file": "analysis/W76woOYHlvY.json"
    },
    {
      "id": "mOf-PP4mVjA",
      "resource": "https://www.youtube.com/watch?v=mOf-PP4mVjA",
      "title": "Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs",
      "author": "James Le, TwelveLabs",
      "last_modified": "2026-07-23T02:00:03Z",
      "analysis_file": "analysis/mOf-PP4mVjA.json"
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

# Vary planning depth by task coupling, uncertainty and risk

## What

Vary planning depth by task coupling, uncertainty and risk

Backend features, migrations and refactors are often specifiable up front; UI feature work benefits from shorter design-feedback cycles because behavior, state and visual choices are harder to fully specify.

## Evidence

Source analysis [^W76woOYHlvY]; no independently matched timestamped quote published.

Source analysis [^mOf-PP4mVjA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^W76woOYHlvY]: [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](https://www.youtube.com/watch?v=W76woOYHlvY); publication: 2026-05-02T21:00:06Z; analysis: `analysis/W76woOYHlvY.json`.
[^mOf-PP4mVjA]: [Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](https://www.youtube.com/watch?v=mOf-PP4mVjA); publication: 2026-07-23T02:00:03Z; analysis: `analysis/mOf-PP4mVjA.json`.
