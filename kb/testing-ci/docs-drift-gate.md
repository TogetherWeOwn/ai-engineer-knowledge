---
{
  "type": "technique",
  "id": "docs-drift-gate",
  "title": "Detect documentation and claim drift against code and deployment artifacts",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-07-31T01:11:30Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "AMiyLItEtLA",
      "resource": "https://www.youtube.com/watch?v=AMiyLItEtLA",
      "title": "fighting slop with slop — Vaibhav Gupta, Boundary",
      "author": "Vaibhav Gupta, Boundary",
      "last_modified": "2026-07-31T01:11:30Z",
      "analysis_file": "analysis/AMiyLItEtLA.json"
    },
    {
      "id": "RFKCzGlAU6Q",
      "resource": "https://www.youtube.com/watch?v=RFKCzGlAU6Q",
      "title": "How Claude Code Works - Jared Zoneraich, PromptLayer",
      "author": "Jared Zoneraich, PromptLayer",
      "last_modified": "2025-12-26T22:04:34Z",
      "analysis_file": "analysis/RFKCzGlAU6Q.json"
    },
    {
      "id": "Wmp2Tku2PrI",
      "resource": "https://www.youtube.com/watch?v=Wmp2Tku2PrI",
      "title": "Vibe Engineering Effect Apps — Michael Arnaldi, Effectful",
      "author": "Michael Arnaldi, Effectful",
      "last_modified": "2026-05-07T15:00:06Z",
      "analysis_file": "analysis/Wmp2Tku2PrI.json"
    },
    {
      "id": "huQPkrwVWwc",
      "resource": "https://www.youtube.com/watch?v=huQPkrwVWwc",
      "title": "Design like Karpathy is watching — Zeke Sikelianos, Replicate",
      "author": "Zeke Sikelianos, Replicate",
      "last_modified": "2025-07-19T16:15:06Z",
      "analysis_file": "analysis/huQPkrwVWwc.json"
    },
    {
      "id": "rnDm57Py54A",
      "resource": "https://www.youtube.com/watch?v=rnDm57Py54A",
      "title": "Building your own software factory — Eric Zakariasson, Cursor",
      "author": "Eric Zakariasson, Cursor",
      "last_modified": "2026-04-28T18:00:06Z",
      "analysis_file": "analysis/rnDm57Py54A.json"
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

# Detect documentation and claim drift against code and deployment artifacts

## What

Detect documentation and claim drift against code and deployment artifacts

Check both implementation drift and disagreement between requirements.

## Evidence

Source analysis [^AMiyLItEtLA]; no independently matched timestamped quote published.

> pushed to our other repos. And we have a lot of commits going and it just runs
> — 54:33 [^RFKCzGlAU6Q]

> run the server instead of exporting
> — 1:16:31 [^Wmp2Tku2PrI]

Source analysis [^huQPkrwVWwc]; no independently matched timestamped quote published.

Source analysis [^rnDm57Py54A]; no independently matched timestamped quote published.

> the specifications that conflict with each other, making it easier to make
> — 07:05 [^x_1EumTaXeE]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^AMiyLItEtLA]: [fighting slop with slop — Vaibhav Gupta, Boundary](https://www.youtube.com/watch?v=AMiyLItEtLA); publication: 2026-07-31T01:11:30Z; analysis: `analysis/AMiyLItEtLA.json`.
[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
[^huQPkrwVWwc]: [Design like Karpathy is watching — Zeke Sikelianos, Replicate](https://www.youtube.com/watch?v=huQPkrwVWwc); publication: 2025-07-19T16:15:06Z; analysis: `analysis/huQPkrwVWwc.json`.
[^rnDm57Py54A]: [Building your own software factory — Eric Zakariasson, Cursor](https://www.youtube.com/watch?v=rnDm57Py54A); publication: 2026-04-28T18:00:06Z; analysis: `analysis/rnDm57Py54A.json`.
[^x_1EumTaXeE]: [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](https://www.youtube.com/watch?v=x_1EumTaXeE); publication: 2025-07-25T23:10:37Z; analysis: `analysis/x_1EumTaXeE.json`.
