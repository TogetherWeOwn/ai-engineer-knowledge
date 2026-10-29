---
{
  "type": "technique",
  "id": "risk-first-adoption",
  "title": "Start with narrow verifiable high-value work before expanding automation scope",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-07-28T17:00:35Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "7wu2hsRfvV0",
      "resource": "https://www.youtube.com/watch?v=7wu2hsRfvV0",
      "title": "How Forward Deployed Engineering is done at Decagon — Sunny Rekhi",
      "author": "Sunny Rekhi",
      "last_modified": "2026-07-28T17:00:35Z",
      "analysis_file": "analysis/7wu2hsRfvV0.json"
    },
    {
      "id": "C1NivhYS1sI",
      "resource": "https://www.youtube.com/watch?v=C1NivhYS1sI",
      "title": "Unlocking AI Powered DevOps Within Your Organization — Jon Peck, GitHub",
      "author": "Jon Peck, GitHub",
      "last_modified": "2025-06-27T10:17:04Z",
      "analysis_file": "analysis/C1NivhYS1sI.json"
    },
    {
      "id": "GdvKNwMcfd0",
      "resource": "https://www.youtube.com/watch?v=GdvKNwMcfd0",
      "title": "From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft",
      "author": "Chris Noring, Microsoft",
      "last_modified": "2026-07-11T14:00:06Z",
      "analysis_file": "analysis/GdvKNwMcfd0.json"
    },
    {
      "id": "Q81AzlA-VE8",
      "resource": "https://www.youtube.com/watch?v=Q81AzlA-VE8",
      "title": "What We Learned Deploying AI within Bloomberg’s Engineering Organization – Lei Zhang, Bloomberg",
      "author": "Lei Zhang, Bloomberg",
      "last_modified": "2025-12-16T15:00:07Z",
      "analysis_file": "analysis/Q81AzlA-VE8.json"
    },
    {
      "id": "WqZq8L-v9pA",
      "resource": "https://www.youtube.com/watch?v=WqZq8L-v9pA",
      "title": "What Data from 20m Pull Requests Reveal About AI Transformation — Nick Arcolano, Jellyfish",
      "author": "Nick Arcolano, Jellyfish",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/WqZq8L-v9pA.json"
    },
    {
      "id": "pSqpC7fFLZA",
      "resource": "https://www.youtube.com/watch?v=pSqpC7fFLZA",
      "title": "The Robots are coming for your job, and that's okay - Elmer Thomas and Maria Bermudez",
      "author": "Elmer Thomas and Maria Bermudez",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/pSqpC7fFLZA.json"
    },
    {
      "id": "zepu8Kk6FBQ",
      "resource": "https://www.youtube.com/watch?v=zepu8Kk6FBQ",
      "title": "Agents for Everything Else — swyx",
      "author": "swyx",
      "last_modified": "2026-05-01T04:10:33Z",
      "analysis_file": "analysis/zepu8Kk6FBQ.json"
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

# Start with narrow verifiable high-value work before expanding automation scope

## What

Start with narrow verifiable high-value work before expanding automation scope

They choose agent candidates by a rule of thumb: repeatable, high volume, low creativity, leaving judgment and clarity to humans.

## Evidence

Source analysis [^7wu2hsRfvV0]; no independently matched timestamped quote published.

Source analysis [^C1NivhYS1sI]; no independently matched timestamped quote published.

Source analysis [^GdvKNwMcfd0]; no independently matched timestamped quote published.

Source analysis [^Q81AzlA-VE8]; no independently matched timestamped quote published.

Source analysis [^WqZq8L-v9pA]; no independently matched timestamped quote published.

Source analysis [^pSqpC7fFLZA]; no independently matched timestamped quote published.

Source analysis [^zepu8Kk6FBQ]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^7wu2hsRfvV0]: [How Forward Deployed Engineering is done at Decagon — Sunny Rekhi](https://www.youtube.com/watch?v=7wu2hsRfvV0); publication: 2026-07-28T17:00:35Z; analysis: `analysis/7wu2hsRfvV0.json`.
[^C1NivhYS1sI]: [Unlocking AI Powered DevOps Within Your Organization — Jon Peck, GitHub](https://www.youtube.com/watch?v=C1NivhYS1sI); publication: 2025-06-27T10:17:04Z; analysis: `analysis/C1NivhYS1sI.json`.
[^GdvKNwMcfd0]: [From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](https://www.youtube.com/watch?v=GdvKNwMcfd0); publication: 2026-07-11T14:00:06Z; analysis: `analysis/GdvKNwMcfd0.json`.
[^Q81AzlA-VE8]: [What We Learned Deploying AI within Bloomberg’s Engineering Organization – Lei Zhang, Bloomberg](https://www.youtube.com/watch?v=Q81AzlA-VE8); publication: 2025-12-16T15:00:07Z; analysis: `analysis/Q81AzlA-VE8.json`.
[^WqZq8L-v9pA]: [What Data from 20m Pull Requests Reveal About AI Transformation — Nick Arcolano, Jellyfish](https://www.youtube.com/watch?v=WqZq8L-v9pA); publication: 2025-11-24T20:16:36Z; analysis: `analysis/WqZq8L-v9pA.json`.
[^pSqpC7fFLZA]: [The Robots are coming for your job, and that's okay - Elmer Thomas and Maria Bermudez](https://www.youtube.com/watch?v=pSqpC7fFLZA); publication: 2025-06-03T22:22:29Z; analysis: `analysis/pSqpC7fFLZA.json`.
[^zepu8Kk6FBQ]: [Agents for Everything Else — swyx](https://www.youtube.com/watch?v=zepu8Kk6FBQ); publication: 2026-05-01T04:10:33Z; analysis: `analysis/zepu8Kk6FBQ.json`.
