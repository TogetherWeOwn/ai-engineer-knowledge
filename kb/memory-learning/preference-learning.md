---
{
  "type": "technique",
  "id": "preference-learning",
  "title": "Learn scoped preferences from approved edits and overrides, not generic persona adjectives",
  "area": "memory-learning",
  "status": "stable",
  "valid_from": "2026-08-21T15:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "7GMKdpLsxwU",
      "resource": "https://www.youtube.com/watch?v=7GMKdpLsxwU",
      "title": "The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI",
      "author": "Hassan El Mghari, Together AI",
      "last_modified": "2026-08-21T15:00:06Z",
      "analysis_file": "analysis/7GMKdpLsxwU.json"
    },
    {
      "id": "Cz4v1WHVyZc",
      "resource": "https://www.youtube.com/watch?v=Cz4v1WHVyZc",
      "title": "HTML Is All Agents Need — James Russo, HeyGen",
      "author": "James Russo, HeyGen",
      "last_modified": "2026-07-21T18:54:01Z",
      "analysis_file": "analysis/Cz4v1WHVyZc.json"
    },
    {
      "id": "YnNF55QV0zs",
      "resource": "https://www.youtube.com/watch?v=YnNF55QV0zs",
      "title": "Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai",
      "author": "Ishan Anand, InsightSciences.ai",
      "last_modified": "2026-07-29T20:15:35Z",
      "analysis_file": "analysis/YnNF55QV0zs.json"
    },
    {
      "id": "ij-AU9dpJjc",
      "resource": "https://www.youtube.com/watch?v=ij-AU9dpJjc",
      "title": "Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co",
      "author": "Isadora Martin-Dye, Isadora & Co",
      "last_modified": "2026-06-26T20:00:35Z",
      "analysis_file": "analysis/ij-AU9dpJjc.json"
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

# Learn scoped preferences from approved edits and overrides, not generic persona adjectives

## What

Learn scoped preferences from approved edits and overrides, not generic persona adjectives

Examples and actual coordinator edits encode desired phrasing more clearly than simply telling the model to sound on-brand.

## Evidence

Source analysis [^7GMKdpLsxwU]; no independently matched timestamped quote published.

Source analysis [^Cz4v1WHVyZc]; no independently matched timestamped quote published.

Source analysis [^YnNF55QV0zs]; no independently matched timestamped quote published.

> actual AI responses and the AI learns from the edits that the coordinators
> — 13:12 [^ij-AU9dpJjc]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated investigation
- **Speed:** Faster reuse of relevant prior work
- **Quality:** More current, scoped lessons
- **Reliability:** Less stale, conflicting or unsupported recall
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^7GMKdpLsxwU]: [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](https://www.youtube.com/watch?v=7GMKdpLsxwU); publication: 2026-08-21T15:00:06Z; analysis: `analysis/7GMKdpLsxwU.json`.
[^Cz4v1WHVyZc]: [HTML Is All Agents Need — James Russo, HeyGen](https://www.youtube.com/watch?v=Cz4v1WHVyZc); publication: 2026-07-21T18:54:01Z; analysis: `analysis/Cz4v1WHVyZc.json`.
[^YnNF55QV0zs]: [Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai](https://www.youtube.com/watch?v=YnNF55QV0zs); publication: 2026-07-29T20:15:35Z; analysis: `analysis/YnNF55QV0zs.json`.
[^ij-AU9dpJjc]: [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](https://www.youtube.com/watch?v=ij-AU9dpJjc); publication: 2026-06-26T20:00:35Z; analysis: `analysis/ij-AU9dpJjc.json`.
