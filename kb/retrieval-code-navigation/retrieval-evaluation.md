---
{
  "type": "technique",
  "id": "retrieval-evaluation",
  "title": "Measure retrieval coverage, relevance, grounding and cost on real file-finding tasks",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-09-16T16:30:16Z",
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
      "id": "RGSFUqzqErE",
      "resource": "https://www.youtube.com/watch?v=RGSFUqzqErE",
      "title": "On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft",
      "author": "Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft",
      "last_modified": "2026-07-17T16:30:06Z",
      "analysis_file": "analysis/RGSFUqzqErE.json"
    },
    {
      "id": "c5qJHr3DnT4",
      "resource": "https://www.youtube.com/watch?v=c5qJHr3DnT4",
      "title": "GraphRAG methods to create optimized LLM context windows for Retrieval — Jonathan Larson, Microsoft",
      "author": "Jonathan Larson, Microsoft",
      "last_modified": "2025-06-27T09:48:38Z",
      "analysis_file": "analysis/c5qJHr3DnT4.json"
    },
    {
      "id": "iJVxxxHM_Oc",
      "resource": "https://www.youtube.com/watch?v=iJVxxxHM_Oc",
      "title": "Where RL Will Take Search — Maximilian-David Rumpf, SID.ai",
      "author": "Maximilian-David Rumpf, SID.ai",
      "last_modified": "2026-09-16T16:30:16Z",
      "analysis_file": "analysis/iJVxxxHM_Oc.json"
    },
    {
      "id": "pPvoLjYj_mY",
      "resource": "https://www.youtube.com/watch?v=pPvoLjYj_mY",
      "title": "Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer",
      "author": "Waseem Alshikh, Writer",
      "last_modified": "2025-04-22T16:00:06Z",
      "analysis_file": "analysis/pPvoLjYj_mY.json"
    },
    {
      "id": "rgjF5o2Qjsc",
      "resource": "https://www.youtube.com/watch?v=rgjF5o2Qjsc",
      "title": "The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo",
      "author": "Itamar Friedman, Qodo",
      "last_modified": "2025-12-11T21:58:59Z",
      "analysis_file": "analysis/rgjF5o2Qjsc.json"
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

# Measure retrieval coverage, relevance, grounding and cost on real file-finding tasks

## What

A retrieval change can be valuable by reducing search calls at similar quality even when accuracy differences fall inside run variance.

## Evidence

> that 90.2% accuracy. You reach it with 20% fewer tool calls. And that's huge
> — 10:38 [^O84lhGc1OOI]

Source analysis [^RGSFUqzqErE]; no independently matched timestamped quote published.

Source analysis [^c5qJHr3DnT4]; no independently matched timestamped quote published.

Source analysis [^iJVxxxHM_Oc]; no independently matched timestamped quote published.

Source analysis [^pPvoLjYj_mY]; no independently matched timestamped quote published.

> necessarily need to include only your code. It could also include context to
> — 15:33 [^rgjF5o2Qjsc]

> factfulness in general which relates to the reality Beyond just the reference
> — 04:37 [^y2Drx0SDZLo]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^O84lhGc1OOI]: [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](https://www.youtube.com/watch?v=O84lhGc1OOI); publication: 2026-09-16T15:00:39Z; analysis: `analysis/O84lhGc1OOI.json`.
[^RGSFUqzqErE]: [On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft](https://www.youtube.com/watch?v=RGSFUqzqErE); publication: 2026-07-17T16:30:06Z; analysis: `analysis/RGSFUqzqErE.json`.
[^c5qJHr3DnT4]: [GraphRAG methods to create optimized LLM context windows for Retrieval — Jonathan Larson, Microsoft](https://www.youtube.com/watch?v=c5qJHr3DnT4); publication: 2025-06-27T09:48:38Z; analysis: `analysis/c5qJHr3DnT4.json`.
[^iJVxxxHM_Oc]: [Where RL Will Take Search — Maximilian-David Rumpf, SID.ai](https://www.youtube.com/watch?v=iJVxxxHM_Oc); publication: 2026-09-16T16:30:16Z; analysis: `analysis/iJVxxxHM_Oc.json`.
[^pPvoLjYj_mY]: [Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer](https://www.youtube.com/watch?v=pPvoLjYj_mY); publication: 2025-04-22T16:00:06Z; analysis: `analysis/pPvoLjYj_mY.json`.
[^rgjF5o2Qjsc]: [The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo](https://www.youtube.com/watch?v=rgjF5o2Qjsc); publication: 2025-12-11T21:58:59Z; analysis: `analysis/rgjF5o2Qjsc.json`.
[^y2Drx0SDZLo]: [Agent Evals: Finally, With The Map](https://www.youtube.com/watch?v=y2Drx0SDZLo); publication: 2025-02-22T19:00:31Z; analysis: `analysis/y2Drx0SDZLo.json`.
