---
{
  "type": "technique",
  "id": "slo-error-budgets",
  "title": "Define service and agent SLOs with actionable thresholds",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-10-21T08:00:37Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-a2oTS9J67U",
      "resource": "https://www.youtube.com/watch?v=-a2oTS9J67U",
      "title": "The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale",
      "author": "Michele Grant, Leading at Scale",
      "last_modified": "2026-10-13T16:00:11Z",
      "analysis_file": "analysis/-a2oTS9J67U.json"
    },
    {
      "id": "EY4O9M6AsWI",
      "resource": "https://www.youtube.com/watch?v=EY4O9M6AsWI",
      "title": "Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI",
      "author": "Keegan McCallum, Luma AI",
      "last_modified": "2025-07-19T17:45:06Z",
      "analysis_file": "analysis/EY4O9M6AsWI.json"
    },
    {
      "id": "Emo5FGGY-wM",
      "resource": "https://www.youtube.com/watch?v=Emo5FGGY-wM",
      "title": "Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab",
      "author": "Felipe Blanes, Amazon AGI Lab",
      "last_modified": "2026-10-09T00:30:02Z",
      "analysis_file": "analysis/Emo5FGGY-wM.json"
    },
    {
      "id": "G7aSH6N7qY4",
      "resource": "https://www.youtube.com/watch?v=G7aSH6N7qY4",
      "title": "AI + Security & Safety — Don Bosco Durai",
      "author": "Don Bosco Durai",
      "last_modified": "2025-04-19T16:00:06Z",
      "analysis_file": "analysis/G7aSH6N7qY4.json"
    },
    {
      "id": "NTBX-wxUhHs",
      "resource": "https://www.youtube.com/watch?v=NTBX-wxUhHs",
      "title": "Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA",
      "author": "Val Bercovici, WEKA",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/NTBX-wxUhHs.json"
    },
    {
      "id": "O72p-rBb2bA",
      "resource": "https://www.youtube.com/watch?v=O72p-rBb2bA",
      "title": "Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind",
      "author": "Akele Reed & Dave Revere, SonderMind",
      "last_modified": "2026-07-25T23:00:36Z",
      "analysis_file": "analysis/O72p-rBb2bA.json"
    },
    {
      "id": "OqM67QG_Ikk",
      "resource": "https://www.youtube.com/watch?v=OqM67QG_Ikk",
      "title": "From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI",
      "author": "Abhishek Bhardwaj, OpenAI",
      "last_modified": "2026-07-13T17:00:06Z",
      "analysis_file": "analysis/OqM67QG_Ikk.json"
    },
    {
      "id": "_-oIuRH4oGA",
      "resource": "https://www.youtube.com/watch?v=_-oIuRH4oGA",
      "title": "How agents broke app-level infrastructure - Evan Boyle",
      "author": "Evan Boyle",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/_-oIuRH4oGA.json"
    },
    {
      "id": "_Zcw_sVF6hU",
      "resource": "https://www.youtube.com/watch?v=_Zcw_sVF6hU",
      "title": "The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "author": "Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "last_modified": "2026-04-18T10:30:06Z",
      "analysis_file": "analysis/_Zcw_sVF6hU.json"
    },
    {
      "id": "bDQn1w0idXs",
      "resource": "https://www.youtube.com/watch?v=bDQn1w0idXs",
      "title": "The AI Pivot: With Chris White of Prefect & Bryan Bischof of Hex",
      "author": null,
      "last_modified": "2023-11-07T19:45:58Z",
      "analysis_file": "analysis/bDQn1w0idXs.json"
    },
    {
      "id": "bI8WyG9YB0I",
      "resource": "https://www.youtube.com/watch?v=bI8WyG9YB0I",
      "title": "SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar",
      "author": "Killian Carlsen-Phelan, Sonar",
      "last_modified": "2026-10-11T19:00:11Z",
      "analysis_file": "analysis/bI8WyG9YB0I.json"
    },
    {
      "id": "bSG9wUYaHWU",
      "resource": "https://www.youtube.com/watch?v=bSG9wUYaHWU",
      "title": "Context Is the New Code — Patrick Debois, Tessl",
      "author": "Patrick Debois, Tessl",
      "last_modified": "2026-05-03T14:00:06Z",
      "analysis_file": "analysis/bSG9wUYaHWU.json"
    },
    {
      "id": "d5EltXhbcfA",
      "resource": "https://www.youtube.com/watch?v=d5EltXhbcfA",
      "title": "Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil",
      "author": "Sayash Kapoor, AI Snake Oil",
      "last_modified": "2025-04-17T16:00:06Z",
      "analysis_file": "analysis/d5EltXhbcfA.json"
    },
    {
      "id": "fOtTHWeU6B8",
      "resource": "https://www.youtube.com/watch?v=fOtTHWeU6B8",
      "title": "How Zapier Builds AI Products and Features with the Help of Braintrust: Ankur Goyal & Olmo Maldonado",
      "author": null,
      "last_modified": "2024-11-07T20:11:02Z",
      "analysis_file": "analysis/fOtTHWeU6B8.json"
    },
    {
      "id": "pPvoLjYj_mY",
      "resource": "https://www.youtube.com/watch?v=pPvoLjYj_mY",
      "title": "Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer",
      "author": "Waseem Alshikh, Writer",
      "last_modified": "2025-04-22T16:00:06Z",
      "analysis_file": "analysis/pPvoLjYj_mY.json"
    },
    {
      "id": "u825uxb7LnA",
      "resource": "https://www.youtube.com/watch?v=u825uxb7LnA",
      "title": "The Coherence Trap: Why LLMs Feel Smart (But Aren’t Thinking) - Travis Frisinger",
      "author": "Travis Frisinger",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/u825uxb7LnA.json"
    },
    {
      "id": "uA4ah-dVHvU",
      "resource": "https://www.youtube.com/watch?v=uA4ah-dVHvU",
      "title": "AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard",
      "author": "Gareth Yoder, Vanguard",
      "last_modified": "2026-10-21T08:00:37Z",
      "analysis_file": "analysis/uA4ah-dVHvU.json"
    },
    {
      "id": "vljxQZfJ9wY",
      "resource": "https://www.youtube.com/watch?v=vljxQZfJ9wY",
      "title": "Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs",
      "author": "Nishant Gupta, Meta Superintelligence Labs",
      "last_modified": "2026-06-25T18:15:06Z",
      "analysis_file": "analysis/vljxQZfJ9wY.json"
    },
    {
      "id": "zrZ1amZBSPw",
      "resource": "https://www.youtube.com/watch?v=zrZ1amZBSPw",
      "title": "Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio",
      "author": "Kanish Manuja, Twilio",
      "last_modified": "2026-08-28T15:30:03Z",
      "analysis_file": "analysis/zrZ1amZBSPw.json"
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

# Define service and agent SLOs with actionable thresholds

## What

Define service and agent SLOs with actionable thresholds

Intentional reliability constraints force decisions about criticality and operational capacity.

## Evidence

Source analysis [^-a2oTS9J67U]; no independently matched timestamped quote published.

Source analysis [^EY4O9M6AsWI]; no independently matched timestamped quote published.

Source analysis [^Emo5FGGY-wM]; no independently matched timestamped quote published.

Source analysis [^G7aSH6N7qY4]; no independently matched timestamped quote published.

Source analysis [^NTBX-wxUhHs]; no independently matched timestamped quote published.

Source analysis [^O72p-rBb2bA]; no independently matched timestamped quote published.

> factors, right? So, if nodes are dying or failing, it won't choose that. It
> — 42:11 [^OqM67QG_Ikk]

Source analysis [^_-oIuRH4oGA]; no independently matched timestamped quote published.

> SLOs are great system that is intentionally designed to put friction
> — 17:38 [^_Zcw_sVF6hU]

Source analysis [^bDQn1w0idXs]; no independently matched timestamped quote published.

Source analysis [^bI8WyG9YB0I]; no independently matched timestamped quote published.

> work or not. I find it personally helpful to think
> — 13:24 [^bSG9wUYaHWU]

> rather than just a modeling problem where you need to work around the
> — 17:43 [^d5EltXhbcfA]

> that we run it we want to make sure that if any regressions happen that we act on
> — 07:05 [^fOtTHWeU6B8]

Source analysis [^pPvoLjYj_mY]; no independently matched timestamped quote published.

Source analysis [^u825uxb7LnA]; no independently matched timestamped quote published.

Source analysis [^uA4ah-dVHvU]; no independently matched timestamped quote published.

> determines scalability. Recovery rate reflects resilience.
> — 06:57 [^vljxQZfJ9wY]

> can actually decentralize the gateway and still centralize government
> — 15:02 [^zrZ1amZBSPw]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-a2oTS9J67U]: [The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale](https://www.youtube.com/watch?v=-a2oTS9J67U); publication: 2026-10-13T16:00:11Z; analysis: `analysis/-a2oTS9J67U.json`.
[^EY4O9M6AsWI]: [Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI](https://www.youtube.com/watch?v=EY4O9M6AsWI); publication: 2025-07-19T17:45:06Z; analysis: `analysis/EY4O9M6AsWI.json`.
[^Emo5FGGY-wM]: [Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab](https://www.youtube.com/watch?v=Emo5FGGY-wM); publication: 2026-10-09T00:30:02Z; analysis: `analysis/Emo5FGGY-wM.json`.
[^G7aSH6N7qY4]: [AI + Security & Safety — Don Bosco Durai](https://www.youtube.com/watch?v=G7aSH6N7qY4); publication: 2025-04-19T16:00:06Z; analysis: `analysis/G7aSH6N7qY4.json`.
[^NTBX-wxUhHs]: [Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA](https://www.youtube.com/watch?v=NTBX-wxUhHs); publication: 2025-11-24T20:16:36Z; analysis: `analysis/NTBX-wxUhHs.json`.
[^O72p-rBb2bA]: [Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind](https://www.youtube.com/watch?v=O72p-rBb2bA); publication: 2026-07-25T23:00:36Z; analysis: `analysis/O72p-rBb2bA.json`.
[^OqM67QG_Ikk]: [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=OqM67QG_Ikk); publication: 2026-07-13T17:00:06Z; analysis: `analysis/OqM67QG_Ikk.json`.
[^_-oIuRH4oGA]: [How agents broke app-level infrastructure - Evan Boyle](https://www.youtube.com/watch?v=_-oIuRH4oGA); publication: 2025-06-03T22:22:28Z; analysis: `analysis/_-oIuRH4oGA.json`.
[^_Zcw_sVF6hU]: [The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil](https://www.youtube.com/watch?v=_Zcw_sVF6hU); publication: 2026-04-18T10:30:06Z; analysis: `analysis/_Zcw_sVF6hU.json`.
[^bDQn1w0idXs]: [The AI Pivot: With Chris White of Prefect & Bryan Bischof of Hex](https://www.youtube.com/watch?v=bDQn1w0idXs); publication: 2023-11-07T19:45:58Z; analysis: `analysis/bDQn1w0idXs.json`.
[^bI8WyG9YB0I]: [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](https://www.youtube.com/watch?v=bI8WyG9YB0I); publication: 2026-10-11T19:00:11Z; analysis: `analysis/bI8WyG9YB0I.json`.
[^bSG9wUYaHWU]: [Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU); publication: 2026-05-03T14:00:06Z; analysis: `analysis/bSG9wUYaHWU.json`.
[^d5EltXhbcfA]: [Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil](https://www.youtube.com/watch?v=d5EltXhbcfA); publication: 2025-04-17T16:00:06Z; analysis: `analysis/d5EltXhbcfA.json`.
[^fOtTHWeU6B8]: [How Zapier Builds AI Products and Features with the Help of Braintrust: Ankur Goyal & Olmo Maldonado](https://www.youtube.com/watch?v=fOtTHWeU6B8); publication: 2024-11-07T20:11:02Z; analysis: `analysis/fOtTHWeU6B8.json`.
[^pPvoLjYj_mY]: [Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer](https://www.youtube.com/watch?v=pPvoLjYj_mY); publication: 2025-04-22T16:00:06Z; analysis: `analysis/pPvoLjYj_mY.json`.
[^u825uxb7LnA]: [The Coherence Trap: Why LLMs Feel Smart (But Aren’t Thinking) - Travis Frisinger](https://www.youtube.com/watch?v=u825uxb7LnA); publication: 2025-06-03T22:22:29Z; analysis: `analysis/u825uxb7LnA.json`.
[^uA4ah-dVHvU]: [AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard](https://www.youtube.com/watch?v=uA4ah-dVHvU); publication: 2026-10-21T08:00:37Z; analysis: `analysis/uA4ah-dVHvU.json`.
[^vljxQZfJ9wY]: [Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs](https://www.youtube.com/watch?v=vljxQZfJ9wY); publication: 2026-06-25T18:15:06Z; analysis: `analysis/vljxQZfJ9wY.json`.
[^zrZ1amZBSPw]: [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](https://www.youtube.com/watch?v=zrZ1amZBSPw); publication: 2026-08-28T15:30:03Z; analysis: `analysis/zrZ1amZBSPw.json`.
