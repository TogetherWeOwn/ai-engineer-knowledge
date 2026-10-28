---
{
  "type": "technique",
  "id": "localization-scaffolding",
  "title": "Build reusable localization primitives rather than ad hoc per-feature translations",
  "area": "product-ui-quality",
  "status": "stable",
  "valid_from": "2026-04-17T00:29:28Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "am_oeAoUhew",
      "resource": "https://www.youtube.com/watch?v=am_oeAoUhew",
      "title": "Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI",
      "author": "Ryan Lopopolo, OpenAI",
      "last_modified": "2026-04-17T00:29:28Z",
      "analysis_file": "analysis/am_oeAoUhew.json"
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

# Build reusable localization primitives rather than ad hoc per-feature translations

## What

Build reusable localization primitives rather than ad hoc per-feature translations

Shared internationalization structure lets additional languages reuse the same application paths.

## Evidence

Source analysis [^am_oeAoUhew]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less rework from misunderstood intent
- **Speed:** Faster useful feedback on runnable behavior
- **Quality:** Better usability, accessibility and actual task completion
- **Reliability:** Real-app evidence rather than attractive but broken demos
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
