---
{
  "type": "technique",
  "id": "red-on-base-tests",
  "title": "Require new regression tests to fail on the unfixed base revision",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-07-23T16:30:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Ib5GBkD555M",
      "resource": "https://www.youtube.com/watch?v=Ib5GBkD555M",
      "title": "Why Software Factories Fail",
      "author": null,
      "last_modified": "2026-07-23T16:30:06Z",
      "analysis_file": "analysis/Ib5GBkD555M.json"
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

# Require new regression tests to fail on the unfixed base revision

## What

Require new regression tests to fail on the unfixed base revision

Benchmarks such as SWE-bench check out the base commit, revert the agent's test edits and apply hidden tests. Frontier Code goes further and penalizes any model-written test that passes on the pre-patch code, because such a test does not exercise the change. The idea transfers as a deterministic check: run the PR's new or changed tests against base code. A test that passes there is vacuous for a fix or feature.

## Evidence

Source analysis [^Ib5GBkD555M]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Ib5GBkD555M]: [Why Software Factories Fail](https://www.youtube.com/watch?v=Ib5GBkD555M); publication: 2026-07-23T16:30:06Z; analysis: `analysis/Ib5GBkD555M.json`.
