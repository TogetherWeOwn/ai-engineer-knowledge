---
{
  "type": "technique",
  "id": "network-egress",
  "title": "Default-deny sandbox egress and allow only task-required destinations",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-20T19:00:34Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "0NHCyq8bBcM",
      "resource": "https://www.youtube.com/watch?v=0NHCyq8bBcM",
      "title": "Remote MCPs: What we learned from shipping — John Welsh, Anthropic",
      "author": "John Welsh, Anthropic",
      "last_modified": "2025-06-19T16:52:25Z",
      "analysis_file": "analysis/0NHCyq8bBcM.json"
    },
    {
      "id": "5rMc-moNVx0",
      "resource": "https://www.youtube.com/watch?v=5rMc-moNVx0",
      "title": "Stateful environments for vertical agents — Josh Purtell, Synth Labs",
      "author": "Josh Purtell, Synth Labs",
      "last_modified": "2025-07-22T19:52:28Z",
      "analysis_file": "analysis/5rMc-moNVx0.json"
    },
    {
      "id": "AHtGAgQ0Q_Q",
      "resource": "https://www.youtube.com/watch?v=AHtGAgQ0Q_Q",
      "title": "Why, and how you need to sandbox AI-Generated Code? — Harshil Agrawal, Cloudflare",
      "author": "Harshil Agrawal, Cloudflare",
      "last_modified": "2026-04-08T08:30:06Z",
      "analysis_file": "analysis/AHtGAgQ0Q_Q.json"
    },
    {
      "id": "FGftGOzfohc",
      "resource": "https://www.youtube.com/watch?v=FGftGOzfohc",
      "title": "Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T06:07:50Z",
      "analysis_file": "analysis/FGftGOzfohc.json"
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
      "id": "LqLoYksJ6do",
      "resource": "https://www.youtube.com/watch?v=LqLoYksJ6do",
      "title": "We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3",
      "author": "Moritz Johner, Form3",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/LqLoYksJ6do.json"
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
      "id": "TqC1qOfiVcQ",
      "resource": "https://www.youtube.com/watch?v=TqC1qOfiVcQ",
      "title": "Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic",
      "author": "Thariq Shihipar, Anthropic",
      "last_modified": "2026-01-05T17:00:06Z",
      "analysis_file": "analysis/TqC1qOfiVcQ.json"
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
      "id": "XjI-AR4pt7Y",
      "resource": "https://www.youtube.com/watch?v=XjI-AR4pt7Y",
      "title": "Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA",
      "author": "Lovina Dmello, NVIDIA",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/XjI-AR4pt7Y.json"
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
      "id": "abw_m-DRi1k",
      "resource": "https://www.youtube.com/watch?v=abw_m-DRi1k",
      "title": "The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder",
      "author": "Michael Patterson, Coder",
      "last_modified": "2026-10-10T15:00:03Z",
      "analysis_file": "analysis/abw_m-DRi1k.json"
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
      "id": "il1c1a2FufU",
      "resource": "https://www.youtube.com/watch?v=il1c1a2FufU",
      "title": "Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex",
      "author": null,
      "last_modified": "2026-07-24T15:00:06Z",
      "analysis_file": "analysis/il1c1a2FufU.json"
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
      "id": "w7IMuYsBNr8",
      "resource": "https://www.youtube.com/watch?v=w7IMuYsBNr8",
      "title": "OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)",
      "author": "Fouad Matin (Codex, Agent Robustness)",
      "last_modified": "2025-07-30T15:00:06Z",
      "analysis_file": "analysis/w7IMuYsBNr8.json"
    },
    {
      "id": "wCIYViPd4SU",
      "resource": "https://www.youtube.com/watch?v=wCIYViPd4SU",
      "title": "Tethered: Our Agents Are Us — Shu Fang, Two Sigma",
      "author": "Shu Fang, Two Sigma",
      "last_modified": "2026-09-03T14:30:21Z",
      "analysis_file": "analysis/wCIYViPd4SU.json"
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

# Default-deny sandbox egress and allow only task-required destinations

## What

Default-deny sandbox egress and allow only task-required destinations

Programmable network policy prevents generated code from turning a legitimate API capability into arbitrary outbound exfiltration.

## Evidence

Source analysis [^0NHCyq8bBcM]; no independently matched timestamped quote published.

Source analysis [^5rMc-moNVx0]; no independently matched timestamped quote published.

Source analysis [^AHtGAgQ0Q_Q]; no independently matched timestamped quote published.

Source analysis [^FGftGOzfohc]; no independently matched timestamped quote published.

> and only making outbound calls to the clawed agent loop.
> — 26:28 [^K0X9QDRkIdg]

> And we also want to apply network policies to these two worlds separately.
> — 16:28 [^LqLoYksJ6do]

> about that because we provision uh standalone VM for for our agents.
> — 09:53 [^MkRYPFIMCSA]

Source analysis [^OE_lLNCNfQo]; no independently matched timestamped quote published.

> sandbox and you say, "Look, these are the places you're allowed to access,
> — 11:39 [^OL7kfezynJM]

Source analysis [^TqC1qOfiVcQ]; no independently matched timestamped quote published.

Source analysis [^Wb2v9Phhnns]; no independently matched timestamped quote published.

Source analysis [^XjI-AR4pt7Y]; no independently matched timestamped quote published.

> run this one, it's like this worker is not permitted to access the internet via
> — 12:34 [^YBYUvGOuotE]

Source analysis [^abw_m-DRi1k]; no independently matched timestamped quote published.

Source analysis [^adfw3xJBx1o]; no independently matched timestamped quote published.

> email, right? Or like you can't uh send a Slack message to external Slack
> — 32:05 [^il1c1a2FufU]

Source analysis [^kv-QAuKWllQ]; no independently matched timestamped quote published.

Source analysis [^w7IMuYsBNr8]; no independently matched timestamped quote published.

Source analysis [^wCIYViPd4SU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^0NHCyq8bBcM]: [Remote MCPs: What we learned from shipping — John Welsh, Anthropic](https://www.youtube.com/watch?v=0NHCyq8bBcM); publication: 2025-06-19T16:52:25Z; analysis: `analysis/0NHCyq8bBcM.json`.
[^5rMc-moNVx0]: [Stateful environments for vertical agents — Josh Purtell, Synth Labs](https://www.youtube.com/watch?v=5rMc-moNVx0); publication: 2025-07-22T19:52:28Z; analysis: `analysis/5rMc-moNVx0.json`.
[^AHtGAgQ0Q_Q]: [Why, and how you need to sandbox AI-Generated Code? — Harshil Agrawal, Cloudflare](https://www.youtube.com/watch?v=AHtGAgQ0Q_Q); publication: 2026-04-08T08:30:06Z; analysis: `analysis/AHtGAgQ0Q_Q.json`.
[^FGftGOzfohc]: [Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](https://www.youtube.com/watch?v=FGftGOzfohc); publication: 2026-10-12T06:07:50Z; analysis: `analysis/FGftGOzfohc.json`.
[^K0X9QDRkIdg]: [Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic](https://www.youtube.com/watch?v=K0X9QDRkIdg); publication: 2026-08-11T16:00:06Z; analysis: `analysis/K0X9QDRkIdg.json`.
[^LqLoYksJ6do]: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](https://www.youtube.com/watch?v=LqLoYksJ6do); publication: 2026-07-20T17:17:53Z; analysis: `analysis/LqLoYksJ6do.json`.
[^MkRYPFIMCSA]: [Security Firewall for Agents — Ryan Dahl, Deno](https://www.youtube.com/watch?v=MkRYPFIMCSA); publication: 2026-08-17T18:30:06Z; analysis: `analysis/MkRYPFIMCSA.json`.
[^OE_lLNCNfQo]: [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](https://www.youtube.com/watch?v=OE_lLNCNfQo); publication: 2026-10-03T00:30:06Z; analysis: `analysis/OE_lLNCNfQo.json`.
[^OL7kfezynJM]: [Multiplayer agentic engineering — Arjun Singh, Superconductor](https://www.youtube.com/watch?v=OL7kfezynJM); publication: 2026-08-09T20:30:34Z; analysis: `analysis/OL7kfezynJM.json`.
[^TqC1qOfiVcQ]: [Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ); publication: 2026-01-05T17:00:06Z; analysis: `analysis/TqC1qOfiVcQ.json`.
[^Wb2v9Phhnns]: [Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder](https://www.youtube.com/watch?v=Wb2v9Phhnns); publication: 2026-10-14T16:00:25Z; analysis: `analysis/Wb2v9Phhnns.json`.
[^XjI-AR4pt7Y]: [Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA](https://www.youtube.com/watch?v=XjI-AR4pt7Y); publication: 2026-07-20T17:17:53Z; analysis: `analysis/XjI-AR4pt7Y.json`.
[^YBYUvGOuotE]: [MCP = Mega Context Problem - Matt Carey](https://www.youtube.com/watch?v=YBYUvGOuotE); publication: 2026-04-25T17:00:06Z; analysis: `analysis/YBYUvGOuotE.json`.
[^abw_m-DRi1k]: [The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder](https://www.youtube.com/watch?v=abw_m-DRi1k); publication: 2026-10-10T15:00:03Z; analysis: `analysis/abw_m-DRi1k.json`.
[^adfw3xJBx1o]: [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](https://www.youtube.com/watch?v=adfw3xJBx1o); publication: 2026-10-20T19:00:34Z; analysis: `analysis/adfw3xJBx1o.json`.
[^il1c1a2FufU]: [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](https://www.youtube.com/watch?v=il1c1a2FufU); publication: 2026-07-24T15:00:06Z; analysis: `analysis/il1c1a2FufU.json`.
[^kv-QAuKWllQ]: [How we hacked YC Spring 2025 batch’s AI agents — Rene Brandel, Casco](https://www.youtube.com/watch?v=kv-QAuKWllQ); publication: 2025-07-30T15:45:06Z; analysis: `analysis/kv-QAuKWllQ.json`.
[^w7IMuYsBNr8]: [OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)](https://www.youtube.com/watch?v=w7IMuYsBNr8); publication: 2025-07-30T15:00:06Z; analysis: `analysis/w7IMuYsBNr8.json`.
[^wCIYViPd4SU]: [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](https://www.youtube.com/watch?v=wCIYViPd4SU); publication: 2026-09-03T14:30:21Z; analysis: `analysis/wCIYViPd4SU.json`.
