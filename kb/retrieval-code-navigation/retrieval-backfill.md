---
{
  "type": "technique",
  "id": "retrieval-backfill",
  "title": "Use explicit history windows with deterministic backfill when a query needs older evidence",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2025-06-22T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "sn79oS4MZFI",
      "resource": "https://www.youtube.com/watch?v=sn79oS4MZFI",
      "title": "Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason",
      "author": "Dan Mason",
      "last_modified": "2025-06-22T16:00:06Z",
      "analysis_file": "analysis/sn79oS4MZFI.json"
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

# Use explicit history windows with deterministic backfill when a query needs older evidence

## What

Use explicit history windows with deterministic backfill when a query needs older evidence

Keep recent external messages plus state, with a tool to retrieve earlier history when needed.

## Evidence

> optionally set it to compress and say, well, just show me the last 50, right?
> — 50:28 [^sn79oS4MZFI]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^sn79oS4MZFI]: [Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason](https://www.youtube.com/watch?v=sn79oS4MZFI); publication: 2025-06-22T16:00:06Z; analysis: `analysis/sn79oS4MZFI.json`.
