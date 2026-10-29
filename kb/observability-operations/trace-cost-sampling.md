---
{
  "type": "technique",
  "id": "trace-cost-sampling",
  "title": "Control tracing overhead with redaction, sampling and retention policy",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-10-05T22:00:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2p2ErKRELHM",
      "resource": "https://www.youtube.com/watch?v=2p2ErKRELHM",
      "title": "Voice Agent Engineering — Nik Caryotakis, SuperDial",
      "author": "Nik Caryotakis, SuperDial",
      "last_modified": "2025-04-18T16:00:06Z",
      "analysis_file": "analysis/2p2ErKRELHM.json"
    },
    {
      "id": "2wgPHvW0mG8",
      "resource": "https://www.youtube.com/watch?v=2wgPHvW0mG8",
      "title": "One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio",
      "author": "Suchet Bargoti, Skydio",
      "last_modified": "2026-09-24T15:00:35Z",
      "analysis_file": "analysis/2wgPHvW0mG8.json"
    },
    {
      "id": "4VhbYlfC7Gs",
      "resource": "https://www.youtube.com/watch?v=4VhbYlfC7Gs",
      "title": "Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw",
      "author": "Vincent Koc, OpenClaw",
      "last_modified": "2026-05-12T16:00:06Z",
      "analysis_file": "analysis/4VhbYlfC7Gs.json"
    },
    {
      "id": "BqZrTdgBaPw",
      "resource": "https://www.youtube.com/watch?v=BqZrTdgBaPw",
      "title": "Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG",
      "author": "Stephan Steinfurt, TNG",
      "last_modified": "2026-07-08T08:30:29Z",
      "analysis_file": "analysis/BqZrTdgBaPw.json"
    },
    {
      "id": "DrTdD-ttjCY",
      "resource": "https://www.youtube.com/watch?v=DrTdD-ttjCY",
      "title": "Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake",
      "author": "Sait Izmit, Snowflake",
      "last_modified": "2026-08-26T15:00:06Z",
      "analysis_file": "analysis/DrTdD-ttjCY.json"
    },
    {
      "id": "HOYLZ7IVgJo",
      "resource": "https://www.youtube.com/watch?v=HOYLZ7IVgJo",
      "title": "Shipping an Enterprise Voice AI Agent in 100 Days - Peter Bar, Intercom Fin",
      "author": "Peter Bar, Intercom Fin",
      "last_modified": "2025-07-18T16:00:06Z",
      "analysis_file": "analysis/HOYLZ7IVgJo.json"
    },
    {
      "id": "IIL2tE4n1Q0",
      "resource": "https://www.youtube.com/watch?v=IIL2tE4n1Q0",
      "title": "Judging LLMs: Alex Volkov",
      "author": null,
      "last_modified": "2024-09-09T18:39:17Z",
      "analysis_file": "analysis/IIL2tE4n1Q0.json"
    },
    {
      "id": "ITMXwI6QL6A",
      "resource": "https://www.youtube.com/watch?v=ITMXwI6QL6A",
      "title": "How Forward Deployed Engineering is done at Ramp — Leo Mehr",
      "author": "Leo Mehr",
      "last_modified": "2026-07-28T19:00:06Z",
      "analysis_file": "analysis/ITMXwI6QL6A.json"
    },
    {
      "id": "PjaVHm_3Ljg",
      "resource": "https://www.youtube.com/watch?v=PjaVHm_3Ljg",
      "title": "Transforming search and discovery using LLMs — Tejaswi & Vinesh, Instacart",
      "author": "Tejaswi & Vinesh, Instacart",
      "last_modified": "2025-07-16T18:01:03Z",
      "analysis_file": "analysis/PjaVHm_3Ljg.json"
    },
    {
      "id": "RVN9HWKmkNU",
      "resource": "https://www.youtube.com/watch?v=RVN9HWKmkNU",
      "title": "Will Agent evaluation via MCP Stabilize Agent Networks? - Ari Heljakka",
      "author": "Ari Heljakka",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/RVN9HWKmkNU.json"
    },
    {
      "id": "VXfRt_H-V08",
      "resource": "https://www.youtube.com/watch?v=VXfRt_H-V08",
      "title": "One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca",
      "author": "Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca",
      "last_modified": "2026-04-10T11:30:06Z",
      "analysis_file": "analysis/VXfRt_H-V08.json"
    },
    {
      "id": "XBaznoTRDFI",
      "resource": "https://www.youtube.com/watch?v=XBaznoTRDFI",
      "title": "How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust",
      "author": "Phil Hetzel, Braintrust",
      "last_modified": "2026-05-28T23:00:06Z",
      "analysis_file": "analysis/XBaznoTRDFI.json"
    },
    {
      "id": "YXEqC05WEI0",
      "resource": "https://www.youtube.com/watch?v=YXEqC05WEI0",
      "title": "Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health",
      "author": "Rashi Agrawal, Hinge Health",
      "last_modified": "2026-08-19T14:30:18Z",
      "analysis_file": "analysis/YXEqC05WEI0.json"
    },
    {
      "id": "ZIYYsAzaLlA",
      "resource": "https://www.youtube.com/watch?v=ZIYYsAzaLlA",
      "title": "Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma",
      "author": "Jesse Lumarie, Figma",
      "last_modified": "2026-08-28T14:00:06Z",
      "analysis_file": "analysis/ZIYYsAzaLlA.json"
    },
    {
      "id": "ZdheJTfLu-s",
      "resource": "https://www.youtube.com/watch?v=ZdheJTfLu-s",
      "title": "Shipping complex AI applications — Braintrust & Trainline",
      "author": "Braintrust & Trainline",
      "last_modified": "2026-05-01T14:00:06Z",
      "analysis_file": "analysis/ZdheJTfLu-s.json"
    },
    {
      "id": "_zl_zimMRak",
      "resource": "https://www.youtube.com/watch?v=_zl_zimMRak",
      "title": "How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit",
      "author": "Jaspreet Singh, Intuit",
      "last_modified": "2025-07-23T15:51:31Z",
      "analysis_file": "analysis/_zl_zimMRak.json"
    },
    {
      "id": "jNE8No-wvok",
      "resource": "https://www.youtube.com/watch?v=jNE8No-wvok",
      "title": "Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta",
      "author": "Aditya Gautam, Meta",
      "last_modified": "2026-09-23T14:00:34Z",
      "analysis_file": "analysis/jNE8No-wvok.json"
    },
    {
      "id": "jxrGodnopHo",
      "resource": "https://www.youtube.com/watch?v=jxrGodnopHo",
      "title": "[Full Workshop] Building Metrics that actually work — David Karam, Pi Labs (fmr Google Search)",
      "author": "David Karam, Pi Labs (fmr Google Search)",
      "last_modified": "2025-07-29T00:29:21Z",
      "analysis_file": "analysis/jxrGodnopHo.json"
    },
    {
      "id": "pzmbleiOfCM",
      "resource": "https://www.youtube.com/watch?v=pzmbleiOfCM",
      "title": "Voice Agents: the good, the bad, and the ugly",
      "author": null,
      "last_modified": "2025-02-22T20:00:06Z",
      "analysis_file": "analysis/pzmbleiOfCM.json"
    },
    {
      "id": "qZj7sqmidqA",
      "resource": "https://www.youtube.com/watch?v=qZj7sqmidqA",
      "title": "From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-05T22:00:36Z",
      "analysis_file": "analysis/qZj7sqmidqA.json"
    },
    {
      "id": "rTojoVotlD8",
      "resource": "https://www.youtube.com/watch?v=rTojoVotlD8",
      "title": "Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog",
      "author": "Marina Petzel, Datadog",
      "last_modified": "2026-10-03T01:30:33Z",
      "analysis_file": "analysis/rTojoVotlD8.json"
    },
    {
      "id": "vh2VGuQ3zhY",
      "resource": "https://www.youtube.com/watch?v=vh2VGuQ3zhY",
      "title": "The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica",
      "author": "Sohail Shaikh & Ankush Rastogi, Prosodica",
      "last_modified": "2026-06-28T15:15:15Z",
      "analysis_file": "analysis/vh2VGuQ3zhY.json"
    },
    {
      "id": "wflNENRSUb4",
      "resource": "https://www.youtube.com/watch?v=wflNENRSUb4",
      "title": "Give Your Agent a Computer — Nico Albanese, Vercel",
      "author": "Nico Albanese, Vercel",
      "last_modified": "2026-05-12T18:00:06Z",
      "analysis_file": "analysis/wflNENRSUb4.json"
    },
    {
      "id": "xJXm4Wcw4m8",
      "resource": "https://www.youtube.com/watch?v=xJXm4Wcw4m8",
      "title": "Taming Rogue AI Agents with Observability-Driven Evaluation — Jim Bennett, Galileo",
      "author": "Jim Bennett, Galileo",
      "last_modified": "2025-06-27T10:27:15Z",
      "analysis_file": "analysis/xJXm4Wcw4m8.json"
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

# Control tracing overhead with redaction, sampling and retention policy

## What

Control tracing overhead with redaction, sampling and retention policy

Reserve expensive semantic assessment for selected traces while broad low-cost checks cover the full stream.

## Evidence

Source analysis [^2p2ErKRELHM]; no independently matched timestamped quote published.

Source analysis [^2wgPHvW0mG8]; no independently matched timestamped quote published.

Source analysis [^4VhbYlfC7Gs]; no independently matched timestamped quote published.

Source analysis [^BqZrTdgBaPw]; no independently matched timestamped quote published.

Source analysis [^DrTdD-ttjCY]; no independently matched timestamped quote published.

Source analysis [^HOYLZ7IVgJo]; no independently matched timestamped quote published.

Source analysis [^IIL2tE4n1Q0]; no independently matched timestamped quote published.

Source analysis [^ITMXwI6QL6A]; no independently matched timestamped quote published.

Source analysis [^PjaVHm_3Ljg]; no independently matched timestamped quote published.

Source analysis [^RVN9HWKmkNU]; no independently matched timestamped quote published.

Source analysis [^VXfRt_H-V08]; no independently matched timestamped quote published.

Source analysis [^XBaznoTRDFI]; no independently matched timestamped quote published.

Source analysis [^YXEqC05WEI0]; no independently matched timestamped quote published.

> we have a um, eval that sort of runs like hundreds of times a week. Engineers
> — 06:45 [^ZIYYsAzaLlA]

Source analysis [^ZdheJTfLu-s]; no independently matched timestamped quote published.

Source analysis [^_zl_zimMRak]; no independently matched timestamped quote published.

Source analysis [^jNE8No-wvok]; no independently matched timestamped quote published.

> purposes. uh the best thing is to to sample from your logs some number of
> — 31:47 [^jxrGodnopHo]

Source analysis [^pzmbleiOfCM]; no independently matched timestamped quote published.

> production uh scale those costs can add up. So you sample 10% of your traffic or
> — 1:43:52 [^qZj7sqmidqA]

Source analysis [^rTojoVotlD8]; no independently matched timestamped quote published.

Source analysis [^vh2VGuQ3zhY]; no independently matched timestamped quote published.

> when you do persist at the very end, you know that you're getting like the full
> — 44:46 [^wflNENRSUb4]

> 10,000 of them use an expensive LLM to prove that it works. Ideally, you want
> — 08:42 [^xJXm4Wcw4m8]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2p2ErKRELHM]: [Voice Agent Engineering — Nik Caryotakis, SuperDial](https://www.youtube.com/watch?v=2p2ErKRELHM); publication: 2025-04-18T16:00:06Z; analysis: `analysis/2p2ErKRELHM.json`.
[^2wgPHvW0mG8]: [One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio](https://www.youtube.com/watch?v=2wgPHvW0mG8); publication: 2026-09-24T15:00:35Z; analysis: `analysis/2wgPHvW0mG8.json`.
[^4VhbYlfC7Gs]: [Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=4VhbYlfC7Gs); publication: 2026-05-12T16:00:06Z; analysis: `analysis/4VhbYlfC7Gs.json`.
[^BqZrTdgBaPw]: [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](https://www.youtube.com/watch?v=BqZrTdgBaPw); publication: 2026-07-08T08:30:29Z; analysis: `analysis/BqZrTdgBaPw.json`.
[^DrTdD-ttjCY]: [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](https://www.youtube.com/watch?v=DrTdD-ttjCY); publication: 2026-08-26T15:00:06Z; analysis: `analysis/DrTdD-ttjCY.json`.
[^HOYLZ7IVgJo]: [Shipping an Enterprise Voice AI Agent in 100 Days - Peter Bar, Intercom Fin](https://www.youtube.com/watch?v=HOYLZ7IVgJo); publication: 2025-07-18T16:00:06Z; analysis: `analysis/HOYLZ7IVgJo.json`.
[^IIL2tE4n1Q0]: [Judging LLMs: Alex Volkov](https://www.youtube.com/watch?v=IIL2tE4n1Q0); publication: 2024-09-09T18:39:17Z; analysis: `analysis/IIL2tE4n1Q0.json`.
[^ITMXwI6QL6A]: [How Forward Deployed Engineering is done at Ramp — Leo Mehr](https://www.youtube.com/watch?v=ITMXwI6QL6A); publication: 2026-07-28T19:00:06Z; analysis: `analysis/ITMXwI6QL6A.json`.
[^PjaVHm_3Ljg]: [Transforming search and discovery using LLMs — Tejaswi & Vinesh, Instacart](https://www.youtube.com/watch?v=PjaVHm_3Ljg); publication: 2025-07-16T18:01:03Z; analysis: `analysis/PjaVHm_3Ljg.json`.
[^RVN9HWKmkNU]: [Will Agent evaluation via MCP Stabilize Agent Networks? - Ari Heljakka](https://www.youtube.com/watch?v=RVN9HWKmkNU); publication: 2025-06-03T22:22:28Z; analysis: `analysis/RVN9HWKmkNU.json`.
[^VXfRt_H-V08]: [One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca](https://www.youtube.com/watch?v=VXfRt_H-V08); publication: 2026-04-10T11:30:06Z; analysis: `analysis/VXfRt_H-V08.json`.
[^XBaznoTRDFI]: [How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust](https://www.youtube.com/watch?v=XBaznoTRDFI); publication: 2026-05-28T23:00:06Z; analysis: `analysis/XBaznoTRDFI.json`.
[^YXEqC05WEI0]: [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](https://www.youtube.com/watch?v=YXEqC05WEI0); publication: 2026-08-19T14:30:18Z; analysis: `analysis/YXEqC05WEI0.json`.
[^ZIYYsAzaLlA]: [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](https://www.youtube.com/watch?v=ZIYYsAzaLlA); publication: 2026-08-28T14:00:06Z; analysis: `analysis/ZIYYsAzaLlA.json`.
[^ZdheJTfLu-s]: [Shipping complex AI applications — Braintrust & Trainline](https://www.youtube.com/watch?v=ZdheJTfLu-s); publication: 2026-05-01T14:00:06Z; analysis: `analysis/ZdheJTfLu-s.json`.
[^_zl_zimMRak]: [How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit](https://www.youtube.com/watch?v=_zl_zimMRak); publication: 2025-07-23T15:51:31Z; analysis: `analysis/_zl_zimMRak.json`.
[^jNE8No-wvok]: [Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta](https://www.youtube.com/watch?v=jNE8No-wvok); publication: 2026-09-23T14:00:34Z; analysis: `analysis/jNE8No-wvok.json`.
[^jxrGodnopHo]: [[Full Workshop] Building Metrics that actually work — David Karam, Pi Labs (fmr Google Search)](https://www.youtube.com/watch?v=jxrGodnopHo); publication: 2025-07-29T00:29:21Z; analysis: `analysis/jxrGodnopHo.json`.
[^pzmbleiOfCM]: [Voice Agents: the good, the bad, and the ugly](https://www.youtube.com/watch?v=pzmbleiOfCM); publication: 2025-02-22T20:00:06Z; analysis: `analysis/pzmbleiOfCM.json`.
[^qZj7sqmidqA]: [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=qZj7sqmidqA); publication: 2026-10-05T22:00:36Z; analysis: `analysis/qZj7sqmidqA.json`.
[^rTojoVotlD8]: [Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog](https://www.youtube.com/watch?v=rTojoVotlD8); publication: 2026-10-03T01:30:33Z; analysis: `analysis/rTojoVotlD8.json`.
[^vh2VGuQ3zhY]: [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](https://www.youtube.com/watch?v=vh2VGuQ3zhY); publication: 2026-06-28T15:15:15Z; analysis: `analysis/vh2VGuQ3zhY.json`.
[^wflNENRSUb4]: [Give Your Agent a Computer — Nico Albanese, Vercel](https://www.youtube.com/watch?v=wflNENRSUb4); publication: 2026-05-12T18:00:06Z; analysis: `analysis/wflNENRSUb4.json`.
[^xJXm4Wcw4m8]: [Taming Rogue AI Agents with Observability-Driven Evaluation — Jim Bennett, Galileo](https://www.youtube.com/watch?v=xJXm4Wcw4m8); publication: 2025-06-27T10:27:15Z; analysis: `analysis/xJXm4Wcw4m8.json`.
