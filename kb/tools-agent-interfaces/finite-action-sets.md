---
{
  "type": "technique",
  "id": "finite-action-sets",
  "title": "Expose finite single-responsibility action sets for bounded automation",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-21T19:01:02Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KHudyx5wW3U",
      "resource": "https://www.youtube.com/watch?v=KHudyx5wW3U",
      "title": "Agent Frameworks Considered Harmful — Rémi Louf, .txt",
      "author": "Rémi Louf, .txt",
      "last_modified": "2026-08-22T16:30:39Z",
      "analysis_file": "analysis/KHudyx5wW3U.json"
    },
    {
      "id": "NaOkR3VSfR4",
      "resource": "https://www.youtube.com/watch?v=NaOkR3VSfR4",
      "title": "Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya",
      "author": "Viren Baraiya",
      "last_modified": "2026-10-08T22:30:09Z",
      "analysis_file": "analysis/NaOkR3VSfR4.json"
    },
    {
      "id": "OD13PiXw60o",
      "resource": "https://www.youtube.com/watch?v=OD13PiXw60o",
      "title": "Building Multi agent Systems with Finite State Machines",
      "author": null,
      "last_modified": "2025-02-22T17:00:05Z",
      "analysis_file": "analysis/OD13PiXw60o.json"
    },
    {
      "id": "VBCDhRrvlYo",
      "resource": "https://www.youtube.com/watch?v=VBCDhRrvlYo",
      "title": "The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu",
      "author": "Arturo Nunez, Nereu",
      "last_modified": "2026-08-18T15:00:29Z",
      "analysis_file": "analysis/VBCDhRrvlYo.json"
    },
    {
      "id": "bU5gDVyu_28",
      "resource": "https://www.youtube.com/watch?v=bU5gDVyu_28",
      "title": "Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One",
      "author": "Max Kanat-Alexander, Capital One",
      "last_modified": "2026-10-21T19:01:02Z",
      "analysis_file": "analysis/bU5gDVyu_28.json"
    },
    {
      "id": "iQ5xldZ9StU",
      "resource": "https://www.youtube.com/watch?v=iQ5xldZ9StU",
      "title": "Realtime multiplayer, automation, and you! — Idan Gazit, GitHub",
      "author": "Idan Gazit, GitHub",
      "last_modified": "2026-08-08T21:30:06Z",
      "analysis_file": "analysis/iQ5xldZ9StU.json"
    },
    {
      "id": "pZ4DIH2BVqg",
      "resource": "https://www.youtube.com/watch?v=pZ4DIH2BVqg",
      "title": "Pydantic is STILL all you need: Jason Liu",
      "author": null,
      "last_modified": "2024-09-06T17:07:06Z",
      "analysis_file": "analysis/pZ4DIH2BVqg.json"
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

# Expose finite single-responsibility action sets for bounded automation

## What

Expose finite single-responsibility action sets for bounded automation

A planner chooses among event emitters, but deterministic transition guards decide whether the requested move is legal.

## Evidence

> job of the kernel is actually to make bad actions impossible not just unlikely
> — 16:48 [^KHudyx5wW3U]

Source analysis [^NaOkR3VSfR4]; no independently matched timestamped quote published.

> transition guards to enforce that these transitions are valid and direct to the
> — 13:00 [^OD13PiXw60o]

Source analysis [^VBCDhRrvlYo]; no independently matched timestamped quote published.

Source analysis [^bU5gDVyu_28]; no independently matched timestamped quote published.

Source analysis [^iQ5xldZ9StU]; no independently matched timestamped quote published.

> owners are the at least one of the participants of the email based on some
> — 10:42 [^pZ4DIH2BVqg]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KHudyx5wW3U]: [Agent Frameworks Considered Harmful — Rémi Louf, .txt](https://www.youtube.com/watch?v=KHudyx5wW3U); publication: 2026-08-22T16:30:39Z; analysis: `analysis/KHudyx5wW3U.json`.
[^NaOkR3VSfR4]: [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](https://www.youtube.com/watch?v=NaOkR3VSfR4); publication: 2026-10-08T22:30:09Z; analysis: `analysis/NaOkR3VSfR4.json`.
[^OD13PiXw60o]: [Building Multi agent Systems with Finite State Machines](https://www.youtube.com/watch?v=OD13PiXw60o); publication: 2025-02-22T17:00:05Z; analysis: `analysis/OD13PiXw60o.json`.
[^VBCDhRrvlYo]: [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](https://www.youtube.com/watch?v=VBCDhRrvlYo); publication: 2026-08-18T15:00:29Z; analysis: `analysis/VBCDhRrvlYo.json`.
[^bU5gDVyu_28]: [Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One](https://www.youtube.com/watch?v=bU5gDVyu_28); publication: 2026-10-21T19:01:02Z; analysis: `analysis/bU5gDVyu_28.json`.
[^iQ5xldZ9StU]: [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](https://www.youtube.com/watch?v=iQ5xldZ9StU); publication: 2026-08-08T21:30:06Z; analysis: `analysis/iQ5xldZ9StU.json`.
[^pZ4DIH2BVqg]: [Pydantic is STILL all you need: Jason Liu](https://www.youtube.com/watch?v=pZ4DIH2BVqg); publication: 2024-09-06T17:07:06Z; analysis: `analysis/pZ4DIH2BVqg.json`.
