---
{
  "type": "technique",
  "id": "data-parity-audit",
  "title": "Verify data parity with row-count, key and column-level checks before promoting a transform",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-21T08:00:37Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "uA4ah-dVHvU",
      "resource": "https://www.youtube.com/watch?v=uA4ah-dVHvU",
      "title": "AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard",
      "author": "Gareth Yoder, Vanguard",
      "last_modified": "2026-10-21T08:00:37Z",
      "analysis_file": "analysis/uA4ah-dVHvU.json"
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

# Verify data parity with row-count, key and column-level checks before promoting a transform

## What

Verify data parity with row-count, key and column-level checks before promoting a transform

Daily audits first verify row-level counts for consistency, then check individual columns for integrity between legacy and modern stores.

## Evidence

Source analysis [^uA4ah-dVHvU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^uA4ah-dVHvU]: [AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard](https://www.youtube.com/watch?v=uA4ah-dVHvU); publication: 2026-10-21T08:00:37Z; analysis: `analysis/uA4ah-dVHvU.json`.
