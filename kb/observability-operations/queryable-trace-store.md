---
{
  "type": "technique",
  "id": "queryable-trace-store",
  "title": "Expose full event and trace evidence through scoped query tools rather than metrics alone",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-10-12T06:07:42Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "TeErpYBUIeM",
      "resource": "https://www.youtube.com/watch?v=TeErpYBUIeM",
      "title": "The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse",
      "author": "Marc Klingen, Langfuse",
      "last_modified": "2026-10-06T17:00:19Z",
      "analysis_file": "analysis/TeErpYBUIeM.json"
    },
    {
      "id": "XBaznoTRDFI",
      "resource": "https://www.youtube.com/watch?v=XBaznoTRDFI",
      "title": "How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust",
      "author": "Phil Hetzel, Braintrust",
      "last_modified": "2026-05-28T23:00:06Z",
      "analysis_file": "analysis/XBaznoTRDFI.json"
    },
    {
      "id": "cgimkNGNjvU",
      "resource": "https://www.youtube.com/watch?v=cgimkNGNjvU",
      "title": "Agentic Development Security — Ezra Tanzer, Snyk",
      "author": "Ezra Tanzer, Snyk",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/cgimkNGNjvU.json"
    },
    {
      "id": "qJtcEDc_WJU",
      "resource": "https://www.youtube.com/watch?v=qJtcEDc_WJU",
      "title": "Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T06:07:42Z",
      "analysis_file": "analysis/qJtcEDc_WJU.json"
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

# Expose full event and trace evidence through scoped query tools rather than metrics alone

## What

Expose full event and trace evidence through scoped query tools rather than metrics alone

A joined session record makes actions, data access and expenditure attributable and enables incident reconstruction.

## Evidence

> evils and traces. Now it's way more read intensive because agents can like like
> — 16:13 [^TeErpYBUIeM]

Source analysis [^XBaznoTRDFI]; no independently matched timestamped quote published.

> Giving me an audit of everything that my LLM's and all of my LLM's are doing on
> — 17:24 [^cgimkNGNjvU]

> >> Uh right now you get all the events and you just filter them on your end. If
> — 05:28 [^qJtcEDc_WJU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^TeErpYBUIeM]: [The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](https://www.youtube.com/watch?v=TeErpYBUIeM); publication: 2026-10-06T17:00:19Z; analysis: `analysis/TeErpYBUIeM.json`.
[^XBaznoTRDFI]: [How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust](https://www.youtube.com/watch?v=XBaznoTRDFI); publication: 2026-05-28T23:00:06Z; analysis: `analysis/XBaznoTRDFI.json`.
[^cgimkNGNjvU]: [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU); publication: 2026-07-20T17:17:53Z; analysis: `analysis/cgimkNGNjvU.json`.
[^qJtcEDc_WJU]: [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](https://www.youtube.com/watch?v=qJtcEDc_WJU); publication: 2026-10-12T06:07:42Z; analysis: `analysis/qJtcEDc_WJU.json`.
