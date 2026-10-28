---
{
  "type": "technique",
  "id": "event-driven-invocation",
  "title": "Trigger work from correlated events instead of repeatedly polling with agents",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-20T19:00:34Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "6pbQgnJ9Voc",
      "resource": "https://www.youtube.com/watch?v=6pbQgnJ9Voc",
      "title": "Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa",
      "author": "Jeffrey Wang, Exa",
      "last_modified": "2026-08-26T16:00:26Z",
      "analysis_file": "analysis/6pbQgnJ9Voc.json"
    },
    {
      "id": "L4I7WgiEquo",
      "resource": "https://www.youtube.com/watch?v=L4I7WgiEquo",
      "title": "AI in GTM at Notion — Flora Liu",
      "author": "Flora Liu",
      "last_modified": "2026-08-26T14:00:05Z",
      "analysis_file": "analysis/L4I7WgiEquo.json"
    },
    {
      "id": "NaOkR3VSfR4",
      "resource": "https://www.youtube.com/watch?v=NaOkR3VSfR4",
      "title": "Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya",
      "author": "Viren Baraiya",
      "last_modified": "2026-10-08T22:30:09Z",
      "analysis_file": "analysis/NaOkR3VSfR4.json"
    },
    {
      "id": "R3hTescenDw",
      "resource": "https://www.youtube.com/watch?v=R3hTescenDw",
      "title": "Which Jobs Can Be Replaced Today:  Fryderyk Wiatrowski and Peter Albert",
      "author": null,
      "last_modified": "2025-02-06T09:24:01Z",
      "analysis_file": "analysis/R3hTescenDw.json"
    },
    {
      "id": "RVxym6mmIns",
      "resource": "https://www.youtube.com/watch?v=RVxym6mmIns",
      "title": "How Forward Deployed Engineering is done at Cognition — Jia Wu",
      "author": "Jia Wu",
      "last_modified": "2026-07-28T20:00:06Z",
      "analysis_file": "analysis/RVxym6mmIns.json"
    },
    {
      "id": "X1kp-ABIIxQ",
      "resource": "https://www.youtube.com/watch?v=X1kp-ABIIxQ",
      "title": "Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest",
      "author": "Dan Farrelly, CTO, Inngest",
      "last_modified": "2026-07-21T03:14:22Z",
      "analysis_file": "analysis/X1kp-ABIIxQ.json"
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
      "id": "adfw3xJBx1o",
      "resource": "https://www.youtube.com/watch?v=adfw3xJBx1o",
      "title": "A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo",
      "author": "Felipe Felisola Caso & Francesco Galletta, Monzo",
      "last_modified": "2026-10-20T19:00:34Z",
      "analysis_file": "analysis/adfw3xJBx1o.json"
    },
    {
      "id": "b9UhZkKjX_A",
      "resource": "https://www.youtube.com/watch?v=b9UhZkKjX_A",
      "title": "From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot",
      "author": null,
      "last_modified": "2026-10-10T16:30:31Z",
      "analysis_file": "analysis/b9UhZkKjX_A.json"
    },
    {
      "id": "buHC7bQE1X4",
      "resource": "https://www.youtube.com/watch?v=buHC7bQE1X4",
      "title": "Get Out of the Model's Way — Kevin Hou, Google Antigravity",
      "author": "Kevin Hou, Google Antigravity",
      "last_modified": "2026-09-27T18:00:24Z",
      "analysis_file": "analysis/buHC7bQE1X4.json"
    },
    {
      "id": "c35YoMdnI78",
      "resource": "https://www.youtube.com/watch?v=c35YoMdnI78",
      "title": "The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "author": "Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "last_modified": "2026-07-17T21:00:06Z",
      "analysis_file": "analysis/c35YoMdnI78.json"
    },
    {
      "id": "cI7zfqusmFU",
      "resource": "https://www.youtube.com/watch?v=cI7zfqusmFU",
      "title": "Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate",
      "author": "Giselle van Dongen, Restate",
      "last_modified": "2026-09-14T15:30:30Z",
      "analysis_file": "analysis/cI7zfqusmFU.json"
    },
    {
      "id": "hd7TOvmyAxU",
      "resource": "https://www.youtube.com/watch?v=hd7TOvmyAxU",
      "title": "An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases",
      "author": "Tim Sweeney, Weights & Biases",
      "last_modified": "2026-09-26T14:30:38Z",
      "analysis_file": "analysis/hd7TOvmyAxU.json"
    },
    {
      "id": "iH_wV8BbS24",
      "resource": "https://www.youtube.com/watch?v=iH_wV8BbS24",
      "title": "Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands",
      "author": "Robert Brennan, OpenHands",
      "last_modified": "2026-10-12T05:10:18Z",
      "analysis_file": "analysis/iH_wV8BbS24.json"
    },
    {
      "id": "kTnfJszFxCg",
      "resource": "https://www.youtube.com/watch?v=kTnfJszFxCg",
      "title": "3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph",
      "author": "Harrison Chase, LangChain/LangGraph",
      "last_modified": "2025-07-23T15:51:25Z",
      "analysis_file": "analysis/kTnfJszFxCg.json"
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
      "id": "p7gaxmCUiIU",
      "resource": "https://www.youtube.com/watch?v=p7gaxmCUiIU",
      "title": "Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase",
      "author": "Shubhankar Srivastava, Browserbase",
      "last_modified": "2026-10-11T21:30:05Z",
      "analysis_file": "analysis/p7gaxmCUiIU.json"
    },
    {
      "id": "s4r6nk5WsZw",
      "resource": "https://www.youtube.com/watch?v=s4r6nk5WsZw",
      "title": "MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal",
      "author": "Cornelia Davis, Temporal",
      "last_modified": "2026-08-02T20:00:06Z",
      "analysis_file": "analysis/s4r6nk5WsZw.json"
    },
    {
      "id": "uFPAtKIN-FQ",
      "resource": "https://www.youtube.com/watch?v=uFPAtKIN-FQ",
      "title": "Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri",
      "author": null,
      "last_modified": "2025-06-11T16:57:37Z",
      "analysis_file": "analysis/uFPAtKIN-FQ.json"
    },
    {
      "id": "uU5Gv2h8-9g",
      "resource": "https://www.youtube.com/watch?v=uU5Gv2h8-9g",
      "title": "Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison",
      "author": "Cat Wu & Thariq Shihipar ft Simon Willison",
      "last_modified": "2026-07-15T15:05:06Z",
      "analysis_file": "analysis/uU5Gv2h8-9g.json"
    },
    {
      "id": "vi-2nasppAg",
      "resource": "https://www.youtube.com/watch?v=vi-2nasppAg",
      "title": "Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate",
      "author": "Jonas Templestein, Iterate",
      "last_modified": "2026-05-14T14:00:06Z",
      "analysis_file": "analysis/vi-2nasppAg.json"
    },
    {
      "id": "zTZ0qunQXnM",
      "resource": "https://www.youtube.com/watch?v=zTZ0qunQXnM",
      "title": "From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data",
      "author": "Rafael Levi, Bright Data",
      "last_modified": "2026-06-07T14:00:12Z",
      "analysis_file": "analysis/zTZ0qunQXnM.json"
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

# Trigger work from correlated events instead of repeatedly polling with agents

## What

Trigger work from correlated events instead of repeatedly polling with agents

Alerts and workflow events can wake an agent only when a state transition needs interpretation.

## Evidence

Source analysis [^6pbQgnJ9Voc]; no independently matched timestamped quote published.

Source analysis [^L4I7WgiEquo]; no independently matched timestamped quote published.

> agents, right? Agents that are listening on various events. Um to give you an
> — 02:08 [^NaOkR3VSfR4]

Source analysis [^R3hTescenDw]; no independently matched timestamped quote published.

Source analysis [^RVxym6mmIns]; no independently matched timestamped quote published.

Source analysis [^X1kp-ABIIxQ]; no independently matched timestamped quote published.

Source analysis [^X4BwOu0GWb8]; no independently matched timestamped quote published.

Source analysis [^adfw3xJBx1o]; no independently matched timestamped quote published.

Source analysis [^b9UhZkKjX_A]; no independently matched timestamped quote published.

Source analysis [^buHC7bQE1X4]; no independently matched timestamped quote published.

> don't have to tell it, "Hey, go check the PR comments and fix them." and then
> — 29:59 [^c35YoMdnI78]

> server, restate actually pushes the invocations and the benefit you get from
> — 18:26 [^cI7zfqusmFU]

Source analysis [^hd7TOvmyAxU]; no independently matched timestamped quote published.

Source analysis [^iH_wV8BbS24]; no independently matched timestamped quote published.

> ambient agents are triggered by events that lets us scale ourselves. Instead of
> — 14:19 [^kTnfJszFxCg]

> ActiveGraph. They all communicate through this shared state, and that's
> — 03:20 [^khVX_BUnEwU]

> the current working theory that we have right now is you don't want to waste
> — 38:13 [^p7gaxmCUiIU]

Source analysis [^s4r6nk5WsZw]; no independently matched timestamped quote published.

Source analysis [^uFPAtKIN-FQ]; no independently matched timestamped quote published.

> you can tell claw tag, hey, monitor every bug report in this channel, put up
> — 07:17 [^uU5Gv2h8-9g]

Source analysis [^vi-2nasppAg]; no independently matched timestamped quote published.

Source analysis [^zTZ0qunQXnM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^6pbQgnJ9Voc]: [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](https://www.youtube.com/watch?v=6pbQgnJ9Voc); publication: 2026-08-26T16:00:26Z; analysis: `analysis/6pbQgnJ9Voc.json`.
[^L4I7WgiEquo]: [AI in GTM at Notion — Flora Liu](https://www.youtube.com/watch?v=L4I7WgiEquo); publication: 2026-08-26T14:00:05Z; analysis: `analysis/L4I7WgiEquo.json`.
[^NaOkR3VSfR4]: [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](https://www.youtube.com/watch?v=NaOkR3VSfR4); publication: 2026-10-08T22:30:09Z; analysis: `analysis/NaOkR3VSfR4.json`.
[^R3hTescenDw]: [Which Jobs Can Be Replaced Today:  Fryderyk Wiatrowski and Peter Albert](https://www.youtube.com/watch?v=R3hTescenDw); publication: 2025-02-06T09:24:01Z; analysis: `analysis/R3hTescenDw.json`.
[^RVxym6mmIns]: [How Forward Deployed Engineering is done at Cognition — Jia Wu](https://www.youtube.com/watch?v=RVxym6mmIns); publication: 2026-07-28T20:00:06Z; analysis: `analysis/RVxym6mmIns.json`.
[^X1kp-ABIIxQ]: [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](https://www.youtube.com/watch?v=X1kp-ABIIxQ); publication: 2026-07-21T03:14:22Z; analysis: `analysis/X1kp-ABIIxQ.json`.
[^X4BwOu0GWb8]: [Your Coding Agent Just Got Cloned And Your Brain Isn't Ready - Rustin Banks, Google Jules](https://www.youtube.com/watch?v=X4BwOu0GWb8); publication: 2025-07-25T23:06:43Z; analysis: `analysis/X4BwOu0GWb8.json`.
[^adfw3xJBx1o]: [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](https://www.youtube.com/watch?v=adfw3xJBx1o); publication: 2026-10-20T19:00:34Z; analysis: `analysis/adfw3xJBx1o.json`.
[^b9UhZkKjX_A]: [From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot](https://www.youtube.com/watch?v=b9UhZkKjX_A); publication: 2026-10-10T16:30:31Z; analysis: `analysis/b9UhZkKjX_A.json`.
[^buHC7bQE1X4]: [Get Out of the Model's Way — Kevin Hou, Google Antigravity](https://www.youtube.com/watch?v=buHC7bQE1X4); publication: 2026-09-27T18:00:24Z; analysis: `analysis/buHC7bQE1X4.json`.
[^c35YoMdnI78]: [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78); publication: 2026-07-17T21:00:06Z; analysis: `analysis/c35YoMdnI78.json`.
[^cI7zfqusmFU]: [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](https://www.youtube.com/watch?v=cI7zfqusmFU); publication: 2026-09-14T15:30:30Z; analysis: `analysis/cI7zfqusmFU.json`.
[^hd7TOvmyAxU]: [An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases](https://www.youtube.com/watch?v=hd7TOvmyAxU); publication: 2026-09-26T14:30:38Z; analysis: `analysis/hd7TOvmyAxU.json`.
[^iH_wV8BbS24]: [Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands](https://www.youtube.com/watch?v=iH_wV8BbS24); publication: 2026-10-12T05:10:18Z; analysis: `analysis/iH_wV8BbS24.json`.
[^kTnfJszFxCg]: [3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph](https://www.youtube.com/watch?v=kTnfJszFxCg); publication: 2025-07-23T15:51:25Z; analysis: `analysis/kTnfJszFxCg.json`.
[^khVX_BUnEwU]: [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](https://www.youtube.com/watch?v=khVX_BUnEwU); publication: 2026-07-22T20:00:06Z; analysis: `analysis/khVX_BUnEwU.json`.
[^p7gaxmCUiIU]: [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](https://www.youtube.com/watch?v=p7gaxmCUiIU); publication: 2026-10-11T21:30:05Z; analysis: `analysis/p7gaxmCUiIU.json`.
[^s4r6nk5WsZw]: [MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal](https://www.youtube.com/watch?v=s4r6nk5WsZw); publication: 2026-08-02T20:00:06Z; analysis: `analysis/s4r6nk5WsZw.json`.
[^uFPAtKIN-FQ]: [Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri](https://www.youtube.com/watch?v=uFPAtKIN-FQ); publication: 2025-06-11T16:57:37Z; analysis: `analysis/uFPAtKIN-FQ.json`.
[^uU5Gv2h8-9g]: [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](https://www.youtube.com/watch?v=uU5Gv2h8-9g); publication: 2026-07-15T15:05:06Z; analysis: `analysis/uU5Gv2h8-9g.json`.
[^vi-2nasppAg]: [Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate](https://www.youtube.com/watch?v=vi-2nasppAg); publication: 2026-05-14T14:00:06Z; analysis: `analysis/vi-2nasppAg.json`.
[^zTZ0qunQXnM]: [From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](https://www.youtube.com/watch?v=zTZ0qunQXnM); publication: 2026-06-07T14:00:12Z; analysis: `analysis/zTZ0qunQXnM.json`.
