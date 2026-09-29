# Reconstruction algorithm

This document describes the executed Track A v74 reconstruction path. It is an implementation record, not a proof of arbitrary-(n) injectivity.

## Input and validation target

For each frozen test poset with zeta matrix (Z), the benchmark constructs

$
K=ZZ^T,qquad d=\operatorname{diag}(K),qquad
G=K/\sqrt{dd^T}.
$

The engine receives (G). The original (Z) is retained only as a validation target: successful reconstruction means that at least one recovered incidence matrix is isomorphic to the target poset.

## 1. Maximum-orthogonality candidates

Construct the graph on the labels of (G) in which two distinct labels are adjacent when their Gram entry is numerically zero. Enumerate maximal cliques and retain those of maximum cardinality.

Each such clique (J) is treated as a candidate maximal layer.

The v74 implementation uses NetworkX `find_cliques`; this is an exact clique-enumeration step in the executed program, not a heuristic maximum-clique approximation.

## 2. Candidate scale recovery

For every candidate (J) and every label (x), collect the positive entries

$
\{G_{xj}:j\in J, G_{xj}>0\}.
$

The candidate is rejected unless this collection is nonempty and numerically constant for every (x).

For its common value (g_x), propose

$
d_x=\frac{1}{g_x^2}.
$

The executed implementation requires this value to be within tolerance of an integer between (1) and (n).

## 3. Inverse-diagonal divisibility filter

Compute the diagonal of (G^{-1}). For each proposed (d_x), the v74 code requires

$
d_x\le (G^{-1})_{xx}
$

within tolerance and requires

$
\frac{(G^{-1})_{xx}}{d_x}
$

to be numerically integral.

This is a rejection filter: a candidate failing it does not proceed.

## 4. Determinant/product filter

The candidate scale vector must satisfy the numerical identity

$
\prod_x d_x=\frac{1}{\det G}.
$

The implementation checks this with a floating-point tolerance.

## 5. Recover an integral unnormalized Gram candidate

Construct

$
K_f=G\odot\sqrt{dd^T}.
$

Round entrywise to an integer matrix (K), rejecting the candidate unless every entry of (K_f) is sufficiently close to its rounded integer.

## 6. Saturation reconstruction

The executed engine proposes an incidence matrix directly from equality with the diagonal:

$
Z^{(r)}_{xy}
=
\mathbf 1[K_{xy}=K_{yy}].
$

It then requires exact integer closure:

$
K=Z^{(r)}(Z^{(r)})^T.
$

Only candidates satisfying this identity are retained.

## 7. External correctness check

For the benchmark, each retained (Z^{(r)}) is compared with the original test poset by directed-graph isomorphism. A test instance is marked correct if at least one retained reconstruction is isomorphic to the target.

This final comparison is a benchmark validation mechanism. It is not information available to the reconstruction engine in an unknown real instance.

## Frozen v74 workload

The source deterministically constructs a 45-instance height-two population using seed `20260935`:

- 6 regular (4\times4) incidence structures;
- 2 degree-2 regular (5\times5) structures;
- 37 deduplicated random degree-3 (8\times8) structures.

It performs one excluded warm-up per family and then seven measured repetitions of all 45 instances, giving 315 measured reconstruction calls.

The frozen run validated all 315 calls.

## What the benchmark establishes

The frozen v74 run establishes that this concrete implementation successfully reconstructed every member of the specified finite workload in every measured repetition.

It does **not** establish that:

- every finite poset is reconstructible from normalized (G);
- maximum-orthogonality candidate generation is polynomial-time;
- the numerical tolerances are universally safe;
- the algorithm has a proved asymptotic advantage over a comparison method.

Those questions are separate from the executed finite benchmark.

## Source of truth

The executable implementation is:

`src/reconstruction/CS_TrackA_Independent_Benchmark_v74.py`

Its original frozen SHA-256 is recorded in `results/checksums/SHA256SUMS.txt`. The source itself, rather than this explanatory document, is authoritative for exact implementation details.
