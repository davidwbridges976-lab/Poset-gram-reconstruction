# Research history and provenance map

This repository is a curated reproducibility layer extracted from a larger mathematical audit record. It is not a replacement for that record.

## Provenance rule

The historical research workflow separated mathematical attacks, experimental attacks, freeze decisions, and later exposition. A later document may organize an earlier result, but it does not become evidence for the earlier result.

Accordingly, repository artifacts are classified as:

- **frozen** — completed checkpoint evidence retained from the research record;
- **historical** — executed earlier material useful for provenance but not the current frozen implementation;
- **pre-freeze** — material created before a freeze and preserved without promoting its status;
- **repository infrastructure** — documentation, tests, CI, and packaging created after the experiments to make the record inspectable and reproducible.

## Mathematical lineage

The underlying problem asks whether the normalized principal-upset Gram matrix

[
G=D^{-1/2}ZZ^TD^{-1/2}
]

determines a finite poset up to isomorphism.

Several surrounding reconstruction statements are already all-n results. In particular, the determinant-one principal minors of (M^TM) recover all order ideals, while those of (ZZ^T) recover all order filters. These unnormalized results do not close the normalized-(G) problem.

The larger mathematical audit subsequently developed intrinsic maximal-layer reconstruction, exact-transport constraints, determinant and primal-dual restrictions, automorphism reduction, and first-deletion structure. The arbitrary-n normalized injectivity question remains open in the manuscript material used to prepare this repository.

## Computational lineage represented here

### v56-v57 — optimization history

The historical v56 branch replaced exhaustive maximum-orthogonal-subset enumeration with an exact maximum-clique front end while preserving the downstream reconstruction semantics being tested. v57 benchmarked that optimized path against its own earlier baseline on a finite matched workload.

These files are retained as historical engineering provenance, not as the independent Track A benchmark.

### v74 — independent Track A benchmark

v74 froze an independent benchmark of the optimized reconstruction path on a deterministic 45-structure population with seed `20260935`.

Seven measured repetitions produced 315 reconstruction calls, all validated correct. The frozen median complete-workload time was `0.051716411999223055 s`.

The executed source and raw-output identities are recorded in the checksum ledger.

### v75 — Track B cvc5 comparison attempt

The cvc5 branch did not produce a completed comparison. Exactly 10 of the planned 315 measured calls executed, and all 10 reached the configured watchdog timeout. The remaining 305 calls were never executed.

A timeout is unresolved, not an UNSAT result and not a demonstrated reconstruction failure. No aggregate Track A/cvc5 speed ratio is justified by this checkpoint.

### v76-v78 — Track C definition and implementation audit

v76 defined a separate directed 2-WL comparison protocol with an explicit firewall: 2-WL and full (G\to P) reconstruction were not assumed to be the same task.

v77 froze the historical directed batch 2-WL semantics and timing boundary.

v78 introduced an optimized implementation and checked exact output equivalence to the preserved reference on finite controls and the frozen workload before timing. This is executed finite equivalence, not a universal proof of implementation equivalence.

### v79 — Track C benchmark

v79 measured the optimized directed batch 2-WL implementation for seven complete repetitions of the same 45-structure population, grouped into same-n batches.

The frozen median complete-workload time was `0.562906189999012 s`.

### v80 — descriptive Track A/Track C comparison

The ratio

[
\frac{0.562906189999012}{0.051716411999223055}
=
10.884478799640405
]

was frozen as a **descriptive timing quotient only**.

It is not a same-task speedup, a proof of task equivalence, an asymptotic comparison, or an expressive-dominance result.

## Later mathematical record

The mathematical audit continued beyond the v80 computational packaging represented above. Later first-deletion and reconstruction-frontier work is relevant to the theory but should not be silently inserted into historical computational checkpoints.

Where later mathematics is summarized in this repository, it belongs in explanatory documentation and must retain its original proved/conditional/open status.

## Repository reconstruction history

This GitHub repository was assembled after the experiments from preserved frozen archives and manuscript material.

Where exact executable source was recovered and verified, it is preserved as source. Where an original artifact is known only through a frozen checksum or where byte identity has not yet been verified, the repository says so rather than fabricating an original.

Modern smoke tests and CI are new infrastructure. They test whether preserved code remains executable; they do not alter the historical experimental record.

## Integrity

See:

- `results/checksums/SHA256SUMS.txt`
- `provenance/FROZEN_CHECKPOINTS.md`
- `provenance/ARTIFACT_STATUS.md`
- `provenance/V74_ARCHIVE_VERIFICATION.md`
- `provenance/V80_ARCHIVE_VERIFICATION.md`
- `provenance/TRACK_C_ARCHIVE_CHAIN.md`

for the artifact-level integrity record.
