---
{
  "type": "technique",
  "id": "offline-summary-reuse",
  "title": "Compute reusable source summaries once per content version",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-10-18T09:00:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Btk8wDUVs74",
      "resource": "https://www.youtube.com/watch?v=Btk8wDUVs74",
      "title": "From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com",
      "author": "Omri Bruchim & Tomer Ast, monday.com",
      "last_modified": "2026-07-22T23:00:11Z",
      "analysis_file": "analysis/Btk8wDUVs74.json"
    },
    {
      "id": "Ot4OPrPH4xY",
      "resource": "https://www.youtube.com/watch?v=Ot4OPrPH4xY",
      "title": "The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data",
      "author": "Omer Primor, Bright Data",
      "last_modified": "2026-08-14T16:30:36Z",
      "analysis_file": "analysis/Ot4OPrPH4xY.json"
    },
    {
      "id": "RmJ4rTLV_x4",
      "resource": "https://www.youtube.com/watch?v=RmJ4rTLV_x4",
      "title": "Your Support Team Should Ship Code – Lisa Orr, Zapier",
      "author": "Lisa Orr, Zapier",
      "last_modified": "2025-12-16T17:00:06Z",
      "analysis_file": "analysis/RmJ4rTLV_x4.json"
    },
    {
      "id": "W4pnzOURwHQ",
      "resource": "https://www.youtube.com/watch?v=W4pnzOURwHQ",
      "title": "Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs",
      "author": "Denys Linkov, Wisedocs",
      "last_modified": "2026-10-18T09:00:25Z",
      "analysis_file": "analysis/W4pnzOURwHQ.json"
    },
    {
      "id": "Ywl4LsvHKzU",
      "resource": "https://www.youtube.com/watch?v=Ywl4LsvHKzU",
      "title": "RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot",
      "author": "Yuval Belfer and Niv Granot",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/Ywl4LsvHKzU.json"
    },
    {
      "id": "ZRM_TfEZcIo",
      "resource": "https://www.youtube.com/watch?v=ZRM_TfEZcIo",
      "title": "Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "author": "Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "last_modified": "2026-06-26T14:00:07Z",
      "analysis_file": "analysis/ZRM_TfEZcIo.json"
    },
    {
      "id": "cSz7aL2nl2U",
      "resource": "https://www.youtube.com/watch?v=cSz7aL2nl2U",
      "title": "Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge",
      "author": "Gil Feig, Merge",
      "last_modified": "2026-10-09T23:30:08Z",
      "analysis_file": "analysis/cSz7aL2nl2U.json"
    },
    {
      "id": "h403btjldDQ",
      "resource": "https://www.youtube.com/watch?v=h403btjldDQ",
      "title": "Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa",
      "author": "Dotta Bippa",
      "last_modified": "2026-04-15T21:59:05Z",
      "analysis_file": "analysis/h403btjldDQ.json"
    },
    {
      "id": "mOf-PP4mVjA",
      "resource": "https://www.youtube.com/watch?v=mOf-PP4mVjA",
      "title": "Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs",
      "author": "James Le, TwelveLabs",
      "last_modified": "2026-07-23T02:00:03Z",
      "analysis_file": "analysis/mOf-PP4mVjA.json"
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

# Compute reusable source summaries once per content version

## What

Compute reusable source summaries once per content version

Ingestion-time summaries amortize synthesis cost across many later questions rather than regenerating an identical summary every run.

## Evidence

Source analysis [^Btk8wDUVs74]; no independently matched timestamped quote published.

Source analysis [^Ot4OPrPH4xY]; no independently matched timestamped quote published.

> context and to provide a recommendation, but it takes a long time to run. Now, we
> — 08:02 [^RmJ4rTLV_x4]

Source analysis [^W4pnzOURwHQ]; no independently matched timestamped quote published.

Source analysis [^Ywl4LsvHKzU]; no independently matched timestamped quote published.

Source analysis [^ZRM_TfEZcIo]; no independently matched timestamped quote published.

Source analysis [^cSz7aL2nl2U]; no independently matched timestamped quote published.

Source analysis [^h403btjldDQ]; no independently matched timestamped quote published.

Source analysis [^mOf-PP4mVjA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Btk8wDUVs74]: [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](https://www.youtube.com/watch?v=Btk8wDUVs74); publication: 2026-07-22T23:00:11Z; analysis: `analysis/Btk8wDUVs74.json`.
[^Ot4OPrPH4xY]: [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](https://www.youtube.com/watch?v=Ot4OPrPH4xY); publication: 2026-08-14T16:30:36Z; analysis: `analysis/Ot4OPrPH4xY.json`.
[^RmJ4rTLV_x4]: [Your Support Team Should Ship Code – Lisa Orr, Zapier](https://www.youtube.com/watch?v=RmJ4rTLV_x4); publication: 2025-12-16T17:00:06Z; analysis: `analysis/RmJ4rTLV_x4.json`.
[^W4pnzOURwHQ]: [Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs](https://www.youtube.com/watch?v=W4pnzOURwHQ); publication: 2026-10-18T09:00:25Z; analysis: `analysis/W4pnzOURwHQ.json`.
[^Ywl4LsvHKzU]: [RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot](https://www.youtube.com/watch?v=Ywl4LsvHKzU); publication: 2025-06-03T22:22:28Z; analysis: `analysis/Ywl4LsvHKzU.json`.
[^ZRM_TfEZcIo]: [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo); publication: 2026-06-26T14:00:07Z; analysis: `analysis/ZRM_TfEZcIo.json`.
[^cSz7aL2nl2U]: [Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge](https://www.youtube.com/watch?v=cSz7aL2nl2U); publication: 2026-10-09T23:30:08Z; analysis: `analysis/cSz7aL2nl2U.json`.
[^h403btjldDQ]: [Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa](https://www.youtube.com/watch?v=h403btjldDQ); publication: 2026-04-15T21:59:05Z; analysis: `analysis/h403btjldDQ.json`.
[^mOf-PP4mVjA]: [Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](https://www.youtube.com/watch?v=mOf-PP4mVjA); publication: 2026-07-23T02:00:03Z; analysis: `analysis/mOf-PP4mVjA.json`.
