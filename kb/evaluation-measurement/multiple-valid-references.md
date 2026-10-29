---
{
  "type": "technique",
  "id": "multiple-valid-references",
  "title": "Support multiple valid reference answers or invariant-based grading for open-ended tasks",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-08-19T14:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "phchDt63qAA",
      "resource": "https://www.youtube.com/watch?v=phchDt63qAA",
      "title": "How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed",
      "author": "Ben Kunkle, Zed",
      "last_modified": "2026-05-30T16:00:06Z",
      "analysis_file": "analysis/phchDt63qAA.json"
    },
    {
      "id": "u6q-byPWUuo",
      "resource": "https://www.youtube.com/watch?v=u6q-byPWUuo",
      "title": "From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge",
      "author": "Chaitanya Asawa, Abridge",
      "last_modified": "2026-08-19T14:00:06Z",
      "analysis_file": "analysis/u6q-byPWUuo.json"
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

# Support multiple valid reference answers or invariant-based grading for open-ended tasks

## What

Support multiple valid reference answers or invariant-based grading for open-ended tasks

For open-ended answers, encode required and forbidden elements; independent authors, adjudication and QA establish the reference.

## Evidence

Source analysis [^phchDt63qAA]; no independently matched timestamped quote published.

> physicians create a rubric. So this rubric said elements of what we wanted
> — 17:10 [^u6q-byPWUuo]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^phchDt63qAA]: [How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed](https://www.youtube.com/watch?v=phchDt63qAA); publication: 2026-05-30T16:00:06Z; analysis: `analysis/phchDt63qAA.json`.
[^u6q-byPWUuo]: [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](https://www.youtube.com/watch?v=u6q-byPWUuo); publication: 2026-08-19T14:00:06Z; analysis: `analysis/u6q-byPWUuo.json`.
