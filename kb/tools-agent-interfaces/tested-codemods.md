---
{
  "type": "technique",
  "id": "tested-codemods",
  "title": "Use tested source-aware codemods for repetitive repository-wide edits",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-04T19:30:20Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Bdrs3uAX0_M",
      "resource": "https://www.youtube.com/watch?v=Bdrs3uAX0_M",
      "title": "AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph",
      "author": "Dan Adler, Sourcegraph",
      "last_modified": "2026-10-04T19:30:20Z",
      "analysis_file": "analysis/Bdrs3uAX0_M.json"
    },
    {
      "id": "GqoNrUz8hEU",
      "resource": "https://www.youtube.com/watch?v=GqoNrUz8hEU",
      "title": "Bringing agents onto the world wide web — Paul Klein IV, Browserbase",
      "author": "Paul Klein IV, Browserbase",
      "last_modified": "2026-08-14T15:00:31Z",
      "analysis_file": "analysis/GqoNrUz8hEU.json"
    },
    {
      "id": "gvIAkmZUEZY",
      "resource": "https://www.youtube.com/watch?v=gvIAkmZUEZY",
      "title": "Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code",
      "author": "Beyang Liu, Amp Code",
      "last_modified": "2025-12-22T17:00:06Z",
      "analysis_file": "analysis/gvIAkmZUEZY.json"
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

# Use tested source-aware codemods for repetitive repository-wide edits

## What

Use tested source-aware codemods for repetitive repository-wide edits

Encode a mechanical transformation once and apply it consistently across files rather than spending tokens and introducing drift through many hand-authored edits.

## Evidence

Source analysis [^Bdrs3uAX0_M]; no independently matched timestamped quote published.

Source analysis [^GqoNrUz8hEU]; no independently matched timestamped quote published.

Source analysis [^gvIAkmZUEZY]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Bdrs3uAX0_M]: [AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](https://www.youtube.com/watch?v=Bdrs3uAX0_M); publication: 2026-10-04T19:30:20Z; analysis: `analysis/Bdrs3uAX0_M.json`.
[^GqoNrUz8hEU]: [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](https://www.youtube.com/watch?v=GqoNrUz8hEU); publication: 2026-08-14T15:00:31Z; analysis: `analysis/GqoNrUz8hEU.json`.
[^gvIAkmZUEZY]: [Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code](https://www.youtube.com/watch?v=gvIAkmZUEZY); publication: 2025-12-22T17:00:06Z; analysis: `analysis/gvIAkmZUEZY.json`.
