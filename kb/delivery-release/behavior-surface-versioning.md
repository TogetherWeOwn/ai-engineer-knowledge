---
{
  "type": "technique",
  "id": "behavior-surface-versioning",
  "title": "Version instructions, tools, skills, memory policy and runtime configuration as distinct behavior surfaces",
  "area": "delivery-release",
  "status": "stable",
  "valid_from": "2026-07-18T07:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "zU4EagB311U",
      "resource": "https://www.youtube.com/watch?v=zU4EagB311U",
      "title": "Agents Need Feature Flags - Sachin Gupta",
      "author": "Sachin Gupta",
      "last_modified": "2026-07-18T07:00:06Z",
      "analysis_file": "analysis/zU4EagB311U.json"
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

# Version instructions, tools, skills, memory policy and runtime configuration as distinct behavior surfaces

## What

Version instructions, tools, skills, memory policy and runtime configuration as distinct behavior surfaces

Prompts, tools, models, memory, autonomy, and kill switches need independently reversible release controls.

## Evidence

> So here it is six type one for each surface prompt variant tool access model
> — 05:49 [^zU4EagB311U]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid failed cutover and repeated integration work
- **Speed:** Shorter safe automated promotion
- **Quality:** Release the actual tested artifact
- **Reliability:** Staging, provenance and rollback contain regressions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^zU4EagB311U]: [Agents Need Feature Flags - Sachin Gupta](https://www.youtube.com/watch?v=zU4EagB311U); publication: 2026-07-18T07:00:06Z; analysis: `analysis/zU4EagB311U.json`.
