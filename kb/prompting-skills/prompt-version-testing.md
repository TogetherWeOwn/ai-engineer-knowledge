---
{
  "type": "technique",
  "id": "prompt-version-testing",
  "title": "Version prompts and skills with regression fixtures and rollback",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-10-18T08:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-TiET_K-E_g",
      "resource": "https://www.youtube.com/watch?v=-TiET_K-E_g",
      "title": "From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google",
      "author": "Cormac Brick, Google",
      "last_modified": "2026-05-20T13:00:06Z",
      "analysis_file": "analysis/-TiET_K-E_g.json"
    },
    {
      "id": "1__V4KTv_Gw",
      "resource": "https://www.youtube.com/watch?v=1__V4KTv_Gw",
      "title": "The Build-Operate Divide: Bridging Product Vision and AI Operational Reality",
      "author": null,
      "last_modified": "2025-07-02T16:00:06Z",
      "analysis_file": "analysis/1__V4KTv_Gw.json"
    },
    {
      "id": "7taOQBfjDyE",
      "resource": "https://www.youtube.com/watch?v=7taOQBfjDyE",
      "title": "The Loop Is the Product — Roland Gavrilescu, Introspection",
      "author": "Roland Gavrilescu, Introspection",
      "last_modified": "2026-09-26T14:00:25Z",
      "analysis_file": "analysis/7taOQBfjDyE.json"
    },
    {
      "id": "89NuzmKokIk",
      "resource": "https://www.youtube.com/watch?v=89NuzmKokIk",
      "title": "Strategies for LLM Evals (GuideLLM, lm-eval-harness, OpenAI Evals Workshop) — Taylor Jordan Smith",
      "author": "Taylor Jordan Smith",
      "last_modified": "2025-07-27T16:15:06Z",
      "analysis_file": "analysis/89NuzmKokIk.json"
    },
    {
      "id": "BKWpYIWvAo4",
      "resource": "https://www.youtube.com/watch?v=BKWpYIWvAo4",
      "title": "TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google",
      "author": "Cormac Brick, Google",
      "last_modified": "2026-05-03T22:00:06Z",
      "analysis_file": "analysis/BKWpYIWvAo4.json"
    },
    {
      "id": "EAfP8pDs7h4",
      "resource": "https://www.youtube.com/watch?v=EAfP8pDs7h4",
      "title": "[Full Workshop] Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments",
      "author": null,
      "last_modified": "2025-06-27T10:19:00Z",
      "analysis_file": "analysis/EAfP8pDs7h4.json"
    },
    {
      "id": "FGftGOzfohc",
      "resource": "https://www.youtube.com/watch?v=FGftGOzfohc",
      "title": "Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T06:07:50Z",
      "analysis_file": "analysis/FGftGOzfohc.json"
    },
    {
      "id": "IAdZxqjZ45U",
      "resource": "https://www.youtube.com/watch?v=IAdZxqjZ45U",
      "title": "Optimizing LLMs in Insurance with DSPy: Jeronim Morina",
      "author": null,
      "last_modified": "2025-02-16T17:15:06Z",
      "analysis_file": "analysis/IAdZxqjZ45U.json"
    },
    {
      "id": "KGFyOtl5ktI",
      "resource": "https://www.youtube.com/watch?v=KGFyOtl5ktI",
      "title": "Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain",
      "author": "Jake Broekhuizen, LangChain",
      "last_modified": "2026-10-08T14:00:37Z",
      "analysis_file": "analysis/KGFyOtl5ktI.json"
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
      "id": "L2r6vLlLgs8",
      "resource": "https://www.youtube.com/watch?v=L2r6vLlLgs8",
      "title": "Fighting AI with AI — Lawrence Jones, Incident",
      "author": "Lawrence Jones, Incident",
      "last_modified": "2026-05-17T16:30:07Z",
      "analysis_file": "analysis/L2r6vLlLgs8.json"
    },
    {
      "id": "LC3-P7v3yoI",
      "resource": "https://www.youtube.com/watch?v=LC3-P7v3yoI",
      "title": "Skills are the New SDKs - Elvin Aghammadzada, DataRobot",
      "author": "Elvin Aghammadzada, DataRobot",
      "last_modified": "2026-07-20T06:24:53Z",
      "analysis_file": "analysis/LC3-P7v3yoI.json"
    },
    {
      "id": "M05vON8i0aI",
      "resource": "https://www.youtube.com/watch?v=M05vON8i0aI",
      "title": "AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack",
      "author": "Imad Touil, QuantumBlack",
      "last_modified": "2026-08-28T18:30:04Z",
      "analysis_file": "analysis/M05vON8i0aI.json"
    },
    {
      "id": "MC55hdWLq4o",
      "resource": "https://www.youtube.com/watch?v=MC55hdWLq4o",
      "title": "The Future of Evals - Ankur Goyal, Braintrust",
      "author": "Ankur Goyal, Braintrust",
      "last_modified": "2025-08-09T15:12:25Z",
      "analysis_file": "analysis/MC55hdWLq4o.json"
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
      "id": "NdrSPm6NCdk",
      "resource": "https://www.youtube.com/watch?v=NdrSPm6NCdk",
      "title": "Evals in AI: A Deep Dive — Tejas Kumar, IBM",
      "author": "Tejas Kumar, IBM",
      "last_modified": "2026-10-05T17:00:22Z",
      "analysis_file": "analysis/NdrSPm6NCdk.json"
    },
    {
      "id": "O72p-rBb2bA",
      "resource": "https://www.youtube.com/watch?v=O72p-rBb2bA",
      "title": "Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind",
      "author": "Akele Reed & Dave Revere, SonderMind",
      "last_modified": "2026-07-25T23:00:36Z",
      "analysis_file": "analysis/O72p-rBb2bA.json"
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
      "id": "QHBjufYK8TA",
      "resource": "https://www.youtube.com/watch?v=QHBjufYK8TA",
      "title": "The State of Model Routing — NVIDIA, Cognition, OpenRouter",
      "author": "NVIDIA, Cognition, OpenRouter",
      "last_modified": "2026-08-06T17:07:24Z",
      "analysis_file": "analysis/QHBjufYK8TA.json"
    },
    {
      "id": "R30col3UPUg",
      "resource": "https://www.youtube.com/watch?v=R30col3UPUg",
      "title": "Building Applications with AI Agents — Michael Albada, Microsoft",
      "author": "Michael Albada, Microsoft",
      "last_modified": "2025-07-24T15:00:53Z",
      "analysis_file": "analysis/R30col3UPUg.json"
    },
    {
      "id": "R3hTescenDw",
      "resource": "https://www.youtube.com/watch?v=R3hTescenDw",
      "title": "Which Jobs Can Be Replaced Today:  Fryderyk Wiatrowski and Peter Albert",
      "author": null,
      "last_modified": "2025-02-06T09:24:01Z",
      "analysis_file": "analysis/R3hTescenDw.json"
    },
    {
      "id": "SbcQYbrvAfI",
      "resource": "https://www.youtube.com/watch?v=SbcQYbrvAfI",
      "title": "Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize",
      "author": "SallyAnn DeLucia & Fuad Ali, Arize",
      "last_modified": "2026-01-06T17:30:06Z",
      "analysis_file": "analysis/SbcQYbrvAfI.json"
    },
    {
      "id": "TN3mj92oZ8I",
      "resource": "https://www.youtube.com/watch?v=TN3mj92oZ8I",
      "title": "Building Self-Improving Agent Software Factories — Suraj Gupta, Warp",
      "author": "Suraj Gupta, Warp",
      "last_modified": "2026-09-27T14:00:40Z",
      "analysis_file": "analysis/TN3mj92oZ8I.json"
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
      "id": "UNzCG3lw6O0",
      "resource": "https://www.youtube.com/watch?v=UNzCG3lw6O0",
      "title": "Building Great Agent Skills: The Missing Manual",
      "author": null,
      "last_modified": "2026-06-29T18:53:10Z",
      "analysis_file": "analysis/UNzCG3lw6O0.json"
    },
    {
      "id": "V_5bn4q-vAI",
      "resource": "https://www.youtube.com/watch?v=V_5bn4q-vAI",
      "title": "How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth",
      "author": "Christopher Burns, Inth",
      "last_modified": "2026-08-26T15:30:07Z",
      "analysis_file": "analysis/V_5bn4q-vAI.json"
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
      "id": "WLXxTaPagA8",
      "resource": "https://www.youtube.com/watch?v=WLXxTaPagA8",
      "title": "Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony",
      "author": "Sumaiya Shrabony",
      "last_modified": "2026-07-11T16:30:04Z",
      "analysis_file": "analysis/WLXxTaPagA8.json"
    },
    {
      "id": "X6l4lpA0_NY",
      "resource": "https://www.youtube.com/watch?v=X6l4lpA0_NY",
      "title": "Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl",
      "author": "Dru Knox, Tessl",
      "last_modified": "2026-10-06T15:30:27Z",
      "analysis_file": "analysis/X6l4lpA0_NY.json"
    },
    {
      "id": "XPj3mIKEtI4",
      "resource": "https://www.youtube.com/watch?v=XPj3mIKEtI4",
      "title": "Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j",
      "author": "Will Lyon, Neo4j",
      "last_modified": "2026-10-08T20:00:21Z",
      "analysis_file": "analysis/XPj3mIKEtI4.json"
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
      "id": "YYcNm2RexnY",
      "resource": "https://www.youtube.com/watch?v=YYcNm2RexnY",
      "title": "Lessons from building GenAI based applications — Juan Peredo",
      "author": "Juan Peredo",
      "last_modified": "2025-02-22T15:00:06Z",
      "analysis_file": "analysis/YYcNm2RexnY.json"
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
      "id": "aeTb5BdmTTc",
      "resource": "https://www.youtube.com/watch?v=aeTb5BdmTTc",
      "title": "Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab",
      "author": "Aditya Khandelwal, Amazon AGI Lab",
      "last_modified": "2026-08-11T00:03:17Z",
      "analysis_file": "analysis/aeTb5BdmTTc.json"
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
      "id": "coKKKKh8Vns",
      "resource": "https://www.youtube.com/watch?v=coKKKKh8Vns",
      "title": "How to run Evals at Scale: Thinking beyond Accuracy or Similarity — Muktesh Mishra, Adobe",
      "author": "Muktesh Mishra, Adobe",
      "last_modified": "2025-07-22T19:46:22Z",
      "analysis_file": "analysis/coKKKKh8Vns.json"
    },
    {
      "id": "eOxOzcw70f0",
      "resource": "https://www.youtube.com/watch?v=eOxOzcw70f0",
      "title": "Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison",
      "author": "Harald Kirschner, Christopher Harrison",
      "last_modified": "2025-08-03T04:30:57Z",
      "analysis_file": "analysis/eOxOzcw70f0.json"
    },
    {
      "id": "fOtTHWeU6B8",
      "resource": "https://www.youtube.com/watch?v=fOtTHWeU6B8",
      "title": "How Zapier Builds AI Products and Features with the Help of Braintrust: Ankur Goyal & Olmo Maldonado",
      "author": null,
      "last_modified": "2024-11-07T20:11:02Z",
      "analysis_file": "analysis/fOtTHWeU6B8.json"
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
      "id": "fiXjTif1nS4",
      "resource": "https://www.youtube.com/watch?v=fiXjTif1nS4",
      "title": "Best Practices for Evaluating Large Language Model Applications with llmeval: Niklas Nielsen",
      "author": null,
      "last_modified": "2025-02-05T11:18:34Z",
      "analysis_file": "analysis/fiXjTif1nS4.json"
    },
    {
      "id": "gpmze-6ueGU",
      "resource": "https://www.youtube.com/watch?v=gpmze-6ueGU",
      "title": "We Let Our Financial Planners Write the Agents — Matthew Ragone, Range",
      "author": "Matthew Ragone, Range",
      "last_modified": "2026-10-12T12:00:24Z",
      "analysis_file": "analysis/gpmze-6ueGU.json"
    },
    {
      "id": "hOWU0KPUp1k",
      "resource": "https://www.youtube.com/watch?v=hOWU0KPUp1k",
      "title": "Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley",
      "author": "Brendan Rappazzo, Morgan Stanley",
      "last_modified": "2026-09-14T15:00:19Z",
      "analysis_file": "analysis/hOWU0KPUp1k.json"
    },
    {
      "id": "iOXM3zE-2dk",
      "resource": "https://www.youtube.com/watch?v=iOXM3zE-2dk",
      "title": "Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft",
      "author": "Amy Boyd & Nitya Narasimhan, Microsoft",
      "last_modified": "2026-05-14T16:00:06Z",
      "analysis_file": "analysis/iOXM3zE-2dk.json"
    },
    {
      "id": "ij-AU9dpJjc",
      "resource": "https://www.youtube.com/watch?v=ij-AU9dpJjc",
      "title": "Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co",
      "author": "Isadora Martin-Dye, Isadora & Co",
      "last_modified": "2026-06-26T20:00:35Z",
      "analysis_file": "analysis/ij-AU9dpJjc.json"
    },
    {
      "id": "jHMiYtjoJfA",
      "resource": "https://www.youtube.com/watch?v=jHMiYtjoJfA",
      "title": "Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop",
      "author": "Ben Hylak, Raindrop",
      "last_modified": "2026-08-12T18:00:34Z",
      "analysis_file": "analysis/jHMiYtjoJfA.json"
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
      "id": "lY1iFbDPRlw",
      "resource": "https://www.youtube.com/watch?v=lY1iFbDPRlw",
      "title": "Minimax M2: Building the #1 Open Model – Olive Song, MiniMax",
      "author": "Olive Song, MiniMax",
      "last_modified": "2025-12-13T17:15:06Z",
      "analysis_file": "analysis/lY1iFbDPRlw.json"
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
      "id": "n9rjuBuShko",
      "resource": "https://www.youtube.com/watch?v=n9rjuBuShko",
      "title": "Building LinkedIn's GenAI Platform — Xiaofeng Wang",
      "author": "Xiaofeng Wang",
      "last_modified": "2025-04-16T16:00:06Z",
      "analysis_file": "analysis/n9rjuBuShko.json"
    },
    {
      "id": "o4scJaQgnFA",
      "resource": "https://www.youtube.com/watch?v=o4scJaQgnFA",
      "title": "From Arc to Dia: Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York",
      "author": "Samir Mody, The Browser Company of New York",
      "last_modified": "2025-12-19T18:15:46Z",
      "analysis_file": "analysis/o4scJaQgnFA.json"
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
      "id": "pFsfax19yOM",
      "resource": "https://www.youtube.com/watch?v=pFsfax19yOM",
      "title": "Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser",
      "author": "Nick Nisi and Zack Proser",
      "last_modified": "2026-05-06T17:00:06Z",
      "analysis_file": "analysis/pFsfax19yOM.json"
    },
    {
      "id": "pP_dSNz_EdQ",
      "resource": "https://www.youtube.com/watch?v=pP_dSNz_EdQ",
      "title": "The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize",
      "author": "Aparna Dhinakaran, Arize",
      "last_modified": "2025-12-23T17:00:06Z",
      "analysis_file": "analysis/pP_dSNz_EdQ.json"
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
      "id": "pmoDeA3RBZY",
      "resource": "https://www.youtube.com/watch?v=pmoDeA3RBZY",
      "title": "Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw",
      "author": "Vincent Koc, OpenClaw",
      "last_modified": "2026-06-05T16:00:06Z",
      "analysis_file": "analysis/pmoDeA3RBZY.json"
    },
    {
      "id": "pyvRID_CZZU",
      "resource": "https://www.youtube.com/watch?v=pyvRID_CZZU",
      "title": "We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI",
      "author": "AssemblyAI",
      "last_modified": "2026-10-04T15:00:15Z",
      "analysis_file": "analysis/pyvRID_CZZU.json"
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
      "id": "rnDm57Py54A",
      "resource": "https://www.youtube.com/watch?v=rnDm57Py54A",
      "title": "Building your own software factory — Eric Zakariasson, Cursor",
      "author": "Eric Zakariasson, Cursor",
      "last_modified": "2026-04-28T18:00:06Z",
      "analysis_file": "analysis/rnDm57Py54A.json"
    },
    {
      "id": "spvXj9tnWAQ",
      "resource": "https://www.youtube.com/watch?v=spvXj9tnWAQ",
      "title": "Engineering Better Evals: Scalable LLM Evaluation Pipelines That Work — Dat Ngo, Aman Khan, Arize",
      "author": "Dat Ngo, Aman Khan, Arize",
      "last_modified": "2025-06-27T10:49:38Z",
      "analysis_file": "analysis/spvXj9tnWAQ.json"
    },
    {
      "id": "uFPAtKIN-FQ",
      "resource": "https://www.youtube.com/watch?v=uFPAtKIN-FQ",
      "title": "Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri",
      "author": null,
      "last_modified": "2025-06-11T16:57:37Z",
      "analysis_file": "analysis/uFPAtKIN-FQ.json"
    },
    {
      "id": "uIiA6DquRiE",
      "resource": "https://www.youtube.com/watch?v=uIiA6DquRiE",
      "title": "Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth",
      "author": "Daniel Han, Unsloth",
      "last_modified": "2026-07-17T17:00:06Z",
      "analysis_file": "analysis/uIiA6DquRiE.json"
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
      "id": "v3Fr2JR47KA",
      "resource": "https://www.youtube.com/watch?v=v3Fr2JR47KA",
      "title": "The Future of MCP — David Soria Parra, Anthropic",
      "author": "David Soria Parra, Anthropic",
      "last_modified": "2026-04-19T15:00:06Z",
      "analysis_file": "analysis/v3Fr2JR47KA.json"
    },
    {
      "id": "vNCY9kXXyDQ",
      "resource": "https://www.youtube.com/watch?v=vNCY9kXXyDQ",
      "title": "Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse",
      "author": "Marc Klingen, Clickhouse",
      "last_modified": "2026-05-20T15:00:06Z",
      "analysis_file": "analysis/vNCY9kXXyDQ.json"
    },
    {
      "id": "vy7o1g2iHY8",
      "resource": "https://www.youtube.com/watch?v=vy7o1g2iHY8",
      "title": "How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS",
      "author": "Nick Nisi, WorkOS",
      "last_modified": "2026-05-30T18:00:06Z",
      "analysis_file": "analysis/vy7o1g2iHY8.json"
    },
    {
      "id": "whue9_YquGA",
      "resource": "https://www.youtube.com/watch?v=whue9_YquGA",
      "title": "Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation",
      "author": "Angie Jones, Agentic AI Foundation",
      "last_modified": "2026-06-28T19:00:10Z",
      "analysis_file": "analysis/whue9_YquGA.json"
    },
    {
      "id": "wpOA-UXynoM",
      "resource": "https://www.youtube.com/watch?v=wpOA-UXynoM",
      "title": "How Forward Deployed Engineering is done at Factory — Eno Reyes",
      "author": "Eno Reyes",
      "last_modified": "2026-07-28T22:00:06Z",
      "analysis_file": "analysis/wpOA-UXynoM.json"
    },
    {
      "id": "zKk7sDMGDEQ",
      "resource": "https://www.youtube.com/watch?v=zKk7sDMGDEQ",
      "title": "Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer",
      "author": "Kuba Rogut, Turbopuffer",
      "last_modified": "2026-06-03T15:00:06Z",
      "analysis_file": "analysis/zKk7sDMGDEQ.json"
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

# Version prompts and skills with regression fixtures and rollback

## What

Version prompts and skills with regression fixtures and rollback

Keep a prompt's inputs, expected behavior and metric implementation together so a configuration change has a reproducible regression contract. Metrics can be ordinary code rather than another model call.

## Evidence

> Uh this works really well though. Uh so, you can use skills to write skills. So,
> — 09:14 [^-TiET_K-E_g]

Source analysis [^1__V4KTv_Gw]; no independently matched timestamped quote published.

Source analysis [^7taOQBfjDyE]; no independently matched timestamped quote published.

Source analysis [^89NuzmKokIk]; no independently matched timestamped quote published.

Source analysis [^BKWpYIWvAo4]; no independently matched timestamped quote published.

Source analysis [^EAfP8pDs7h4]; no independently matched timestamped quote published.

Source analysis [^FGftGOzfohc]; no independently matched timestamped quote published.

Source analysis [^IAdZxqjZ45U]; no independently matched timestamped quote published.

> become data sets to do offline evaluations and things like that.
> — 13:33 [^KGFyOtl5ktI]

Source analysis [^KtBivPzmOM8]; no independently matched timestamped quote published.

> And for us, evals live in YAML files right next to all to like our go
> — 04:25 [^L2r6vLlLgs8]

> turn up, and it will create an eval case where it proves that the thing is failed
> — 07:40 [^L2r6vLlLgs8]

> should actually start versioning them, evaluating and testing them, and
> — 26:27 [^LC3-P7v3yoI]

> skills as well. You have the versioning uh and and life cycle. So you understand
> — 14:14 [^M05vON8i0aI]

> that have a catalog with metadata in it that's actually can discover skills and
> — 13:54 [^M05vON8i0aI]

Source analysis [^MC55hdWLq4o]; no independently matched timestamped quote published.

> changes alone have been seen to swing a benchmark by 76 percentage points. And
> — 11:37 [^McknwOzbmyg]

> deterministic because I write them right and so there's no room for eval there.
> — 57:22 [^NdrSPm6NCdk]

Source analysis [^O72p-rBb2bA]; no independently matched timestamped quote published.

Source analysis [^ObTPqBGsEbA]; no independently matched timestamped quote published.

> rerun the the test as a regression, make sure make sure it changes. Like it's a
> — 42:55 [^QHBjufYK8TA]

> type of clustering and summarization on those outputs and you can suggest
> — 11:20 [^R30col3UPUg]

Source analysis [^R3hTescenDw]; no independently matched timestamped quote published.

Source analysis [^SbcQYbrvAfI]; no independently matched timestamped quote published.

Source analysis [^TN3mj92oZ8I]; no independently matched timestamped quote published.

Source analysis [^U3MVU6JpocU]; no independently matched timestamped quote published.

> resource to another, the model may just choose not to follow it, you know, even
> — 06:44 [^UNzCG3lw6O0]

Source analysis [^V_5bn4q-vAI]; no independently matched timestamped quote published.

> um without you having to update your Cursor version. Um
> — 08:52 [^WE_Gnowy3uw]

Source analysis [^WLXxTaPagA8]; no independently matched timestamped quote published.

> have a skills registry where you can publish and version the workflows and
> — 16:48 [^X6l4lpA0_NY]

> deterministic. Um we're really only leveraging an LLM here uh for
> — 13:19 [^XPj3mIKEtI4]

> that underlying data changes, is removed or uh becomes uh contradictory.
> — 14:08 [^XPj3mIKEtI4]

> uh having sort of like a governed skills registry that allows us to retrieve uh
> — 11:57 [^XPj3mIKEtI4]

> instructions in a different order, it can suddenly make the model much worse
> — 20:03 [^XzJD1bvXKjs]

Source analysis [^YYcNm2RexnY]; no independently matched timestamped quote published.

Source analysis [^ZdheJTfLu-s]; no independently matched timestamped quote published.

> across. Make sure that that's kind of a shared setup.
> — 09:43 [^aeTb5BdmTTc]

> Then hopefully we test the context. We distribute context maybe to some
> — 03:26 [^bSG9wUYaHWU]

Source analysis [^coKKKKh8Vns]; no independently matched timestamped quote published.

Source analysis [^eOxOzcw70f0]; no independently matched timestamped quote published.

> in some ways we we had prompts that were too fine-tuned to GP 3.5 turbo so we had
> — 12:42 [^fOtTHWeU6B8]

> optimize one step at a time. You want to isolate one variable per prompt variant
> — 21:18 [^fWXJM-J0ZB8]

Source analysis [^fiXjTif1nS4]; no independently matched timestamped quote published.

Source analysis [^gpmze-6ueGU]; no independently matched timestamped quote published.

Source analysis [^hOWU0KPUp1k]; no independently matched timestamped quote published.

Source analysis [^iOXM3zE-2dk]; no independently matched timestamped quote published.

> this talk. It's a single entry point. Every narrator goes through it to
> — 03:41 [^ij-AU9dpJjc]

Source analysis [^jHMiYtjoJfA]; no independently matched timestamped quote published.

> prompts. see if your scores are going down on your on your test set. So again,
> — 39:04 [^jxrGodnopHo]

Source analysis [^lY1iFbDPRlw]; no independently matched timestamped quote published.

> to distribute this at scale. And MP servers so- solve that problem. And
> — 1:32:37 [^mYSRn6PC1mc]

Source analysis [^n9rjuBuShko]; no independently matched timestamped quote published.

Source analysis [^o4scJaQgnFA]; no independently matched timestamped quote published.

> going to run the eval gates to tell me if I'm passing or failing any of the
> — 37:15 [^obfPzbapMIM]

> essentially do routing and determine if this skill is relevant to the task that
> — 08:09 [^pFsfax19yOM]

Source analysis [^pP_dSNz_EdQ]; no independently matched timestamped quote published.

Source analysis [^pj_hKFhnJCw]; no independently matched timestamped quote published.

> uh 2 weeks. Go through the Codex sessions, read the logs, make
> — 13:59 [^pmoDeA3RBZY]

Source analysis [^pyvRID_CZZU]; no independently matched timestamped quote published.

> evals pass. Um and second, you should tell it to find themes and not chase
> — 1:47:27 [^qZj7sqmidqA]

> in your eval results. Uh so you should version them. You should test them on
> — 1:17:59 [^qZj7sqmidqA]

> the same principles and apply that to the tools we're building as well and
> — 37:02 [^rnDm57Py54A]

Source analysis [^spvXj9tnWAQ]; no independently matched timestamped quote published.

Source analysis [^uFPAtKIN-FQ]; no independently matched timestamped quote published.

Source analysis [^uIiA6DquRiE]; no independently matched timestamped quote published.

> So, it's only our uh most frontier models that have this 80% token decrease
> — 25:20 [^uU5Gv2h8-9g]

Source analysis [^v3Fr2JR47KA]; no independently matched timestamped quote published.

> is how do I know whether it's out of date? So I think so just like time
> — 23:25 [^vNCY9kXXyDQ]

Source analysis [^vy7o1g2iHY8]; no independently matched timestamped quote published.

Source analysis [^whue9_YquGA]; no independently matched timestamped quote published.

> for the other 60% some of them involve workflow changes. Sometimes humans are
> — 13:30 [^wpOA-UXynoM]

Source analysis [^zKk7sDMGDEQ]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-TiET_K-E_g]: [From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google](https://www.youtube.com/watch?v=-TiET_K-E_g); publication: 2026-05-20T13:00:06Z; analysis: `analysis/-TiET_K-E_g.json`.
[^1__V4KTv_Gw]: [The Build-Operate Divide: Bridging Product Vision and AI Operational Reality](https://www.youtube.com/watch?v=1__V4KTv_Gw); publication: 2025-07-02T16:00:06Z; analysis: `analysis/1__V4KTv_Gw.json`.
[^7taOQBfjDyE]: [The Loop Is the Product — Roland Gavrilescu, Introspection](https://www.youtube.com/watch?v=7taOQBfjDyE); publication: 2026-09-26T14:00:25Z; analysis: `analysis/7taOQBfjDyE.json`.
[^89NuzmKokIk]: [Strategies for LLM Evals (GuideLLM, lm-eval-harness, OpenAI Evals Workshop) — Taylor Jordan Smith](https://www.youtube.com/watch?v=89NuzmKokIk); publication: 2025-07-27T16:15:06Z; analysis: `analysis/89NuzmKokIk.json`.
[^BKWpYIWvAo4]: [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google](https://www.youtube.com/watch?v=BKWpYIWvAo4); publication: 2026-05-03T22:00:06Z; analysis: `analysis/BKWpYIWvAo4.json`.
[^EAfP8pDs7h4]: [[Full Workshop] Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments](https://www.youtube.com/watch?v=EAfP8pDs7h4); publication: 2025-06-27T10:19:00Z; analysis: `analysis/EAfP8pDs7h4.json`.
[^FGftGOzfohc]: [Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](https://www.youtube.com/watch?v=FGftGOzfohc); publication: 2026-10-12T06:07:50Z; analysis: `analysis/FGftGOzfohc.json`.
[^IAdZxqjZ45U]: [Optimizing LLMs in Insurance with DSPy: Jeronim Morina](https://www.youtube.com/watch?v=IAdZxqjZ45U); publication: 2025-02-16T17:15:06Z; analysis: `analysis/IAdZxqjZ45U.json`.
[^KGFyOtl5ktI]: [Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain](https://www.youtube.com/watch?v=KGFyOtl5ktI); publication: 2026-10-08T14:00:37Z; analysis: `analysis/KGFyOtl5ktI.json`.
[^KtBivPzmOM8]: [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](https://www.youtube.com/watch?v=KtBivPzmOM8); publication: 2026-10-17T07:00:25Z; analysis: `analysis/KtBivPzmOM8.json`.
[^L2r6vLlLgs8]: [Fighting AI with AI — Lawrence Jones, Incident](https://www.youtube.com/watch?v=L2r6vLlLgs8); publication: 2026-05-17T16:30:07Z; analysis: `analysis/L2r6vLlLgs8.json`.
[^LC3-P7v3yoI]: [Skills are the New SDKs - Elvin Aghammadzada, DataRobot](https://www.youtube.com/watch?v=LC3-P7v3yoI); publication: 2026-07-20T06:24:53Z; analysis: `analysis/LC3-P7v3yoI.json`.
[^M05vON8i0aI]: [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](https://www.youtube.com/watch?v=M05vON8i0aI); publication: 2026-08-28T18:30:04Z; analysis: `analysis/M05vON8i0aI.json`.
[^MC55hdWLq4o]: [The Future of Evals - Ankur Goyal, Braintrust](https://www.youtube.com/watch?v=MC55hdWLq4o); publication: 2025-08-09T15:12:25Z; analysis: `analysis/MC55hdWLq4o.json`.
[^McknwOzbmyg]: [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](https://www.youtube.com/watch?v=McknwOzbmyg); publication: 2026-08-19T15:00:31Z; analysis: `analysis/McknwOzbmyg.json`.
[^NdrSPm6NCdk]: [Evals in AI: A Deep Dive — Tejas Kumar, IBM](https://www.youtube.com/watch?v=NdrSPm6NCdk); publication: 2026-10-05T17:00:22Z; analysis: `analysis/NdrSPm6NCdk.json`.
[^O72p-rBb2bA]: [Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind](https://www.youtube.com/watch?v=O72p-rBb2bA); publication: 2026-07-25T23:00:36Z; analysis: `analysis/O72p-rBb2bA.json`.
[^ObTPqBGsEbA]: [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA); publication: 2026-06-18T13:00:06Z; analysis: `analysis/ObTPqBGsEbA.json`.
[^QHBjufYK8TA]: [The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA); publication: 2026-08-06T17:07:24Z; analysis: `analysis/QHBjufYK8TA.json`.
[^R30col3UPUg]: [Building Applications with AI Agents — Michael Albada, Microsoft](https://www.youtube.com/watch?v=R30col3UPUg); publication: 2025-07-24T15:00:53Z; analysis: `analysis/R30col3UPUg.json`.
[^R3hTescenDw]: [Which Jobs Can Be Replaced Today:  Fryderyk Wiatrowski and Peter Albert](https://www.youtube.com/watch?v=R3hTescenDw); publication: 2025-02-06T09:24:01Z; analysis: `analysis/R3hTescenDw.json`.
[^SbcQYbrvAfI]: [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](https://www.youtube.com/watch?v=SbcQYbrvAfI); publication: 2026-01-06T17:30:06Z; analysis: `analysis/SbcQYbrvAfI.json`.
[^TN3mj92oZ8I]: [Building Self-Improving Agent Software Factories — Suraj Gupta, Warp](https://www.youtube.com/watch?v=TN3mj92oZ8I); publication: 2026-09-27T14:00:40Z; analysis: `analysis/TN3mj92oZ8I.json`.
[^U3MVU6JpocU]: [AI Agents, Meet Test Driven Development](https://www.youtube.com/watch?v=U3MVU6JpocU); publication: 2025-02-22T22:05:15Z; analysis: `analysis/U3MVU6JpocU.json`.
[^UNzCG3lw6O0]: [Building Great Agent Skills: The Missing Manual](https://www.youtube.com/watch?v=UNzCG3lw6O0); publication: 2026-06-29T18:53:10Z; analysis: `analysis/UNzCG3lw6O0.json`.
[^V_5bn4q-vAI]: [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](https://www.youtube.com/watch?v=V_5bn4q-vAI); publication: 2026-08-26T15:30:07Z; analysis: `analysis/V_5bn4q-vAI.json`.
[^WE_Gnowy3uw]: [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](https://www.youtube.com/watch?v=WE_Gnowy3uw); publication: 2026-04-30T12:00:06Z; analysis: `analysis/WE_Gnowy3uw.json`.
[^WLXxTaPagA8]: [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](https://www.youtube.com/watch?v=WLXxTaPagA8); publication: 2026-07-11T16:30:04Z; analysis: `analysis/WLXxTaPagA8.json`.
[^X6l4lpA0_NY]: [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](https://www.youtube.com/watch?v=X6l4lpA0_NY); publication: 2026-10-06T15:30:27Z; analysis: `analysis/X6l4lpA0_NY.json`.
[^XPj3mIKEtI4]: [Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j](https://www.youtube.com/watch?v=XPj3mIKEtI4); publication: 2026-10-08T20:00:21Z; analysis: `analysis/XPj3mIKEtI4.json`.
[^XzJD1bvXKjs]: [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=XzJD1bvXKjs); publication: 2026-09-09T15:00:06Z; analysis: `analysis/XzJD1bvXKjs.json`.
[^YYcNm2RexnY]: [Lessons from building GenAI based applications — Juan Peredo](https://www.youtube.com/watch?v=YYcNm2RexnY); publication: 2025-02-22T15:00:06Z; analysis: `analysis/YYcNm2RexnY.json`.
[^ZdheJTfLu-s]: [Shipping complex AI applications — Braintrust & Trainline](https://www.youtube.com/watch?v=ZdheJTfLu-s); publication: 2026-05-01T14:00:06Z; analysis: `analysis/ZdheJTfLu-s.json`.
[^aeTb5BdmTTc]: [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](https://www.youtube.com/watch?v=aeTb5BdmTTc); publication: 2026-08-11T00:03:17Z; analysis: `analysis/aeTb5BdmTTc.json`.
[^bSG9wUYaHWU]: [Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU); publication: 2026-05-03T14:00:06Z; analysis: `analysis/bSG9wUYaHWU.json`.
[^coKKKKh8Vns]: [How to run Evals at Scale: Thinking beyond Accuracy or Similarity — Muktesh Mishra, Adobe](https://www.youtube.com/watch?v=coKKKKh8Vns); publication: 2025-07-22T19:46:22Z; analysis: `analysis/coKKKKh8Vns.json`.
[^eOxOzcw70f0]: [Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](https://www.youtube.com/watch?v=eOxOzcw70f0); publication: 2025-08-03T04:30:57Z; analysis: `analysis/eOxOzcw70f0.json`.
[^fOtTHWeU6B8]: [How Zapier Builds AI Products and Features with the Help of Braintrust: Ankur Goyal & Olmo Maldonado](https://www.youtube.com/watch?v=fOtTHWeU6B8); publication: 2024-11-07T20:11:02Z; analysis: `analysis/fOtTHWeU6B8.json`.
[^fWXJM-J0ZB8]: [Frontier results, on device - RL Nabors, Arize](https://www.youtube.com/watch?v=fWXJM-J0ZB8); publication: 2026-06-29T03:30:03Z; analysis: `analysis/fWXJM-J0ZB8.json`.
[^fiXjTif1nS4]: [Best Practices for Evaluating Large Language Model Applications with llmeval: Niklas Nielsen](https://www.youtube.com/watch?v=fiXjTif1nS4); publication: 2025-02-05T11:18:34Z; analysis: `analysis/fiXjTif1nS4.json`.
[^gpmze-6ueGU]: [We Let Our Financial Planners Write the Agents — Matthew Ragone, Range](https://www.youtube.com/watch?v=gpmze-6ueGU); publication: 2026-10-12T12:00:24Z; analysis: `analysis/gpmze-6ueGU.json`.
[^hOWU0KPUp1k]: [Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley](https://www.youtube.com/watch?v=hOWU0KPUp1k); publication: 2026-09-14T15:00:19Z; analysis: `analysis/hOWU0KPUp1k.json`.
[^iOXM3zE-2dk]: [Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft](https://www.youtube.com/watch?v=iOXM3zE-2dk); publication: 2026-05-14T16:00:06Z; analysis: `analysis/iOXM3zE-2dk.json`.
[^ij-AU9dpJjc]: [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](https://www.youtube.com/watch?v=ij-AU9dpJjc); publication: 2026-06-26T20:00:35Z; analysis: `analysis/ij-AU9dpJjc.json`.
[^jHMiYtjoJfA]: [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](https://www.youtube.com/watch?v=jHMiYtjoJfA); publication: 2026-08-12T18:00:34Z; analysis: `analysis/jHMiYtjoJfA.json`.
[^jxrGodnopHo]: [[Full Workshop] Building Metrics that actually work — David Karam, Pi Labs (fmr Google Search)](https://www.youtube.com/watch?v=jxrGodnopHo); publication: 2025-07-29T00:29:21Z; analysis: `analysis/jxrGodnopHo.json`.
[^lY1iFbDPRlw]: [Minimax M2: Building the #1 Open Model – Olive Song, MiniMax](https://www.youtube.com/watch?v=lY1iFbDPRlw); publication: 2025-12-13T17:15:06Z; analysis: `analysis/lY1iFbDPRlw.json`.
[^mYSRn6PC1mc]: [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](https://www.youtube.com/watch?v=mYSRn6PC1mc); publication: 2026-04-20T18:45:16Z; analysis: `analysis/mYSRn6PC1mc.json`.
[^n9rjuBuShko]: [Building LinkedIn's GenAI Platform — Xiaofeng Wang](https://www.youtube.com/watch?v=n9rjuBuShko); publication: 2025-04-16T16:00:06Z; analysis: `analysis/n9rjuBuShko.json`.
[^o4scJaQgnFA]: [From Arc to Dia: Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York](https://www.youtube.com/watch?v=o4scJaQgnFA); publication: 2025-12-19T18:15:46Z; analysis: `analysis/o4scJaQgnFA.json`.
[^obfPzbapMIM]: [Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=obfPzbapMIM); publication: 2026-10-18T08:00:06Z; analysis: `analysis/obfPzbapMIM.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
[^pP_dSNz_EdQ]: [The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize](https://www.youtube.com/watch?v=pP_dSNz_EdQ); publication: 2025-12-23T17:00:06Z; analysis: `analysis/pP_dSNz_EdQ.json`.
[^pj_hKFhnJCw]: [How to evaluate a model for your use case: Emmanuel Turlay](https://www.youtube.com/watch?v=pj_hKFhnJCw); publication: 2025-02-05T11:18:34Z; analysis: `analysis/pj_hKFhnJCw.json`.
[^pmoDeA3RBZY]: [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=pmoDeA3RBZY); publication: 2026-06-05T16:00:06Z; analysis: `analysis/pmoDeA3RBZY.json`.
[^pyvRID_CZZU]: [We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](https://www.youtube.com/watch?v=pyvRID_CZZU); publication: 2026-10-04T15:00:15Z; analysis: `analysis/pyvRID_CZZU.json`.
[^qZj7sqmidqA]: [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=qZj7sqmidqA); publication: 2026-10-05T22:00:36Z; analysis: `analysis/qZj7sqmidqA.json`.
[^rnDm57Py54A]: [Building your own software factory — Eric Zakariasson, Cursor](https://www.youtube.com/watch?v=rnDm57Py54A); publication: 2026-04-28T18:00:06Z; analysis: `analysis/rnDm57Py54A.json`.
[^spvXj9tnWAQ]: [Engineering Better Evals: Scalable LLM Evaluation Pipelines That Work — Dat Ngo, Aman Khan, Arize](https://www.youtube.com/watch?v=spvXj9tnWAQ); publication: 2025-06-27T10:49:38Z; analysis: `analysis/spvXj9tnWAQ.json`.
[^uFPAtKIN-FQ]: [Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri](https://www.youtube.com/watch?v=uFPAtKIN-FQ); publication: 2025-06-11T16:57:37Z; analysis: `analysis/uFPAtKIN-FQ.json`.
[^uIiA6DquRiE]: [Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth](https://www.youtube.com/watch?v=uIiA6DquRiE); publication: 2026-07-17T17:00:06Z; analysis: `analysis/uIiA6DquRiE.json`.
[^uU5Gv2h8-9g]: [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](https://www.youtube.com/watch?v=uU5Gv2h8-9g); publication: 2026-07-15T15:05:06Z; analysis: `analysis/uU5Gv2h8-9g.json`.
[^v3Fr2JR47KA]: [The Future of MCP — David Soria Parra, Anthropic](https://www.youtube.com/watch?v=v3Fr2JR47KA); publication: 2026-04-19T15:00:06Z; analysis: `analysis/v3Fr2JR47KA.json`.
[^vNCY9kXXyDQ]: [Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse](https://www.youtube.com/watch?v=vNCY9kXXyDQ); publication: 2026-05-20T15:00:06Z; analysis: `analysis/vNCY9kXXyDQ.json`.
[^vy7o1g2iHY8]: [How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS](https://www.youtube.com/watch?v=vy7o1g2iHY8); publication: 2026-05-30T18:00:06Z; analysis: `analysis/vy7o1g2iHY8.json`.
[^whue9_YquGA]: [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](https://www.youtube.com/watch?v=whue9_YquGA); publication: 2026-06-28T19:00:10Z; analysis: `analysis/whue9_YquGA.json`.
[^wpOA-UXynoM]: [How Forward Deployed Engineering is done at Factory — Eno Reyes](https://www.youtube.com/watch?v=wpOA-UXynoM); publication: 2026-07-28T22:00:06Z; analysis: `analysis/wpOA-UXynoM.json`.
[^zKk7sDMGDEQ]: [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](https://www.youtube.com/watch?v=zKk7sDMGDEQ); publication: 2026-06-03T15:00:06Z; analysis: `analysis/zKk7sDMGDEQ.json`.
