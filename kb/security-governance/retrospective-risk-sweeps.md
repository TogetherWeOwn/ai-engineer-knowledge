---
{
  "type": "technique",
  "id": "retrospective-risk-sweeps",
  "title": "Back-scan existing repositories and saved artifacts for newly confirmed risk patterns",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-07-29T22:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "UXOLprPvr-0",
      "resource": "https://www.youtube.com/watch?v=UXOLprPvr-0",
      "title": "Building AI Agents with Real ROI in the Enterprise SDLC: Bruno (Booking.com) & Beyang (Sourcegraph)",
      "author": null,
      "last_modified": "2025-04-08T17:00:06Z",
      "analysis_file": "analysis/UXOLprPvr-0.json"
    },
    {
      "id": "iKQ78wyJEXU",
      "resource": "https://www.youtube.com/watch?v=iKQ78wyJEXU",
      "title": "We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank",
      "author": "Lucas Palma, Nubank",
      "last_modified": "2026-07-29T22:00:06Z",
      "analysis_file": "analysis/iKQ78wyJEXU.json"
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

# Back-scan existing repositories and saved artifacts for newly confirmed risk patterns

## What

Back-scan existing repositories and saved artifacts for newly confirmed risk patterns

A historical defect's context and affected code paths seed a targeted search for the same failure pattern elsewhere.

## Evidence

Source analysis [^UXOLprPvr-0]; no independently matched timestamped quote published.

Source analysis [^iKQ78wyJEXU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^UXOLprPvr-0]: [Building AI Agents with Real ROI in the Enterprise SDLC: Bruno (Booking.com) & Beyang (Sourcegraph)](https://www.youtube.com/watch?v=UXOLprPvr-0); publication: 2025-04-08T17:00:06Z; analysis: `analysis/UXOLprPvr-0.json`.
[^iKQ78wyJEXU]: [We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](https://www.youtube.com/watch?v=iKQ78wyJEXU); publication: 2026-07-29T22:00:06Z; analysis: `analysis/iKQ78wyJEXU.json`.
