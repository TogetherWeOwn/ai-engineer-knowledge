---
{
  "type": "technique",
  "id": "own-visual-assets",
  "title": "Create owned design assets and verify them in the actual rendered application",
  "area": "product-ui-quality",
  "status": "stable",
  "valid_from": "2026-07-15T15:05:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "MhHEGMFCEB0",
      "resource": "https://www.youtube.com/watch?v=MhHEGMFCEB0",
      "title": "OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman",
      "author": "Vaibhav Srivastav & Katia Gil Guzman",
      "last_modified": "2026-04-29T16:00:06Z",
      "analysis_file": "analysis/MhHEGMFCEB0.json"
    },
    {
      "id": "XZ0boOjtbNo",
      "resource": "https://www.youtube.com/watch?v=XZ0boOjtbNo",
      "title": "AI Didn’t Kill the Web, It Moved in! — Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)",
      "author": "Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)",
      "last_modified": "2026-04-10T00:24:17Z",
      "analysis_file": "analysis/XZ0boOjtbNo.json"
    },
    {
      "id": "uU5Gv2h8-9g",
      "resource": "https://www.youtube.com/watch?v=uU5Gv2h8-9g",
      "title": "Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison",
      "author": "Cat Wu & Thariq Shihipar ft Simon Willison",
      "last_modified": "2026-07-15T15:05:06Z",
      "analysis_file": "analysis/uU5Gv2h8-9g.json"
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

# Create owned design assets and verify them in the actual rendered application

## What

Create owned design assets and verify them in the actual rendered application

Asset generation becomes useful when paired with browser feedback on the integrated result, not isolated images.

## Evidence

> And I'm asking it to use Imagen to create visual assets, so sprites for the
> — 16:59 [^MhHEGMFCEB0]

Source analysis [^XZ0boOjtbNo]; no independently matched timestamped quote published.

> does all this stuff. It does ffmpeg, it does remotion, it does.
> — 43:31 [^uU5Gv2h8-9g]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less rework from misunderstood intent
- **Speed:** Faster useful feedback on runnable behavior
- **Quality:** Better usability, accessibility and actual task completion
- **Reliability:** Real-app evidence rather than attractive but broken demos
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^MhHEGMFCEB0]: [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](https://www.youtube.com/watch?v=MhHEGMFCEB0); publication: 2026-04-29T16:00:06Z; analysis: `analysis/MhHEGMFCEB0.json`.
[^XZ0boOjtbNo]: [AI Didn’t Kill the Web, It Moved in! — Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](https://www.youtube.com/watch?v=XZ0boOjtbNo); publication: 2026-04-10T00:24:17Z; analysis: `analysis/XZ0boOjtbNo.json`.
[^uU5Gv2h8-9g]: [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](https://www.youtube.com/watch?v=uU5Gv2h8-9g); publication: 2026-07-15T15:05:06Z; analysis: `analysis/uU5Gv2h8-9g.json`.
