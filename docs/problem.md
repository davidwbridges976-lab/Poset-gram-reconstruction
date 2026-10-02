# Reconstruction problem and current status

For a finite poset, let $U_x=\{y:x\le y\}$, including $x$ itself. Set $Z_{xy}=\mathbf{1}[x\le y]$, $K=ZZ^T$, $d_x=|U_x|$, $D=\mathrm{diag}(d)$, and

$$G=D^{-1/2}KD^{-1/2},\qquad G_{xy}=\frac{|U_x\cap U_y|}{\sqrt{d_xd_y}}.$$

## Original question: answered negatively

Does $G$, up to simultaneous row/column permutation, determine the order up to isomorphism? **No.** The verified 16-element pair consists of nonisomorphic orders with identical normalized principal-upset Gram matrices. This is an exact collision. Relabelings of the same order are not counterexamples.

Read the [counterexample note](current/Counterexample_Note.pdf), then run the [exact checks](../research/v130/README.md). All 16 possible maximum anchors were checked for this positive-entry matrix: exactly two pass, producing the original P and Q. Their comparability-degree multisets differ.

## Current question: unresolved in this project

Let $\Delta$ be the unordered multiset of comparability degrees, where the degree of $x$ counts other elements comparable to $x$. Does $(G,\Delta)$ determine every finite poset up to isomorphism?

No general theorem or counterexample for this richer invariant is established here. The known original fiber is separated by degree data; that scoped success does not answer the universal question. Degree values are not assumed to be assigned to Gram rows.

## What survives

- $K$ recovers order by $x\le y$ iff $K_{xy}=K_{yy}$.
- $G$ with labeled upset sizes recovers $K$ and the order.
- $\det G=1/\prod_xd_x$; zero-overlap data recover the number of maxima and comparability components.
- A supplied compatible linear extension permits conditional Cholesky reconstruction.
- Exact candidate-validity tests and maximal-layer reductions enumerate realizations without asserting uniqueness.
- For positive-entry $G$, all realizations occur among its $n$ maximum anchors, with $d_i=1/G_{im}^2$.

The [current PDF](current/Audit10_Current_Mathematics_v130.pdf) provides proofs, assumptions, scope boundaries and open problems.

## Finite evidence

The complete positive-entry class through eight elements has been independently checked by two generators. No nonisomorphic alternatives occur, even without degree data. This is finite computational verification, not arbitrary-size injectivity. It is separate from the older Track A/B/C benchmarks and bounded n15 runs.

## Historical preservation

The [v120 problem statement](historical/v120/problem.md) records the earlier open G-only target. That status is superseded. Historical failures and conditional results remain preserved; they are not rewritten as current general theorems. Novelty and priority remain unresolved.
