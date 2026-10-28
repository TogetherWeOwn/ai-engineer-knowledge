---
{
  "type": "technique",
  "id": "progress-loop-budgets",
  "title": "Stop retry and self-fix loops when progress or attempt budgets are exhausted",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-17T09:00:27Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "17-YSUHo6Lk",
      "resource": "https://www.youtube.com/watch?v=17-YSUHo6Lk",
      "title": "Building Blocks for Uber’s Software Factory— Uday Kiran Medisetty & Adam Huda, Uber",
      "author": null,
      "last_modified": "2026-08-21T13:00:06Z",
      "analysis_file": "analysis/17-YSUHo6Lk.json"
    },
    {
      "id": "31GUkCBD-Uc",
      "resource": "https://www.youtube.com/watch?v=31GUkCBD-Uc",
      "title": "Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber",
      "author": "Soumya Gupta & Jai Chopra, Uber",
      "last_modified": "2026-07-24T22:00:25Z",
      "analysis_file": "analysis/31GUkCBD-Uc.json"
    },
    {
      "id": "33Oct2hqGnk",
      "resource": "https://www.youtube.com/watch?v=33Oct2hqGnk",
      "title": "Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS",
      "author": "Sandhya Subramani, AWS",
      "last_modified": "2026-10-04T21:00:13Z",
      "analysis_file": "analysis/33Oct2hqGnk.json"
    },
    {
      "id": "72XxWkd8Jrk",
      "resource": "https://www.youtube.com/watch?v=72XxWkd8Jrk",
      "title": "Effective agent design patterns in production — Laurie Voss, LlamaIndex",
      "author": "Laurie Voss, LlamaIndex",
      "last_modified": "2025-06-27T10:22:56Z",
      "analysis_file": "analysis/72XxWkd8Jrk.json"
    },
    {
      "id": "7c9FSUVcXR0",
      "resource": "https://www.youtube.com/watch?v=7c9FSUVcXR0",
      "title": "Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta",
      "author": "Nishant Gupta & Naman Ahuja, Meta",
      "last_modified": "2026-09-19T15:00:10Z",
      "analysis_file": "analysis/7c9FSUVcXR0.json"
    },
    {
      "id": "APh1Vx0oLmQ",
      "resource": "https://www.youtube.com/watch?v=APh1Vx0oLmQ",
      "title": "Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs",
      "author": "Nishant Gupta, Meta Superintelligence Labs",
      "last_modified": "2026-06-29T02:00:28Z",
      "analysis_file": "analysis/APh1Vx0oLmQ.json"
    },
    {
      "id": "C_GG5g38vLU",
      "resource": "https://www.youtube.com/watch?v=C_GG5g38vLU",
      "title": "Harnesses in AI: A Deep Dive — Tejas Kumar, IBM",
      "author": "Tejas Kumar, IBM",
      "last_modified": "2026-05-17T17:30:06Z",
      "analysis_file": "analysis/C_GG5g38vLU.json"
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
      "id": "EnT4Wej5M5k",
      "resource": "https://www.youtube.com/watch?v=EnT4Wej5M5k",
      "title": "The Benchmarks Game: Why It's Rigged and How You Can (Really) Win - Darius Emrani",
      "author": "Darius Emrani",
      "last_modified": "2025-06-03T22:22:25Z",
      "analysis_file": "analysis/EnT4Wej5M5k.json"
    },
    {
      "id": "FlzpEGHNVKQ",
      "resource": "https://www.youtube.com/watch?v=FlzpEGHNVKQ",
      "title": "Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take",
      "author": "Anant Dole and Asbjorn Steinskog, Take Take Take",
      "last_modified": "2026-05-13T15:00:06Z",
      "analysis_file": "analysis/FlzpEGHNVKQ.json"
    },
    {
      "id": "GJX19pNhmSw",
      "resource": "https://www.youtube.com/watch?v=GJX19pNhmSw",
      "title": "FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft",
      "author": "Tisha Chawla & Susheem Koul, Microsoft",
      "last_modified": "2026-08-22T14:30:07Z",
      "analysis_file": "analysis/GJX19pNhmSw.json"
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
      "id": "KtBivPzmOM8",
      "resource": "https://www.youtube.com/watch?v=KtBivPzmOM8",
      "title": "Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle",
      "author": "Nacho Martinez, Oracle",
      "last_modified": "2026-10-17T07:00:25Z",
      "analysis_file": "analysis/KtBivPzmOM8.json"
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
      "id": "Lqq_LcBaJCc",
      "resource": "https://www.youtube.com/watch?v=Lqq_LcBaJCc",
      "title": "How agents will unlock the $500B promise of AI - Donald Hruska, Retool",
      "author": "Donald Hruska, Retool",
      "last_modified": "2025-07-23T15:51:38Z",
      "analysis_file": "analysis/Lqq_LcBaJCc.json"
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
      "id": "MpZzWMdmQCE",
      "resource": "https://www.youtube.com/watch?v=MpZzWMdmQCE",
      "title": "Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com",
      "author": "Talha Sheikh, Checkout.com",
      "last_modified": "2026-07-08T08:31:41Z",
      "analysis_file": "analysis/MpZzWMdmQCE.json"
    },
    {
      "id": "NaOkR3VSfR4",
      "resource": "https://www.youtube.com/watch?v=NaOkR3VSfR4",
      "title": "Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya",
      "author": "Viren Baraiya",
      "last_modified": "2026-10-08T22:30:09Z",
      "analysis_file": "analysis/NaOkR3VSfR4.json"
    },
    {
      "id": "OC04sP_QgTI",
      "resource": "https://www.youtube.com/watch?v=OC04sP_QgTI",
      "title": "Ensure AI Agents Work: Evaluation Frameworks for Scaling Success — Aparna Dhinkaran, CEO Arize",
      "author": "Aparna Dhinkaran, CEO Arize",
      "last_modified": "2025-04-23T16:00:06Z",
      "analysis_file": "analysis/OC04sP_QgTI.json"
    },
    {
      "id": "OD13PiXw60o",
      "resource": "https://www.youtube.com/watch?v=OD13PiXw60o",
      "title": "Building Multi agent Systems with Finite State Machines",
      "author": null,
      "last_modified": "2025-02-22T17:00:05Z",
      "analysis_file": "analysis/OD13PiXw60o.json"
    },
    {
      "id": "ORVh4GivEU0",
      "resource": "https://www.youtube.com/watch?v=ORVh4GivEU0",
      "title": "Beyond RAG: A Relational Context Engine That Cuts Token Burn — Unblocked",
      "author": "Unblocked",
      "last_modified": "2026-10-10T19:30:39Z",
      "analysis_file": "analysis/ORVh4GivEU0.json"
    },
    {
      "id": "ObTPqBGsEbA",
      "resource": "https://www.youtube.com/watch?v=ObTPqBGsEbA",
      "title": "The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks",
      "author": "Sandipan Bhaumik, Databricks",
      "last_modified": "2026-06-18T13:00:06Z",
      "analysis_file": "analysis/ObTPqBGsEbA.json"
    },
    {
      "id": "PXj0p_mW9nI",
      "resource": "https://www.youtube.com/watch?v=PXj0p_mW9nI",
      "title": "Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic",
      "author": "Katelyn Lesse & Angela Jiang, Anthropic",
      "last_modified": "2026-09-14T14:00:06Z",
      "analysis_file": "analysis/PXj0p_mW9nI.json"
    },
    {
      "id": "QSeaZ6qHyXs",
      "resource": "https://www.youtube.com/watch?v=QSeaZ6qHyXs",
      "title": "Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T06:07:45Z",
      "analysis_file": "analysis/QSeaZ6qHyXs.json"
    },
    {
      "id": "Qvp9vw4jJQ8",
      "resource": "https://www.youtube.com/watch?v=Qvp9vw4jJQ8",
      "title": "Break It 'Til You Make It: Building the Self-Improving Stack for AI Agents - Aparna Dhinakaran",
      "author": "Aparna Dhinakaran",
      "last_modified": "2025-06-10T17:30:11Z",
      "analysis_file": "analysis/Qvp9vw4jJQ8.json"
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
      "id": "Sir59K8ZDPU",
      "resource": "https://www.youtube.com/watch?v=Sir59K8ZDPU",
      "title": "Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley",
      "author": "Frank Coyle, UC Berkeley",
      "last_modified": "2026-07-23T01:00:07Z",
      "analysis_file": "analysis/Sir59K8ZDPU.json"
    },
    {
      "id": "TeGsFFNqRLA",
      "resource": "https://www.youtube.com/watch?v=TeGsFFNqRLA",
      "title": "Fast Models Need Slow Developers — Sarah Chieng, Cerebras",
      "author": "Sarah Chieng, Cerebras",
      "last_modified": "2026-05-22T18:00:06Z",
      "analysis_file": "analysis/TeGsFFNqRLA.json"
    },
    {
      "id": "Ti-BmGU1_mQ",
      "resource": "https://www.youtube.com/watch?v=Ti-BmGU1_mQ",
      "title": "The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI",
      "author": "Eugene Cheah, Featherless AI",
      "last_modified": "2026-10-17T09:00:27Z",
      "analysis_file": "analysis/Ti-BmGU1_mQ.json"
    },
    {
      "id": "U3MVU6JpocU",
      "resource": "https://www.youtube.com/watch?v=U3MVU6JpocU",
      "title": "AI Agents, Meet Test Driven Development",
      "author": null,
      "last_modified": "2025-02-22T22:05:15Z",
      "analysis_file": "analysis/U3MVU6JpocU.json"
    },
    {
      "id": "VaS2h-dY1-4",
      "resource": "https://www.youtube.com/watch?v=VaS2h-dY1-4",
      "title": "Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw",
      "author": "Onur Solmaz, OpenClaw",
      "last_modified": "2026-05-21T15:00:06Z",
      "analysis_file": "analysis/VaS2h-dY1-4.json"
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
      "id": "YIxzNZDDy1A",
      "resource": "https://www.youtube.com/watch?v=YIxzNZDDy1A",
      "title": "From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases",
      "author": "Wolfram Ravenwolf, Weights & Biases",
      "last_modified": "2026-10-11T17:00:18Z",
      "analysis_file": "analysis/YIxzNZDDy1A.json"
    },
    {
      "id": "YXiLj4tJt5A",
      "resource": "https://www.youtube.com/watch?v=YXiLj4tJt5A",
      "title": "Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS",
      "author": "Elizabeth Fuentes Leone & Sandhya Subramani, AWS",
      "last_modified": "2026-10-11T15:00:05Z",
      "analysis_file": "analysis/YXiLj4tJt5A.json"
    },
    {
      "id": "ZpK5PWX2YRM",
      "resource": "https://www.youtube.com/watch?v=ZpK5PWX2YRM",
      "title": "Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI",
      "author": "Alex Volkov, ThursdAI",
      "last_modified": "2026-07-10T18:00:06Z",
      "analysis_file": "analysis/ZpK5PWX2YRM.json"
    },
    {
      "id": "_-oIuRH4oGA",
      "resource": "https://www.youtube.com/watch?v=_-oIuRH4oGA",
      "title": "How agents broke app-level infrastructure - Evan Boyle",
      "author": "Evan Boyle",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/_-oIuRH4oGA.json"
    },
    {
      "id": "atwSCxWFVMg",
      "resource": "https://www.youtube.com/watch?v=atwSCxWFVMg",
      "title": "GPT Web App Generator - 10,000 apps created in a month: Matija Sosic",
      "author": "10,000 apps created in a month: Matija Sosic",
      "last_modified": "2024-01-26T20:51:42Z",
      "analysis_file": "analysis/atwSCxWFVMg.json"
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
      "id": "bjNYEc908oQ",
      "resource": "https://www.youtube.com/watch?v=bjNYEc908oQ",
      "title": "Building Reliable Agentic Systems: Eno Reyes",
      "author": null,
      "last_modified": "2024-08-20T13:44:51Z",
      "analysis_file": "analysis/bjNYEc908oQ.json"
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
      "id": "fLUtUkqYHnQ",
      "resource": "https://www.youtube.com/watch?v=fLUtUkqYHnQ",
      "title": "Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI",
      "author": "Maxime Labonne, Liquid AI",
      "last_modified": "2026-04-29T12:00:06Z",
      "analysis_file": "analysis/fLUtUkqYHnQ.json"
    },
    {
      "id": "gEDl9C8s_-4",
      "resource": "https://www.youtube.com/watch?v=gEDl9C8s_-4",
      "title": "How to Train Your Agent: Building Reliable Agents with RL — Kyle Corbitt, OpenPipe",
      "author": "Kyle Corbitt, OpenPipe",
      "last_modified": "2025-07-19T21:12:06Z",
      "analysis_file": "analysis/gEDl9C8s_-4.json"
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
      "id": "kDlqpN1JyIw",
      "resource": "https://www.youtube.com/watch?v=kDlqpN1JyIw",
      "title": "Vercel AI SDK Masterclass: From Fundamentals to Deep Research",
      "author": null,
      "last_modified": "2025-04-20T21:39:01Z",
      "analysis_file": "analysis/kDlqpN1JyIw.json"
    },
    {
      "id": "mYSRn6PC1mc",
      "resource": "https://www.youtube.com/watch?v=mYSRn6PC1mc",
      "title": "Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi",
      "author": "Louis-François Bouchard, Paul Iusztin, Samridhi",
      "last_modified": "2026-04-20T18:45:16Z",
      "analysis_file": "analysis/mYSRn6PC1mc.json"
    },
    {
      "id": "o6U_2vd967Y",
      "resource": "https://www.youtube.com/watch?v=o6U_2vd967Y",
      "title": "Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft",
      "author": "Divakar Kumar, FlyersSoft",
      "last_modified": "2026-07-30T00:00:06Z",
      "analysis_file": "analysis/o6U_2vd967Y.json"
    },
    {
      "id": "o_LRtAomJCs",
      "resource": "https://www.youtube.com/watch?v=o_LRtAomJCs",
      "title": "Human seeded Evals — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-07-25T07:00:06Z",
      "analysis_file": "analysis/o_LRtAomJCs.json"
    },
    {
      "id": "ow1we5PzK-o",
      "resource": "https://www.youtube.com/watch?v=ow1we5PzK-o",
      "title": "The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory",
      "author": "Luke Alvoeiro, Factory",
      "last_modified": "2026-05-06T15:00:06Z",
      "analysis_file": "analysis/ow1we5PzK-o.json"
    },
    {
      "id": "pZ4DIH2BVqg",
      "resource": "https://www.youtube.com/watch?v=pZ4DIH2BVqg",
      "title": "Pydantic is STILL all you need: Jason Liu",
      "author": null,
      "last_modified": "2024-09-06T17:07:06Z",
      "analysis_file": "analysis/pZ4DIH2BVqg.json"
    },
    {
      "id": "pmoDeA3RBZY",
      "resource": "https://www.youtube.com/watch?v=pmoDeA3RBZY",
      "title": "Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw",
      "author": "Vincent Koc, OpenClaw",
      "last_modified": "2026-06-05T16:00:06Z",
      "analysis_file": "analysis/pmoDeA3RBZY.json"
    },
    {
      "id": "sOB3HSiG8vo",
      "resource": "https://www.youtube.com/watch?v=sOB3HSiG8vo",
      "title": "Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI",
      "author": "Qianru Lao & Lu Zhang, OpenAI",
      "last_modified": "2026-09-19T15:30:04Z",
      "analysis_file": "analysis/sOB3HSiG8vo.json"
    },
    {
      "id": "shRR1e2HXMk",
      "resource": "https://www.youtube.com/watch?v=shRR1e2HXMk",
      "title": "How Codex Works — Dominik Kundel, OpenAI",
      "author": "Dominik Kundel, OpenAI",
      "last_modified": "2026-08-10T16:00:06Z",
      "analysis_file": "analysis/shRR1e2HXMk.json"
    },
    {
      "id": "sn79oS4MZFI",
      "resource": "https://www.youtube.com/watch?v=sn79oS4MZFI",
      "title": "Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason",
      "author": "Dan Mason",
      "last_modified": "2025-06-22T16:00:06Z",
      "analysis_file": "analysis/sn79oS4MZFI.json"
    },
    {
      "id": "uiP88SpCi1Q",
      "resource": "https://www.youtube.com/watch?v=uiP88SpCi1Q",
      "title": "Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS",
      "author": "Erik Hanchett, AWS",
      "last_modified": "2026-06-28T22:00:14Z",
      "analysis_file": "analysis/uiP88SpCi1Q.json"
    },
    {
      "id": "vGCJ7diEtrw",
      "resource": "https://www.youtube.com/watch?v=vGCJ7diEtrw",
      "title": "What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory",
      "author": "Tereza Tížková, Factory",
      "last_modified": "2026-09-27T15:00:02Z",
      "analysis_file": "analysis/vGCJ7diEtrw.json"
    },
    {
      "id": "xIt_mTQp6mY",
      "resource": "https://www.youtube.com/watch?v=xIt_mTQp6mY",
      "title": "Loop Engineering from First Principles — Kyle Mistele, HumanLayer",
      "author": "Kyle Mistele, HumanLayer",
      "last_modified": "2026-07-25T20:41:40Z",
      "analysis_file": "analysis/xIt_mTQp6mY.json"
    },
    {
      "id": "xs-ob87TTzg",
      "resource": "https://www.youtube.com/watch?v=xs-ob87TTzg",
      "title": "Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle",
      "author": "Ignacio Martinez, Oracle",
      "last_modified": "2026-09-18T16:00:11Z",
      "analysis_file": "analysis/xs-ob87TTzg.json"
    },
    {
      "id": "yj-wSRJwrrc",
      "resource": "https://www.youtube.com/watch?v=yj-wSRJwrrc",
      "title": "Pydantic is all you need: Jason Liu",
      "author": null,
      "last_modified": "2023-11-01T16:27:08Z",
      "analysis_file": "analysis/yj-wSRJwrrc.json"
    },
    {
      "id": "z0sh8HyTrDo",
      "resource": "https://www.youtube.com/watch?v=z0sh8HyTrDo",
      "title": "Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI",
      "author": "Ramana Siddanth Emani, Auditoria AI",
      "last_modified": "2026-07-30T03:00:06Z",
      "analysis_file": "analysis/z0sh8HyTrDo.json"
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

# Stop retry and self-fix loops when progress or attempt budgets are exhausted

## What

Stop retry and self-fix loops when progress or attempt budgets are exhausted

A specialist critic supplies actionable feedback and the author revises; explicit state transitions keep iteration controlled.

## Evidence

Source analysis [^17-YSUHo6Lk]; no independently matched timestamped quote published.

Source analysis [^31GUkCBD-Uc]; no independently matched timestamped quote published.

Source analysis [^33Oct2hqGnk]; no independently matched timestamped quote published.

> not, you can get the LLM to generate feedback and send it back uh to the
> — 13:33 [^72XxWkd8Jrk]

Source analysis [^7c9FSUVcXR0]; no independently matched timestamped quote published.

Source analysis [^APh1Vx0oLmQ]; no independently matched timestamped quote published.

Source analysis [^C_GG5g38vLU]; no independently matched timestamped quote published.

Source analysis [^Djv8Sp11UjI]; no independently matched timestamped quote published.

Source analysis [^EnT4Wej5M5k]; no independently matched timestamped quote published.

Source analysis [^FlzpEGHNVKQ]; no independently matched timestamped quote published.

Source analysis [^GJX19pNhmSw]; no independently matched timestamped quote published.

> So, one clear signal of someone being stuck is that they ask for the same
> — 05:30 [^KA5kPbdkK2E]

Source analysis [^KtBivPzmOM8]; no independently matched timestamped quote published.

Source analysis [^LqLoYksJ6do]; no independently matched timestamped quote published.

Source analysis [^Lqq_LcBaJCc]; no independently matched timestamped quote published.

Source analysis [^MhHEGMFCEB0]; no independently matched timestamped quote published.

Source analysis [^MpZzWMdmQCE]; no independently matched timestamped quote published.

Source analysis [^NaOkR3VSfR4]; no independently matched timestamped quote published.

> of steps that your agent takes to actually consistently complete a task so
> — 11:07 [^OC04sP_QgTI]

> from another agent another human or both can dramatically improve response
> — 10:17 [^OD13PiXw60o]

> technical standpoint. It's just a loop with some sort of maximum retry.
> — 15:37 [^ORVh4GivEU0]

> it will say, "Okay, go and retry for three times, not more than three times.
> — 14:53 [^ObTPqBGsEbA]

> You can define this in a rubric and then each time an executor tries to
> — 02:56 [^PXj0p_mW9nI]

Source analysis [^QSeaZ6qHyXs]; no independently matched timestamped quote published.

Source analysis [^Qvp9vw4jJQ8]; no independently matched timestamped quote published.

> calls, but make your tool calls very rigorous. So I think it's okay to have a
> — 25:17 [^RFKCzGlAU6Q]

Source analysis [^Sir59K8ZDPU]; no independently matched timestamped quote published.

Source analysis [^TeGsFFNqRLA]; no independently matched timestamped quote published.

Source analysis [^Ti-BmGU1_mQ]; no independently matched timestamped quote published.

Source analysis [^U3MVU6JpocU]; no independently matched timestamped quote published.

Source analysis [^VaS2h-dY1-4]; no independently matched timestamped quote published.

> error it uses five different techniques then goes back and your context window
> — 13:31 [^Ve-akpov78Q]

> if the model can't do the task, it sometimes just goes in circles and tries
> — 22:18 [^YIxzNZDDy1A]

> end the agent's turn if we wanted to. For demo purposes, we wanted to show you
> — 34:35 [^YXiLj4tJt5A]

Source analysis [^ZpK5PWX2YRM]; no independently matched timestamped quote published.

Source analysis [^_-oIuRH4oGA]; no independently matched timestamped quote published.

Source analysis [^atwSCxWFVMg]; no independently matched timestamped quote published.

> But by providing the agents with tools to validate the quality of of the
> — 13:42 [^b_PmGocP4rc]

> let's do fancy algorithms to decide where we want to move based on the
> — 11:12 [^bjNYEc908oQ]

> saying whether a loop should continue or not.
> — 45:48 [^c35YoMdnI78]

> sub agents there can be recursions there can be all sorts of systems maybe just
> — 08:30 [^d5EltXhbcfA]

Source analysis [^eAXxdtNlK04]; no independently matched timestamped quote published.

Source analysis [^fLUtUkqYHnQ]; no independently matched timestamped quote published.

Source analysis [^gEDl9C8s_-4]; no independently matched timestamped quote published.

> you have some kind of stopping criteria? Right? So, for example, like I was I had
> — 1:13:16 [^il1c1a2FufU]

Source analysis [^kDlqpN1JyIw]; no independently matched timestamped quote published.

> exists, and then it's going to ask a different question every time to fill
> — 1:05:28 [^mYSRn6PC1mc]

> realize that it's just easier to just put a fixed number of iterations, and
> — 1:23:42 [^mYSRn6PC1mc]

Source analysis [^o6U_2vd967Y]; no independently matched timestamped quote published.

Source analysis [^o_LRtAomJCs]; no independently matched timestamped quote published.

> The errors get caught at milestone boundaries. Corrective work gets scoped
> — 08:47 [^ow1we5PzK-o]

> first thing is that often one retry for models like open Ai and anthropic are
> — 12:30 [^pZ4DIH2BVqg]

> right in agents A lot of it now becomes generating workflows and dags to then go
> — 13:59 [^pZ4DIH2BVqg]

> it's doing. It sounds off because of how it's explaining itself to me. It's
> — 12:41 [^pmoDeA3RBZY]

Source analysis [^sOB3HSiG8vo]; no independently matched timestamped quote published.

> been trying to um into your goal, but instead have very concrete and very
> — 18:39 [^shRR1e2HXMk]

> we want to pass through to the human, right? So low confidence is a valid
> — 1:33:52 [^sn79oS4MZFI]

> would be very bad for your token usage. So always set a max iterations of how
> — 03:08 [^uiP88SpCi1Q]

> just to see how important is the validation as well. it takes even 40% of
> — 12:35 [^vGCJ7diEtrw]

> The key questions are, can we find something we can measure? Can we apply
> — 09:00 [^xIt_mTQp6mY]

> holds the amount of patience that the harness will get with the model.
> — 56:44 [^xs-ob87TTzg]

> the validations in one shot send it back to the language model and try again
> — 08:22 [^yj-wSRJwrrc]

Source analysis [^z0sh8HyTrDo]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^17-YSUHo6Lk]: [Building Blocks for Uber’s Software Factory— Uday Kiran Medisetty & Adam Huda, Uber](https://www.youtube.com/watch?v=17-YSUHo6Lk); publication: 2026-08-21T13:00:06Z; analysis: `analysis/17-YSUHo6Lk.json`.
[^31GUkCBD-Uc]: [Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber](https://www.youtube.com/watch?v=31GUkCBD-Uc); publication: 2026-07-24T22:00:25Z; analysis: `analysis/31GUkCBD-Uc.json`.
[^33Oct2hqGnk]: [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](https://www.youtube.com/watch?v=33Oct2hqGnk); publication: 2026-10-04T21:00:13Z; analysis: `analysis/33Oct2hqGnk.json`.
[^72XxWkd8Jrk]: [Effective agent design patterns in production — Laurie Voss, LlamaIndex](https://www.youtube.com/watch?v=72XxWkd8Jrk); publication: 2025-06-27T10:22:56Z; analysis: `analysis/72XxWkd8Jrk.json`.
[^7c9FSUVcXR0]: [Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta](https://www.youtube.com/watch?v=7c9FSUVcXR0); publication: 2026-09-19T15:00:10Z; analysis: `analysis/7c9FSUVcXR0.json`.
[^APh1Vx0oLmQ]: [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](https://www.youtube.com/watch?v=APh1Vx0oLmQ); publication: 2026-06-29T02:00:28Z; analysis: `analysis/APh1Vx0oLmQ.json`.
[^C_GG5g38vLU]: [Harnesses in AI: A Deep Dive — Tejas Kumar, IBM](https://www.youtube.com/watch?v=C_GG5g38vLU); publication: 2026-05-17T17:30:06Z; analysis: `analysis/C_GG5g38vLU.json`.
[^Djv8Sp11UjI]: [The Current State of Browser Agents - Jerry Wu and Wyatt Marshall](https://www.youtube.com/watch?v=Djv8Sp11UjI); publication: 2025-06-03T22:22:26Z; analysis: `analysis/Djv8Sp11UjI.json`.
[^EnT4Wej5M5k]: [The Benchmarks Game: Why It's Rigged and How You Can (Really) Win - Darius Emrani](https://www.youtube.com/watch?v=EnT4Wej5M5k); publication: 2025-06-03T22:22:25Z; analysis: `analysis/EnT4Wej5M5k.json`.
[^FlzpEGHNVKQ]: [Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take](https://www.youtube.com/watch?v=FlzpEGHNVKQ); publication: 2026-05-13T15:00:06Z; analysis: `analysis/FlzpEGHNVKQ.json`.
[^GJX19pNhmSw]: [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](https://www.youtube.com/watch?v=GJX19pNhmSw); publication: 2026-08-22T14:30:07Z; analysis: `analysis/GJX19pNhmSw.json`.
[^KA5kPbdkK2E]: [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](https://www.youtube.com/watch?v=KA5kPbdkK2E); publication: 2026-06-02T16:00:33Z; analysis: `analysis/KA5kPbdkK2E.json`.
[^KtBivPzmOM8]: [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](https://www.youtube.com/watch?v=KtBivPzmOM8); publication: 2026-10-17T07:00:25Z; analysis: `analysis/KtBivPzmOM8.json`.
[^LqLoYksJ6do]: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](https://www.youtube.com/watch?v=LqLoYksJ6do); publication: 2026-07-20T17:17:53Z; analysis: `analysis/LqLoYksJ6do.json`.
[^Lqq_LcBaJCc]: [How agents will unlock the $500B promise of AI - Donald Hruska, Retool](https://www.youtube.com/watch?v=Lqq_LcBaJCc); publication: 2025-07-23T15:51:38Z; analysis: `analysis/Lqq_LcBaJCc.json`.
[^MhHEGMFCEB0]: [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](https://www.youtube.com/watch?v=MhHEGMFCEB0); publication: 2026-04-29T16:00:06Z; analysis: `analysis/MhHEGMFCEB0.json`.
[^MpZzWMdmQCE]: [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](https://www.youtube.com/watch?v=MpZzWMdmQCE); publication: 2026-07-08T08:31:41Z; analysis: `analysis/MpZzWMdmQCE.json`.
[^NaOkR3VSfR4]: [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](https://www.youtube.com/watch?v=NaOkR3VSfR4); publication: 2026-10-08T22:30:09Z; analysis: `analysis/NaOkR3VSfR4.json`.
[^OC04sP_QgTI]: [Ensure AI Agents Work: Evaluation Frameworks for Scaling Success — Aparna Dhinkaran, CEO Arize](https://www.youtube.com/watch?v=OC04sP_QgTI); publication: 2025-04-23T16:00:06Z; analysis: `analysis/OC04sP_QgTI.json`.
[^OD13PiXw60o]: [Building Multi agent Systems with Finite State Machines](https://www.youtube.com/watch?v=OD13PiXw60o); publication: 2025-02-22T17:00:05Z; analysis: `analysis/OD13PiXw60o.json`.
[^ORVh4GivEU0]: [Beyond RAG: A Relational Context Engine That Cuts Token Burn — Unblocked](https://www.youtube.com/watch?v=ORVh4GivEU0); publication: 2026-10-10T19:30:39Z; analysis: `analysis/ORVh4GivEU0.json`.
[^ObTPqBGsEbA]: [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA); publication: 2026-06-18T13:00:06Z; analysis: `analysis/ObTPqBGsEbA.json`.
[^PXj0p_mW9nI]: [Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic](https://www.youtube.com/watch?v=PXj0p_mW9nI); publication: 2026-09-14T14:00:06Z; analysis: `analysis/PXj0p_mW9nI.json`.
[^QSeaZ6qHyXs]: [Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic](https://www.youtube.com/watch?v=QSeaZ6qHyXs); publication: 2026-10-12T06:07:45Z; analysis: `analysis/QSeaZ6qHyXs.json`.
[^Qvp9vw4jJQ8]: [Break It 'Til You Make It: Building the Self-Improving Stack for AI Agents - Aparna Dhinakaran](https://www.youtube.com/watch?v=Qvp9vw4jJQ8); publication: 2025-06-10T17:30:11Z; analysis: `analysis/Qvp9vw4jJQ8.json`.
[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^Sir59K8ZDPU]: [Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Sir59K8ZDPU); publication: 2026-07-23T01:00:07Z; analysis: `analysis/Sir59K8ZDPU.json`.
[^TeGsFFNqRLA]: [Fast Models Need Slow Developers — Sarah Chieng, Cerebras](https://www.youtube.com/watch?v=TeGsFFNqRLA); publication: 2026-05-22T18:00:06Z; analysis: `analysis/TeGsFFNqRLA.json`.
[^Ti-BmGU1_mQ]: [The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI](https://www.youtube.com/watch?v=Ti-BmGU1_mQ); publication: 2026-10-17T09:00:27Z; analysis: `analysis/Ti-BmGU1_mQ.json`.
[^U3MVU6JpocU]: [AI Agents, Meet Test Driven Development](https://www.youtube.com/watch?v=U3MVU6JpocU); publication: 2025-02-22T22:05:15Z; analysis: `analysis/U3MVU6JpocU.json`.
[^VaS2h-dY1-4]: [Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw](https://www.youtube.com/watch?v=VaS2h-dY1-4); publication: 2026-05-21T15:00:06Z; analysis: `analysis/VaS2h-dY1-4.json`.
[^Ve-akpov78Q]: [Code Generation and Maintenance at Scale: Morgante Pell](https://www.youtube.com/watch?v=Ve-akpov78Q); publication: 2024-10-17T18:52:20Z; analysis: `analysis/Ve-akpov78Q.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^YXiLj4tJt5A]: [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](https://www.youtube.com/watch?v=YXiLj4tJt5A); publication: 2026-10-11T15:00:05Z; analysis: `analysis/YXiLj4tJt5A.json`.
[^ZpK5PWX2YRM]: [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](https://www.youtube.com/watch?v=ZpK5PWX2YRM); publication: 2026-07-10T18:00:06Z; analysis: `analysis/ZpK5PWX2YRM.json`.
[^_-oIuRH4oGA]: [How agents broke app-level infrastructure - Evan Boyle](https://www.youtube.com/watch?v=_-oIuRH4oGA); publication: 2025-06-03T22:22:28Z; analysis: `analysis/_-oIuRH4oGA.json`.
[^atwSCxWFVMg]: [GPT Web App Generator - 10,000 apps created in a month: Matija Sosic](https://www.youtube.com/watch?v=atwSCxWFVMg); publication: 2024-01-26T20:51:42Z; analysis: `analysis/atwSCxWFVMg.json`.
[^b_PmGocP4rc]: [Evaling Video Slop — Maor Bril, Character.ai](https://www.youtube.com/watch?v=b_PmGocP4rc); publication: 2026-07-25T00:00:02Z; analysis: `analysis/b_PmGocP4rc.json`.
[^bjNYEc908oQ]: [Building Reliable Agentic Systems: Eno Reyes](https://www.youtube.com/watch?v=bjNYEc908oQ); publication: 2024-08-20T13:44:51Z; analysis: `analysis/bjNYEc908oQ.json`.
[^c35YoMdnI78]: [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78); publication: 2026-07-17T21:00:06Z; analysis: `analysis/c35YoMdnI78.json`.
[^d5EltXhbcfA]: [Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil](https://www.youtube.com/watch?v=d5EltXhbcfA); publication: 2025-04-17T16:00:06Z; analysis: `analysis/d5EltXhbcfA.json`.
[^eAXxdtNlK04]: [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=eAXxdtNlK04); publication: 2026-07-18T20:15:06Z; analysis: `analysis/eAXxdtNlK04.json`.
[^fLUtUkqYHnQ]: [Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI](https://www.youtube.com/watch?v=fLUtUkqYHnQ); publication: 2026-04-29T12:00:06Z; analysis: `analysis/fLUtUkqYHnQ.json`.
[^gEDl9C8s_-4]: [How to Train Your Agent: Building Reliable Agents with RL — Kyle Corbitt, OpenPipe](https://www.youtube.com/watch?v=gEDl9C8s_-4); publication: 2025-07-19T21:12:06Z; analysis: `analysis/gEDl9C8s_-4.json`.
[^il1c1a2FufU]: [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](https://www.youtube.com/watch?v=il1c1a2FufU); publication: 2026-07-24T15:00:06Z; analysis: `analysis/il1c1a2FufU.json`.
[^kDlqpN1JyIw]: [Vercel AI SDK Masterclass: From Fundamentals to Deep Research](https://www.youtube.com/watch?v=kDlqpN1JyIw); publication: 2025-04-20T21:39:01Z; analysis: `analysis/kDlqpN1JyIw.json`.
[^mYSRn6PC1mc]: [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](https://www.youtube.com/watch?v=mYSRn6PC1mc); publication: 2026-04-20T18:45:16Z; analysis: `analysis/mYSRn6PC1mc.json`.
[^o6U_2vd967Y]: [Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft](https://www.youtube.com/watch?v=o6U_2vd967Y); publication: 2026-07-30T00:00:06Z; analysis: `analysis/o6U_2vd967Y.json`.
[^o_LRtAomJCs]: [Human seeded Evals — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=o_LRtAomJCs); publication: 2025-07-25T07:00:06Z; analysis: `analysis/o_LRtAomJCs.json`.
[^ow1we5PzK-o]: [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](https://www.youtube.com/watch?v=ow1we5PzK-o); publication: 2026-05-06T15:00:06Z; analysis: `analysis/ow1we5PzK-o.json`.
[^pZ4DIH2BVqg]: [Pydantic is STILL all you need: Jason Liu](https://www.youtube.com/watch?v=pZ4DIH2BVqg); publication: 2024-09-06T17:07:06Z; analysis: `analysis/pZ4DIH2BVqg.json`.
[^pmoDeA3RBZY]: [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=pmoDeA3RBZY); publication: 2026-06-05T16:00:06Z; analysis: `analysis/pmoDeA3RBZY.json`.
[^sOB3HSiG8vo]: [Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI](https://www.youtube.com/watch?v=sOB3HSiG8vo); publication: 2026-09-19T15:30:04Z; analysis: `analysis/sOB3HSiG8vo.json`.
[^shRR1e2HXMk]: [How Codex Works — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=shRR1e2HXMk); publication: 2026-08-10T16:00:06Z; analysis: `analysis/shRR1e2HXMk.json`.
[^sn79oS4MZFI]: [Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason](https://www.youtube.com/watch?v=sn79oS4MZFI); publication: 2025-06-22T16:00:06Z; analysis: `analysis/sn79oS4MZFI.json`.
[^uiP88SpCi1Q]: [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](https://www.youtube.com/watch?v=uiP88SpCi1Q); publication: 2026-06-28T22:00:14Z; analysis: `analysis/uiP88SpCi1Q.json`.
[^vGCJ7diEtrw]: [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](https://www.youtube.com/watch?v=vGCJ7diEtrw); publication: 2026-09-27T15:00:02Z; analysis: `analysis/vGCJ7diEtrw.json`.
[^xIt_mTQp6mY]: [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](https://www.youtube.com/watch?v=xIt_mTQp6mY); publication: 2026-07-25T20:41:40Z; analysis: `analysis/xIt_mTQp6mY.json`.
[^xs-ob87TTzg]: [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](https://www.youtube.com/watch?v=xs-ob87TTzg); publication: 2026-09-18T16:00:11Z; analysis: `analysis/xs-ob87TTzg.json`.
[^yj-wSRJwrrc]: [Pydantic is all you need: Jason Liu](https://www.youtube.com/watch?v=yj-wSRJwrrc); publication: 2023-11-01T16:27:08Z; analysis: `analysis/yj-wSRJwrrc.json`.
[^z0sh8HyTrDo]: [Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](https://www.youtube.com/watch?v=z0sh8HyTrDo); publication: 2026-07-30T03:00:06Z; analysis: `analysis/z0sh8HyTrDo.json`.
