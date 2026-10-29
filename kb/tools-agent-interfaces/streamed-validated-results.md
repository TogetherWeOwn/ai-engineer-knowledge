---
{
  "type": "technique",
  "id": "streamed-validated-results",
  "title": "Stream completed validated objects while treating incomplete chunks as provisional",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2025-06-27T09:38:08Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "WXy8Yy9xGss",
      "resource": "https://www.youtube.com/watch?v=WXy8Yy9xGss",
      "title": "CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed",
      "author": "Nathan Sobo, Zed",
      "last_modified": "2025-06-27T09:22:37Z",
      "analysis_file": "analysis/WXy8Yy9xGss.json"
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
      "id": "vRFqbEzzDsI",
      "resource": "https://www.youtube.com/watch?v=vRFqbEzzDsI",
      "title": "Building Agentic Applications w/ Heroku Managed Inference and Agents — Julián Duque & Anush Dsouza",
      "author": "Julián Duque & Anush Dsouza",
      "last_modified": "2025-06-27T09:38:08Z",
      "analysis_file": "analysis/vRFqbEzzDsI.json"
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

# Stream completed validated objects while treating incomplete chunks as provisional

## What

Stream completed validated objects while treating incomplete chunks as provisional

Iterable outputs expose completed objects early; partial structured output enables rendering without bespoke JSON-stack parsing.

## Evidence

> old text, is that because it was deleted or it just hasn't been streamed out yet?
> — 07:54 [^WXy8Yy9xGss]

> want to extract two objects and as long as you set stream equals true you're
> — 03:37 [^pZ4DIH2BVqg]

Source analysis [^vRFqbEzzDsI]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^WXy8Yy9xGss]: [CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed](https://www.youtube.com/watch?v=WXy8Yy9xGss); publication: 2025-06-27T09:22:37Z; analysis: `analysis/WXy8Yy9xGss.json`.
[^pZ4DIH2BVqg]: [Pydantic is STILL all you need: Jason Liu](https://www.youtube.com/watch?v=pZ4DIH2BVqg); publication: 2024-09-06T17:07:06Z; analysis: `analysis/pZ4DIH2BVqg.json`.
[^vRFqbEzzDsI]: [Building Agentic Applications w/ Heroku Managed Inference and Agents — Julián Duque & Anush Dsouza](https://www.youtube.com/watch?v=vRFqbEzzDsI); publication: 2025-06-27T09:38:08Z; analysis: `analysis/vRFqbEzzDsI.json`.
