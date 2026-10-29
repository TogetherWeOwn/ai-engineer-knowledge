---
{
  "type": "technique",
  "id": "provider-capability-contract",
  "title": "Verify actual provider capability, limits and fallback behavior",
  "area": "model-routing-capacity",
  "status": "stable",
  "valid_from": "2026-10-19T14:06:53Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2p2ErKRELHM",
      "resource": "https://www.youtube.com/watch?v=2p2ErKRELHM",
      "title": "Voice Agent Engineering — Nik Caryotakis, SuperDial",
      "author": "Nik Caryotakis, SuperDial",
      "last_modified": "2025-04-18T16:00:06Z",
      "analysis_file": "analysis/2p2ErKRELHM.json"
    },
    {
      "id": "32nrHU6zHU8",
      "resource": "https://www.youtube.com/watch?v=32nrHU6zHU8",
      "title": "Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan",
      "author": "Roberto Milev & Uday Kanagala, Navan",
      "last_modified": "2026-08-29T16:30:28Z",
      "analysis_file": "analysis/32nrHU6zHU8.json"
    },
    {
      "id": "84Vtz2IL1Ug",
      "resource": "https://www.youtube.com/watch?v=84Vtz2IL1Ug",
      "title": "Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter",
      "author": "Alex Atallah, OpenRouter",
      "last_modified": "2025-06-25T19:47:43Z",
      "analysis_file": "analysis/84Vtz2IL1Ug.json"
    },
    {
      "id": "9arM9b7JgOo",
      "resource": "https://www.youtube.com/watch?v=9arM9b7JgOo",
      "title": "Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat",
      "author": "Jeffrey Lee-Chan, Snapchat",
      "last_modified": "2026-07-11T14:45:18Z",
      "analysis_file": "analysis/9arM9b7JgOo.json"
    },
    {
      "id": "MC55hdWLq4o",
      "resource": "https://www.youtube.com/watch?v=MC55hdWLq4o",
      "title": "The Future of Evals - Ankur Goyal, Braintrust",
      "author": "Ankur Goyal, Braintrust",
      "last_modified": "2025-08-09T15:12:25Z",
      "analysis_file": "analysis/MC55hdWLq4o.json"
    },
    {
      "id": "MpZzWMdmQCE",
      "resource": "https://www.youtube.com/watch?v=MpZzWMdmQCE",
      "title": "Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com",
      "author": "Talha Sheikh, Checkout.com",
      "last_modified": "2026-07-08T08:31:41Z",
      "analysis_file": "analysis/MpZzWMdmQCE.json"
    },
    {
      "id": "O-CBZ3JtRvo",
      "resource": "https://www.youtube.com/watch?v=O-CBZ3JtRvo",
      "title": "Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face",
      "author": "Uri Rolls, Arithmetic & Thom Wolf, Hugging Face",
      "last_modified": "2026-07-24T05:19:15Z",
      "analysis_file": "analysis/O-CBZ3JtRvo.json"
    },
    {
      "id": "ObTPqBGsEbA",
      "resource": "https://www.youtube.com/watch?v=ObTPqBGsEbA",
      "title": "The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks",
      "author": "Sandipan Bhaumik, Databricks",
      "last_modified": "2026-06-18T13:00:06Z",
      "analysis_file": "analysis/ObTPqBGsEbA.json"
    },
    {
      "id": "OrtBEBLMXdM",
      "resource": "https://www.youtube.com/watch?v=OrtBEBLMXdM",
      "title": "Iterating on LLM apps at scale  Learnings from Discord: Ian Webster",
      "author": null,
      "last_modified": "2024-11-22T20:27:24Z",
      "analysis_file": "analysis/OrtBEBLMXdM.json"
    },
    {
      "id": "Q5IVm_CxN2w",
      "resource": "https://www.youtube.com/watch?v=Q5IVm_CxN2w",
      "title": "Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway",
      "author": "Mahmoud Abdelwahab, Railway",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/Q5IVm_CxN2w.json"
    },
    {
      "id": "QHBjufYK8TA",
      "resource": "https://www.youtube.com/watch?v=QHBjufYK8TA",
      "title": "The State of Model Routing — NVIDIA, Cognition, OpenRouter",
      "author": "NVIDIA, Cognition, OpenRouter",
      "last_modified": "2026-08-06T17:07:24Z",
      "analysis_file": "analysis/QHBjufYK8TA.json"
    },
    {
      "id": "SS-A8sE7hkw",
      "resource": "https://www.youtube.com/watch?v=SS-A8sE7hkw",
      "title": "Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind",
      "author": "Gus Martins, & Ian Ballantyne, Google DeepMind",
      "last_modified": "2026-06-10T15:00:06Z",
      "analysis_file": "analysis/SS-A8sE7hkw.json"
    },
    {
      "id": "Ti-BmGU1_mQ",
      "resource": "https://www.youtube.com/watch?v=Ti-BmGU1_mQ",
      "title": "The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI",
      "author": "Eugene Cheah, Featherless AI",
      "last_modified": "2026-10-17T09:00:27Z",
      "analysis_file": "analysis/Ti-BmGU1_mQ.json"
    },
    {
      "id": "UGjk3Uk0MxM",
      "resource": "https://www.youtube.com/watch?v=UGjk3Uk0MxM",
      "title": "The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft",
      "author": "Pamela Fox, Microsoft",
      "last_modified": "2026-10-19T14:06:53Z",
      "analysis_file": "analysis/UGjk3Uk0MxM.json"
    },
    {
      "id": "UXOLprPvr-0",
      "resource": "https://www.youtube.com/watch?v=UXOLprPvr-0",
      "title": "Building AI Agents with Real ROI in the Enterprise SDLC: Bruno (Booking.com) & Beyang (Sourcegraph)",
      "author": null,
      "last_modified": "2025-04-08T17:00:06Z",
      "analysis_file": "analysis/UXOLprPvr-0.json"
    },
    {
      "id": "Ubwb6NzegyA",
      "resource": "https://www.youtube.com/watch?v=Ubwb6NzegyA",
      "title": "Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind",
      "author": "Nicholas Kang & Michael Aaron, Google DeepMind",
      "last_modified": "2026-05-25T17:00:06Z",
      "analysis_file": "analysis/Ubwb6NzegyA.json"
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
      "id": "YIxzNZDDy1A",
      "resource": "https://www.youtube.com/watch?v=YIxzNZDDy1A",
      "title": "From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases",
      "author": "Wolfram Ravenwolf, Weights & Biases",
      "last_modified": "2026-10-11T17:00:18Z",
      "analysis_file": "analysis/YIxzNZDDy1A.json"
    },
    {
      "id": "YgEv7IQzGdM",
      "resource": "https://www.youtube.com/watch?v=YgEv7IQzGdM",
      "title": "How to Kill the Code Review — Ankit Jain, Aviator",
      "author": "Ankit Jain, Aviator",
      "last_modified": "2026-08-17T20:00:08Z",
      "analysis_file": "analysis/YgEv7IQzGdM.json"
    },
    {
      "id": "ZFxh7sqbUZo",
      "resource": "https://www.youtube.com/watch?v=ZFxh7sqbUZo",
      "title": "Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd",
      "author": "Prof. David Brumley, Bugcrowd",
      "last_modified": "2026-08-01T00:30:06Z",
      "analysis_file": "analysis/ZFxh7sqbUZo.json"
    },
    {
      "id": "ZUZVNKFSmTM",
      "resource": "https://www.youtube.com/watch?v=ZUZVNKFSmTM",
      "title": "How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker",
      "author": "Jim Clark, Docker",
      "last_modified": "2026-10-06T00:30:15Z",
      "analysis_file": "analysis/ZUZVNKFSmTM.json"
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
      "id": "dvft0Gp9sEE",
      "resource": "https://www.youtube.com/watch?v=dvft0Gp9sEE",
      "title": "Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo",
      "author": "Charlie Guo",
      "last_modified": "2025-06-03T07:00:07Z",
      "analysis_file": "analysis/dvft0Gp9sEE.json"
    },
    {
      "id": "esY99nYXxR4",
      "resource": "https://www.youtube.com/watch?v=esY99nYXxR4",
      "title": "How we solved Context Management in Agents — Sally-Ann Delucia",
      "author": "Sally-Ann Delucia",
      "last_modified": "2026-05-10T19:00:06Z",
      "analysis_file": "analysis/esY99nYXxR4.json"
    },
    {
      "id": "fmZWvE7yDZo",
      "resource": "https://www.youtube.com/watch?v=fmZWvE7yDZo",
      "title": "UX Design Principles for Semi Autonomous Multi Agent Systems — Victor Dibia, Microsoft",
      "author": "Victor Dibia, Microsoft",
      "last_modified": "2025-07-21T19:11:17Z",
      "analysis_file": "analysis/fmZWvE7yDZo.json"
    },
    {
      "id": "gvIAkmZUEZY",
      "resource": "https://www.youtube.com/watch?v=gvIAkmZUEZY",
      "title": "Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code",
      "author": "Beyang Liu, Amp Code",
      "last_modified": "2025-12-22T17:00:06Z",
      "analysis_file": "analysis/gvIAkmZUEZY.json"
    },
    {
      "id": "pMggiOb18tc",
      "resource": "https://www.youtube.com/watch?v=pMggiOb18tc",
      "title": "The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI",
      "author": "Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI",
      "last_modified": "2026-07-09T18:53:34Z",
      "analysis_file": "analysis/pMggiOb18tc.json"
    },
    {
      "id": "qBHfQT3YtyY",
      "resource": "https://www.youtube.com/watch?v=qBHfQT3YtyY",
      "title": "Lessons From A Year Building With LLMs",
      "author": null,
      "last_modified": "2024-07-19T17:41:05Z",
      "analysis_file": "analysis/qBHfQT3YtyY.json"
    },
    {
      "id": "sXXl3YMU7ZI",
      "resource": "https://www.youtube.com/watch?v=sXXl3YMU7ZI",
      "title": "Building Reliable Support Agents Using the Effect Typescript Library - Michael Fester",
      "author": "Michael Fester",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/sXXl3YMU7ZI.json"
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
      "id": "uiq95JYpBGY",
      "resource": "https://www.youtube.com/watch?v=uiq95JYpBGY",
      "title": "Productionizing GenAI Models – Lessons from the world's best AI teams: Lukas Biewald",
      "author": "Lessons from the world's best AI teams: Lukas Biewald",
      "last_modified": "2024-10-23T19:23:33Z",
      "analysis_file": "analysis/uiq95JYpBGY.json"
    },
    {
      "id": "vGCJ7diEtrw",
      "resource": "https://www.youtube.com/watch?v=vGCJ7diEtrw",
      "title": "What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory",
      "author": "Tereza Tížková, Factory",
      "last_modified": "2026-09-27T15:00:02Z",
      "analysis_file": "analysis/vGCJ7diEtrw.json"
    },
    {
      "id": "vrDvatGtIxs",
      "resource": "https://www.youtube.com/watch?v=vrDvatGtIxs",
      "title": "Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph",
      "author": "Tejas Bhakta, Morph",
      "last_modified": "2026-09-26T15:00:32Z",
      "analysis_file": "analysis/vrDvatGtIxs.json"
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
      "id": "xs-ob87TTzg",
      "resource": "https://www.youtube.com/watch?v=xs-ob87TTzg",
      "title": "Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle",
      "author": "Ignacio Martinez, Oracle",
      "last_modified": "2026-09-18T16:00:11Z",
      "analysis_file": "analysis/xs-ob87TTzg.json"
    },
    {
      "id": "yUmS-F9IX90",
      "resource": "https://www.youtube.com/watch?v=yUmS-F9IX90",
      "title": "Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline",
      "author": "Ara Khan, Cline",
      "last_modified": "2026-05-19T15:00:06Z",
      "analysis_file": "analysis/yUmS-F9IX90.json"
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

# Verify actual provider capability, limits and fallback behavior

## What

Verify actual provider capability, limits and fallback behavior

Separate model/account transport from task policy; fail over only to an available model that meets the same capability and governance constraints.

## Evidence

> AI tools so behind our open a endpoint we can kind of route to different models
> — 13:34 [^2p2ErKRELHM]

Source analysis [^32nrHU6zHU8]; no independently matched timestamped quote published.

Source analysis [^84Vtz2IL1Ug]; no independently matched timestamped quote published.

Source analysis [^9arM9b7JgOo]; no independently matched timestamped quote published.

Source analysis [^MC55hdWLq4o]; no independently matched timestamped quote published.

Source analysis [^MpZzWMdmQCE]; no independently matched timestamped quote published.

Source analysis [^O-CBZ3JtRvo]; no independently matched timestamped quote published.

Source analysis [^ObTPqBGsEbA]; no independently matched timestamped quote published.

Source analysis [^OrtBEBLMXdM]; no independently matched timestamped quote published.

> automatically check the status pages of these services. Imagine like a payment
> — 05:51 [^Q5IVm_CxN2w]

Source analysis [^QHBjufYK8TA]; no independently matched timestamped quote published.

Source analysis [^SS-A8sE7hkw]; no independently matched timestamped quote published.

Source analysis [^Ti-BmGU1_mQ]; no independently matched timestamped quote published.

Source analysis [^UGjk3Uk0MxM]; no independently matched timestamped quote published.

> is because we found the llms had expertise right and so if we were going
> — 07:59 [^UXOLprPvr-0]

Source analysis [^Ubwb6NzegyA]; no independently matched timestamped quote published.

> another model that has a better multimodal capability
> — 14:59 [^XLEYtv3cMlw]

> this provider and half the task with the other provider. So, you definitely have
> — 26:28 [^YIxzNZDDy1A]

Source analysis [^YgEv7IQzGdM]; no independently matched timestamped quote published.

Source analysis [^ZFxh7sqbUZo]; no independently matched timestamped quote published.

Source analysis [^ZUZVNKFSmTM]; no independently matched timestamped quote published.

Source analysis [^_-oIuRH4oGA]; no independently matched timestamped quote published.

Source analysis [^dvft0Gp9sEE]; no independently matched timestamped quote published.

Source analysis [^esY99nYXxR4]; no independently matched timestamped quote published.

> you can do is to have proactive suggestions based on user context. Let's
> — 14:10 [^fmZWvE7yDZo]

Source analysis [^gvIAkmZUEZY]; no independently matched timestamped quote published.

> compaction. Codex needed a way to compact long contexts for long-running
> — 10:23 [^pMggiOb18tc]

> but great um and finally when using llms as apis pin model version
> — 30:21 [^qBHfQT3YtyY]

Source analysis [^sXXl3YMU7ZI]; no independently matched timestamped quote published.

Source analysis [^u825uxb7LnA]; no independently matched timestamped quote published.

> model for free exact same API to llama two got the accuracy 79% right so this
> — 13:42 [^uiq95JYpBGY]

> speed because open source models are often faster and uh if one LM provider
> — 07:20 [^vGCJ7diEtrw]

Source analysis [^vrDvatGtIxs]; no independently matched timestamped quote published.

Source analysis [^wJwTlvb_TSo]; no independently matched timestamped quote published.

> swappable and the harness is what we're going to focus on today.
> — 13:41 [^xs-ob87TTzg]

> would still work, except that the performance would be degraded, and you
> — 10:29 [^yUmS-F9IX90]

> expensive. So blind retries just multiply your cost and your tail
> — 02:53 [^zrZ1amZBSPw]

> provider because that's your last line of defense. If that goes down, your
> — 06:21 [^zrZ1amZBSPw]

> to really test your fallbacks well. They can have differences in your tool
> — 04:50 [^zrZ1amZBSPw]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Use the cheapest evidenced capable mechanism
- **Speed:** Admit work within real quota and resource limits
- **Quality:** Preserve the role quality floor
- **Reliability:** Avoid exhaustion, unsafe fallback and policy bypass
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2p2ErKRELHM]: [Voice Agent Engineering — Nik Caryotakis, SuperDial](https://www.youtube.com/watch?v=2p2ErKRELHM); publication: 2025-04-18T16:00:06Z; analysis: `analysis/2p2ErKRELHM.json`.
[^32nrHU6zHU8]: [Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan](https://www.youtube.com/watch?v=32nrHU6zHU8); publication: 2026-08-29T16:30:28Z; analysis: `analysis/32nrHU6zHU8.json`.
[^84Vtz2IL1Ug]: [Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter](https://www.youtube.com/watch?v=84Vtz2IL1Ug); publication: 2025-06-25T19:47:43Z; analysis: `analysis/84Vtz2IL1Ug.json`.
[^9arM9b7JgOo]: [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](https://www.youtube.com/watch?v=9arM9b7JgOo); publication: 2026-07-11T14:45:18Z; analysis: `analysis/9arM9b7JgOo.json`.
[^MC55hdWLq4o]: [The Future of Evals - Ankur Goyal, Braintrust](https://www.youtube.com/watch?v=MC55hdWLq4o); publication: 2025-08-09T15:12:25Z; analysis: `analysis/MC55hdWLq4o.json`.
[^MpZzWMdmQCE]: [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](https://www.youtube.com/watch?v=MpZzWMdmQCE); publication: 2026-07-08T08:31:41Z; analysis: `analysis/MpZzWMdmQCE.json`.
[^O-CBZ3JtRvo]: [Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face](https://www.youtube.com/watch?v=O-CBZ3JtRvo); publication: 2026-07-24T05:19:15Z; analysis: `analysis/O-CBZ3JtRvo.json`.
[^ObTPqBGsEbA]: [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA); publication: 2026-06-18T13:00:06Z; analysis: `analysis/ObTPqBGsEbA.json`.
[^OrtBEBLMXdM]: [Iterating on LLM apps at scale  Learnings from Discord: Ian Webster](https://www.youtube.com/watch?v=OrtBEBLMXdM); publication: 2024-11-22T20:27:24Z; analysis: `analysis/OrtBEBLMXdM.json`.
[^Q5IVm_CxN2w]: [Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway](https://www.youtube.com/watch?v=Q5IVm_CxN2w); publication: 2025-11-24T20:16:36Z; analysis: `analysis/Q5IVm_CxN2w.json`.
[^QHBjufYK8TA]: [The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA); publication: 2026-08-06T17:07:24Z; analysis: `analysis/QHBjufYK8TA.json`.
[^SS-A8sE7hkw]: [Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind](https://www.youtube.com/watch?v=SS-A8sE7hkw); publication: 2026-06-10T15:00:06Z; analysis: `analysis/SS-A8sE7hkw.json`.
[^Ti-BmGU1_mQ]: [The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI](https://www.youtube.com/watch?v=Ti-BmGU1_mQ); publication: 2026-10-17T09:00:27Z; analysis: `analysis/Ti-BmGU1_mQ.json`.
[^UGjk3Uk0MxM]: [The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft](https://www.youtube.com/watch?v=UGjk3Uk0MxM); publication: 2026-10-19T14:06:53Z; analysis: `analysis/UGjk3Uk0MxM.json`.
[^UXOLprPvr-0]: [Building AI Agents with Real ROI in the Enterprise SDLC: Bruno (Booking.com) & Beyang (Sourcegraph)](https://www.youtube.com/watch?v=UXOLprPvr-0); publication: 2025-04-08T17:00:06Z; analysis: `analysis/UXOLprPvr-0.json`.
[^Ubwb6NzegyA]: [Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind](https://www.youtube.com/watch?v=Ubwb6NzegyA); publication: 2026-05-25T17:00:06Z; analysis: `analysis/Ubwb6NzegyA.json`.
[^XLEYtv3cMlw]: [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](https://www.youtube.com/watch?v=XLEYtv3cMlw); publication: 2026-07-18T23:30:06Z; analysis: `analysis/XLEYtv3cMlw.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^YgEv7IQzGdM]: [How to Kill the Code Review — Ankit Jain, Aviator](https://www.youtube.com/watch?v=YgEv7IQzGdM); publication: 2026-08-17T20:00:08Z; analysis: `analysis/YgEv7IQzGdM.json`.
[^ZFxh7sqbUZo]: [Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd](https://www.youtube.com/watch?v=ZFxh7sqbUZo); publication: 2026-08-01T00:30:06Z; analysis: `analysis/ZFxh7sqbUZo.json`.
[^ZUZVNKFSmTM]: [How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker](https://www.youtube.com/watch?v=ZUZVNKFSmTM); publication: 2026-10-06T00:30:15Z; analysis: `analysis/ZUZVNKFSmTM.json`.
[^_-oIuRH4oGA]: [How agents broke app-level infrastructure - Evan Boyle](https://www.youtube.com/watch?v=_-oIuRH4oGA); publication: 2025-06-03T22:22:28Z; analysis: `analysis/_-oIuRH4oGA.json`.
[^dvft0Gp9sEE]: [Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo](https://www.youtube.com/watch?v=dvft0Gp9sEE); publication: 2025-06-03T07:00:07Z; analysis: `analysis/dvft0Gp9sEE.json`.
[^esY99nYXxR4]: [How we solved Context Management in Agents — Sally-Ann Delucia](https://www.youtube.com/watch?v=esY99nYXxR4); publication: 2026-05-10T19:00:06Z; analysis: `analysis/esY99nYXxR4.json`.
[^fmZWvE7yDZo]: [UX Design Principles for Semi Autonomous Multi Agent Systems — Victor Dibia, Microsoft](https://www.youtube.com/watch?v=fmZWvE7yDZo); publication: 2025-07-21T19:11:17Z; analysis: `analysis/fmZWvE7yDZo.json`.
[^gvIAkmZUEZY]: [Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code](https://www.youtube.com/watch?v=gvIAkmZUEZY); publication: 2025-12-22T17:00:06Z; analysis: `analysis/gvIAkmZUEZY.json`.
[^pMggiOb18tc]: [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](https://www.youtube.com/watch?v=pMggiOb18tc); publication: 2026-07-09T18:53:34Z; analysis: `analysis/pMggiOb18tc.json`.
[^qBHfQT3YtyY]: [Lessons From A Year Building With LLMs](https://www.youtube.com/watch?v=qBHfQT3YtyY); publication: 2024-07-19T17:41:05Z; analysis: `analysis/qBHfQT3YtyY.json`.
[^sXXl3YMU7ZI]: [Building Reliable Support Agents Using the Effect Typescript Library - Michael Fester](https://www.youtube.com/watch?v=sXXl3YMU7ZI); publication: 2025-06-03T22:22:29Z; analysis: `analysis/sXXl3YMU7ZI.json`.
[^u825uxb7LnA]: [The Coherence Trap: Why LLMs Feel Smart (But Aren’t Thinking) - Travis Frisinger](https://www.youtube.com/watch?v=u825uxb7LnA); publication: 2025-06-03T22:22:29Z; analysis: `analysis/u825uxb7LnA.json`.
[^uiq95JYpBGY]: [Productionizing GenAI Models – Lessons from the world's best AI teams: Lukas Biewald](https://www.youtube.com/watch?v=uiq95JYpBGY); publication: 2024-10-23T19:23:33Z; analysis: `analysis/uiq95JYpBGY.json`.
[^vGCJ7diEtrw]: [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](https://www.youtube.com/watch?v=vGCJ7diEtrw); publication: 2026-09-27T15:00:02Z; analysis: `analysis/vGCJ7diEtrw.json`.
[^vrDvatGtIxs]: [Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph](https://www.youtube.com/watch?v=vrDvatGtIxs); publication: 2026-09-26T15:00:32Z; analysis: `analysis/vrDvatGtIxs.json`.
[^wJwTlvb_TSo]: [WTF do people use Open Models for??](https://www.youtube.com/watch?v=wJwTlvb_TSo); publication: 2025-02-22T20:00:06Z; analysis: `analysis/wJwTlvb_TSo.json`.
[^xs-ob87TTzg]: [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](https://www.youtube.com/watch?v=xs-ob87TTzg); publication: 2026-09-18T16:00:11Z; analysis: `analysis/xs-ob87TTzg.json`.
[^yUmS-F9IX90]: [Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline](https://www.youtube.com/watch?v=yUmS-F9IX90); publication: 2026-05-19T15:00:06Z; analysis: `analysis/yUmS-F9IX90.json`.
[^zrZ1amZBSPw]: [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](https://www.youtube.com/watch?v=zrZ1amZBSPw); publication: 2026-08-28T15:30:03Z; analysis: `analysis/zrZ1amZBSPw.json`.
