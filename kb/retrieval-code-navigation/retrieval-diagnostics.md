---
{
  "type": "technique",
  "id": "retrieval-diagnostics",
  "title": "Separate retrieval misses from reasoning failures with oracle-gap analysis",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-10-14T12:00:07Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "6YdPI9YbjbI",
      "resource": "https://www.youtube.com/watch?v=6YdPI9YbjbI",
      "title": "How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)",
      "author": "Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)",
      "last_modified": "2025-06-27T10:40:32Z",
      "analysis_file": "analysis/6YdPI9YbjbI.json"
    },
    {
      "id": "LzeC1AQ-U5o",
      "resource": "https://www.youtube.com/watch?v=LzeC1AQ-U5o",
      "title": "Building Blocks for LLM Systems & Products: Eugene Yan",
      "author": null,
      "last_modified": "2023-11-02T13:08:20Z",
      "analysis_file": "analysis/LzeC1AQ-U5o.json"
    },
    {
      "id": "O84lhGc1OOI",
      "resource": "https://www.youtube.com/watch?v=O84lhGc1OOI",
      "title": "If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread",
      "author": "Benjamin Clavié, Mixedbread",
      "last_modified": "2026-09-16T15:00:39Z",
      "analysis_file": "analysis/O84lhGc1OOI.json"
    },
    {
      "id": "R3-anFK1YM8",
      "resource": "https://www.youtube.com/watch?v=R3-anFK1YM8",
      "title": "Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai",
      "author": "Stefania Druga, Sakana.ai",
      "last_modified": "2026-08-12T15:00:06Z",
      "analysis_file": "analysis/R3-anFK1YM8.json"
    },
    {
      "id": "fZH97QHHYjY",
      "resource": "https://www.youtube.com/watch?v=fZH97QHHYjY",
      "title": "The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev",
      "author": "Jo Kristian Bergum, Hornet.dev",
      "last_modified": "2026-09-16T13:30:32Z",
      "analysis_file": "analysis/fZH97QHHYjY.json"
    },
    {
      "id": "gonAewBZxfU",
      "resource": "https://www.youtube.com/watch?v=gonAewBZxfU",
      "title": "Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket",
      "author": "Eleonora Drykina & Nina Žižakić, In The Pocket",
      "last_modified": "2026-10-14T12:00:07Z",
      "analysis_file": "analysis/gonAewBZxfU.json"
    },
    {
      "id": "qflLT3SoVbw",
      "resource": "https://www.youtube.com/watch?v=qflLT3SoVbw",
      "title": "Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava",
      "author": "Anant Srivastava",
      "last_modified": "2026-10-04T00:00:35Z",
      "analysis_file": "analysis/qflLT3SoVbw.json"
    },
    {
      "id": "vljxQZfJ9wY",
      "resource": "https://www.youtube.com/watch?v=vljxQZfJ9wY",
      "title": "Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs",
      "author": "Nishant Gupta, Meta Superintelligence Labs",
      "last_modified": "2026-06-25T18:15:06Z",
      "analysis_file": "analysis/vljxQZfJ9wY.json"
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

# Separate retrieval misses from reasoning failures with oracle-gap analysis

## What

Separate retrieval misses from reasoning failures with oracle-gap analysis

Compare observed results with results given the right evidence to distinguish missing-information failures from reasoning failures.

## Evidence

Source analysis [^6YdPI9YbjbI]; no independently matched timestamped quote published.

> reinvent the wheel bm25 metadata fetching uh metadata matching can get
> — 16:26 [^LzeC1AQ-U5o]

> like an oracle gap. And the oracle gap is the difference between perfect
> — 14:47 [^O84lhGc1OOI]

> to the model but it doesn't force it to use it. So the model can get the right
> — 08:44 [^R3-anFK1YM8]

Source analysis [^fZH97QHHYjY]; no independently matched timestamped quote published.

Source analysis [^gonAewBZxfU]; no independently matched timestamped quote published.

Source analysis [^qflLT3SoVbw]; no independently matched timestamped quote published.

> multi-agent coordination failures. And this is why evaluating only model
> — 02:33 [^vljxQZfJ9wY]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^6YdPI9YbjbI]: [How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)](https://www.youtube.com/watch?v=6YdPI9YbjbI); publication: 2025-06-27T10:40:32Z; analysis: `analysis/6YdPI9YbjbI.json`.
[^LzeC1AQ-U5o]: [Building Blocks for LLM Systems & Products: Eugene Yan](https://www.youtube.com/watch?v=LzeC1AQ-U5o); publication: 2023-11-02T13:08:20Z; analysis: `analysis/LzeC1AQ-U5o.json`.
[^O84lhGc1OOI]: [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](https://www.youtube.com/watch?v=O84lhGc1OOI); publication: 2026-09-16T15:00:39Z; analysis: `analysis/O84lhGc1OOI.json`.
[^R3-anFK1YM8]: [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](https://www.youtube.com/watch?v=R3-anFK1YM8); publication: 2026-08-12T15:00:06Z; analysis: `analysis/R3-anFK1YM8.json`.
[^fZH97QHHYjY]: [The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev](https://www.youtube.com/watch?v=fZH97QHHYjY); publication: 2026-09-16T13:30:32Z; analysis: `analysis/fZH97QHHYjY.json`.
[^gonAewBZxfU]: [Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket](https://www.youtube.com/watch?v=gonAewBZxfU); publication: 2026-10-14T12:00:07Z; analysis: `analysis/gonAewBZxfU.json`.
[^qflLT3SoVbw]: [Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava](https://www.youtube.com/watch?v=qflLT3SoVbw); publication: 2026-10-04T00:00:35Z; analysis: `analysis/qflLT3SoVbw.json`.
[^vljxQZfJ9wY]: [Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs](https://www.youtube.com/watch?v=vljxQZfJ9wY); publication: 2026-06-25T18:15:06Z; analysis: `analysis/vljxQZfJ9wY.json`.
