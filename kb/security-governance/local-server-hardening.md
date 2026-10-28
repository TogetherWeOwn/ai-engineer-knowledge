---
{
  "type": "technique",
  "id": "local-server-hardening",
  "title": "Harden local tool servers and interactive sessions against cross-origin access",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-04-16T22:58:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "RjfbvDXpFls",
      "resource": "https://www.youtube.com/watch?v=RjfbvDXpFls",
      "title": "Building pi in a World of Slop — Mario Zechner",
      "author": "Mario Zechner",
      "last_modified": "2026-04-16T22:58:06Z",
      "analysis_file": "analysis/RjfbvDXpFls.json"
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

# Harden local tool servers and interactive sessions against cross-origin access

## What

Harden local tool servers and interactive sessions against cross-origin access

A permissive local server can let arbitrary visited websites reach privileged agent capabilities.

## Evidence

> up, course headers are set in such a way that any website you open in your
> — 04:36 [^RjfbvDXpFls]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^RjfbvDXpFls]: [Building pi in a World of Slop — Mario Zechner](https://www.youtube.com/watch?v=RjfbvDXpFls); publication: 2026-04-16T22:58:06Z; analysis: `analysis/RjfbvDXpFls.json`.
