# Positive-entry degree-filter exhaustive audit through eight elements

David Bridges — 2 October 2026 — completed experimental attack, pending checkpoint freeze.

## Target and outcome

Can a positive-entry normalized principal-upset Gram matrix have nonisomorphic realizations with the same unordered comparability-degree multiset?

No such example occurs for 1 <= n <= 8. Indeed every passing anchor in this complete finite class is isomorphic to the generating order, without needing degree data. This confirms the positive-entry portion of the previously recorded n <= 8 finite evidence; it is not a new general theorem or a narrowing of the larger-n obstruction. Universal G-only injectivity remains false. Universal G-plus-degree injectivity remains unresolved.

## Exact input and completeness

Use Z_ij = 1[i <= j], with principal upsets including their own element, d_i = |U_i|, K_ij = |U_i intersect U_j| and q_ij = G_ij^2 = K_ij^2/(d_i d_j). All entries of a positive-entry input are nonnegative and strictly positive. A finite realization has a unique maximal element, which is greatest. Conversely a greatest element belongs to every upset and makes every Gram entry positive.

Any such n-element order has a linear extension ending at its greatest element. Remove that element: the remaining arbitrary (n-1)-element poset admits a compatible linear extension. The primary generator exhausts every upper-triangular relation on those labels and retains precisely the transitive relations; it then appends the greatest element. Therefore every isomorphism class in the target class occurs, with repetitions. Counts below are orders in compatible labelings, NOT counts of unlabeled posets or distinct Gram matrices.

For each generated order, every label m is tested as the maximum. Its entire candidate size vector is d'_i = 1/q_im. A nonintegral value or a value outside [1,n] rejects it. Otherwise saturation fixes Z'_ij = 1[q_ij d'_i = d'_j]. The checker requires reflexivity, antisymmetry, transitivity, the proposed row sizes, and exact squared Gram closure. Strict positivity makes squared closure sufficient for equality of G. The v129 maximum-anchor completeness theorem guarantees that no realization is omitted. Isomorphism is checked exactly by backtracking, and each successful permutation is verified against all order entries.

## Results

| n | Orders in compatible labelings | Anchors checked | Valid anchors | Nonisomorphic degree-matching candidates |
|---|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 |
| 2 | 1 | 2 | 2 | 0 |
| 3 | 2 | 6 | 2 | 0 |
| 4 | 7 | 28 | 10 | 0 |
| 5 | 40 | 200 | 45 | 0 |
| 6 | 357 | 2,142 | 396 | 0 |
| 7 | 4,824 | 33,768 | 4,992 | 0 |
| 8 | 96,428 | 771,424 | 98,114 | 0 |
| Total | 101,660 | 807,571 | 103,562 | 0 |

Every valid candidate has matching degrees and an explicit order isomorphism. At n=8 there are 94,790 source orders with one valid anchor, 1,630 with two, and eight with eight. Multiple labeled anchors are not structural collisions.

The primary run took about 16.24 seconds. The independent run took about 40.83 seconds on this execution environment. These timings are observations, not performance guarantees.

## Independent verification and control

check.py is the primary bitset/integer checker. verify.py independently generates orders by adding a final label with every possible predecessor ideal. It uses sets and exact rational arithmetic for reconstruction and closure, with a separate permutation search. It agrees with every source count, anchor histogram, valid-candidate count, and rejection category. Its compressed JSON-lines ledger preserves every generated source, every anchor outcome, every valid candidate order and every successful isomorphism certificate.

control.py reconstructs the frozen 16-element pair from the unchanged phi input and runs the primary checker. It finds exactly anchors 8 and 15, reconstructing Q and P respectively, detects their nonisomorphism, and detects their differing degree multisets. This guards against accidentally treating all alternatives as isomorphic or overlooking the established counterexample.

No execution failed in this attack. Exact stdout/stderr, executed source, outputs and input copy are retained. No floating-point comparison, external poset catalog, unreviewed conditional historical lemma, or physical interpretation is used. No new literature claim is made.

## Provenance and scope firewall

Parent checkpoint: Audit10_Degree_Scale_Maximum_Anchor_Import_Audit_v129_FROZEN.zip. Its exact digest and canonical-PDF reference are in PARENT_CHECKPOINT.json. The source record was consulted for the origin, corrected surviving identities, conditional results, counterexample, approved degree filter, anchor completeness and current roadmap. Historical universal confluence/orbit claims are refuted; conditional q=2/L=4 results are not dependencies of this test. Dirac work remains quarantined. The novelty audit is standalone and does not supply a mathematical premise.

This is one experimental attack. The canonical v129 packet and compact reader edition are unchanged. No canonical promotion, new canonical version or next attack is authorized by this report. Freeze and packet integration remain the next workflow step.

## Next mathematical frontier

The test does not justify repeating already covered small-n searches as new progress. The useful next target is a structural analysis of two valid maximum anchors with matching degree multisets, or a precisely bounded larger-n family that can realize a genuinely new collision. That choice remains proposed, not executed. General inputs with several maximal elements also remain outside this positive-entry test.

## Reproduce

Run python3 check.py, then python3 verify.py, then python3 control.py from this folder. The first writes exact_output.json; the second writes independent_output.json and independent_ledger.jsonl.gz; the third writes control_output.json. SHA256.json records the completed artifact bytes. pack.py is the executed packaging source. A repeat run changes timing fields and compressed-file timestamp bytes; compare mathematical counts and certificates rather than expecting identical timing-dependent file hashes.
