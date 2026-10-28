---
{
  "type": "technique",
  "id": "stateless-tool-adapters",
  "title": "Use stateless remote tool adapters where the protocol and task semantics support them",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-04-19T15:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "v3Fr2JR47KA",
      "resource": "https://www.youtube.com/watch?v=v3Fr2JR47KA",
      "title": "The Future of MCP — David Soria Parra, Anthropic",
      "author": "David Soria Parra, Anthropic",
      "last_modified": "2026-04-19T15:00:06Z",
      "analysis_file": "analysis/v3Fr2JR47KA.json"
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

# Use stateless remote tool adapters where the protocol and task semantics support them

## What

Use stateless remote tool adapters where the protocol and task semantics support them

Reduce per-session transport affinity to scale remote tool endpoints like ordinary stateless services.

## Evidence

Source analysis [^v3Fr2JR47KA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^v3Fr2JR47KA]: [The Future of MCP — David Soria Parra, Anthropic](https://www.youtube.com/watch?v=v3Fr2JR47KA); publication: 2026-04-19T15:00:06Z; analysis: `analysis/v3Fr2JR47KA.json`.
