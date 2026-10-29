---
{
  "type": "technique",
  "id": "scoped-instructions",
  "title": "Route folder and path-scoped instructions deterministically with explicit precedence",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-08-08T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "DdaAABdAqZY",
      "resource": "https://www.youtube.com/watch?v=DdaAABdAqZY",
      "title": "Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft",
      "author": "Christopher Harrison, Microsoft",
      "last_modified": "2025-07-26T07:00:13Z",
      "analysis_file": "analysis/DdaAABdAqZY.json"
    },
    {
      "id": "EAfP8pDs7h4",
      "resource": "https://www.youtube.com/watch?v=EAfP8pDs7h4",
      "title": "[Full Workshop] Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments",
      "author": null,
      "last_modified": "2025-06-27T10:19:00Z",
      "analysis_file": "analysis/EAfP8pDs7h4.json"
    },
    {
      "id": "Z-c11pV_uvU",
      "resource": "https://www.youtube.com/watch?v=Z-c11pV_uvU",
      "title": "Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley",
      "author": "Frank Coyle, UC Berkeley",
      "last_modified": "2026-08-08T16:00:06Z",
      "analysis_file": "analysis/Z-c11pV_uvU.json"
    },
    {
      "id": "eOxOzcw70f0",
      "resource": "https://www.youtube.com/watch?v=eOxOzcw70f0",
      "title": "Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison",
      "author": "Harald Kirschner, Christopher Harrison",
      "last_modified": "2025-08-03T04:30:57Z",
      "analysis_file": "analysis/eOxOzcw70f0.json"
    },
    {
      "id": "i1uPAN6uW4s",
      "resource": "https://www.youtube.com/watch?v=i1uPAN6uW4s",
      "title": "Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments - Harald Kirshner,",
      "author": "Harald Kirshner,",
      "last_modified": "2025-06-27T10:15:59Z",
      "analysis_file": "analysis/i1uPAN6uW4s.json"
    },
    {
      "id": "tHJSZ1-ZqcA",
      "resource": "https://www.youtube.com/watch?v=tHJSZ1-ZqcA",
      "title": "The Agent Awakens: Collaborative Development with Copilot - Christopher Harrison, GitHub",
      "author": "Christopher Harrison, GitHub",
      "last_modified": "2025-06-27T10:11:01Z",
      "analysis_file": "analysis/tHJSZ1-ZqcA.json"
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

# Route folder and path-scoped instructions deterministically with explicit precedence

## What

Route folder and path-scoped instructions deterministically with explicit precedence

Company-wide invariants and local repository/directory rules have different scope; hierarchy avoids injecting every project detail into every request.

## Evidence

Source analysis [^DdaAABdAqZY]; no independently matched timestamped quote published.

Source analysis [^EAfP8pDs7h4]; no independently matched timestamped quote published.

> So, the idea is to have a hierarchical set of rules that that can then control
> — 11:48 [^Z-c11pV_uvU]

Source analysis [^eOxOzcw70f0]; no independently matched timestamped quote published.

Source analysis [^i1uPAN6uW4s]; no independently matched timestamped quote published.

Source analysis [^tHJSZ1-ZqcA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^DdaAABdAqZY]: [Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft](https://www.youtube.com/watch?v=DdaAABdAqZY); publication: 2025-07-26T07:00:13Z; analysis: `analysis/DdaAABdAqZY.json`.
[^EAfP8pDs7h4]: [[Full Workshop] Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments](https://www.youtube.com/watch?v=EAfP8pDs7h4); publication: 2025-06-27T10:19:00Z; analysis: `analysis/EAfP8pDs7h4.json`.
[^Z-c11pV_uvU]: [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Z-c11pV_uvU); publication: 2026-08-08T16:00:06Z; analysis: `analysis/Z-c11pV_uvU.json`.
[^eOxOzcw70f0]: [Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](https://www.youtube.com/watch?v=eOxOzcw70f0); publication: 2025-08-03T04:30:57Z; analysis: `analysis/eOxOzcw70f0.json`.
[^i1uPAN6uW4s]: [Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments - Harald Kirshner,](https://www.youtube.com/watch?v=i1uPAN6uW4s); publication: 2025-06-27T10:15:59Z; analysis: `analysis/i1uPAN6uW4s.json`.
[^tHJSZ1-ZqcA]: [The Agent Awakens: Collaborative Development with Copilot - Christopher Harrison, GitHub](https://www.youtube.com/watch?v=tHJSZ1-ZqcA); publication: 2025-06-27T10:11:01Z; analysis: `analysis/tHJSZ1-ZqcA.json`.
