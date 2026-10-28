---
{
  "type": "technique",
  "id": "command-allowlist",
  "title": "Enforce process-level command and argument allowlists where the task has a finite operation set",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-10T15:00:03Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "abw_m-DRi1k",
      "resource": "https://www.youtube.com/watch?v=abw_m-DRi1k",
      "title": "The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder",
      "author": "Michael Patterson, Coder",
      "last_modified": "2026-10-10T15:00:03Z",
      "analysis_file": "analysis/abw_m-DRi1k.json"
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

# Enforce process-level command and argument allowlists where the task has a finite operation set

## What

Enforce process-level command and argument allowlists where the task has a finite operation set

An agent firewall watches process execution and denies commands that were not pre-approved, e.g. destructive git or DB operations, regardless of what the prompt asked for.

## Evidence

Source analysis [^abw_m-DRi1k]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^abw_m-DRi1k]: [The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder](https://www.youtube.com/watch?v=abw_m-DRi1k); publication: 2026-10-10T15:00:03Z; analysis: `analysis/abw_m-DRi1k.json`.
