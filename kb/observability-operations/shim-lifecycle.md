---
{
  "type": "technique",
  "id": "shim-lifecycle",
  "title": "Register temporary guards with firing telemetry, ownership and a retirement condition",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-10-19T19:00:17Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "7Y4sbZgBdnc",
      "resource": "https://www.youtube.com/watch?v=7Y4sbZgBdnc",
      "title": "Is the Agent Harness Dead? — Jediah Katz, SpaceXAI",
      "author": "Jediah Katz, SpaceXAI",
      "last_modified": "2026-10-19T19:00:17Z",
      "analysis_file": "analysis/7Y4sbZgBdnc.json"
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

# Register temporary guards with firing telemetry, ownership and a retirement condition

## What

Register temporary guards with firing telemetry, ownership and a retirement condition

Deterministic guardrails that patch model or harness gaps are tracked in one place, and every firing is logged. A bot watches the dashboard and opens a deletion PR when a shim stops firing, so the harness sheds dead scaffolding as models and upstream improve.

## Evidence

Source analysis [^7Y4sbZgBdnc]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^7Y4sbZgBdnc]: [Is the Agent Harness Dead? — Jediah Katz, SpaceXAI](https://www.youtube.com/watch?v=7Y4sbZgBdnc); publication: 2026-10-19T19:00:17Z; analysis: `analysis/7Y4sbZgBdnc.json`.
