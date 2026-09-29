# Mathematical foundation

This note records the proved principal-minor reconstruction layer that sits beneath the harder normalized reconstruction problem.

## Zeta and Möbius matrices

For a finite poset (P=(V,\le)), choose a linear extension and define its zeta matrix (Z) by (Z_{xy}=1) when (x\le y), and zero otherwise. Then (Z) is unit upper triangular and is invertible over the integers. Write

$$
M=Z^{-1}.
$$

The entries of (M) are the Möbius function of the poset.

Define

$$
G_\mu=M^TM,\qquad G_\zeta=ZZ^T.
$$

A change of linear extension simultaneously conjugates these matrices by a permutation, so their indexed principal-minor structure is intrinsic up to relabeling.

## Möbius-Gram principal-minor theorem

For every (J\subseteq V),

$$
\det G_\mu[J,J]=1
\quad\Longleftrightarrow\quad
J\text{ is an order ideal}.
$$

The proof uses Cauchy–Binet:

$$
\det G_\mu[J,J]
=
\sum_{I\subseteq V, |I|=|J|}
\det(M[I,J])^2.
$$

If (J) is an ideal, support of the Möbius matrix forces every exterior-row contribution to vanish, leaving the unit-triangular principal term.

If (J) is not an ideal, a saturated chain supplies a cover crossing into (J). The Möbius value on that cover is (-1), producing a nonzero exterior row. Replacing an appropriate principal row gives an additional nonzero integral maximal minor. The Cauchy–Binet sum therefore contains the principal square (1) plus at least one additional positive integer square, so the determinant is at least (2).

## Reconstruction from the ideal family

Once every order ideal has been recovered, define

$$
x\preceq y
\quad\Longleftrightarrow\quad
\text{every recovered order ideal containing }y\text{ also contains }x.
$$

This relation is exactly the original partial order. Therefore (M^TM), considered up to simultaneous row/column permutation, determines the finite poset up to isomorphism.

## Dual zeta-Gram theorem

Dually,

$$
\det G_\zeta[J,J]=1
\quad\Longleftrightarrow\quad
J\text{ is an order filter}.
$$

Thus (ZZ^T) also determines the finite poset up to isomorphism.

## Relation to normalized reconstruction

The principal-minor theorem does **not** solve the main normalized problem. The research target uses

$$
G=D^{-1/2}ZZ^TD^{-1/2},
$$

where (D_{xx}=|U_x|). Diagonal normalization removes directly visible absolute cone sizes. Establishing that this normalized data still forces the poset for arbitrary finite (n) is the open problem.

## Literature/novelty boundary

The underlying linear-algebra identity used in the proof is standard Cauchy–Binet, and the required Möbius-function support facts are standard poset theory. The research manuscript's claim is the poset-specific determinant-one characterization and its reconstruction consequence.

The current manuscript deliberately does not make a certified novelty or priority claim. Continued bibliographic and external specialist review remain appropriate.
