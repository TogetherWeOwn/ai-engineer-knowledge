---
{
  "type": "technique",
  "id": "retrieval-query",
  "title": "Generate focused retrieval queries and broaden only after misses",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-10-11T10:00:18Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "O84lhGc1OOI",
      "resource": "https://www.youtube.com/watch?v=O84lhGc1OOI",
      "title": "If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread",
      "author": "Benjamin Clavié, Mixedbread",
      "last_modified": "2026-09-16T15:00:39Z",
      "analysis_file": "analysis/O84lhGc1OOI.json"
    },
    {
      "id": "T5IMo5ntyhA",
      "resource": "https://www.youtube.com/watch?v=T5IMo5ntyhA",
      "title": "Stop Using RAG as Memory — Daniel Chalef, Zep",
      "author": "Daniel Chalef, Zep",
      "last_modified": "2025-07-22T16:00:06Z",
      "analysis_file": "analysis/T5IMo5ntyhA.json"
    },
    {
      "id": "eXA2tjRZIbY",
      "resource": "https://www.youtube.com/watch?v=eXA2tjRZIbY",
      "title": "The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI",
      "author": "Varun Krovvidi, Resolve AI",
      "last_modified": "2026-10-06T23:30:36Z",
      "analysis_file": "analysis/eXA2tjRZIbY.json"
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
      "id": "lArgRvBV3tQ",
      "resource": "https://www.youtube.com/watch?v=lArgRvBV3tQ",
      "title": "Forget RAG Pipelines—Build Production Ready Agents in 15 Mins: Nina Lopatina, Rajiv Shah, Contextual",
      "author": null,
      "last_modified": "2025-06-27T10:35:06Z",
      "analysis_file": "analysis/lArgRvBV3tQ.json"
    },
    {
      "id": "pZ4DIH2BVqg",
      "resource": "https://www.youtube.com/watch?v=pZ4DIH2BVqg",
      "title": "Pydantic is STILL all you need: Jason Liu",
      "author": null,
      "last_modified": "2024-09-06T17:07:06Z",
      "analysis_file": "analysis/pZ4DIH2BVqg.json"
    },
    {
      "id": "pijYURicI1Y",
      "resource": "https://www.youtube.com/watch?v=pijYURicI1Y",
      "title": "Building efficient hybrid context query for LLM grounding: Simrat Hanspal",
      "author": null,
      "last_modified": "2025-02-05T11:18:34Z",
      "analysis_file": "analysis/pijYURicI1Y.json"
    },
    {
      "id": "spxoDAfh5ig",
      "resource": "https://www.youtube.com/watch?v=spxoDAfh5ig",
      "title": "Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked",
      "author": "Peter Werry, Unblocked",
      "last_modified": "2026-10-11T10:00:18Z",
      "analysis_file": "analysis/spxoDAfh5ig.json"
    },
    {
      "id": "vNCY9kXXyDQ",
      "resource": "https://www.youtube.com/watch?v=vNCY9kXXyDQ",
      "title": "Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse",
      "author": "Marc Klingen, Clickhouse",
      "last_modified": "2026-05-20T15:00:06Z",
      "analysis_file": "analysis/vNCY9kXXyDQ.json"
    },
    {
      "id": "xLUQOqjudtA",
      "resource": "https://www.youtube.com/watch?v=xLUQOqjudtA",
      "title": "Tolan: Voice-First AI Companion — Paula Dozsa, Tolan",
      "author": "Paula Dozsa, Tolan",
      "last_modified": "2026-09-15T14:30:14Z",
      "analysis_file": "analysis/xLUQOqjudtA.json"
    },
    {
      "id": "xnXqpUW_Kp8",
      "resource": "https://www.youtube.com/watch?v=xnXqpUW_Kp8",
      "title": "Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai",
      "author": "Will Bryk, Exa.ai",
      "last_modified": "2025-07-29T07:01:00Z",
      "analysis_file": "analysis/xnXqpUW_Kp8.json"
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

# Generate focused retrieval queries and broaden only after misses

## What

Generate focused retrieval queries and broaden only after misses

Initial graph navigation locates the problem; bounded log/metric/code calls gather just the next needed evidence.

## Evidence

> problem for me. Please write queries about the aspects that you think are
> — 14:28 [^O84lhGc1OOI]

Source analysis [^T5IMo5ntyhA]; no independently matched timestamped quote published.

Source analysis [^eXA2tjRZIbY]; no independently matched timestamped quote published.

Source analysis [^fZH97QHHYjY]; no independently matched timestamped quote published.

Source analysis [^lArgRvBV3tQ]; no independently matched timestamped quote published.

> have a search question query for y a search query for x and again my rag
> — 09:01 [^pZ4DIH2BVqg]

Source analysis [^pijYURicI1Y]; no independently matched timestamped quote published.

Source analysis [^spxoDAfh5ig]; no independently matched timestamped quote published.

Source analysis [^vNCY9kXXyDQ]; no independently matched timestamped quote published.

> questions about the person and the relationship and retrieve against those.
> — 07:52 [^xLUQOqjudtA]

Source analysis [^xnXqpUW_Kp8]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^O84lhGc1OOI]: [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](https://www.youtube.com/watch?v=O84lhGc1OOI); publication: 2026-09-16T15:00:39Z; analysis: `analysis/O84lhGc1OOI.json`.
[^T5IMo5ntyhA]: [Stop Using RAG as Memory — Daniel Chalef, Zep](https://www.youtube.com/watch?v=T5IMo5ntyhA); publication: 2025-07-22T16:00:06Z; analysis: `analysis/T5IMo5ntyhA.json`.
[^eXA2tjRZIbY]: [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](https://www.youtube.com/watch?v=eXA2tjRZIbY); publication: 2026-10-06T23:30:36Z; analysis: `analysis/eXA2tjRZIbY.json`.
[^fZH97QHHYjY]: [The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev](https://www.youtube.com/watch?v=fZH97QHHYjY); publication: 2026-09-16T13:30:32Z; analysis: `analysis/fZH97QHHYjY.json`.
[^lArgRvBV3tQ]: [Forget RAG Pipelines—Build Production Ready Agents in 15 Mins: Nina Lopatina, Rajiv Shah, Contextual](https://www.youtube.com/watch?v=lArgRvBV3tQ); publication: 2025-06-27T10:35:06Z; analysis: `analysis/lArgRvBV3tQ.json`.
[^pZ4DIH2BVqg]: [Pydantic is STILL all you need: Jason Liu](https://www.youtube.com/watch?v=pZ4DIH2BVqg); publication: 2024-09-06T17:07:06Z; analysis: `analysis/pZ4DIH2BVqg.json`.
[^pijYURicI1Y]: [Building efficient hybrid context query for LLM grounding: Simrat Hanspal](https://www.youtube.com/watch?v=pijYURicI1Y); publication: 2025-02-05T11:18:34Z; analysis: `analysis/pijYURicI1Y.json`.
[^spxoDAfh5ig]: [Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked](https://www.youtube.com/watch?v=spxoDAfh5ig); publication: 2026-10-11T10:00:18Z; analysis: `analysis/spxoDAfh5ig.json`.
[^vNCY9kXXyDQ]: [Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse](https://www.youtube.com/watch?v=vNCY9kXXyDQ); publication: 2026-05-20T15:00:06Z; analysis: `analysis/vNCY9kXXyDQ.json`.
[^xLUQOqjudtA]: [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](https://www.youtube.com/watch?v=xLUQOqjudtA); publication: 2026-09-15T14:30:14Z; analysis: `analysis/xLUQOqjudtA.json`.
[^xnXqpUW_Kp8]: [Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai](https://www.youtube.com/watch?v=xnXqpUW_Kp8); publication: 2025-07-29T07:01:00Z; analysis: `analysis/xnXqpUW_Kp8.json`.
