---
{
  "type": "technique",
  "id": "service-exposure-risk",
  "title": "Compute security exposure from actual service, data and network relationships",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-07-22T18:30:02Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Q0VkgCyNVUg",
      "resource": "https://www.youtube.com/watch?v=Q0VkgCyNVUg",
      "title": "CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j",
      "author": "Stephen Chin, Neo4j",
      "last_modified": "2026-07-22T18:30:02Z",
      "analysis_file": "analysis/Q0VkgCyNVUg.json"
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

# Compute security exposure from actual service, data and network relationships

## What

Compute security exposure from actual service, data and network relationships

Join service versions, listener configuration, firewall/routing exposure and ownership to identify reachable obsolete services and management ports; these are multi-hop inventory questions rather than prose similarity questions.

## Evidence

Source analysis [^Q0VkgCyNVUg]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Q0VkgCyNVUg]: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=Q0VkgCyNVUg); publication: 2026-07-22T18:30:02Z; analysis: `analysis/Q0VkgCyNVUg.json`.
