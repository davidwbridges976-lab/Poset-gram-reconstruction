# Degree data and scale reconstruction: direct audit
David Bridges — quarantined mathematical reduction — 1 October 2026

## Outcome
The reconstruction machinery remains applicable to the richer invariant: degree data are an exact candidate filter and supply additional scale constraints. They do not automatically give a unique labeled upset-size vector. General uniqueness up to isomorphism remains unresolved in this audit.

This is a direct audit of the foundation identities and candidate-closure rules, not a certification of every historical Audit 10 lemma or a promotion of the quarantine branch.

## Definitions
G is a nonnegative normalized principal-upset Gram matrix on n labeled rows. It is symmetric with diagonal one. Write q_ij=G_ij², exactly; these values are rational for a finite-poset realization. The additional data are an unordered comparability-degree multiset Delta. No assignment of degrees to rows is supplied.

For a proposed integer upset-size vector d in {1,...,n}^n define

Z_d(i,j)=1[q_ij d_i=d_j].

This is the saturation formula without radicals: K_ij=G_ij sqrt(d_i d_j)=d_j iff q_ij d_i=d_j, because all quantities are nonnegative and d_j>0. The nonnegativity assumption is essential when squaring.

## Exact complete candidate test
A proposed d represents a poset with the supplied richer invariant if and only if all of the following hold:
1. Z_d is reflexive, antisymmetric and transitive.
2. sum_j Z_d(i,j)=d_i for every row.
3. For all i,j, q_ij d_i d_j=(sum_k Z_d(i,k)Z_d(j,k))².
4. The multiset of gamma_i=sum_j Z_d(i,j)+sum_j Z_d(j,i)-2 equals Delta.

Necessity: an actual poset satisfies saturation, row sizes, the Gram identity and the degree identity. Sufficiency: conditions 1 and 2 produce a poset with exactly those upset sizes; condition 3 and nonnegativity identify its normalized Gram matrix with G; condition 4 gives the degree multiset. Therefore enumerating the finite set {1,...,n}^n with these tests produces all labeled realizations, though it is generally impractical. This establishes validity and completeness of the candidate description, not uniqueness or efficiency.

## Scale constraints supplied by degrees
For any valid candidate, gamma_i=d_i+down_i-2. Since both upper and lower sizes lie between 1 and n,

max(1,gamma_i+2-n) ≤ d_i ≤ min(n,gamma_i+1).

The degree assignment remains unknown; it must be consistent with the order reconstructed from d. One cannot attach sorted degree entries to the existing row labels without justification.

Summing strict upper and strict lower incidences counts the same comparable pairs twice. Hence

sum_i d_i = n + (1/2)sum_{delta in Delta} delta.

This gives an assignment-independent sum constraint. The retained determinant identity gives another:

product_i d_i=1/det(G).

These constraints can prune enumeration; they do not ensure realizability or uniqueness. The exact closure and degree tests are still necessary. In the original 16-element pair, both upset-size sums are 81, so the sum constraint alone fails to separate them; the complete degree multiset does separate them.

## A necessary distinction: labeled versus structural uniqueness
For a two-element chain,

G=[[1,1/sqrt(2)],[1/sqrt(2),1]], Delta={1,1}.

Both d=(1,2) and d=(2,1) pass all four tests. Their orders are opposite in the fixed labeling but become identical after swapping the two labels. The executed exact enumeration of all four possible vectors in {1,2}² verifies precisely these two candidates.

Thus G plus degrees does not force a single labeled size vector, even in the smallest nontrivial chain. This is not a nonisomorphic collision and does not refute the richer invariant up to isomorphism.

The correct uniqueness question is whether all surviving candidates belong to one orbit under permutations preserving G. Any isomorphism between two orders realizing the same labeled G induces such a permutation and carries their size vectors to each other. Conversely, if two valid size vectors are related by a G-preserving permutation, the saturation formula carries their reconstructed orders to each other. The degree multiset is unchanged by permutation. Therefore the richer invariant is injective at an input exactly when its passing candidate size vectors form one such orbit.

## Survival map
| Machinery | Treatment here |
| --- | --- |
| Saturation / order recovery from labeled sizes | Directly justified, unchanged |
| Exact candidate Gram closure | Directly justified, with exact degree filter added |
| Determinant product of sizes | Retained direct identity |
| Scale sum from degree multiset | Directly derived above |
| Zero-overlap geometry and maximal-count identity | Remain properties of G; no uniqueness added |
| Known compatible-order Cholesky | Still conditional on supplying compatible order |
| Maximal-layer / residual validity reductions | No new uniqueness implication; detailed historical dependencies not reaudited here |
| Historical q=2 and L=4 conditional branches | Not extended to the richer universal target by this audit |
| Universal G-only uniqueness | Still refuted by the exact original pair |
| Universal G-plus-degree uniqueness | Unresolved by this audit |

## Executed checks and scope
check.py uses only standard-library exact fractions. It exhausts all four n=2 size vectors and verifies the two isomorphic passing reconstructions. It also evaluates only the two already known n=16 size vectors against their shared q, verifies recovery of their respective original zeta matrices, and confirms their distinct degree multisets. With the P degree data, only P survives among those two candidates. The entire n=16 size fiber was not enumerated; no assertion that P is its unique realization is made.

No execution failed in this attack. The exact output is retained. Earlier branch failures and corrections remain unchanged.

## Result and next target
The audit supplies a complete candidate formulation for arbitrary finite n under the stated exact-input assumptions. It exposes the remaining obstruction: more than one nonisomorphic candidate orbit might survive the degree filter. This attack neither exhibits nor excludes such a pair universally.

Next proposed, not executed: seek a structural reason that degree matching constrains these candidate orbits, or construct an adversary satisfying the degree filter in a distinctly broader class. The target must be chosen before execution. Merely observing multiple labeled size vectors is not an adequate counterexample.

Status: direct reconstruction audit complete; canonical v127 unchanged; no import, promotion, novelty claim or physical interpretation.
