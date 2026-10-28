---
{
  "type": "technique",
  "id": "secret-broker",
  "title": "Keep credentials outside agent sandboxes behind a constrained broker",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-17T23:00:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "0uC6u0lJJl4",
      "resource": "https://www.youtube.com/watch?v=0uC6u0lJJl4",
      "title": "Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL",
      "author": "Tanmai Gopal, PromptQL",
      "last_modified": "2026-09-03T15:30:26Z",
      "analysis_file": "analysis/0uC6u0lJJl4.json"
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
      "id": "F1DYkY1BlfM",
      "resource": "https://www.youtube.com/watch?v=F1DYkY1BlfM",
      "title": "Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat",
      "author": "Sally Ann O'Malley, Red Hat",
      "last_modified": "2026-05-22T17:00:06Z",
      "analysis_file": "analysis/F1DYkY1BlfM.json"
    },
    {
      "id": "IavxrdVnwXM",
      "resource": "https://www.youtube.com/watch?v=IavxrdVnwXM",
      "title": "An AI Agent Got Its User Banned From Resy — Keycard, JPMorgan Chase & AAuth",
      "author": "Keycard, JPMorgan Chase & AAuth",
      "last_modified": "2026-10-17T23:00:05Z",
      "analysis_file": "analysis/IavxrdVnwXM.json"
    },
    {
      "id": "K0X9QDRkIdg",
      "resource": "https://www.youtube.com/watch?v=K0X9QDRkIdg",
      "title": "Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic",
      "author": "Gagan Bhat & Isabella Kai He, Anthropic",
      "last_modified": "2026-08-11T16:00:06Z",
      "analysis_file": "analysis/K0X9QDRkIdg.json"
    },
    {
      "id": "MkRYPFIMCSA",
      "resource": "https://www.youtube.com/watch?v=MkRYPFIMCSA",
      "title": "Security Firewall for Agents — Ryan Dahl, Deno",
      "author": "Ryan Dahl, Deno",
      "last_modified": "2026-08-17T18:30:06Z",
      "analysis_file": "analysis/MkRYPFIMCSA.json"
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
      "id": "OL7kfezynJM",
      "resource": "https://www.youtube.com/watch?v=OL7kfezynJM",
      "title": "Multiplayer agentic engineering — Arjun Singh, Superconductor",
      "author": "Arjun Singh, Superconductor",
      "last_modified": "2026-08-09T20:30:34Z",
      "analysis_file": "analysis/OL7kfezynJM.json"
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
      "id": "Uv0nAf_7tyU",
      "resource": "https://www.youtube.com/watch?v=Uv0nAf_7tyU",
      "title": "Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T05:44:00Z",
      "analysis_file": "analysis/Uv0nAf_7tyU.json"
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
      "id": "bUBF5V6oDKw",
      "resource": "https://www.youtube.com/watch?v=bUBF5V6oDKw",
      "title": "Containing Agent Chaos — Solomon Hykes, Dagger",
      "author": "Solomon Hykes, Dagger",
      "last_modified": "2025-06-28T16:30:06Z",
      "analysis_file": "analysis/bUBF5V6oDKw.json"
    },
    {
      "id": "blW-lSd5CYQ",
      "resource": "https://www.youtube.com/watch?v=blW-lSd5CYQ",
      "title": "The rise of the agentic economy on the shoulders of MCP — Jan Curn, Apify",
      "author": "Jan Curn, Apify",
      "last_modified": "2025-07-18T18:59:57Z",
      "analysis_file": "analysis/blW-lSd5CYQ.json"
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
      "id": "cgimkNGNjvU",
      "resource": "https://www.youtube.com/watch?v=cgimkNGNjvU",
      "title": "Agentic Development Security — Ezra Tanzer, Snyk",
      "author": "Ezra Tanzer, Snyk",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/cgimkNGNjvU.json"
    },
    {
      "id": "fjF8EKnxKCU",
      "resource": "https://www.youtube.com/watch?v=fjF8EKnxKCU",
      "title": "Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind",
      "author": "Philipp Schmid, Google DeepMind",
      "last_modified": "2026-09-14T17:30:25Z",
      "analysis_file": "analysis/fjF8EKnxKCU.json"
    },
    {
      "id": "iQ5xldZ9StU",
      "resource": "https://www.youtube.com/watch?v=iQ5xldZ9StU",
      "title": "Realtime multiplayer, automation, and you! — Idan Gazit, GitHub",
      "author": "Idan Gazit, GitHub",
      "last_modified": "2026-08-08T21:30:06Z",
      "analysis_file": "analysis/iQ5xldZ9StU.json"
    },
    {
      "id": "juoNbJiZUi0",
      "resource": "https://www.youtube.com/watch?v=juoNbJiZUi0",
      "title": "LLM codegen fails and how to stop 'em — Danilo Campos, PostHog",
      "author": "Danilo Campos, PostHog",
      "last_modified": "2026-04-30T14:00:06Z",
      "analysis_file": "analysis/juoNbJiZUi0.json"
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
      "id": "o_hhkJtlbSs",
      "resource": "https://www.youtube.com/watch?v=o_hhkJtlbSs",
      "title": "Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands",
      "author": "Robert Brennan, OpenHands",
      "last_modified": "2025-07-25T23:10:11Z",
      "analysis_file": "analysis/o_hhkJtlbSs.json"
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
      "id": "pFsfax19yOM",
      "resource": "https://www.youtube.com/watch?v=pFsfax19yOM",
      "title": "Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser",
      "author": "Nick Nisi and Zack Proser",
      "last_modified": "2026-05-06T17:00:06Z",
      "analysis_file": "analysis/pFsfax19yOM.json"
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
      "id": "x_1EumTaXeE",
      "resource": "https://www.youtube.com/watch?v=x_1EumTaXeE",
      "title": "Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue",
      "author": "Josh Albrecht, Imbue",
      "last_modified": "2025-07-25T23:10:37Z",
      "analysis_file": "analysis/x_1EumTaXeE.json"
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
      "id": "zuMw0pkPXpU",
      "resource": "https://www.youtube.com/watch?v=zuMw0pkPXpU",
      "title": "Tool Calling Is Not Just Plumbing for AI Agents — Roy Derks",
      "author": "Roy Derks",
      "last_modified": "2025-02-22T17:00:24Z",
      "analysis_file": "analysis/zuMw0pkPXpU.json"
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

# Keep credentials outside agent sandboxes behind a constrained broker

## What

Keep credentials outside agent sandboxes behind a constrained broker

A broker can hold service credentials and execute narrowly authorized operations, avoiding secret material in the agent filesystem, environment and prompt.

## Evidence

Source analysis [^0uC6u0lJJl4]; no independently matched timestamped quote published.

Source analysis [^BM2JX9hqsVQ]; no independently matched timestamped quote published.

Source analysis [^F1DYkY1BlfM]; no independently matched timestamped quote published.

Source analysis [^IavxrdVnwXM]; no independently matched timestamped quote published.

> your agent and the model never sees your security tokens.
> — 22:44 [^K0X9QDRkIdg]

Source analysis [^MkRYPFIMCSA]; no independently matched timestamped quote published.

Source analysis [^OE_lLNCNfQo]; no independently matched timestamped quote published.

> give your agents access to only what they need.
> — 10:14 [^OL7kfezynJM]

Source analysis [^OqM67QG_Ikk]; no independently matched timestamped quote published.

> The other thing that we did was credentials never entered our sandbox.
> — 09:08 [^Uv0nAf_7tyU]

Source analysis [^ZUZVNKFSmTM]; no independently matched timestamped quote published.

Source analysis [^bI8WyG9YB0I]; no independently matched timestamped quote published.

> remove the secret. Let me look at your memory files. So, you have to really
> — 21:15 [^bSG9wUYaHWU]

> this environment gets this secret and boom, it can use it, right? Um
> — 15:25 [^bUBF5V6oDKw]

Source analysis [^blW-lSd5CYQ]; no independently matched timestamped quote published.

> can do to secure your environment is just not have secrets as files.
> — 19:00 [^c35YoMdnI78]

> actually blocked the access of of reading this file. Um so yes, the agents
> — 18:50 [^cgimkNGNjvU]

Source analysis [^fjF8EKnxKCU]; no independently matched timestamped quote published.

Source analysis [^iQ5xldZ9StU]; no independently matched timestamped quote published.

> And it could write to a key a new value. And that was it. There was nothing that
> — 13:27 [^juoNbJiZUi0]

> actually get substituted for what like the actual credential is. So, there's no
> — 1:23:02 [^kiClTcJUnhc]

> lease privilege as you're granting agents access to do these things.
> — 07:21 [^o_hhkJtlbSs]

> log into websites uh save the cookies uh reuse those cookies in future runs so
> — 29:59 [^p7gaxmCUiIU]

> don't put it in the zip file. But, you know, it's evolving. So.
> — 1:06:21 [^pFsfax19yOM]

> are only usable by the agent but not accessible by the agent. So we insert it
> — 37:26 [^uU5Gv2h8-9g]

> uh we try to make it easy to run tests in sandboxes and without secrets as much
> — 14:31 [^x_1EumTaXeE]

Source analysis [^xn8EsW0wxyc]; no independently matched timestamped quote published.

> database they require different sort of credentials uh where you set those
> — 18:39 [^zuMw0pkPXpU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^0uC6u0lJJl4]: [Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](https://www.youtube.com/watch?v=0uC6u0lJJl4); publication: 2026-09-03T15:30:26Z; analysis: `analysis/0uC6u0lJJl4.json`.
[^BM2JX9hqsVQ]: [What if the network was the sandbox? — Remy Guercio, Tailscale](https://www.youtube.com/watch?v=BM2JX9hqsVQ); publication: 2026-06-01T15:00:31Z; analysis: `analysis/BM2JX9hqsVQ.json`.
[^F1DYkY1BlfM]: [Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat](https://www.youtube.com/watch?v=F1DYkY1BlfM); publication: 2026-05-22T17:00:06Z; analysis: `analysis/F1DYkY1BlfM.json`.
[^IavxrdVnwXM]: [An AI Agent Got Its User Banned From Resy — Keycard, JPMorgan Chase & AAuth](https://www.youtube.com/watch?v=IavxrdVnwXM); publication: 2026-10-17T23:00:05Z; analysis: `analysis/IavxrdVnwXM.json`.
[^K0X9QDRkIdg]: [Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic](https://www.youtube.com/watch?v=K0X9QDRkIdg); publication: 2026-08-11T16:00:06Z; analysis: `analysis/K0X9QDRkIdg.json`.
[^MkRYPFIMCSA]: [Security Firewall for Agents — Ryan Dahl, Deno](https://www.youtube.com/watch?v=MkRYPFIMCSA); publication: 2026-08-17T18:30:06Z; analysis: `analysis/MkRYPFIMCSA.json`.
[^OE_lLNCNfQo]: [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](https://www.youtube.com/watch?v=OE_lLNCNfQo); publication: 2026-10-03T00:30:06Z; analysis: `analysis/OE_lLNCNfQo.json`.
[^OL7kfezynJM]: [Multiplayer agentic engineering — Arjun Singh, Superconductor](https://www.youtube.com/watch?v=OL7kfezynJM); publication: 2026-08-09T20:30:34Z; analysis: `analysis/OL7kfezynJM.json`.
[^OqM67QG_Ikk]: [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=OqM67QG_Ikk); publication: 2026-07-13T17:00:06Z; analysis: `analysis/OqM67QG_Ikk.json`.
[^Uv0nAf_7tyU]: [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](https://www.youtube.com/watch?v=Uv0nAf_7tyU); publication: 2026-10-12T05:44:00Z; analysis: `analysis/Uv0nAf_7tyU.json`.
[^ZUZVNKFSmTM]: [How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker](https://www.youtube.com/watch?v=ZUZVNKFSmTM); publication: 2026-10-06T00:30:15Z; analysis: `analysis/ZUZVNKFSmTM.json`.
[^bI8WyG9YB0I]: [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](https://www.youtube.com/watch?v=bI8WyG9YB0I); publication: 2026-10-11T19:00:11Z; analysis: `analysis/bI8WyG9YB0I.json`.
[^bSG9wUYaHWU]: [Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU); publication: 2026-05-03T14:00:06Z; analysis: `analysis/bSG9wUYaHWU.json`.
[^bUBF5V6oDKw]: [Containing Agent Chaos — Solomon Hykes, Dagger](https://www.youtube.com/watch?v=bUBF5V6oDKw); publication: 2025-06-28T16:30:06Z; analysis: `analysis/bUBF5V6oDKw.json`.
[^blW-lSd5CYQ]: [The rise of the agentic economy on the shoulders of MCP — Jan Curn, Apify](https://www.youtube.com/watch?v=blW-lSd5CYQ); publication: 2025-07-18T18:59:57Z; analysis: `analysis/blW-lSd5CYQ.json`.
[^c35YoMdnI78]: [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78); publication: 2026-07-17T21:00:06Z; analysis: `analysis/c35YoMdnI78.json`.
[^cgimkNGNjvU]: [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU); publication: 2026-07-20T17:17:53Z; analysis: `analysis/cgimkNGNjvU.json`.
[^fjF8EKnxKCU]: [Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=fjF8EKnxKCU); publication: 2026-09-14T17:30:25Z; analysis: `analysis/fjF8EKnxKCU.json`.
[^iQ5xldZ9StU]: [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](https://www.youtube.com/watch?v=iQ5xldZ9StU); publication: 2026-08-08T21:30:06Z; analysis: `analysis/iQ5xldZ9StU.json`.
[^juoNbJiZUi0]: [LLM codegen fails and how to stop 'em — Danilo Campos, PostHog](https://www.youtube.com/watch?v=juoNbJiZUi0); publication: 2026-04-30T14:00:06Z; analysis: `analysis/juoNbJiZUi0.json`.
[^kiClTcJUnhc]: [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc); publication: 2026-10-16T19:00:10Z; analysis: `analysis/kiClTcJUnhc.json`.
[^o_hhkJtlbSs]: [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=o_hhkJtlbSs); publication: 2025-07-25T23:10:11Z; analysis: `analysis/o_hhkJtlbSs.json`.
[^p7gaxmCUiIU]: [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](https://www.youtube.com/watch?v=p7gaxmCUiIU); publication: 2026-10-11T21:30:05Z; analysis: `analysis/p7gaxmCUiIU.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
[^uU5Gv2h8-9g]: [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](https://www.youtube.com/watch?v=uU5Gv2h8-9g); publication: 2026-07-15T15:05:06Z; analysis: `analysis/uU5Gv2h8-9g.json`.
[^x_1EumTaXeE]: [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](https://www.youtube.com/watch?v=x_1EumTaXeE); publication: 2025-07-25T23:10:37Z; analysis: `analysis/x_1EumTaXeE.json`.
[^xn8EsW0wxyc]: [How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI](https://www.youtube.com/watch?v=xn8EsW0wxyc); publication: 2026-10-11T16:30:34Z; analysis: `analysis/xn8EsW0wxyc.json`.
[^zuMw0pkPXpU]: [Tool Calling Is Not Just Plumbing for AI Agents — Roy Derks](https://www.youtube.com/watch?v=zuMw0pkPXpU); publication: 2025-02-22T17:00:24Z; analysis: `analysis/zuMw0pkPXpU.json`.
