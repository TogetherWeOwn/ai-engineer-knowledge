---
{
  "type": "technique",
  "id": "failure-counter-scope",
  "title": "Scope failure counters to the relevant request, task and provider rather than unrelated traffic",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-08-28T15:30:03Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "zrZ1amZBSPw",
      "resource": "https://www.youtube.com/watch?v=zrZ1amZBSPw",
      "title": "Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio",
      "author": "Kanish Manuja, Twilio",
      "last_modified": "2026-08-28T15:30:03Z",
      "analysis_file": "analysis/zrZ1amZBSPw.json"
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

# Scope failure counters to the relevant request, task and provider rather than unrelated traffic

## What

Scope failure counters to the relevant request, task and provider rather than unrelated traffic

Fleet-shared cooldown counters react faster; instance-local counters change behavior when replica counts change.

## Evidence

> If you want quick failovers, then fleetwide helps. And with instance uh
> — 04:15 [^zrZ1amZBSPw]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^zrZ1amZBSPw]: [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](https://www.youtube.com/watch?v=zrZ1amZBSPw); publication: 2026-08-28T15:30:03Z; analysis: `analysis/zrZ1amZBSPw.json`.
