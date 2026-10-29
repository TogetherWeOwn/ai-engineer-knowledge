---
{
  "type": "technique",
  "id": "pluggable-execution-provider",
  "title": "Select supported sandbox providers by declared operation and environment requirements",
  "area": "sandbox-compute",
  "status": "stable",
  "valid_from": "2026-10-12T06:07:45Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "L173Z8DpaJg",
      "resource": "https://www.youtube.com/watch?v=L173Z8DpaJg",
      "title": "The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp",
      "author": "Safia Abdalla, Warp",
      "last_modified": "2026-08-22T17:30:13Z",
      "analysis_file": "analysis/L173Z8DpaJg.json"
    },
    {
      "id": "QSeaZ6qHyXs",
      "resource": "https://www.youtube.com/watch?v=QSeaZ6qHyXs",
      "title": "Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T06:07:45Z",
      "analysis_file": "analysis/QSeaZ6qHyXs.json"
    },
    {
      "id": "Uv0nAf_7tyU",
      "resource": "https://www.youtube.com/watch?v=Uv0nAf_7tyU",
      "title": "Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T05:44:00Z",
      "analysis_file": "analysis/Uv0nAf_7tyU.json"
    },
    {
      "id": "pMggiOb18tc",
      "resource": "https://www.youtube.com/watch?v=pMggiOb18tc",
      "title": "The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI",
      "author": "Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI",
      "last_modified": "2026-07-09T18:53:34Z",
      "analysis_file": "analysis/pMggiOb18tc.json"
    },
    {
      "id": "s-glGHAa1a4",
      "resource": "https://www.youtube.com/watch?v=s-glGHAa1a4",
      "title": "An AI Future Without the Lock-In — Remy Guercio, Tailscale",
      "author": "Remy Guercio, Tailscale",
      "last_modified": "2026-10-11T00:00:35Z",
      "analysis_file": "analysis/s-glGHAa1a4.json"
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

# Select supported sandbox providers by declared operation and environment requirements

## What

Select supported sandbox providers by declared operation and environment requirements

Some jobs require local resources while others are suitable for isolated cloud execution; placement can be separated from user interaction.

## Evidence

Source analysis [^L173Z8DpaJg]; no independently matched timestamped quote published.

Source analysis [^QSeaZ6qHyXs]; no independently matched timestamped quote published.

> MCP server. So all these like hands are essentially interchangeable. You can
> — 11:02 [^Uv0nAf_7tyU]

> any of my machines. They should know which work can be done
> — 24:01 [^pMggiOb18tc]

Source analysis [^s-glGHAa1a4]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable idle and duplicated compute
- **Speed:** Reduce measured execution/queue bottlenecks
- **Quality:** Reproducible command and environment evidence
- **Reliability:** Isolation, cleanup and recovery guarantees
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^L173Z8DpaJg]: [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](https://www.youtube.com/watch?v=L173Z8DpaJg); publication: 2026-08-22T17:30:13Z; analysis: `analysis/L173Z8DpaJg.json`.
[^QSeaZ6qHyXs]: [Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic](https://www.youtube.com/watch?v=QSeaZ6qHyXs); publication: 2026-10-12T06:07:45Z; analysis: `analysis/QSeaZ6qHyXs.json`.
[^Uv0nAf_7tyU]: [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](https://www.youtube.com/watch?v=Uv0nAf_7tyU); publication: 2026-10-12T05:44:00Z; analysis: `analysis/Uv0nAf_7tyU.json`.
[^pMggiOb18tc]: [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](https://www.youtube.com/watch?v=pMggiOb18tc); publication: 2026-07-09T18:53:34Z; analysis: `analysis/pMggiOb18tc.json`.
[^s-glGHAa1a4]: [An AI Future Without the Lock-In — Remy Guercio, Tailscale](https://www.youtube.com/watch?v=s-glGHAa1a4); publication: 2026-10-11T00:00:35Z; analysis: `analysis/s-glGHAa1a4.json`.
