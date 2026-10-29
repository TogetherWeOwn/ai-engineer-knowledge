---
{
  "type": "technique",
  "id": "diagnostic-metrics",
  "title": "Use reference-free diagnostics to locate failures, not as unvalidated success guarantees",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-07-28T22:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "RFKCzGlAU6Q",
      "resource": "https://www.youtube.com/watch?v=RFKCzGlAU6Q",
      "title": "How Claude Code Works - Jared Zoneraich, PromptLayer",
      "author": "Jared Zoneraich, PromptLayer",
      "last_modified": "2025-12-26T22:04:34Z",
      "analysis_file": "analysis/RFKCzGlAU6Q.json"
    },
    {
      "id": "phchDt63qAA",
      "resource": "https://www.youtube.com/watch?v=phchDt63qAA",
      "title": "How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed",
      "author": "Ben Kunkle, Zed",
      "last_modified": "2026-05-30T16:00:06Z",
      "analysis_file": "analysis/phchDt63qAA.json"
    },
    {
      "id": "wRJD0inpmjU",
      "resource": "https://www.youtube.com/watch?v=wRJD0inpmjU",
      "title": "Evaluating AI Search: A Practical Framework for Augmented AI Systems — Quotient AI + Tavily",
      "author": "Quotient AI + Tavily",
      "last_modified": "2025-07-29T16:01:34Z",
      "analysis_file": "analysis/wRJD0inpmjU.json"
    },
    {
      "id": "wpOA-UXynoM",
      "resource": "https://www.youtube.com/watch?v=wpOA-UXynoM",
      "title": "How Forward Deployed Engineering is done at Factory — Eno Reyes",
      "author": "Eno Reyes",
      "last_modified": "2026-07-28T22:00:06Z",
      "analysis_file": "analysis/wpOA-UXynoM.json"
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

# Use reference-free diagnostics to locate failures, not as unvalidated success guarantees

## What

Use reference-free diagnostics to locate failures, not as unvalidated success guarantees

Tool count, retries and latency reveal looping or regressions but cannot replace task correctness.

## Evidence

> call a tool call. How many times does it retry? How long does it take? And these
> — 50:00 [^RFKCzGlAU6Q]

Source analysis [^phchDt63qAA]; no independently matched timestamped quote published.

Source analysis [^wRJD0inpmjU]; no independently matched timestamped quote published.

> means the ratio of actions done by humans to AI systems before
> — 18:33 [^wpOA-UXynoM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^phchDt63qAA]: [How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed](https://www.youtube.com/watch?v=phchDt63qAA); publication: 2026-05-30T16:00:06Z; analysis: `analysis/phchDt63qAA.json`.
[^wRJD0inpmjU]: [Evaluating AI Search: A Practical Framework for Augmented AI Systems — Quotient AI + Tavily](https://www.youtube.com/watch?v=wRJD0inpmjU); publication: 2025-07-29T16:01:34Z; analysis: `analysis/wRJD0inpmjU.json`.
[^wpOA-UXynoM]: [How Forward Deployed Engineering is done at Factory — Eno Reyes](https://www.youtube.com/watch?v=wpOA-UXynoM); publication: 2026-07-28T22:00:06Z; analysis: `analysis/wpOA-UXynoM.json`.
