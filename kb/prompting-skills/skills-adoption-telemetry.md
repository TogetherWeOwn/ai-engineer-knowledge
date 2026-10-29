---
{
  "type": "technique",
  "id": "skills-adoption-telemetry",
  "title": "Measure actual skill invocation, cost and outcomes rather than counting installed skills",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-08-22T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "4_VQBbs2iQA",
      "resource": "https://www.youtube.com/watch?v=4_VQBbs2iQA",
      "title": "How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom",
      "author": "Brian Scanlan, Intercom",
      "last_modified": "2026-05-15T13:00:06Z",
      "analysis_file": "analysis/4_VQBbs2iQA.json"
    },
    {
      "id": "JvosMkuNxF8",
      "resource": "https://www.youtube.com/watch?v=JvosMkuNxF8",
      "title": "Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford",
      "author": "Yegor Denisov-Blanch, Stanford",
      "last_modified": "2025-12-11T21:56:44Z",
      "analysis_file": "analysis/JvosMkuNxF8.json"
    },
    {
      "id": "h403btjldDQ",
      "resource": "https://www.youtube.com/watch?v=h403btjldDQ",
      "title": "Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa",
      "author": "Dotta Bippa",
      "last_modified": "2026-04-15T21:59:05Z",
      "analysis_file": "analysis/h403btjldDQ.json"
    },
    {
      "id": "zCJtYuqwm7E",
      "resource": "https://www.youtube.com/watch?v=zCJtYuqwm7E",
      "title": "Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl",
      "author": "Patrick Debois, Tessl",
      "last_modified": "2026-08-22T16:00:06Z",
      "analysis_file": "analysis/zCJtYuqwm7E.json"
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

# Measure actual skill invocation, cost and outcomes rather than counting installed skills

## What

Measure actual skill invocation, cost and outcomes rather than counting installed skills

A skill can be configured but not invoked or applied correctly. Inspect real run exposure and outcomes to find policy/materialization problems and ineffective instructions.

## Evidence

Source analysis [^4_VQBbs2iQA]; no independently matched timestamped quote published.

> use whereby teams are are sharing these kind of prompts and rules. And then
> — 07:10 [^JvosMkuNxF8]

Source analysis [^h403btjldDQ]; no independently matched timestamped quote published.

> explain me what happened. Why is this a good idea?" That's where you are testing
> — 16:36 [^zCJtYuqwm7E]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^4_VQBbs2iQA]: [How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom](https://www.youtube.com/watch?v=4_VQBbs2iQA); publication: 2026-05-15T13:00:06Z; analysis: `analysis/4_VQBbs2iQA.json`.
[^JvosMkuNxF8]: [Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford](https://www.youtube.com/watch?v=JvosMkuNxF8); publication: 2025-12-11T21:56:44Z; analysis: `analysis/JvosMkuNxF8.json`.
[^h403btjldDQ]: [Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa](https://www.youtube.com/watch?v=h403btjldDQ); publication: 2026-04-15T21:59:05Z; analysis: `analysis/h403btjldDQ.json`.
[^zCJtYuqwm7E]: [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](https://www.youtube.com/watch?v=zCJtYuqwm7E); publication: 2026-08-22T16:00:06Z; analysis: `analysis/zCJtYuqwm7E.json`.
