---
{
  "type": "technique",
  "id": "risk-shaped-tool-interface",
  "title": "Choose the tool interface by action risk, composability and required state",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-04-19T15:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "TqC1qOfiVcQ",
      "resource": "https://www.youtube.com/watch?v=TqC1qOfiVcQ",
      "title": "Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic",
      "author": "Thariq Shihipar, Anthropic",
      "last_modified": "2026-01-05T17:00:06Z",
      "analysis_file": "analysis/TqC1qOfiVcQ.json"
    },
    {
      "id": "aopgVJBQC0o",
      "resource": "https://www.youtube.com/watch?v=aopgVJBQC0o",
      "title": "Excalidraw: AI and Human Whiteboarding Partnership - Christopher Chedeau",
      "author": "Christopher Chedeau",
      "last_modified": "2025-07-21T19:12:58Z",
      "analysis_file": "analysis/aopgVJBQC0o.json"
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
      "id": "w7IMuYsBNr8",
      "resource": "https://www.youtube.com/watch?v=w7IMuYsBNr8",
      "title": "OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)",
      "author": "Fouad Matin (Codex, Agent Robustness)",
      "last_modified": "2025-07-30T15:00:06Z",
      "analysis_file": "analysis/w7IMuYsBNr8.json"
    },
    {
      "id": "x-8pBqWiTzk",
      "resource": "https://www.youtube.com/watch?v=x-8pBqWiTzk",
      "title": "MCP: Origins and Requests For Startups — Theodora Chu, Model Context Protocol PM, Anthropic",
      "author": "Theodora Chu, Model Context Protocol PM, Anthropic",
      "last_modified": "2025-06-18T22:55:21Z",
      "analysis_file": "analysis/x-8pBqWiTzk.json"
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

# Choose the tool interface by action risk, composability and required state

## What

Choose the tool interface by action risk, composability and required state

Typed tools suit atomic controlled actions; scripts/CLI and generated code suit composable read/analysis work. Avoid exposing a tool for every tiny API operation.

## Evidence

> want to think about them as atomic actions your agent usually needs to
> — 27:58 [^TqC1qOfiVcQ]

Source analysis [^aopgVJBQC0o]; no independently matched timestamped quote published.

> tool for the right job. And in my mind, there are three major things that you
> — 05:26 [^v3Fr2JR47KA]

Source analysis [^w7IMuYsBNr8]; no independently matched timestamped quote published.

Source analysis [^x-8pBqWiTzk]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^TqC1qOfiVcQ]: [Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ); publication: 2026-01-05T17:00:06Z; analysis: `analysis/TqC1qOfiVcQ.json`.
[^aopgVJBQC0o]: [Excalidraw: AI and Human Whiteboarding Partnership - Christopher Chedeau](https://www.youtube.com/watch?v=aopgVJBQC0o); publication: 2025-07-21T19:12:58Z; analysis: `analysis/aopgVJBQC0o.json`.
[^v3Fr2JR47KA]: [The Future of MCP — David Soria Parra, Anthropic](https://www.youtube.com/watch?v=v3Fr2JR47KA); publication: 2026-04-19T15:00:06Z; analysis: `analysis/v3Fr2JR47KA.json`.
[^w7IMuYsBNr8]: [OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)](https://www.youtube.com/watch?v=w7IMuYsBNr8); publication: 2025-07-30T15:00:06Z; analysis: `analysis/w7IMuYsBNr8.json`.
[^x-8pBqWiTzk]: [MCP: Origins and Requests For Startups — Theodora Chu, Model Context Protocol PM, Anthropic](https://www.youtube.com/watch?v=x-8pBqWiTzk); publication: 2025-06-18T22:55:21Z; analysis: `analysis/x-8pBqWiTzk.json`.
