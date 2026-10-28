---
{
  "type": "technique",
  "id": "decision-changing-questions",
  "title": "Ask only clarifications that change a material decision; otherwise document a reversible assumption",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-10-11T22:00:02Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "L173Z8DpaJg",
      "resource": "https://www.youtube.com/watch?v=L173Z8DpaJg",
      "title": "The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp",
      "author": "Safia Abdalla, Warp",
      "last_modified": "2026-08-22T17:30:13Z",
      "analysis_file": "analysis/L173Z8DpaJg.json"
    },
    {
      "id": "_ehJyfHg1Vk",
      "resource": "https://www.youtube.com/watch?v=_ehJyfHg1Vk",
      "title": "The Era of Compound Engineering — Kieran Klaassen, Every/Cora",
      "author": "Kieran Klaassen, Every/Cora",
      "last_modified": "2026-08-20T15:00:06Z",
      "analysis_file": "analysis/_ehJyfHg1Vk.json"
    },
    {
      "id": "iheWKg2Tkrk",
      "resource": "https://www.youtube.com/watch?v=iheWKg2Tkrk",
      "title": "Ship Production Software in Minutes, Not Months — Eno Reyes, Factory",
      "author": "Eno Reyes, Factory",
      "last_modified": "2025-07-25T23:11:00Z",
      "analysis_file": "analysis/iheWKg2Tkrk.json"
    },
    {
      "id": "tyFPqtyOK5w",
      "resource": "https://www.youtube.com/watch?v=tyFPqtyOK5w",
      "title": "The Autonomous Computer: Infrastructure for Computer Use Agents — Ang Li, Simular",
      "author": "Ang Li, Simular",
      "last_modified": "2026-10-11T22:00:02Z",
      "analysis_file": "analysis/tyFPqtyOK5w.json"
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

# Ask only clarifications that change a material decision; otherwise document a reversible assumption

## What

Ask only clarifications that change a material decision; otherwise document a reversible assumption

Question volume is not progress; stop asking when further answers are unlikely to change the plan.

## Evidence

Source analysis [^L173Z8DpaJg]; no independently matched timestamped quote published.

> the goal is not to answer questions. In the end, it's to get the absolute best
> — 14:11 [^_ehJyfHg1Vk]

Source analysis [^iheWKg2Tkrk]; no independently matched timestamped quote published.

Source analysis [^tyFPqtyOK5w]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^L173Z8DpaJg]: [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](https://www.youtube.com/watch?v=L173Z8DpaJg); publication: 2026-08-22T17:30:13Z; analysis: `analysis/L173Z8DpaJg.json`.
[^_ehJyfHg1Vk]: [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](https://www.youtube.com/watch?v=_ehJyfHg1Vk); publication: 2026-08-20T15:00:06Z; analysis: `analysis/_ehJyfHg1Vk.json`.
[^iheWKg2Tkrk]: [Ship Production Software in Minutes, Not Months — Eno Reyes, Factory](https://www.youtube.com/watch?v=iheWKg2Tkrk); publication: 2025-07-25T23:11:00Z; analysis: `analysis/iheWKg2Tkrk.json`.
[^tyFPqtyOK5w]: [The Autonomous Computer: Infrastructure for Computer Use Agents — Ang Li, Simular](https://www.youtube.com/watch?v=tyFPqtyOK5w); publication: 2026-10-11T22:00:02Z; analysis: `analysis/tyFPqtyOK5w.json`.
