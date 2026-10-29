---
{
  "type": "technique",
  "id": "agent-registry",
  "title": "Discover agent capabilities through versioned machine-readable registry records",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-07T18:30:34Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "UOcHfR3_tys",
      "resource": "https://www.youtube.com/watch?v=UOcHfR3_tys",
      "title": "Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band",
      "author": "Vlad Luzin, Band",
      "last_modified": "2026-09-30T13:00:33Z",
      "analysis_file": "analysis/UOcHfR3_tys.json"
    },
    {
      "id": "W2HVdB4Jbjs",
      "resource": "https://www.youtube.com/watch?v=W2HVdB4Jbjs",
      "title": "Architecting Agent Memory: Principles, Patterns, and Best Practices — Richmond Alake, MongoDB",
      "author": "Richmond Alake, MongoDB",
      "last_modified": "2025-06-27T09:56:46Z",
      "analysis_file": "analysis/W2HVdB4Jbjs.json"
    },
    {
      "id": "fz6-NS7qpZc",
      "resource": "https://www.youtube.com/watch?v=fz6-NS7qpZc",
      "title": "How I Learned to Stop Worrying and Love the Sandbox — Matt Brockman, E2B",
      "author": "Matt Brockman, E2B",
      "last_modified": "2026-10-05T18:00:17Z",
      "analysis_file": "analysis/fz6-NS7qpZc.json"
    },
    {
      "id": "q-WOjZhOMCA",
      "resource": "https://www.youtube.com/watch?v=q-WOjZhOMCA",
      "title": "IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork",
      "author": "Sarthak Aggarwal, Decawork",
      "last_modified": "2026-08-20T14:30:38Z",
      "analysis_file": "analysis/q-WOjZhOMCA.json"
    },
    {
      "id": "toq-jyGLZDk",
      "resource": "https://www.youtube.com/watch?v=toq-jyGLZDk",
      "title": "Why Your AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND",
      "author": "Vlad Luzin, BAND",
      "last_modified": "2026-10-07T18:30:34Z",
      "analysis_file": "analysis/toq-jyGLZDk.json"
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

# Discover agent capabilities through versioned machine-readable registry records

## What

Discover agent capabilities through versioned machine-readable registry records

Store agent information such as tools, persona, and capabilities in an agent registry so the system can reason about available agents.

## Evidence

> agent, programmatic registration and onboarding and agent card appears.
> — 10:06 [^UOcHfR3_tys]

> contact request sent to my personal assistant to require bilateral consent.
> — 10:32 [^UOcHfR3_tys]

Source analysis [^W2HVdB4Jbjs]; no independently matched timestamped quote published.

Source analysis [^fz6-NS7qpZc]; no independently matched timestamped quote published.

Source analysis [^q-WOjZhOMCA]; no independently matched timestamped quote published.

Source analysis [^toq-jyGLZDk]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^UOcHfR3_tys]: [Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band](https://www.youtube.com/watch?v=UOcHfR3_tys); publication: 2026-09-30T13:00:33Z; analysis: `analysis/UOcHfR3_tys.json`.
[^W2HVdB4Jbjs]: [Architecting Agent Memory: Principles, Patterns, and Best Practices — Richmond Alake, MongoDB](https://www.youtube.com/watch?v=W2HVdB4Jbjs); publication: 2025-06-27T09:56:46Z; analysis: `analysis/W2HVdB4Jbjs.json`.
[^fz6-NS7qpZc]: [How I Learned to Stop Worrying and Love the Sandbox — Matt Brockman, E2B](https://www.youtube.com/watch?v=fz6-NS7qpZc); publication: 2026-10-05T18:00:17Z; analysis: `analysis/fz6-NS7qpZc.json`.
[^q-WOjZhOMCA]: [IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork](https://www.youtube.com/watch?v=q-WOjZhOMCA); publication: 2026-08-20T14:30:38Z; analysis: `analysis/q-WOjZhOMCA.json`.
[^toq-jyGLZDk]: [Why Your AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND](https://www.youtube.com/watch?v=toq-jyGLZDk); publication: 2026-10-07T18:30:34Z; analysis: `analysis/toq-jyGLZDk.json`.
