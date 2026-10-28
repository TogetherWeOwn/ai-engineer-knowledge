---
{
  "type": "technique",
  "id": "least-privilege-capabilities",
  "title": "Grant task-scoped read, write and execution capabilities",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-16T19:00:10Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-CnA2lGfymY",
      "resource": "https://www.youtube.com/watch?v=-CnA2lGfymY",
      "title": "\"I've never seen anything scarier than an LLM with tool calls.\" — Erik Meijer aka @HeadinTheBox",
      "author": "Erik Meijer aka @HeadinTheBox",
      "last_modified": "2026-07-13T19:25:09Z",
      "analysis_file": "analysis/-CnA2lGfymY.json"
    },
    {
      "id": "0uC6u0lJJl4",
      "resource": "https://www.youtube.com/watch?v=0uC6u0lJJl4",
      "title": "Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL",
      "author": "Tanmai Gopal, PromptQL",
      "last_modified": "2026-09-03T15:30:26Z",
      "analysis_file": "analysis/0uC6u0lJJl4.json"
    },
    {
      "id": "33Oct2hqGnk",
      "resource": "https://www.youtube.com/watch?v=33Oct2hqGnk",
      "title": "Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS",
      "author": "Sandhya Subramani, AWS",
      "last_modified": "2026-10-04T21:00:13Z",
      "analysis_file": "analysis/33Oct2hqGnk.json"
    },
    {
      "id": "5eJqXtevlXg",
      "resource": "https://www.youtube.com/watch?v=5eJqXtevlXg",
      "title": "Hacking Subagents Into Codex CLI — Brian John, Betterup",
      "author": "Brian John, Betterup",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/5eJqXtevlXg.json"
    },
    {
      "id": "6pbQgnJ9Voc",
      "resource": "https://www.youtube.com/watch?v=6pbQgnJ9Voc",
      "title": "Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa",
      "author": "Jeffrey Wang, Exa",
      "last_modified": "2026-08-26T16:00:26Z",
      "analysis_file": "analysis/6pbQgnJ9Voc.json"
    },
    {
      "id": "AvVoJBxgSQk",
      "resource": "https://www.youtube.com/watch?v=AvVoJBxgSQk",
      "title": "Agentic GraphRAG: AI’s Logical Edge — Stephen Chin, Neo4j",
      "author": "Stephen Chin, Neo4j",
      "last_modified": "2025-07-21T17:15:06Z",
      "analysis_file": "analysis/AvVoJBxgSQk.json"
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
      "id": "DdaAABdAqZY",
      "resource": "https://www.youtube.com/watch?v=DdaAABdAqZY",
      "title": "Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft",
      "author": "Christopher Harrison, Microsoft",
      "last_modified": "2025-07-26T07:00:13Z",
      "analysis_file": "analysis/DdaAABdAqZY.json"
    },
    {
      "id": "Djv8Sp11UjI",
      "resource": "https://www.youtube.com/watch?v=Djv8Sp11UjI",
      "title": "The Current State of Browser Agents - Jerry Wu and Wyatt Marshall",
      "author": "Jerry Wu and Wyatt Marshall",
      "last_modified": "2025-06-03T22:22:26Z",
      "analysis_file": "analysis/Djv8Sp11UjI.json"
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
      "id": "G1hhmz6mXT0",
      "resource": "https://www.youtube.com/watch?v=G1hhmz6mXT0",
      "title": "Collaborating with Agents in your Software Dev Workflow - Jon Peck & Christopher Harrison, Microsoft",
      "author": "Jon Peck & Christopher Harrison, Microsoft",
      "last_modified": "2025-06-27T10:05:42Z",
      "analysis_file": "analysis/G1hhmz6mXT0.json"
    },
    {
      "id": "GdvKNwMcfd0",
      "resource": "https://www.youtube.com/watch?v=GdvKNwMcfd0",
      "title": "From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft",
      "author": "Chris Noring, Microsoft",
      "last_modified": "2026-07-11T14:00:06Z",
      "analysis_file": "analysis/GdvKNwMcfd0.json"
    },
    {
      "id": "Lqq_LcBaJCc",
      "resource": "https://www.youtube.com/watch?v=Lqq_LcBaJCc",
      "title": "How agents will unlock the $500B promise of AI - Donald Hruska, Retool",
      "author": "Donald Hruska, Retool",
      "last_modified": "2025-07-23T15:51:38Z",
      "analysis_file": "analysis/Lqq_LcBaJCc.json"
    },
    {
      "id": "M05vON8i0aI",
      "resource": "https://www.youtube.com/watch?v=M05vON8i0aI",
      "title": "AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack",
      "author": "Imad Touil, QuantumBlack",
      "last_modified": "2026-08-28T18:30:04Z",
      "analysis_file": "analysis/M05vON8i0aI.json"
    },
    {
      "id": "MhHEGMFCEB0",
      "resource": "https://www.youtube.com/watch?v=MhHEGMFCEB0",
      "title": "OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman",
      "author": "Vaibhav Srivastav & Katia Gil Guzman",
      "last_modified": "2026-04-29T16:00:06Z",
      "analysis_file": "analysis/MhHEGMFCEB0.json"
    },
    {
      "id": "OE_lLNCNfQo",
      "resource": "https://www.youtube.com/watch?v=OE_lLNCNfQo",
      "title": "YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker",
      "author": "Rowan Christmas, Docker",
      "last_modified": "2026-10-03T00:30:06Z",
      "analysis_file": "analysis/OE_lLNCNfQo.json"
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
      "id": "RmJ4rTLV_x4",
      "resource": "https://www.youtube.com/watch?v=RmJ4rTLV_x4",
      "title": "Your Support Team Should Ship Code – Lisa Orr, Zapier",
      "author": "Lisa Orr, Zapier",
      "last_modified": "2025-12-16T17:00:06Z",
      "analysis_file": "analysis/RmJ4rTLV_x4.json"
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
      "id": "Wb2v9Phhnns",
      "resource": "https://www.youtube.com/watch?v=Wb2v9Phhnns",
      "title": "Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder",
      "author": "Jiachen Jiang, Coder",
      "last_modified": "2026-10-14T16:00:25Z",
      "analysis_file": "analysis/Wb2v9Phhnns.json"
    },
    {
      "id": "X6l4lpA0_NY",
      "resource": "https://www.youtube.com/watch?v=X6l4lpA0_NY",
      "title": "Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl",
      "author": "Dru Knox, Tessl",
      "last_modified": "2026-10-06T15:30:27Z",
      "analysis_file": "analysis/X6l4lpA0_NY.json"
    },
    {
      "id": "XNtkiQJ49Ps",
      "resource": "https://www.youtube.com/watch?v=XNtkiQJ49Ps",
      "title": "Agents need more than a chat - Jacob Lauritzen, CTO Legora",
      "author": "Jacob Lauritzen, CTO Legora",
      "last_modified": "2026-04-22T15:15:06Z",
      "analysis_file": "analysis/XNtkiQJ49Ps.json"
    },
    {
      "id": "YBYUvGOuotE",
      "resource": "https://www.youtube.com/watch?v=YBYUvGOuotE",
      "title": "MCP = Mega Context Problem - Matt Carey",
      "author": "Matt Carey",
      "last_modified": "2026-04-25T17:00:06Z",
      "analysis_file": "analysis/YBYUvGOuotE.json"
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
      "id": "ZyC56eV8sVw",
      "resource": "https://www.youtube.com/watch?v=ZyC56eV8sVw",
      "title": "AI Security Engineer Foundations + Certificate — Javier Garza, Snyk",
      "author": "Javier Garza, Snyk",
      "last_modified": "2026-10-11T19:30:16Z",
      "analysis_file": "analysis/ZyC56eV8sVw.json"
    },
    {
      "id": "bmWZk9vTze0",
      "resource": "https://www.youtube.com/watch?v=bmWZk9vTze0",
      "title": "MCP is all you need — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-07-18T18:52:25Z",
      "analysis_file": "analysis/bmWZk9vTze0.json"
    },
    {
      "id": "eXA2tjRZIbY",
      "resource": "https://www.youtube.com/watch?v=eXA2tjRZIbY",
      "title": "The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI",
      "author": "Varun Krovvidi, Resolve AI",
      "last_modified": "2026-10-06T23:30:36Z",
      "analysis_file": "analysis/eXA2tjRZIbY.json"
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
      "id": "hD9-V56FNRI",
      "resource": "https://www.youtube.com/watch?v=hD9-V56FNRI",
      "title": "AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok",
      "author": "Salman Munaf, TikTok",
      "last_modified": "2026-08-29T16:00:06Z",
      "analysis_file": "analysis/hD9-V56FNRI.json"
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
      "id": "i1uPAN6uW4s",
      "resource": "https://www.youtube.com/watch?v=i1uPAN6uW4s",
      "title": "Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments - Harald Kirshner,",
      "author": "Harald Kirshner,",
      "last_modified": "2025-06-27T10:15:59Z",
      "analysis_file": "analysis/i1uPAN6uW4s.json"
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
      "id": "kiClTcJUnhc",
      "resource": "https://www.youtube.com/watch?v=kiClTcJUnhc",
      "title": "Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic",
      "author": "CJ Avilla & Harrison Stall, Anthropic",
      "last_modified": "2026-10-16T19:00:10Z",
      "analysis_file": "analysis/kiClTcJUnhc.json"
    },
    {
      "id": "kv-QAuKWllQ",
      "resource": "https://www.youtube.com/watch?v=kv-QAuKWllQ",
      "title": "How we hacked YC Spring 2025 batch’s AI agents — Rene Brandel, Casco",
      "author": "Rene Brandel, Casco",
      "last_modified": "2025-07-30T15:45:06Z",
      "analysis_file": "analysis/kv-QAuKWllQ.json"
    },
    {
      "id": "oWTEiYpxl80",
      "resource": "https://www.youtube.com/watch?v=oWTEiYpxl80",
      "title": "Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind",
      "author": "Philipp Schmid, Google DeepMind",
      "last_modified": "2026-10-07T17:00:07Z",
      "analysis_file": "analysis/oWTEiYpxl80.json"
    },
    {
      "id": "ohKt066uFhg",
      "resource": "https://www.youtube.com/watch?v=ohKt066uFhg",
      "title": "Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski",
      "author": "Fryderyk Wiatrowski",
      "last_modified": "2026-05-11T15:00:06Z",
      "analysis_file": "analysis/ohKt066uFhg.json"
    },
    {
      "id": "p-2MT8KYZqU",
      "resource": "https://www.youtube.com/watch?v=p-2MT8KYZqU",
      "title": "AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk",
      "author": "Micah Silverman, Snyk",
      "last_modified": "2026-10-11T13:30:04Z",
      "analysis_file": "analysis/p-2MT8KYZqU.json"
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
      "id": "pijYURicI1Y",
      "resource": "https://www.youtube.com/watch?v=pijYURicI1Y",
      "title": "Building efficient hybrid context query for LLM grounding: Simrat Hanspal",
      "author": null,
      "last_modified": "2025-02-05T11:18:34Z",
      "analysis_file": "analysis/pijYURicI1Y.json"
    },
    {
      "id": "qdAkxLoYNI8",
      "resource": "https://www.youtube.com/watch?v=qdAkxLoYNI8",
      "title": "How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked",
      "author": "Peter Werry, Unblocked",
      "last_modified": "2026-08-27T18:00:23Z",
      "analysis_file": "analysis/qdAkxLoYNI8.json"
    },
    {
      "id": "spNAUEgq_A8",
      "resource": "https://www.youtube.com/watch?v=spNAUEgq_A8",
      "title": "The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents",
      "author": "Justin Schroeder, StandardAgents",
      "last_modified": "2026-06-29T03:00:14Z",
      "analysis_file": "analysis/spNAUEgq_A8.json"
    },
    {
      "id": "tZycGA_Fbfo",
      "resource": "https://www.youtube.com/watch?v=tZycGA_Fbfo",
      "title": "Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma",
      "author": "Harish Gaggar, Credit Karma",
      "last_modified": "2026-10-14T17:00:04Z",
      "analysis_file": "analysis/tZycGA_Fbfo.json"
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
      "id": "w7IMuYsBNr8",
      "resource": "https://www.youtube.com/watch?v=w7IMuYsBNr8",
      "title": "OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)",
      "author": "Fouad Matin (Codex, Agent Robustness)",
      "last_modified": "2025-07-30T15:00:06Z",
      "analysis_file": "analysis/w7IMuYsBNr8.json"
    },
    {
      "id": "xn8EsW0wxyc",
      "resource": "https://www.youtube.com/watch?v=xn8EsW0wxyc",
      "title": "How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI",
      "author": "Venice AI",
      "last_modified": "2026-10-11T16:30:34Z",
      "analysis_file": "analysis/xn8EsW0wxyc.json"
    },
    {
      "id": "yWS0udrIOc8",
      "resource": "https://www.youtube.com/watch?v=yWS0udrIOc8",
      "title": "Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town",
      "author": "Steve Yegge, Gas Town",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/yWS0udrIOc8.json"
    },
    {
      "id": "zaGyGgLW3SM",
      "resource": "https://www.youtube.com/watch?v=zaGyGgLW3SM",
      "title": "Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker",
      "author": "Tushar Jain, Docker",
      "last_modified": "2026-08-20T16:30:33Z",
      "analysis_file": "analysis/zaGyGgLW3SM.json"
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

# Grant task-scoped read, write and execution capabilities

## What

Grant task-scoped read, write and execution capabilities

Limit the accessible files and services instead of relying on either per-action approval or unrestricted autonomy.

## Evidence

Source analysis [^-CnA2lGfymY]; no independently matched timestamped quote published.

Source analysis [^0uC6u0lJJl4]; no independently matched timestamped quote published.

> Next we have to constrain the tools. We have to constrain permissions. We have
> — 18:12 [^33Oct2hqGnk]

Source analysis [^5eJqXtevlXg]; no independently matched timestamped quote published.

Source analysis [^6pbQgnJ9Voc]; no independently matched timestamped quote published.

> You kind of use MCP as your tools where your agents are talking to them. Um with
> — 04:40 [^AvVoJBxgSQk]

Source analysis [^BKWpYIWvAo4]; no independently matched timestamped quote published.

Source analysis [^DdaAABdAqZY]; no independently matched timestamped quote published.

Source analysis [^Djv8Sp11UjI]; no independently matched timestamped quote published.

Source analysis [^ExeD-8gFUMM]; no independently matched timestamped quote published.

Source analysis [^G1hhmz6mXT0]; no independently matched timestamped quote published.

Source analysis [^GdvKNwMcfd0]; no independently matched timestamped quote published.

Source analysis [^Lqq_LcBaJCc]; no independently matched timestamped quote published.

> and permissions. Not every skills is actually something that anyone in the
> — 12:59 [^M05vON8i0aI]

> in read-only mode. You would never want your review agent to execute anything,
> — 42:38 [^MhHEGMFCEB0]

Source analysis [^OE_lLNCNfQo]; no independently matched timestamped quote published.

Source analysis [^PwCSYy-oGsM]; no independently matched timestamped quote published.

> our side, it made some of our tools no longer necessary.
> — 06:32 [^RmJ4rTLV_x4]

Source analysis [^V-L0INGTEOg]; no independently matched timestamped quote published.

> when they get simultaneous access to three different capabilities.
> — 05:08 [^Wb2v9Phhnns]

> it. I I promise it's worse than you think.
> — 13:21 [^X6l4lpA0_NY]

> increase trust by limiting what the agent can do. So instead of being able
> — 07:15 [^XNtkiQJ49Ps]

> have read-only access to the whole of the Cloudflare API. All of my Cloudflare
> — 13:32 [^YBYUvGOuotE]

Source analysis [^ZUZVNKFSmTM]; no independently matched timestamped quote published.

Source analysis [^ZyC56eV8sVw]; no independently matched timestamped quote published.

> people are over complicating the situation sometimes trying to come up
> — 01:56 [^bmWZk9vTze0]

> What is the least privilege access that AI can operate with in any given
> — 11:00 [^eXA2tjRZIbY]

Source analysis [^gvIAkmZUEZY]; no independently matched timestamped quote published.

> uh it is important to give scoped credentials to it. There should be
> — 15:34 [^hD9-V56FNRI]

Source analysis [^hfEczxdNyvU]; no independently matched timestamped quote published.

Source analysis [^i1uPAN6uW4s]; no independently matched timestamped quote published.

Source analysis [^iH_wV8BbS24]; no independently matched timestamped quote published.

> you don't expose anything over the open internet. And I think that's like
> — 1:40:31 [^kiClTcJUnhc]

Source analysis [^kv-QAuKWllQ]; no independently matched timestamped quote published.

> runs inside that remote sandbox you can also connect remote MCP servers or run
> — 19:50 [^oWTEiYpxl80]

Source analysis [^ohKt066uFhg]; no independently matched timestamped quote published.

Source analysis [^p-2MT8KYZqU]; no independently matched timestamped quote published.

> where you can sort of control which URLs it can go to. You can control what kind
> — 48:03 [^p7gaxmCUiIU]

Source analysis [^pijYURicI1Y]; no independently matched timestamped quote published.

Source analysis [^qdAkxLoYNI8]; no independently matched timestamped quote published.

> each of them is a separate isolated agent, a full agent.
> — 14:26 [^spNAUEgq_A8]

> some filters, limits, and block the fields which is really not required to
> — 09:15 [^tZycGA_Fbfo]

> removed it's just hidden and not reachable until needed. So it's just for
> — 17:02 [^vGCJ7diEtrw]

> spins up a container fully isolated. It then produces a PR at the end, that's
> — 04:35 [^w7IMuYsBNr8]

Source analysis [^xn8EsW0wxyc]; no independently matched timestamped quote published.

> credentials on that service account? Really, right? Only for this one action,
> — 20:08 [^yWS0udrIOc8]

Source analysis [^zaGyGgLW3SM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-CnA2lGfymY]: ["I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox](https://www.youtube.com/watch?v=-CnA2lGfymY); publication: 2026-07-13T19:25:09Z; analysis: `analysis/-CnA2lGfymY.json`.
[^0uC6u0lJJl4]: [Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](https://www.youtube.com/watch?v=0uC6u0lJJl4); publication: 2026-09-03T15:30:26Z; analysis: `analysis/0uC6u0lJJl4.json`.
[^33Oct2hqGnk]: [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](https://www.youtube.com/watch?v=33Oct2hqGnk); publication: 2026-10-04T21:00:13Z; analysis: `analysis/33Oct2hqGnk.json`.
[^5eJqXtevlXg]: [Hacking Subagents Into Codex CLI — Brian John, Betterup](https://www.youtube.com/watch?v=5eJqXtevlXg); publication: 2025-11-24T20:16:36Z; analysis: `analysis/5eJqXtevlXg.json`.
[^6pbQgnJ9Voc]: [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](https://www.youtube.com/watch?v=6pbQgnJ9Voc); publication: 2026-08-26T16:00:26Z; analysis: `analysis/6pbQgnJ9Voc.json`.
[^AvVoJBxgSQk]: [Agentic GraphRAG: AI’s Logical Edge — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=AvVoJBxgSQk); publication: 2025-07-21T17:15:06Z; analysis: `analysis/AvVoJBxgSQk.json`.
[^BKWpYIWvAo4]: [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google](https://www.youtube.com/watch?v=BKWpYIWvAo4); publication: 2026-05-03T22:00:06Z; analysis: `analysis/BKWpYIWvAo4.json`.
[^DdaAABdAqZY]: [Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft](https://www.youtube.com/watch?v=DdaAABdAqZY); publication: 2025-07-26T07:00:13Z; analysis: `analysis/DdaAABdAqZY.json`.
[^Djv8Sp11UjI]: [The Current State of Browser Agents - Jerry Wu and Wyatt Marshall](https://www.youtube.com/watch?v=Djv8Sp11UjI); publication: 2025-06-03T22:22:26Z; analysis: `analysis/Djv8Sp11UjI.json`.
[^ExeD-8gFUMM]: [Full Spec MCP: Hidden Capabilities of the MCP spec — Harald Kirschner, Microsoft/VSCode](https://www.youtube.com/watch?v=ExeD-8gFUMM); publication: 2025-07-18T18:42:25Z; analysis: `analysis/ExeD-8gFUMM.json`.
[^G1hhmz6mXT0]: [Collaborating with Agents in your Software Dev Workflow - Jon Peck & Christopher Harrison, Microsoft](https://www.youtube.com/watch?v=G1hhmz6mXT0); publication: 2025-06-27T10:05:42Z; analysis: `analysis/G1hhmz6mXT0.json`.
[^GdvKNwMcfd0]: [From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](https://www.youtube.com/watch?v=GdvKNwMcfd0); publication: 2026-07-11T14:00:06Z; analysis: `analysis/GdvKNwMcfd0.json`.
[^Lqq_LcBaJCc]: [How agents will unlock the $500B promise of AI - Donald Hruska, Retool](https://www.youtube.com/watch?v=Lqq_LcBaJCc); publication: 2025-07-23T15:51:38Z; analysis: `analysis/Lqq_LcBaJCc.json`.
[^M05vON8i0aI]: [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](https://www.youtube.com/watch?v=M05vON8i0aI); publication: 2026-08-28T18:30:04Z; analysis: `analysis/M05vON8i0aI.json`.
[^MhHEGMFCEB0]: [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](https://www.youtube.com/watch?v=MhHEGMFCEB0); publication: 2026-04-29T16:00:06Z; analysis: `analysis/MhHEGMFCEB0.json`.
[^OE_lLNCNfQo]: [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](https://www.youtube.com/watch?v=OE_lLNCNfQo); publication: 2026-10-03T00:30:06Z; analysis: `analysis/OE_lLNCNfQo.json`.
[^PwCSYy-oGsM]: [Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI](https://www.youtube.com/watch?v=PwCSYy-oGsM); publication: 2026-10-12T00:00:10Z; analysis: `analysis/PwCSYy-oGsM.json`.
[^RmJ4rTLV_x4]: [Your Support Team Should Ship Code – Lisa Orr, Zapier](https://www.youtube.com/watch?v=RmJ4rTLV_x4); publication: 2025-12-16T17:00:06Z; analysis: `analysis/RmJ4rTLV_x4.json`.
[^V-L0INGTEOg]: [Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs](https://www.youtube.com/watch?v=V-L0INGTEOg); publication: 2026-05-29T14:00:06Z; analysis: `analysis/V-L0INGTEOg.json`.
[^Wb2v9Phhnns]: [Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder](https://www.youtube.com/watch?v=Wb2v9Phhnns); publication: 2026-10-14T16:00:25Z; analysis: `analysis/Wb2v9Phhnns.json`.
[^X6l4lpA0_NY]: [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](https://www.youtube.com/watch?v=X6l4lpA0_NY); publication: 2026-10-06T15:30:27Z; analysis: `analysis/X6l4lpA0_NY.json`.
[^XNtkiQJ49Ps]: [Agents need more than a chat - Jacob Lauritzen, CTO Legora](https://www.youtube.com/watch?v=XNtkiQJ49Ps); publication: 2026-04-22T15:15:06Z; analysis: `analysis/XNtkiQJ49Ps.json`.
[^YBYUvGOuotE]: [MCP = Mega Context Problem - Matt Carey](https://www.youtube.com/watch?v=YBYUvGOuotE); publication: 2026-04-25T17:00:06Z; analysis: `analysis/YBYUvGOuotE.json`.
[^ZUZVNKFSmTM]: [How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker](https://www.youtube.com/watch?v=ZUZVNKFSmTM); publication: 2026-10-06T00:30:15Z; analysis: `analysis/ZUZVNKFSmTM.json`.
[^ZyC56eV8sVw]: [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](https://www.youtube.com/watch?v=ZyC56eV8sVw); publication: 2026-10-11T19:30:16Z; analysis: `analysis/ZyC56eV8sVw.json`.
[^bmWZk9vTze0]: [MCP is all you need — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=bmWZk9vTze0); publication: 2025-07-18T18:52:25Z; analysis: `analysis/bmWZk9vTze0.json`.
[^eXA2tjRZIbY]: [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](https://www.youtube.com/watch?v=eXA2tjRZIbY); publication: 2026-10-06T23:30:36Z; analysis: `analysis/eXA2tjRZIbY.json`.
[^gvIAkmZUEZY]: [Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code](https://www.youtube.com/watch?v=gvIAkmZUEZY); publication: 2025-12-22T17:00:06Z; analysis: `analysis/gvIAkmZUEZY.json`.
[^hD9-V56FNRI]: [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](https://www.youtube.com/watch?v=hD9-V56FNRI); publication: 2026-08-29T16:00:06Z; analysis: `analysis/hD9-V56FNRI.json`.
[^hfEczxdNyvU]: [Advanced Workshop: Mastering AI Observability — Doug Guthrie, Braintrust](https://www.youtube.com/watch?v=hfEczxdNyvU); publication: 2026-10-06T01:00:25Z; analysis: `analysis/hfEczxdNyvU.json`.
[^i1uPAN6uW4s]: [Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments - Harald Kirshner,](https://www.youtube.com/watch?v=i1uPAN6uW4s); publication: 2025-06-27T10:15:59Z; analysis: `analysis/i1uPAN6uW4s.json`.
[^iH_wV8BbS24]: [Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands](https://www.youtube.com/watch?v=iH_wV8BbS24); publication: 2026-10-12T05:10:18Z; analysis: `analysis/iH_wV8BbS24.json`.
[^kiClTcJUnhc]: [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc); publication: 2026-10-16T19:00:10Z; analysis: `analysis/kiClTcJUnhc.json`.
[^kv-QAuKWllQ]: [How we hacked YC Spring 2025 batch’s AI agents — Rene Brandel, Casco](https://www.youtube.com/watch?v=kv-QAuKWllQ); publication: 2025-07-30T15:45:06Z; analysis: `analysis/kv-QAuKWllQ.json`.
[^oWTEiYpxl80]: [Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=oWTEiYpxl80); publication: 2026-10-07T17:00:07Z; analysis: `analysis/oWTEiYpxl80.json`.
[^ohKt066uFhg]: [Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski](https://www.youtube.com/watch?v=ohKt066uFhg); publication: 2026-05-11T15:00:06Z; analysis: `analysis/ohKt066uFhg.json`.
[^p-2MT8KYZqU]: [AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk](https://www.youtube.com/watch?v=p-2MT8KYZqU); publication: 2026-10-11T13:30:04Z; analysis: `analysis/p-2MT8KYZqU.json`.
[^p7gaxmCUiIU]: [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](https://www.youtube.com/watch?v=p7gaxmCUiIU); publication: 2026-10-11T21:30:05Z; analysis: `analysis/p7gaxmCUiIU.json`.
[^pijYURicI1Y]: [Building efficient hybrid context query for LLM grounding: Simrat Hanspal](https://www.youtube.com/watch?v=pijYURicI1Y); publication: 2025-02-05T11:18:34Z; analysis: `analysis/pijYURicI1Y.json`.
[^qdAkxLoYNI8]: [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](https://www.youtube.com/watch?v=qdAkxLoYNI8); publication: 2026-08-27T18:00:23Z; analysis: `analysis/qdAkxLoYNI8.json`.
[^spNAUEgq_A8]: [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](https://www.youtube.com/watch?v=spNAUEgq_A8); publication: 2026-06-29T03:00:14Z; analysis: `analysis/spNAUEgq_A8.json`.
[^tZycGA_Fbfo]: [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](https://www.youtube.com/watch?v=tZycGA_Fbfo); publication: 2026-10-14T17:00:04Z; analysis: `analysis/tZycGA_Fbfo.json`.
[^vGCJ7diEtrw]: [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](https://www.youtube.com/watch?v=vGCJ7diEtrw); publication: 2026-09-27T15:00:02Z; analysis: `analysis/vGCJ7diEtrw.json`.
[^w7IMuYsBNr8]: [OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)](https://www.youtube.com/watch?v=w7IMuYsBNr8); publication: 2025-07-30T15:00:06Z; analysis: `analysis/w7IMuYsBNr8.json`.
[^xn8EsW0wxyc]: [How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI](https://www.youtube.com/watch?v=xn8EsW0wxyc); publication: 2026-10-11T16:30:34Z; analysis: `analysis/xn8EsW0wxyc.json`.
[^yWS0udrIOc8]: [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](https://www.youtube.com/watch?v=yWS0udrIOc8); publication: 2026-07-20T17:17:53Z; analysis: `analysis/yWS0udrIOc8.json`.
[^zaGyGgLW3SM]: [Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker](https://www.youtube.com/watch?v=zaGyGgLW3SM); publication: 2026-08-20T16:30:33Z; analysis: `analysis/zaGyGgLW3SM.json`.
