---
{
  "type": "technique",
  "id": "independent-audit-log",
  "title": "Write immutable audit provenance outside the agent's modification authority",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-14T16:00:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Wb2v9Phhnns",
      "resource": "https://www.youtube.com/watch?v=Wb2v9Phhnns",
      "title": "Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder",
      "author": "Jiachen Jiang, Coder",
      "last_modified": "2026-10-14T16:00:25Z",
      "analysis_file": "analysis/Wb2v9Phhnns.json"
    },
    {
      "id": "ZyC56eV8sVw",
      "resource": "https://www.youtube.com/watch?v=ZyC56eV8sVw",
      "title": "AI Security Engineer Foundations + Certificate — Javier Garza, Snyk",
      "author": "Javier Garza, Snyk",
      "last_modified": "2026-10-11T19:30:16Z",
      "analysis_file": "analysis/ZyC56eV8sVw.json"
    },
    {
      "id": "exiwa9QbQXI",
      "resource": "https://www.youtube.com/watch?v=exiwa9QbQXI",
      "title": "The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory",
      "author": "Davis Palmie, Factory",
      "last_modified": "2026-10-07T20:00:04Z",
      "analysis_file": "analysis/exiwa9QbQXI.json"
    },
    {
      "id": "rbjWzZK2LU0",
      "resource": "https://www.youtube.com/watch?v=rbjWzZK2LU0",
      "title": "Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic",
      "author": "Sachin Malhotra, Anthropic",
      "last_modified": "2026-08-22T14:00:06Z",
      "analysis_file": "analysis/rbjWzZK2LU0.json"
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

# Write immutable audit provenance outside the agent's modification authority

## What

Write immutable audit provenance outside the agent's modification authority

Agent-generated logs or claimed test passes cannot be the sole incident record if the same agent can rewrite them.

## Evidence

> The last important piece here is having audit logging that you own, not the
> — 13:53 [^Wb2v9Phhnns]

Source analysis [^ZyC56eV8sVw]; no independently matched timestamped quote published.

> agent performance and control behavior. At factory, every action is auditable.
> — 14:58 [^exiwa9QbQXI]

> whether it's a skip or an unskip. um the agent technically never holds uh the pen
> — 08:18 [^rbjWzZK2LU0]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Wb2v9Phhnns]: [Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder](https://www.youtube.com/watch?v=Wb2v9Phhnns); publication: 2026-10-14T16:00:25Z; analysis: `analysis/Wb2v9Phhnns.json`.
[^ZyC56eV8sVw]: [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](https://www.youtube.com/watch?v=ZyC56eV8sVw); publication: 2026-10-11T19:30:16Z; analysis: `analysis/ZyC56eV8sVw.json`.
[^exiwa9QbQXI]: [The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](https://www.youtube.com/watch?v=exiwa9QbQXI); publication: 2026-10-07T20:00:04Z; analysis: `analysis/exiwa9QbQXI.json`.
[^rbjWzZK2LU0]: [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](https://www.youtube.com/watch?v=rbjWzZK2LU0); publication: 2026-08-22T14:00:06Z; analysis: `analysis/rbjWzZK2LU0.json`.
