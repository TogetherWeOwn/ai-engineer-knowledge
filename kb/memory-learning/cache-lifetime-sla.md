---
{
  "type": "technique",
  "id": "cache-lifetime-sla",
  "title": "Choose hot-state persistence and cache lifetimes from recovery and freshness requirements",
  "area": "memory-learning",
  "status": "stable",
  "valid_from": "2026-07-30T00:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "o6U_2vd967Y",
      "resource": "https://www.youtube.com/watch?v=o6U_2vd967Y",
      "title": "Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft",
      "author": "Divakar Kumar, FlyersSoft",
      "last_modified": "2026-07-30T00:00:06Z",
      "analysis_file": "analysis/o6U_2vd967Y.json"
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

# Choose hot-state persistence and cache lifetimes from recovery and freshness requirements

## What

Choose hot-state persistence and cache lifetimes from recovery and freshness requirements

They deliberately use in-memory short-term memory rather than long-term memory because the transaction SLA is sub-500ms, trading memory richness for latency.

## Evidence

Source analysis [^o6U_2vd967Y]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated investigation
- **Speed:** Faster reuse of relevant prior work
- **Quality:** More current, scoped lessons
- **Reliability:** Less stale, conflicting or unsupported recall
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^o6U_2vd967Y]: [Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft](https://www.youtube.com/watch?v=o6U_2vd967Y); publication: 2026-07-30T00:00:06Z; analysis: `analysis/o6U_2vd967Y.json`.
