---
{
  "type": "technique",
  "id": "robustness-envelope",
  "title": "Declare and exercise realistic input perturbations and operating limits",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-09-14T15:00:19Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "UQKg0td-Bf4",
      "resource": "https://www.youtube.com/watch?v=UQKg0td-Bf4",
      "title": "Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence",
      "author": "Steven Willmott, SafeIntelligence",
      "last_modified": "2026-05-31T15:00:10Z",
      "analysis_file": "analysis/UQKg0td-Bf4.json"
    },
    {
      "id": "hOWU0KPUp1k",
      "resource": "https://www.youtube.com/watch?v=hOWU0KPUp1k",
      "title": "Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley",
      "author": "Brendan Rappazzo, Morgan Stanley",
      "last_modified": "2026-09-14T15:00:19Z",
      "analysis_file": "analysis/hOWU0KPUp1k.json"
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

# Declare and exercise realistic input perturbations and operating limits

## What

Declare and exercise realistic input perturbations and operating limits

Typos, paraphrases and stress variations test whether behavior remains stable within a declared range of acceptable input change.

## Evidence

Source analysis [^UQKg0td-Bf4]; no independently matched timestamped quote published.

Source analysis [^hOWU0KPUp1k]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^UQKg0td-Bf4]: [Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence](https://www.youtube.com/watch?v=UQKg0td-Bf4); publication: 2026-05-31T15:00:10Z; analysis: `analysis/UQKg0td-Bf4.json`.
[^hOWU0KPUp1k]: [Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley](https://www.youtube.com/watch?v=hOWU0KPUp1k); publication: 2026-09-14T15:00:19Z; analysis: `analysis/hOWU0KPUp1k.json`.
