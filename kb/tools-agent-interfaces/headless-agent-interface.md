---
{
  "type": "technique",
  "id": "headless-agent-interface",
  "title": "Use a bounded official headless CLI or SDK interface for coding-agent execution",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-11T20:30:04Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "FCi4jT86gSw",
      "resource": "https://www.youtube.com/watch?v=FCi4jT86gSw",
      "title": "MCP Is Not Good Yet — David Cramer, Sentry",
      "author": "David Cramer, Sentry",
      "last_modified": "2025-07-03T16:00:06Z",
      "analysis_file": "analysis/FCi4jT86gSw.json"
    },
    {
      "id": "aV_vgUSatqs",
      "resource": "https://www.youtube.com/watch?v=aV_vgUSatqs",
      "title": "Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal",
      "author": "Mark Lummus & Navinkumar Patil, PayPal",
      "last_modified": "2026-10-11T20:30:04Z",
      "analysis_file": "analysis/aV_vgUSatqs.json"
    },
    {
      "id": "uFPAtKIN-FQ",
      "resource": "https://www.youtube.com/watch?v=uFPAtKIN-FQ",
      "title": "Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri",
      "author": null,
      "last_modified": "2025-06-11T16:57:37Z",
      "analysis_file": "analysis/uFPAtKIN-FQ.json"
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

# Use a bounded official headless CLI or SDK interface for coding-agent execution

## What

Use a bounded official headless CLI or SDK interface for coding-agent execution

Run the interactive CLI detached in a tmux session and have the agent drive it with send-keys and read output with capture-pane, giving persistent sessions and resumability for long-running tasks.

## Evidence

Source analysis [^FCi4jT86gSw]; no independently matched timestamped quote published.

Source analysis [^aV_vgUSatqs]; no independently matched timestamped quote published.

Source analysis [^uFPAtKIN-FQ]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^FCi4jT86gSw]: [MCP Is Not Good Yet — David Cramer, Sentry](https://www.youtube.com/watch?v=FCi4jT86gSw); publication: 2025-07-03T16:00:06Z; analysis: `analysis/FCi4jT86gSw.json`.
[^aV_vgUSatqs]: [Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal](https://www.youtube.com/watch?v=aV_vgUSatqs); publication: 2026-10-11T20:30:04Z; analysis: `analysis/aV_vgUSatqs.json`.
[^uFPAtKIN-FQ]: [Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri](https://www.youtube.com/watch?v=uFPAtKIN-FQ); publication: 2025-06-11T16:57:37Z; analysis: `analysis/uFPAtKIN-FQ.json`.
