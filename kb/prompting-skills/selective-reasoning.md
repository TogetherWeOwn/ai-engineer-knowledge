---
{
  "type": "technique",
  "id": "selective-reasoning",
  "title": "Use explicit reasoning checkpoints only where they improve the task",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-10-11T17:00:18Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2JX6JYyQG4Y",
      "resource": "https://www.youtube.com/watch?v=2JX6JYyQG4Y",
      "title": "Perception Agents — Antje Barth, Amazon AGI Lab",
      "author": "Antje Barth, Amazon AGI Lab",
      "last_modified": "2026-07-23T16:00:06Z",
      "analysis_file": "analysis/2JX6JYyQG4Y.json"
    },
    {
      "id": "3E7VAZaTG9M",
      "resource": "https://www.youtube.com/watch?v=3E7VAZaTG9M",
      "title": "Scaling AI in Education: A Khanmigo case study: Shawn Jansepar",
      "author": null,
      "last_modified": "2025-02-05T02:56:08Z",
      "analysis_file": "analysis/3E7VAZaTG9M.json"
    },
    {
      "id": "5eJqXtevlXg",
      "resource": "https://www.youtube.com/watch?v=5eJqXtevlXg",
      "title": "Hacking Subagents Into Codex CLI — Brian John, Betterup",
      "author": "Brian John, Betterup",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/5eJqXtevlXg.json"
    },
    {
      "id": "Bf71xMwd-Y0",
      "resource": "https://www.youtube.com/watch?v=Bf71xMwd-Y0",
      "title": "Buy Now, Maybe Pay Later: Dealing with Prompt-Tax While Staying at the Frontier - Andrew Thomspson",
      "author": "Andrew Thomspson",
      "last_modified": "2025-06-03T22:22:25Z",
      "analysis_file": "analysis/Bf71xMwd-Y0.json"
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
      "id": "K0X9QDRkIdg",
      "resource": "https://www.youtube.com/watch?v=K0X9QDRkIdg",
      "title": "Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic",
      "author": "Gagan Bhat & Isabella Kai He, Anthropic",
      "last_modified": "2026-08-11T16:00:06Z",
      "analysis_file": "analysis/K0X9QDRkIdg.json"
    },
    {
      "id": "QHBjufYK8TA",
      "resource": "https://www.youtube.com/watch?v=QHBjufYK8TA",
      "title": "The State of Model Routing — NVIDIA, Cognition, OpenRouter",
      "author": "NVIDIA, Cognition, OpenRouter",
      "last_modified": "2026-08-06T17:07:24Z",
      "analysis_file": "analysis/QHBjufYK8TA.json"
    },
    {
      "id": "QuuIywMG4s8",
      "resource": "https://www.youtube.com/watch?v=QuuIywMG4s8",
      "title": "Evals Are Broken, Use Them Anyway — Ara Khan, Cline",
      "author": "Ara Khan, Cline",
      "last_modified": "2026-06-06T16:00:00Z",
      "analysis_file": "analysis/QuuIywMG4s8.json"
    },
    {
      "id": "R7A8rX-09Zw",
      "resource": "https://www.youtube.com/watch?v=R7A8rX-09Zw",
      "title": "What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench",
      "author": "Peter Gostev, Arena.ai, BullshitBench",
      "last_modified": "2026-04-24T14:30:06Z",
      "analysis_file": "analysis/R7A8rX-09Zw.json"
    },
    {
      "id": "RFKCzGlAU6Q",
      "resource": "https://www.youtube.com/watch?v=RFKCzGlAU6Q",
      "title": "How Claude Code Works - Jared Zoneraich, PromptLayer",
      "author": "Jared Zoneraich, PromptLayer",
      "last_modified": "2025-12-26T22:04:34Z",
      "analysis_file": "analysis/RFKCzGlAU6Q.json"
    },
    {
      "id": "TyPpSRXGhbc",
      "resource": "https://www.youtube.com/watch?v=TyPpSRXGhbc",
      "title": "Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI",
      "author": "Charles Dickens, Snorkel AI",
      "last_modified": "2026-10-10T00:30:10Z",
      "analysis_file": "analysis/TyPpSRXGhbc.json"
    },
    {
      "id": "Ve-akpov78Q",
      "resource": "https://www.youtube.com/watch?v=Ve-akpov78Q",
      "title": "Code Generation and Maintenance at Scale: Morgante Pell",
      "author": null,
      "last_modified": "2024-10-17T18:52:20Z",
      "analysis_file": "analysis/Ve-akpov78Q.json"
    },
    {
      "id": "VrpEyglYgeU",
      "resource": "https://www.youtube.com/watch?v=VrpEyglYgeU",
      "title": "In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar",
      "author": "Tariq Shaukat, Sonar",
      "last_modified": "2026-07-20T15:00:06Z",
      "analysis_file": "analysis/VrpEyglYgeU.json"
    },
    {
      "id": "WRBNDpUhsJQ",
      "resource": "https://www.youtube.com/watch?v=WRBNDpUhsJQ",
      "title": "Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum",
      "author": "Adrian Bertagnoli, Callosum",
      "last_modified": "2026-05-24T14:00:06Z",
      "analysis_file": "analysis/WRBNDpUhsJQ.json"
    },
    {
      "id": "YIxzNZDDy1A",
      "resource": "https://www.youtube.com/watch?v=YIxzNZDDy1A",
      "title": "From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases",
      "author": "Wolfram Ravenwolf, Weights & Biases",
      "last_modified": "2026-10-11T17:00:18Z",
      "analysis_file": "analysis/YIxzNZDDy1A.json"
    },
    {
      "id": "YpY83-kA7Bo",
      "resource": "https://www.youtube.com/watch?v=YpY83-kA7Bo",
      "title": "2025 in LLMs so far, illustrated by Pelicans on Bicycles — Simon Willison",
      "author": "Simon Willison",
      "last_modified": "2025-07-09T16:00:06Z",
      "analysis_file": "analysis/YpY83-kA7Bo.json"
    },
    {
      "id": "_BRhRh7mOX0",
      "resource": "https://www.youtube.com/watch?v=_BRhRh7mOX0",
      "title": "Prompt Engineering and AI Red Teaming — Sander Schulhoff, HackAPrompt/LearnPrompting",
      "author": "Sander Schulhoff, HackAPrompt/LearnPrompting",
      "last_modified": "2025-07-14T19:00:11Z",
      "analysis_file": "analysis/_BRhRh7mOX0.json"
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
      "id": "il1c1a2FufU",
      "resource": "https://www.youtube.com/watch?v=il1c1a2FufU",
      "title": "Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex",
      "author": null,
      "last_modified": "2026-07-24T15:00:06Z",
      "analysis_file": "analysis/il1c1a2FufU.json"
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
      "id": "jQcsVk0KWiQ",
      "resource": "https://www.youtube.com/watch?v=jQcsVk0KWiQ",
      "title": "A Taxonomy for Next-gen Reasoning — Nathan Lambert, Allen Institute (AI2) & Interconnects.ai",
      "author": "Nathan Lambert, Allen Institute (AI2) & Interconnects.ai",
      "last_modified": "2025-07-19T21:15:55Z",
      "analysis_file": "analysis/jQcsVk0KWiQ.json"
    },
    {
      "id": "lY1iFbDPRlw",
      "resource": "https://www.youtube.com/watch?v=lY1iFbDPRlw",
      "title": "Minimax M2: Building the #1 Open Model – Olive Song, MiniMax",
      "author": "Olive Song, MiniMax",
      "last_modified": "2025-12-13T17:15:06Z",
      "analysis_file": "analysis/lY1iFbDPRlw.json"
    },
    {
      "id": "pPvoLjYj_mY",
      "resource": "https://www.youtube.com/watch?v=pPvoLjYj_mY",
      "title": "Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer",
      "author": "Waseem Alshikh, Writer",
      "last_modified": "2025-04-22T16:00:06Z",
      "analysis_file": "analysis/pPvoLjYj_mY.json"
    },
    {
      "id": "zM9RYqCcioM",
      "resource": "https://www.youtube.com/watch?v=zM9RYqCcioM",
      "title": "Finetuning: 500m AI agents in production with 2 engineers — Mustafa Ali & Kyle Corbitt",
      "author": "Mustafa Ali & Kyle Corbitt",
      "last_modified": "2025-04-12T16:00:06Z",
      "analysis_file": "analysis/zM9RYqCcioM.json"
    },
    {
      "id": "zTZ0qunQXnM",
      "resource": "https://www.youtube.com/watch?v=zTZ0qunQXnM",
      "title": "From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data",
      "author": "Rafael Levi, Bright Data",
      "last_modified": "2026-06-07T14:00:12Z",
      "analysis_file": "analysis/zTZ0qunQXnM.json"
    },
    {
      "id": "zrZ1amZBSPw",
      "resource": "https://www.youtube.com/watch?v=zrZ1amZBSPw",
      "title": "Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio",
      "author": "Kanish Manuja, Twilio",
      "last_modified": "2026-08-28T15:30:03Z",
      "analysis_file": "analysis/zrZ1amZBSPw.json"
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

# Use explicit reasoning checkpoints only where they improve the task

## What

Use explicit reasoning checkpoints only where they improve the task

More thinking can reduce success under a fixed timeout by leaving too few tool actions; inspect productive progress, not effort labels alone.

## Evidence

Source analysis [^2JX6JYyQG4Y]; no independently matched timestamped quote published.

Source analysis [^3E7VAZaTG9M]; no independently matched timestamped quote published.

Source analysis [^5eJqXtevlXg]; no independently matched timestamped quote published.

Source analysis [^Bf71xMwd-Y0]; no independently matched timestamped quote published.

Source analysis [^BqZrTdgBaPw]; no independently matched timestamped quote published.

> immediately and we can run container setup in parallel. What this means is
> — 23:39 [^K0X9QDRkIdg]

> of distribution small models may actually increase your cost because of
> — 15:18 [^QHBjufYK8TA]

> asking model to think more actually interferes with the quality of the
> — 15:09 [^QuuIywMG4s8]

Source analysis [^R7A8rX-09Zw]; no independently matched timestamped quote published.

> in a way that you're not just stuffing everything you're seeing in the terminal
> — 21:06 [^RFKCzGlAU6Q]

> thing about these is they move move it to a cheaper and faster model. So for
> — 15:05 [^RFKCzGlAU6Q]

> earlier. The bottleneck was never reasoning depth, it was just tool use,
> — 13:00 [^TyPpSRXGhbc]

> in a row we want to go back to a known good checkpoint uh and then build from
> — 14:06 [^Ve-akpov78Q]

Source analysis [^VrpEyglYgeU]; no independently matched timestamped quote published.

> because you don't need GPT to zoom for you.
> — 12:17 [^WRBNDpUhsJQ]

> thinks too much. It's overthinking. And that means I give it 1 hour. And if the
> — 46:03 [^YIxzNZDDy1A]

Source analysis [^YpY83-kA7Bo]; no independently matched timestamped quote published.

Source analysis [^_BRhRh7mOX0]; no independently matched timestamped quote published.

> going to explain you the whole run or just direct your attention into
> — 08:43 [^blrovBxxN9o]

Source analysis [^il1c1a2FufU]; no independently matched timestamped quote published.

Source analysis [^jNE8No-wvok]; no independently matched timestamped quote published.

Source analysis [^jQcsVk0KWiQ]; no independently matched timestamped quote published.

Source analysis [^lY1iFbDPRlw]; no independently matched timestamped quote published.

Source analysis [^pPvoLjYj_mY]; no independently matched timestamped quote published.

Source analysis [^zM9RYqCcioM]; no independently matched timestamped quote published.

Source analysis [^zTZ0qunQXnM]; no independently matched timestamped quote published.

> start with fixing the reasoning level per route. So with router models, they
> — 09:01 [^zrZ1amZBSPw]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2JX6JYyQG4Y]: [Perception Agents — Antje Barth, Amazon AGI Lab](https://www.youtube.com/watch?v=2JX6JYyQG4Y); publication: 2026-07-23T16:00:06Z; analysis: `analysis/2JX6JYyQG4Y.json`.
[^3E7VAZaTG9M]: [Scaling AI in Education: A Khanmigo case study: Shawn Jansepar](https://www.youtube.com/watch?v=3E7VAZaTG9M); publication: 2025-02-05T02:56:08Z; analysis: `analysis/3E7VAZaTG9M.json`.
[^5eJqXtevlXg]: [Hacking Subagents Into Codex CLI — Brian John, Betterup](https://www.youtube.com/watch?v=5eJqXtevlXg); publication: 2025-11-24T20:16:36Z; analysis: `analysis/5eJqXtevlXg.json`.
[^Bf71xMwd-Y0]: [Buy Now, Maybe Pay Later: Dealing with Prompt-Tax While Staying at the Frontier - Andrew Thomspson](https://www.youtube.com/watch?v=Bf71xMwd-Y0); publication: 2025-06-03T22:22:25Z; analysis: `analysis/Bf71xMwd-Y0.json`.
[^BqZrTdgBaPw]: [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](https://www.youtube.com/watch?v=BqZrTdgBaPw); publication: 2026-07-08T08:30:29Z; analysis: `analysis/BqZrTdgBaPw.json`.
[^K0X9QDRkIdg]: [Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic](https://www.youtube.com/watch?v=K0X9QDRkIdg); publication: 2026-08-11T16:00:06Z; analysis: `analysis/K0X9QDRkIdg.json`.
[^QHBjufYK8TA]: [The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA); publication: 2026-08-06T17:07:24Z; analysis: `analysis/QHBjufYK8TA.json`.
[^QuuIywMG4s8]: [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](https://www.youtube.com/watch?v=QuuIywMG4s8); publication: 2026-06-06T16:00:00Z; analysis: `analysis/QuuIywMG4s8.json`.
[^R7A8rX-09Zw]: [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](https://www.youtube.com/watch?v=R7A8rX-09Zw); publication: 2026-04-24T14:30:06Z; analysis: `analysis/R7A8rX-09Zw.json`.
[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^TyPpSRXGhbc]: [Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI](https://www.youtube.com/watch?v=TyPpSRXGhbc); publication: 2026-10-10T00:30:10Z; analysis: `analysis/TyPpSRXGhbc.json`.
[^Ve-akpov78Q]: [Code Generation and Maintenance at Scale: Morgante Pell](https://www.youtube.com/watch?v=Ve-akpov78Q); publication: 2024-10-17T18:52:20Z; analysis: `analysis/Ve-akpov78Q.json`.
[^VrpEyglYgeU]: [In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](https://www.youtube.com/watch?v=VrpEyglYgeU); publication: 2026-07-20T15:00:06Z; analysis: `analysis/VrpEyglYgeU.json`.
[^WRBNDpUhsJQ]: [Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum](https://www.youtube.com/watch?v=WRBNDpUhsJQ); publication: 2026-05-24T14:00:06Z; analysis: `analysis/WRBNDpUhsJQ.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^YpY83-kA7Bo]: [2025 in LLMs so far, illustrated by Pelicans on Bicycles — Simon Willison](https://www.youtube.com/watch?v=YpY83-kA7Bo); publication: 2025-07-09T16:00:06Z; analysis: `analysis/YpY83-kA7Bo.json`.
[^_BRhRh7mOX0]: [Prompt Engineering and AI Red Teaming — Sander Schulhoff, HackAPrompt/LearnPrompting](https://www.youtube.com/watch?v=_BRhRh7mOX0); publication: 2025-07-14T19:00:11Z; analysis: `analysis/_BRhRh7mOX0.json`.
[^blrovBxxN9o]: [Turning Fails into Features: Zapier’s Hard-Won Eval Lessons — Rafal Willinski, Vitor Balocco, Zapier](https://www.youtube.com/watch?v=blrovBxxN9o); publication: 2025-06-30T17:15:06Z; analysis: `analysis/blrovBxxN9o.json`.
[^il1c1a2FufU]: [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](https://www.youtube.com/watch?v=il1c1a2FufU); publication: 2026-07-24T15:00:06Z; analysis: `analysis/il1c1a2FufU.json`.
[^jNE8No-wvok]: [Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta](https://www.youtube.com/watch?v=jNE8No-wvok); publication: 2026-09-23T14:00:34Z; analysis: `analysis/jNE8No-wvok.json`.
[^jQcsVk0KWiQ]: [A Taxonomy for Next-gen Reasoning — Nathan Lambert, Allen Institute (AI2) & Interconnects.ai](https://www.youtube.com/watch?v=jQcsVk0KWiQ); publication: 2025-07-19T21:15:55Z; analysis: `analysis/jQcsVk0KWiQ.json`.
[^lY1iFbDPRlw]: [Minimax M2: Building the #1 Open Model – Olive Song, MiniMax](https://www.youtube.com/watch?v=lY1iFbDPRlw); publication: 2025-12-13T17:15:06Z; analysis: `analysis/lY1iFbDPRlw.json`.
[^pPvoLjYj_mY]: [Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer](https://www.youtube.com/watch?v=pPvoLjYj_mY); publication: 2025-04-22T16:00:06Z; analysis: `analysis/pPvoLjYj_mY.json`.
[^zM9RYqCcioM]: [Finetuning: 500m AI agents in production with 2 engineers — Mustafa Ali & Kyle Corbitt](https://www.youtube.com/watch?v=zM9RYqCcioM); publication: 2025-04-12T16:00:06Z; analysis: `analysis/zM9RYqCcioM.json`.
[^zTZ0qunQXnM]: [From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](https://www.youtube.com/watch?v=zTZ0qunQXnM); publication: 2026-06-07T14:00:12Z; analysis: `analysis/zTZ0qunQXnM.json`.
[^zrZ1amZBSPw]: [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](https://www.youtube.com/watch?v=zrZ1amZBSPw); publication: 2026-08-28T15:30:03Z; analysis: `analysis/zrZ1amZBSPw.json`.
