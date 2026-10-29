---
{
  "type": "technique",
  "id": "unknown-state-contracts",
  "title": "Represent unknown, missing and partial state distinctly from zero, false or success",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-11T12:30:23Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KhRjivBSwiw",
      "resource": "https://www.youtube.com/watch?v=KhRjivBSwiw",
      "title": "The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef",
      "author": "Yoni Michael & Brandon Callender, Typedef",
      "last_modified": "2026-10-11T12:30:23Z",
      "analysis_file": "analysis/KhRjivBSwiw.json"
    },
    {
      "id": "UNKDAo8YNmg",
      "resource": "https://www.youtube.com/watch?v=UNKDAo8YNmg",
      "title": "Pragmatic AI with TypeChat: Daniel Rosenwasser",
      "author": null,
      "last_modified": "2023-11-14T18:31:59Z",
      "analysis_file": "analysis/UNKDAo8YNmg.json"
    },
    {
      "id": "vJukHCIv7Ck",
      "resource": "https://www.youtube.com/watch?v=vJukHCIv7Ck",
      "title": "Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS",
      "author": "Elizabeth Fuentes, AWS",
      "last_modified": "2026-07-11T21:45:00Z",
      "analysis_file": "analysis/vJukHCIv7Ck.json"
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

# Represent unknown, missing and partial state distinctly from zero, false or success

## What

Represent unknown, missing and partial state distinctly from zero, false or success

Include an unknown-text or unhandled-intent branch in the schema, allowing correct partial extraction while preserving the parts the model could not map instead of forcing every phrase into a supported action.

## Evidence

> that we ingest and load the data. And if you make that modular, then you can
> — 1:27:11 [^KhRjivBSwiw]

> reason that it did is because we have this thing called unknown text so we've
> — 09:16 [^UNKDAo8YNmg]

> are currently no hotel listed in Antarctica. Of course, because it create
> — 27:36 [^vJukHCIv7Ck]

> results actually a valid response or is it a
> — 27:58 [^ynJyIKwjonM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KhRjivBSwiw]: [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](https://www.youtube.com/watch?v=KhRjivBSwiw); publication: 2026-10-11T12:30:23Z; analysis: `analysis/KhRjivBSwiw.json`.
[^UNKDAo8YNmg]: [Pragmatic AI with TypeChat: Daniel Rosenwasser](https://www.youtube.com/watch?v=UNKDAo8YNmg); publication: 2023-11-14T18:31:59Z; analysis: `analysis/UNKDAo8YNmg.json`.
[^vJukHCIv7Ck]: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](https://www.youtube.com/watch?v=vJukHCIv7Ck); publication: 2026-07-11T21:45:00Z; analysis: `analysis/vJukHCIv7Ck.json`.
[^ynJyIKwjonM]: [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](https://www.youtube.com/watch?v=ynJyIKwjonM); publication: 2026-05-08T13:00:06Z; analysis: `analysis/ynJyIKwjonM.json`.
