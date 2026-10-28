---
{
  "type": "technique",
  "id": "quality-ratchets",
  "title": "Ratchet lint and quality deltas without requiring a legacy-code rewrite",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-07-25T20:41:40Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "JvosMkuNxF8",
      "resource": "https://www.youtube.com/watch?v=JvosMkuNxF8",
      "title": "Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford",
      "author": "Yegor Denisov-Blanch, Stanford",
      "last_modified": "2025-12-11T21:56:44Z",
      "analysis_file": "analysis/JvosMkuNxF8.json"
    },
    {
      "id": "xIt_mTQp6mY",
      "resource": "https://www.youtube.com/watch?v=xIt_mTQp6mY",
      "title": "Loop Engineering from First Principles — Kyle Mistele, HumanLayer",
      "author": "Kyle Mistele, HumanLayer",
      "last_modified": "2026-07-25T20:41:40Z",
      "analysis_file": "analysis/xIt_mTQp6mY.json"
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

# Ratchet lint and quality deltas without requiring a legacy-code rewrite

## What

Ratchet lint and quality deltas without requiring a legacy-code rewrite

Compare base and head diagnostics so new errors fail without requiring all historical debt to be fixed.

## Evidence

> codebase hygiene to unlock these AI productivity gains.
> — 04:46 [^JvosMkuNxF8]

> all the violations deterministically, and track it in our version control.
> — 10:51 [^xIt_mTQp6mY]

> there before it started and then what issues were there after it ran. So at
> — 09:43 [^x_1EumTaXeE]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^JvosMkuNxF8]: [Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford](https://www.youtube.com/watch?v=JvosMkuNxF8); publication: 2025-12-11T21:56:44Z; analysis: `analysis/JvosMkuNxF8.json`.
[^xIt_mTQp6mY]: [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](https://www.youtube.com/watch?v=xIt_mTQp6mY); publication: 2026-07-25T20:41:40Z; analysis: `analysis/xIt_mTQp6mY.json`.
[^x_1EumTaXeE]: [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](https://www.youtube.com/watch?v=x_1EumTaXeE); publication: 2025-07-25T23:10:37Z; analysis: `analysis/x_1EumTaXeE.json`.
