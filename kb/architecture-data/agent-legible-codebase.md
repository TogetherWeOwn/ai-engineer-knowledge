---
{
  "type": "technique",
  "id": "agent-legible-codebase",
  "title": "Organize modules, imports and entry points so agents can navigate and change code reliably",
  "area": "architecture-data",
  "status": "stable",
  "valid_from": "2026-07-14T17:16:43Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "OXMMN-XbxwA",
      "resource": "https://www.youtube.com/watch?v=OXMMN-XbxwA",
      "title": "Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc",
      "author": "Vaidas Razgaitis, Higharc",
      "last_modified": "2026-06-28T19:30:02Z",
      "analysis_file": "analysis/OXMMN-XbxwA.json"
    },
    {
      "id": "_Zcw_sVF6hU",
      "resource": "https://www.youtube.com/watch?v=_Zcw_sVF6hU",
      "title": "The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "author": "Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "last_modified": "2026-04-18T10:30:06Z",
      "analysis_file": "analysis/_Zcw_sVF6hU.json"
    },
    {
      "id": "am_oeAoUhew",
      "resource": "https://www.youtube.com/watch?v=am_oeAoUhew",
      "title": "Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI",
      "author": "Ryan Lopopolo, OpenAI",
      "last_modified": "2026-04-17T00:29:28Z",
      "analysis_file": "analysis/am_oeAoUhew.json"
    },
    {
      "id": "avWhreBUYF0",
      "resource": "https://www.youtube.com/watch?v=avWhreBUYF0",
      "title": "#define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)",
      "author": "Greg Brockman, OpenAI (ft. Jensen Huang)",
      "last_modified": "2025-08-10T16:00:06Z",
      "analysis_file": "analysis/avWhreBUYF0.json"
    },
    {
      "id": "n97BCfyFIvw",
      "resource": "https://www.youtube.com/watch?v=n97BCfyFIvw",
      "title": "\"The engineer of the future is the person who chooses what is worth doing.\" — Addy Osmani, Anthropic",
      "author": "Addy Osmani, Anthropic",
      "last_modified": "2026-07-14T17:16:43Z",
      "analysis_file": "analysis/n97BCfyFIvw.json"
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

# Organize modules, imports and entry points so agents can navigate and change code reliably

## What

Organize modules, imports and entry points so agents can navigate and change code reliably

Bound source-unit size so an agent can inspect a coherent component without consuming excessive context.

## Evidence

Source analysis [^OXMMN-XbxwA]; no independently matched timestamped quote published.

> of behavior. We don't have any dynamic imports.
> — 13:21 [^_Zcw_sVF6hU]

> we can write a test that limits the fact that files are no longer than 350 lines.
> — 14:03 [^am_oeAoUhew]

Source analysis [^avWhreBUYF0]; no independently matched timestamped quote published.

Source analysis [^n97BCfyFIvw]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Lower future change and maintenance cost
- **Speed:** Faster localized reasoning and edits
- **Quality:** Explicit domain/query semantics
- **Reliability:** Narrow testable boundaries and preserved invariants
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^OXMMN-XbxwA]: [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](https://www.youtube.com/watch?v=OXMMN-XbxwA); publication: 2026-06-28T19:30:02Z; analysis: `analysis/OXMMN-XbxwA.json`.
[^_Zcw_sVF6hU]: [The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil](https://www.youtube.com/watch?v=_Zcw_sVF6hU); publication: 2026-04-18T10:30:06Z; analysis: `analysis/_Zcw_sVF6hU.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
[^avWhreBUYF0]: [#define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)](https://www.youtube.com/watch?v=avWhreBUYF0); publication: 2025-08-10T16:00:06Z; analysis: `analysis/avWhreBUYF0.json`.
[^n97BCfyFIvw]: ["The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic](https://www.youtube.com/watch?v=n97BCfyFIvw); publication: 2026-07-14T17:16:43Z; analysis: `analysis/n97BCfyFIvw.json`.
