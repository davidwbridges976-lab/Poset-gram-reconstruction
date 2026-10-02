# Complete maximum-anchor audit of the original Gram fiber
David Bridges — quarantined mathematical audit — 1 October 2026

## Result
The original labeled normalized Gram matrix has exactly two labeled finite-poset realizations: the original P and Q. Their comparability-degree multisets differ. Supplying either one's degree multiset leaves exactly that labeled realization.

This classifies one complete fiber, rather than another bounded generator sample. It does not establish reconstruction from G plus degree data at arbitrary inputs. The original G-only collision remains valid and exact.

| Maximum-anchor outcome | Count |
| --- | ---: |
| Integer upset-size bounds fail | 6 |
| Reconstructed row sizes fail | 8 |
| Fully valid realizations | 2 |
| Total anchors | 16 |

Maximum label 8 yields precisely Q; maximum label 15 yields precisely P. These are zero-based labels in the original sector/bitmask ordering. Each degree multiset retains one valid anchor and excludes the other.

## Completeness proof
Every entry of the original G is strictly positive, including all off-diagonal entries. In any finite-poset realization, two distinct maximal elements would have disjoint singleton principal upsets, giving G_mm'=0. Therefore there is at most one maximal element. Every nonempty finite poset has a maximal element, so each realization has exactly one. It is a greatest element: extending upward from any element ends at that unique maximum.

For a proposed maximum m, d_m=1 and every upset contains m. Hence

G_im=1/sqrt(d_i), so d_i=1/G_im²=1/q_im.

Thus each of the n possible maximum labels fixes the entire labeled upset-size vector. Saturation then fixes the order:

Z(i,j)=1[q_ij d_i=d_j].

There is at most one valid realization per anchor. Checking every anchor, poset axioms, row sizes and exact Gram closure therefore exhausts the entire labeled realization fiber. This argument applies to any realizable nonempty finite-poset G with strictly positive entries. It is a complete enumeration reduction, not a universal uniqueness claim.

For this input n=16, all 16 anchors were checked. Six vectors violate the required integer bounds 1≤d_i≤16. Eight give orders whose upset row sizes disagree with the proposed vector. The remaining two satisfy all poset axioms, size identities and 256 exact Gram equalities. Their matrices agree entrywise with the original P and Q; no third labeled realization exists.

Any unlabeled poset realizing G up to permutation can be relabeled into this fixed Gram matrix, so the same enumeration covers that interpretation too. Since P and Q are nonisomorphic by the earlier audited up/down-size certificate, this fiber has exactly two order-isomorphism classes.

## Degree filter and surviving machinery
The complete degree multisets of P and Q differ. The richer invariant therefore chooses one of these two realizations. This strengthens the earlier scoped check of just the two known candidates: the present completeness proof excludes other candidates as well.

The result uses the retained maximum/saturation and exact closure machinery. It does not claim that degree data always choose one anchor or that every Gram matrix has positive entries. Inputs with several maximal elements require a different enumeration mechanism. Historical conditional branches are not promoted or globally reaudited here.

## Executed verification
check.py computes exact q entries as fractions, enumerates all 16 anchors, checks order axioms and row sizes, and checks exact squared Gram closure. Valid entries retain their zeta matrices, degree multisets and explicit isomorphism certificates against the original orders.

verify.py independently reconstructs candidate sizes from source row-intersection bit counts and uses integer cross-multiplication to recover and validate each candidate order. It confirms every rejection and verifies entrywise that the only valid matrices are Q at anchor 8 and P at anchor 15. Both use only the Python standard library. No execution failed. All exact outputs are retained.

Run python3 check.py, then python3 verify.py. The first script's exact_output.json contains every anchor and rejection status; independent_output.json records the independent audit. This is a computation with a completeness proof, not a claim based on approximate spectra or an incomplete search bound.

## Status
Complete: one full Gram fiber classified; degree data select a unique realization in that fiber.
Unresolved: whether G plus degree multiset is injective for every finite poset, including other positive-entry inputs.
Canonical v127: unchanged; no import or promotion.
Next proposed, unexecuted: test whether degree matching can leave two nonisomorphic valid maximum-anchor realizations at a different positive-entry G, or seek a structural exclusion theorem. No next test ran.
