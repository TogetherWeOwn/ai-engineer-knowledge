---
{
  "type": "technique",
  "id": "review-proof-obligations",
  "title": "Select explicit proof obligations by the change's risk before implementation",
  "area": "review-quality",
  "status": "stable",
  "valid_from": "2026-08-18T14:30:38Z",
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
      "id": "WLXxTaPagA8",
      "resource": "https://www.youtube.com/watch?v=WLXxTaPagA8",
      "title": "Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony",
      "author": "Sumaiya Shrabony",
      "last_modified": "2026-07-11T16:30:04Z",
      "analysis_file": "analysis/WLXxTaPagA8.json"
    },
    {
      "id": "ZpK5PWX2YRM",
      "resource": "https://www.youtube.com/watch?v=ZpK5PWX2YRM",
      "title": "Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI",
      "author": "Alex Volkov, ThursdAI",
      "last_modified": "2026-07-10T18:00:06Z",
      "analysis_file": "analysis/ZpK5PWX2YRM.json"
    },
    {
      "id": "pPj_tjlvYjA",
      "resource": "https://www.youtube.com/watch?v=pPj_tjlvYjA",
      "title": "Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful",
      "author": "Ekaterina Deyneka, Reelful",
      "last_modified": "2026-08-18T14:30:38Z",
      "analysis_file": "analysis/pPj_tjlvYjA.json"
    },
    {
      "id": "qLqttdO33UM",
      "resource": "https://www.youtube.com/watch?v=qLqttdO33UM",
      "title": "Vision: Zero Bugs — Johann Schleier-Smith, Temporal",
      "author": "Johann Schleier-Smith, Temporal",
      "last_modified": "2025-11-24T20:16:38Z",
      "analysis_file": "analysis/qLqttdO33UM.json"
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

# Select explicit proof obligations by the change's risk before implementation

## What

Select explicit proof obligations by the change's risk before implementation

Cosmetic, ordinary and irreversible changes need different verification evidence; uniform expensive review wastes capacity while missing specific high-risk obligations.

## Evidence

> into the process. So, we're aligning on the key decisions up front.
> — 16:09 [^Kz4QJmNrVXU]

Source analysis [^WLXxTaPagA8]; no independently matched timestamped quote published.

> Different task just need different proof.
> — 12:34 [^ZpK5PWX2YRM]

Source analysis [^pPj_tjlvYjA]; no independently matched timestamped quote published.

Source analysis [^qLqttdO33UM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer redundant or low-value review rounds
- **Speed:** Shorter evidence-backed review/repair cycles
- **Quality:** Better focus on actionable defects rather than cosmetic scores
- **Reliability:** Independent, revision-bound verification
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Kz4QJmNrVXU]: [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](https://www.youtube.com/watch?v=Kz4QJmNrVXU); publication: 2026-08-09T16:30:28Z; analysis: `analysis/Kz4QJmNrVXU.json`.
[^WLXxTaPagA8]: [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](https://www.youtube.com/watch?v=WLXxTaPagA8); publication: 2026-07-11T16:30:04Z; analysis: `analysis/WLXxTaPagA8.json`.
[^ZpK5PWX2YRM]: [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](https://www.youtube.com/watch?v=ZpK5PWX2YRM); publication: 2026-07-10T18:00:06Z; analysis: `analysis/ZpK5PWX2YRM.json`.
[^pPj_tjlvYjA]: [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](https://www.youtube.com/watch?v=pPj_tjlvYjA); publication: 2026-08-18T14:30:38Z; analysis: `analysis/pPj_tjlvYjA.json`.
[^qLqttdO33UM]: [Vision: Zero Bugs — Johann Schleier-Smith, Temporal](https://www.youtube.com/watch?v=qLqttdO33UM); publication: 2025-11-24T20:16:38Z; analysis: `analysis/qLqttdO33UM.json`.
