---
{
  "type": "technique",
  "id": "trajectory-efficiency",
  "title": "Diagnose repetition, context rereads and unproductive steps separately from final-answer quality",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-22T19:00:39Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "AMiyLItEtLA",
      "resource": "https://www.youtube.com/watch?v=AMiyLItEtLA",
      "title": "fighting slop with slop — Vaibhav Gupta, Boundary",
      "author": "Vaibhav Gupta, Boundary",
      "last_modified": "2026-07-31T01:11:30Z",
      "analysis_file": "analysis/AMiyLItEtLA.json"
    },
    {
      "id": "EL123UNokkI",
      "resource": "https://www.youtube.com/watch?v=EL123UNokkI",
      "title": "Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber",
      "author": "Will Bond & Ameya Ketkar, Uber",
      "last_modified": "2026-08-28T14:30:12Z",
      "analysis_file": "analysis/EL123UNokkI.json"
    },
    {
      "id": "Ve2bAarPA2I",
      "resource": "https://www.youtube.com/watch?v=Ve2bAarPA2I",
      "title": "Better AI Models Won't Fix Your Engineering Team — Nicholas Arcolano, Jellyfish",
      "author": "Nicholas Arcolano, Jellyfish",
      "last_modified": "2026-10-22T19:00:39Z",
      "analysis_file": "analysis/Ve2bAarPA2I.json"
    },
    {
      "id": "fLUtUkqYHnQ",
      "resource": "https://www.youtube.com/watch?v=fLUtUkqYHnQ",
      "title": "Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI",
      "author": "Maxime Labonne, Liquid AI",
      "last_modified": "2026-04-29T12:00:06Z",
      "analysis_file": "analysis/fLUtUkqYHnQ.json"
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
      "id": "q2JrUKBMf0w",
      "resource": "https://www.youtube.com/watch?v=q2JrUKBMf0w",
      "title": "The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI",
      "author": "Aparna Dhinakaran, Arize AI",
      "last_modified": "2026-07-24T20:00:06Z",
      "analysis_file": "analysis/q2JrUKBMf0w.json"
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

# Diagnose repetition, context rereads and unproductive steps separately from final-answer quality

## What

Diagnose repetition, context rereads and unproductive steps separately from final-answer quality

Repeated calls and loops can waste time even when the final response appears acceptable.

## Evidence

Source analysis [^AMiyLItEtLA]; no independently matched timestamped quote published.

Source analysis [^EL123UNokkI]; no independently matched timestamped quote published.

Source analysis [^Ve2bAarPA2I]; no independently matched timestamped quote published.

Source analysis [^fLUtUkqYHnQ]; no independently matched timestamped quote published.

Source analysis [^n97BCfyFIvw]; no independently matched timestamped quote published.

> even think of doing, such as something going on in a loop for multiple times,
> — 05:04 [^q2JrUKBMf0w]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^AMiyLItEtLA]: [fighting slop with slop — Vaibhav Gupta, Boundary](https://www.youtube.com/watch?v=AMiyLItEtLA); publication: 2026-07-31T01:11:30Z; analysis: `analysis/AMiyLItEtLA.json`.
[^EL123UNokkI]: [Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](https://www.youtube.com/watch?v=EL123UNokkI); publication: 2026-08-28T14:30:12Z; analysis: `analysis/EL123UNokkI.json`.
[^Ve2bAarPA2I]: [Better AI Models Won't Fix Your Engineering Team — Nicholas Arcolano, Jellyfish](https://www.youtube.com/watch?v=Ve2bAarPA2I); publication: 2026-10-22T19:00:39Z; analysis: `analysis/Ve2bAarPA2I.json`.
[^fLUtUkqYHnQ]: [Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI](https://www.youtube.com/watch?v=fLUtUkqYHnQ); publication: 2026-04-29T12:00:06Z; analysis: `analysis/fLUtUkqYHnQ.json`.
[^n97BCfyFIvw]: ["The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic](https://www.youtube.com/watch?v=n97BCfyFIvw); publication: 2026-07-14T17:16:43Z; analysis: `analysis/n97BCfyFIvw.json`.
[^q2JrUKBMf0w]: [The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI](https://www.youtube.com/watch?v=q2JrUKBMf0w); publication: 2026-07-24T20:00:06Z; analysis: `analysis/q2JrUKBMf0w.json`.
