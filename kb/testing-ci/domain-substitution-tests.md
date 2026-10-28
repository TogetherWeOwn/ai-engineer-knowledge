---
{
  "type": "technique",
  "id": "domain-substitution-tests",
  "title": "Encode valid domain substitutions and dictionaries as focused regression tests",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-05-31T15:00:10Z",
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

# Encode valid domain substitutions and dictionaries as focused regression tests

## What

Encode valid domain substitutions and dictionaries as focused regression tests

Perturbations must preserve domain meaning; near-synonyms such as gross sales and gross profit are not interchangeable test variants.

## Evidence

Source analysis [^UQKg0td-Bf4]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^UQKg0td-Bf4]: [Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence](https://www.youtube.com/watch?v=UQKg0td-Bf4); publication: 2026-05-31T15:00:10Z; analysis: `analysis/UQKg0td-Bf4.json`.
