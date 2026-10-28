---
{
  "type": "technique",
  "id": "agent-readiness-checklist",
  "title": "Assess executable validators, setup, docs and test seams before expanding autonomy",
  "area": "architecture-data",
  "status": "stable",
  "valid_from": "2026-10-07T20:00:04Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "CTLa_p6iOiY",
      "resource": "https://www.youtube.com/watch?v=CTLa_p6iOiY",
      "title": "Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs",
      "author": "Pierluca D'Oro, Programma Labs",
      "last_modified": "2026-08-14T14:30:31Z",
      "analysis_file": "analysis/CTLa_p6iOiY.json"
    },
    {
      "id": "RFKCzGlAU6Q",
      "resource": "https://www.youtube.com/watch?v=RFKCzGlAU6Q",
      "title": "How Claude Code Works - Jared Zoneraich, PromptLayer",
      "author": "Jared Zoneraich, PromptLayer",
      "last_modified": "2025-12-26T22:04:34Z",
      "analysis_file": "analysis/RFKCzGlAU6Q.json"
    },
    {
      "id": "Se8jHLliLXE",
      "resource": "https://www.youtube.com/watch?v=Se8jHLliLXE",
      "title": "The State of AI in Software Development: Data from 400+ Orgs — Justin Reock, DX",
      "author": "Justin Reock, DX",
      "last_modified": "2026-09-30T14:30:20Z",
      "analysis_file": "analysis/Se8jHLliLXE.json"
    },
    {
      "id": "XjI-AR4pt7Y",
      "resource": "https://www.youtube.com/watch?v=XjI-AR4pt7Y",
      "title": "Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA",
      "author": "Lovina Dmello, NVIDIA",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/XjI-AR4pt7Y.json"
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
      "id": "wpOA-UXynoM",
      "resource": "https://www.youtube.com/watch?v=wpOA-UXynoM",
      "title": "How Forward Deployed Engineering is done at Factory — Eno Reyes",
      "author": "Eno Reyes",
      "last_modified": "2026-07-28T22:00:06Z",
      "analysis_file": "analysis/wpOA-UXynoM.json"
    },
    {
      "id": "yUmS-F9IX90",
      "resource": "https://www.youtube.com/watch?v=yUmS-F9IX90",
      "title": "Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline",
      "author": "Ara Khan, Cline",
      "last_modified": "2026-05-19T15:00:06Z",
      "analysis_file": "analysis/yUmS-F9IX90.json"
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

# Assess executable validators, setup, docs and test seams before expanding autonomy

## What

Assess executable validators, setup, docs and test seams before expanding autonomy

Check validation, builds, tests, docs, reproducibility, modularity, observability and security before blaming the agent model.

## Evidence

Source analysis [^CTLa_p6iOiY]; no independently matched timestamped quote published.

> repo that the agent can run tests on how do you build the feedback loop because
> — 45:26 [^RFKCzGlAU6Q]

Source analysis [^Se8jHLliLXE]; no independently matched timestamped quote published.

Source analysis [^XjI-AR4pt7Y]; no independently matched timestamped quote published.

> At factory, we have the concept of agent readiness and we evaluate this based on
> — 13:35 [^exiwa9QbQXI]

> is is it's a measure of how many of these deterministic validation loops are
> — 12:31 [^wpOA-UXynoM]

> like the agent other coding agents can easily build your agent, test it, make
> — 08:19 [^yUmS-F9IX90]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Lower future change and maintenance cost
- **Speed:** Faster localized reasoning and edits
- **Quality:** Explicit domain/query semantics
- **Reliability:** Narrow testable boundaries and preserved invariants
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^CTLa_p6iOiY]: [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](https://www.youtube.com/watch?v=CTLa_p6iOiY); publication: 2026-08-14T14:30:31Z; analysis: `analysis/CTLa_p6iOiY.json`.
[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^Se8jHLliLXE]: [The State of AI in Software Development: Data from 400+ Orgs — Justin Reock, DX](https://www.youtube.com/watch?v=Se8jHLliLXE); publication: 2026-09-30T14:30:20Z; analysis: `analysis/Se8jHLliLXE.json`.
[^XjI-AR4pt7Y]: [Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA](https://www.youtube.com/watch?v=XjI-AR4pt7Y); publication: 2026-07-20T17:17:53Z; analysis: `analysis/XjI-AR4pt7Y.json`.
[^exiwa9QbQXI]: [The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](https://www.youtube.com/watch?v=exiwa9QbQXI); publication: 2026-10-07T20:00:04Z; analysis: `analysis/exiwa9QbQXI.json`.
[^wpOA-UXynoM]: [How Forward Deployed Engineering is done at Factory — Eno Reyes](https://www.youtube.com/watch?v=wpOA-UXynoM); publication: 2026-07-28T22:00:06Z; analysis: `analysis/wpOA-UXynoM.json`.
[^yUmS-F9IX90]: [Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline](https://www.youtube.com/watch?v=yUmS-F9IX90); publication: 2026-05-19T15:00:06Z; analysis: `analysis/yUmS-F9IX90.json`.
