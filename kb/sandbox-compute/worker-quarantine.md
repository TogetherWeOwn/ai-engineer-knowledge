---
{
  "type": "technique",
  "id": "worker-quarantine",
  "title": "Quarantine proven unhealthy workers through a bounded supported policy while honoring explicit holds",
  "area": "sandbox-compute",
  "status": "stable",
  "valid_from": "2026-10-03T21:00:39Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "bRGyYaE0lxI",
      "resource": "https://www.youtube.com/watch?v=bRGyYaE0lxI",
      "title": "GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe",
      "author": "Crusoe",
      "last_modified": "2026-10-03T21:00:39Z",
      "analysis_file": "analysis/bRGyYaE0lxI.json"
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

# Quarantine proven unhealthy workers through a bounded supported policy while honoring explicit holds

## What

Quarantine proven unhealthy workers through a bounded supported policy while honoring explicit holds

On a critical hardware error, the system marks the node down, cancels running jobs, cordons and drains the Kubernetes node, removes it from the pool, and replaces it from spare capacity.

## Evidence

Source analysis [^bRGyYaE0lxI]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable idle and duplicated compute
- **Speed:** Reduce measured execution/queue bottlenecks
- **Quality:** Reproducible command and environment evidence
- **Reliability:** Isolation, cleanup and recovery guarantees
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^bRGyYaE0lxI]: [GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe](https://www.youtube.com/watch?v=bRGyYaE0lxI); publication: 2026-10-03T21:00:39Z; analysis: `analysis/bRGyYaE0lxI.json`.
