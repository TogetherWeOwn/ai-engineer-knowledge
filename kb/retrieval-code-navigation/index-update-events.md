---
{
  "type": "technique",
  "id": "index-update-events",
  "title": "Update indexes incrementally from versioned source changes rather than rebuilding per session",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-09-16T13:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "4Xe_iMYxBQc",
      "resource": "https://www.youtube.com/watch?v=4Xe_iMYxBQc",
      "title": "Information Retrieval from the Ground Up - Philipp Krenn, Elastic",
      "author": "Philipp Krenn, Elastic",
      "last_modified": "2025-07-27T05:08:44Z",
      "analysis_file": "analysis/4Xe_iMYxBQc.json"
    },
    {
      "id": "IN-rb-9WmiY",
      "resource": "https://www.youtube.com/watch?v=IN-rb-9WmiY",
      "title": "Pinecone 2.0 — Edo Liberty, Pinecone",
      "author": "Edo Liberty, Pinecone",
      "last_modified": "2026-09-16T13:00:06Z",
      "analysis_file": "analysis/IN-rb-9WmiY.json"
    },
    {
      "id": "TqC1qOfiVcQ",
      "resource": "https://www.youtube.com/watch?v=TqC1qOfiVcQ",
      "title": "Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic",
      "author": "Thariq Shihipar, Anthropic",
      "last_modified": "2026-01-05T17:00:06Z",
      "analysis_file": "analysis/TqC1qOfiVcQ.json"
    },
    {
      "id": "pijYURicI1Y",
      "resource": "https://www.youtube.com/watch?v=pijYURicI1Y",
      "title": "Building efficient hybrid context query for LLM grounding: Simrat Hanspal",
      "author": null,
      "last_modified": "2025-02-05T11:18:34Z",
      "analysis_file": "analysis/pijYURicI1Y.json"
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

# Update indexes incrementally from versioned source changes rather than rebuilding per session

## What

Update indexes incrementally from versioned source changes rather than rebuilding per session

Headers, index hints and annotations give a small starting context; scratchpads preserve references while the agent retrieves needed regions.

## Evidence

Source analysis [^4Xe_iMYxBQc]; no independently matched timestamped quote published.

> I need to go update these tables these relationships my graph uh this uh these
> — 12:47 [^IN-rb-9WmiY]

Source analysis [^TqC1qOfiVcQ]; no independently matched timestamped quote published.

Source analysis [^pijYURicI1Y]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^4Xe_iMYxBQc]: [Information Retrieval from the Ground Up - Philipp Krenn, Elastic](https://www.youtube.com/watch?v=4Xe_iMYxBQc); publication: 2025-07-27T05:08:44Z; analysis: `analysis/4Xe_iMYxBQc.json`.
[^IN-rb-9WmiY]: [Pinecone 2.0 — Edo Liberty, Pinecone](https://www.youtube.com/watch?v=IN-rb-9WmiY); publication: 2026-09-16T13:00:06Z; analysis: `analysis/IN-rb-9WmiY.json`.
[^TqC1qOfiVcQ]: [Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ); publication: 2026-01-05T17:00:06Z; analysis: `analysis/TqC1qOfiVcQ.json`.
[^pijYURicI1Y]: [Building efficient hybrid context query for LLM grounding: Simrat Hanspal](https://www.youtube.com/watch?v=pijYURicI1Y); publication: 2025-02-05T11:18:34Z; analysis: `analysis/pijYURicI1Y.json`.
