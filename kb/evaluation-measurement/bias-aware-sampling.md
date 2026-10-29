---
{
  "type": "technique",
  "id": "bias-aware-sampling",
  "title": "Combine representative random audits with explicit feedback to avoid selection bias",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2025-08-06T16:14:42Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "L8OoYeDI_ls",
      "resource": "https://www.youtube.com/watch?v=L8OoYeDI_ls",
      "title": "Evals Are Not Unit Tests — Ido Pesok, Vercel v0",
      "author": "Ido Pesok, Vercel v0",
      "last_modified": "2025-08-06T16:14:42Z",
      "analysis_file": "analysis/L8OoYeDI_ls.json"
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

# Combine representative random audits with explicit feedback to avoid selection bias

## What

Combine representative random audits with explicit feedback to avoid selection bias

Thumbs feedback and complaints expose problems, but random traces reveal silent failures and actual usage distribution.

## Evidence

> recommended you can just read through random samples in your log in your logs.
> — 08:10 [^L8OoYeDI_ls]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^L8OoYeDI_ls]: [Evals Are Not Unit Tests — Ido Pesok, Vercel v0](https://www.youtube.com/watch?v=L8OoYeDI_ls); publication: 2025-08-06T16:14:42Z; analysis: `analysis/L8OoYeDI_ls.json`.
