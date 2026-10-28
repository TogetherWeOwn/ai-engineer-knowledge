---
{
  "type": "technique",
  "id": "tool-recovery-curriculum",
  "title": "Use deterministic detours and recovery examples for repeated wrong-tool habits",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-06-05T17:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "_B4Pv9ttFgY",
      "resource": "https://www.youtube.com/watch?v=_B4Pv9ttFgY",
      "title": "Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google",
      "author": "Michael Hablich, Google",
      "last_modified": "2026-06-05T17:00:06Z",
      "analysis_file": "analysis/_B4Pv9ttFgY.json"
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

# Use deterministic detours and recovery examples for repeated wrong-tool habits

## What

Use deterministic detours and recovery examples for repeated wrong-tool habits

At known confusion points, tell the agent the preferred operation before it chooses a familiar but unsuitable one.

## Evidence

> And that's what you can do with proactive detours. Like in this example,
> — 14:37 [^_B4Pv9ttFgY]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^_B4Pv9ttFgY]: [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](https://www.youtube.com/watch?v=_B4Pv9ttFgY); publication: 2026-06-05T17:00:06Z; analysis: `analysis/_B4Pv9ttFgY.json`.
