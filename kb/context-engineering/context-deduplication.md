---
{
  "type": "technique",
  "id": "context-deduplication",
  "title": "Deduplicate repeated evidence while preserving distinct sources and lineage",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-07-23T04:00:02Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "GGxAQVbwBL4",
      "resource": "https://www.youtube.com/watch?v=GGxAQVbwBL4",
      "title": "Graph Intelligence: Enhance Reasoning and Retrieval Using Graph Analytics - Alison & Andreas, Neo4j",
      "author": "Alison & Andreas, Neo4j",
      "last_modified": "2025-06-27T09:49:33Z",
      "analysis_file": "analysis/GGxAQVbwBL4.json"
    },
    {
      "id": "H7puB0RwJMM",
      "resource": "https://www.youtube.com/watch?v=H7puB0RwJMM",
      "title": "Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI",
      "author": "Daniel Chalef, Zep AI",
      "last_modified": "2026-07-23T04:00:02Z",
      "analysis_file": "analysis/H7puB0RwJMM.json"
    },
    {
      "id": "kDlqpN1JyIw",
      "resource": "https://www.youtube.com/watch?v=kDlqpN1JyIw",
      "title": "Vercel AI SDK Masterclass: From Fundamentals to Deep Research",
      "author": null,
      "last_modified": "2025-04-20T21:39:01Z",
      "analysis_file": "analysis/kDlqpN1JyIw.json"
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

# Deduplicate repeated evidence while preserving distinct sources and lineage

## What

Deduplicate repeated evidence while preserving distinct sources and lineage

They pass previously used URLs into the evaluator and mark repeats irrelevant, so the same large page is never re-injected.

## Evidence

Source analysis [^GGxAQVbwBL4]; no independently matched timestamped quote published.

Source analysis [^H7puB0RwJMM]; no independently matched timestamped quote published.

Source analysis [^kDlqpN1JyIw]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^GGxAQVbwBL4]: [Graph Intelligence: Enhance Reasoning and Retrieval Using Graph Analytics - Alison & Andreas, Neo4j](https://www.youtube.com/watch?v=GGxAQVbwBL4); publication: 2025-06-27T09:49:33Z; analysis: `analysis/GGxAQVbwBL4.json`.
[^H7puB0RwJMM]: [Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI](https://www.youtube.com/watch?v=H7puB0RwJMM); publication: 2026-07-23T04:00:02Z; analysis: `analysis/H7puB0RwJMM.json`.
[^kDlqpN1JyIw]: [Vercel AI SDK Masterclass: From Fundamentals to Deep Research](https://www.youtube.com/watch?v=kDlqpN1JyIw); publication: 2025-04-20T21:39:01Z; analysis: `analysis/kDlqpN1JyIw.json`.
