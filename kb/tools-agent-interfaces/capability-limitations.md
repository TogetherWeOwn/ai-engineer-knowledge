---
{
  "type": "technique",
  "id": "capability-limitations",
  "title": "Publish truthful operation limits and unsupported cases as discoverable contracts",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-09T00:30:02Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Emo5FGGY-wM",
      "resource": "https://www.youtube.com/watch?v=Emo5FGGY-wM",
      "title": "Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab",
      "author": "Felipe Blanes, Amazon AGI Lab",
      "last_modified": "2026-10-09T00:30:02Z",
      "analysis_file": "analysis/Emo5FGGY-wM.json"
    },
    {
      "id": "buHC7bQE1X4",
      "resource": "https://www.youtube.com/watch?v=buHC7bQE1X4",
      "title": "Get Out of the Model's Way — Kevin Hou, Google Antigravity",
      "author": "Kevin Hou, Google Antigravity",
      "last_modified": "2026-09-27T18:00:24Z",
      "analysis_file": "analysis/buHC7bQE1X4.json"
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

# Publish truthful operation limits and unsupported cases as discoverable contracts

## What

Publish truthful operation limits and unsupported cases as discoverable contracts

Do not let warm first-person language imply a human identity or physical capabilities the agent does not have.

## Evidence

Source analysis [^Emo5FGGY-wM]; no independently matched timestamped quote published.

Source analysis [^buHC7bQE1X4]; no independently matched timestamped quote published.

> favorite ones. You are software. You do not have a body. You cannot physically
> — 06:06 [^ij-AU9dpJjc]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Emo5FGGY-wM]: [Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab](https://www.youtube.com/watch?v=Emo5FGGY-wM); publication: 2026-10-09T00:30:02Z; analysis: `analysis/Emo5FGGY-wM.json`.
[^buHC7bQE1X4]: [Get Out of the Model's Way — Kevin Hou, Google Antigravity](https://www.youtube.com/watch?v=buHC7bQE1X4); publication: 2026-09-27T18:00:24Z; analysis: `analysis/buHC7bQE1X4.json`.
[^ij-AU9dpJjc]: [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](https://www.youtube.com/watch?v=ij-AU9dpJjc); publication: 2026-06-26T20:00:35Z; analysis: `analysis/ij-AU9dpJjc.json`.
