---
{
  "type": "technique",
  "id": "retrieval-before-reasoning",
  "title": "Acquire decisive source evidence before spending additional reasoning effort",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-06-26T14:00:07Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "LU9KgcZDRfY",
      "resource": "https://www.youtube.com/watch?v=LU9KgcZDRfY",
      "title": "Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual",
      "author": "Asaf Bord, Northwestern Mutual",
      "last_modified": "2025-12-23T17:45:00Z",
      "analysis_file": "analysis/LU9KgcZDRfY.json"
    },
    {
      "id": "Lue8K2jqfKk",
      "resource": "https://www.youtube.com/watch?v=Lue8K2jqfKk",
      "title": "Claude Code & the evolution of agentic coding — Boris Cherny, Anthropic",
      "author": "Boris Cherny, Anthropic",
      "last_modified": "2025-07-04T16:00:06Z",
      "analysis_file": "analysis/Lue8K2jqfKk.json"
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
      "id": "ZRM_TfEZcIo",
      "resource": "https://www.youtube.com/watch?v=ZRM_TfEZcIo",
      "title": "Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "author": "Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "last_modified": "2026-06-26T14:00:07Z",
      "analysis_file": "analysis/ZRM_TfEZcIo.json"
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

# Acquire decisive source evidence before spending additional reasoning effort

## What

Acquire decisive source evidence before spending additional reasoning effort

Reusing prior notes and project research prevents re-deriving decisions and repeating work already done by another session.

## Evidence

Source analysis [^LU9KgcZDRfY]; no independently matched timestamped quote published.

Source analysis [^Lue8K2jqfKk]; no independently matched timestamped quote published.

> you'd insert it between the gathering context and taking action step, right?
> — 24:41 [^TqC1qOfiVcQ]

Source analysis [^ZRM_TfEZcIo]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^LU9KgcZDRfY]: [Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual](https://www.youtube.com/watch?v=LU9KgcZDRfY); publication: 2025-12-23T17:45:00Z; analysis: `analysis/LU9KgcZDRfY.json`.
[^Lue8K2jqfKk]: [Claude Code & the evolution of agentic coding — Boris Cherny, Anthropic](https://www.youtube.com/watch?v=Lue8K2jqfKk); publication: 2025-07-04T16:00:06Z; analysis: `analysis/Lue8K2jqfKk.json`.
[^TqC1qOfiVcQ]: [Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ); publication: 2026-01-05T17:00:06Z; analysis: `analysis/TqC1qOfiVcQ.json`.
[^ZRM_TfEZcIo]: [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo); publication: 2026-06-26T14:00:07Z; analysis: `analysis/ZRM_TfEZcIo.json`.
