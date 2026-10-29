---
{
  "type": "technique",
  "id": "code-mode",
  "title": "Offer sandboxed code-mode access to typed APIs",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-12T06:07:50Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-rsTkYgnNzM",
      "resource": "https://www.youtube.com/watch?v=-rsTkYgnNzM",
      "title": "Rethinking how we Scaffold AI Agents - Rahul Sengottuvelu, Ramp",
      "author": "Rahul Sengottuvelu, Ramp",
      "last_modified": "2025-03-19T17:09:54Z",
      "analysis_file": "analysis/-rsTkYgnNzM.json"
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
      "id": "8oyalrfwgjw",
      "resource": "https://www.youtube.com/watch?v=8oyalrfwgjw",
      "title": "RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI",
      "author": "Shashi, Superagentic AI",
      "last_modified": "2026-07-12T23:00:06Z",
      "analysis_file": "analysis/8oyalrfwgjw.json"
    },
    {
      "id": "8txf05vVVl4",
      "resource": "https://www.youtube.com/watch?v=8txf05vVVl4",
      "title": "Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare",
      "author": "Sunil Pai, Cloudflare",
      "last_modified": "2026-04-19T17:19:35Z",
      "analysis_file": "analysis/8txf05vVVl4.json"
    },
    {
      "id": "CEvIs9y1uog",
      "resource": "https://www.youtube.com/watch?v=CEvIs9y1uog",
      "title": "Don't Build Agents, Build Skills Instead – Barry Zhang & Mahesh Murag, Anthropic",
      "author": "Barry Zhang & Mahesh Murag, Anthropic",
      "last_modified": "2025-12-08T17:30:06Z",
      "analysis_file": "analysis/CEvIs9y1uog.json"
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
      "id": "HEFSExa0xl0",
      "resource": "https://www.youtube.com/watch?v=HEFSExa0xl0",
      "title": "Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs",
      "author": "Nuno Campos, Witan Labs",
      "last_modified": "2026-07-08T09:03:25Z",
      "analysis_file": "analysis/HEFSExa0xl0.json"
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
      "id": "fmZWvE7yDZo",
      "resource": "https://www.youtube.com/watch?v=fmZWvE7yDZo",
      "title": "UX Design Principles for Semi Autonomous Multi Agent Systems — Victor Dibia, Microsoft",
      "author": "Victor Dibia, Microsoft",
      "last_modified": "2025-07-21T19:11:17Z",
      "analysis_file": "analysis/fmZWvE7yDZo.json"
    },
    {
      "id": "jHMiYtjoJfA",
      "resource": "https://www.youtube.com/watch?v=jHMiYtjoJfA",
      "title": "Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop",
      "author": "Ben Hylak, Raindrop",
      "last_modified": "2026-08-12T18:00:34Z",
      "analysis_file": "analysis/jHMiYtjoJfA.json"
    },
    {
      "id": "nnktgWtfJHE",
      "resource": "https://www.youtube.com/watch?v=nnktgWtfJHE",
      "title": "Blender MCP and The Future Of Creative Tools - Siddharth Ahuja",
      "author": "Siddharth Ahuja",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/nnktgWtfJHE.json"
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
      "id": "vi-2nasppAg",
      "resource": "https://www.youtube.com/watch?v=vi-2nasppAg",
      "title": "Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate",
      "author": "Jonas Templestein, Iterate",
      "last_modified": "2026-05-14T14:00:06Z",
      "analysis_file": "analysis/vi-2nasppAg.json"
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

# Offer sandboxed code-mode access to typed APIs

## What

Offer sandboxed code-mode access to typed APIs

Compact input/output types guide generated code against a large API instead of requiring a separate model tool decision per endpoint.

## Evidence

Source analysis [^-rsTkYgnNzM]; no independently matched timestamped quote published.

Source analysis [^33Oct2hqGnk]; no independently matched timestamped quote published.

Source analysis [^8oyalrfwgjw]; no independently matched timestamped quote published.

Source analysis [^8txf05vVVl4]; no independently matched timestamped quote published.

Source analysis [^CEvIs9y1uog]; no independently matched timestamped quote published.

Source analysis [^FGftGOzfohc]; no independently matched timestamped quote published.

Source analysis [^HEFSExa0xl0]; no independently matched timestamped quote published.

> generates this code um against a typed SDK that we generate from our API. You
> — 08:13 [^YBYUvGOuotE]

> tool calls, you can have one tool called code where the model generates the code
> — 15:05 [^YBYUvGOuotE]

Source analysis [^fmZWvE7yDZo]; no independently matched timestamped quote published.

Source analysis [^jHMiYtjoJfA]; no independently matched timestamped quote published.

Source analysis [^nnktgWtfJHE]; no independently matched timestamped quote published.

> all of it stuff could be done way more effective if you would instead write
> — 10:12 [^v3Fr2JR47KA]

Source analysis [^vi-2nasppAg]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-rsTkYgnNzM]: [Rethinking how we Scaffold AI Agents - Rahul Sengottuvelu, Ramp](https://www.youtube.com/watch?v=-rsTkYgnNzM); publication: 2025-03-19T17:09:54Z; analysis: `analysis/-rsTkYgnNzM.json`.
[^33Oct2hqGnk]: [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](https://www.youtube.com/watch?v=33Oct2hqGnk); publication: 2026-10-04T21:00:13Z; analysis: `analysis/33Oct2hqGnk.json`.
[^8oyalrfwgjw]: [RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](https://www.youtube.com/watch?v=8oyalrfwgjw); publication: 2026-07-12T23:00:06Z; analysis: `analysis/8oyalrfwgjw.json`.
[^8txf05vVVl4]: [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](https://www.youtube.com/watch?v=8txf05vVVl4); publication: 2026-04-19T17:19:35Z; analysis: `analysis/8txf05vVVl4.json`.
[^CEvIs9y1uog]: [Don't Build Agents, Build Skills Instead – Barry Zhang & Mahesh Murag, Anthropic](https://www.youtube.com/watch?v=CEvIs9y1uog); publication: 2025-12-08T17:30:06Z; analysis: `analysis/CEvIs9y1uog.json`.
[^FGftGOzfohc]: [Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](https://www.youtube.com/watch?v=FGftGOzfohc); publication: 2026-10-12T06:07:50Z; analysis: `analysis/FGftGOzfohc.json`.
[^HEFSExa0xl0]: [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](https://www.youtube.com/watch?v=HEFSExa0xl0); publication: 2026-07-08T09:03:25Z; analysis: `analysis/HEFSExa0xl0.json`.
[^YBYUvGOuotE]: [MCP = Mega Context Problem - Matt Carey](https://www.youtube.com/watch?v=YBYUvGOuotE); publication: 2026-04-25T17:00:06Z; analysis: `analysis/YBYUvGOuotE.json`.
[^fmZWvE7yDZo]: [UX Design Principles for Semi Autonomous Multi Agent Systems — Victor Dibia, Microsoft](https://www.youtube.com/watch?v=fmZWvE7yDZo); publication: 2025-07-21T19:11:17Z; analysis: `analysis/fmZWvE7yDZo.json`.
[^jHMiYtjoJfA]: [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](https://www.youtube.com/watch?v=jHMiYtjoJfA); publication: 2026-08-12T18:00:34Z; analysis: `analysis/jHMiYtjoJfA.json`.
[^nnktgWtfJHE]: [Blender MCP and The Future Of Creative Tools - Siddharth Ahuja](https://www.youtube.com/watch?v=nnktgWtfJHE); publication: 2025-06-03T22:22:29Z; analysis: `analysis/nnktgWtfJHE.json`.
[^v3Fr2JR47KA]: [The Future of MCP — David Soria Parra, Anthropic](https://www.youtube.com/watch?v=v3Fr2JR47KA); publication: 2026-04-19T15:00:06Z; analysis: `analysis/v3Fr2JR47KA.json`.
[^vi-2nasppAg]: [Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate](https://www.youtube.com/watch?v=vi-2nasppAg); publication: 2026-05-14T14:00:06Z; analysis: `analysis/vi-2nasppAg.json`.
