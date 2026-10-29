---
{
  "type": "technique",
  "id": "deterministic-early-exits",
  "title": "Exit deterministic no-change and invalid-prerequisite cases before invoking reasoning",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-17T19:00:23Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "SHMCGrNJJGc",
      "resource": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
      "title": "How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-17T19:00:23Z",
      "analysis_file": "analysis/SHMCGrNJJGc.json"
    },
    {
      "id": "_cVfz88_j7A",
      "resource": "https://www.youtube.com/watch?v=_cVfz88_j7A",
      "title": "Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs",
      "author": "Anant Shankhdhar, Risa Labs",
      "last_modified": "2026-07-20T06:24:47Z",
      "analysis_file": "analysis/_cVfz88_j7A.json"
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

# Exit deterministic no-change and invalid-prerequisite cases before invoking reasoning

## What

Exit deterministic no-change and invalid-prerequisite cases before invoking reasoning

Evaluate hard eligibility and preconditions first, stopping invalid work without an LLM.

## Evidence

Source analysis [^SHMCGrNJJGc]; no independently matched timestamped quote published.

> Agents only for the rules that where what rules can't decide.
> — 16:07 [^_cVfz88_j7A]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^SHMCGrNJJGc]: [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=SHMCGrNJJGc); publication: 2026-10-17T19:00:23Z; analysis: `analysis/SHMCGrNJJGc.json`.
[^_cVfz88_j7A]: [Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs](https://www.youtube.com/watch?v=_cVfz88_j7A); publication: 2026-07-20T06:24:47Z; analysis: `analysis/_cVfz88_j7A.json`.
