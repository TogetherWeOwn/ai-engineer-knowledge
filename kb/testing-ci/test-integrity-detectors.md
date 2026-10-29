---
{
  "type": "technique",
  "id": "test-integrity-detectors",
  "title": "Detect tautological, source-reading and over-mocked tests that can make green CI misleading",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-09-26T00:07:54Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "LlgiOCmFG_w",
      "resource": "https://www.youtube.com/watch?v=LlgiOCmFG_w",
      "title": "Fixing the PR Bottleneck — Matt Pocock, AIHero",
      "author": "Matt Pocock, AIHero",
      "last_modified": "2026-09-26T00:07:54Z",
      "analysis_file": "analysis/LlgiOCmFG_w.json"
    },
    {
      "id": "uIiA6DquRiE",
      "resource": "https://www.youtube.com/watch?v=uIiA6DquRiE",
      "title": "Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth",
      "author": "Daniel Han, Unsloth",
      "last_modified": "2026-07-17T17:00:06Z",
      "analysis_file": "analysis/uIiA6DquRiE.json"
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

# Detect tautological, source-reading and over-mocked tests that can make green CI misleading

## What

Detect tautological, source-reading and over-mocked tests that can make green CI misleading

Three named patterns of tests that lie: tests that restate a constant or the implementation; tests that read source text to check UI ordering; mocks that remove real failure modes, so the test cannot fail. Countermeasures: deep modules with small interfaces that tests go through, a red test first (TDD), and a reviewer that checks what the tests actually assert.

## Evidence

Source analysis [^LlgiOCmFG_w]; no independently matched timestamped quote published.

Source analysis [^uIiA6DquRiE]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^LlgiOCmFG_w]: [Fixing the PR Bottleneck — Matt Pocock, AIHero](https://www.youtube.com/watch?v=LlgiOCmFG_w); publication: 2026-09-26T00:07:54Z; analysis: `analysis/LlgiOCmFG_w.json`.
[^uIiA6DquRiE]: [Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth](https://www.youtube.com/watch?v=uIiA6DquRiE); publication: 2026-07-17T17:00:06Z; analysis: `analysis/uIiA6DquRiE.json`.
