---
{
  "type": "technique",
  "id": "mutation-testing",
  "title": "Use diff-scoped mutation testing to detect hollow coverage",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-09T14:00:20Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "E3KbFLAGD6A",
      "resource": "https://www.youtube.com/watch?v=E3KbFLAGD6A",
      "title": "Stop Prompting — Greg Pstrucha, Sentry",
      "author": "Greg Pstrucha, Sentry",
      "last_modified": "2026-10-09T14:00:20Z",
      "analysis_file": "analysis/E3KbFLAGD6A.json"
    },
    {
      "id": "ShuJ_CN6zr4",
      "resource": "https://www.youtube.com/watch?v=ShuJ_CN6zr4",
      "title": "Making Codebases Agent Ready – Eno Reyes, Factory AI",
      "author": "Eno Reyes, Factory AI",
      "last_modified": "2025-12-22T17:00:06Z",
      "analysis_file": "analysis/ShuJ_CN6zr4.json"
    },
    {
      "id": "TJPInBjhE4Q",
      "resource": "https://www.youtube.com/watch?v=TJPInBjhE4Q",
      "title": "ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay",
      "author": "Sachin Gupta, Ebay",
      "last_modified": "2026-07-12T12:15:38Z",
      "analysis_file": "analysis/TJPInBjhE4Q.json"
    },
    {
      "id": "X6l4lpA0_NY",
      "resource": "https://www.youtube.com/watch?v=X6l4lpA0_NY",
      "title": "Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl",
      "author": "Dru Knox, Tessl",
      "last_modified": "2026-10-06T15:30:27Z",
      "analysis_file": "analysis/X6l4lpA0_NY.json"
    },
    {
      "id": "x_1EumTaXeE",
      "resource": "https://www.youtube.com/watch?v=x_1EumTaXeE",
      "title": "Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue",
      "author": "Josh Albrecht, Imbue",
      "last_modified": "2025-07-25T23:10:37Z",
      "analysis_file": "analysis/x_1EumTaXeE.json"
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

# Use diff-scoped mutation testing to detect hollow coverage

## What

Use diff-scoped mutation testing to detect hollow coverage

Deliberately altered behavior reveals tests that execute code but fail to detect wrong results, complementing line coverage and LLM test review.

## Evidence

Source analysis [^E3KbFLAGD6A]; no independently matched timestamped quote published.

Source analysis [^ShuJ_CN6zr4]; no independently matched timestamped quote published.

Source analysis [^TJPInBjhE4Q]; no independently matched timestamped quote published.

Source analysis [^X6l4lpA0_NY]; no independently matched timestamped quote published.

> also a thing looked at the tests and thought they were reasonable. Now you
> — 14:23 [^x_1EumTaXeE]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^E3KbFLAGD6A]: [Stop Prompting — Greg Pstrucha, Sentry](https://www.youtube.com/watch?v=E3KbFLAGD6A); publication: 2026-10-09T14:00:20Z; analysis: `analysis/E3KbFLAGD6A.json`.
[^ShuJ_CN6zr4]: [Making Codebases Agent Ready – Eno Reyes, Factory AI](https://www.youtube.com/watch?v=ShuJ_CN6zr4); publication: 2025-12-22T17:00:06Z; analysis: `analysis/ShuJ_CN6zr4.json`.
[^TJPInBjhE4Q]: [ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay](https://www.youtube.com/watch?v=TJPInBjhE4Q); publication: 2026-07-12T12:15:38Z; analysis: `analysis/TJPInBjhE4Q.json`.
[^X6l4lpA0_NY]: [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](https://www.youtube.com/watch?v=X6l4lpA0_NY); publication: 2026-10-06T15:30:27Z; analysis: `analysis/X6l4lpA0_NY.json`.
[^x_1EumTaXeE]: [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](https://www.youtube.com/watch?v=x_1EumTaXeE); publication: 2025-07-25T23:10:37Z; analysis: `analysis/x_1EumTaXeE.json`.
