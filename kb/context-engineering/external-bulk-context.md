---
{
  "type": "technique",
  "id": "external-bulk-context",
  "title": "Keep bulk evidence in queryable files, not repeated prompt payloads",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-10-10T01:30:14Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2aS7aKoXn64",
      "resource": "https://www.youtube.com/watch?v=2aS7aKoXn64",
      "title": "Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software",
      "author": "Rayan Garg, Theta Software",
      "last_modified": "2026-08-01T00:00:06Z",
      "analysis_file": "analysis/2aS7aKoXn64.json"
    },
    {
      "id": "3hXJI2q0Jz8",
      "resource": "https://www.youtube.com/watch?v=3hXJI2q0Jz8",
      "title": "Recursive Coding Agents - Raymond Weitekamp, OpenProse",
      "author": "Raymond Weitekamp, OpenProse",
      "last_modified": "2026-06-25T21:00:06Z",
      "analysis_file": "analysis/3hXJI2q0Jz8.json"
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
      "id": "DrfyORO8RqA",
      "resource": "https://www.youtube.com/watch?v=DrfyORO8RqA",
      "title": "Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS",
      "author": "Elizabeth Fuentes Leone, AWS",
      "last_modified": "2026-10-08T00:30:18Z",
      "analysis_file": "analysis/DrfyORO8RqA.json"
    },
    {
      "id": "ExeD-8gFUMM",
      "resource": "https://www.youtube.com/watch?v=ExeD-8gFUMM",
      "title": "Full Spec MCP: Hidden Capabilities of the MCP spec — Harald Kirschner, Microsoft/VSCode",
      "author": "Harald Kirschner, Microsoft/VSCode",
      "last_modified": "2025-07-18T18:42:25Z",
      "analysis_file": "analysis/ExeD-8gFUMM.json"
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
      "id": "RFKCzGlAU6Q",
      "resource": "https://www.youtube.com/watch?v=RFKCzGlAU6Q",
      "title": "How Claude Code Works - Jared Zoneraich, PromptLayer",
      "author": "Jared Zoneraich, PromptLayer",
      "last_modified": "2025-12-26T22:04:34Z",
      "analysis_file": "analysis/RFKCzGlAU6Q.json"
    },
    {
      "id": "TqC1qOfiVcQ",
      "resource": "https://www.youtube.com/watch?v=TqC1qOfiVcQ",
      "title": "Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic",
      "author": "Thariq Shihipar, Anthropic",
      "last_modified": "2026-01-05T17:00:06Z",
      "analysis_file": "analysis/TqC1qOfiVcQ.json"
    },
    {
      "id": "UyyOoJmuATU",
      "resource": "https://www.youtube.com/watch?v=UyyOoJmuATU",
      "title": "Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay",
      "author": "Vasant Kearney, Onlay",
      "last_modified": "2026-08-19T16:30:32Z",
      "analysis_file": "analysis/UyyOoJmuATU.json"
    },
    {
      "id": "WRBNDpUhsJQ",
      "resource": "https://www.youtube.com/watch?v=WRBNDpUhsJQ",
      "title": "Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum",
      "author": "Adrian Bertagnoli, Callosum",
      "last_modified": "2026-05-24T14:00:06Z",
      "analysis_file": "analysis/WRBNDpUhsJQ.json"
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
      "id": "YiFqcu9YA38",
      "resource": "https://www.youtube.com/watch?v=YiFqcu9YA38",
      "title": "Dashboards Are Dead — Sarah Simionescu, Composio",
      "author": "Sarah Simionescu, Composio",
      "last_modified": "2026-10-04T01:30:36Z",
      "analysis_file": "analysis/YiFqcu9YA38.json"
    },
    {
      "id": "Z-c11pV_uvU",
      "resource": "https://www.youtube.com/watch?v=Z-c11pV_uvU",
      "title": "Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley",
      "author": "Frank Coyle, UC Berkeley",
      "last_modified": "2026-08-08T16:00:06Z",
      "analysis_file": "analysis/Z-c11pV_uvU.json"
    },
    {
      "id": "ZIYYsAzaLlA",
      "resource": "https://www.youtube.com/watch?v=ZIYYsAzaLlA",
      "title": "Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma",
      "author": "Jesse Lumarie, Figma",
      "last_modified": "2026-08-28T14:00:06Z",
      "analysis_file": "analysis/ZIYYsAzaLlA.json"
    },
    {
      "id": "_B4Pv9ttFgY",
      "resource": "https://www.youtube.com/watch?v=_B4Pv9ttFgY",
      "title": "Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google",
      "author": "Michael Hablich, Google",
      "last_modified": "2026-06-05T17:00:06Z",
      "analysis_file": "analysis/_B4Pv9ttFgY.json"
    },
    {
      "id": "bUJgirn4_yc",
      "resource": "https://www.youtube.com/watch?v=bUJgirn4_yc",
      "title": "When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain",
      "author": "Dmitry Petrov, DataChain",
      "last_modified": "2026-07-20T06:25:07Z",
      "analysis_file": "analysis/bUJgirn4_yc.json"
    },
    {
      "id": "ckLXb15BnM8",
      "resource": "https://www.youtube.com/watch?v=ckLXb15BnM8",
      "title": "The Adversarial Path to the Personal Assistant: Sumit Agarwal",
      "author": null,
      "last_modified": "2025-02-15T19:30:06Z",
      "analysis_file": "analysis/ckLXb15BnM8.json"
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
      "id": "fWXJM-J0ZB8",
      "resource": "https://www.youtube.com/watch?v=fWXJM-J0ZB8",
      "title": "Frontier results, on device - RL Nabors, Arize",
      "author": "RL Nabors, Arize",
      "last_modified": "2026-06-29T03:30:03Z",
      "analysis_file": "analysis/fWXJM-J0ZB8.json"
    },
    {
      "id": "fZH97QHHYjY",
      "resource": "https://www.youtube.com/watch?v=fZH97QHHYjY",
      "title": "The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev",
      "author": "Jo Kristian Bergum, Hornet.dev",
      "last_modified": "2026-09-16T13:30:32Z",
      "analysis_file": "analysis/fZH97QHHYjY.json"
    },
    {
      "id": "khVX_BUnEwU",
      "resource": "https://www.youtube.com/watch?v=khVX_BUnEwU",
      "title": "Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital",
      "author": "Yohei Nakajima, Untapped Capital",
      "last_modified": "2026-07-22T20:00:06Z",
      "analysis_file": "analysis/khVX_BUnEwU.json"
    },
    {
      "id": "lp0pswT_FEI",
      "resource": "https://www.youtube.com/watch?v=lp0pswT_FEI",
      "title": "Just do it. (let your tools think for themselves) - Robert Chandler",
      "author": "Robert Chandler",
      "last_modified": "2025-06-10T17:30:11Z",
      "analysis_file": "analysis/lp0pswT_FEI.json"
    },
    {
      "id": "mav15aW9lLM",
      "resource": "https://www.youtube.com/watch?v=mav15aW9lLM",
      "title": "Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard",
      "author": "Christopher Lovejoy & Saul Howard",
      "last_modified": "2026-08-19T18:30:15Z",
      "analysis_file": "analysis/mav15aW9lLM.json"
    },
    {
      "id": "pAnLpiAG6Es",
      "resource": "https://www.youtube.com/watch?v=pAnLpiAG6Es",
      "title": "MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify",
      "author": "Jan Čurn, Apify",
      "last_modified": "2026-10-02T14:00:05Z",
      "analysis_file": "analysis/pAnLpiAG6Es.json"
    },
    {
      "id": "rbjWzZK2LU0",
      "resource": "https://www.youtube.com/watch?v=rbjWzZK2LU0",
      "title": "Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic",
      "author": "Sachin Malhotra, Anthropic",
      "last_modified": "2026-08-22T14:00:06Z",
      "analysis_file": "analysis/rbjWzZK2LU0.json"
    },
    {
      "id": "rmvDxxNubIg",
      "resource": "https://www.youtube.com/watch?v=rmvDxxNubIg",
      "title": "No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer",
      "author": "Dex Horthy, HumanLayer",
      "last_modified": "2025-12-02T22:52:58Z",
      "analysis_file": "analysis/rmvDxxNubIg.json"
    },
    {
      "id": "tNAV259UhCM",
      "resource": "https://www.youtube.com/watch?v=tNAV259UhCM",
      "title": "From 15% to 90% GPU Utilization: Fix the Data Pipeline, Not the Model",
      "author": null,
      "last_modified": "2026-10-10T01:30:14Z",
      "analysis_file": "analysis/tNAV259UhCM.json"
    },
    {
      "id": "uiP88SpCi1Q",
      "resource": "https://www.youtube.com/watch?v=uiP88SpCi1Q",
      "title": "Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS",
      "author": "Erik Hanchett, AWS",
      "last_modified": "2026-06-28T22:00:14Z",
      "analysis_file": "analysis/uiP88SpCi1Q.json"
    },
    {
      "id": "wXVvfFMTyzY",
      "resource": "https://www.youtube.com/watch?v=wXVvfFMTyzY",
      "title": "A2A & MCP Workshop: Automating Business Processes with LLMs — Damien Murphy, Bench",
      "author": "Damien Murphy, Bench",
      "last_modified": "2025-07-26T14:15:05Z",
      "analysis_file": "analysis/wXVvfFMTyzY.json"
    },
    {
      "id": "xo68uCibfm8",
      "resource": "https://www.youtube.com/watch?v=xo68uCibfm8",
      "title": "It’s Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners",
      "author": "Kevin Madura, AlixPartners",
      "last_modified": "2026-09-09T13:30:27Z",
      "analysis_file": "analysis/xo68uCibfm8.json"
    },
    {
      "id": "xyL2Ltkh-SA",
      "resource": "https://www.youtube.com/watch?v=xyL2Ltkh-SA",
      "title": "How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads",
      "author": "Preetika Bhateja & Daniel Bump, YouTube Ads",
      "last_modified": "2026-07-24T21:00:00Z",
      "analysis_file": "analysis/xyL2Ltkh-SA.json"
    },
    {
      "id": "ya_9_niq2as",
      "resource": "https://www.youtube.com/watch?v=ya_9_niq2as",
      "title": "Your LLM Ran Out of Knowledge — Now What?",
      "author": "Now What?",
      "last_modified": "2025-02-22T17:00:06Z",
      "analysis_file": "analysis/ya_9_niq2as.json"
    },
    {
      "id": "zKk7sDMGDEQ",
      "resource": "https://www.youtube.com/watch?v=zKk7sDMGDEQ",
      "title": "Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer",
      "author": "Kuba Rogut, Turbopuffer",
      "last_modified": "2026-06-03T15:00:06Z",
      "analysis_file": "analysis/zKk7sDMGDEQ.json"
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

# Keep bulk evidence in queryable files, not repeated prompt payloads

## What

Keep bulk evidence in queryable files, not repeated prompt payloads

Keep logs, tables and source in files; use code, regex and retrieval to select evidence before semantic reasoning. Preserve source locations so selected excerpts remain verifiable.

## Evidence

Source analysis [^2aS7aKoXn64]; no independently matched timestamped quote published.

Source analysis [^3hXJI2q0Jz8]; no independently matched timestamped quote published.

Source analysis [^8oyalrfwgjw]; no independently matched timestamped quote published.

Source analysis [^DrfyORO8RqA]; no independently matched timestamped quote published.

Source analysis [^ExeD-8gFUMM]; no independently matched timestamped quote published.

> most of the context by default will only be going to like one model. So, like
> — 11:34 [^QHBjufYK8TA]

> instructing it save markdown files because the shorter the context, the
> — 22:04 [^RFKCzGlAU6Q]

> after every tool call, insert changes that the user has made. Uh and you and
> — 1:47:46 [^TqC1qOfiVcQ]

> like search across it and then have the tool call return the path of the result.
> — 30:32 [^TqC1qOfiVcQ]

Source analysis [^UyyOoJmuATU]; no independently matched timestamped quote published.

Source analysis [^WRBNDpUhsJQ]; no independently matched timestamped quote published.

> Keep using MD files or links to documentation to getting started doc
> — 12:58 [^X4BwOu0GWb8]

Source analysis [^YiFqcu9YA38]; no independently matched timestamped quote published.

> For the reasons we just talked about. You want to isolate your subtask output,
> — 15:38 [^Z-c11pV_uvU]

Source analysis [^ZIYYsAzaLlA]; no independently matched timestamped quote published.

Source analysis [^_B4Pv9ttFgY]; no independently matched timestamped quote published.

Source analysis [^bUJgirn4_yc]; no independently matched timestamped quote published.

Source analysis [^ckLXb15BnM8]; no independently matched timestamped quote published.

Source analysis [^esY99nYXxR4]; no independently matched timestamped quote published.

Source analysis [^fWXJM-J0ZB8]; no independently matched timestamped quote published.

Source analysis [^fZH97QHHYjY]; no independently matched timestamped quote published.

> relevant messages, grabbed a couple messages before and after, made sure it
> — 08:42 [^khVX_BUnEwU]

Source analysis [^lp0pswT_FEI]; no independently matched timestamped quote published.

Source analysis [^mav15aW9lLM]; no independently matched timestamped quote published.

> place to uh pass sensitive value or like large data and sub agents only push that
> — 04:28 [^pAnLpiAG6Es]

> basically evaluated to nothing and the filter dropped out and now the selector
> — 01:49 [^rbjWzZK2LU0]

Source analysis [^rmvDxxNubIg]; no independently matched timestamped quote published.

Source analysis [^tNAV259UhCM]; no independently matched timestamped quote published.

> If you have a large tool result that's coming back, you can store it locally or
> — 02:06 [^uiP88SpCi1Q]

Source analysis [^wXVvfFMTyzY]; no independently matched timestamped quote published.

Source analysis [^xo68uCibfm8]; no independently matched timestamped quote published.

> works better to first do intuition based approach where you kind of um first see
> — 04:29 [^xyL2Ltkh-SA]

Source analysis [^ya_9_niq2as]; no independently matched timestamped quote published.

> max of 50 line reads at a time and then the same thing with a windowed reads
> — 06:00 [^zKk7sDMGDEQ]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2aS7aKoXn64]: [Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software](https://www.youtube.com/watch?v=2aS7aKoXn64); publication: 2026-08-01T00:00:06Z; analysis: `analysis/2aS7aKoXn64.json`.
[^3hXJI2q0Jz8]: [Recursive Coding Agents - Raymond Weitekamp, OpenProse](https://www.youtube.com/watch?v=3hXJI2q0Jz8); publication: 2026-06-25T21:00:06Z; analysis: `analysis/3hXJI2q0Jz8.json`.
[^8oyalrfwgjw]: [RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](https://www.youtube.com/watch?v=8oyalrfwgjw); publication: 2026-07-12T23:00:06Z; analysis: `analysis/8oyalrfwgjw.json`.
[^DrfyORO8RqA]: [Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS](https://www.youtube.com/watch?v=DrfyORO8RqA); publication: 2026-10-08T00:30:18Z; analysis: `analysis/DrfyORO8RqA.json`.
[^ExeD-8gFUMM]: [Full Spec MCP: Hidden Capabilities of the MCP spec — Harald Kirschner, Microsoft/VSCode](https://www.youtube.com/watch?v=ExeD-8gFUMM); publication: 2025-07-18T18:42:25Z; analysis: `analysis/ExeD-8gFUMM.json`.
[^QHBjufYK8TA]: [The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA); publication: 2026-08-06T17:07:24Z; analysis: `analysis/QHBjufYK8TA.json`.
[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^TqC1qOfiVcQ]: [Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ); publication: 2026-01-05T17:00:06Z; analysis: `analysis/TqC1qOfiVcQ.json`.
[^UyyOoJmuATU]: [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](https://www.youtube.com/watch?v=UyyOoJmuATU); publication: 2026-08-19T16:30:32Z; analysis: `analysis/UyyOoJmuATU.json`.
[^WRBNDpUhsJQ]: [Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum](https://www.youtube.com/watch?v=WRBNDpUhsJQ); publication: 2026-05-24T14:00:06Z; analysis: `analysis/WRBNDpUhsJQ.json`.
[^X4BwOu0GWb8]: [Your Coding Agent Just Got Cloned And Your Brain Isn't Ready - Rustin Banks, Google Jules](https://www.youtube.com/watch?v=X4BwOu0GWb8); publication: 2025-07-25T23:06:43Z; analysis: `analysis/X4BwOu0GWb8.json`.
[^YiFqcu9YA38]: [Dashboards Are Dead — Sarah Simionescu, Composio](https://www.youtube.com/watch?v=YiFqcu9YA38); publication: 2026-10-04T01:30:36Z; analysis: `analysis/YiFqcu9YA38.json`.
[^Z-c11pV_uvU]: [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Z-c11pV_uvU); publication: 2026-08-08T16:00:06Z; analysis: `analysis/Z-c11pV_uvU.json`.
[^ZIYYsAzaLlA]: [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](https://www.youtube.com/watch?v=ZIYYsAzaLlA); publication: 2026-08-28T14:00:06Z; analysis: `analysis/ZIYYsAzaLlA.json`.
[^_B4Pv9ttFgY]: [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](https://www.youtube.com/watch?v=_B4Pv9ttFgY); publication: 2026-06-05T17:00:06Z; analysis: `analysis/_B4Pv9ttFgY.json`.
[^bUJgirn4_yc]: [When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain](https://www.youtube.com/watch?v=bUJgirn4_yc); publication: 2026-07-20T06:25:07Z; analysis: `analysis/bUJgirn4_yc.json`.
[^ckLXb15BnM8]: [The Adversarial Path to the Personal Assistant: Sumit Agarwal](https://www.youtube.com/watch?v=ckLXb15BnM8); publication: 2025-02-15T19:30:06Z; analysis: `analysis/ckLXb15BnM8.json`.
[^esY99nYXxR4]: [How we solved Context Management in Agents — Sally-Ann Delucia](https://www.youtube.com/watch?v=esY99nYXxR4); publication: 2026-05-10T19:00:06Z; analysis: `analysis/esY99nYXxR4.json`.
[^fWXJM-J0ZB8]: [Frontier results, on device - RL Nabors, Arize](https://www.youtube.com/watch?v=fWXJM-J0ZB8); publication: 2026-06-29T03:30:03Z; analysis: `analysis/fWXJM-J0ZB8.json`.
[^fZH97QHHYjY]: [The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev](https://www.youtube.com/watch?v=fZH97QHHYjY); publication: 2026-09-16T13:30:32Z; analysis: `analysis/fZH97QHHYjY.json`.
[^khVX_BUnEwU]: [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](https://www.youtube.com/watch?v=khVX_BUnEwU); publication: 2026-07-22T20:00:06Z; analysis: `analysis/khVX_BUnEwU.json`.
[^lp0pswT_FEI]: [Just do it. (let your tools think for themselves) - Robert Chandler](https://www.youtube.com/watch?v=lp0pswT_FEI); publication: 2025-06-10T17:30:11Z; analysis: `analysis/lp0pswT_FEI.json`.
[^mav15aW9lLM]: [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard](https://www.youtube.com/watch?v=mav15aW9lLM); publication: 2026-08-19T18:30:15Z; analysis: `analysis/mav15aW9lLM.json`.
[^pAnLpiAG6Es]: [MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](https://www.youtube.com/watch?v=pAnLpiAG6Es); publication: 2026-10-02T14:00:05Z; analysis: `analysis/pAnLpiAG6Es.json`.
[^rbjWzZK2LU0]: [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](https://www.youtube.com/watch?v=rbjWzZK2LU0); publication: 2026-08-22T14:00:06Z; analysis: `analysis/rbjWzZK2LU0.json`.
[^rmvDxxNubIg]: [No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=rmvDxxNubIg); publication: 2025-12-02T22:52:58Z; analysis: `analysis/rmvDxxNubIg.json`.
[^tNAV259UhCM]: [From 15% to 90% GPU Utilization: Fix the Data Pipeline, Not the Model](https://www.youtube.com/watch?v=tNAV259UhCM); publication: 2026-10-10T01:30:14Z; analysis: `analysis/tNAV259UhCM.json`.
[^uiP88SpCi1Q]: [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](https://www.youtube.com/watch?v=uiP88SpCi1Q); publication: 2026-06-28T22:00:14Z; analysis: `analysis/uiP88SpCi1Q.json`.
[^wXVvfFMTyzY]: [A2A & MCP Workshop: Automating Business Processes with LLMs — Damien Murphy, Bench](https://www.youtube.com/watch?v=wXVvfFMTyzY); publication: 2025-07-26T14:15:05Z; analysis: `analysis/wXVvfFMTyzY.json`.
[^xo68uCibfm8]: [It’s Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners](https://www.youtube.com/watch?v=xo68uCibfm8); publication: 2026-09-09T13:30:27Z; analysis: `analysis/xo68uCibfm8.json`.
[^xyL2Ltkh-SA]: [How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](https://www.youtube.com/watch?v=xyL2Ltkh-SA); publication: 2026-07-24T21:00:00Z; analysis: `analysis/xyL2Ltkh-SA.json`.
[^ya_9_niq2as]: [Your LLM Ran Out of Knowledge — Now What?](https://www.youtube.com/watch?v=ya_9_niq2as); publication: 2025-02-22T17:00:06Z; analysis: `analysis/ya_9_niq2as.json`.
[^zKk7sDMGDEQ]: [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](https://www.youtube.com/watch?v=zKk7sDMGDEQ); publication: 2026-06-03T15:00:06Z; analysis: `analysis/zKk7sDMGDEQ.json`.
