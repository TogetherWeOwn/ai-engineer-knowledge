---
{
  "type": "technique",
  "id": "instruction-trust",
  "title": "Verify repository instruction provenance before automatically loading executable procedures",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-05-03T14:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "bSG9wUYaHWU",
      "resource": "https://www.youtube.com/watch?v=bSG9wUYaHWU",
      "title": "Context Is the New Code — Patrick Debois, Tessl",
      "author": "Patrick Debois, Tessl",
      "last_modified": "2026-05-03T14:00:06Z",
      "analysis_file": "analysis/bSG9wUYaHWU.json"
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

# Verify repository instruction provenance before automatically loading executable procedures

## What

Verify repository instruction provenance before automatically loading executable procedures

Filesystem isolation does not stop an agent from reading malicious AGENTS.md or SKILL.md; instruction admission is a separate boundary.

## Evidence

> sandboxes. You need to have another way. I call that a context filter. Think of
> — 21:59 [^bSG9wUYaHWU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^bSG9wUYaHWU]: [Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU); publication: 2026-05-03T14:00:06Z; analysis: `analysis/bSG9wUYaHWU.json`.
