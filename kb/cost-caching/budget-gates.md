---
{
  "type": "technique",
  "id": "budget-gates",
  "title": "Apply deterministic task budgets tied to progress rather than arbitrary context restrictions",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-10-16T19:00:10Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "4uFVSLgD2Q4",
      "resource": "https://www.youtube.com/watch?v=4uFVSLgD2Q4",
      "title": "Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov",
      "author": "Gabe De Mesa, OpenGov",
      "last_modified": "2026-06-26T07:00:38Z",
      "analysis_file": "analysis/4uFVSLgD2Q4.json"
    },
    {
      "id": "8EQo4J2BWKw",
      "resource": "https://www.youtube.com/watch?v=8EQo4J2BWKw",
      "title": "Thinking Deeper in Gemini — Jack Rae, Google DeepMind",
      "author": "Jack Rae, Google DeepMind",
      "last_modified": "2025-07-10T16:00:06Z",
      "analysis_file": "analysis/8EQo4J2BWKw.json"
    },
    {
      "id": "8oyalrfwgjw",
      "resource": "https://www.youtube.com/watch?v=8oyalrfwgjw",
      "title": "RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI",
      "author": "Shashi, Superagentic AI",
      "last_modified": "2026-07-12T23:00:06Z",
      "analysis_file": "analysis/8oyalrfwgjw.json"
    },
    {
      "id": "BM2JX9hqsVQ",
      "resource": "https://www.youtube.com/watch?v=BM2JX9hqsVQ",
      "title": "What if the network was the sandbox? — Remy Guercio, Tailscale",
      "author": "Remy Guercio, Tailscale",
      "last_modified": "2026-06-01T15:00:31Z",
      "analysis_file": "analysis/BM2JX9hqsVQ.json"
    },
    {
      "id": "FB-MLPhL9Ms",
      "resource": "https://www.youtube.com/watch?v=FB-MLPhL9Ms",
      "title": "The maturity phases of running evals — Phil Hetzel, Braintrust",
      "author": "Phil Hetzel, Braintrust",
      "last_modified": "2026-05-27T13:00:06Z",
      "analysis_file": "analysis/FB-MLPhL9Ms.json"
    },
    {
      "id": "NW-jwOVr32w",
      "resource": "https://www.youtube.com/watch?v=NW-jwOVr32w",
      "title": "The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI",
      "author": "Jonathan Gordon, ReWeaver AI",
      "last_modified": "2026-09-10T14:30:11Z",
      "analysis_file": "analysis/NW-jwOVr32w.json"
    },
    {
      "id": "PwCSYy-oGsM",
      "resource": "https://www.youtube.com/watch?v=PwCSYy-oGsM",
      "title": "Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI",
      "author": "Druid AI",
      "last_modified": "2026-10-12T00:00:10Z",
      "analysis_file": "analysis/PwCSYy-oGsM.json"
    },
    {
      "id": "Rx8f05JI_WA",
      "resource": "https://www.youtube.com/watch?v=Rx8f05JI_WA",
      "title": "SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI",
      "author": "Rishi Desai, Abundant AI",
      "last_modified": "2026-07-07T03:45:51Z",
      "analysis_file": "analysis/Rx8f05JI_WA.json"
    },
    {
      "id": "Th5e4h-oVmc",
      "resource": "https://www.youtube.com/watch?v=Th5e4h-oVmc",
      "title": "Real AI Agents Need Planning, Not Just Prompting - Yuval Belfer",
      "author": "Yuval Belfer",
      "last_modified": "2025-06-03T22:22:27Z",
      "analysis_file": "analysis/Th5e4h-oVmc.json"
    },
    {
      "id": "UNzCG3lw6O0",
      "resource": "https://www.youtube.com/watch?v=UNzCG3lw6O0",
      "title": "Building Great Agent Skills: The Missing Manual",
      "author": null,
      "last_modified": "2026-06-29T18:53:10Z",
      "analysis_file": "analysis/UNzCG3lw6O0.json"
    },
    {
      "id": "VXfRt_H-V08",
      "resource": "https://www.youtube.com/watch?v=VXfRt_H-V08",
      "title": "One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca",
      "author": "Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca",
      "last_modified": "2026-04-10T11:30:06Z",
      "analysis_file": "analysis/VXfRt_H-V08.json"
    },
    {
      "id": "X4BwOu0GWb8",
      "resource": "https://www.youtube.com/watch?v=X4BwOu0GWb8",
      "title": "Your Coding Agent Just Got Cloned And Your Brain Isn't Ready - Rustin Banks, Google Jules",
      "author": "Rustin Banks, Google Jules",
      "last_modified": "2025-07-25T23:06:43Z",
      "analysis_file": "analysis/X4BwOu0GWb8.json"
    },
    {
      "id": "bZISsg7H7DA",
      "resource": "https://www.youtube.com/watch?v=bZISsg7H7DA",
      "title": "Your Agents Need a Save Button - Hamza Tahir, ZenML",
      "author": "Hamza Tahir, ZenML",
      "last_modified": "2026-07-18T07:00:06Z",
      "analysis_file": "analysis/bZISsg7H7DA.json"
    },
    {
      "id": "cf2IhzqeQH4",
      "resource": "https://www.youtube.com/watch?v=cf2IhzqeQH4",
      "title": "Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg",
      "author": "Dor Sasson, Stigg",
      "last_modified": "2026-10-07T00:30:28Z",
      "analysis_file": "analysis/cf2IhzqeQH4.json"
    },
    {
      "id": "ib-wTAvCZqg",
      "resource": "https://www.youtube.com/watch?v=ib-wTAvCZqg",
      "title": "Architecting and Testing Controllable Agents: Lance Martin",
      "author": null,
      "last_modified": "2024-10-11T18:57:05Z",
      "analysis_file": "analysis/ib-wTAvCZqg.json"
    },
    {
      "id": "kiClTcJUnhc",
      "resource": "https://www.youtube.com/watch?v=kiClTcJUnhc",
      "title": "Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic",
      "author": "CJ Avilla & Harrison Stall, Anthropic",
      "last_modified": "2026-10-16T19:00:10Z",
      "analysis_file": "analysis/kiClTcJUnhc.json"
    },
    {
      "id": "mJqwmmOx4WA",
      "resource": "https://www.youtube.com/watch?v=mJqwmmOx4WA",
      "title": "How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe",
      "author": "Andrew Garvin, Stripe",
      "last_modified": "2026-08-28T16:00:06Z",
      "analysis_file": "analysis/mJqwmmOx4WA.json"
    },
    {
      "id": "sl3icG-IjHo",
      "resource": "https://www.youtube.com/watch?v=sl3icG-IjHo",
      "title": "How to Build Planning Agents without losing control - Yogendra Miraje, Factset",
      "author": "Yogendra Miraje, Factset",
      "last_modified": "2025-07-23T15:51:06Z",
      "analysis_file": "analysis/sl3icG-IjHo.json"
    },
    {
      "id": "y2Drx0SDZLo",
      "resource": "https://www.youtube.com/watch?v=y2Drx0SDZLo",
      "title": "Agent Evals: Finally, With The Map",
      "author": null,
      "last_modified": "2025-02-22T19:00:31Z",
      "analysis_file": "analysis/y2Drx0SDZLo.json"
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

# Apply deterministic task budgets tied to progress rather than arbitrary context restrictions

## What

Apply deterministic task budgets tied to progress rather than arbitrary context restrictions

Limit loops and replans so repeated nonprogress cannot consume unlimited tokens.

## Evidence

Source analysis [^4uFVSLgD2Q4]; no independently matched timestamped quote published.

Source analysis [^8EQo4J2BWKw]; no independently matched timestamped quote published.

Source analysis [^8oyalrfwgjw]; no independently matched timestamped quote published.

Source analysis [^BM2JX9hqsVQ]; no independently matched timestamped quote published.

Source analysis [^FB-MLPhL9Ms]; no independently matched timestamped quote published.

> And with Ruby Weaver, there's zero extra token costs. So, we're fully local LLM,
> — 15:38 [^NW-jwOVr32w]

Source analysis [^PwCSYy-oGsM]; no independently matched timestamped quote published.

> 31 million tokens, and the longest rollout
> — 06:40 [^Rx8f05JI_WA]

Source analysis [^Th5e4h-oVmc]; no independently matched timestamped quote published.

Source analysis [^UNzCG3lw6O0]; no independently matched timestamped quote published.

Source analysis [^VXfRt_H-V08]; no independently matched timestamped quote published.

> a complex task, and saying, "Try it this way, try it that way, or give me this
> — 04:25 [^X4BwOu0GWb8]

> This can get very expensive of course and this is where you have to be really
> — 14:57 [^bZISsg7H7DA]

Source analysis [^cf2IhzqeQH4]; no independently matched timestamped quote published.

Source analysis [^ib-wTAvCZqg]; no independently matched timestamped quote published.

> component where any work that you've already accomplished is not thrown away
> — 39:48 [^kiClTcJUnhc]

Source analysis [^mJqwmmOx4WA]; no independently matched timestamped quote published.

> the user. Sometimes you also set some recussion
> — 06:16 [^sl3icG-IjHo]

> optimization the number of steps optimization and then moving to the what
> — 08:36 [^y2Drx0SDZLo]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^4uFVSLgD2Q4]: [Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](https://www.youtube.com/watch?v=4uFVSLgD2Q4); publication: 2026-06-26T07:00:38Z; analysis: `analysis/4uFVSLgD2Q4.json`.
[^8EQo4J2BWKw]: [Thinking Deeper in Gemini — Jack Rae, Google DeepMind](https://www.youtube.com/watch?v=8EQo4J2BWKw); publication: 2025-07-10T16:00:06Z; analysis: `analysis/8EQo4J2BWKw.json`.
[^8oyalrfwgjw]: [RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](https://www.youtube.com/watch?v=8oyalrfwgjw); publication: 2026-07-12T23:00:06Z; analysis: `analysis/8oyalrfwgjw.json`.
[^BM2JX9hqsVQ]: [What if the network was the sandbox? — Remy Guercio, Tailscale](https://www.youtube.com/watch?v=BM2JX9hqsVQ); publication: 2026-06-01T15:00:31Z; analysis: `analysis/BM2JX9hqsVQ.json`.
[^FB-MLPhL9Ms]: [The maturity phases of running evals — Phil Hetzel, Braintrust](https://www.youtube.com/watch?v=FB-MLPhL9Ms); publication: 2026-05-27T13:00:06Z; analysis: `analysis/FB-MLPhL9Ms.json`.
[^NW-jwOVr32w]: [The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI](https://www.youtube.com/watch?v=NW-jwOVr32w); publication: 2026-09-10T14:30:11Z; analysis: `analysis/NW-jwOVr32w.json`.
[^PwCSYy-oGsM]: [Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI](https://www.youtube.com/watch?v=PwCSYy-oGsM); publication: 2026-10-12T00:00:10Z; analysis: `analysis/PwCSYy-oGsM.json`.
[^Rx8f05JI_WA]: [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](https://www.youtube.com/watch?v=Rx8f05JI_WA); publication: 2026-07-07T03:45:51Z; analysis: `analysis/Rx8f05JI_WA.json`.
[^Th5e4h-oVmc]: [Real AI Agents Need Planning, Not Just Prompting - Yuval Belfer](https://www.youtube.com/watch?v=Th5e4h-oVmc); publication: 2025-06-03T22:22:27Z; analysis: `analysis/Th5e4h-oVmc.json`.
[^UNzCG3lw6O0]: [Building Great Agent Skills: The Missing Manual](https://www.youtube.com/watch?v=UNzCG3lw6O0); publication: 2026-06-29T18:53:10Z; analysis: `analysis/UNzCG3lw6O0.json`.
[^VXfRt_H-V08]: [One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca](https://www.youtube.com/watch?v=VXfRt_H-V08); publication: 2026-04-10T11:30:06Z; analysis: `analysis/VXfRt_H-V08.json`.
[^X4BwOu0GWb8]: [Your Coding Agent Just Got Cloned And Your Brain Isn't Ready - Rustin Banks, Google Jules](https://www.youtube.com/watch?v=X4BwOu0GWb8); publication: 2025-07-25T23:06:43Z; analysis: `analysis/X4BwOu0GWb8.json`.
[^bZISsg7H7DA]: [Your Agents Need a Save Button - Hamza Tahir, ZenML](https://www.youtube.com/watch?v=bZISsg7H7DA); publication: 2026-07-18T07:00:06Z; analysis: `analysis/bZISsg7H7DA.json`.
[^cf2IhzqeQH4]: [Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg](https://www.youtube.com/watch?v=cf2IhzqeQH4); publication: 2026-10-07T00:30:28Z; analysis: `analysis/cf2IhzqeQH4.json`.
[^ib-wTAvCZqg]: [Architecting and Testing Controllable Agents: Lance Martin](https://www.youtube.com/watch?v=ib-wTAvCZqg); publication: 2024-10-11T18:57:05Z; analysis: `analysis/ib-wTAvCZqg.json`.
[^kiClTcJUnhc]: [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc); publication: 2026-10-16T19:00:10Z; analysis: `analysis/kiClTcJUnhc.json`.
[^mJqwmmOx4WA]: [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](https://www.youtube.com/watch?v=mJqwmmOx4WA); publication: 2026-08-28T16:00:06Z; analysis: `analysis/mJqwmmOx4WA.json`.
[^sl3icG-IjHo]: [How to Build Planning Agents without losing control - Yogendra Miraje, Factset](https://www.youtube.com/watch?v=sl3icG-IjHo); publication: 2025-07-23T15:51:06Z; analysis: `analysis/sl3icG-IjHo.json`.
[^y2Drx0SDZLo]: [Agent Evals: Finally, With The Map](https://www.youtube.com/watch?v=y2Drx0SDZLo); publication: 2025-02-22T19:00:31Z; analysis: `analysis/y2Drx0SDZLo.json`.
