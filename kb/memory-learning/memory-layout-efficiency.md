---
{
  "type": "technique",
  "id": "memory-layout-efficiency",
  "title": "Use compact indexed memory layouts only when recall quality and provenance survive",
  "area": "memory-learning",
  "status": "stable",
  "valid_from": "2026-09-14T16:30:33Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "5ZGyKWjQDr0",
      "resource": "https://www.youtube.com/watch?v=5ZGyKWjQDr0",
      "title": "Lessons from Studying Every Memory System — Shlok Khemani, Independent",
      "author": "Shlok Khemani, Independent",
      "last_modified": "2026-08-12T18:30:06Z",
      "analysis_file": "analysis/5ZGyKWjQDr0.json"
    },
    {
      "id": "jA_x7F8caHI",
      "resource": "https://www.youtube.com/watch?v=jA_x7F8caHI",
      "title": "No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle",
      "author": "Kay Malcolm, Oracle",
      "last_modified": "2026-09-14T16:30:33Z",
      "analysis_file": "analysis/jA_x7F8caHI.json"
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

# Use compact indexed memory layouts only when recall quality and provenance survive

## What

Use compact indexed memory layouts only when recall quality and provenance survive

File or chat memory works for one agent but breaks when multiple agents need shared context.

## Evidence

Source analysis [^5ZGyKWjQDr0]; no independently matched timestamped quote published.

Source analysis [^jA_x7F8caHI]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated investigation
- **Speed:** Faster reuse of relevant prior work
- **Quality:** More current, scoped lessons
- **Reliability:** Less stale, conflicting or unsupported recall
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^5ZGyKWjQDr0]: [Lessons from Studying Every Memory System — Shlok Khemani, Independent](https://www.youtube.com/watch?v=5ZGyKWjQDr0); publication: 2026-08-12T18:30:06Z; analysis: `analysis/5ZGyKWjQDr0.json`.
[^jA_x7F8caHI]: [No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle](https://www.youtube.com/watch?v=jA_x7F8caHI); publication: 2026-09-14T16:30:33Z; analysis: `analysis/jA_x7F8caHI.json`.
