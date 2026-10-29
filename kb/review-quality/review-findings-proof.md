---
{
  "type": "technique",
  "id": "review-findings-proof",
  "title": "Require a concrete failure scenario and verify each review finding",
  "area": "review-quality",
  "status": "stable",
  "valid_from": "2026-10-20T09:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "0ML7ZLMdcl4",
      "resource": "https://www.youtube.com/watch?v=0ML7ZLMdcl4",
      "title": "AI Engineering at Jane Street - John Crepezzi",
      "author": "John Crepezzi",
      "last_modified": "2025-03-28T15:04:44Z",
      "analysis_file": "analysis/0ML7ZLMdcl4.json"
    },
    {
      "id": "0tVu-V3_fFw",
      "resource": "https://www.youtube.com/watch?v=0tVu-V3_fFw",
      "title": "Designing AI To Scale Human Thought — Jun Yu Tan, Tusk",
      "author": "Jun Yu Tan, Tusk",
      "last_modified": "2025-06-03T07:00:06Z",
      "analysis_file": "analysis/0tVu-V3_fFw.json"
    },
    {
      "id": "Bz1HFxQA1o8",
      "resource": "https://www.youtube.com/watch?v=Bz1HFxQA1o8",
      "title": "Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco",
      "author": "Al Chen, Cisco",
      "last_modified": "2026-10-20T09:00:06Z",
      "analysis_file": "analysis/Bz1HFxQA1o8.json"
    },
    {
      "id": "JJGbw4ggaFs",
      "resource": "https://www.youtube.com/watch?v=JJGbw4ggaFs",
      "title": "From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud",
      "author": "May Walter, Hud",
      "last_modified": "2026-07-19T13:45:06Z",
      "analysis_file": "analysis/JJGbw4ggaFs.json"
    },
    {
      "id": "McknwOzbmyg",
      "resource": "https://www.youtube.com/watch?v=McknwOzbmyg",
      "title": "Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia",
      "author": "Jared Joselowitz, Ufonia",
      "last_modified": "2026-08-19T15:00:31Z",
      "analysis_file": "analysis/McknwOzbmyg.json"
    },
    {
      "id": "OMGPvW8TBHc",
      "resource": "https://www.youtube.com/watch?v=OMGPvW8TBHc",
      "title": "Fuzzing in the GenAI Era — Leonard Tang, Haize Labs",
      "author": "Leonard Tang, Haize Labs",
      "last_modified": "2025-08-22T15:00:05Z",
      "analysis_file": "analysis/OMGPvW8TBHc.json"
    },
    {
      "id": "ON5LIT0M4do",
      "resource": "https://www.youtube.com/watch?v=ON5LIT0M4do",
      "title": "Feedback Loops are All You Need — Mehedi Hassan, Granola",
      "author": "Mehedi Hassan, Granola",
      "last_modified": "2026-05-10T18:00:06Z",
      "analysis_file": "analysis/ON5LIT0M4do.json"
    },
    {
      "id": "Q5IVm_CxN2w",
      "resource": "https://www.youtube.com/watch?v=Q5IVm_CxN2w",
      "title": "Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway",
      "author": "Mahmoud Abdelwahab, Railway",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/Q5IVm_CxN2w.json"
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
      "id": "YgEv7IQzGdM",
      "resource": "https://www.youtube.com/watch?v=YgEv7IQzGdM",
      "title": "How to Kill the Code Review — Ankit Jain, Aviator",
      "author": "Ankit Jain, Aviator",
      "last_modified": "2026-08-17T20:00:08Z",
      "analysis_file": "analysis/YgEv7IQzGdM.json"
    },
    {
      "id": "ZGzthw4BZiA",
      "resource": "https://www.youtube.com/watch?v=ZGzthw4BZiA",
      "title": "Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab",
      "author": "Emile Baizel & Shruti Arora, Amazon AGI Lab",
      "last_modified": "2026-10-11T20:00:38Z",
      "analysis_file": "analysis/ZGzthw4BZiA.json"
    },
    {
      "id": "_mi3alkqy4s",
      "resource": "https://www.youtube.com/watch?v=_mi3alkqy4s",
      "title": "The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-09-30T13:30:35Z",
      "analysis_file": "analysis/_mi3alkqy4s.json"
    },
    {
      "id": "bSG9wUYaHWU",
      "resource": "https://www.youtube.com/watch?v=bSG9wUYaHWU",
      "title": "Context Is the New Code — Patrick Debois, Tessl",
      "author": "Patrick Debois, Tessl",
      "last_modified": "2026-05-03T14:00:06Z",
      "analysis_file": "analysis/bSG9wUYaHWU.json"
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
      "id": "c35YoMdnI78",
      "resource": "https://www.youtube.com/watch?v=c35YoMdnI78",
      "title": "The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "author": "Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "last_modified": "2026-07-17T21:00:06Z",
      "analysis_file": "analysis/c35YoMdnI78.json"
    },
    {
      "id": "f3o0-9Dlw3E",
      "resource": "https://www.youtube.com/watch?v=f3o0-9Dlw3E",
      "title": "AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk",
      "author": "Eli Cohen, Snyk",
      "last_modified": "2026-10-07T21:30:34Z",
      "analysis_file": "analysis/f3o0-9Dlw3E.json"
    },
    {
      "id": "fnuNVFgLjHA",
      "resource": "https://www.youtube.com/watch?v=fnuNVFgLjHA",
      "title": "Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI",
      "author": "Fuad Ali, Arize AI",
      "last_modified": "2026-10-11T15:30:31Z",
      "analysis_file": "analysis/fnuNVFgLjHA.json"
    },
    {
      "id": "kR64LOqBBCU",
      "resource": "https://www.youtube.com/watch?v=kR64LOqBBCU",
      "title": "AgentCraft: Putting the Orc in Orchestration — Ido Salomon",
      "author": "Ido Salomon",
      "last_modified": "2026-04-25T16:00:06Z",
      "analysis_file": "analysis/kR64LOqBBCU.json"
    },
    {
      "id": "lCBf9slCanI",
      "resource": "https://www.youtube.com/watch?v=lCBf9slCanI",
      "title": "Ending AI Slop — Thais Castello Branco, Taste Labs",
      "author": "Thais Castello Branco, Taste Labs",
      "last_modified": "2026-07-31T19:26:20Z",
      "analysis_file": "analysis/lCBf9slCanI.json"
    },
    {
      "id": "prttz9_1XDc",
      "resource": "https://www.youtube.com/watch?v=prttz9_1XDc",
      "title": "Enhancing Quality and Security in CI: Gunjan Patel",
      "author": null,
      "last_modified": "2024-11-27T19:56:40Z",
      "analysis_file": "analysis/prttz9_1XDc.json"
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
      "id": "uU5Gv2h8-9g",
      "resource": "https://www.youtube.com/watch?v=uU5Gv2h8-9g",
      "title": "Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison",
      "author": "Cat Wu & Thariq Shihipar ft Simon Willison",
      "last_modified": "2026-07-15T15:05:06Z",
      "analysis_file": "analysis/uU5Gv2h8-9g.json"
    },
    {
      "id": "uuwDWRbxoYo",
      "resource": "https://www.youtube.com/watch?v=uuwDWRbxoYo",
      "title": "AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar",
      "author": "Ali-Reza Adl-Tabatabai, Sonar",
      "last_modified": "2026-10-09T01:30:15Z",
      "analysis_file": "analysis/uuwDWRbxoYo.json"
    },
    {
      "id": "wAQK7O3WGEE",
      "resource": "https://www.youtube.com/watch?v=wAQK7O3WGEE",
      "title": "Agents reported thousands of bugs, how many were real? - Ian Butler and Nick Gregory",
      "author": "Ian Butler and Nick Gregory",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/wAQK7O3WGEE.json"
    },
    {
      "id": "xLUQOqjudtA",
      "resource": "https://www.youtube.com/watch?v=xLUQOqjudtA",
      "title": "Tolan: Voice-First AI Companion — Paula Dozsa, Tolan",
      "author": "Paula Dozsa, Tolan",
      "last_modified": "2026-09-15T14:30:14Z",
      "analysis_file": "analysis/xLUQOqjudtA.json"
    },
    {
      "id": "x_1EumTaXeE",
      "resource": "https://www.youtube.com/watch?v=x_1EumTaXeE",
      "title": "Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue",
      "author": "Josh Albrecht, Imbue",
      "last_modified": "2025-07-25T23:10:37Z",
      "analysis_file": "analysis/x_1EumTaXeE.json"
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

# Require a concrete failure scenario and verify each review finding

## What

Require a concrete failure scenario and verify each review finding

Counter the tendency to approve plausible-looking code by actively looking for a concrete counterexample.

## Evidence

Source analysis [^0ML7ZLMdcl4]; no independently matched timestamped quote published.

Source analysis [^0tVu-V3_fFw]; no independently matched timestamped quote published.

Source analysis [^Bz1HFxQA1o8]; no independently matched timestamped quote published.

Source analysis [^JJGbw4ggaFs]; no independently matched timestamped quote published.

> from the harm. What could actually harm a patient? And let's look at some
> — 03:56 [^McknwOzbmyg]

> particular data point uh critique it self-verify your critique and then
> — 18:18 [^OMGPvW8TBHc]

Source analysis [^ON5LIT0M4do]; no independently matched timestamped quote published.

> changes, uh, an analysis summary, the root causes, what was fixed. So, we
> — 17:37 [^Q5IVm_CxN2w]

> be quite um impactful here is that a combination of algorithmic verification
> — 12:02 [^VrpEyglYgeU]

> capture screenshots as evidence. And then take those screenshots as well
> — 12:42 [^YgEv7IQzGdM]

Source analysis [^ZGzthw4BZiA]; no independently matched timestamped quote published.

> code by default. Assume there is something wrong with it. Um and
> — 13:02 [^_mi3alkqy4s]

> do is the reviewer running the code to prove its own bug report is real. Um the
> — 13:38 [^_mi3alkqy4s]

> passes, see keep what they agree on. Uh, and they found that it review raised
> — 12:23 [^_mi3alkqy4s]

> I want to test the endpoint. I just don't want only to check the code. I
> — 10:56 [^bSG9wUYaHWU]

> different set of rubrics, rubrics that were handcrafted by a human and describe
> — 13:52 [^blrovBxxN9o]

> to run all the checks that we want. But, that's where we made an explicit
> — 37:19 [^c35YoMdnI78]

Source analysis [^f3o0-9Dlw3E]; no independently matched timestamped quote published.

Source analysis [^fnuNVFgLjHA]; no independently matched timestamped quote published.

Source analysis [^kR64LOqBBCU]; no independently matched timestamped quote published.

Source analysis [^lCBf9slCanI]; no independently matched timestamped quote published.

> so what context am I providing the red team engineer security policies and the
> — 14:30 [^prttz9_1XDc]

> reason before it scores and have it explain its thinking first. Uh, this
> — 1:13:12 [^qZj7sqmidqA]

> share a recording of of your final implementation. And then I'll tag in
> — 10:36 [^uU5Gv2h8-9g]

Source analysis [^uuwDWRbxoYo]; no independently matched timestamped quote published.

Source analysis [^wAQK7O3WGEE]; no independently matched timestamped quote published.

> then they evaluated the changes against real production logs over three find fix
> — 11:55 [^xLUQOqjudtA]

> you really understand what went wrong, then it's much easier to solve the
> — 15:49 [^x_1EumTaXeE]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer redundant or low-value review rounds
- **Speed:** Shorter evidence-backed review/repair cycles
- **Quality:** Better focus on actionable defects rather than cosmetic scores
- **Reliability:** Independent, revision-bound verification
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^0ML7ZLMdcl4]: [AI Engineering at Jane Street - John Crepezzi](https://www.youtube.com/watch?v=0ML7ZLMdcl4); publication: 2025-03-28T15:04:44Z; analysis: `analysis/0ML7ZLMdcl4.json`.
[^0tVu-V3_fFw]: [Designing AI To Scale Human Thought — Jun Yu Tan, Tusk](https://www.youtube.com/watch?v=0tVu-V3_fFw); publication: 2025-06-03T07:00:06Z; analysis: `analysis/0tVu-V3_fFw.json`.
[^Bz1HFxQA1o8]: [Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco](https://www.youtube.com/watch?v=Bz1HFxQA1o8); publication: 2026-10-20T09:00:06Z; analysis: `analysis/Bz1HFxQA1o8.json`.
[^JJGbw4ggaFs]: [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud](https://www.youtube.com/watch?v=JJGbw4ggaFs); publication: 2026-07-19T13:45:06Z; analysis: `analysis/JJGbw4ggaFs.json`.
[^McknwOzbmyg]: [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](https://www.youtube.com/watch?v=McknwOzbmyg); publication: 2026-08-19T15:00:31Z; analysis: `analysis/McknwOzbmyg.json`.
[^OMGPvW8TBHc]: [Fuzzing in the GenAI Era — Leonard Tang, Haize Labs](https://www.youtube.com/watch?v=OMGPvW8TBHc); publication: 2025-08-22T15:00:05Z; analysis: `analysis/OMGPvW8TBHc.json`.
[^ON5LIT0M4do]: [Feedback Loops are All You Need — Mehedi Hassan, Granola](https://www.youtube.com/watch?v=ON5LIT0M4do); publication: 2026-05-10T18:00:06Z; analysis: `analysis/ON5LIT0M4do.json`.
[^Q5IVm_CxN2w]: [Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway](https://www.youtube.com/watch?v=Q5IVm_CxN2w); publication: 2025-11-24T20:16:36Z; analysis: `analysis/Q5IVm_CxN2w.json`.
[^VrpEyglYgeU]: [In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](https://www.youtube.com/watch?v=VrpEyglYgeU); publication: 2026-07-20T15:00:06Z; analysis: `analysis/VrpEyglYgeU.json`.
[^YgEv7IQzGdM]: [How to Kill the Code Review — Ankit Jain, Aviator](https://www.youtube.com/watch?v=YgEv7IQzGdM); publication: 2026-08-17T20:00:08Z; analysis: `analysis/YgEv7IQzGdM.json`.
[^ZGzthw4BZiA]: [Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab](https://www.youtube.com/watch?v=ZGzthw4BZiA); publication: 2026-10-11T20:00:38Z; analysis: `analysis/ZGzthw4BZiA.json`.
[^_mi3alkqy4s]: [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=_mi3alkqy4s); publication: 2026-09-30T13:30:35Z; analysis: `analysis/_mi3alkqy4s.json`.
[^bSG9wUYaHWU]: [Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU); publication: 2026-05-03T14:00:06Z; analysis: `analysis/bSG9wUYaHWU.json`.
[^blrovBxxN9o]: [Turning Fails into Features: Zapier’s Hard-Won Eval Lessons — Rafal Willinski, Vitor Balocco, Zapier](https://www.youtube.com/watch?v=blrovBxxN9o); publication: 2025-06-30T17:15:06Z; analysis: `analysis/blrovBxxN9o.json`.
[^c35YoMdnI78]: [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78); publication: 2026-07-17T21:00:06Z; analysis: `analysis/c35YoMdnI78.json`.
[^f3o0-9Dlw3E]: [AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk](https://www.youtube.com/watch?v=f3o0-9Dlw3E); publication: 2026-10-07T21:30:34Z; analysis: `analysis/f3o0-9Dlw3E.json`.
[^fnuNVFgLjHA]: [Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI](https://www.youtube.com/watch?v=fnuNVFgLjHA); publication: 2026-10-11T15:30:31Z; analysis: `analysis/fnuNVFgLjHA.json`.
[^kR64LOqBBCU]: [AgentCraft: Putting the Orc in Orchestration — Ido Salomon](https://www.youtube.com/watch?v=kR64LOqBBCU); publication: 2026-04-25T16:00:06Z; analysis: `analysis/kR64LOqBBCU.json`.
[^lCBf9slCanI]: [Ending AI Slop — Thais Castello Branco, Taste Labs](https://www.youtube.com/watch?v=lCBf9slCanI); publication: 2026-07-31T19:26:20Z; analysis: `analysis/lCBf9slCanI.json`.
[^prttz9_1XDc]: [Enhancing Quality and Security in CI: Gunjan Patel](https://www.youtube.com/watch?v=prttz9_1XDc); publication: 2024-11-27T19:56:40Z; analysis: `analysis/prttz9_1XDc.json`.
[^qZj7sqmidqA]: [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=qZj7sqmidqA); publication: 2026-10-05T22:00:36Z; analysis: `analysis/qZj7sqmidqA.json`.
[^uU5Gv2h8-9g]: [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](https://www.youtube.com/watch?v=uU5Gv2h8-9g); publication: 2026-07-15T15:05:06Z; analysis: `analysis/uU5Gv2h8-9g.json`.
[^uuwDWRbxoYo]: [AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar](https://www.youtube.com/watch?v=uuwDWRbxoYo); publication: 2026-10-09T01:30:15Z; analysis: `analysis/uuwDWRbxoYo.json`.
[^wAQK7O3WGEE]: [Agents reported thousands of bugs, how many were real? - Ian Butler and Nick Gregory](https://www.youtube.com/watch?v=wAQK7O3WGEE); publication: 2025-06-03T22:22:29Z; analysis: `analysis/wAQK7O3WGEE.json`.
[^xLUQOqjudtA]: [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](https://www.youtube.com/watch?v=xLUQOqjudtA); publication: 2026-09-15T14:30:14Z; analysis: `analysis/xLUQOqjudtA.json`.
[^x_1EumTaXeE]: [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](https://www.youtube.com/watch?v=x_1EumTaXeE); publication: 2025-07-25T23:10:37Z; analysis: `analysis/x_1EumTaXeE.json`.
