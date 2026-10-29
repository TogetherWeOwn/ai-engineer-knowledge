---
{
  "type": "technique",
  "id": "skills-source-generation",
  "title": "Generate reusable skills from authoritative source procedures and verify their contracts",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-07-18T16:15:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "RGiXcVxSD3s",
      "resource": "https://www.youtube.com/watch?v=RGiXcVxSD3s",
      "title": "Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc",
      "author": "Atul Ramachandran, Filed Inc",
      "last_modified": "2026-07-11T17:30:06Z",
      "analysis_file": "analysis/RGiXcVxSD3s.json"
    },
    {
      "id": "am_oeAoUhew",
      "resource": "https://www.youtube.com/watch?v=am_oeAoUhew",
      "title": "Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI",
      "author": "Ryan Lopopolo, OpenAI",
      "last_modified": "2026-04-17T00:29:28Z",
      "analysis_file": "analysis/am_oeAoUhew.json"
    },
    {
      "id": "ro5HkZvzfiQ",
      "resource": "https://www.youtube.com/watch?v=ro5HkZvzfiQ",
      "title": "The LLM Triangle: Engineering Principles for Robust AI Applications - Almog Baku:",
      "author": "Almog Baku:",
      "last_modified": "2025-02-22T15:00:06Z",
      "analysis_file": "analysis/ro5HkZvzfiQ.json"
    },
    {
      "id": "yv6xovSsB1U",
      "resource": "https://www.youtube.com/watch?v=yv6xovSsB1U",
      "title": "Content Is Code - Matt Palmer, Conductor",
      "author": "Matt Palmer, Conductor",
      "last_modified": "2026-07-18T16:15:06Z",
      "analysis_file": "analysis/yv6xovSsB1U.json"
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

# Generate reusable skills from authoritative source procedures and verify their contracts

## What

Generate reusable skills from authoritative source procedures and verify their contracts

Interview an operator and play the proposed procedure back to expose omitted reasoning steps.

## Evidence

Source analysis [^RGiXcVxSD3s]; no independently matched timestamped quote published.

Source analysis [^am_oeAoUhew]; no independently matched timestamped quote published.

> is to find the hidden implicit uh cognition jumps that the
> — 07:54 [^ro5HkZvzfiQ]

Source analysis [^yv6xovSsB1U]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^RGiXcVxSD3s]: [Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc](https://www.youtube.com/watch?v=RGiXcVxSD3s); publication: 2026-07-11T17:30:06Z; analysis: `analysis/RGiXcVxSD3s.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
[^ro5HkZvzfiQ]: [The LLM Triangle: Engineering Principles for Robust AI Applications - Almog Baku:](https://www.youtube.com/watch?v=ro5HkZvzfiQ); publication: 2025-02-22T15:00:06Z; analysis: `analysis/ro5HkZvzfiQ.json`.
[^yv6xovSsB1U]: [Content Is Code - Matt Palmer, Conductor](https://www.youtube.com/watch?v=yv6xovSsB1U); publication: 2026-07-18T16:15:06Z; analysis: `analysis/yv6xovSsB1U.json`.
