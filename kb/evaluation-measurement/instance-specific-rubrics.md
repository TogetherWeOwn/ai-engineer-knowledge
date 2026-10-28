---
{
  "type": "technique",
  "id": "instance-specific-rubrics",
  "title": "Add task-specific criteria without replacing immutable global policy",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-07-11T00:57:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "IIL2tE4n1Q0",
      "resource": "https://www.youtube.com/watch?v=IIL2tE4n1Q0",
      "title": "Judging LLMs: Alex Volkov",
      "author": null,
      "last_modified": "2024-09-09T18:39:17Z",
      "analysis_file": "analysis/IIL2tE4n1Q0.json"
    },
    {
      "id": "OMGPvW8TBHc",
      "resource": "https://www.youtube.com/watch?v=OMGPvW8TBHc",
      "title": "Fuzzing in the GenAI Era — Leonard Tang, Haize Labs",
      "author": "Leonard Tang, Haize Labs",
      "last_modified": "2025-08-22T15:00:05Z",
      "analysis_file": "analysis/OMGPvW8TBHc.json"
    },
    {
      "id": "YZQsWVeN3rE",
      "resource": "https://www.youtube.com/watch?v=YZQsWVeN3rE",
      "title": "Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech",
      "author": "Alex Bauer, Upside.tech",
      "last_modified": "2026-07-11T00:57:36Z",
      "analysis_file": "analysis/YZQsWVeN3rE.json"
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

# Add task-specific criteria without replacing immutable global policy

## What

Add task-specific criteria without replacing immutable global policy

Task-specific rubrics expose idiosyncratic requirements that a generic score misses, while shared safety criteria remain fixed.

## Evidence

Source analysis [^IIL2tE4n1Q0]; no independently matched timestamped quote published.

> criteria. Right? So it's like instance specific rubric and then instance
> — 12:58 [^OMGPvW8TBHc]

> that inhabits each of the important personas and I can have them review
> — 12:06 [^YZQsWVeN3rE]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^IIL2tE4n1Q0]: [Judging LLMs: Alex Volkov](https://www.youtube.com/watch?v=IIL2tE4n1Q0); publication: 2024-09-09T18:39:17Z; analysis: `analysis/IIL2tE4n1Q0.json`.
[^OMGPvW8TBHc]: [Fuzzing in the GenAI Era — Leonard Tang, Haize Labs](https://www.youtube.com/watch?v=OMGPvW8TBHc); publication: 2025-08-22T15:00:05Z; analysis: `analysis/OMGPvW8TBHc.json`.
[^YZQsWVeN3rE]: [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](https://www.youtube.com/watch?v=YZQsWVeN3rE); publication: 2026-07-11T00:57:36Z; analysis: `analysis/YZQsWVeN3rE.json`.
