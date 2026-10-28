---
{
  "type": "technique",
  "id": "modality-preserving-retrieval",
  "title": "Preserve layout and non-text evidence when plain text retrieval is insufficient",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-09-16T15:00:39Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1P1hJ36rxM0",
      "resource": "https://www.youtube.com/watch?v=1P1hJ36rxM0",
      "title": "\"Software engineering is not about writing code\" — Benoit Schillings, Google DeepMind VP of Research",
      "author": "Benoit Schillings, Google DeepMind VP of Research",
      "last_modified": "2026-07-17T15:24:44Z",
      "analysis_file": "analysis/1P1hJ36rxM0.json"
    },
    {
      "id": "7GMKdpLsxwU",
      "resource": "https://www.youtube.com/watch?v=7GMKdpLsxwU",
      "title": "The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI",
      "author": "Hassan El Mghari, Together AI",
      "last_modified": "2026-08-21T15:00:06Z",
      "analysis_file": "analysis/7GMKdpLsxwU.json"
    },
    {
      "id": "O84lhGc1OOI",
      "resource": "https://www.youtube.com/watch?v=O84lhGc1OOI",
      "title": "If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread",
      "author": "Benjamin Clavié, Mixedbread",
      "last_modified": "2026-09-16T15:00:39Z",
      "analysis_file": "analysis/O84lhGc1OOI.json"
    },
    {
      "id": "ZIYYsAzaLlA",
      "resource": "https://www.youtube.com/watch?v=ZIYYsAzaLlA",
      "title": "Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma",
      "author": "Jesse Lumarie, Figma",
      "last_modified": "2026-08-28T14:00:06Z",
      "analysis_file": "analysis/ZIYYsAzaLlA.json"
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

# Preserve layout and non-text evidence when plain text retrieval is insufficient

## What

Preserve layout and non-text evidence when plain text retrieval is insufficient

OCR-only lexical retrieval can omit PDF tables and visual relationships; layout/vision-aware retrieval can recover evidence unavailable in plain text.

## Evidence

Source analysis [^1P1hJ36rxM0]; no independently matched timestamped quote published.

Source analysis [^7GMKdpLsxwU]; no independently matched timestamped quote published.

> multimodel. So, it can read the PDF, you get the tables, you get all that nice
> — 13:43 [^O84lhGc1OOI]

Source analysis [^ZIYYsAzaLlA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1P1hJ36rxM0]: ["Software engineering is not about writing code" — Benoit Schillings, Google DeepMind VP of Research](https://www.youtube.com/watch?v=1P1hJ36rxM0); publication: 2026-07-17T15:24:44Z; analysis: `analysis/1P1hJ36rxM0.json`.
[^7GMKdpLsxwU]: [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](https://www.youtube.com/watch?v=7GMKdpLsxwU); publication: 2026-08-21T15:00:06Z; analysis: `analysis/7GMKdpLsxwU.json`.
[^O84lhGc1OOI]: [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](https://www.youtube.com/watch?v=O84lhGc1OOI); publication: 2026-09-16T15:00:39Z; analysis: `analysis/O84lhGc1OOI.json`.
[^ZIYYsAzaLlA]: [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](https://www.youtube.com/watch?v=ZIYYsAzaLlA); publication: 2026-08-28T14:00:06Z; analysis: `analysis/ZIYYsAzaLlA.json`.
