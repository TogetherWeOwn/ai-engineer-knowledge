# cost-caching

## Techniques and revisions

- [Schedule delay-tolerant work for cheaper included capacity without adding a paid batch dependency](async-cheap-work.md) — `async-cheap-work` (stable)
- [Avoid redundant retrieval and context rereads when evidence is already valid](avoid-context-rereads.md) — `avoid-context-rereads` (stable)
- [Apply deterministic task budgets tied to progress rather than arbitrary context restrictions](budget-gates.md) — `budget-gates` (stable)
- [Preserve justified provider and prefix affinity within a run without defeating quota safety](cache-affinity.md) — `cache-affinity` (stable)
- [Share correctness-scoped cache and feedback primitives through existing adapters](central-cache-service.md) — `central-cache-service` (stable)
- [Run deterministic scheduled work without waking a full agent](cheap-scheduled-routines.md) — `cheap-scheduled-routines` (stable)
- [Reuse expensive work keyed to all correctness-relevant input versions](incremental-work-cache.md) — `incremental-work-cache` (stable)
- [Amortize approved offline improvement into reusable assets instead of permanent premium inference](offline-improvement-amortization.md) — `offline-improvement-amortization` (stable)
- [Compute reusable source summaries once per content version](offline-summary-reuse.md) — `offline-summary-reuse` (stable)
- [Classify avoidable work into eliminate, share, move or defer before increasing inference](optimization-accounting.md) — `optimization-accounting` (stable)
- [Invalidate cached decisions whenever policy, scope, evidence or authorization changes](policy-cache-invalidation.md) — `policy-cache-invalidation` (stable)
- [Prefetch proven next work with bounded low-watermark queues](prefetch-watermarks.md) — `prefetch-watermarks` (stable)
- [Use similarity-based cache hits only with tenant, freshness and correctness checks](semantic-cache.md) — `semantic-cache` (stable)
- [Keep cacheable prompt prefixes byte-stable and correctly scoped](stable-prefix-cache.md) — `stable-prefix-cache` (stable)
- [Track cancellation semantics and charged usage for interrupted streams](stream-billing-cancellation.md) — `stream-billing-cancellation` (stable)
- [Attribute usage across the complete run and distinguish list price from actual spend](usage-accounting.md) — `usage-accounting` (stable)
