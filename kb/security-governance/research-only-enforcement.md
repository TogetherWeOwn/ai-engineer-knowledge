---
{
  "type": "technique",
  "id": "research-only-enforcement",
  "title": "Enforce research and replay modes with write authority disabled and no production data access",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-14T16:00:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Wb2v9Phhnns",
      "resource": "https://www.youtube.com/watch?v=Wb2v9Phhnns",
      "title": "Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder",
      "author": "Jiachen Jiang, Coder",
      "last_modified": "2026-10-14T16:00:25Z",
      "analysis_file": "analysis/Wb2v9Phhnns.json"
    },
    {
      "id": "dQ-_i1tZiws",
      "resource": "https://www.youtube.com/watch?v=dQ-_i1tZiws",
      "title": "Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk",
      "author": "Dmitry Buykin, Maersk",
      "last_modified": "2026-08-29T17:30:21Z",
      "analysis_file": "analysis/dQ-_i1tZiws.json"
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

# Enforce research and replay modes with write authority disabled and no production data access

## What

Enforce research and replay modes with write authority disabled and no production data access

Historical examples are replayed without write permissions so corrections can be checked without production damage.

## Evidence

Source analysis [^Wb2v9Phhnns]; no independently matched timestamped quote published.

> protect the production systems and checking whether behavior improved.
> — 06:06 [^dQ-_i1tZiws]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Wb2v9Phhnns]: [Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder](https://www.youtube.com/watch?v=Wb2v9Phhnns); publication: 2026-10-14T16:00:25Z; analysis: `analysis/Wb2v9Phhnns.json`.
[^dQ-_i1tZiws]: [Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk](https://www.youtube.com/watch?v=dQ-_i1tZiws); publication: 2026-08-29T17:30:21Z; analysis: `analysis/dQ-_i1tZiws.json`.
