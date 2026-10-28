---
{
  "type": "technique",
  "id": "safe-autonomy-horizon",
  "title": "Calibrate safe unattended duration from reliable outcomes, not a 50-percent benchmark horizon",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-08-01T00:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2aS7aKoXn64",
      "resource": "https://www.youtube.com/watch?v=2aS7aKoXn64",
      "title": "Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software",
      "author": "Rayan Garg, Theta Software",
      "last_modified": "2026-08-01T00:00:06Z",
      "analysis_file": "analysis/2aS7aKoXn64.json"
    },
    {
      "id": "RhfqQKe22ZA",
      "resource": "https://www.youtube.com/watch?v=RhfqQKe22ZA",
      "title": "Why Agent Hype can fall short of reality – Joel Becker, METR",
      "author": "Joel Becker, METR",
      "last_modified": "2025-12-24T16:30:06Z",
      "analysis_file": "analysis/RhfqQKe22ZA.json"
    },
    {
      "id": "VrpEyglYgeU",
      "resource": "https://www.youtube.com/watch?v=VrpEyglYgeU",
      "title": "In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar",
      "author": "Tariq Shaukat, Sonar",
      "last_modified": "2026-07-20T15:00:06Z",
      "analysis_file": "analysis/VrpEyglYgeU.json"
    },
    {
      "id": "wpOA-UXynoM",
      "resource": "https://www.youtube.com/watch?v=wpOA-UXynoM",
      "title": "How Forward Deployed Engineering is done at Factory — Eno Reyes",
      "author": "Eno Reyes",
      "last_modified": "2026-07-28T22:00:06Z",
      "analysis_file": "analysis/wpOA-UXynoM.json"
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

# Calibrate safe unattended duration from reliable outcomes, not a 50-percent benchmark horizon

## What

Calibrate safe unattended duration from reliable outcomes, not a 50-percent benchmark horizon

The horizon axis is human task time at 50% modeled success, not agent wall-clock or a production reliability guarantee.

## Evidence

Source analysis [^2aS7aKoXn64]; no independently matched timestamped quote published.

> 50% of the time the time horizon of those models that there's much to debate
> — 05:55 [^RhfqQKe22ZA]

Source analysis [^VrpEyglYgeU]; no independently matched timestamped quote published.

> solve this task and here is what solving this task means. I will now basically
> — 14:21 [^wpOA-UXynoM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2aS7aKoXn64]: [Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software](https://www.youtube.com/watch?v=2aS7aKoXn64); publication: 2026-08-01T00:00:06Z; analysis: `analysis/2aS7aKoXn64.json`.
[^RhfqQKe22ZA]: [Why Agent Hype can fall short of reality – Joel Becker, METR](https://www.youtube.com/watch?v=RhfqQKe22ZA); publication: 2025-12-24T16:30:06Z; analysis: `analysis/RhfqQKe22ZA.json`.
[^VrpEyglYgeU]: [In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](https://www.youtube.com/watch?v=VrpEyglYgeU); publication: 2026-07-20T15:00:06Z; analysis: `analysis/VrpEyglYgeU.json`.
[^wpOA-UXynoM]: [How Forward Deployed Engineering is done at Factory — Eno Reyes](https://www.youtube.com/watch?v=wpOA-UXynoM); publication: 2026-07-28T22:00:06Z; analysis: `analysis/wpOA-UXynoM.json`.
