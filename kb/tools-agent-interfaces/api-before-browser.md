---
{
  "type": "technique",
  "id": "api-before-browser",
  "title": "Prefer deterministic APIs or DOM automation; reserve visual interaction for gaps",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-08-26T07:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "BurJvbqFr4c",
      "resource": "https://www.youtube.com/watch?v=BurJvbqFr4c",
      "title": "Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses",
      "author": "Tun Shwe, Lenses",
      "last_modified": "2026-04-08T07:31:01Z",
      "analysis_file": "analysis/BurJvbqFr4c.json"
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
      "id": "MLhAA9yguwM",
      "resource": "https://www.youtube.com/watch?v=MLhAA9yguwM",
      "title": "The 3 Pillars of Autonomy – Michele Catasta, Replit",
      "author": "Michele Catasta, Replit",
      "last_modified": "2025-12-22T16:30:06Z",
      "analysis_file": "analysis/MLhAA9yguwM.json"
    },
    {
      "id": "U00AOI1eJUE",
      "resource": "https://www.youtube.com/watch?v=U00AOI1eJUE",
      "title": "Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz",
      "author": "Nimrod Hauser, Baz",
      "last_modified": "2026-04-08T00:45:06Z",
      "analysis_file": "analysis/U00AOI1eJUE.json"
    },
    {
      "id": "XsvUhpnHepE",
      "resource": "https://www.youtube.com/watch?v=XsvUhpnHepE",
      "title": "The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs",
      "author": "Giedrius Šteimantas, Oxylabs",
      "last_modified": "2026-08-26T07:00:06Z",
      "analysis_file": "analysis/XsvUhpnHepE.json"
    },
    {
      "id": "Yphdry8ttAQ",
      "resource": "https://www.youtube.com/watch?v=Yphdry8ttAQ",
      "title": "Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI",
      "author": "Ayush Bhardwaj, Allos AI",
      "last_modified": "2026-08-19T17:00:31Z",
      "analysis_file": "analysis/Yphdry8ttAQ.json"
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
      "id": "ghJmWQCIHRM",
      "resource": "https://www.youtube.com/watch?v=ghJmWQCIHRM",
      "title": "The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google",
      "author": "Tara Agyemang, Google",
      "last_modified": "2026-06-11T16:00:06Z",
      "analysis_file": "analysis/ghJmWQCIHRM.json"
    },
    {
      "id": "v3Fr2JR47KA",
      "resource": "https://www.youtube.com/watch?v=v3Fr2JR47KA",
      "title": "The Future of MCP — David Soria Parra, Anthropic",
      "author": "David Soria Parra, Anthropic",
      "last_modified": "2026-04-19T15:00:06Z",
      "analysis_file": "analysis/v3Fr2JR47KA.json"
    },
    {
      "id": "wEc9aG7cRQc",
      "resource": "https://www.youtube.com/watch?v=wEc9aG7cRQc",
      "title": "Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog",
      "author": "Diane Lin, Datadog",
      "last_modified": "2026-07-20T06:25:22Z",
      "analysis_file": "analysis/wEc9aG7cRQc.json"
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

# Prefer deterministic APIs or DOM automation; reserve visual interaction for gaps

## What

Prefer deterministic APIs or DOM automation; reserve visual interaction for gaps

DOM/browser and API interactions avoid the cost of screenshot-driven computer use; visuals remain available for unobservable cases.

## Evidence

Source analysis [^BurJvbqFr4c]; no independently matched timestamped quote published.

> you you test across the entire court. Uh a lot of people have been talking
> — 07:49 [^L8OoYeDI_ls]

> times what we do is that we have programmatic interactions with the
> — 12:57 [^MLhAA9yguwM]

> snapshot tool. It's actually not a visual snapshot. It's the accessibility
> — 19:46 [^U00AOI1eJUE]

Source analysis [^XsvUhpnHepE]; no independently matched timestamped quote published.

Source analysis [^Yphdry8ttAQ]; no independently matched timestamped quote published.

Source analysis [^eLXF0VojuSs]; no independently matched timestamped quote published.

Source analysis [^ghJmWQCIHRM]; no independently matched timestamped quote published.

> by specifying how you can discover servers on well-known URLs
> — 15:49 [^v3Fr2JR47KA]

Source analysis [^wEc9aG7cRQc]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^BurJvbqFr4c]: [Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses](https://www.youtube.com/watch?v=BurJvbqFr4c); publication: 2026-04-08T07:31:01Z; analysis: `analysis/BurJvbqFr4c.json`.
[^L8OoYeDI_ls]: [Evals Are Not Unit Tests — Ido Pesok, Vercel v0](https://www.youtube.com/watch?v=L8OoYeDI_ls); publication: 2025-08-06T16:14:42Z; analysis: `analysis/L8OoYeDI_ls.json`.
[^MLhAA9yguwM]: [The 3 Pillars of Autonomy – Michele Catasta, Replit](https://www.youtube.com/watch?v=MLhAA9yguwM); publication: 2025-12-22T16:30:06Z; analysis: `analysis/MLhAA9yguwM.json`.
[^U00AOI1eJUE]: [Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz](https://www.youtube.com/watch?v=U00AOI1eJUE); publication: 2026-04-08T00:45:06Z; analysis: `analysis/U00AOI1eJUE.json`.
[^XsvUhpnHepE]: [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](https://www.youtube.com/watch?v=XsvUhpnHepE); publication: 2026-08-26T07:00:06Z; analysis: `analysis/XsvUhpnHepE.json`.
[^Yphdry8ttAQ]: [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](https://www.youtube.com/watch?v=Yphdry8ttAQ); publication: 2026-08-19T17:00:31Z; analysis: `analysis/Yphdry8ttAQ.json`.
[^eLXF0VojuSs]: [How to Construct Domain Specific LLM Evaluation Systems: Hamel Husain and Emil Sedgh](https://www.youtube.com/watch?v=eLXF0VojuSs); publication: 2024-09-19T16:47:24Z; analysis: `analysis/eLXF0VojuSs.json`.
[^ghJmWQCIHRM]: [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](https://www.youtube.com/watch?v=ghJmWQCIHRM); publication: 2026-06-11T16:00:06Z; analysis: `analysis/ghJmWQCIHRM.json`.
[^v3Fr2JR47KA]: [The Future of MCP — David Soria Parra, Anthropic](https://www.youtube.com/watch?v=v3Fr2JR47KA); publication: 2026-04-19T15:00:06Z; analysis: `analysis/v3Fr2JR47KA.json`.
[^wEc9aG7cRQc]: [Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog](https://www.youtube.com/watch?v=wEc9aG7cRQc); publication: 2026-07-20T06:25:22Z; analysis: `analysis/wEc9aG7cRQc.json`.
