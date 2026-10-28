---
{
  "type": "technique",
  "id": "local-distillation",
  "title": "Distill task-specific behavior only from validated traces with a maintenance case",
  "area": "memory-learning",
  "status": "stable",
  "valid_from": "2026-10-11T21:30:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-TiET_K-E_g",
      "resource": "https://www.youtube.com/watch?v=-TiET_K-E_g",
      "title": "From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google",
      "author": "Cormac Brick, Google",
      "last_modified": "2026-05-20T13:00:06Z",
      "analysis_file": "analysis/-TiET_K-E_g.json"
    },
    {
      "id": "2Wtq2GvUicw",
      "resource": "https://www.youtube.com/watch?v=2Wtq2GvUicw",
      "title": "LLM Quality Optimization Bootcamp: Thierry Moreau and Pedro Torruella",
      "author": null,
      "last_modified": "2025-02-08T21:32:17Z",
      "analysis_file": "analysis/2Wtq2GvUicw.json"
    },
    {
      "id": "42q8OmAF_Gw",
      "resource": "https://www.youtube.com/watch?v=42q8OmAF_Gw",
      "title": "What It Actually Takes to Deploy GenAI Applications to Enterprises: Arjun Bansal and Trey Doig",
      "author": null,
      "last_modified": "2024-11-04T20:48:26Z",
      "analysis_file": "analysis/42q8OmAF_Gw.json"
    },
    {
      "id": "4loPnxvWWhg",
      "resource": "https://www.youtube.com/watch?v=4loPnxvWWhg",
      "title": "Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End",
      "author": "Dan Bjornn, Lease End",
      "last_modified": "2026-08-20T16:00:22Z",
      "analysis_file": "analysis/4loPnxvWWhg.json"
    },
    {
      "id": "71V3fTaUp2Q",
      "resource": "https://www.youtube.com/watch?v=71V3fTaUp2Q",
      "title": "Let LLMs Wander: Engineering RL Environments — Stefano Fiorucci",
      "author": "Stefano Fiorucci",
      "last_modified": "2026-04-08T06:15:06Z",
      "analysis_file": "analysis/71V3fTaUp2Q.json"
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
      "id": "ACPEpji5NV4",
      "resource": "https://www.youtube.com/watch?v=ACPEpji5NV4",
      "title": "Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash",
      "author": "Raghav Saboo, DoorDash",
      "last_modified": "2026-09-25T13:30:37Z",
      "analysis_file": "analysis/ACPEpji5NV4.json"
    },
    {
      "id": "BKWpYIWvAo4",
      "resource": "https://www.youtube.com/watch?v=BKWpYIWvAo4",
      "title": "TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google",
      "author": "Cormac Brick, Google",
      "last_modified": "2026-05-03T22:00:06Z",
      "analysis_file": "analysis/BKWpYIWvAo4.json"
    },
    {
      "id": "EUHx5ooJHuQ",
      "resource": "https://www.youtube.com/watch?v=EUHx5ooJHuQ",
      "title": "How Coding Agents change Software Development Forever - Hailong Zhang",
      "author": "Hailong Zhang",
      "last_modified": "2025-02-22T16:00:06Z",
      "analysis_file": "analysis/EUHx5ooJHuQ.json"
    },
    {
      "id": "IJXjTLPzvAU",
      "resource": "https://www.youtube.com/watch?v=IJXjTLPzvAU",
      "title": "The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen",
      "author": "Jacob E. Thomas, Results Gen",
      "last_modified": "2026-06-25T16:30:06Z",
      "analysis_file": "analysis/IJXjTLPzvAU.json"
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
      "id": "N7b1PJc7SFc",
      "resource": "https://www.youtube.com/watch?v=N7b1PJc7SFc",
      "title": "Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI",
      "author": "Rishabh Bhargava, Together AI",
      "last_modified": "2026-05-31T16:00:06Z",
      "analysis_file": "analysis/N7b1PJc7SFc.json"
    },
    {
      "id": "Nqb7JTx0Pqo",
      "resource": "https://www.youtube.com/watch?v=Nqb7JTx0Pqo",
      "title": "MCP Agent Fine tuning Workshop - Ronan McGovern",
      "author": "Ronan McGovern",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/Nqb7JTx0Pqo.json"
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
      "id": "PjaVHm_3Ljg",
      "resource": "https://www.youtube.com/watch?v=PjaVHm_3Ljg",
      "title": "Transforming search and discovery using LLMs — Tejaswi & Vinesh, Instacart",
      "author": "Tejaswi & Vinesh, Instacart",
      "last_modified": "2025-07-16T18:01:03Z",
      "analysis_file": "analysis/PjaVHm_3Ljg.json"
    },
    {
      "id": "Sjfz1TqxzEs",
      "resource": "https://www.youtube.com/watch?v=Sjfz1TqxzEs",
      "title": "Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics",
      "author": "Jason Ma, Dyna Robotics",
      "last_modified": "2026-09-24T14:30:12Z",
      "analysis_file": "analysis/Sjfz1TqxzEs.json"
    },
    {
      "id": "VZzUhELgYk4",
      "resource": "https://www.youtube.com/watch?v=VZzUhELgYk4",
      "title": "The Devops Engineer Who Never Sleeps — Diamond Bishop, Datadog",
      "author": "Diamond Bishop, Datadog",
      "last_modified": "2025-04-22T16:00:06Z",
      "analysis_file": "analysis/VZzUhELgYk4.json"
    },
    {
      "id": "VhPfM_aGBVc",
      "resource": "https://www.youtube.com/watch?v=VhPfM_aGBVc",
      "title": "Anthropic in the Enterprise — Alexander Bricken & Joe Bayley",
      "author": "Alexander Bricken & Joe Bayley",
      "last_modified": "2025-04-13T16:00:06Z",
      "analysis_file": "analysis/VhPfM_aGBVc.json"
    },
    {
      "id": "XdAWgO11zuk",
      "resource": "https://www.youtube.com/watch?v=XdAWgO11zuk",
      "title": "What We Learned from Using LLMs in Pinterest — Mukuntha Narayanan, Han Wang, Pinterest",
      "author": "Mukuntha Narayanan, Han Wang, Pinterest",
      "last_modified": "2025-07-16T17:58:25Z",
      "analysis_file": "analysis/XdAWgO11zuk.json"
    },
    {
      "id": "YZHPEkfy2kc",
      "resource": "https://www.youtube.com/watch?v=YZHPEkfy2kc",
      "title": "$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpintero",
      "author": "Diego Carpintero",
      "last_modified": "2026-04-16T11:00:07Z",
      "analysis_file": "analysis/YZHPEkfy2kc.json"
    },
    {
      "id": "YnNF55QV0zs",
      "resource": "https://www.youtube.com/watch?v=YnNF55QV0zs",
      "title": "Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai",
      "author": "Ishan Anand, InsightSciences.ai",
      "last_modified": "2026-07-29T20:15:35Z",
      "analysis_file": "analysis/YnNF55QV0zs.json"
    },
    {
      "id": "_IzZWeuTx7I",
      "resource": "https://www.youtube.com/watch?v=_IzZWeuTx7I",
      "title": "RL Environments at Scale – Will Brown, Prime Intellect",
      "author": "Will Brown, Prime Intellect",
      "last_modified": "2025-12-09T15:53:42Z",
      "analysis_file": "analysis/_IzZWeuTx7I.json"
    },
    {
      "id": "_KFbT6eph5A",
      "resource": "https://www.youtube.com/watch?v=_KFbT6eph5A",
      "title": "Using AI to Build an Infinite Game: Jeff Schomay",
      "author": null,
      "last_modified": "2024-02-01T17:41:28Z",
      "analysis_file": "analysis/_KFbT6eph5A.json"
    },
    {
      "id": "_zl_zimMRak",
      "resource": "https://www.youtube.com/watch?v=_zl_zimMRak",
      "title": "How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit",
      "author": "Jaspreet Singh, Intuit",
      "last_modified": "2025-07-23T15:51:31Z",
      "analysis_file": "analysis/_zl_zimMRak.json"
    },
    {
      "id": "atwSCxWFVMg",
      "resource": "https://www.youtube.com/watch?v=atwSCxWFVMg",
      "title": "GPT Web App Generator - 10,000 apps created in a month: Matija Sosic",
      "author": "10,000 apps created in a month: Matija Sosic",
      "last_modified": "2024-01-26T20:51:42Z",
      "analysis_file": "analysis/atwSCxWFVMg.json"
    },
    {
      "id": "b_PmGocP4rc",
      "resource": "https://www.youtube.com/watch?v=b_PmGocP4rc",
      "title": "Evaling Video Slop — Maor Bril, Character.ai",
      "author": "Maor Bril, Character.ai",
      "last_modified": "2026-07-25T00:00:02Z",
      "analysis_file": "analysis/b_PmGocP4rc.json"
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
      "id": "cwjs1WAG9CM",
      "resource": "https://www.youtube.com/watch?v=cwjs1WAG9CM",
      "title": "Building Context-Aware Reasoning Applications with LangChain and LangSmith: Harrison Chase",
      "author": null,
      "last_modified": "2023-11-01T15:15:07Z",
      "analysis_file": "analysis/cwjs1WAG9CM.json"
    },
    {
      "id": "eLXF0VojuSs",
      "resource": "https://www.youtube.com/watch?v=eLXF0VojuSs",
      "title": "How to Construct Domain Specific LLM Evaluation Systems: Hamel Husain and Emil Sedgh",
      "author": null,
      "last_modified": "2024-09-19T16:47:24Z",
      "analysis_file": "analysis/eLXF0VojuSs.json"
    },
    {
      "id": "fLUtUkqYHnQ",
      "resource": "https://www.youtube.com/watch?v=fLUtUkqYHnQ",
      "title": "Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI",
      "author": "Maxime Labonne, Liquid AI",
      "last_modified": "2026-04-29T12:00:06Z",
      "analysis_file": "analysis/fLUtUkqYHnQ.json"
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
      "id": "hxFpUcvWPcU",
      "resource": "https://www.youtube.com/watch?v=hxFpUcvWPcU",
      "title": "How to build Enterprise Aware Agents - Chau Tran, Glean",
      "author": "Chau Tran, Glean",
      "last_modified": "2025-07-24T09:22:32Z",
      "analysis_file": "analysis/hxFpUcvWPcU.json"
    },
    {
      "id": "jNE8No-wvok",
      "resource": "https://www.youtube.com/watch?v=jNE8No-wvok",
      "title": "Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta",
      "author": "Aditya Gautam, Meta",
      "last_modified": "2026-09-23T14:00:34Z",
      "analysis_file": "analysis/jNE8No-wvok.json"
    },
    {
      "id": "jtzh-GBXBWc",
      "resource": "https://www.youtube.com/watch?v=jtzh-GBXBWc",
      "title": "The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft",
      "author": "Rushabh Doshi, Machinecraft",
      "last_modified": "2026-07-11T20:00:27Z",
      "analysis_file": "analysis/jtzh-GBXBWc.json"
    },
    {
      "id": "kwnCvA9l-TY",
      "resource": "https://www.youtube.com/watch?v=kwnCvA9l-TY",
      "title": "AI Frontiers in Trust and Safety  Combatting Multifaceted Harm on Tinder at Scale: Vibhor Kumar",
      "author": null,
      "last_modified": "2024-12-02T20:37:40Z",
      "analysis_file": "analysis/kwnCvA9l-TY.json"
    },
    {
      "id": "l0FLhNqBOic",
      "resource": "https://www.youtube.com/watch?v=l0FLhNqBOic",
      "title": "AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents",
      "author": "Vasuman Moza, Varick Agents",
      "last_modified": "2026-07-28T21:00:06Z",
      "analysis_file": "analysis/l0FLhNqBOic.json"
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
      "id": "phchDt63qAA",
      "resource": "https://www.youtube.com/watch?v=phchDt63qAA",
      "title": "How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed",
      "author": "Ben Kunkle, Zed",
      "last_modified": "2026-05-30T16:00:06Z",
      "analysis_file": "analysis/phchDt63qAA.json"
    },
    {
      "id": "wcUJWP6WpGM",
      "resource": "https://www.youtube.com/watch?v=wcUJWP6WpGM",
      "title": "SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius",
      "author": "Ibragim Badertdinov, Nebius",
      "last_modified": "2026-06-04T14:00:06Z",
      "analysis_file": "analysis/wcUJWP6WpGM.json"
    },
    {
      "id": "zM9RYqCcioM",
      "resource": "https://www.youtube.com/watch?v=zM9RYqCcioM",
      "title": "Finetuning: 500m AI agents in production with 2 engineers — Mustafa Ali & Kyle Corbitt",
      "author": "Mustafa Ali & Kyle Corbitt",
      "last_modified": "2025-04-12T16:00:06Z",
      "analysis_file": "analysis/zM9RYqCcioM.json"
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

# Distill task-specific behavior only from validated traces with a maintenance case

## What

Distill task-specific behavior only from validated traces with a maintenance case

A compact task-specific model can learn a stable labeled decision that otherwise requires a committee of costly evaluators.

## Evidence

Source analysis [^-TiET_K-E_g]; no independently matched timestamped quote published.

Source analysis [^2Wtq2GvUicw]; no independently matched timestamped quote published.

Source analysis [^42q8OmAF_Gw]; no independently matched timestamped quote published.

Source analysis [^4loPnxvWWhg]; no independently matched timestamped quote published.

Source analysis [^71V3fTaUp2Q]; no independently matched timestamped quote published.

Source analysis [^8EQo4J2BWKw]; no independently matched timestamped quote published.

Source analysis [^ACPEpji5NV4]; no independently matched timestamped quote published.

Source analysis [^BKWpYIWvAo4]; no independently matched timestamped quote published.

Source analysis [^EUHx5ooJHuQ]; no independently matched timestamped quote published.

Source analysis [^IJXjTLPzvAU]; no independently matched timestamped quote published.

> of kind of evaluations and then trained a model to replicate this panel of
> — 01:24 [^JvosMkuNxF8]

Source analysis [^N7b1PJc7SFc]; no independently matched timestamped quote published.

Source analysis [^Nqb7JTx0Pqo]; no independently matched timestamped quote published.

Source analysis [^PbHm2qKnu10]; no independently matched timestamped quote published.

Source analysis [^PjaVHm_3Ljg]; no independently matched timestamped quote published.

Source analysis [^Sjfz1TqxzEs]; no independently matched timestamped quote published.

> you should be at a point where you can easily try out any of these models um
> — 13:45 [^VZzUhELgYk4]

> fine tuning is not a silver bullet so it comes at a cost and most people aren't
> — 17:58 [^VhPfM_aGBVc]

Source analysis [^XdAWgO11zuk]; no independently matched timestamped quote published.

> And in this manner, we managed to reach around 70% memory savings.
> — 35:56 [^YZHPEkfy2kc]

Source analysis [^YnNF55QV0zs]; no independently matched timestamped quote published.

Source analysis [^_IzZWeuTx7I]; no independently matched timestamped quote published.

Source analysis [^_KFbT6eph5A]; no independently matched timestamped quote published.

Source analysis [^_zl_zimMRak]; no independently matched timestamped quote published.

Source analysis [^atwSCxWFVMg]; no independently matched timestamped quote published.

> take all these committee of experts and distill it into one small model that is
> — 07:59 [^b_PmGocP4rc]

> night. So uh this is an example of a modern BERT PII classifier we trained.
> — 13:30 [^bdHaOXZOhcM]

Source analysis [^cwjs1WAG9CM]; no independently matched timestamped quote published.

> showed with that application and you can start to curate data for fine tuning and
> — 11:07 [^eLXF0VojuSs]

Source analysis [^fLUtUkqYHnQ]; no independently matched timestamped quote published.

Source analysis [^g4SsanB0gMc]; no independently matched timestamped quote published.

> time or like across different users. um dynamic prompting with search is better
> — 15:35 [^hxFpUcvWPcU]

Source analysis [^jNE8No-wvok]; no independently matched timestamped quote published.

> We never trained a model. No GPUs humming in the basement, no fine-tuning.
> — 02:48 [^jtzh-GBXBWc]

Source analysis [^kwnCvA9l-TY]; no independently matched timestamped quote published.

> are trying to do a long analysis, frontier models are extremely verbose,
> — 16:27 [^l0FLhNqBOic]

> probably run is like maybe $30 $40 if it's super complicated $100 at most. Uh
> — 28:21 [^p7gaxmCUiIU]

Source analysis [^phchDt63qAA]; no independently matched timestamped quote published.

Source analysis [^wcUJWP6WpGM]; no independently matched timestamped quote published.

Source analysis [^zM9RYqCcioM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated investigation
- **Speed:** Faster reuse of relevant prior work
- **Quality:** More current, scoped lessons
- **Reliability:** Less stale, conflicting or unsupported recall
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-TiET_K-E_g]: [From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google](https://www.youtube.com/watch?v=-TiET_K-E_g); publication: 2026-05-20T13:00:06Z; analysis: `analysis/-TiET_K-E_g.json`.
[^2Wtq2GvUicw]: [LLM Quality Optimization Bootcamp: Thierry Moreau and Pedro Torruella](https://www.youtube.com/watch?v=2Wtq2GvUicw); publication: 2025-02-08T21:32:17Z; analysis: `analysis/2Wtq2GvUicw.json`.
[^42q8OmAF_Gw]: [What It Actually Takes to Deploy GenAI Applications to Enterprises: Arjun Bansal and Trey Doig](https://www.youtube.com/watch?v=42q8OmAF_Gw); publication: 2024-11-04T20:48:26Z; analysis: `analysis/42q8OmAF_Gw.json`.
[^4loPnxvWWhg]: [Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End](https://www.youtube.com/watch?v=4loPnxvWWhg); publication: 2026-08-20T16:00:22Z; analysis: `analysis/4loPnxvWWhg.json`.
[^71V3fTaUp2Q]: [Let LLMs Wander: Engineering RL Environments — Stefano Fiorucci](https://www.youtube.com/watch?v=71V3fTaUp2Q); publication: 2026-04-08T06:15:06Z; analysis: `analysis/71V3fTaUp2Q.json`.
[^8EQo4J2BWKw]: [Thinking Deeper in Gemini — Jack Rae, Google DeepMind](https://www.youtube.com/watch?v=8EQo4J2BWKw); publication: 2025-07-10T16:00:06Z; analysis: `analysis/8EQo4J2BWKw.json`.
[^ACPEpji5NV4]: [Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash](https://www.youtube.com/watch?v=ACPEpji5NV4); publication: 2026-09-25T13:30:37Z; analysis: `analysis/ACPEpji5NV4.json`.
[^BKWpYIWvAo4]: [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google](https://www.youtube.com/watch?v=BKWpYIWvAo4); publication: 2026-05-03T22:00:06Z; analysis: `analysis/BKWpYIWvAo4.json`.
[^EUHx5ooJHuQ]: [How Coding Agents change Software Development Forever - Hailong Zhang](https://www.youtube.com/watch?v=EUHx5ooJHuQ); publication: 2025-02-22T16:00:06Z; analysis: `analysis/EUHx5ooJHuQ.json`.
[^IJXjTLPzvAU]: [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen](https://www.youtube.com/watch?v=IJXjTLPzvAU); publication: 2026-06-25T16:30:06Z; analysis: `analysis/IJXjTLPzvAU.json`.
[^JvosMkuNxF8]: [Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford](https://www.youtube.com/watch?v=JvosMkuNxF8); publication: 2025-12-11T21:56:44Z; analysis: `analysis/JvosMkuNxF8.json`.
[^N7b1PJc7SFc]: [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](https://www.youtube.com/watch?v=N7b1PJc7SFc); publication: 2026-05-31T16:00:06Z; analysis: `analysis/N7b1PJc7SFc.json`.
[^Nqb7JTx0Pqo]: [MCP Agent Fine tuning Workshop - Ronan McGovern](https://www.youtube.com/watch?v=Nqb7JTx0Pqo); publication: 2025-06-03T22:22:28Z; analysis: `analysis/Nqb7JTx0Pqo.json`.
[^PbHm2qKnu10]: [Training Agentic Reasoners — Will Brown, Prime Intellect](https://www.youtube.com/watch?v=PbHm2qKnu10); publication: 2025-07-07T17:20:54Z; analysis: `analysis/PbHm2qKnu10.json`.
[^PjaVHm_3Ljg]: [Transforming search and discovery using LLMs — Tejaswi & Vinesh, Instacart](https://www.youtube.com/watch?v=PjaVHm_3Ljg); publication: 2025-07-16T18:01:03Z; analysis: `analysis/PjaVHm_3Ljg.json`.
[^Sjfz1TqxzEs]: [Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics](https://www.youtube.com/watch?v=Sjfz1TqxzEs); publication: 2026-09-24T14:30:12Z; analysis: `analysis/Sjfz1TqxzEs.json`.
[^VZzUhELgYk4]: [The Devops Engineer Who Never Sleeps — Diamond Bishop, Datadog](https://www.youtube.com/watch?v=VZzUhELgYk4); publication: 2025-04-22T16:00:06Z; analysis: `analysis/VZzUhELgYk4.json`.
[^VhPfM_aGBVc]: [Anthropic in the Enterprise — Alexander Bricken & Joe Bayley](https://www.youtube.com/watch?v=VhPfM_aGBVc); publication: 2025-04-13T16:00:06Z; analysis: `analysis/VhPfM_aGBVc.json`.
[^XdAWgO11zuk]: [What We Learned from Using LLMs in Pinterest — Mukuntha Narayanan, Han Wang, Pinterest](https://www.youtube.com/watch?v=XdAWgO11zuk); publication: 2025-07-16T17:58:25Z; analysis: `analysis/XdAWgO11zuk.json`.
[^YZHPEkfy2kc]: [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpintero](https://www.youtube.com/watch?v=YZHPEkfy2kc); publication: 2026-04-16T11:00:07Z; analysis: `analysis/YZHPEkfy2kc.json`.
[^YnNF55QV0zs]: [Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai](https://www.youtube.com/watch?v=YnNF55QV0zs); publication: 2026-07-29T20:15:35Z; analysis: `analysis/YnNF55QV0zs.json`.
[^_IzZWeuTx7I]: [RL Environments at Scale – Will Brown, Prime Intellect](https://www.youtube.com/watch?v=_IzZWeuTx7I); publication: 2025-12-09T15:53:42Z; analysis: `analysis/_IzZWeuTx7I.json`.
[^_KFbT6eph5A]: [Using AI to Build an Infinite Game: Jeff Schomay](https://www.youtube.com/watch?v=_KFbT6eph5A); publication: 2024-02-01T17:41:28Z; analysis: `analysis/_KFbT6eph5A.json`.
[^_zl_zimMRak]: [How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit](https://www.youtube.com/watch?v=_zl_zimMRak); publication: 2025-07-23T15:51:31Z; analysis: `analysis/_zl_zimMRak.json`.
[^atwSCxWFVMg]: [GPT Web App Generator - 10,000 apps created in a month: Matija Sosic](https://www.youtube.com/watch?v=atwSCxWFVMg); publication: 2024-01-26T20:51:42Z; analysis: `analysis/atwSCxWFVMg.json`.
[^b_PmGocP4rc]: [Evaling Video Slop — Maor Bril, Character.ai](https://www.youtube.com/watch?v=b_PmGocP4rc); publication: 2026-07-25T00:00:02Z; analysis: `analysis/b_PmGocP4rc.json`.
[^bdHaOXZOhcM]: [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](https://www.youtube.com/watch?v=bdHaOXZOhcM); publication: 2026-08-20T14:00:21Z; analysis: `analysis/bdHaOXZOhcM.json`.
[^cwjs1WAG9CM]: [Building Context-Aware Reasoning Applications with LangChain and LangSmith: Harrison Chase](https://www.youtube.com/watch?v=cwjs1WAG9CM); publication: 2023-11-01T15:15:07Z; analysis: `analysis/cwjs1WAG9CM.json`.
[^eLXF0VojuSs]: [How to Construct Domain Specific LLM Evaluation Systems: Hamel Husain and Emil Sedgh](https://www.youtube.com/watch?v=eLXF0VojuSs); publication: 2024-09-19T16:47:24Z; analysis: `analysis/eLXF0VojuSs.json`.
[^fLUtUkqYHnQ]: [Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI](https://www.youtube.com/watch?v=fLUtUkqYHnQ); publication: 2026-04-29T12:00:06Z; analysis: `analysis/fLUtUkqYHnQ.json`.
[^g4SsanB0gMc]: [Large clusters for small models — Daniel Svonava, Superlinked](https://www.youtube.com/watch?v=g4SsanB0gMc); publication: 2026-09-19T17:30:33Z; analysis: `analysis/g4SsanB0gMc.json`.
[^hxFpUcvWPcU]: [How to build Enterprise Aware Agents - Chau Tran, Glean](https://www.youtube.com/watch?v=hxFpUcvWPcU); publication: 2025-07-24T09:22:32Z; analysis: `analysis/hxFpUcvWPcU.json`.
[^jNE8No-wvok]: [Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta](https://www.youtube.com/watch?v=jNE8No-wvok); publication: 2026-09-23T14:00:34Z; analysis: `analysis/jNE8No-wvok.json`.
[^jtzh-GBXBWc]: [The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft](https://www.youtube.com/watch?v=jtzh-GBXBWc); publication: 2026-07-11T20:00:27Z; analysis: `analysis/jtzh-GBXBWc.json`.
[^kwnCvA9l-TY]: [AI Frontiers in Trust and Safety  Combatting Multifaceted Harm on Tinder at Scale: Vibhor Kumar](https://www.youtube.com/watch?v=kwnCvA9l-TY); publication: 2024-12-02T20:37:40Z; analysis: `analysis/kwnCvA9l-TY.json`.
[^l0FLhNqBOic]: [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](https://www.youtube.com/watch?v=l0FLhNqBOic); publication: 2026-07-28T21:00:06Z; analysis: `analysis/l0FLhNqBOic.json`.
[^p7gaxmCUiIU]: [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](https://www.youtube.com/watch?v=p7gaxmCUiIU); publication: 2026-10-11T21:30:05Z; analysis: `analysis/p7gaxmCUiIU.json`.
[^phchDt63qAA]: [How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed](https://www.youtube.com/watch?v=phchDt63qAA); publication: 2026-05-30T16:00:06Z; analysis: `analysis/phchDt63qAA.json`.
[^wcUJWP6WpGM]: [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](https://www.youtube.com/watch?v=wcUJWP6WpGM); publication: 2026-06-04T14:00:06Z; analysis: `analysis/wcUJWP6WpGM.json`.
[^zM9RYqCcioM]: [Finetuning: 500m AI agents in production with 2 engineers — Mustafa Ali & Kyle Corbitt](https://www.youtube.com/watch?v=zM9RYqCcioM); publication: 2025-04-12T16:00:06Z; analysis: `analysis/zM9RYqCcioM.json`.
