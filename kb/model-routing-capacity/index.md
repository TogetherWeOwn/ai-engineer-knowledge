# model-routing-capacity

## Techniques and revisions

- [Reserve output capacity and detect reasoning-only exhaustion](answer-token-reserve.md) — `answer-token-reserve` (stable)
- [Reserve and settle approved capacity atomically across pooled accounts](budget-reservations.md) — `budget-reservations` (stable)
- [Use task- and harness-specific capability evidence as routing eligibility](capability-evidence-routing.md) — `capability-evidence-routing` (stable)
- [Use rules and classic ML baselines before LLM decision models](classic-ml-baseline.md) — `classic-ml-baseline` (stable)
- [Gate decision models with held-out lift, repeatability, abstention and drift exits](classifier-entry-exit.md) — `classifier-entry-exit` (stable)
- [Adopt a provider capability only when existing evidence and actual workload demand justify it](conditional-provider-adoption.md) — `conditional-provider-adoption` (stable)
- [Treat heterogeneous hardware or local inference as conditional optimization, not a purchase mandate](heterogeneous-inference.md) — `heterogeneous-inference` (stable)
- [Inventory stale model references and verify compatibility before any migration](model-id-inventory.md) — `model-id-inventory` (stable)
- [Optimize scheduling heuristics on existing traces and execute the selected policy deterministically](offline-scheduling-policy.md) — `offline-scheduling-policy` (stable)
- [Verify actual provider capability, limits and fallback behavior](provider-capability-contract.md) — `provider-capability-contract` (stable)
- [Keep resumable task state provider-neutral while preserving exact tool and instruction semantics](provider-neutral-continuation.md) — `provider-neutral-continuation` (stable)
- [Route residual semantic work by stage, risk and measured difficulty](risk-stage-routing.md) — `risk-stage-routing` (stable)
- [Prevent priority inversion and shed overload with resource-aware admission](scheduler-fairness.md) — `scheduler-fairness` (stable)
