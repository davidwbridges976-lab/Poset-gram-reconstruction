# Poset–Gram Reconstruction

Reproducibility repository for a finite-poset reconstruction program studying whether normalized Gram-type data determine the underlying order structure.

## Reading guide

Start with the [three-page sharing overview and reproducible packet (v143)](sharing/v143/README.md). The [10-page v130 mathematics PDF](docs/current/Audit10_Current_Mathematics_v130.pdf) and [research guide](docs/research-guide.md) remain the earlier evidence entry points; the v74-v80 benchmarks remain separate historical experiments.

**Current status:** normalized Gram data $G$ alone do **not** determine every finite poset. An exact 16-element nonisomorphic pair has identical $G$. For this entire Gram fiber, the comparability-degree multiset separates the two realizations. Whether $G$ together with the unordered comparability-degree multiset determines every finite poset remains **unresolved in this project**. No literature-wide open-problem or novelty claim is made.

[Counterexample note](docs/current/Counterexample_Note.pdf) · [Exact verification](research/v130/README.md) · [Historical v120 guide](docs/historical/v120/research-guide.md)

## Mathematical problem

For a finite poset with zeta/incidence matrix $Z$, set

$$
K=ZZ^T,\qquad D=\mathrm{diag}(K),\qquad G=D^{-1/2}KD^{-1/2}.
$$

The original question was whether $G$, considered up to simultaneous row and column permutation and without a supplied compatible linear extension, determines the finite poset up to isomorphism. The verified counterexample answers this in the negative. The current target adds the unordered comparability-degree multiset.

The unnormalized matrix $K=ZZ^T$ recovers order directly by $x\le y$ iff $K_{xy}=K_{yy}$. Labeled upset sizes together with $G$ also recover order. The historical principal-minor results are preserved in [the mathematical foundation](docs/mathematics.md); they do not establish uniqueness for normalized $G$.

See [the problem statement](docs/problem.md) and [mathematical foundation](docs/mathematics.md).

## Frozen computational evidence

The packaged computational chain currently ends at **v80**.

On the frozen 45-structure population (seed `20260935`):

- **Track A / v74:** independently validated $G \to$ poset reconstruction, seven repetitions, 315/315 measured reconstructions validated correct; median complete 45-instance workload `0.051716411999223055 s`.
- **Track B / v75:** incomplete cvc5 experiment; exactly 10 of 315 planned measured calls executed and all 10 reached the configured timeout. The other 305 were never executed.
- **Track C / v79:** directed batch 2-WL refinement with shared palettes on same-$n$ batches, seven complete repetitions; median complete 45-structure workload `0.562906189999012 s`.

v80 records the numerical quotient

$$
0.562906189999012/0.051716411999223055
=10.884478799640405.
$$

**This is a descriptive timing quotient only.** Track A and Track C compute different defined outputs. It is not a same-task speedup, a proof of task equivalence, an asymptotic comparison, or an expressive-dominance result.

See [experimental method](docs/experimental-method.md) and [limitations](docs/limitations.md).

## Reconstruction implementation

The preserved v74 Track A implementation is:

`src/reconstruction/CS_TrackA_Independent_Benchmark_v74.py`

Its reconstruction path is documented in [algorithm.md](docs/algorithm.md). The preserved optimized Track C implementation and historical directed 2-WL reference are under `src/comparators/wl2/`.

## Reproducing and auditing

Start with [REPRODUCING.md](REPRODUCING.md). Modern smoke tests live under `tests/` and run in GitHub Actions on Python 3.11 and 3.12. These tests are new repository infrastructure, not retroactive historical evidence.

Artifact identities and archive verification are recorded in:

- [SHA-256 ledger](results/checksums/SHA256SUMS.txt)
- [artifact-status guide](provenance/ARTIFACT_STATUS.md)
- [frozen-checkpoint map](provenance/FROZEN_CHECKPOINTS.md)
- [v74 archive verification](provenance/V74_ARCHIVE_VERIFICATION.md)
- [Track C archive chain](provenance/TRACK_C_ARCHIVE_CHAIN.md)
- [v80 archive verification](provenance/V80_ARCHIVE_VERIFICATION.md)
- [research history](provenance/research-history.md)

The untouched frozen archives remain byte-authoritative wherever an individual repository copy has not independently been verified byte-for-byte.

## Evidence boundary

This repository deliberately separates:

1. all-$n$ mathematical results;
2. finite computational evidence;
3. the refuted general $G$-only claim and unresolved richer-invariant questions;
4. historical/pre-freeze artifacts; and
5. modern repository/testing infrastructure.

No finite benchmark is promoted into an arbitrary-$n$ theorem, and later mathematical developments are not back-imported into earlier computational checkpoints.

## License

This repository uses a split-license structure:

- project-owned software: **GPL-3.0-only**;
- project-owned documentation and research exposition: **CC BY-SA 4.0**;
- project-owned experimental/result records: **CC BY 4.0**;
- the historical reference source `src/comparators/wl2/reference/cs_ao4_wl_power_result.py` is **explicitly excluded** from these license grants because its right-to-license status is unresolved.

See `LICENSE.md` for the controlling scope notice and `COPYING` for the GPLv3 text. Licensing does not alter any artifact's frozen, historical, pre-freeze, or evidentiary status.

## Packaging status

The original v74 raw output is mirrored exactly at `results/frozen/trackA_raw_v74.jsonl` (315 records; 45,264 bytes; SHA-256 `429430fb692d2b2e36afd10da03330e93566906ae650b9362f12207f29dfcd91`). Its bytes were extracted from the verified archive and fetched back from GitHub for comparison.

The repository is public. The controlling split-license notice is `LICENSE.md`; the historical 2-WL reference exclusion remains in force.

See [the final packaging audit](provenance/FINAL_OUTSIDER_AUDIT_2026-09-29.md) for verified checks and remaining reproducibility limits.

## Later bounded experiments

Two n=15 experimental packets, including an exact timed rerun, are documented in [the n15 experiment guide](results/experimental/n15/README.md). Both returned 68/68 target matches on the same fixed population. They remain finite experimental evidence, separate from the frozen v74–v80 benchmarks, and do not establish unique reconstruction.

## Current mathematical evidence (v130)

The repository now includes the exact counterexample, complete original-fiber anchor enumeration, approved degree/scale audit, and independent exhaustive positive-entry verification through eight elements. The latter covers 101,660 orders in compatible labelings and 807,571 anchor checks; these are not counts of unlabeled posets or distinct Gram matrices. Every valid anchor is isomorphic to its source. This independently confirms older finite evidence and does not narrow the general larger-n obstruction.

See [the current reproduction map](research/v130/README.md) and [update provenance](provenance/MATHEMATICAL_STATUS_UPDATE_v130.md). The old computational records and licensing exclusion remain unchanged.
