---
{
  "type": "technique",
  "id": "attack-surface-inventory",
  "title": "Inventory generated code, model components, tool capabilities and runtime actions separately",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-11T19:30:16Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "ZyC56eV8sVw",
      "resource": "https://www.youtube.com/watch?v=ZyC56eV8sVw",
      "title": "AI Security Engineer Foundations + Certificate — Javier Garza, Snyk",
      "author": "Javier Garza, Snyk",
      "last_modified": "2026-10-11T19:30:16Z",
      "analysis_file": "analysis/ZyC56eV8sVw.json"
    },
    {
      "id": "cgimkNGNjvU",
      "resource": "https://www.youtube.com/watch?v=cgimkNGNjvU",
      "title": "Agentic Development Security — Ezra Tanzer, Snyk",
      "author": "Ezra Tanzer, Snyk",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/cgimkNGNjvU.json"
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

# Inventory generated code, model components, tool capabilities and runtime actions separately

## What

Inventory generated code, model components, tool capabilities and runtime actions separately

Code scanning, supply-chain review and runtime authorization address different threat surfaces; none substitutes for the other two.

## Evidence

Source analysis [^ZyC56eV8sVw]; no independently matched timestamped quote published.

> secure what agents generate, what they use, and what they do. Um and I'll spend
> — 04:03 [^cgimkNGNjvU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^ZyC56eV8sVw]: [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](https://www.youtube.com/watch?v=ZyC56eV8sVw); publication: 2026-10-11T19:30:16Z; analysis: `analysis/ZyC56eV8sVw.json`.
[^cgimkNGNjvU]: [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU); publication: 2026-07-20T17:17:53Z; analysis: `analysis/cgimkNGNjvU.json`.
