---
{
  "type": "technique",
  "id": "capability-evidence-routing",
  "title": "Use task- and harness-specific capability evidence as routing eligibility",
  "area": "model-routing-capacity",
  "status": "stable",
  "valid_from": "2026-10-19T14:06:53Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "C3geUfBR2js",
      "resource": "https://www.youtube.com/watch?v=C3geUfBR2js",
      "title": "Rise of the AI Architect — Clay Bavor, Cofounder, Sierra w/ Alessio Fanelli",
      "author": "Clay Bavor, Cofounder, Sierra w/ Alessio Fanelli",
      "last_modified": "2025-07-24T16:45:06Z",
      "analysis_file": "analysis/C3geUfBR2js.json"
    },
    {
      "id": "UGjk3Uk0MxM",
      "resource": "https://www.youtube.com/watch?v=UGjk3Uk0MxM",
      "title": "The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft",
      "author": "Pamela Fox, Microsoft",
      "last_modified": "2026-10-19T14:06:53Z",
      "analysis_file": "analysis/UGjk3Uk0MxM.json"
    },
    {
      "id": "W3khHzajE04",
      "resource": "https://www.youtube.com/watch?v=W3khHzajE04",
      "title": "Benchmarks Are Memes: How What We Measure Shapes AI—and Us - Alex Duffy, Every.to",
      "author": "Alex Duffy, Every.to",
      "last_modified": "2025-07-15T17:05:49Z",
      "analysis_file": "analysis/W3khHzajE04.json"
    },
    {
      "id": "WE_Gnowy3uw",
      "resource": "https://www.youtube.com/watch?v=WE_Gnowy3uw",
      "title": "Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor",
      "author": "David Gomes, Cursor",
      "last_modified": "2026-04-30T12:00:06Z",
      "analysis_file": "analysis/WE_Gnowy3uw.json"
    },
    {
      "id": "YZQsWVeN3rE",
      "resource": "https://www.youtube.com/watch?v=YZQsWVeN3rE",
      "title": "Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech",
      "author": "Alex Bauer, Upside.tech",
      "last_modified": "2026-07-11T00:57:36Z",
      "analysis_file": "analysis/YZQsWVeN3rE.json"
    },
    {
      "id": "oVsEddfhdxc",
      "resource": "https://www.youtube.com/watch?v=oVsEddfhdxc",
      "title": "We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect",
      "author": "Elie Bakouch, Prime Intellect",
      "last_modified": "2026-09-26T17:30:10Z",
      "analysis_file": "analysis/oVsEddfhdxc.json"
    },
    {
      "id": "y2W4FNAuPEA",
      "resource": "https://www.youtube.com/watch?v=y2W4FNAuPEA",
      "title": "Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher",
      "author": "Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher",
      "last_modified": "2026-09-08T15:00:06Z",
      "analysis_file": "analysis/y2W4FNAuPEA.json"
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

# Use task- and harness-specific capability evidence as routing eligibility

## What

Use task- and harness-specific capability evidence as routing eligibility

## Evidence

Source analysis [^C3geUfBR2js]; no independently matched timestamped quote published.

Source analysis [^UGjk3Uk0MxM]; no independently matched timestamped quote published.

Source analysis [^W3khHzajE04]; no independently matched timestamped quote published.

Source analysis [^WE_Gnowy3uw]; no independently matched timestamped quote published.

> So, this basically means friends don't let friends use really bad harnesses or
> — 15:31 [^YZQsWVeN3rE]

Source analysis [^oVsEddfhdxc]; no independently matched timestamped quote published.

Source analysis [^y2W4FNAuPEA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Use the cheapest evidenced capable mechanism
- **Speed:** Admit work within real quota and resource limits
- **Quality:** Preserve the role quality floor
- **Reliability:** Avoid exhaustion, unsafe fallback and policy bypass
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^C3geUfBR2js]: [Rise of the AI Architect — Clay Bavor, Cofounder, Sierra w/ Alessio Fanelli](https://www.youtube.com/watch?v=C3geUfBR2js); publication: 2025-07-24T16:45:06Z; analysis: `analysis/C3geUfBR2js.json`.
[^UGjk3Uk0MxM]: [The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft](https://www.youtube.com/watch?v=UGjk3Uk0MxM); publication: 2026-10-19T14:06:53Z; analysis: `analysis/UGjk3Uk0MxM.json`.
[^W3khHzajE04]: [Benchmarks Are Memes: How What We Measure Shapes AI—and Us - Alex Duffy, Every.to](https://www.youtube.com/watch?v=W3khHzajE04); publication: 2025-07-15T17:05:49Z; analysis: `analysis/W3khHzajE04.json`.
[^WE_Gnowy3uw]: [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](https://www.youtube.com/watch?v=WE_Gnowy3uw); publication: 2026-04-30T12:00:06Z; analysis: `analysis/WE_Gnowy3uw.json`.
[^YZQsWVeN3rE]: [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](https://www.youtube.com/watch?v=YZQsWVeN3rE); publication: 2026-07-11T00:57:36Z; analysis: `analysis/YZQsWVeN3rE.json`.
[^oVsEddfhdxc]: [We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect](https://www.youtube.com/watch?v=oVsEddfhdxc); publication: 2026-09-26T17:30:10Z; analysis: `analysis/oVsEddfhdxc.json`.
[^y2W4FNAuPEA]: [Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher](https://www.youtube.com/watch?v=y2W4FNAuPEA); publication: 2026-09-08T15:00:06Z; analysis: `analysis/y2W4FNAuPEA.json`.
