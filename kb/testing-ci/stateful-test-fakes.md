---
{
  "type": "technique",
  "id": "stateful-test-fakes",
  "title": "Keep coherent deterministic state across mocked tool calls and fake services",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-07-29T19:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KMR_RBoCa4M",
      "resource": "https://www.youtube.com/watch?v=KMR_RBoCa4M",
      "title": "SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)",
      "author": "Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)",
      "last_modified": "2026-07-29T19:00:06Z",
      "analysis_file": "analysis/KMR_RBoCa4M.json"
    },
    {
      "id": "R30col3UPUg",
      "resource": "https://www.youtube.com/watch?v=R30col3UPUg",
      "title": "Building Applications with AI Agents — Michael Albada, Microsoft",
      "author": "Michael Albada, Microsoft",
      "last_modified": "2025-07-24T15:00:53Z",
      "analysis_file": "analysis/R30col3UPUg.json"
    },
    {
      "id": "RkVILz06y08",
      "resource": "https://www.youtube.com/watch?v=RkVILz06y08",
      "title": "Real world MCPs in GitHub Copilot Agent Mode — Jon Peck, Microsoft",
      "author": "Jon Peck, Microsoft",
      "last_modified": "2025-07-19T07:00:21Z",
      "analysis_file": "analysis/RkVILz06y08.json"
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

# Keep coherent deterministic state across mocked tool calls and fake services

## What

Keep coherent deterministic state across mocked tool calls and fake services

Back simulated conversations with deterministic state transitions so identities, addresses, account data and prior mutations stay consistent across tools and turns.

## Evidence

Source analysis [^KMR_RBoCa4M]; no independently matched timestamped quote published.

> have access to your raw user data uh for uh security or privacy concerns, or
> — 11:39 [^R30col3UPUg]

> that Postgress database, pull the data and then make a mock.json which I can
> — 07:32 [^RkVILz06y08]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KMR_RBoCa4M]: [SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)](https://www.youtube.com/watch?v=KMR_RBoCa4M); publication: 2026-07-29T19:00:06Z; analysis: `analysis/KMR_RBoCa4M.json`.
[^R30col3UPUg]: [Building Applications with AI Agents — Michael Albada, Microsoft](https://www.youtube.com/watch?v=R30col3UPUg); publication: 2025-07-24T15:00:53Z; analysis: `analysis/R30col3UPUg.json`.
[^RkVILz06y08]: [Real world MCPs in GitHub Copilot Agent Mode — Jon Peck, Microsoft](https://www.youtube.com/watch?v=RkVILz06y08); publication: 2025-07-19T07:00:21Z; analysis: `analysis/RkVILz06y08.json`.
