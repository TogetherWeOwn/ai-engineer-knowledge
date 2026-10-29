---
{
  "type": "technique",
  "id": "entity-resolution",
  "title": "Resolve entity identity before creating duplicate graph or memory nodes",
  "area": "memory-learning",
  "status": "stable",
  "valid_from": "2026-10-11T10:00:18Z",
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
      "id": "Q0VkgCyNVUg",
      "resource": "https://www.youtube.com/watch?v=Q0VkgCyNVUg",
      "title": "CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j",
      "author": "Stephen Chin, Neo4j",
      "last_modified": "2026-07-22T18:30:02Z",
      "analysis_file": "analysis/Q0VkgCyNVUg.json"
    },
    {
      "id": "XPj3mIKEtI4",
      "resource": "https://www.youtube.com/watch?v=XPj3mIKEtI4",
      "title": "Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j",
      "author": "Will Lyon, Neo4j",
      "last_modified": "2026-10-08T20:00:21Z",
      "analysis_file": "analysis/XPj3mIKEtI4.json"
    },
    {
      "id": "spxoDAfh5ig",
      "resource": "https://www.youtube.com/watch?v=spxoDAfh5ig",
      "title": "Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked",
      "author": "Peter Werry, Unblocked",
      "last_modified": "2026-10-11T10:00:18Z",
      "analysis_file": "analysis/spxoDAfh5ig.json"
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

# Resolve entity identity before creating duplicate graph or memory nodes

## What

Resolve entity identity before creating duplicate graph or memory nodes

Unify alternate names for the same thing before retrieval and reuse, avoiding conflicting or duplicated knowledge.

## Evidence

Source analysis [^3ySF0I5iE_0]; no independently matched timestamped quote published.

Source analysis [^GGxAQVbwBL4]; no independently matched timestamped quote published.

> similarity in vector space, is not the same as actual relationships.
> — 08:31 [^Q0VkgCyNVUg]

> canonical representation of the thing, right? So really agents need knowledge
> — 01:50 [^XPj3mIKEtI4]

Source analysis [^spxoDAfh5ig]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated investigation
- **Speed:** Faster reuse of relevant prior work
- **Quality:** More current, scoped lessons
- **Reliability:** Less stale, conflicting or unsupported recall
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^3ySF0I5iE_0]: [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](https://www.youtube.com/watch?v=3ySF0I5iE_0); publication: 2026-07-18T21:30:06Z; analysis: `analysis/3ySF0I5iE_0.json`.
[^GGxAQVbwBL4]: [Graph Intelligence: Enhance Reasoning and Retrieval Using Graph Analytics - Alison & Andreas, Neo4j](https://www.youtube.com/watch?v=GGxAQVbwBL4); publication: 2025-06-27T09:49:33Z; analysis: `analysis/GGxAQVbwBL4.json`.
[^Q0VkgCyNVUg]: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=Q0VkgCyNVUg); publication: 2026-07-22T18:30:02Z; analysis: `analysis/Q0VkgCyNVUg.json`.
[^XPj3mIKEtI4]: [Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j](https://www.youtube.com/watch?v=XPj3mIKEtI4); publication: 2026-10-08T20:00:21Z; analysis: `analysis/XPj3mIKEtI4.json`.
[^spxoDAfh5ig]: [Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked](https://www.youtube.com/watch?v=spxoDAfh5ig); publication: 2026-10-11T10:00:18Z; analysis: `analysis/spxoDAfh5ig.json`.
