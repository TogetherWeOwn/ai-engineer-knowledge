---
{
  "type": "technique",
  "id": "deterministic-ownership-routing",
  "title": "Route defects and vulnerability work using verified service ownership metadata",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-07-17T21:27:20Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "imFedndyXYQ",
      "resource": "https://www.youtube.com/watch?v=imFedndyXYQ",
      "title": "Using LLMs to Secure Source Code — Eugene Yan, Anthropic",
      "author": "Eugene Yan, Anthropic",
      "last_modified": "2026-07-17T21:27:20Z",
      "analysis_file": "analysis/imFedndyXYQ.json"
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

# Route defects and vulnerability work using verified service ownership metadata

## What

Route defects and vulnerability work using verified service ownership metadata

Known ownership mapping can dispatch findings without an LLM reasoning about the recipient each time.

## Evidence

Source analysis [^imFedndyXYQ]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^imFedndyXYQ]: [Using LLMs to Secure Source Code — Eugene Yan, Anthropic](https://www.youtube.com/watch?v=imFedndyXYQ); publication: 2026-07-17T21:27:20Z; analysis: `analysis/imFedndyXYQ.json`.
