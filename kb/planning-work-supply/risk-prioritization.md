---
{
  "type": "technique",
  "id": "risk-prioritization",
  "title": "Prioritize failures by frequency, severity, novelty and real downstream cost",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-10-22T09:00:12Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "0tVu-V3_fFw",
      "resource": "https://www.youtube.com/watch?v=0tVu-V3_fFw",
      "title": "Designing AI To Scale Human Thought — Jun Yu Tan, Tusk",
      "author": "Jun Yu Tan, Tusk",
      "last_modified": "2025-06-03T07:00:06Z",
      "analysis_file": "analysis/0tVu-V3_fFw.json"
    },
    {
      "id": "L8OoYeDI_ls",
      "resource": "https://www.youtube.com/watch?v=L8OoYeDI_ls",
      "title": "Evals Are Not Unit Tests — Ido Pesok, Vercel v0",
      "author": "Ido Pesok, Vercel v0",
      "last_modified": "2025-08-06T16:14:42Z",
      "analysis_file": "analysis/L8OoYeDI_ls.json"
    },
    {
      "id": "SHMCGrNJJGc",
      "resource": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
      "title": "How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-17T19:00:23Z",
      "analysis_file": "analysis/SHMCGrNJJGc.json"
    },
    {
      "id": "dQ-_i1tZiws",
      "resource": "https://www.youtube.com/watch?v=dQ-_i1tZiws",
      "title": "Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk",
      "author": "Dmitry Buykin, Maersk",
      "last_modified": "2026-08-29T17:30:21Z",
      "analysis_file": "analysis/dQ-_i1tZiws.json"
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
      "id": "eSvXbb2EBYc",
      "resource": "https://www.youtube.com/watch?v=eSvXbb2EBYc",
      "title": "Building AI Products That Actually Work — Ben Hylak (Raindrop), Sid Bendre (Oleve)",
      "author": "Ben Hylak (Raindrop), Sid Bendre (Oleve)",
      "last_modified": "2025-07-24T17:15:06Z",
      "analysis_file": "analysis/eSvXbb2EBYc.json"
    },
    {
      "id": "kZsf_Sfm7RU",
      "resource": "https://www.youtube.com/watch?v=kZsf_Sfm7RU",
      "title": "The Missing Layer After Launch - Raphael Kalandadze, Wandero AI",
      "author": "Raphael Kalandadze, Wandero AI",
      "last_modified": "2026-07-05T03:15:05Z",
      "analysis_file": "analysis/kZsf_Sfm7RU.json"
    },
    {
      "id": "mMw3arwQsL0",
      "resource": "https://www.youtube.com/watch?v=mMw3arwQsL0",
      "title": "1,368 AI Failures and What They Teach About Evals — Vishal Srivastava & Tanmay Sah, New York Life",
      "author": "Vishal Srivastava & Tanmay Sah, New York Life",
      "last_modified": "2026-10-22T09:00:12Z",
      "analysis_file": "analysis/mMw3arwQsL0.json"
    },
    {
      "id": "qStB9GbppMU",
      "resource": "https://www.youtube.com/watch?v=qStB9GbppMU",
      "title": "1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI",
      "author": "Sumanyu Sharma, Hamming AI",
      "last_modified": "2026-09-15T15:00:06Z",
      "analysis_file": "analysis/qStB9GbppMU.json"
    },
    {
      "id": "wJwTlvb_TSo",
      "resource": "https://www.youtube.com/watch?v=wJwTlvb_TSo",
      "title": "WTF do people use Open Models for??",
      "author": null,
      "last_modified": "2025-02-22T20:00:06Z",
      "analysis_file": "analysis/wJwTlvb_TSo.json"
    },
    {
      "id": "xIt_mTQp6mY",
      "resource": "https://www.youtube.com/watch?v=xIt_mTQp6mY",
      "title": "Loop Engineering from First Principles — Kyle Mistele, HumanLayer",
      "author": "Kyle Mistele, HumanLayer",
      "last_modified": "2026-07-25T20:41:40Z",
      "analysis_file": "analysis/xIt_mTQp6mY.json"
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

# Prioritize failures by frequency, severity, novelty and real downstream cost

## What

Prioritize failures by frequency, severity, novelty and real downstream cost

Count categories but weight expected impact; rare dangerous failures outrank frequent cosmetic ones.

## Evidence

Source analysis [^0tVu-V3_fFw]; no independently matched timestamped quote published.

> really easy to tell, okay, maybe next week we need to prioritize uh the team
> — 08:59 [^L8OoYeDI_ls]

Source analysis [^SHMCGrNJJGc]; no independently matched timestamped quote published.

> It clusters the failures and hands back something you can act on. Not just look
> — 05:19 [^dQ-_i1tZiws]

> overall then on the fit data set you do this error analysis. So you really look
> — 06:03 [^eAXxdtNlK04]

Source analysis [^eSvXbb2EBYc]; no independently matched timestamped quote published.

Source analysis [^kZsf_Sfm7RU]; no independently matched timestamped quote published.

Source analysis [^mMw3arwQsL0]; no independently matched timestamped quote published.

Source analysis [^qStB9GbppMU]; no independently matched timestamped quote published.

Source analysis [^wJwTlvb_TSo]; no independently matched timestamped quote published.

> and figure out which procedures have the most errors or the least instrumentation
> — 12:05 [^xIt_mTQp6mY]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^0tVu-V3_fFw]: [Designing AI To Scale Human Thought — Jun Yu Tan, Tusk](https://www.youtube.com/watch?v=0tVu-V3_fFw); publication: 2025-06-03T07:00:06Z; analysis: `analysis/0tVu-V3_fFw.json`.
[^L8OoYeDI_ls]: [Evals Are Not Unit Tests — Ido Pesok, Vercel v0](https://www.youtube.com/watch?v=L8OoYeDI_ls); publication: 2025-08-06T16:14:42Z; analysis: `analysis/L8OoYeDI_ls.json`.
[^SHMCGrNJJGc]: [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=SHMCGrNJJGc); publication: 2026-10-17T19:00:23Z; analysis: `analysis/SHMCGrNJJGc.json`.
[^dQ-_i1tZiws]: [Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk](https://www.youtube.com/watch?v=dQ-_i1tZiws); publication: 2026-08-29T17:30:21Z; analysis: `analysis/dQ-_i1tZiws.json`.
[^eAXxdtNlK04]: [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=eAXxdtNlK04); publication: 2026-07-18T20:15:06Z; analysis: `analysis/eAXxdtNlK04.json`.
[^eSvXbb2EBYc]: [Building AI Products That Actually Work — Ben Hylak (Raindrop), Sid Bendre (Oleve)](https://www.youtube.com/watch?v=eSvXbb2EBYc); publication: 2025-07-24T17:15:06Z; analysis: `analysis/eSvXbb2EBYc.json`.
[^kZsf_Sfm7RU]: [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](https://www.youtube.com/watch?v=kZsf_Sfm7RU); publication: 2026-07-05T03:15:05Z; analysis: `analysis/kZsf_Sfm7RU.json`.
[^mMw3arwQsL0]: [1,368 AI Failures and What They Teach About Evals — Vishal Srivastava & Tanmay Sah, New York Life](https://www.youtube.com/watch?v=mMw3arwQsL0); publication: 2026-10-22T09:00:12Z; analysis: `analysis/mMw3arwQsL0.json`.
[^qStB9GbppMU]: [1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI](https://www.youtube.com/watch?v=qStB9GbppMU); publication: 2026-09-15T15:00:06Z; analysis: `analysis/qStB9GbppMU.json`.
[^wJwTlvb_TSo]: [WTF do people use Open Models for??](https://www.youtube.com/watch?v=wJwTlvb_TSo); publication: 2025-02-22T20:00:06Z; analysis: `analysis/wJwTlvb_TSo.json`.
[^xIt_mTQp6mY]: [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](https://www.youtube.com/watch?v=xIt_mTQp6mY); publication: 2026-07-25T20:41:40Z; analysis: `analysis/xIt_mTQp6mY.json`.
