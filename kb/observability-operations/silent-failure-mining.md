---
{
  "type": "technique",
  "id": "silent-failure-mining",
  "title": "Inspect nominally successful traces for silent failures and repeated friction",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-10-11T18:00:10Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "0RNNfxpdbQk",
      "resource": "https://www.youtube.com/watch?v=0RNNfxpdbQk",
      "title": "Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest",
      "author": "Drasko Profirovic, Pinterest",
      "last_modified": "2026-07-20T06:24:50Z",
      "analysis_file": "analysis/0RNNfxpdbQk.json"
    },
    {
      "id": "7_WhRAuP2Wg",
      "resource": "https://www.youtube.com/watch?v=7_WhRAuP2Wg",
      "title": "Building and Scaling an AI Agent Swarm of low latency real time voice bots: Damien Murphy",
      "author": null,
      "last_modified": "2024-10-08T18:28:46Z",
      "analysis_file": "analysis/7_WhRAuP2Wg.json"
    },
    {
      "id": "89aQ7T6cMwA",
      "resource": "https://www.youtube.com/watch?v=89aQ7T6cMwA",
      "title": "How to Fail at AI Strategy: Hamel Husain & Greg Ceccarelli",
      "author": null,
      "last_modified": "2025-04-13T16:19:16Z",
      "analysis_file": "analysis/89aQ7T6cMwA.json"
    },
    {
      "id": "BOCjybvJYM4",
      "resource": "https://www.youtube.com/watch?v=BOCjybvJYM4",
      "title": "Continuously Improving Agents with Langfuse — Annabell Schäfer & Lotte Verheyden, ClickHouse",
      "author": "Annabell Schäfer & Lotte Verheyden, ClickHouse",
      "last_modified": "2026-10-11T18:00:10Z",
      "analysis_file": "analysis/BOCjybvJYM4.json"
    },
    {
      "id": "F0TNSmbo5hE",
      "resource": "https://www.youtube.com/watch?v=F0TNSmbo5hE",
      "title": "From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-05T23:00:09Z",
      "analysis_file": "analysis/F0TNSmbo5hE.json"
    },
    {
      "id": "HEFSExa0xl0",
      "resource": "https://www.youtube.com/watch?v=HEFSExa0xl0",
      "title": "Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs",
      "author": "Nuno Campos, Witan Labs",
      "last_modified": "2026-07-08T09:03:25Z",
      "analysis_file": "analysis/HEFSExa0xl0.json"
    },
    {
      "id": "I2LL_wd89-A",
      "resource": "https://www.youtube.com/watch?v=I2LL_wd89-A",
      "title": "How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner",
      "author": "Harald Kirschner",
      "last_modified": "2026-10-03T15:00:10Z",
      "analysis_file": "analysis/I2LL_wd89-A.json"
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
      "id": "LqLoYksJ6do",
      "resource": "https://www.youtube.com/watch?v=LqLoYksJ6do",
      "title": "We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3",
      "author": "Moritz Johner, Form3",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/LqLoYksJ6do.json"
    },
    {
      "id": "Lrw0jqBNaw0",
      "resource": "https://www.youtube.com/watch?v=Lrw0jqBNaw0",
      "title": "The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph",
      "author": "Stephanie Jarmak, Sourcegraph",
      "last_modified": "2026-08-26T17:00:32Z",
      "analysis_file": "analysis/Lrw0jqBNaw0.json"
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
      "id": "PNjMwdCo_YM",
      "resource": "https://www.youtube.com/watch?v=PNjMwdCo_YM",
      "title": "BotDojo Launch: Enhancing AI Assistants with Evaluations and Synthetic Data",
      "author": null,
      "last_modified": "2025-02-05T11:18:34Z",
      "analysis_file": "analysis/PNjMwdCo_YM.json"
    },
    {
      "id": "QuuIywMG4s8",
      "resource": "https://www.youtube.com/watch?v=QuuIywMG4s8",
      "title": "Evals Are Broken, Use Them Anyway — Ara Khan, Cline",
      "author": "Ara Khan, Cline",
      "last_modified": "2026-06-06T16:00:00Z",
      "analysis_file": "analysis/QuuIywMG4s8.json"
    },
    {
      "id": "XBaznoTRDFI",
      "resource": "https://www.youtube.com/watch?v=XBaznoTRDFI",
      "title": "How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust",
      "author": "Phil Hetzel, Braintrust",
      "last_modified": "2026-05-28T23:00:06Z",
      "analysis_file": "analysis/XBaznoTRDFI.json"
    },
    {
      "id": "_fQ7Z_Wfouk",
      "resource": "https://www.youtube.com/watch?v=_fQ7Z_Wfouk",
      "title": "Why building eval platforms is hard — Phil Hetzel, Braintrust",
      "author": "Phil Hetzel, Braintrust",
      "last_modified": "2026-04-28T16:00:06Z",
      "analysis_file": "analysis/_fQ7Z_Wfouk.json"
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
      "id": "atwSCxWFVMg",
      "resource": "https://www.youtube.com/watch?v=atwSCxWFVMg",
      "title": "GPT Web App Generator - 10,000 apps created in a month: Matija Sosic",
      "author": "10,000 apps created in a month: Matija Sosic",
      "last_modified": "2024-01-26T20:51:42Z",
      "analysis_file": "analysis/atwSCxWFVMg.json"
    },
    {
      "id": "btxG75rNJC4",
      "resource": "https://www.youtube.com/watch?v=btxG75rNJC4",
      "title": "Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer",
      "author": "Asaf Gardin & Yuval Belfer",
      "last_modified": "2026-09-19T18:30:06Z",
      "analysis_file": "analysis/btxG75rNJC4.json"
    },
    {
      "id": "btxGmN8RvNU",
      "resource": "https://www.youtube.com/watch?v=btxGmN8RvNU",
      "title": "Your Agent's Biggest Lie: \"I Searched the Web\" — Rafael Levi, Bright Data",
      "author": "Rafael Levi, Bright Data",
      "last_modified": "2026-06-17T13:00:06Z",
      "analysis_file": "analysis/btxGmN8RvNU.json"
    },
    {
      "id": "cKhpeEBnT1o",
      "resource": "https://www.youtube.com/watch?v=cKhpeEBnT1o",
      "title": "Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa",
      "author": "Jakub Hojsan, Exa",
      "last_modified": "2026-10-02T15:30:31Z",
      "analysis_file": "analysis/cKhpeEBnT1o.json"
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
      "id": "fnuNVFgLjHA",
      "resource": "https://www.youtube.com/watch?v=fnuNVFgLjHA",
      "title": "Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI",
      "author": "Fuad Ali, Arize AI",
      "last_modified": "2026-10-11T15:30:31Z",
      "analysis_file": "analysis/fnuNVFgLjHA.json"
    },
    {
      "id": "hfEczxdNyvU",
      "resource": "https://www.youtube.com/watch?v=hfEczxdNyvU",
      "title": "Advanced Workshop: Mastering AI Observability — Doug Guthrie, Braintrust",
      "author": "Doug Guthrie, Braintrust",
      "last_modified": "2026-10-06T01:00:25Z",
      "analysis_file": "analysis/hfEczxdNyvU.json"
    },
    {
      "id": "iRcX54EO5g8",
      "resource": "https://www.youtube.com/watch?v=iRcX54EO5g8",
      "title": "Your agent is blindfolded — Johan Lajili, Poolside AI",
      "author": "Johan Lajili, Poolside AI",
      "last_modified": "2026-07-08T13:45:06Z",
      "analysis_file": "analysis/iRcX54EO5g8.json"
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
      "id": "kZsf_Sfm7RU",
      "resource": "https://www.youtube.com/watch?v=kZsf_Sfm7RU",
      "title": "The Missing Layer After Launch - Raphael Kalandadze, Wandero AI",
      "author": "Raphael Kalandadze, Wandero AI",
      "last_modified": "2026-07-05T03:15:05Z",
      "analysis_file": "analysis/kZsf_Sfm7RU.json"
    },
    {
      "id": "pFsfax19yOM",
      "resource": "https://www.youtube.com/watch?v=pFsfax19yOM",
      "title": "Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser",
      "author": "Nick Nisi and Zack Proser",
      "last_modified": "2026-05-06T17:00:06Z",
      "analysis_file": "analysis/pFsfax19yOM.json"
    },
    {
      "id": "pQz-PgA1eJw",
      "resource": "https://www.youtube.com/watch?v=pQz-PgA1eJw",
      "title": "The New Lean Startup — Sid Bendre, Oleve",
      "author": "Sid Bendre, Oleve",
      "last_modified": "2025-07-01T16:57:59Z",
      "analysis_file": "analysis/pQz-PgA1eJw.json"
    },
    {
      "id": "pSto5YaNGUo",
      "resource": "https://www.youtube.com/watch?v=pSto5YaNGUo",
      "title": "The Agentic AI Engineer - Benedikt Sanftl, Mutagent",
      "author": "Benedikt Sanftl, Mutagent",
      "last_modified": "2026-06-29T01:30:19Z",
      "analysis_file": "analysis/pSto5YaNGUo.json"
    },
    {
      "id": "q2JrUKBMf0w",
      "resource": "https://www.youtube.com/watch?v=q2JrUKBMf0w",
      "title": "The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI",
      "author": "Aparna Dhinakaran, Arize AI",
      "last_modified": "2026-07-24T20:00:06Z",
      "analysis_file": "analysis/q2JrUKBMf0w.json"
    },
    {
      "id": "qZj7sqmidqA",
      "resource": "https://www.youtube.com/watch?v=qZj7sqmidqA",
      "title": "From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-05T22:00:36Z",
      "analysis_file": "analysis/qZj7sqmidqA.json"
    },
    {
      "id": "qqXdLf3wy1E",
      "resource": "https://www.youtube.com/watch?v=qqXdLf3wy1E",
      "title": "Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant",
      "author": "Jesse Hu, Abundant",
      "last_modified": "2025-11-24T20:16:38Z",
      "analysis_file": "analysis/qqXdLf3wy1E.json"
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
      "id": "rcsliSIy_YU",
      "resource": "https://www.youtube.com/watch?v=rcsliSIy_YU",
      "title": "Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands",
      "author": "Robert Brennan, OpenHands",
      "last_modified": "2026-01-08T16:30:23Z",
      "analysis_file": "analysis/rcsliSIy_YU.json"
    },
    {
      "id": "s-glGHAa1a4",
      "resource": "https://www.youtube.com/watch?v=s-glGHAa1a4",
      "title": "An AI Future Without the Lock-In — Remy Guercio, Tailscale",
      "author": "Remy Guercio, Tailscale",
      "last_modified": "2026-10-11T00:00:35Z",
      "analysis_file": "analysis/s-glGHAa1a4.json"
    },
    {
      "id": "so9l_MwS2yg",
      "resource": "https://www.youtube.com/watch?v=so9l_MwS2yg",
      "title": "Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS",
      "author": "Zack Proser, WorkOS",
      "last_modified": "2026-06-11T14:00:06Z",
      "analysis_file": "analysis/so9l_MwS2yg.json"
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

# Inspect nominally successful traces for silent failures and repeated friction

## What

Inspect nominally successful traces for silent failures and repeated friction

No error spans: every call returned 200. The real signals were quality anomalies: 42% of searches returned zero results, tool calls with every argument null, a search tool that 'suspiciously' returned in 1 ms. An agent (Signal, every 6 h) reads traces at scale, groups identical failures ('a hundred that are the same failure') and files one issue per cluster.

## Evidence

Source analysis [^0RNNfxpdbQk]; no independently matched timestamped quote published.

Source analysis [^7_WhRAuP2Wg]; no independently matched timestamped quote published.

Source analysis [^89aQ7T6cMwA]; no independently matched timestamped quote published.

Source analysis [^BOCjybvJYM4]; no independently matched timestamped quote published.

Source analysis [^F0TNSmbo5hE]; no independently matched timestamped quote published.

Source analysis [^HEFSExa0xl0]; no independently matched timestamped quote published.

Source analysis [^I2LL_wd89-A]; no independently matched timestamped quote published.

> removing duplicates and investigating and creating a PR for all these issues
> — 17:00 [^KA5kPbdkK2E]

> retrospective. What went well, what went wrong, what tools are missing, and what
> — 08:44 [^LqLoYksJ6do]

Source analysis [^Lrw0jqBNaw0]; no independently matched timestamped quote published.

> your environment contains is observed. Second, it runs reflection with an LLM
> — 08:41 [^OA-Mc60Rboo]

Source analysis [^PNjMwdCo_YM]; no independently matched timestamped quote published.

Source analysis [^QuuIywMG4s8]; no independently matched timestamped quote published.

Source analysis [^XBaznoTRDFI]; no independently matched timestamped quote published.

Source analysis [^_fQ7Z_Wfouk]; no independently matched timestamped quote published.

> analyze all these traces. We do clustering of the failure modes, right?
> — 20:44 [^aHhB3sjGjkI]

Source analysis [^atwSCxWFVMg]; no independently matched timestamped quote published.

Source analysis [^btxG75rNJC4]; no independently matched timestamped quote published.

Source analysis [^btxGmN8RvNU]; no independently matched timestamped quote published.

Source analysis [^cKhpeEBnT1o]; no independently matched timestamped quote published.

> and you need to fight as hard as you can to remove all friction and looking at
> — 08:24 [^eLXF0VojuSs]

Source analysis [^fnuNVFgLjHA]; no independently matched timestamped quote published.

Source analysis [^hfEczxdNyvU]; no independently matched timestamped quote published.

> Is there anything that you keep doing over and over like running storybooks?
> — 09:12 [^iRcX54EO5g8]

Source analysis [^iheWKg2Tkrk]; no independently matched timestamped quote published.

Source analysis [^kZsf_Sfm7RU]; no independently matched timestamped quote published.

> "Oh, it's going and doing like 10 tool calls." Maybe you could like
> — 1:18:14 [^pFsfax19yOM]

Source analysis [^pQz-PgA1eJw]; no independently matched timestamped quote published.

> trigger the diagnostics, you can also specify an issue that you have seen
> — 30:58 [^pSto5YaNGUo]

> tool to solve a different type of problem. Agent as a judge is about
> — 04:04 [^q2JrUKBMf0w]

> you should resist that. When you find a failure, you should ask why it failed.
> — 46:49 [^qZj7sqmidqA]

Source analysis [^qqXdLf3wy1E]; no independently matched timestamped quote published.

> actually an infrastructure failure that was causing the same test failure
> — 11:43 [^rbjWzZK2LU0]

> the agent decides to skip a test uh due to whatever reason, it shouldn't have.
> — 06:43 [^rbjWzZK2LU0]

Source analysis [^rcsliSIy_YU]; no independently matched timestamped quote published.

Source analysis [^s-glGHAa1a4]; no independently matched timestamped quote published.

Source analysis [^so9l_MwS2yg]; no independently matched timestamped quote published.

Source analysis [^wcUJWP6WpGM]; no independently matched timestamped quote published.

Source analysis [^xo68uCibfm8]; no independently matched timestamped quote published.

> point so you should focus on patterns rather than isolated runs so a tempting
> — 14:50 [^xyL2Ltkh-SA]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^0RNNfxpdbQk]: [Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest](https://www.youtube.com/watch?v=0RNNfxpdbQk); publication: 2026-07-20T06:24:50Z; analysis: `analysis/0RNNfxpdbQk.json`.
[^7_WhRAuP2Wg]: [Building and Scaling an AI Agent Swarm of low latency real time voice bots: Damien Murphy](https://www.youtube.com/watch?v=7_WhRAuP2Wg); publication: 2024-10-08T18:28:46Z; analysis: `analysis/7_WhRAuP2Wg.json`.
[^89aQ7T6cMwA]: [How to Fail at AI Strategy: Hamel Husain & Greg Ceccarelli](https://www.youtube.com/watch?v=89aQ7T6cMwA); publication: 2025-04-13T16:19:16Z; analysis: `analysis/89aQ7T6cMwA.json`.
[^BOCjybvJYM4]: [Continuously Improving Agents with Langfuse — Annabell Schäfer & Lotte Verheyden, ClickHouse](https://www.youtube.com/watch?v=BOCjybvJYM4); publication: 2026-10-11T18:00:10Z; analysis: `analysis/BOCjybvJYM4.json`.
[^F0TNSmbo5hE]: [From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=F0TNSmbo5hE); publication: 2026-10-05T23:00:09Z; analysis: `analysis/F0TNSmbo5hE.json`.
[^HEFSExa0xl0]: [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](https://www.youtube.com/watch?v=HEFSExa0xl0); publication: 2026-07-08T09:03:25Z; analysis: `analysis/HEFSExa0xl0.json`.
[^I2LL_wd89-A]: [How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner](https://www.youtube.com/watch?v=I2LL_wd89-A); publication: 2026-10-03T15:00:10Z; analysis: `analysis/I2LL_wd89-A.json`.
[^KA5kPbdkK2E]: [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](https://www.youtube.com/watch?v=KA5kPbdkK2E); publication: 2026-06-02T16:00:33Z; analysis: `analysis/KA5kPbdkK2E.json`.
[^LqLoYksJ6do]: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](https://www.youtube.com/watch?v=LqLoYksJ6do); publication: 2026-07-20T17:17:53Z; analysis: `analysis/LqLoYksJ6do.json`.
[^Lrw0jqBNaw0]: [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](https://www.youtube.com/watch?v=Lrw0jqBNaw0); publication: 2026-08-26T17:00:32Z; analysis: `analysis/Lrw0jqBNaw0.json`.
[^OA-Mc60Rboo]: [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](https://www.youtube.com/watch?v=OA-Mc60Rboo); publication: 2026-09-26T17:00:06Z; analysis: `analysis/OA-Mc60Rboo.json`.
[^PNjMwdCo_YM]: [BotDojo Launch: Enhancing AI Assistants with Evaluations and Synthetic Data](https://www.youtube.com/watch?v=PNjMwdCo_YM); publication: 2025-02-05T11:18:34Z; analysis: `analysis/PNjMwdCo_YM.json`.
[^QuuIywMG4s8]: [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](https://www.youtube.com/watch?v=QuuIywMG4s8); publication: 2026-06-06T16:00:00Z; analysis: `analysis/QuuIywMG4s8.json`.
[^XBaznoTRDFI]: [How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust](https://www.youtube.com/watch?v=XBaznoTRDFI); publication: 2026-05-28T23:00:06Z; analysis: `analysis/XBaznoTRDFI.json`.
[^_fQ7Z_Wfouk]: [Why building eval platforms is hard — Phil Hetzel, Braintrust](https://www.youtube.com/watch?v=_fQ7Z_Wfouk); publication: 2026-04-28T16:00:06Z; analysis: `analysis/_fQ7Z_Wfouk.json`.
[^aHhB3sjGjkI]: [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI); publication: 2026-06-28T16:00:34Z; analysis: `analysis/aHhB3sjGjkI.json`.
[^atwSCxWFVMg]: [GPT Web App Generator - 10,000 apps created in a month: Matija Sosic](https://www.youtube.com/watch?v=atwSCxWFVMg); publication: 2024-01-26T20:51:42Z; analysis: `analysis/atwSCxWFVMg.json`.
[^btxG75rNJC4]: [Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer](https://www.youtube.com/watch?v=btxG75rNJC4); publication: 2026-09-19T18:30:06Z; analysis: `analysis/btxG75rNJC4.json`.
[^btxGmN8RvNU]: [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](https://www.youtube.com/watch?v=btxGmN8RvNU); publication: 2026-06-17T13:00:06Z; analysis: `analysis/btxGmN8RvNU.json`.
[^cKhpeEBnT1o]: [Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa](https://www.youtube.com/watch?v=cKhpeEBnT1o); publication: 2026-10-02T15:30:31Z; analysis: `analysis/cKhpeEBnT1o.json`.
[^eLXF0VojuSs]: [How to Construct Domain Specific LLM Evaluation Systems: Hamel Husain and Emil Sedgh](https://www.youtube.com/watch?v=eLXF0VojuSs); publication: 2024-09-19T16:47:24Z; analysis: `analysis/eLXF0VojuSs.json`.
[^fnuNVFgLjHA]: [Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI](https://www.youtube.com/watch?v=fnuNVFgLjHA); publication: 2026-10-11T15:30:31Z; analysis: `analysis/fnuNVFgLjHA.json`.
[^hfEczxdNyvU]: [Advanced Workshop: Mastering AI Observability — Doug Guthrie, Braintrust](https://www.youtube.com/watch?v=hfEczxdNyvU); publication: 2026-10-06T01:00:25Z; analysis: `analysis/hfEczxdNyvU.json`.
[^iRcX54EO5g8]: [Your agent is blindfolded — Johan Lajili, Poolside AI](https://www.youtube.com/watch?v=iRcX54EO5g8); publication: 2026-07-08T13:45:06Z; analysis: `analysis/iRcX54EO5g8.json`.
[^iheWKg2Tkrk]: [Ship Production Software in Minutes, Not Months — Eno Reyes, Factory](https://www.youtube.com/watch?v=iheWKg2Tkrk); publication: 2025-07-25T23:11:00Z; analysis: `analysis/iheWKg2Tkrk.json`.
[^kZsf_Sfm7RU]: [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](https://www.youtube.com/watch?v=kZsf_Sfm7RU); publication: 2026-07-05T03:15:05Z; analysis: `analysis/kZsf_Sfm7RU.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
[^pQz-PgA1eJw]: [The New Lean Startup — Sid Bendre, Oleve](https://www.youtube.com/watch?v=pQz-PgA1eJw); publication: 2025-07-01T16:57:59Z; analysis: `analysis/pQz-PgA1eJw.json`.
[^pSto5YaNGUo]: [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](https://www.youtube.com/watch?v=pSto5YaNGUo); publication: 2026-06-29T01:30:19Z; analysis: `analysis/pSto5YaNGUo.json`.
[^q2JrUKBMf0w]: [The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI](https://www.youtube.com/watch?v=q2JrUKBMf0w); publication: 2026-07-24T20:00:06Z; analysis: `analysis/q2JrUKBMf0w.json`.
[^qZj7sqmidqA]: [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=qZj7sqmidqA); publication: 2026-10-05T22:00:36Z; analysis: `analysis/qZj7sqmidqA.json`.
[^qqXdLf3wy1E]: [Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant](https://www.youtube.com/watch?v=qqXdLf3wy1E); publication: 2025-11-24T20:16:38Z; analysis: `analysis/qqXdLf3wy1E.json`.
[^rbjWzZK2LU0]: [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](https://www.youtube.com/watch?v=rbjWzZK2LU0); publication: 2026-08-22T14:00:06Z; analysis: `analysis/rbjWzZK2LU0.json`.
[^rcsliSIy_YU]: [Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=rcsliSIy_YU); publication: 2026-01-08T16:30:23Z; analysis: `analysis/rcsliSIy_YU.json`.
[^s-glGHAa1a4]: [An AI Future Without the Lock-In — Remy Guercio, Tailscale](https://www.youtube.com/watch?v=s-glGHAa1a4); publication: 2026-10-11T00:00:35Z; analysis: `analysis/s-glGHAa1a4.json`.
[^so9l_MwS2yg]: [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](https://www.youtube.com/watch?v=so9l_MwS2yg); publication: 2026-06-11T14:00:06Z; analysis: `analysis/so9l_MwS2yg.json`.
[^wcUJWP6WpGM]: [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](https://www.youtube.com/watch?v=wcUJWP6WpGM); publication: 2026-06-04T14:00:06Z; analysis: `analysis/wcUJWP6WpGM.json`.
[^xo68uCibfm8]: [It’s Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners](https://www.youtube.com/watch?v=xo68uCibfm8); publication: 2026-09-09T13:30:27Z; analysis: `analysis/xo68uCibfm8.json`.
[^xyL2Ltkh-SA]: [How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](https://www.youtube.com/watch?v=xyL2Ltkh-SA); publication: 2026-07-24T21:00:00Z; analysis: `analysis/xyL2Ltkh-SA.json`.
