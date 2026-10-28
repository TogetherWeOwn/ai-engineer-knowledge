---
{
  "type": "technique",
  "id": "validated-metadata-extraction",
  "title": "Extract reusable search metadata offline and validate tags before treating them as facts",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-08-18T15:00:29Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "VBCDhRrvlYo",
      "resource": "https://www.youtube.com/watch?v=VBCDhRrvlYo",
      "title": "The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu",
      "author": "Arturo Nunez, Nereu",
      "last_modified": "2026-08-18T15:00:29Z",
      "analysis_file": "analysis/VBCDhRrvlYo.json"
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

# Extract reusable search metadata offline and validate tags before treating them as facts

## What

Extract reusable search metadata offline and validate tags before treating them as facts

Instead of hand-labeling 6-7k 3D assets, they screenshot each and run a vision model to produce descriptions used for retrieval.

## Evidence

Source analysis [^VBCDhRrvlYo]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^VBCDhRrvlYo]: [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](https://www.youtube.com/watch?v=VBCDhRrvlYo); publication: 2026-08-18T15:00:29Z; analysis: `analysis/VBCDhRrvlYo.json`.
