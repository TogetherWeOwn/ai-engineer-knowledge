---
{
  "type": "technique",
  "id": "shared-workspace-awareness",
  "title": "Expose shared task and workspace ownership so agents avoid conflicting actions",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-04-25T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "kR64LOqBBCU",
      "resource": "https://www.youtube.com/watch?v=kR64LOqBBCU",
      "title": "AgentCraft: Putting the Orc in Orchestration — Ido Salomon",
      "author": "Ido Salomon",
      "last_modified": "2026-04-25T16:00:06Z",
      "analysis_file": "analysis/kR64LOqBBCU.json"
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

# Expose shared task and workspace ownership so agents avoid conflicting actions

## What

Expose shared task and workspace ownership so agents avoid conflicting actions

Shared workspaces and chat let humans and agents see each other’s active work and files, so agents know when someone else is already working.

## Evidence

Source analysis [^kR64LOqBBCU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^kR64LOqBBCU]: [AgentCraft: Putting the Orc in Orchestration — Ido Salomon](https://www.youtube.com/watch?v=kR64LOqBBCU); publication: 2026-04-25T16:00:06Z; analysis: `analysis/kR64LOqBBCU.json`.
