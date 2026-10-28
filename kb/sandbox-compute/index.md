# sandbox-compute

## Techniques and revisions

- [Collect validated evidence artifacts before destroying ephemeral execution state](artifact-before-cleanup.md) — `artifact-before-cleanup` (stable)
- [Offload the measured expensive command rather than the entire control plane](command-offload.md) — `command-offload` (stable)
- [Profile host, database and command bottlenecks before changing capacity](compute-profiling.md) — `compute-profiling` (stable)
- [Consider local model compression only for an approved accessible workload with measured value](conditional-local-compression.md) — `conditional-local-compression` (stable)
- [Choose approved execution placement from measured needs instead of defaulting every session to the cloud](deployment-placement.md) — `deployment-placement` (stable)
- [Separate worker execution resources from durable orchestration and control-plane state](execution-control-separation.md) — `execution-control-separation` (stable)
- [Provision a sandbox only when needed and overlap safe independent setup with reasoning](lazy-provisioning.md) — `lazy-provisioning` (stable)
- [Move blocking I/O and expensive command work off the control loop through supported boundaries](nonblocking-control-loop.md) — `nonblocking-control-loop` (stable)
- [Select supported sandbox providers by declared operation and environment requirements](pluggable-execution-provider.md) — `pluggable-execution-provider` (stable)
- [Clean up the full task process tree and stale workspaces safely](process-cleanup.md) — `process-cleanup` (stable)
- [Make environment setup, dependencies and network requirements executable](reproducible-environments.md) — `reproducible-environments` (stable)
- [Use deterministic lifecycle hooks for setup, resource claims, audit and cleanup](sandbox-lifecycle-hooks.md) — `sandbox-lifecycle-hooks` (stable)
- [Distinguish snapshot acknowledgment from durable recoverable completion](snapshot-durability.md) — `snapshot-durability` (stable)
- [Use filesystem and storage measurements to reduce build I/O overhead](storage-io-locality.md) — `storage-io-locality` (stable)
- [Quarantine proven unhealthy workers through a bounded supported policy while honoring explicit holds](worker-quarantine.md) — `worker-quarantine` (stable)
- [Use isolated revision-bound workspaces for concurrent tasks](workspace-isolation.md) — `workspace-isolation` (stable)
