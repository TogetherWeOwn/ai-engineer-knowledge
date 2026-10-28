---
{
  "type": "technique",
  "id": "evaluation-contracts",
  "title": "Define reusable task, dataset and scorer contracts before interpreting scores",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-17T19:00:23Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "GgLQ02aO-hs",
      "resource": "https://www.youtube.com/watch?v=GgLQ02aO-hs",
      "title": "The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller",
      "author": "Maxime Rivest & Isaac Miller",
      "last_modified": "2026-07-23T17:45:06Z",
      "analysis_file": "analysis/GgLQ02aO-hs.json"
    },
    {
      "id": "L2r6vLlLgs8",
      "resource": "https://www.youtube.com/watch?v=L2r6vLlLgs8",
      "title": "Fighting AI with AI — Lawrence Jones, Incident",
      "author": "Lawrence Jones, Incident",
      "last_modified": "2026-05-17T16:30:07Z",
      "analysis_file": "analysis/L2r6vLlLgs8.json"
    },
    {
      "id": "PthmdT92qNg",
      "resource": "https://www.youtube.com/watch?v=PthmdT92qNg",
      "title": "Shipping Products When You Don't Know What they Can Do — Ben Stein, Teammates",
      "author": "Ben Stein, Teammates",
      "last_modified": "2025-07-28T19:55:05Z",
      "analysis_file": "analysis/PthmdT92qNg.json"
    },
    {
      "id": "RVN9HWKmkNU",
      "resource": "https://www.youtube.com/watch?v=RVN9HWKmkNU",
      "title": "Will Agent evaluation via MCP Stabilize Agent Networks? - Ari Heljakka",
      "author": "Ari Heljakka",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/RVN9HWKmkNU.json"
    },
    {
      "id": "RmJ4rTLV_x4",
      "resource": "https://www.youtube.com/watch?v=RmJ4rTLV_x4",
      "title": "Your Support Team Should Ship Code – Lisa Orr, Zapier",
      "author": "Lisa Orr, Zapier",
      "last_modified": "2025-12-16T17:00:06Z",
      "analysis_file": "analysis/RmJ4rTLV_x4.json"
    },
    {
      "id": "SHMCGrNJJGc",
      "resource": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
      "title": "How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-17T19:00:23Z",
      "analysis_file": "analysis/SHMCGrNJJGc.json"
    },
    {
      "id": "Ubwb6NzegyA",
      "resource": "https://www.youtube.com/watch?v=Ubwb6NzegyA",
      "title": "Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind",
      "author": "Nicholas Kang & Michael Aaron, Google DeepMind",
      "last_modified": "2026-05-25T17:00:06Z",
      "analysis_file": "analysis/Ubwb6NzegyA.json"
    },
    {
      "id": "_fQ7Z_Wfouk",
      "resource": "https://www.youtube.com/watch?v=_fQ7Z_Wfouk",
      "title": "Why building eval platforms is hard — Phil Hetzel, Braintrust",
      "author": "Phil Hetzel, Braintrust",
      "last_modified": "2026-04-28T16:00:06Z",
      "analysis_file": "analysis/_fQ7Z_Wfouk.json"
    },
    {
      "id": "bk0TmxoZlUY",
      "resource": "https://www.youtube.com/watch?v=bk0TmxoZlUY",
      "title": "Evals 101 — Doug Guthrie, Braintrust",
      "author": "Doug Guthrie, Braintrust",
      "last_modified": "2025-06-27T10:53:13Z",
      "analysis_file": "analysis/bk0TmxoZlUY.json"
    },
    {
      "id": "coKKKKh8Vns",
      "resource": "https://www.youtube.com/watch?v=coKKKKh8Vns",
      "title": "How to run Evals at Scale: Thinking beyond Accuracy or Similarity — Muktesh Mishra, Adobe",
      "author": "Muktesh Mishra, Adobe",
      "last_modified": "2025-07-22T19:46:22Z",
      "analysis_file": "analysis/coKKKKh8Vns.json"
    },
    {
      "id": "eSvXbb2EBYc",
      "resource": "https://www.youtube.com/watch?v=eSvXbb2EBYc",
      "title": "Building AI Products That Actually Work — Ben Hylak (Raindrop), Sid Bendre (Oleve)",
      "author": "Ben Hylak (Raindrop), Sid Bendre (Oleve)",
      "last_modified": "2025-07-24T17:15:06Z",
      "analysis_file": "analysis/eSvXbb2EBYc.json"
    },
    {
      "id": "pj_hKFhnJCw",
      "resource": "https://www.youtube.com/watch?v=pj_hKFhnJCw",
      "title": "How to evaluate a model for your use case: Emmanuel Turlay",
      "author": null,
      "last_modified": "2025-02-05T11:18:34Z",
      "analysis_file": "analysis/pj_hKFhnJCw.json"
    },
    {
      "id": "sn79oS4MZFI",
      "resource": "https://www.youtube.com/watch?v=sn79oS4MZFI",
      "title": "Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason",
      "author": "Dan Mason",
      "last_modified": "2025-06-22T16:00:06Z",
      "analysis_file": "analysis/sn79oS4MZFI.json"
    },
    {
      "id": "uU5Gv2h8-9g",
      "resource": "https://www.youtube.com/watch?v=uU5Gv2h8-9g",
      "title": "Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison",
      "author": "Cat Wu & Thariq Shihipar ft Simon Willison",
      "last_modified": "2026-07-15T15:05:06Z",
      "analysis_file": "analysis/uU5Gv2h8-9g.json"
    },
    {
      "id": "y2Drx0SDZLo",
      "resource": "https://www.youtube.com/watch?v=y2Drx0SDZLo",
      "title": "Agent Evals: Finally, With The Map",
      "author": null,
      "last_modified": "2025-02-22T19:00:31Z",
      "analysis_file": "analysis/y2Drx0SDZLo.json"
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

# Define reusable task, dataset and scorer contracts before interpreting scores

## What

Define reusable task, dataset and scorer contracts before interpreting scores

Separating executable task, examples and scoring logic makes tests reproducible and reusable from code or another interface.

## Evidence

Source analysis [^GgLQ02aO-hs]; no independently matched timestamped quote published.

> small CLI that can go what test cases do you have in here? I want to edit one, I
> — 07:07 [^L2r6vLlLgs8]

Source analysis [^PthmdT92qNg]; no independently matched timestamped quote published.

Source analysis [^RVN9HWKmkNU]; no independently matched timestamped quote published.

> agent is working so we ask three questions categorization right is was it
> — 12:41 [^RmJ4rTLV_x4]

Source analysis [^SHMCGrNJJGc]; no independently matched timestamped quote published.

Source analysis [^Ubwb6NzegyA]; no independently matched timestamped quote published.

Source analysis [^_fQ7Z_Wfouk]; no independently matched timestamped quote published.

> Again, like just to summarize, we need a task, we need a data set, and we need at
> — 23:19 [^bk0TmxoZlUY]

Source analysis [^coKKKKh8Vns]; no independently matched timestamped quote published.

Source analysis [^eSvXbb2EBYc]; no independently matched timestamped quote published.

Source analysis [^pj_hKFhnJCw]; no independently matched timestamped quote published.

> this very fuzzy. What we really want to know is is anything completely busted,
> — 1:37:21 [^sn79oS4MZFI]

> or people really don't like it when it says like, "Hey, I finished two out of
> — 19:51 [^uU5Gv2h8-9g]

> actually neatly divided to the semantic and behavioral parts of what the agents
> — 00:44 [^y2Drx0SDZLo]

> the task progression and planning or then individual selection and usage of
> — 01:51 [^y2Drx0SDZLo]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^GgLQ02aO-hs]: [The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller](https://www.youtube.com/watch?v=GgLQ02aO-hs); publication: 2026-07-23T17:45:06Z; analysis: `analysis/GgLQ02aO-hs.json`.
[^L2r6vLlLgs8]: [Fighting AI with AI — Lawrence Jones, Incident](https://www.youtube.com/watch?v=L2r6vLlLgs8); publication: 2026-05-17T16:30:07Z; analysis: `analysis/L2r6vLlLgs8.json`.
[^PthmdT92qNg]: [Shipping Products When You Don't Know What they Can Do — Ben Stein, Teammates](https://www.youtube.com/watch?v=PthmdT92qNg); publication: 2025-07-28T19:55:05Z; analysis: `analysis/PthmdT92qNg.json`.
[^RVN9HWKmkNU]: [Will Agent evaluation via MCP Stabilize Agent Networks? - Ari Heljakka](https://www.youtube.com/watch?v=RVN9HWKmkNU); publication: 2025-06-03T22:22:28Z; analysis: `analysis/RVN9HWKmkNU.json`.
[^RmJ4rTLV_x4]: [Your Support Team Should Ship Code – Lisa Orr, Zapier](https://www.youtube.com/watch?v=RmJ4rTLV_x4); publication: 2025-12-16T17:00:06Z; analysis: `analysis/RmJ4rTLV_x4.json`.
[^SHMCGrNJJGc]: [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=SHMCGrNJJGc); publication: 2026-10-17T19:00:23Z; analysis: `analysis/SHMCGrNJJGc.json`.
[^Ubwb6NzegyA]: [Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind](https://www.youtube.com/watch?v=Ubwb6NzegyA); publication: 2026-05-25T17:00:06Z; analysis: `analysis/Ubwb6NzegyA.json`.
[^_fQ7Z_Wfouk]: [Why building eval platforms is hard — Phil Hetzel, Braintrust](https://www.youtube.com/watch?v=_fQ7Z_Wfouk); publication: 2026-04-28T16:00:06Z; analysis: `analysis/_fQ7Z_Wfouk.json`.
[^bk0TmxoZlUY]: [Evals 101 — Doug Guthrie, Braintrust](https://www.youtube.com/watch?v=bk0TmxoZlUY); publication: 2025-06-27T10:53:13Z; analysis: `analysis/bk0TmxoZlUY.json`.
[^coKKKKh8Vns]: [How to run Evals at Scale: Thinking beyond Accuracy or Similarity — Muktesh Mishra, Adobe](https://www.youtube.com/watch?v=coKKKKh8Vns); publication: 2025-07-22T19:46:22Z; analysis: `analysis/coKKKKh8Vns.json`.
[^eSvXbb2EBYc]: [Building AI Products That Actually Work — Ben Hylak (Raindrop), Sid Bendre (Oleve)](https://www.youtube.com/watch?v=eSvXbb2EBYc); publication: 2025-07-24T17:15:06Z; analysis: `analysis/eSvXbb2EBYc.json`.
[^pj_hKFhnJCw]: [How to evaluate a model for your use case: Emmanuel Turlay](https://www.youtube.com/watch?v=pj_hKFhnJCw); publication: 2025-02-05T11:18:34Z; analysis: `analysis/pj_hKFhnJCw.json`.
[^sn79oS4MZFI]: [Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason](https://www.youtube.com/watch?v=sn79oS4MZFI); publication: 2025-06-22T16:00:06Z; analysis: `analysis/sn79oS4MZFI.json`.
[^uU5Gv2h8-9g]: [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](https://www.youtube.com/watch?v=uU5Gv2h8-9g); publication: 2026-07-15T15:05:06Z; analysis: `analysis/uU5Gv2h8-9g.json`.
[^y2Drx0SDZLo]: [Agent Evals: Finally, With The Map](https://www.youtube.com/watch?v=y2Drx0SDZLo); publication: 2025-02-22T19:00:31Z; analysis: `analysis/y2Drx0SDZLo.json`.
