---
{
  "type": "technique",
  "id": "instruction-fidelity",
  "title": "Preserve the original winning request and final intent across handoffs",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-08-08T21:30:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "UG9IAdmi2Dg",
      "resource": "https://www.youtube.com/watch?v=UG9IAdmi2Dg",
      "title": "Building the platform for agent coordination — Tom Moor, Linear",
      "author": "Tom Moor, Linear",
      "last_modified": "2025-07-28T19:37:32Z",
      "analysis_file": "analysis/UG9IAdmi2Dg.json"
    },
    {
      "id": "VaS2h-dY1-4",
      "resource": "https://www.youtube.com/watch?v=VaS2h-dY1-4",
      "title": "Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw",
      "author": "Onur Solmaz, OpenClaw",
      "last_modified": "2026-05-21T15:00:06Z",
      "analysis_file": "analysis/VaS2h-dY1-4.json"
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
      "id": "sKiTUuEV1rw",
      "resource": "https://www.youtube.com/watch?v=sKiTUuEV1rw",
      "title": "[Full Workshop from Microsoft] Github Copilot - The World's Most Widely Adopted AI Developer Tool",
      "author": "The World's Most Widely Adopted AI Developer Tool",
      "last_modified": "2025-02-07T20:28:55Z",
      "analysis_file": "analysis/sKiTUuEV1rw.json"
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

# Preserve the original winning request and final intent across handoffs

## What

Preserve the original winning request and final intent across handoffs

Bind the user's request directly to the executing session and retain it verbatim, avoiding meaning changes from an intermediary LLM paraphrase.

## Evidence

Source analysis [^UG9IAdmi2Dg]; no independently matched timestamped quote published.

Source analysis [^VaS2h-dY1-4]; no independently matched timestamped quote published.

Source analysis [^iQ5xldZ9StU]; no independently matched timestamped quote published.

Source analysis [^sKiTUuEV1rw]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^UG9IAdmi2Dg]: [Building the platform for agent coordination — Tom Moor, Linear](https://www.youtube.com/watch?v=UG9IAdmi2Dg); publication: 2025-07-28T19:37:32Z; analysis: `analysis/UG9IAdmi2Dg.json`.
[^VaS2h-dY1-4]: [Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw](https://www.youtube.com/watch?v=VaS2h-dY1-4); publication: 2026-05-21T15:00:06Z; analysis: `analysis/VaS2h-dY1-4.json`.
[^iQ5xldZ9StU]: [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](https://www.youtube.com/watch?v=iQ5xldZ9StU); publication: 2026-08-08T21:30:06Z; analysis: `analysis/iQ5xldZ9StU.json`.
[^sKiTUuEV1rw]: [[Full Workshop from Microsoft] Github Copilot - The World's Most Widely Adopted AI Developer Tool](https://www.youtube.com/watch?v=sKiTUuEV1rw); publication: 2025-02-07T20:28:55Z; analysis: `analysis/sKiTUuEV1rw.json`.
