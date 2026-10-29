---
{
  "type": "technique",
  "id": "durability-proof-tests",
  "title": "Demonstrate crash, restart and persistence invariants before claiming durable execution",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-01-12T19:30:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "k8cnVCMYmNc",
      "resource": "https://www.youtube.com/watch?v=k8cnVCMYmNc",
      "title": "OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal",
      "author": "Cornelia Davis, Temporal",
      "last_modified": "2026-01-12T19:30:06Z",
      "analysis_file": "analysis/k8cnVCMYmNc.json"
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

# Demonstrate crash, restart and persistence invariants before claiming durable execution

## What

Demonstrate crash, restart and persistence invariants before claiming durable execution

Demonstrate worker loss, network failure and state reconstruction; verify that the backing service itself uses durable storage, not only in-memory development state.

## Evidence

> it keeps going. So, it picked up where it left off. Now, when I say it picked
> — 41:55 [^k8cnVCMYmNc]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^k8cnVCMYmNc]: [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](https://www.youtube.com/watch?v=k8cnVCMYmNc); publication: 2026-01-12T19:30:06Z; analysis: `analysis/k8cnVCMYmNc.json`.
