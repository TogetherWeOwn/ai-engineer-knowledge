---
{
  "type": "technique",
  "id": "domain-vocabulary",
  "title": "Provide a shared domain vocabulary and business ontology as authoritative context",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-09-18T16:00:11Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1nOTQsfe1RU",
      "resource": "https://www.youtube.com/watch?v=1nOTQsfe1RU",
      "title": "\"Data readiness\" is a Myth: Reliable AI with an Agentic Semantic Layer — Anushrut Gupta, PromptQL",
      "author": "Anushrut Gupta, PromptQL",
      "last_modified": "2025-06-27T09:40:39Z",
      "analysis_file": "analysis/1nOTQsfe1RU.json"
    },
    {
      "id": "ITMXwI6QL6A",
      "resource": "https://www.youtube.com/watch?v=ITMXwI6QL6A",
      "title": "How Forward Deployed Engineering is done at Ramp — Leo Mehr",
      "author": "Leo Mehr",
      "last_modified": "2026-07-28T19:00:06Z",
      "analysis_file": "analysis/ITMXwI6QL6A.json"
    },
    {
      "id": "VGN22pPpb-8",
      "resource": "https://www.youtube.com/watch?v=VGN22pPpb-8",
      "title": "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j",
      "author": "Emil Eifrem, Neo4j",
      "last_modified": "2026-07-22T17:00:38Z",
      "analysis_file": "analysis/VGN22pPpb-8.json"
    },
    {
      "id": "cZ5ZJy19KMo",
      "resource": "https://www.youtube.com/watch?v=cZ5ZJy19KMo",
      "title": "Mission-Critical Evals at Scale (Learnings from 100k medical decisions)",
      "author": null,
      "last_modified": "2025-02-22T19:00:06Z",
      "analysis_file": "analysis/cZ5ZJy19KMo.json"
    },
    {
      "id": "v42opQpCy60",
      "resource": "https://www.youtube.com/watch?v=v42opQpCy60",
      "title": "Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.",
      "author": "Paul Bakaus, Renaissance Geek, Inc.",
      "last_modified": "2026-09-10T15:30:14Z",
      "analysis_file": "analysis/v42opQpCy60.json"
    },
    {
      "id": "v4F1gFy-hqg",
      "resource": "https://www.youtube.com/watch?v=v4F1gFy-hqg",
      "title": "\"Software Fundamentals Matter More Than Ever\" — Matt Pocock",
      "author": "Matt Pocock",
      "last_modified": "2026-04-23T15:15:06Z",
      "analysis_file": "analysis/v4F1gFy-hqg.json"
    },
    {
      "id": "xs-ob87TTzg",
      "resource": "https://www.youtube.com/watch?v=xs-ob87TTzg",
      "title": "Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle",
      "author": "Ignacio Martinez, Oracle",
      "last_modified": "2026-09-18T16:00:11Z",
      "analysis_file": "analysis/xs-ob87TTzg.json"
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

# Provide a shared domain vocabulary and business ontology as authoritative context

## What

Provide a shared domain vocabulary and business ontology as authoritative context

Keep domain terms aligned across conversations, planning, code and module names to reduce translation ambiguity.

## Evidence

Source analysis [^1nOTQsfe1RU]; no independently matched timestamped quote published.

Source analysis [^ITMXwI6QL6A]; no independently matched timestamped quote published.

Source analysis [^VGN22pPpb-8]; no independently matched timestamped quote published.

> and therefore this is not just suspicious it's confirmed which means
> — 01:48 [^cZ5ZJy19KMo]

Source analysis [^v42opQpCy60]; no independently matched timestamped quote published.

> a list of terms that you and the AI have in common. And you really focus on those
> — 08:41 [^v4F1gFy-hqg]

> knowledge that that an an enterprise has, right? Institutional knowledge as
> — 36:23 [^xs-ob87TTzg]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1nOTQsfe1RU]: ["Data readiness" is a Myth: Reliable AI with an Agentic Semantic Layer — Anushrut Gupta, PromptQL](https://www.youtube.com/watch?v=1nOTQsfe1RU); publication: 2025-06-27T09:40:39Z; analysis: `analysis/1nOTQsfe1RU.json`.
[^ITMXwI6QL6A]: [How Forward Deployed Engineering is done at Ramp — Leo Mehr](https://www.youtube.com/watch?v=ITMXwI6QL6A); publication: 2026-07-28T19:00:06Z; analysis: `analysis/ITMXwI6QL6A.json`.
[^VGN22pPpb-8]: [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j](https://www.youtube.com/watch?v=VGN22pPpb-8); publication: 2026-07-22T17:00:38Z; analysis: `analysis/VGN22pPpb-8.json`.
[^cZ5ZJy19KMo]: [Mission-Critical Evals at Scale (Learnings from 100k medical decisions)](https://www.youtube.com/watch?v=cZ5ZJy19KMo); publication: 2025-02-22T19:00:06Z; analysis: `analysis/cZ5ZJy19KMo.json`.
[^v42opQpCy60]: [Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.](https://www.youtube.com/watch?v=v42opQpCy60); publication: 2026-09-10T15:30:14Z; analysis: `analysis/v42opQpCy60.json`.
[^v4F1gFy-hqg]: ["Software Fundamentals Matter More Than Ever" — Matt Pocock](https://www.youtube.com/watch?v=v4F1gFy-hqg); publication: 2026-04-23T15:15:06Z; analysis: `analysis/v4F1gFy-hqg.json`.
[^xs-ob87TTzg]: [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](https://www.youtube.com/watch?v=xs-ob87TTzg); publication: 2026-09-18T16:00:11Z; analysis: `analysis/xs-ob87TTzg.json`.
