---
{
  "type": "technique",
  "id": "error-taxonomy",
  "title": "Distinguish environment, transport, policy and reasoning failures before recovery",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-20T09:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Bz1HFxQA1o8",
      "resource": "https://www.youtube.com/watch?v=Bz1HFxQA1o8",
      "title": "Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco",
      "author": "Al Chen, Cisco",
      "last_modified": "2026-10-20T09:00:06Z",
      "analysis_file": "analysis/Bz1HFxQA1o8.json"
    },
    {
      "id": "Djv8Sp11UjI",
      "resource": "https://www.youtube.com/watch?v=Djv8Sp11UjI",
      "title": "The Current State of Browser Agents - Jerry Wu and Wyatt Marshall",
      "author": "Jerry Wu and Wyatt Marshall",
      "last_modified": "2025-06-03T22:22:26Z",
      "analysis_file": "analysis/Djv8Sp11UjI.json"
    },
    {
      "id": "I8fs4omN1no",
      "resource": "https://www.youtube.com/watch?v=I8fs4omN1no",
      "title": "Hard Won Lessons from Building Effective AI Coding Agents – Nik Pash, Cline",
      "author": "Nik Pash, Cline",
      "last_modified": "2025-12-12T15:00:06Z",
      "analysis_file": "analysis/I8fs4omN1no.json"
    },
    {
      "id": "KA5kPbdkK2E",
      "resource": "https://www.youtube.com/watch?v=KA5kPbdkK2E",
      "title": "How Lovable self-improves every hour — Benjamin Verbeek, Lovable",
      "author": "Benjamin Verbeek, Lovable",
      "last_modified": "2026-06-02T16:00:33Z",
      "analysis_file": "analysis/KA5kPbdkK2E.json"
    },
    {
      "id": "LqLoYksJ6do",
      "resource": "https://www.youtube.com/watch?v=LqLoYksJ6do",
      "title": "We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3",
      "author": "Moritz Johner, Form3",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/LqLoYksJ6do.json"
    },
    {
      "id": "NdrSPm6NCdk",
      "resource": "https://www.youtube.com/watch?v=NdrSPm6NCdk",
      "title": "Evals in AI: A Deep Dive — Tejas Kumar, IBM",
      "author": "Tejas Kumar, IBM",
      "last_modified": "2026-10-05T17:00:22Z",
      "analysis_file": "analysis/NdrSPm6NCdk.json"
    },
    {
      "id": "SHMCGrNJJGc",
      "resource": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
      "title": "How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-17T19:00:23Z",
      "analysis_file": "analysis/SHMCGrNJJGc.json"
    },
    {
      "id": "TNwJ1LMiENk",
      "resource": "https://www.youtube.com/watch?v=TNwJ1LMiENk",
      "title": "Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel",
      "author": "Kobie Crawford, Snorkel",
      "last_modified": "2026-06-10T17:00:25Z",
      "analysis_file": "analysis/TNwJ1LMiENk.json"
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
      "id": "WJRdLNhrsLQ",
      "resource": "https://www.youtube.com/watch?v=WJRdLNhrsLQ",
      "title": "How to build an AI-Native Health Company — Dan Feng, Maven Clinic",
      "author": "Dan Feng, Maven Clinic",
      "last_modified": "2026-08-19T17:30:19Z",
      "analysis_file": "analysis/WJRdLNhrsLQ.json"
    },
    {
      "id": "XzJD1bvXKjs",
      "resource": "https://www.youtube.com/watch?v=XzJD1bvXKjs",
      "title": "How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-09-09T15:00:06Z",
      "analysis_file": "analysis/XzJD1bvXKjs.json"
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
      "id": "_zUp6y9bDU8",
      "resource": "https://www.youtube.com/watch?v=_zUp6y9bDU8",
      "title": "Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI",
      "author": "Ankur Duggal, Arize AI",
      "last_modified": "2026-10-11T18:30:14Z",
      "analysis_file": "analysis/_zUp6y9bDU8.json"
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
      "id": "byn9PURoBNY",
      "resource": "https://www.youtube.com/watch?v=byn9PURoBNY",
      "title": "Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai",
      "author": "Gabriel Jorge Menezes, Krea.ai",
      "last_modified": "2026-08-18T17:00:05Z",
      "analysis_file": "analysis/byn9PURoBNY.json"
    },
    {
      "id": "k72eLcYpVys",
      "resource": "https://www.youtube.com/watch?v=k72eLcYpVys",
      "title": "1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS",
      "author": "Kevin Orellana, AWS",
      "last_modified": "2026-10-12T05:36:31Z",
      "analysis_file": "analysis/k72eLcYpVys.json"
    },
    {
      "id": "khVX_BUnEwU",
      "resource": "https://www.youtube.com/watch?v=khVX_BUnEwU",
      "title": "Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital",
      "author": "Yohei Nakajima, Untapped Capital",
      "last_modified": "2026-07-22T20:00:06Z",
      "analysis_file": "analysis/khVX_BUnEwU.json"
    },
    {
      "id": "nxokqOq1imY",
      "resource": "https://www.youtube.com/watch?v=nxokqOq1imY",
      "title": "Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust",
      "author": "Ameya Bhatawdekar, Braintrust",
      "last_modified": "2026-08-20T13:00:06Z",
      "analysis_file": "analysis/nxokqOq1imY.json"
    },
    {
      "id": "tZycGA_Fbfo",
      "resource": "https://www.youtube.com/watch?v=tZycGA_Fbfo",
      "title": "Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma",
      "author": "Harish Gaggar, Credit Karma",
      "last_modified": "2026-10-14T17:00:04Z",
      "analysis_file": "analysis/tZycGA_Fbfo.json"
    },
    {
      "id": "wHhlvcQgi9M",
      "resource": "https://www.youtube.com/watch?v=wHhlvcQgi9M",
      "title": "7 Habits of Highly Effective Generative AI Evaluations - Justin Muller",
      "author": "Justin Muller",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/wHhlvcQgi9M.json"
    },
    {
      "id": "wcUJWP6WpGM",
      "resource": "https://www.youtube.com/watch?v=wcUJWP6WpGM",
      "title": "SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius",
      "author": "Ibragim Badertdinov, Nebius",
      "last_modified": "2026-06-04T14:00:06Z",
      "analysis_file": "analysis/wcUJWP6WpGM.json"
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

# Distinguish environment, transport, policy and reasoning failures before recovery

## What

Distinguish environment, transport, policy and reasoning failures before recovery

Classifying the failing layer prevents a corrupt tool wrapper from being misdiagnosed as a model or VM failure.

## Evidence

Source analysis [^Bz1HFxQA1o8]; no independently matched timestamped quote published.

Source analysis [^Djv8Sp11UjI]; no independently matched timestamped quote published.

Source analysis [^I8fs4omN1no]; no independently matched timestamped quote published.

> solvable even if you say all the right things. Maybe we're just not supporting
> — 06:18 [^KA5kPbdkK2E]

Source analysis [^LqLoYksJ6do]; no independently matched timestamped quote published.

> lowerase this. A lot of this was just case sensitive, right? So, we'll
> — 40:16 [^NdrSPm6NCdk]

Source analysis [^SHMCGrNJJGc]; no independently matched timestamped quote published.

Source analysis [^TNwJ1LMiENk]; no independently matched timestamped quote published.

Source analysis [^WE_Gnowy3uw]; no independently matched timestamped quote published.

Source analysis [^WJRdLNhrsLQ]; no independently matched timestamped quote published.

> instructions no longer has one failure mode. It has four different ways that it
> — 14:12 [^XzJD1bvXKjs]

> causes a crash on its own by doing something stupid, that is actually a
> — 23:44 [^YIxzNZDDy1A]

Source analysis [^_zUp6y9bDU8]; no independently matched timestamped quote published.

> six-second generation that drifted and and regenerated that regenerate that
> — 06:47 [^b_PmGocP4rc]

Source analysis [^byn9PURoBNY]; no independently matched timestamped quote published.

> layers. One was at the interface and the other one was at the sandbox layer. And
> — 06:16 [^k72eLcYpVys]

> based on the failure it classified it was a it was allowed to edit a specific
> — 11:28 [^khVX_BUnEwU]

> new categories of failures that you had not anticipated. So your system is now
> — 21:08 [^nxokqOq1imY]

> latencies for a given tool, right? Whether my auth
> — 13:38 [^tZycGA_Fbfo]

Source analysis [^wHhlvcQgi9M]; no independently matched timestamped quote published.

Source analysis [^wcUJWP6WpGM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Bz1HFxQA1o8]: [Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco](https://www.youtube.com/watch?v=Bz1HFxQA1o8); publication: 2026-10-20T09:00:06Z; analysis: `analysis/Bz1HFxQA1o8.json`.
[^Djv8Sp11UjI]: [The Current State of Browser Agents - Jerry Wu and Wyatt Marshall](https://www.youtube.com/watch?v=Djv8Sp11UjI); publication: 2025-06-03T22:22:26Z; analysis: `analysis/Djv8Sp11UjI.json`.
[^I8fs4omN1no]: [Hard Won Lessons from Building Effective AI Coding Agents – Nik Pash, Cline](https://www.youtube.com/watch?v=I8fs4omN1no); publication: 2025-12-12T15:00:06Z; analysis: `analysis/I8fs4omN1no.json`.
[^KA5kPbdkK2E]: [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](https://www.youtube.com/watch?v=KA5kPbdkK2E); publication: 2026-06-02T16:00:33Z; analysis: `analysis/KA5kPbdkK2E.json`.
[^LqLoYksJ6do]: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](https://www.youtube.com/watch?v=LqLoYksJ6do); publication: 2026-07-20T17:17:53Z; analysis: `analysis/LqLoYksJ6do.json`.
[^NdrSPm6NCdk]: [Evals in AI: A Deep Dive — Tejas Kumar, IBM](https://www.youtube.com/watch?v=NdrSPm6NCdk); publication: 2026-10-05T17:00:22Z; analysis: `analysis/NdrSPm6NCdk.json`.
[^SHMCGrNJJGc]: [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=SHMCGrNJJGc); publication: 2026-10-17T19:00:23Z; analysis: `analysis/SHMCGrNJJGc.json`.
[^TNwJ1LMiENk]: [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](https://www.youtube.com/watch?v=TNwJ1LMiENk); publication: 2026-06-10T17:00:25Z; analysis: `analysis/TNwJ1LMiENk.json`.
[^WE_Gnowy3uw]: [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](https://www.youtube.com/watch?v=WE_Gnowy3uw); publication: 2026-04-30T12:00:06Z; analysis: `analysis/WE_Gnowy3uw.json`.
[^WJRdLNhrsLQ]: [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](https://www.youtube.com/watch?v=WJRdLNhrsLQ); publication: 2026-08-19T17:30:19Z; analysis: `analysis/WJRdLNhrsLQ.json`.
[^XzJD1bvXKjs]: [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=XzJD1bvXKjs); publication: 2026-09-09T15:00:06Z; analysis: `analysis/XzJD1bvXKjs.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^_zUp6y9bDU8]: [Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI](https://www.youtube.com/watch?v=_zUp6y9bDU8); publication: 2026-10-11T18:30:14Z; analysis: `analysis/_zUp6y9bDU8.json`.
[^b_PmGocP4rc]: [Evaling Video Slop — Maor Bril, Character.ai](https://www.youtube.com/watch?v=b_PmGocP4rc); publication: 2026-07-25T00:00:02Z; analysis: `analysis/b_PmGocP4rc.json`.
[^byn9PURoBNY]: [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](https://www.youtube.com/watch?v=byn9PURoBNY); publication: 2026-08-18T17:00:05Z; analysis: `analysis/byn9PURoBNY.json`.
[^k72eLcYpVys]: [1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS](https://www.youtube.com/watch?v=k72eLcYpVys); publication: 2026-10-12T05:36:31Z; analysis: `analysis/k72eLcYpVys.json`.
[^khVX_BUnEwU]: [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](https://www.youtube.com/watch?v=khVX_BUnEwU); publication: 2026-07-22T20:00:06Z; analysis: `analysis/khVX_BUnEwU.json`.
[^nxokqOq1imY]: [Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust](https://www.youtube.com/watch?v=nxokqOq1imY); publication: 2026-08-20T13:00:06Z; analysis: `analysis/nxokqOq1imY.json`.
[^tZycGA_Fbfo]: [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](https://www.youtube.com/watch?v=tZycGA_Fbfo); publication: 2026-10-14T17:00:04Z; analysis: `analysis/tZycGA_Fbfo.json`.
[^wHhlvcQgi9M]: [7 Habits of Highly Effective Generative AI Evaluations - Justin Muller](https://www.youtube.com/watch?v=wHhlvcQgi9M); publication: 2025-06-03T22:22:29Z; analysis: `analysis/wHhlvcQgi9M.json`.
[^wcUJWP6WpGM]: [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](https://www.youtube.com/watch?v=wcUJWP6WpGM); publication: 2026-06-04T14:00:06Z; analysis: `analysis/wcUJWP6WpGM.json`.
