---
{
  "type": "technique",
  "id": "escape-rate",
  "title": "Use defect escape rates and non-inferiority as the quality guardrail",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-13T18:00:17Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "X6l4lpA0_NY",
      "resource": "https://www.youtube.com/watch?v=X6l4lpA0_NY",
      "title": "Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl",
      "author": "Dru Knox, Tessl",
      "last_modified": "2026-10-06T15:30:27Z",
      "analysis_file": "analysis/X6l4lpA0_NY.json"
    },
    {
      "id": "ZpK5PWX2YRM",
      "resource": "https://www.youtube.com/watch?v=ZpK5PWX2YRM",
      "title": "Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI",
      "author": "Alex Volkov, ThursdAI",
      "last_modified": "2026-07-10T18:00:06Z",
      "analysis_file": "analysis/ZpK5PWX2YRM.json"
    },
    {
      "id": "b_PmGocP4rc",
      "resource": "https://www.youtube.com/watch?v=b_PmGocP4rc",
      "title": "Evaling Video Slop — Maor Bril, Character.ai",
      "author": "Maor Bril, Character.ai",
      "last_modified": "2026-07-25T00:00:02Z",
      "analysis_file": "analysis/b_PmGocP4rc.json"
    },
    {
      "id": "blrovBxxN9o",
      "resource": "https://www.youtube.com/watch?v=blrovBxxN9o",
      "title": "Turning Fails into Features: Zapier’s Hard-Won Eval Lessons — Rafal Willinski, Vitor Balocco, Zapier",
      "author": "Rafal Willinski, Vitor Balocco, Zapier",
      "last_modified": "2025-06-30T17:15:06Z",
      "analysis_file": "analysis/blrovBxxN9o.json"
    },
    {
      "id": "gDRCpTMCqEU",
      "resource": "https://www.youtube.com/watch?v=gDRCpTMCqEU",
      "title": "What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad",
      "author": "Soukaïna Abelhad",
      "last_modified": "2026-10-13T18:00:17Z",
      "analysis_file": "analysis/gDRCpTMCqEU.json"
    },
    {
      "id": "qqrk7CtkuIw",
      "resource": "https://www.youtube.com/watch?v=qqrk7CtkuIw",
      "title": "How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic",
      "author": "Mike Krieger, Anthropic",
      "last_modified": "2026-08-27T16:00:06Z",
      "analysis_file": "analysis/qqrk7CtkuIw.json"
    },
    {
      "id": "wCIYViPd4SU",
      "resource": "https://www.youtube.com/watch?v=wCIYViPd4SU",
      "title": "Tethered: Our Agents Are Us — Shu Fang, Two Sigma",
      "author": "Shu Fang, Two Sigma",
      "last_modified": "2026-09-03T14:30:21Z",
      "analysis_file": "analysis/wCIYViPd4SU.json"
    },
    {
      "id": "wJwTlvb_TSo",
      "resource": "https://www.youtube.com/watch?v=wJwTlvb_TSo",
      "title": "WTF do people use Open Models for??",
      "author": null,
      "last_modified": "2025-02-22T20:00:06Z",
      "analysis_file": "analysis/wJwTlvb_TSo.json"
    },
    {
      "id": "ynJyIKwjonM",
      "resource": "https://www.youtube.com/watch?v=ynJyIKwjonM",
      "title": "Agentic Search for Context Engineering — Leonie Monigatti, Elastic",
      "author": "Leonie Monigatti, Elastic",
      "last_modified": "2026-05-08T13:00:06Z",
      "analysis_file": "analysis/ynJyIKwjonM.json"
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

# Use defect escape rates and non-inferiority as the quality guardrail

## What

Use defect escape rates and non-inferiority as the quality guardrail

Simple specialized interfaces lower parameter errors, while a constrained general tool covers unusual needs.

## Evidence

> a human to stop that from happening and it feeds back into the inner and the
> — 08:30 [^X6l4lpA0_NY]

> suffers from a little bit of golf. Output does not mean stability, okay?
> — 10:19 [^ZpK5PWX2YRM]

> scored the vibe as opposed to the the the axes. So, it it learned how to how
> — 11:26 [^b_PmGocP4rc]

> lab-like setting. Uh your end goal is user satisfaction. So the ultimate judge
> — 15:29 [^blrovBxxN9o]

> and ask what bad output escaped. So, when arithmetic's definition and
> — 04:05 [^gDRCpTMCqEU]

Source analysis [^qqrk7CtkuIw]; no independently matched timestamped quote published.

Source analysis [^wCIYViPd4SU]; no independently matched timestamped quote published.

Source analysis [^wJwTlvb_TSo]; no independently matched timestamped quote published.

> list of parameters you have, the more difficult um it's going to get for the
> — 12:49 [^ynJyIKwjonM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^X6l4lpA0_NY]: [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](https://www.youtube.com/watch?v=X6l4lpA0_NY); publication: 2026-10-06T15:30:27Z; analysis: `analysis/X6l4lpA0_NY.json`.
[^ZpK5PWX2YRM]: [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](https://www.youtube.com/watch?v=ZpK5PWX2YRM); publication: 2026-07-10T18:00:06Z; analysis: `analysis/ZpK5PWX2YRM.json`.
[^b_PmGocP4rc]: [Evaling Video Slop — Maor Bril, Character.ai](https://www.youtube.com/watch?v=b_PmGocP4rc); publication: 2026-07-25T00:00:02Z; analysis: `analysis/b_PmGocP4rc.json`.
[^blrovBxxN9o]: [Turning Fails into Features: Zapier’s Hard-Won Eval Lessons — Rafal Willinski, Vitor Balocco, Zapier](https://www.youtube.com/watch?v=blrovBxxN9o); publication: 2025-06-30T17:15:06Z; analysis: `analysis/blrovBxxN9o.json`.
[^gDRCpTMCqEU]: [What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad](https://www.youtube.com/watch?v=gDRCpTMCqEU); publication: 2026-10-13T18:00:17Z; analysis: `analysis/gDRCpTMCqEU.json`.
[^qqrk7CtkuIw]: [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](https://www.youtube.com/watch?v=qqrk7CtkuIw); publication: 2026-08-27T16:00:06Z; analysis: `analysis/qqrk7CtkuIw.json`.
[^wCIYViPd4SU]: [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](https://www.youtube.com/watch?v=wCIYViPd4SU); publication: 2026-09-03T14:30:21Z; analysis: `analysis/wCIYViPd4SU.json`.
[^wJwTlvb_TSo]: [WTF do people use Open Models for??](https://www.youtube.com/watch?v=wJwTlvb_TSo); publication: 2025-02-22T20:00:06Z; analysis: `analysis/wJwTlvb_TSo.json`.
[^ynJyIKwjonM]: [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](https://www.youtube.com/watch?v=ynJyIKwjonM); publication: 2026-05-08T13:00:06Z; analysis: `analysis/ynJyIKwjonM.json`.
