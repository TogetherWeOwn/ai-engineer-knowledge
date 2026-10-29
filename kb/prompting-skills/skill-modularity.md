---
{
  "type": "technique",
  "id": "skill-modularity",
  "title": "Give each skill one coherent capability with linked references and scripts",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-10-08T20:00:21Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "XPj3mIKEtI4",
      "resource": "https://www.youtube.com/watch?v=XPj3mIKEtI4",
      "title": "Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j",
      "author": "Will Lyon, Neo4j",
      "last_modified": "2026-10-08T20:00:21Z",
      "analysis_file": "analysis/XPj3mIKEtI4.json"
    },
    {
      "id": "eBUyTS7SzV4",
      "resource": "https://www.youtube.com/watch?v=eBUyTS7SzV4",
      "title": "Every company should have a Brain — Garry Tan, Y Combinator",
      "author": "Garry Tan, Y Combinator",
      "last_modified": "2026-07-17T01:00:06Z",
      "analysis_file": "analysis/eBUyTS7SzV4.json"
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

# Give each skill one coherent capability with linked references and scripts

## What

Give each skill one coherent capability with linked references and scripts

Small, versioned procedures make ownership and expected behavior explicit rather than hiding a whole role inside an omnibus prompt.

## Evidence

> graph algorithms like community detection, right? So, if we're mixing uh
> — 14:24 [^XPj3mIKEtI4]

> It has one capability, one job, written down clearly enough that someone can
> — 04:35 [^eBUyTS7SzV4]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^XPj3mIKEtI4]: [Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j](https://www.youtube.com/watch?v=XPj3mIKEtI4); publication: 2026-10-08T20:00:21Z; analysis: `analysis/XPj3mIKEtI4.json`.
[^eBUyTS7SzV4]: [Every company should have a Brain — Garry Tan, Y Combinator](https://www.youtube.com/watch?v=eBUyTS7SzV4); publication: 2026-07-17T01:00:06Z; analysis: `analysis/eBUyTS7SzV4.json`.
