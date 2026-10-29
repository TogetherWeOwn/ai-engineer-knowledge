---
{
  "type": "technique",
  "id": "downstream-impact-preflight",
  "title": "Check downstream data and service impact before editing high-coupling behavior",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-20T19:00:34Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "adfw3xJBx1o",
      "resource": "https://www.youtube.com/watch?v=adfw3xJBx1o",
      "title": "A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo",
      "author": "Felipe Felisola Caso & Francesco Galletta, Monzo",
      "last_modified": "2026-10-20T19:00:34Z",
      "analysis_file": "analysis/adfw3xJBx1o.json"
    },
    {
      "id": "eIoohUmYpGI",
      "resource": "https://www.youtube.com/watch?v=eIoohUmYpGI",
      "title": "The Infinite Software Crisis – Jake Nations, Netflix",
      "author": "Jake Nations, Netflix",
      "last_modified": "2025-12-20T17:00:06Z",
      "analysis_file": "analysis/eIoohUmYpGI.json"
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

# Check downstream data and service impact before editing high-coupling behavior

## What

Check downstream data and service impact before editing high-coupling behavior

Produce one map of existing components, dependencies and affected behavior, refining it with targeted questions.

## Evidence

Source analysis [^adfw3xJBx1o]; no independently matched timestamped quote published.

Source analysis [^eIoohUmYpGI]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^adfw3xJBx1o]: [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](https://www.youtube.com/watch?v=adfw3xJBx1o); publication: 2026-10-20T19:00:34Z; analysis: `analysis/adfw3xJBx1o.json`.
[^eIoohUmYpGI]: [The Infinite Software Crisis – Jake Nations, Netflix](https://www.youtube.com/watch?v=eIoohUmYpGI); publication: 2025-12-20T17:00:06Z; analysis: `analysis/eIoohUmYpGI.json`.
