---
{
  "type": "technique",
  "id": "kill-switch-drills",
  "title": "Test kill switches and mitigation latency on isolated staging scenarios",
  "area": "security-governance",
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

# Test kill switches and mitigation latency on isolated staging scenarios

## What

Test kill switches and mitigation latency on isolated staging scenarios

A switch that was never exercised may silently stop working after configuration changes.

## Evidence

> rot. They get wired on day one and then never trade. 6 months later, a config
> — 17:02 [^zU4EagB311U]

> switch goes off silently. The product owner finds out next week. Every kill
> — 16:06 [^zU4EagB311U]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^zU4EagB311U]: [Agents Need Feature Flags - Sachin Gupta](https://www.youtube.com/watch?v=zU4EagB311U); publication: 2026-07-18T07:00:06Z; analysis: `analysis/zU4EagB311U.json`.
