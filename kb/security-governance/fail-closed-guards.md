---
{
  "type": "technique",
  "id": "fail-closed-guards",
  "title": "Fail closed on missing evidence, invalid state and policy-check errors",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-09-10T14:30:11Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "I3znWC3MEXM",
      "resource": "https://www.youtube.com/watch?v=I3znWC3MEXM",
      "title": "It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard",
      "author": "Kim Maida, Keycard",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/I3znWC3MEXM.json"
    },
    {
      "id": "JvKO40CFq-s",
      "resource": "https://www.youtube.com/watch?v=JvKO40CFq-s",
      "title": "Full Workshop: Better Auth — Paola Estefania, Better Auth",
      "author": "Paola Estefania, Better Auth",
      "last_modified": "2026-07-21T23:43:54Z",
      "analysis_file": "analysis/JvKO40CFq-s.json"
    },
    {
      "id": "NW-jwOVr32w",
      "resource": "https://www.youtube.com/watch?v=NW-jwOVr32w",
      "title": "The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI",
      "author": "Jonathan Gordon, ReWeaver AI",
      "last_modified": "2026-09-10T14:30:11Z",
      "analysis_file": "analysis/NW-jwOVr32w.json"
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
      "id": "WLXxTaPagA8",
      "resource": "https://www.youtube.com/watch?v=WLXxTaPagA8",
      "title": "Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony",
      "author": "Sumaiya Shrabony",
      "last_modified": "2026-07-11T16:30:04Z",
      "analysis_file": "analysis/WLXxTaPagA8.json"
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
      "id": "_Zcw_sVF6hU",
      "resource": "https://www.youtube.com/watch?v=_Zcw_sVF6hU",
      "title": "The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "author": "Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "last_modified": "2026-04-18T10:30:06Z",
      "analysis_file": "analysis/_Zcw_sVF6hU.json"
    },
    {
      "id": "_cVfz88_j7A",
      "resource": "https://www.youtube.com/watch?v=_cVfz88_j7A",
      "title": "Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs",
      "author": "Anant Shankhdhar, Risa Labs",
      "last_modified": "2026-07-20T06:24:47Z",
      "analysis_file": "analysis/_cVfz88_j7A.json"
    },
    {
      "id": "eSvXbb2EBYc",
      "resource": "https://www.youtube.com/watch?v=eSvXbb2EBYc",
      "title": "Building AI Products That Actually Work — Ben Hylak (Raindrop), Sid Bendre (Oleve)",
      "author": "Ben Hylak (Raindrop), Sid Bendre (Oleve)",
      "last_modified": "2025-07-24T17:15:06Z",
      "analysis_file": "analysis/eSvXbb2EBYc.json"
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
      "id": "pPvoLjYj_mY",
      "resource": "https://www.youtube.com/watch?v=pPvoLjYj_mY",
      "title": "Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer",
      "author": "Waseem Alshikh, Writer",
      "last_modified": "2025-04-22T16:00:06Z",
      "analysis_file": "analysis/pPvoLjYj_mY.json"
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

# Fail closed on missing evidence, invalid state and policy-check errors

## What

Fail closed on missing evidence, invalid state and policy-check errors

Models can keep answering when the required document is absent or entirely wrong; this should be an explicit admissibility case.

## Evidence

Source analysis [^I3znWC3MEXM]; no independently matched timestamped quote published.

Source analysis [^JvKO40CFq-s]; no independently matched timestamped quote published.

Source analysis [^NW-jwOVr32w]; no independently matched timestamped quote published.

> critical for this. and make sure that you're building trip wires and detectors
> — 15:02 [^R30col3UPUg]

> task. One day, it silently fails, but you haven't noticed for a week.
> — 02:21 [^WLXxTaPagA8]

> So, for safety bugs, when you're not sure, always hold and fix.
> — 16:02 [^YXEqC05WEI0]

> after 2 hours when I already wrote database records with wrong data.
> — 08:01 [^_Zcw_sVF6hU]

Source analysis [^_cVfz88_j7A]; no independently matched timestamped quote published.

Source analysis [^eSvXbb2EBYc]; no independently matched timestamped quote published.

Source analysis [^ij-AU9dpJjc]; no independently matched timestamped quote published.

Source analysis [^pPvoLjYj_mY]; no independently matched timestamped quote published.

> worst case that you can live with.
> — 10:57 [^zrZ1amZBSPw]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^I3znWC3MEXM]: [It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard](https://www.youtube.com/watch?v=I3znWC3MEXM); publication: 2026-07-20T17:17:53Z; analysis: `analysis/I3znWC3MEXM.json`.
[^JvKO40CFq-s]: [Full Workshop: Better Auth — Paola Estefania, Better Auth](https://www.youtube.com/watch?v=JvKO40CFq-s); publication: 2026-07-21T23:43:54Z; analysis: `analysis/JvKO40CFq-s.json`.
[^NW-jwOVr32w]: [The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI](https://www.youtube.com/watch?v=NW-jwOVr32w); publication: 2026-09-10T14:30:11Z; analysis: `analysis/NW-jwOVr32w.json`.
[^R30col3UPUg]: [Building Applications with AI Agents — Michael Albada, Microsoft](https://www.youtube.com/watch?v=R30col3UPUg); publication: 2025-07-24T15:00:53Z; analysis: `analysis/R30col3UPUg.json`.
[^WLXxTaPagA8]: [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](https://www.youtube.com/watch?v=WLXxTaPagA8); publication: 2026-07-11T16:30:04Z; analysis: `analysis/WLXxTaPagA8.json`.
[^YXEqC05WEI0]: [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](https://www.youtube.com/watch?v=YXEqC05WEI0); publication: 2026-08-19T14:30:18Z; analysis: `analysis/YXEqC05WEI0.json`.
[^_Zcw_sVF6hU]: [The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil](https://www.youtube.com/watch?v=_Zcw_sVF6hU); publication: 2026-04-18T10:30:06Z; analysis: `analysis/_Zcw_sVF6hU.json`.
[^_cVfz88_j7A]: [Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs](https://www.youtube.com/watch?v=_cVfz88_j7A); publication: 2026-07-20T06:24:47Z; analysis: `analysis/_cVfz88_j7A.json`.
[^eSvXbb2EBYc]: [Building AI Products That Actually Work — Ben Hylak (Raindrop), Sid Bendre (Oleve)](https://www.youtube.com/watch?v=eSvXbb2EBYc); publication: 2025-07-24T17:15:06Z; analysis: `analysis/eSvXbb2EBYc.json`.
[^ij-AU9dpJjc]: [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](https://www.youtube.com/watch?v=ij-AU9dpJjc); publication: 2026-06-26T20:00:35Z; analysis: `analysis/ij-AU9dpJjc.json`.
[^pPvoLjYj_mY]: [Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer](https://www.youtube.com/watch?v=pPvoLjYj_mY); publication: 2025-04-22T16:00:06Z; analysis: `analysis/pPvoLjYj_mY.json`.
[^zrZ1amZBSPw]: [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](https://www.youtube.com/watch?v=zrZ1amZBSPw); publication: 2026-08-28T15:30:03Z; analysis: `analysis/zrZ1amZBSPw.json`.
