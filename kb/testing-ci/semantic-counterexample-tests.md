---
{
  "type": "technique",
  "id": "semantic-counterexample-tests",
  "title": "Test semantic counterexamples before enforcing regex or heuristic verdicts",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-05T17:00:22Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "NdrSPm6NCdk",
      "resource": "https://www.youtube.com/watch?v=NdrSPm6NCdk",
      "title": "Evals in AI: A Deep Dive — Tejas Kumar, IBM",
      "author": "Tejas Kumar, IBM",
      "last_modified": "2026-10-05T17:00:22Z",
      "analysis_file": "analysis/NdrSPm6NCdk.json"
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

# Test semantic counterexamples before enforcing regex or heuristic verdicts

## What

Test semantic counterexamples before enforcing regex or heuristic verdicts

A keyword can occur in a policy-violating answer, so matching the word is not proof that the intended decision was made.

## Evidence

> cannot pay for the shipping, right? And now that absolute nonsense is green,
> — 31:56 [^NdrSPm6NCdk]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^NdrSPm6NCdk]: [Evals in AI: A Deep Dive — Tejas Kumar, IBM](https://www.youtube.com/watch?v=NdrSPm6NCdk); publication: 2026-10-05T17:00:22Z; analysis: `analysis/NdrSPm6NCdk.json`.
