# Reconstruction problem

Let (P=(V,\le)) be a finite poset and choose a linear extension. Its zeta matrix is

$
Z_{xy}=\mathbf 1[x\le y].
$

Set

$
K=ZZ^T,qquad d_x=K_{xx}=|U_x|,qquad D=\operatorname{diag}(d_x),
$

where (U_x) is the principal upper set of (x). The normalized principal-upset Gram matrix is

$
G=D^{-1/2}KD^{-1/2}.
$

Equivalently,

$
G_{xy}=\frac{|U_x\cap U_y|}{\sqrt{|U_x||U_y|}}.
$

The central problem of this repository is:

> Given (G), can the underlying finite poset (P) be reconstructed up to isomorphism?

## What is already reconstructible

There are closely related Gram products for which reconstruction is proved for arbitrary finite posets.

Writing (M=Z^{-1}), the Möbius Gram matrix is (G_\mu=M^TM). For every subset (J\subseteq V),

$
\det G_\mu[J,J]=1
\quad\Longleftrightarrow\quad
J\text{ is an order ideal of }P.
$

Thus (M^TM), up to simultaneous permutation of rows and columns, recovers the complete ideal family and therefore determines the poset up to isomorphism.

Dually, for (G_\zeta=ZZ^T),

$
\det G_\zeta[J,J]=1
\quad\Longleftrightarrow\quad
J\text{ is an order filter of }P.
$

Hence (ZZ^T) also determines the finite poset up to isomorphism.

These are structural reconstruction statements. They should not be confused with the normalized-(G) problem.

## Where the difficulty enters

Passing from (K=ZZ^T) to

$
G=D^{-1/2}KD^{-1/2}
$

removes the absolute principal-upset scales (d_x) from direct observation. The research problem is therefore not whether the unnormalized incidence Gram matrix retains the order—it does—but whether the lost diagonal scale information is intrinsically recoverable from the normalized matrix strongly enough to force a unique poset up to isomorphism.

A compatible linear-extension order is another easier regime: when the relevant matrix is already presented in such an order, triangular/Cholesky structure gives exact reconstruction. The unlabeled normalized problem cannot assume that ordering in advance.

## Current status

The arbitrary-(n) injectivity problem for normalized (G) remains open.

The frozen research record contains all-(n) structural consequences, finite exhaustive verification, intrinsic maximal-layer and residual-closure machinery, exact transport constraints, determinant and primal-dual constraints, automorphism reductions, and first-deletion rigidity results. These substantially constrain any competing reconstruction but are not presented as closure of the main theorem.

Complete unlabeled finite verification through (n\le8) found no (G)-collision. This is computational evidence, not an all-(n) proof.

## Claim boundary

The repository deliberately separates three levels of evidence:

1. proved all-(n) structural statements;
2. finite computational verification and benchmark results;
3. open arbitrary-(n) normalized reconstruction questions.

No result from levels 2 or 3 is promoted into an all-(n) theorem without a proof.
