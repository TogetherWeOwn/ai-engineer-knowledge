---
{
  "type": "technique",
  "id": "investment-decay-review",
  "title": "Revisit capability investments using measured value, decay and existing roadmap constraints",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-08-29T14:30:22Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "gWLVu9OGvBg",
      "resource": "https://www.youtube.com/watch?v=gWLVu9OGvBg",
      "title": "Understanding AI Stakes to Break Production Code: Philip Rathle",
      "author": null,
      "last_modified": "2024-12-31T17:17:42Z",
      "analysis_file": "analysis/gWLVu9OGvBg.json"
    },
    {
      "id": "iCj_ATyThvc",
      "resource": "https://www.youtube.com/watch?v=iCj_ATyThvc",
      "title": "How Autoresearch is changing ML research — Zhengyao Jiang, Weco",
      "author": "Zhengyao Jiang, Weco",
      "last_modified": "2026-07-16T18:08:16Z",
      "analysis_file": "analysis/iCj_ATyThvc.json"
    },
    {
      "id": "n97BCfyFIvw",
      "resource": "https://www.youtube.com/watch?v=n97BCfyFIvw",
      "title": "\"The engineer of the future is the person who chooses what is worth doing.\" — Addy Osmani, Anthropic",
      "author": "Addy Osmani, Anthropic",
      "last_modified": "2026-07-14T17:16:43Z",
      "analysis_file": "analysis/n97BCfyFIvw.json"
    },
    {
      "id": "sM1iYgz93HI",
      "resource": "https://www.youtube.com/watch?v=sM1iYgz93HI",
      "title": "The Half Life of Agent Infrastructure — Ben Kus, Box",
      "author": "Ben Kus, Box",
      "last_modified": "2026-08-29T14:30:22Z",
      "analysis_file": "analysis/sM1iYgz93HI.json"
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

# Revisit capability investments using measured value, decay and existing roadmap constraints

## What

Revisit capability investments using measured value, decay and existing roadmap constraints

Search papers, comments and unmerged work for useful ideas people could not finish, then validate their applicability.

## Evidence

Source analysis [^gWLVu9OGvBg]; no independently matched timestamped quote published.

> researcher said oh I give up this idea because of some implementation
> — 06:07 [^iCj_ATyThvc]

Source analysis [^n97BCfyFIvw]; no independently matched timestamped quote published.

Source analysis [^sM1iYgz93HI]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^gWLVu9OGvBg]: [Understanding AI Stakes to Break Production Code: Philip Rathle](https://www.youtube.com/watch?v=gWLVu9OGvBg); publication: 2024-12-31T17:17:42Z; analysis: `analysis/gWLVu9OGvBg.json`.
[^iCj_ATyThvc]: [How Autoresearch is changing ML research — Zhengyao Jiang, Weco](https://www.youtube.com/watch?v=iCj_ATyThvc); publication: 2026-07-16T18:08:16Z; analysis: `analysis/iCj_ATyThvc.json`.
[^n97BCfyFIvw]: ["The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic](https://www.youtube.com/watch?v=n97BCfyFIvw); publication: 2026-07-14T17:16:43Z; analysis: `analysis/n97BCfyFIvw.json`.
[^sM1iYgz93HI]: [The Half Life of Agent Infrastructure — Ben Kus, Box](https://www.youtube.com/watch?v=sM1iYgz93HI); publication: 2026-08-29T14:30:22Z; analysis: `analysis/sM1iYgz93HI.json`.
