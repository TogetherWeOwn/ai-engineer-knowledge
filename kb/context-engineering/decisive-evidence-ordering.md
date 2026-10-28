---
{
  "type": "technique",
  "id": "decisive-evidence-ordering",
  "title": "Rank decisive evidence first while retaining accessible full provenance",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2023-11-02T13:08:20Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "LzeC1AQ-U5o",
      "resource": "https://www.youtube.com/watch?v=LzeC1AQ-U5o",
      "title": "Building Blocks for LLM Systems & Products: Eugene Yan",
      "author": null,
      "last_modified": "2023-11-02T13:08:20Z",
      "analysis_file": "analysis/LzeC1AQ-U5o.json"
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

# Rank decisive evidence first while retaining accessible full provenance

## What

Rank decisive evidence first while retaining accessible full provenance

Position affects use of retrieved evidence; keep high-relevance material prominent instead of assuming a larger window compensates for low-quality ranking.

## Evidence

> worse right right getting the most relevant documents to rank highly still
> — 07:28 [^LzeC1AQ-U5o]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^LzeC1AQ-U5o]: [Building Blocks for LLM Systems & Products: Eugene Yan](https://www.youtube.com/watch?v=LzeC1AQ-U5o); publication: 2023-11-02T13:08:20Z; analysis: `analysis/LzeC1AQ-U5o.json`.
