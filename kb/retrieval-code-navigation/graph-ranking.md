---
{
  "type": "technique",
  "id": "graph-ranking",
  "title": "Use bounded graph expansion and relationship ranking for genuinely multi-hop questions",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-07-23T07:00:23Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "3ySF0I5iE_0",
      "resource": "https://www.youtube.com/watch?v=3ySF0I5iE_0",
      "title": "A Practitioner's Guide to Graphs - Tim Ainge, Good Collective",
      "author": "Tim Ainge, Good Collective",
      "last_modified": "2026-07-18T21:30:06Z",
      "analysis_file": "analysis/3ySF0I5iE_0.json"
    },
    {
      "id": "GGxAQVbwBL4",
      "resource": "https://www.youtube.com/watch?v=GGxAQVbwBL4",
      "title": "Graph Intelligence: Enhance Reasoning and Retrieval Using Graph Analytics - Alison & Andreas, Neo4j",
      "author": "Alison & Andreas, Neo4j",
      "last_modified": "2025-06-27T09:49:33Z",
      "analysis_file": "analysis/GGxAQVbwBL4.json"
    },
    {
      "id": "LLuKshphGOE",
      "resource": "https://www.youtube.com/watch?v=LLuKshphGOE",
      "title": "Context Engineering: Connecting the Dots with Graphs — Stephen Chin, Neo4j",
      "author": "Stephen Chin, Neo4j",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/LLuKshphGOE.json"
    },
    {
      "id": "_zl_zimMRak",
      "resource": "https://www.youtube.com/watch?v=_zl_zimMRak",
      "title": "How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit",
      "author": "Jaspreet Singh, Intuit",
      "last_modified": "2025-07-23T15:51:31Z",
      "analysis_file": "analysis/_zl_zimMRak.json"
    },
    {
      "id": "kRkcNOsRyYg",
      "resource": "https://www.youtube.com/watch?v=kRkcNOsRyYg",
      "title": "AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j",
      "author": "Zach Blumenfeld, Neo4j",
      "last_modified": "2026-07-23T07:00:23Z",
      "analysis_file": "analysis/kRkcNOsRyYg.json"
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

# Use bounded graph expansion and relationship ranking for genuinely multi-hop questions

## What

Use bounded graph expansion and relationship ranking for genuinely multi-hop questions

Run personalized PageRank from a seed node to surface the nodes most strongly related to it in a dense graph, used for recommendations and for finding authoritative related cases.

## Evidence

Source analysis [^3ySF0I5iE_0]; no independently matched timestamped quote published.

Source analysis [^GGxAQVbwBL4]; no independently matched timestamped quote published.

Source analysis [^LLuKshphGOE]; no independently matched timestamped quote published.

Source analysis [^_zl_zimMRak]; no independently matched timestamped quote published.

Source analysis [^kRkcNOsRyYg]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^3ySF0I5iE_0]: [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](https://www.youtube.com/watch?v=3ySF0I5iE_0); publication: 2026-07-18T21:30:06Z; analysis: `analysis/3ySF0I5iE_0.json`.
[^GGxAQVbwBL4]: [Graph Intelligence: Enhance Reasoning and Retrieval Using Graph Analytics - Alison & Andreas, Neo4j](https://www.youtube.com/watch?v=GGxAQVbwBL4); publication: 2025-06-27T09:49:33Z; analysis: `analysis/GGxAQVbwBL4.json`.
[^LLuKshphGOE]: [Context Engineering: Connecting the Dots with Graphs — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=LLuKshphGOE); publication: 2025-11-24T20:16:36Z; analysis: `analysis/LLuKshphGOE.json`.
[^_zl_zimMRak]: [How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit](https://www.youtube.com/watch?v=_zl_zimMRak); publication: 2025-07-23T15:51:31Z; analysis: `analysis/_zl_zimMRak.json`.
[^kRkcNOsRyYg]: [AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j](https://www.youtube.com/watch?v=kRkcNOsRyYg); publication: 2026-07-23T07:00:23Z; analysis: `analysis/kRkcNOsRyYg.json`.
