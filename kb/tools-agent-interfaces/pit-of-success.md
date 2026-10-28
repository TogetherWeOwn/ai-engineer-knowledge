---
{
  "type": "technique",
  "id": "pit-of-success",
  "title": "Make the safe standard path the easiest executable path",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-14T17:00:04Z",
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
      "id": "tZycGA_Fbfo",
      "resource": "https://www.youtube.com/watch?v=tZycGA_Fbfo",
      "title": "Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma",
      "author": "Harish Gaggar, Credit Karma",
      "last_modified": "2026-10-14T17:00:04Z",
      "analysis_file": "analysis/tZycGA_Fbfo.json"
    },
    {
      "id": "zCJtYuqwm7E",
      "resource": "https://www.youtube.com/watch?v=zCJtYuqwm7E",
      "title": "Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl",
      "author": "Patrick Debois, Tessl",
      "last_modified": "2026-08-22T16:00:06Z",
      "analysis_file": "analysis/zCJtYuqwm7E.json"
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

# Make the safe standard path the easiest executable path

## What

Make the safe standard path the easiest executable path

Generate new projects with memory, tracing/evaluation, context controls, identity and secret handling rather than relying on every builder to remember them.

## Evidence

Source analysis [^0NHCyq8bBcM]; no independently matched timestamped quote published.

> sure they are consistent across the company
> — 05:53 [^tZycGA_Fbfo]

> you probably don't end up with one thing but a catalog of three, four paved roads
> — 13:07 [^zCJtYuqwm7E]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^0NHCyq8bBcM]: [Remote MCPs: What we learned from shipping — John Welsh, Anthropic](https://www.youtube.com/watch?v=0NHCyq8bBcM); publication: 2025-06-19T16:52:25Z; analysis: `analysis/0NHCyq8bBcM.json`.
[^tZycGA_Fbfo]: [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](https://www.youtube.com/watch?v=tZycGA_Fbfo); publication: 2026-10-14T17:00:04Z; analysis: `analysis/tZycGA_Fbfo.json`.
[^zCJtYuqwm7E]: [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](https://www.youtube.com/watch?v=zCJtYuqwm7E); publication: 2026-08-22T16:00:06Z; analysis: `analysis/zCJtYuqwm7E.json`.
