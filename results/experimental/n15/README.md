# Bounded n15 experiments

| Run | Result | Timing |
| --- | --- | --- |
| [Initial exploration](N15_Bounded_Engine_Exploration_2026-09-29.zip) | 68/68 target matches | Internal section: 0.397761936 s; total process time not measured |
| [Exact timed rerun](N15_Exact_Test_Timed_Rerun_2026-09-29.zip) | 68/68 target matches | Total process: 0.617931844 s; internal section: 0.418709713 s |

These are later experimental records, separate from frozen v74–v80. The unchanged v74 engine tested 34 fixed n=15 base inputs and one relabeling of each. Population: four controls, ten height-two, ten three-layer, and ten ordered-DAG closure samples; seed 20260930. Limits: five seconds per call and 120 seconds overall. Driver, engine, inputs, and protocol were byte-identical between runs.

Every one of the 561 base-input pairs had different exact rational squared normalized-Gram entry multisets. No pair required weighted-graph isomorphism. No collision occurred within this population. Relabelings intentionally preserve the poset and G up to permutation.

Target matches establish existence of a matching candidate, not uniqueness or correctness of every retained candidate. The structured population is not exhaustive or uniformly sampled. These experiments do not establish arbitrary-n injectivity.

The external timer includes startup/imports, population generation, 68 isolated calls, exact screening, and result writing. It excludes setup and packaging. Per-call records include process overhead. Single-run times are not directly comparable to the frozen benchmark medians or exhaustive n=15 runtime.

Each unchanged ZIP contains executed code, exact inputs, protocol, raw outputs, environment, notes, and checksums. The initial packet retains a startup dependency failure that executed zero cases. Extract into a fresh directory for reproduction. The rerun wrapper's temporary dependency path may need adjustment on another machine; record any reproduction changes.

## Integrity and licensing

See [archive SHA-256 values](SHA256SUMS.txt). Uploaded ZIPs match the delivered packets exactly.

The existing split-license categories apply to project-owned contents: Python code GPL-3.0-only, prose CC BY-SA 4.0, records CC BY 4.0, factual metadata as described in the root LICENSE.md. No historical 2-WL reference is included.

Status: both experiments complete and preserved. No next test has started.
