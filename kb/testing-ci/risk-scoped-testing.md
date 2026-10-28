---
{
  "type": "technique",
  "id": "risk-scoped-testing",
  "title": "Select tests by changed behavior and risk while preserving required safety coverage",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-02T21:30:22Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "4VhbYlfC7Gs",
      "resource": "https://www.youtube.com/watch?v=4VhbYlfC7Gs",
      "title": "Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw",
      "author": "Vincent Koc, OpenClaw",
      "last_modified": "2026-05-12T16:00:06Z",
      "analysis_file": "analysis/4VhbYlfC7Gs.json"
    },
    {
      "id": "EUHx5ooJHuQ",
      "resource": "https://www.youtube.com/watch?v=EUHx5ooJHuQ",
      "title": "How Coding Agents change Software Development Forever - Hailong Zhang",
      "author": "Hailong Zhang",
      "last_modified": "2025-02-22T16:00:06Z",
      "analysis_file": "analysis/EUHx5ooJHuQ.json"
    },
    {
      "id": "HLTa7Vcs4X0",
      "resource": "https://www.youtube.com/watch?v=HLTa7Vcs4X0",
      "title": "Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous",
      "author": "Gabriel Spencer-Harper, Meticulous",
      "last_modified": "2026-10-02T21:30:22Z",
      "analysis_file": "analysis/HLTa7Vcs4X0.json"
    },
    {
      "id": "ObTPqBGsEbA",
      "resource": "https://www.youtube.com/watch?v=ObTPqBGsEbA",
      "title": "The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks",
      "author": "Sandipan Bhaumik, Databricks",
      "last_modified": "2026-06-18T13:00:06Z",
      "analysis_file": "analysis/ObTPqBGsEbA.json"
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

# Select tests by changed behavior and risk while preserving required safety coverage

## What

Select tests by changed behavior and risk while preserving required safety coverage

Run relevant small subsets during iteration and schedule broader coverage only at controlled milestones, avoiding repeated expensive full-suite execution.

## Evidence

Source analysis [^4VhbYlfC7Gs]; no independently matched timestamped quote published.

Source analysis [^EUHx5ooJHuQ]; no independently matched timestamped quote published.

Source analysis [^HLTa7Vcs4X0]; no independently matched timestamped quote published.

> just just selecting a small subset of the eval data set to do the testing. And
> — 35:41 [^ObTPqBGsEbA]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^4VhbYlfC7Gs]: [Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=4VhbYlfC7Gs); publication: 2026-05-12T16:00:06Z; analysis: `analysis/4VhbYlfC7Gs.json`.
[^EUHx5ooJHuQ]: [How Coding Agents change Software Development Forever - Hailong Zhang](https://www.youtube.com/watch?v=EUHx5ooJHuQ); publication: 2025-02-22T16:00:06Z; analysis: `analysis/EUHx5ooJHuQ.json`.
[^HLTa7Vcs4X0]: [Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous](https://www.youtube.com/watch?v=HLTa7Vcs4X0); publication: 2026-10-02T21:30:22Z; analysis: `analysis/HLTa7Vcs4X0.json`.
[^ObTPqBGsEbA]: [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA); publication: 2026-06-18T13:00:06Z; analysis: `analysis/ObTPqBGsEbA.json`.
