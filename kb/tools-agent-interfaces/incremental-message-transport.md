---
{
  "type": "technique",
  "id": "incremental-message-transport",
  "title": "Reuse persistent transport and send revision-checked deltas instead of full history",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-08-10T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "MhHEGMFCEB0",
      "resource": "https://www.youtube.com/watch?v=MhHEGMFCEB0",
      "title": "OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman",
      "author": "Vaibhav Srivastav & Katia Gil Guzman",
      "last_modified": "2026-04-29T16:00:06Z",
      "analysis_file": "analysis/MhHEGMFCEB0.json"
    },
    {
      "id": "shRR1e2HXMk",
      "resource": "https://www.youtube.com/watch?v=shRR1e2HXMk",
      "title": "How Codex Works — Dominik Kundel, OpenAI",
      "author": "Dominik Kundel, OpenAI",
      "last_modified": "2026-08-10T16:00:06Z",
      "analysis_file": "analysis/shRR1e2HXMk.json"
    },
    {
      "id": "wflNENRSUb4",
      "resource": "https://www.youtube.com/watch?v=wflNENRSUb4",
      "title": "Give Your Agent a Computer — Nico Albanese, Vercel",
      "author": "Nico Albanese, Vercel",
      "last_modified": "2026-05-12T18:00:06Z",
      "analysis_file": "analysis/wflNENRSUb4.json"
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

# Reuse persistent transport and send revision-checked deltas instead of full history

## What

Reuse persistent transport and send revision-checked deltas instead of full history

Reuse connections and server conversation state to reduce repeated request transport, particularly across many tool turns.

## Evidence

Source analysis [^MhHEGMFCEB0]; no independently matched timestamped quote published.

Source analysis [^shRR1e2HXMk]; no independently matched timestamped quote published.

> the more classic pattern is sending just the most recent message here.
> — 34:47 [^wflNENRSUb4]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^MhHEGMFCEB0]: [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](https://www.youtube.com/watch?v=MhHEGMFCEB0); publication: 2026-04-29T16:00:06Z; analysis: `analysis/MhHEGMFCEB0.json`.
[^shRR1e2HXMk]: [How Codex Works — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=shRR1e2HXMk); publication: 2026-08-10T16:00:06Z; analysis: `analysis/shRR1e2HXMk.json`.
[^wflNENRSUb4]: [Give Your Agent a Computer — Nico Albanese, Vercel](https://www.youtube.com/watch?v=wflNENRSUb4); publication: 2026-05-12T18:00:06Z; analysis: `analysis/wflNENRSUb4.json`.
