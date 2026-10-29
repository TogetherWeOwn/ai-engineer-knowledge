---
{
  "type": "technique",
  "id": "tail-distributions",
  "title": "Inspect tail failures, variance and per-class slices rather than averages alone",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-22T07:00:28Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "0NHCyq8bBcM",
      "resource": "https://www.youtube.com/watch?v=0NHCyq8bBcM",
      "title": "Remote MCPs: What we learned from shipping — John Welsh, Anthropic",
      "author": "John Welsh, Anthropic",
      "last_modified": "2025-06-19T16:52:25Z",
      "analysis_file": "analysis/0NHCyq8bBcM.json"
    },
    {
      "id": "2aS7aKoXn64",
      "resource": "https://www.youtube.com/watch?v=2aS7aKoXn64",
      "title": "Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software",
      "author": "Rayan Garg, Theta Software",
      "last_modified": "2026-08-01T00:00:06Z",
      "analysis_file": "analysis/2aS7aKoXn64.json"
    },
    {
      "id": "474j-n1Ltxc",
      "resource": "https://www.youtube.com/watch?v=474j-n1Ltxc",
      "title": "AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile",
      "author": "Daksh Gupta, Greptile",
      "last_modified": "2026-09-27T18:30:07Z",
      "analysis_file": "analysis/474j-n1Ltxc.json"
    },
    {
      "id": "71V3fTaUp2Q",
      "resource": "https://www.youtube.com/watch?v=71V3fTaUp2Q",
      "title": "Let LLMs Wander: Engineering RL Environments — Stefano Fiorucci",
      "author": "Stefano Fiorucci",
      "last_modified": "2026-04-08T06:15:06Z",
      "analysis_file": "analysis/71V3fTaUp2Q.json"
    },
    {
      "id": "CTLa_p6iOiY",
      "resource": "https://www.youtube.com/watch?v=CTLa_p6iOiY",
      "title": "Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs",
      "author": "Pierluca D'Oro, Programma Labs",
      "last_modified": "2026-08-14T14:30:31Z",
      "analysis_file": "analysis/CTLa_p6iOiY.json"
    },
    {
      "id": "DId2KP8Ykz4",
      "resource": "https://www.youtube.com/watch?v=DId2KP8Ykz4",
      "title": "Navigating RAG Optimization with an Evaluation Driven Compass: Atita Arora and Deanna Emery",
      "author": null,
      "last_modified": "2024-11-12T19:16:46Z",
      "analysis_file": "analysis/DId2KP8Ykz4.json"
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
      "id": "Hp4MzVTXcKw",
      "resource": "https://www.youtube.com/watch?v=Hp4MzVTXcKw",
      "title": "The Model Isn’t Wrong—You’re Just Bad at Prompting",
      "author": null,
      "last_modified": "2025-02-22T18:00:06Z",
      "analysis_file": "analysis/Hp4MzVTXcKw.json"
    },
    {
      "id": "I6aiEf3aEFQ",
      "resource": "https://www.youtube.com/watch?v=I6aiEf3aEFQ",
      "title": "Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition",
      "author": "Yu Su, NeoCognition",
      "last_modified": "2026-08-12T16:00:08Z",
      "analysis_file": "analysis/I6aiEf3aEFQ.json"
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
      "id": "MhHEGMFCEB0",
      "resource": "https://www.youtube.com/watch?v=MhHEGMFCEB0",
      "title": "OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman",
      "author": "Vaibhav Srivastav & Katia Gil Guzman",
      "last_modified": "2026-04-29T16:00:06Z",
      "analysis_file": "analysis/MhHEGMFCEB0.json"
    },
    {
      "id": "O-CBZ3JtRvo",
      "resource": "https://www.youtube.com/watch?v=O-CBZ3JtRvo",
      "title": "Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face",
      "author": "Uri Rolls, Arithmetic & Thom Wolf, Hugging Face",
      "last_modified": "2026-07-24T05:19:15Z",
      "analysis_file": "analysis/O-CBZ3JtRvo.json"
    },
    {
      "id": "O3FEoMYvUf8",
      "resource": "https://www.youtube.com/watch?v=O3FEoMYvUf8",
      "title": "Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers",
      "author": "Alejandro Vidal, Mindmakers",
      "last_modified": "2026-07-13T17:56:55Z",
      "analysis_file": "analysis/O3FEoMYvUf8.json"
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
      "id": "R7A8rX-09Zw",
      "resource": "https://www.youtube.com/watch?v=R7A8rX-09Zw",
      "title": "What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench",
      "author": "Peter Gostev, Arena.ai, BullshitBench",
      "last_modified": "2026-04-24T14:30:06Z",
      "analysis_file": "analysis/R7A8rX-09Zw.json"
    },
    {
      "id": "RhfqQKe22ZA",
      "resource": "https://www.youtube.com/watch?v=RhfqQKe22ZA",
      "title": "Why Agent Hype can fall short of reality – Joel Becker, METR",
      "author": "Joel Becker, METR",
      "last_modified": "2025-12-24T16:30:06Z",
      "analysis_file": "analysis/RhfqQKe22ZA.json"
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
      "id": "UGjk3Uk0MxM",
      "resource": "https://www.youtube.com/watch?v=UGjk3Uk0MxM",
      "title": "The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft",
      "author": "Pamela Fox, Microsoft",
      "last_modified": "2026-10-19T14:06:53Z",
      "analysis_file": "analysis/UGjk3Uk0MxM.json"
    },
    {
      "id": "UM6sFg_jdlE",
      "resource": "https://www.youtube.com/watch?v=UM6sFg_jdlE",
      "title": "RAG is dead, right?? — Kuba Rogut, Turbopuffer",
      "author": "Kuba Rogut, Turbopuffer",
      "last_modified": "2026-06-09T17:00:27Z",
      "analysis_file": "analysis/UM6sFg_jdlE.json"
    },
    {
      "id": "VBCDhRrvlYo",
      "resource": "https://www.youtube.com/watch?v=VBCDhRrvlYo",
      "title": "The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu",
      "author": "Arturo Nunez, Nereu",
      "last_modified": "2026-08-18T15:00:29Z",
      "analysis_file": "analysis/VBCDhRrvlYo.json"
    },
    {
      "id": "X4dEHRzBLmc",
      "resource": "https://www.youtube.com/watch?v=X4dEHRzBLmc",
      "title": "Judge the Judge: Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI",
      "author": "Mahmoud Mabrouk, Agenta AI",
      "last_modified": "2026-04-10T10:00:06Z",
      "analysis_file": "analysis/X4dEHRzBLmc.json"
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
      "id": "YXEqC05WEI0",
      "resource": "https://www.youtube.com/watch?v=YXEqC05WEI0",
      "title": "Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health",
      "author": "Rashi Agrawal, Hinge Health",
      "last_modified": "2026-08-19T14:30:18Z",
      "analysis_file": "analysis/YXEqC05WEI0.json"
    },
    {
      "id": "Yk87oUPVaxU",
      "resource": "https://www.youtube.com/watch?v=Yk87oUPVaxU",
      "title": "DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve",
      "author": "James Shi, Datacurve",
      "last_modified": "2026-07-26T18:10:56Z",
      "analysis_file": "analysis/Yk87oUPVaxU.json"
    },
    {
      "id": "YvQ4BVTWfHI",
      "resource": "https://www.youtube.com/watch?v=YvQ4BVTWfHI",
      "title": "Is a Faster Model Actually Faster? Test the Whole Job — Morgan Suo, MiniMax",
      "author": "Morgan Suo, MiniMax",
      "last_modified": "2026-10-21T07:00:34Z",
      "analysis_file": "analysis/YvQ4BVTWfHI.json"
    },
    {
      "id": "ZFxh7sqbUZo",
      "resource": "https://www.youtube.com/watch?v=ZFxh7sqbUZo",
      "title": "Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd",
      "author": "Prof. David Brumley, Bugcrowd",
      "last_modified": "2026-08-01T00:30:06Z",
      "analysis_file": "analysis/ZFxh7sqbUZo.json"
    },
    {
      "id": "_4Ph2dhmUFI",
      "resource": "https://www.youtube.com/watch?v=_4Ph2dhmUFI",
      "title": "How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase",
      "author": "Evan Kormos, Coinbase",
      "last_modified": "2026-10-19T23:00:08Z",
      "analysis_file": "analysis/_4Ph2dhmUFI.json"
    },
    {
      "id": "_dTF3NpPzGo",
      "resource": "https://www.youtube.com/watch?v=_dTF3NpPzGo",
      "title": "Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI",
      "author": "Louis-François Bouchard, Towards AI",
      "last_modified": "2026-10-22T07:00:28Z",
      "analysis_file": "analysis/_dTF3NpPzGo.json"
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
      "id": "bZISsg7H7DA",
      "resource": "https://www.youtube.com/watch?v=bZISsg7H7DA",
      "title": "Your Agents Need a Save Button - Hamza Tahir, ZenML",
      "author": "Hamza Tahir, ZenML",
      "last_modified": "2026-07-18T07:00:06Z",
      "analysis_file": "analysis/bZISsg7H7DA.json"
    },
    {
      "id": "bbq0b_FpYEY",
      "resource": "https://www.youtube.com/watch?v=bbq0b_FpYEY",
      "title": "Rust is the language of the AGI - Michael Yuan",
      "author": "Michael Yuan",
      "last_modified": "2025-06-03T22:22:27Z",
      "analysis_file": "analysis/bbq0b_FpYEY.json"
    },
    {
      "id": "cZ5ZJy19KMo",
      "resource": "https://www.youtube.com/watch?v=cZ5ZJy19KMo",
      "title": "Mission-Critical Evals at Scale (Learnings from 100k medical decisions)",
      "author": null,
      "last_modified": "2025-02-22T19:00:06Z",
      "analysis_file": "analysis/cZ5ZJy19KMo.json"
    },
    {
      "id": "d5EltXhbcfA",
      "resource": "https://www.youtube.com/watch?v=d5EltXhbcfA",
      "title": "Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil",
      "author": "Sayash Kapoor, AI Snake Oil",
      "last_modified": "2025-04-17T16:00:06Z",
      "analysis_file": "analysis/d5EltXhbcfA.json"
    },
    {
      "id": "eAXxdtNlK04",
      "resource": "https://www.youtube.com/watch?v=eAXxdtNlK04",
      "title": "Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse",
      "author": "Annabell Schäfer, Langfuse",
      "last_modified": "2026-07-18T20:15:06Z",
      "analysis_file": "analysis/eAXxdtNlK04.json"
    },
    {
      "id": "esY99nYXxR4",
      "resource": "https://www.youtube.com/watch?v=esY99nYXxR4",
      "title": "How we solved Context Management in Agents — Sally-Ann Delucia",
      "author": "Sally-Ann Delucia",
      "last_modified": "2026-05-10T19:00:06Z",
      "analysis_file": "analysis/esY99nYXxR4.json"
    },
    {
      "id": "fWXJM-J0ZB8",
      "resource": "https://www.youtube.com/watch?v=fWXJM-J0ZB8",
      "title": "Frontier results, on device - RL Nabors, Arize",
      "author": "RL Nabors, Arize",
      "last_modified": "2026-06-29T03:30:03Z",
      "analysis_file": "analysis/fWXJM-J0ZB8.json"
    },
    {
      "id": "gvIAkmZUEZY",
      "resource": "https://www.youtube.com/watch?v=gvIAkmZUEZY",
      "title": "Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code",
      "author": "Beyang Liu, Amp Code",
      "last_modified": "2025-12-22T17:00:06Z",
      "analysis_file": "analysis/gvIAkmZUEZY.json"
    },
    {
      "id": "hqHC6Z_lXyo",
      "resource": "https://www.youtube.com/watch?v=hqHC6Z_lXyo",
      "title": "20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna",
      "author": "Bertrand Charpentier, Pruna",
      "last_modified": "2026-06-01T17:00:06Z",
      "analysis_file": "analysis/hqHC6Z_lXyo.json"
    },
    {
      "id": "iNkFlCiij0U",
      "resource": "https://www.youtube.com/watch?v=iNkFlCiij0U",
      "title": "The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI",
      "author": "Vincent Chen, Snorkel AI",
      "last_modified": "2026-06-04T16:00:06Z",
      "analysis_file": "analysis/iNkFlCiij0U.json"
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
      "id": "kDEvo2__Ijg",
      "resource": "https://www.youtube.com/watch?v=kDEvo2__Ijg",
      "title": "From Copilot to Colleague: Trustworthy Agents for High-Stakes - Joel Hron, CTO Thomson Reuters",
      "author": "Joel Hron, CTO Thomson Reuters",
      "last_modified": "2025-07-23T12:15:13Z",
      "analysis_file": "analysis/kDEvo2__Ijg.json"
    },
    {
      "id": "kDczF4wBh8s",
      "resource": "https://www.youtube.com/watch?v=kDczF4wBh8s",
      "title": "From Self-driving to Autonomous Voice Agents — Brooke Hopkins, Coval",
      "author": "Brooke Hopkins, Coval",
      "last_modified": "2025-07-31T16:45:05Z",
      "analysis_file": "analysis/kDczF4wBh8s.json"
    },
    {
      "id": "kiClTcJUnhc",
      "resource": "https://www.youtube.com/watch?v=kiClTcJUnhc",
      "title": "Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic",
      "author": "CJ Avilla & Harrison Stall, Anthropic",
      "last_modified": "2026-10-16T19:00:10Z",
      "analysis_file": "analysis/kiClTcJUnhc.json"
    },
    {
      "id": "mpzktdYTcdE",
      "resource": "https://www.youtube.com/watch?v=mpzktdYTcdE",
      "title": "E-Values Evaluating the Values of AI: Sheila Gulati and Nischal Nadhamuni",
      "author": null,
      "last_modified": "2024-12-31T17:25:58Z",
      "analysis_file": "analysis/mpzktdYTcdE.json"
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
      "id": "obfPzbapMIM",
      "resource": "https://www.youtube.com/watch?v=obfPzbapMIM",
      "title": "Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse",
      "author": "Doneyli De Jesus & Annabell Schäfer, Langfuse",
      "last_modified": "2026-10-18T08:00:06Z",
      "analysis_file": "analysis/obfPzbapMIM.json"
    },
    {
      "id": "pj_hKFhnJCw",
      "resource": "https://www.youtube.com/watch?v=pj_hKFhnJCw",
      "title": "How to evaluate a model for your use case: Emmanuel Turlay",
      "author": null,
      "last_modified": "2025-02-05T11:18:34Z",
      "analysis_file": "analysis/pj_hKFhnJCw.json"
    },
    {
      "id": "tHN44yJoeS8",
      "resource": "https://www.youtube.com/watch?v=tHN44yJoeS8",
      "title": "Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor",
      "author": "Naman Jain, Cursor",
      "last_modified": "2025-12-15T17:18:09Z",
      "analysis_file": "analysis/tHN44yJoeS8.json"
    },
    {
      "id": "uiq95JYpBGY",
      "resource": "https://www.youtube.com/watch?v=uiq95JYpBGY",
      "title": "Productionizing GenAI Models – Lessons from the world's best AI teams: Lukas Biewald",
      "author": "Lessons from the world's best AI teams: Lukas Biewald",
      "last_modified": "2024-10-23T19:23:33Z",
      "analysis_file": "analysis/uiq95JYpBGY.json"
    },
    {
      "id": "v4F1gFy-hqg",
      "resource": "https://www.youtube.com/watch?v=v4F1gFy-hqg",
      "title": "\"Software Fundamentals Matter More Than Ever\" — Matt Pocock",
      "author": "Matt Pocock",
      "last_modified": "2026-04-23T15:15:06Z",
      "analysis_file": "analysis/v4F1gFy-hqg.json"
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
      "id": "wflNENRSUb4",
      "resource": "https://www.youtube.com/watch?v=wflNENRSUb4",
      "title": "Give Your Agent a Computer — Nico Albanese, Vercel",
      "author": "Nico Albanese, Vercel",
      "last_modified": "2026-05-12T18:00:06Z",
      "analysis_file": "analysis/wflNENRSUb4.json"
    },
    {
      "id": "xyL2Ltkh-SA",
      "resource": "https://www.youtube.com/watch?v=xyL2Ltkh-SA",
      "title": "How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads",
      "author": "Preetika Bhateja & Daniel Bump, YouTube Ads",
      "last_modified": "2026-07-24T21:00:00Z",
      "analysis_file": "analysis/xyL2Ltkh-SA.json"
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

# Inspect tail failures, variance and per-class slices rather than averages alone

## What

Inspect tail failures, variance and per-class slices rather than averages alone

Aggregate improvement can conceal unacceptable regressions on critical cases.

## Evidence

Source analysis [^0NHCyq8bBcM]; no independently matched timestamped quote published.

Source analysis [^2aS7aKoXn64]; no independently matched timestamped quote published.

Source analysis [^474j-n1Ltxc]; no independently matched timestamped quote published.

Source analysis [^71V3fTaUp2Q]; no independently matched timestamped quote published.

Source analysis [^CTLa_p6iOiY]; no independently matched timestamped quote published.

Source analysis [^DId2KP8Ykz4]; no independently matched timestamped quote published.

Source analysis [^Djv8Sp11UjI]; no independently matched timestamped quote published.

Source analysis [^Hp4MzVTXcKw]; no independently matched timestamped quote published.

Source analysis [^I6aiEf3aEFQ]; no independently matched timestamped quote published.

> simply recover it by just rereading it from the session log because everything
> — 15:42 [^K0X9QDRkIdg]

> it it gave the exact files that this particular sub-agent should review,
> — 38:51 [^MhHEGMFCEB0]

Source analysis [^O-CBZ3JtRvo]; no independently matched timestamped quote published.

Source analysis [^O3FEoMYvUf8]; no independently matched timestamped quote published.

Source analysis [^PjaVHm_3Ljg]; no independently matched timestamped quote published.

Source analysis [^R7A8rX-09Zw]; no independently matched timestamped quote published.

> sense. They don't require a ton of coordination with humans. They're often
> — 09:17 [^RhfqQKe22ZA]

> important thing is did anything that used to pass break? We can filter down
> — 1:46:31 [^SHMCGrNJJGc]

Source analysis [^UGjk3Uk0MxM]; no independently matched timestamped quote published.

Source analysis [^UM6sFg_jdlE]; no independently matched timestamped quote published.

Source analysis [^VBCDhRrvlYo]; no independently matched timestamped quote published.

> with very low to recall full non-compliance
> — 28:39 [^X4dEHRzBLmc]

> enough because performance is a distribution, not a point. The thing I
> — 04:22 [^YIxzNZDDy1A]

Source analysis [^YXEqC05WEI0]; no independently matched timestamped quote published.

> emphasis on bug localization and refactoring these are obviously very
> — 14:38 [^Yk87oUPVaxU]

Source analysis [^YvQ4BVTWfHI]; no independently matched timestamped quote published.

Source analysis [^ZFxh7sqbUZo]; no independently matched timestamped quote published.

> what the humans aren't seeing is still meeting the quality bar.
> — 15:25 [^_4Ph2dhmUFI]

Source analysis [^_dTF3NpPzGo]; no independently matched timestamped quote published.

> stop finding defects effectively if they try to read more than 400 lines of code
> — 03:56 [^_mi3alkqy4s]

> skill where we say, well, you need to have the description. It can only be so
> — 07:20 [^bSG9wUYaHWU]

> Build cohorts that matter. Um maybe take the expensive ones, maybe
> — 15:23 [^bZISsg7H7DA]

Source analysis [^bbq0b_FpYEY]; no independently matched timestamped quote published.

> can segment them by Enterprise by uh specific medical type medical conditions
> — 04:57 [^cZ5ZJy19KMo]

> do you construct these meaningful multi-dimensional metrics to evaluate
> — 09:16 [^d5EltXhbcfA]

> to also like make sure that it was only 10 labels so each of them got covered
> — 10:57 [^eAXxdtNlK04]

Source analysis [^esY99nYXxR4]; no independently matched timestamped quote published.

Source analysis [^fWXJM-J0ZB8]; no independently matched timestamped quote published.

> generating. We stream the diffs that it's making. uh we show you what CLI
> — 01:43 [^gvIAkmZUEZY]

> are very different models working well for the for different target use cases.
> — 05:16 [^hqHC6Z_lXyo]

> domain, for real-world tasks, and distribute those tasks uh intentionally.
> — 08:35 [^iNkFlCiij0U]

> data then you can like slice and dice by way finer grain things. And that's kind
> — 18:55 [^jxrGodnopHo]

Source analysis [^kDEvo2__Ijg]; no independently matched timestamped quote published.

> is like what reliability are you looking for for different parts of your product.
> — 12:13 [^kDczF4wBh8s]

> if you have some representation of the dependency graph that you know ahead of
> — 1:39:07 [^kiClTcJUnhc]

Source analysis [^mpzktdYTcdE]; no independently matched timestamped quote published.

> couple of times you would see you know dramatically different trajectories
> — 14:38 [^nxokqOq1imY]

> basically red teaming my agent and looking for prompt injection attacks and
> — 22:23 [^obfPzbapMIM]

> evaluation data set you can draw a distribution of that particular metric
> — 06:14 [^pj_hKFhnJCw]

Source analysis [^tHN44yJoeS8]; no independently matched timestamped quote published.

> but I kind of looked at the errors it was making looking at the errors
> — 13:11 [^uiq95JYpBGY]

> fast because the rate of feedback is your speed
> — 10:56 [^v4F1gFy-hqg]

Source analysis [^wAQK7O3WGEE]; no independently matched timestamped quote published.

> actual deterministic code for pulling that in, injecting it into the system
> — 57:35 [^wflNENRSUb4]

> your gatekeeping rule like what's your launch criteria. Is there a certain
> — 17:44 [^xyL2Ltkh-SA]

> if your primary request actually consumed let's say P90 of your latency
> — 09:30 [^zrZ1amZBSPw]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^0NHCyq8bBcM]: [Remote MCPs: What we learned from shipping — John Welsh, Anthropic](https://www.youtube.com/watch?v=0NHCyq8bBcM); publication: 2025-06-19T16:52:25Z; analysis: `analysis/0NHCyq8bBcM.json`.
[^2aS7aKoXn64]: [Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software](https://www.youtube.com/watch?v=2aS7aKoXn64); publication: 2026-08-01T00:00:06Z; analysis: `analysis/2aS7aKoXn64.json`.
[^474j-n1Ltxc]: [AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile](https://www.youtube.com/watch?v=474j-n1Ltxc); publication: 2026-09-27T18:30:07Z; analysis: `analysis/474j-n1Ltxc.json`.
[^71V3fTaUp2Q]: [Let LLMs Wander: Engineering RL Environments — Stefano Fiorucci](https://www.youtube.com/watch?v=71V3fTaUp2Q); publication: 2026-04-08T06:15:06Z; analysis: `analysis/71V3fTaUp2Q.json`.
[^CTLa_p6iOiY]: [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](https://www.youtube.com/watch?v=CTLa_p6iOiY); publication: 2026-08-14T14:30:31Z; analysis: `analysis/CTLa_p6iOiY.json`.
[^DId2KP8Ykz4]: [Navigating RAG Optimization with an Evaluation Driven Compass: Atita Arora and Deanna Emery](https://www.youtube.com/watch?v=DId2KP8Ykz4); publication: 2024-11-12T19:16:46Z; analysis: `analysis/DId2KP8Ykz4.json`.
[^Djv8Sp11UjI]: [The Current State of Browser Agents - Jerry Wu and Wyatt Marshall](https://www.youtube.com/watch?v=Djv8Sp11UjI); publication: 2025-06-03T22:22:26Z; analysis: `analysis/Djv8Sp11UjI.json`.
[^Hp4MzVTXcKw]: [The Model Isn’t Wrong—You’re Just Bad at Prompting](https://www.youtube.com/watch?v=Hp4MzVTXcKw); publication: 2025-02-22T18:00:06Z; analysis: `analysis/Hp4MzVTXcKw.json`.
[^I6aiEf3aEFQ]: [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](https://www.youtube.com/watch?v=I6aiEf3aEFQ); publication: 2026-08-12T16:00:08Z; analysis: `analysis/I6aiEf3aEFQ.json`.
[^K0X9QDRkIdg]: [Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic](https://www.youtube.com/watch?v=K0X9QDRkIdg); publication: 2026-08-11T16:00:06Z; analysis: `analysis/K0X9QDRkIdg.json`.
[^MhHEGMFCEB0]: [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](https://www.youtube.com/watch?v=MhHEGMFCEB0); publication: 2026-04-29T16:00:06Z; analysis: `analysis/MhHEGMFCEB0.json`.
[^O-CBZ3JtRvo]: [Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face](https://www.youtube.com/watch?v=O-CBZ3JtRvo); publication: 2026-07-24T05:19:15Z; analysis: `analysis/O-CBZ3JtRvo.json`.
[^O3FEoMYvUf8]: [Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers](https://www.youtube.com/watch?v=O3FEoMYvUf8); publication: 2026-07-13T17:56:55Z; analysis: `analysis/O3FEoMYvUf8.json`.
[^PjaVHm_3Ljg]: [Transforming search and discovery using LLMs — Tejaswi & Vinesh, Instacart](https://www.youtube.com/watch?v=PjaVHm_3Ljg); publication: 2025-07-16T18:01:03Z; analysis: `analysis/PjaVHm_3Ljg.json`.
[^R7A8rX-09Zw]: [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](https://www.youtube.com/watch?v=R7A8rX-09Zw); publication: 2026-04-24T14:30:06Z; analysis: `analysis/R7A8rX-09Zw.json`.
[^RhfqQKe22ZA]: [Why Agent Hype can fall short of reality – Joel Becker, METR](https://www.youtube.com/watch?v=RhfqQKe22ZA); publication: 2025-12-24T16:30:06Z; analysis: `analysis/RhfqQKe22ZA.json`.
[^SHMCGrNJJGc]: [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=SHMCGrNJJGc); publication: 2026-10-17T19:00:23Z; analysis: `analysis/SHMCGrNJJGc.json`.
[^UGjk3Uk0MxM]: [The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft](https://www.youtube.com/watch?v=UGjk3Uk0MxM); publication: 2026-10-19T14:06:53Z; analysis: `analysis/UGjk3Uk0MxM.json`.
[^UM6sFg_jdlE]: [RAG is dead, right?? — Kuba Rogut, Turbopuffer](https://www.youtube.com/watch?v=UM6sFg_jdlE); publication: 2026-06-09T17:00:27Z; analysis: `analysis/UM6sFg_jdlE.json`.
[^VBCDhRrvlYo]: [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](https://www.youtube.com/watch?v=VBCDhRrvlYo); publication: 2026-08-18T15:00:29Z; analysis: `analysis/VBCDhRrvlYo.json`.
[^X4dEHRzBLmc]: [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI](https://www.youtube.com/watch?v=X4dEHRzBLmc); publication: 2026-04-10T10:00:06Z; analysis: `analysis/X4dEHRzBLmc.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^YXEqC05WEI0]: [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](https://www.youtube.com/watch?v=YXEqC05WEI0); publication: 2026-08-19T14:30:18Z; analysis: `analysis/YXEqC05WEI0.json`.
[^Yk87oUPVaxU]: [DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve](https://www.youtube.com/watch?v=Yk87oUPVaxU); publication: 2026-07-26T18:10:56Z; analysis: `analysis/Yk87oUPVaxU.json`.
[^YvQ4BVTWfHI]: [Is a Faster Model Actually Faster? Test the Whole Job — Morgan Suo, MiniMax](https://www.youtube.com/watch?v=YvQ4BVTWfHI); publication: 2026-10-21T07:00:34Z; analysis: `analysis/YvQ4BVTWfHI.json`.
[^ZFxh7sqbUZo]: [Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd](https://www.youtube.com/watch?v=ZFxh7sqbUZo); publication: 2026-08-01T00:30:06Z; analysis: `analysis/ZFxh7sqbUZo.json`.
[^_4Ph2dhmUFI]: [How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase](https://www.youtube.com/watch?v=_4Ph2dhmUFI); publication: 2026-10-19T23:00:08Z; analysis: `analysis/_4Ph2dhmUFI.json`.
[^_dTF3NpPzGo]: [Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=_dTF3NpPzGo); publication: 2026-10-22T07:00:28Z; analysis: `analysis/_dTF3NpPzGo.json`.
[^_mi3alkqy4s]: [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=_mi3alkqy4s); publication: 2026-09-30T13:30:35Z; analysis: `analysis/_mi3alkqy4s.json`.
[^bSG9wUYaHWU]: [Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU); publication: 2026-05-03T14:00:06Z; analysis: `analysis/bSG9wUYaHWU.json`.
[^bZISsg7H7DA]: [Your Agents Need a Save Button - Hamza Tahir, ZenML](https://www.youtube.com/watch?v=bZISsg7H7DA); publication: 2026-07-18T07:00:06Z; analysis: `analysis/bZISsg7H7DA.json`.
[^bbq0b_FpYEY]: [Rust is the language of the AGI - Michael Yuan](https://www.youtube.com/watch?v=bbq0b_FpYEY); publication: 2025-06-03T22:22:27Z; analysis: `analysis/bbq0b_FpYEY.json`.
[^cZ5ZJy19KMo]: [Mission-Critical Evals at Scale (Learnings from 100k medical decisions)](https://www.youtube.com/watch?v=cZ5ZJy19KMo); publication: 2025-02-22T19:00:06Z; analysis: `analysis/cZ5ZJy19KMo.json`.
[^d5EltXhbcfA]: [Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil](https://www.youtube.com/watch?v=d5EltXhbcfA); publication: 2025-04-17T16:00:06Z; analysis: `analysis/d5EltXhbcfA.json`.
[^eAXxdtNlK04]: [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=eAXxdtNlK04); publication: 2026-07-18T20:15:06Z; analysis: `analysis/eAXxdtNlK04.json`.
[^esY99nYXxR4]: [How we solved Context Management in Agents — Sally-Ann Delucia](https://www.youtube.com/watch?v=esY99nYXxR4); publication: 2026-05-10T19:00:06Z; analysis: `analysis/esY99nYXxR4.json`.
[^fWXJM-J0ZB8]: [Frontier results, on device - RL Nabors, Arize](https://www.youtube.com/watch?v=fWXJM-J0ZB8); publication: 2026-06-29T03:30:03Z; analysis: `analysis/fWXJM-J0ZB8.json`.
[^gvIAkmZUEZY]: [Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code](https://www.youtube.com/watch?v=gvIAkmZUEZY); publication: 2025-12-22T17:00:06Z; analysis: `analysis/gvIAkmZUEZY.json`.
[^hqHC6Z_lXyo]: [20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna](https://www.youtube.com/watch?v=hqHC6Z_lXyo); publication: 2026-06-01T17:00:06Z; analysis: `analysis/hqHC6Z_lXyo.json`.
[^iNkFlCiij0U]: [The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI](https://www.youtube.com/watch?v=iNkFlCiij0U); publication: 2026-06-04T16:00:06Z; analysis: `analysis/iNkFlCiij0U.json`.
[^jxrGodnopHo]: [[Full Workshop] Building Metrics that actually work — David Karam, Pi Labs (fmr Google Search)](https://www.youtube.com/watch?v=jxrGodnopHo); publication: 2025-07-29T00:29:21Z; analysis: `analysis/jxrGodnopHo.json`.
[^kDEvo2__Ijg]: [From Copilot to Colleague: Trustworthy Agents for High-Stakes - Joel Hron, CTO Thomson Reuters](https://www.youtube.com/watch?v=kDEvo2__Ijg); publication: 2025-07-23T12:15:13Z; analysis: `analysis/kDEvo2__Ijg.json`.
[^kDczF4wBh8s]: [From Self-driving to Autonomous Voice Agents — Brooke Hopkins, Coval](https://www.youtube.com/watch?v=kDczF4wBh8s); publication: 2025-07-31T16:45:05Z; analysis: `analysis/kDczF4wBh8s.json`.
[^kiClTcJUnhc]: [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc); publication: 2026-10-16T19:00:10Z; analysis: `analysis/kiClTcJUnhc.json`.
[^mpzktdYTcdE]: [E-Values Evaluating the Values of AI: Sheila Gulati and Nischal Nadhamuni](https://www.youtube.com/watch?v=mpzktdYTcdE); publication: 2024-12-31T17:25:58Z; analysis: `analysis/mpzktdYTcdE.json`.
[^nxokqOq1imY]: [Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust](https://www.youtube.com/watch?v=nxokqOq1imY); publication: 2026-08-20T13:00:06Z; analysis: `analysis/nxokqOq1imY.json`.
[^obfPzbapMIM]: [Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=obfPzbapMIM); publication: 2026-10-18T08:00:06Z; analysis: `analysis/obfPzbapMIM.json`.
[^pj_hKFhnJCw]: [How to evaluate a model for your use case: Emmanuel Turlay](https://www.youtube.com/watch?v=pj_hKFhnJCw); publication: 2025-02-05T11:18:34Z; analysis: `analysis/pj_hKFhnJCw.json`.
[^tHN44yJoeS8]: [Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor](https://www.youtube.com/watch?v=tHN44yJoeS8); publication: 2025-12-15T17:18:09Z; analysis: `analysis/tHN44yJoeS8.json`.
[^uiq95JYpBGY]: [Productionizing GenAI Models – Lessons from the world's best AI teams: Lukas Biewald](https://www.youtube.com/watch?v=uiq95JYpBGY); publication: 2024-10-23T19:23:33Z; analysis: `analysis/uiq95JYpBGY.json`.
[^v4F1gFy-hqg]: ["Software Fundamentals Matter More Than Ever" — Matt Pocock](https://www.youtube.com/watch?v=v4F1gFy-hqg); publication: 2026-04-23T15:15:06Z; analysis: `analysis/v4F1gFy-hqg.json`.
[^wAQK7O3WGEE]: [Agents reported thousands of bugs, how many were real? - Ian Butler and Nick Gregory](https://www.youtube.com/watch?v=wAQK7O3WGEE); publication: 2025-06-03T22:22:29Z; analysis: `analysis/wAQK7O3WGEE.json`.
[^wflNENRSUb4]: [Give Your Agent a Computer — Nico Albanese, Vercel](https://www.youtube.com/watch?v=wflNENRSUb4); publication: 2026-05-12T18:00:06Z; analysis: `analysis/wflNENRSUb4.json`.
[^xyL2Ltkh-SA]: [How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](https://www.youtube.com/watch?v=xyL2Ltkh-SA); publication: 2026-07-24T21:00:00Z; analysis: `analysis/xyL2Ltkh-SA.json`.
[^zrZ1amZBSPw]: [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](https://www.youtube.com/watch?v=zrZ1amZBSPw); publication: 2026-08-28T15:30:03Z; analysis: `analysis/zrZ1amZBSPw.json`.
