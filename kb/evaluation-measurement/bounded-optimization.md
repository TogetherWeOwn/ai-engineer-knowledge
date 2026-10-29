---
{
  "type": "technique",
  "id": "bounded-optimization",
  "title": "Keep optimization proposals behind a fixed objective, holdout and rollback",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-12T06:07:42Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-cKUW6n8hBU",
      "resource": "https://www.youtube.com/watch?v=-cKUW6n8hBU",
      "title": "DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners",
      "author": "Kevin Madura, AlixPartners",
      "last_modified": "2026-01-08T20:48:21Z",
      "analysis_file": "analysis/-cKUW6n8hBU.json"
    },
    {
      "id": "1P1hJ36rxM0",
      "resource": "https://www.youtube.com/watch?v=1P1hJ36rxM0",
      "title": "\"Software engineering is not about writing code\" — Benoit Schillings, Google DeepMind VP of Research",
      "author": "Benoit Schillings, Google DeepMind VP of Research",
      "last_modified": "2026-07-17T15:24:44Z",
      "analysis_file": "analysis/1P1hJ36rxM0.json"
    },
    {
      "id": "7RFJRDYroic",
      "resource": "https://www.youtube.com/watch?v=7RFJRDYroic",
      "title": "Parameter Golf with AutoResearch — Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI",
      "author": "Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI",
      "last_modified": "2026-10-11T21:00:16Z",
      "analysis_file": "analysis/7RFJRDYroic.json"
    },
    {
      "id": "GqoNrUz8hEU",
      "resource": "https://www.youtube.com/watch?v=GqoNrUz8hEU",
      "title": "Bringing agents onto the world wide web — Paul Klein IV, Browserbase",
      "author": "Paul Klein IV, Browserbase",
      "last_modified": "2026-08-14T15:00:31Z",
      "analysis_file": "analysis/GqoNrUz8hEU.json"
    },
    {
      "id": "IAdZxqjZ45U",
      "resource": "https://www.youtube.com/watch?v=IAdZxqjZ45U",
      "title": "Optimizing LLMs in Insurance with DSPy: Jeronim Morina",
      "author": null,
      "last_modified": "2025-02-16T17:15:06Z",
      "analysis_file": "analysis/IAdZxqjZ45U.json"
    },
    {
      "id": "JomVvNDjGb8",
      "resource": "https://www.youtube.com/watch?v=JomVvNDjGb8",
      "title": "Your Coding Agent Should Do AI System Engineering — Ben Burtenshaw, Hugging Face",
      "author": "Ben Burtenshaw, Hugging Face",
      "last_modified": "2026-05-21T13:00:06Z",
      "analysis_file": "analysis/JomVvNDjGb8.json"
    },
    {
      "id": "KA5kPbdkK2E",
      "resource": "https://www.youtube.com/watch?v=KA5kPbdkK2E",
      "title": "How Lovable self-improves every hour — Benjamin Verbeek, Lovable",
      "author": "Benjamin Verbeek, Lovable",
      "last_modified": "2026-06-02T16:00:33Z",
      "analysis_file": "analysis/KA5kPbdkK2E.json"
    },
    {
      "id": "L173Z8DpaJg",
      "resource": "https://www.youtube.com/watch?v=L173Z8DpaJg",
      "title": "The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp",
      "author": "Safia Abdalla, Warp",
      "last_modified": "2026-08-22T17:30:13Z",
      "analysis_file": "analysis/L173Z8DpaJg.json"
    },
    {
      "id": "McknwOzbmyg",
      "resource": "https://www.youtube.com/watch?v=McknwOzbmyg",
      "title": "Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia",
      "author": "Jared Joselowitz, Ufonia",
      "last_modified": "2026-08-19T15:00:31Z",
      "analysis_file": "analysis/McknwOzbmyg.json"
    },
    {
      "id": "NuePCNMpWGc",
      "resource": "https://www.youtube.com/watch?v=NuePCNMpWGc",
      "title": "Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar",
      "author": "Prasenjit Sarkar, Sonar",
      "last_modified": "2026-05-31T18:00:21Z",
      "analysis_file": "analysis/NuePCNMpWGc.json"
    },
    {
      "id": "OA-Mc60Rboo",
      "resource": "https://www.youtube.com/watch?v=OA-Mc60Rboo",
      "title": "Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA",
      "author": "Lakshya A. Agrawal, GEPA",
      "last_modified": "2026-09-26T17:00:06Z",
      "analysis_file": "analysis/OA-Mc60Rboo.json"
    },
    {
      "id": "PbHm2qKnu10",
      "resource": "https://www.youtube.com/watch?v=PbHm2qKnu10",
      "title": "Training Agentic Reasoners — Will Brown, Prime Intellect",
      "author": "Will Brown, Prime Intellect",
      "last_modified": "2025-07-07T17:20:54Z",
      "analysis_file": "analysis/PbHm2qKnu10.json"
    },
    {
      "id": "R30col3UPUg",
      "resource": "https://www.youtube.com/watch?v=R30col3UPUg",
      "title": "Building Applications with AI Agents — Michael Albada, Microsoft",
      "author": "Michael Albada, Microsoft",
      "last_modified": "2025-07-24T15:00:53Z",
      "analysis_file": "analysis/R30col3UPUg.json"
    },
    {
      "id": "RGSFUqzqErE",
      "resource": "https://www.youtube.com/watch?v=RGSFUqzqErE",
      "title": "On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft",
      "author": "Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft",
      "last_modified": "2026-07-17T16:30:06Z",
      "analysis_file": "analysis/RGSFUqzqErE.json"
    },
    {
      "id": "SbcQYbrvAfI",
      "resource": "https://www.youtube.com/watch?v=SbcQYbrvAfI",
      "title": "Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize",
      "author": "SallyAnn DeLucia & Fuad Ali, Arize",
      "last_modified": "2026-01-06T17:30:06Z",
      "analysis_file": "analysis/SbcQYbrvAfI.json"
    },
    {
      "id": "TeErpYBUIeM",
      "resource": "https://www.youtube.com/watch?v=TeErpYBUIeM",
      "title": "The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse",
      "author": "Marc Klingen, Langfuse",
      "last_modified": "2026-10-06T17:00:19Z",
      "analysis_file": "analysis/TeErpYBUIeM.json"
    },
    {
      "id": "V-L0INGTEOg",
      "resource": "https://www.youtube.com/watch?v=V-L0INGTEOg",
      "title": "Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs",
      "author": "Boris Starkov, Eleven Labs",
      "last_modified": "2026-05-29T14:00:06Z",
      "analysis_file": "analysis/V-L0INGTEOg.json"
    },
    {
      "id": "X4dEHRzBLmc",
      "resource": "https://www.youtube.com/watch?v=X4dEHRzBLmc",
      "title": "Judge the Judge: Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI",
      "author": "Mahmoud Mabrouk, Agenta AI",
      "last_modified": "2026-04-10T10:00:06Z",
      "analysis_file": "analysis/X4dEHRzBLmc.json"
    },
    {
      "id": "XLEYtv3cMlw",
      "resource": "https://www.youtube.com/watch?v=XLEYtv3cMlw",
      "title": "Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait",
      "author": "Sina Shahandeh, Radicait",
      "last_modified": "2026-07-18T23:30:06Z",
      "analysis_file": "analysis/XLEYtv3cMlw.json"
    },
    {
      "id": "_BRhRh7mOX0",
      "resource": "https://www.youtube.com/watch?v=_BRhRh7mOX0",
      "title": "Prompt Engineering and AI Red Teaming — Sander Schulhoff, HackAPrompt/LearnPrompting",
      "author": "Sander Schulhoff, HackAPrompt/LearnPrompting",
      "last_modified": "2025-07-14T19:00:11Z",
      "analysis_file": "analysis/_BRhRh7mOX0.json"
    },
    {
      "id": "aHhB3sjGjkI",
      "resource": "https://www.youtube.com/watch?v=aHhB3sjGjkI",
      "title": "Agents Building Agents - Alfonso Graziano, Nearform",
      "author": "Alfonso Graziano, Nearform",
      "last_modified": "2026-06-28T16:00:34Z",
      "analysis_file": "analysis/aHhB3sjGjkI.json"
    },
    {
      "id": "bMjlRrWjdT0",
      "resource": "https://www.youtube.com/watch?v=bMjlRrWjdT0",
      "title": "AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "author": "Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "last_modified": "2026-08-28T15:00:03Z",
      "analysis_file": "analysis/bMjlRrWjdT0.json"
    },
    {
      "id": "bbq0b_FpYEY",
      "resource": "https://www.youtube.com/watch?v=bbq0b_FpYEY",
      "title": "Rust is the language of the AGI - Michael Yuan",
      "author": "Michael Yuan",
      "last_modified": "2025-06-03T22:22:27Z",
      "analysis_file": "analysis/bbq0b_FpYEY.json"
    },
    {
      "id": "bdHaOXZOhcM",
      "resource": "https://www.youtube.com/watch?v=bdHaOXZOhcM",
      "title": "Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company",
      "author": "Hursh Agrawal, The Browser Company",
      "last_modified": "2026-08-20T14:00:21Z",
      "analysis_file": "analysis/bdHaOXZOhcM.json"
    },
    {
      "id": "eAXxdtNlK04",
      "resource": "https://www.youtube.com/watch?v=eAXxdtNlK04",
      "title": "Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse",
      "author": "Annabell Schäfer, Langfuse",
      "last_modified": "2026-07-18T20:15:06Z",
      "analysis_file": "analysis/eAXxdtNlK04.json"
    },
    {
      "id": "g4SsanB0gMc",
      "resource": "https://www.youtube.com/watch?v=g4SsanB0gMc",
      "title": "Large clusters for small models — Daniel Svonava, Superlinked",
      "author": "Daniel Svonava, Superlinked",
      "last_modified": "2026-09-19T17:30:33Z",
      "analysis_file": "analysis/g4SsanB0gMc.json"
    },
    {
      "id": "jvKf6zXrNO4",
      "resource": "https://www.youtube.com/watch?v=jvKf6zXrNO4",
      "title": "Prompt Engineering is Dead — Nir Gazit, Traceloop",
      "author": "Nir Gazit, Traceloop",
      "last_modified": "2025-06-27T09:34:55Z",
      "analysis_file": "analysis/jvKf6zXrNO4.json"
    },
    {
      "id": "kiqubc5b5Yo",
      "resource": "https://www.youtube.com/watch?v=kiqubc5b5Yo",
      "title": "Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo",
      "author": "Brendan Rappazzo",
      "last_modified": "2026-07-29T17:06:26Z",
      "analysis_file": "analysis/kiqubc5b5Yo.json"
    },
    {
      "id": "o4scJaQgnFA",
      "resource": "https://www.youtube.com/watch?v=o4scJaQgnFA",
      "title": "From Arc to Dia: Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York",
      "author": "Samir Mody, The Browser Company of New York",
      "last_modified": "2025-12-19T18:15:46Z",
      "analysis_file": "analysis/o4scJaQgnFA.json"
    },
    {
      "id": "p7gaxmCUiIU",
      "resource": "https://www.youtube.com/watch?v=p7gaxmCUiIU",
      "title": "Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase",
      "author": "Shubhankar Srivastava, Browserbase",
      "last_modified": "2026-10-11T21:30:05Z",
      "analysis_file": "analysis/p7gaxmCUiIU.json"
    },
    {
      "id": "qJtcEDc_WJU",
      "resource": "https://www.youtube.com/watch?v=qJtcEDc_WJU",
      "title": "Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T06:07:42Z",
      "analysis_file": "analysis/qJtcEDc_WJU.json"
    },
    {
      "id": "ro5HkZvzfiQ",
      "resource": "https://www.youtube.com/watch?v=ro5HkZvzfiQ",
      "title": "The LLM Triangle: Engineering Principles for Robust AI Applications - Almog Baku:",
      "author": "Almog Baku:",
      "last_modified": "2025-02-22T15:00:06Z",
      "analysis_file": "analysis/ro5HkZvzfiQ.json"
    },
    {
      "id": "sOB3HSiG8vo",
      "resource": "https://www.youtube.com/watch?v=sOB3HSiG8vo",
      "title": "Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI",
      "author": "Qianru Lao & Lu Zhang, OpenAI",
      "last_modified": "2026-09-19T15:30:04Z",
      "analysis_file": "analysis/sOB3HSiG8vo.json"
    },
    {
      "id": "tzRvcTEapzo",
      "resource": "https://www.youtube.com/watch?v=tzRvcTEapzo",
      "title": "From Mixture of Experts to Mixture of Agents with Super Fast Inference - Daniel Kim & Daria Soboleva",
      "author": "Daniel Kim & Daria Soboleva",
      "last_modified": "2025-06-27T10:38:41Z",
      "analysis_file": "analysis/tzRvcTEapzo.json"
    },
    {
      "id": "vrDvatGtIxs",
      "resource": "https://www.youtube.com/watch?v=vrDvatGtIxs",
      "title": "Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph",
      "author": "Tejas Bhakta, Morph",
      "last_modified": "2026-09-26T15:00:32Z",
      "analysis_file": "analysis/vrDvatGtIxs.json"
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

# Keep optimization proposals behind a fixed objective, holdout and rollback

## What

Keep optimization proposals behind a fixed objective, holdout and rollback

A failure-driven optimizer proposes prompt variants and retains a Pareto frontier under a fixed search budget.

## Evidence

Source analysis [^-cKUW6n8hBU]; no independently matched timestamped quote published.

Source analysis [^1P1hJ36rxM0]; no independently matched timestamped quote published.

Source analysis [^7RFJRDYroic]; no independently matched timestamped quote published.

Source analysis [^GqoNrUz8hEU]; no independently matched timestamped quote published.

Source analysis [^IAdZxqjZ45U]; no independently matched timestamped quote published.

Source analysis [^JomVvNDjGb8]; no independently matched timestamped quote published.

> That they actually finish a project. This is a very very strong signal that
> — 11:21 [^KA5kPbdkK2E]

Source analysis [^L173Z8DpaJg]; no independently matched timestamped quote published.

> to reflect on the failures and update the prompt automatically. You do this
> — 12:28 [^McknwOzbmyg]

> any issues or not. If there is an issues, it is going to discard it. We
> — 13:51 [^NuePCNMpWGc]

> agent harness is eventually just a Python or a JavaScript file and we can
> — 10:49 [^OA-Mc60Rboo]

Source analysis [^PbHm2qKnu10]; no independently matched timestamped quote published.

> judge. So it can look at your failures and automatically suggest changes back
> — 12:21 [^R30col3UPUg]

Source analysis [^RGSFUqzqErE]; no independently matched timestamped quote published.

Source analysis [^SbcQYbrvAfI]; no independently matched timestamped quote published.

Source analysis [^TeErpYBUIeM]; no independently matched timestamped quote published.

Source analysis [^V-L0INGTEOg]; no independently matched timestamped quote published.

Source analysis [^X4dEHRzBLmc]; no independently matched timestamped quote published.

> around with problems that it knows but it wouldn't do a very radical change. uh
> — 06:08 [^XLEYtv3cMlw]

> here. Some of them not necessarily um a quantitative but qualitative and also
> — 14:05 [^XLEYtv3cMlw]

Source analysis [^_BRhRh7mOX0]; no independently matched timestamped quote published.

Source analysis [^aHhB3sjGjkI]; no independently matched timestamped quote published.

Source analysis [^bMjlRrWjdT0]; no independently matched timestamped quote published.

Source analysis [^bbq0b_FpYEY]; no independently matched timestamped quote published.

> you need to do to get these scores to go up. And obviously with this kind of
> — 12:27 [^bdHaOXZOhcM]

Source analysis [^eAXxdtNlK04]; no independently matched timestamped quote published.

Source analysis [^g4SsanB0gMc]; no independently matched timestamped quote published.

Source analysis [^jvKf6zXrNO4]; no independently matched timestamped quote published.

> looking at the about, you know, the results, and improving the harness
> — 17:23 [^kiqubc5b5Yo]

Source analysis [^o4scJaQgnFA]; no independently matched timestamped quote published.

> uh there's like failures happening after there have been successes right uh so
> — 24:29 [^p7gaxmCUiIU]

Source analysis [^qJtcEDc_WJU]; no independently matched timestamped quote published.

> going to take you time start with the big model collect data understand what's
> — 19:10 [^ro5HkZvzfiQ]

Source analysis [^sOB3HSiG8vo]; no independently matched timestamped quote published.

Source analysis [^tzRvcTEapzo]; no independently matched timestamped quote published.

Source analysis [^vrDvatGtIxs]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-cKUW6n8hBU]: [DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](https://www.youtube.com/watch?v=-cKUW6n8hBU); publication: 2026-01-08T20:48:21Z; analysis: `analysis/-cKUW6n8hBU.json`.
[^1P1hJ36rxM0]: ["Software engineering is not about writing code" — Benoit Schillings, Google DeepMind VP of Research](https://www.youtube.com/watch?v=1P1hJ36rxM0); publication: 2026-07-17T15:24:44Z; analysis: `analysis/1P1hJ36rxM0.json`.
[^7RFJRDYroic]: [Parameter Golf with AutoResearch — Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI](https://www.youtube.com/watch?v=7RFJRDYroic); publication: 2026-10-11T21:00:16Z; analysis: `analysis/7RFJRDYroic.json`.
[^GqoNrUz8hEU]: [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](https://www.youtube.com/watch?v=GqoNrUz8hEU); publication: 2026-08-14T15:00:31Z; analysis: `analysis/GqoNrUz8hEU.json`.
[^IAdZxqjZ45U]: [Optimizing LLMs in Insurance with DSPy: Jeronim Morina](https://www.youtube.com/watch?v=IAdZxqjZ45U); publication: 2025-02-16T17:15:06Z; analysis: `analysis/IAdZxqjZ45U.json`.
[^JomVvNDjGb8]: [Your Coding Agent Should Do AI System Engineering — Ben Burtenshaw, Hugging Face](https://www.youtube.com/watch?v=JomVvNDjGb8); publication: 2026-05-21T13:00:06Z; analysis: `analysis/JomVvNDjGb8.json`.
[^KA5kPbdkK2E]: [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](https://www.youtube.com/watch?v=KA5kPbdkK2E); publication: 2026-06-02T16:00:33Z; analysis: `analysis/KA5kPbdkK2E.json`.
[^L173Z8DpaJg]: [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](https://www.youtube.com/watch?v=L173Z8DpaJg); publication: 2026-08-22T17:30:13Z; analysis: `analysis/L173Z8DpaJg.json`.
[^McknwOzbmyg]: [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](https://www.youtube.com/watch?v=McknwOzbmyg); publication: 2026-08-19T15:00:31Z; analysis: `analysis/McknwOzbmyg.json`.
[^NuePCNMpWGc]: [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](https://www.youtube.com/watch?v=NuePCNMpWGc); publication: 2026-05-31T18:00:21Z; analysis: `analysis/NuePCNMpWGc.json`.
[^OA-Mc60Rboo]: [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](https://www.youtube.com/watch?v=OA-Mc60Rboo); publication: 2026-09-26T17:00:06Z; analysis: `analysis/OA-Mc60Rboo.json`.
[^PbHm2qKnu10]: [Training Agentic Reasoners — Will Brown, Prime Intellect](https://www.youtube.com/watch?v=PbHm2qKnu10); publication: 2025-07-07T17:20:54Z; analysis: `analysis/PbHm2qKnu10.json`.
[^R30col3UPUg]: [Building Applications with AI Agents — Michael Albada, Microsoft](https://www.youtube.com/watch?v=R30col3UPUg); publication: 2025-07-24T15:00:53Z; analysis: `analysis/R30col3UPUg.json`.
[^RGSFUqzqErE]: [On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft](https://www.youtube.com/watch?v=RGSFUqzqErE); publication: 2026-07-17T16:30:06Z; analysis: `analysis/RGSFUqzqErE.json`.
[^SbcQYbrvAfI]: [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](https://www.youtube.com/watch?v=SbcQYbrvAfI); publication: 2026-01-06T17:30:06Z; analysis: `analysis/SbcQYbrvAfI.json`.
[^TeErpYBUIeM]: [The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](https://www.youtube.com/watch?v=TeErpYBUIeM); publication: 2026-10-06T17:00:19Z; analysis: `analysis/TeErpYBUIeM.json`.
[^V-L0INGTEOg]: [Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs](https://www.youtube.com/watch?v=V-L0INGTEOg); publication: 2026-05-29T14:00:06Z; analysis: `analysis/V-L0INGTEOg.json`.
[^X4dEHRzBLmc]: [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI](https://www.youtube.com/watch?v=X4dEHRzBLmc); publication: 2026-04-10T10:00:06Z; analysis: `analysis/X4dEHRzBLmc.json`.
[^XLEYtv3cMlw]: [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](https://www.youtube.com/watch?v=XLEYtv3cMlw); publication: 2026-07-18T23:30:06Z; analysis: `analysis/XLEYtv3cMlw.json`.
[^_BRhRh7mOX0]: [Prompt Engineering and AI Red Teaming — Sander Schulhoff, HackAPrompt/LearnPrompting](https://www.youtube.com/watch?v=_BRhRh7mOX0); publication: 2025-07-14T19:00:11Z; analysis: `analysis/_BRhRh7mOX0.json`.
[^aHhB3sjGjkI]: [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI); publication: 2026-06-28T16:00:34Z; analysis: `analysis/aHhB3sjGjkI.json`.
[^bMjlRrWjdT0]: [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](https://www.youtube.com/watch?v=bMjlRrWjdT0); publication: 2026-08-28T15:00:03Z; analysis: `analysis/bMjlRrWjdT0.json`.
[^bbq0b_FpYEY]: [Rust is the language of the AGI - Michael Yuan](https://www.youtube.com/watch?v=bbq0b_FpYEY); publication: 2025-06-03T22:22:27Z; analysis: `analysis/bbq0b_FpYEY.json`.
[^bdHaOXZOhcM]: [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](https://www.youtube.com/watch?v=bdHaOXZOhcM); publication: 2026-08-20T14:00:21Z; analysis: `analysis/bdHaOXZOhcM.json`.
[^eAXxdtNlK04]: [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=eAXxdtNlK04); publication: 2026-07-18T20:15:06Z; analysis: `analysis/eAXxdtNlK04.json`.
[^g4SsanB0gMc]: [Large clusters for small models — Daniel Svonava, Superlinked](https://www.youtube.com/watch?v=g4SsanB0gMc); publication: 2026-09-19T17:30:33Z; analysis: `analysis/g4SsanB0gMc.json`.
[^jvKf6zXrNO4]: [Prompt Engineering is Dead — Nir Gazit, Traceloop](https://www.youtube.com/watch?v=jvKf6zXrNO4); publication: 2025-06-27T09:34:55Z; analysis: `analysis/jvKf6zXrNO4.json`.
[^kiqubc5b5Yo]: [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](https://www.youtube.com/watch?v=kiqubc5b5Yo); publication: 2026-07-29T17:06:26Z; analysis: `analysis/kiqubc5b5Yo.json`.
[^o4scJaQgnFA]: [From Arc to Dia: Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York](https://www.youtube.com/watch?v=o4scJaQgnFA); publication: 2025-12-19T18:15:46Z; analysis: `analysis/o4scJaQgnFA.json`.
[^p7gaxmCUiIU]: [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](https://www.youtube.com/watch?v=p7gaxmCUiIU); publication: 2026-10-11T21:30:05Z; analysis: `analysis/p7gaxmCUiIU.json`.
[^qJtcEDc_WJU]: [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](https://www.youtube.com/watch?v=qJtcEDc_WJU); publication: 2026-10-12T06:07:42Z; analysis: `analysis/qJtcEDc_WJU.json`.
[^ro5HkZvzfiQ]: [The LLM Triangle: Engineering Principles for Robust AI Applications - Almog Baku:](https://www.youtube.com/watch?v=ro5HkZvzfiQ); publication: 2025-02-22T15:00:06Z; analysis: `analysis/ro5HkZvzfiQ.json`.
[^sOB3HSiG8vo]: [Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI](https://www.youtube.com/watch?v=sOB3HSiG8vo); publication: 2026-09-19T15:30:04Z; analysis: `analysis/sOB3HSiG8vo.json`.
[^tzRvcTEapzo]: [From Mixture of Experts to Mixture of Agents with Super Fast Inference - Daniel Kim & Daria Soboleva](https://www.youtube.com/watch?v=tzRvcTEapzo); publication: 2025-06-27T10:38:41Z; analysis: `analysis/tzRvcTEapzo.json`.
[^vrDvatGtIxs]: [Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph](https://www.youtube.com/watch?v=vrDvatGtIxs); publication: 2026-09-26T15:00:32Z; analysis: `analysis/vrDvatGtIxs.json`.
