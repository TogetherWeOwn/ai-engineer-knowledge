---
{
  "type": "technique",
  "id": "context-relevance-gating",
  "title": "Gate context by task relevance without mistaking relevance filtering for authorization",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-10-19T07:00:39Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "A48uhxfxbsM",
      "resource": "https://www.youtube.com/watch?v=A48uhxfxbsM",
      "title": "Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2026-05-07T17:00:06Z",
      "analysis_file": "analysis/A48uhxfxbsM.json"
    },
    {
      "id": "FDEmbYPgG-s",
      "resource": "https://www.youtube.com/watch?v=FDEmbYPgG-s",
      "title": "Retrieval Augmented Generation in the Wild: Anton Troynikov",
      "author": null,
      "last_modified": "2023-11-15T18:20:31Z",
      "analysis_file": "analysis/FDEmbYPgG-s.json"
    },
    {
      "id": "L4dUFimVDKU",
      "resource": "https://www.youtube.com/watch?v=L4dUFimVDKU",
      "title": "Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa",
      "author": "Ryan Ahern, Exa",
      "last_modified": "2026-10-19T07:00:39Z",
      "analysis_file": "analysis/L4dUFimVDKU.json"
    },
    {
      "id": "Ot4OPrPH4xY",
      "resource": "https://www.youtube.com/watch?v=Ot4OPrPH4xY",
      "title": "The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data",
      "author": "Omer Primor, Bright Data",
      "last_modified": "2026-08-14T16:30:36Z",
      "analysis_file": "analysis/Ot4OPrPH4xY.json"
    },
    {
      "id": "VjEP0xqTUI0",
      "resource": "https://www.youtube.com/watch?v=VjEP0xqTUI0",
      "title": "The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp",
      "author": "Arman Vaziri, Ramp",
      "last_modified": "2026-08-26T14:30:38Z",
      "analysis_file": "analysis/VjEP0xqTUI0.json"
    },
    {
      "id": "XKup1pj-34M",
      "resource": "https://www.youtube.com/watch?v=XKup1pj-34M",
      "title": "The New Application Layer - Malte Ubl, CTO Vercel",
      "author": "Malte Ubl, CTO Vercel",
      "last_modified": "2026-04-20T15:15:06Z",
      "analysis_file": "analysis/XKup1pj-34M.json"
    },
    {
      "id": "eJOjdjO45Sc",
      "resource": "https://www.youtube.com/watch?v=eJOjdjO45Sc",
      "title": "How Deep Research Works - Mukund Sridhar & Aarush Selvan, Google DeepMind",
      "author": "Mukund Sridhar & Aarush Selvan, Google DeepMind",
      "last_modified": "2025-03-26T19:41:41Z",
      "analysis_file": "analysis/eJOjdjO45Sc.json"
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

# Gate context by task relevance without mistaking relevance filtering for authorization

## What

Gate context by task relevance without mistaking relevance filtering for authorization

GEPA has a proposer LLM write new prompts from eval feedback and recombines the best ones (the Pareto frontier), scored against a golden set with a deterministic evaluator. To stop prompts growing with every edge case, split the instructions into snippets and optimize which K to include.

## Evidence

Source analysis [^A48uhxfxbsM]; no independently matched timestamped quote published.

Source analysis [^FDEmbYPgG-s]; no independently matched timestamped quote published.

> technologies to try and return just the tokens that you need, not just across
> — 05:06 [^L4dUFimVDKU]

Source analysis [^Ot4OPrPH4xY]; no independently matched timestamped quote published.

Source analysis [^VjEP0xqTUI0]; no independently matched timestamped quote published.

Source analysis [^XKup1pj-34M]; no independently matched timestamped quote published.

Source analysis [^eJOjdjO45Sc]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^A48uhxfxbsM]: [Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=A48uhxfxbsM); publication: 2026-05-07T17:00:06Z; analysis: `analysis/A48uhxfxbsM.json`.
[^FDEmbYPgG-s]: [Retrieval Augmented Generation in the Wild: Anton Troynikov](https://www.youtube.com/watch?v=FDEmbYPgG-s); publication: 2023-11-15T18:20:31Z; analysis: `analysis/FDEmbYPgG-s.json`.
[^L4dUFimVDKU]: [Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa](https://www.youtube.com/watch?v=L4dUFimVDKU); publication: 2026-10-19T07:00:39Z; analysis: `analysis/L4dUFimVDKU.json`.
[^Ot4OPrPH4xY]: [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](https://www.youtube.com/watch?v=Ot4OPrPH4xY); publication: 2026-08-14T16:30:36Z; analysis: `analysis/Ot4OPrPH4xY.json`.
[^VjEP0xqTUI0]: [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](https://www.youtube.com/watch?v=VjEP0xqTUI0); publication: 2026-08-26T14:30:38Z; analysis: `analysis/VjEP0xqTUI0.json`.
[^XKup1pj-34M]: [The New Application Layer - Malte Ubl, CTO Vercel](https://www.youtube.com/watch?v=XKup1pj-34M); publication: 2026-04-20T15:15:06Z; analysis: `analysis/XKup1pj-34M.json`.
[^eJOjdjO45Sc]: [How Deep Research Works - Mukund Sridhar & Aarush Selvan, Google DeepMind](https://www.youtube.com/watch?v=eJOjdjO45Sc); publication: 2025-03-26T19:41:41Z; analysis: `analysis/eJOjdjO45Sc.json`.
