---
{
  "type": "technique",
  "id": "scoped-domain-context",
  "title": "Use verified domain expertise to narrow the search space before adding model sophistication",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-08-12T16:00:08Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "7CrPrHgoEYk",
      "resource": "https://www.youtube.com/watch?v=7CrPrHgoEYk",
      "title": "What the Best Agents Share — Mardu Swanepoel, Flinn AI",
      "author": "Mardu Swanepoel, Flinn AI",
      "last_modified": "2026-05-26T15:00:06Z",
      "analysis_file": "analysis/7CrPrHgoEYk.json"
    },
    {
      "id": "7wu2hsRfvV0",
      "resource": "https://www.youtube.com/watch?v=7wu2hsRfvV0",
      "title": "How Forward Deployed Engineering is done at Decagon — Sunny Rekhi",
      "author": "Sunny Rekhi",
      "last_modified": "2026-07-28T17:00:35Z",
      "analysis_file": "analysis/7wu2hsRfvV0.json"
    },
    {
      "id": "I6aiEf3aEFQ",
      "resource": "https://www.youtube.com/watch?v=I6aiEf3aEFQ",
      "title": "Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition",
      "author": "Yu Su, NeoCognition",
      "last_modified": "2026-08-12T16:00:08Z",
      "analysis_file": "analysis/I6aiEf3aEFQ.json"
    },
    {
      "id": "SZStlIhyTCY",
      "resource": "https://www.youtube.com/watch?v=SZStlIhyTCY",
      "title": "Moving away from Agile: What's Next – Martin Harrysson & Natasha Maniar, McKinsey & Company",
      "author": "Martin Harrysson & Natasha Maniar, McKinsey & Company",
      "last_modified": "2025-12-12T17:00:06Z",
      "analysis_file": "analysis/SZStlIhyTCY.json"
    },
    {
      "id": "atwSCxWFVMg",
      "resource": "https://www.youtube.com/watch?v=atwSCxWFVMg",
      "title": "GPT Web App Generator - 10,000 apps created in a month: Matija Sosic",
      "author": "10,000 apps created in a month: Matija Sosic",
      "last_modified": "2024-01-26T20:51:42Z",
      "analysis_file": "analysis/atwSCxWFVMg.json"
    },
    {
      "id": "ckLXb15BnM8",
      "resource": "https://www.youtube.com/watch?v=ckLXb15BnM8",
      "title": "The Adversarial Path to the Personal Assistant: Sumit Agarwal",
      "author": null,
      "last_modified": "2025-02-15T19:30:06Z",
      "analysis_file": "analysis/ckLXb15BnM8.json"
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

# Use verified domain expertise to narrow the search space before adding model sophistication

## What

Use verified domain expertise to narrow the search space before adding model sophistication

Constrain generation to known stack conventions and feature shapes instead of asking a general agent to invent everything.

## Evidence

Source analysis [^7CrPrHgoEYk]; no independently matched timestamped quote published.

Source analysis [^7wu2hsRfvV0]; no independently matched timestamped quote published.

Source analysis [^I6aiEf3aEFQ]; no independently matched timestamped quote published.

Source analysis [^SZStlIhyTCY]; no independently matched timestamped quote published.

Source analysis [^atwSCxWFVMg]; no independently matched timestamped quote published.

Source analysis [^ckLXb15BnM8]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^7CrPrHgoEYk]: [What the Best Agents Share — Mardu Swanepoel, Flinn AI](https://www.youtube.com/watch?v=7CrPrHgoEYk); publication: 2026-05-26T15:00:06Z; analysis: `analysis/7CrPrHgoEYk.json`.
[^7wu2hsRfvV0]: [How Forward Deployed Engineering is done at Decagon — Sunny Rekhi](https://www.youtube.com/watch?v=7wu2hsRfvV0); publication: 2026-07-28T17:00:35Z; analysis: `analysis/7wu2hsRfvV0.json`.
[^I6aiEf3aEFQ]: [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](https://www.youtube.com/watch?v=I6aiEf3aEFQ); publication: 2026-08-12T16:00:08Z; analysis: `analysis/I6aiEf3aEFQ.json`.
[^SZStlIhyTCY]: [Moving away from Agile: What's Next – Martin Harrysson & Natasha Maniar, McKinsey & Company](https://www.youtube.com/watch?v=SZStlIhyTCY); publication: 2025-12-12T17:00:06Z; analysis: `analysis/SZStlIhyTCY.json`.
[^atwSCxWFVMg]: [GPT Web App Generator - 10,000 apps created in a month: Matija Sosic](https://www.youtube.com/watch?v=atwSCxWFVMg); publication: 2024-01-26T20:51:42Z; analysis: `analysis/atwSCxWFVMg.json`.
[^ckLXb15BnM8]: [The Adversarial Path to the Personal Assistant: Sumit Agarwal](https://www.youtube.com/watch?v=ckLXb15BnM8); publication: 2025-02-15T19:30:06Z; analysis: `analysis/ckLXb15BnM8.json`.
