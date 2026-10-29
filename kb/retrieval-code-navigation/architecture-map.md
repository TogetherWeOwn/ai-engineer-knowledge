---
{
  "type": "technique",
  "id": "architecture-map",
  "title": "Supply a compact repository architecture and dependency map",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-10-05T22:30:12Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "6NIr_cYPglk",
      "resource": "https://www.youtube.com/watch?v=6NIr_cYPglk",
      "title": "To the moon! Navigating deep context in legacy code with Augment Agent — Forrest Brazeal, Matt Ball",
      "author": "Forrest Brazeal, Matt Ball",
      "last_modified": "2025-06-27T10:46:59Z",
      "analysis_file": "analysis/6NIr_cYPglk.json"
    },
    {
      "id": "9fubhllmsBU",
      "resource": "https://www.youtube.com/watch?v=9fubhllmsBU",
      "title": "Field Guide to Fable — Thariq Shihipar, Anthropic",
      "author": "Thariq Shihipar, Anthropic",
      "last_modified": "2026-07-06T16:00:06Z",
      "analysis_file": "analysis/9fubhllmsBU.json"
    },
    {
      "id": "UOcHfR3_tys",
      "resource": "https://www.youtube.com/watch?v=UOcHfR3_tys",
      "title": "Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band",
      "author": "Vlad Luzin, Band",
      "last_modified": "2026-09-30T13:00:33Z",
      "analysis_file": "analysis/UOcHfR3_tys.json"
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
      "id": "_QAVExf_1uw",
      "resource": "https://www.youtube.com/watch?v=_QAVExf_1uw",
      "title": "Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure",
      "author": null,
      "last_modified": "2026-05-05T13:00:06Z",
      "analysis_file": "analysis/_QAVExf_1uw.json"
    },
    {
      "id": "g03m-WFEu1U",
      "resource": "https://www.youtube.com/watch?v=g03m-WFEu1U",
      "title": "How to Improve your Vibe Coding — Ian Butler",
      "author": "Ian Butler",
      "last_modified": "2025-08-03T04:32:57Z",
      "analysis_file": "analysis/g03m-WFEu1U.json"
    },
    {
      "id": "whue9_YquGA",
      "resource": "https://www.youtube.com/watch?v=whue9_YquGA",
      "title": "Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation",
      "author": "Angie Jones, Agentic AI Foundation",
      "last_modified": "2026-06-28T19:00:10Z",
      "analysis_file": "analysis/whue9_YquGA.json"
    },
    {
      "id": "wzWNYDY7toc",
      "resource": "https://www.youtube.com/watch?v=wzWNYDY7toc",
      "title": "From Raw Documents to AI-Ready Data — Leo Platzer & Jeff Koss",
      "author": "Leo Platzer & Jeff Koss",
      "last_modified": "2026-10-05T22:30:12Z",
      "analysis_file": "analysis/wzWNYDY7toc.json"
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

# Supply a compact repository architecture and dependency map

## What

Supply a compact repository architecture and dependency map

Expose service ownership, interfaces and dependency edges as structured data so agents can discover impact without reconstructing the company from prose each time.

## Evidence

Source analysis [^6NIr_cYPglk]; no independently matched timestamped quote published.

Source analysis [^9fubhllmsBU]; no independently matched timestamped quote published.

Source analysis [^UOcHfR3_tys]; no independently matched timestamped quote published.

> understand your codebase. So, how do you give it architectural awareness? How do
> — 10:07 [^VrpEyglYgeU]

Source analysis [^_QAVExf_1uw]; no independently matched timestamped quote published.

Source analysis [^g03m-WFEu1U]; no independently matched timestamped quote published.

Source analysis [^whue9_YquGA]; no independently matched timestamped quote published.

Source analysis [^wzWNYDY7toc]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^6NIr_cYPglk]: [To the moon! Navigating deep context in legacy code with Augment Agent — Forrest Brazeal, Matt Ball](https://www.youtube.com/watch?v=6NIr_cYPglk); publication: 2025-06-27T10:46:59Z; analysis: `analysis/6NIr_cYPglk.json`.
[^9fubhllmsBU]: [Field Guide to Fable — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=9fubhllmsBU); publication: 2026-07-06T16:00:06Z; analysis: `analysis/9fubhllmsBU.json`.
[^UOcHfR3_tys]: [Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band](https://www.youtube.com/watch?v=UOcHfR3_tys); publication: 2026-09-30T13:00:33Z; analysis: `analysis/UOcHfR3_tys.json`.
[^VrpEyglYgeU]: [In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](https://www.youtube.com/watch?v=VrpEyglYgeU); publication: 2026-07-20T15:00:06Z; analysis: `analysis/VrpEyglYgeU.json`.
[^_QAVExf_1uw]: [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](https://www.youtube.com/watch?v=_QAVExf_1uw); publication: 2026-05-05T13:00:06Z; analysis: `analysis/_QAVExf_1uw.json`.
[^g03m-WFEu1U]: [How to Improve your Vibe Coding — Ian Butler](https://www.youtube.com/watch?v=g03m-WFEu1U); publication: 2025-08-03T04:32:57Z; analysis: `analysis/g03m-WFEu1U.json`.
[^whue9_YquGA]: [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](https://www.youtube.com/watch?v=whue9_YquGA); publication: 2026-06-28T19:00:10Z; analysis: `analysis/whue9_YquGA.json`.
[^wzWNYDY7toc]: [From Raw Documents to AI-Ready Data — Leo Platzer & Jeff Koss](https://www.youtube.com/watch?v=wzWNYDY7toc); publication: 2026-10-05T22:30:12Z; analysis: `analysis/wzWNYDY7toc.json`.
