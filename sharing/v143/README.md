# Normalized upset overlaps: a reproducible investigation

David Bridges · Sharing snapshot from frozen v143 · 3 October 2026

**[Read the three-page overview](Poset_Gram_Research_Overview_v143.pdf)** · **[Download the complete packet](https://raw.githubusercontent.com/davidwbridges976-lab/Poset-gram-reconstruction/main/sharing/v143/Poset_Gram_Research_Share_v143.zip)**

The ZIP is about 173 KB. It includes the overview, exact counterexample, Python code, complete certificates and optional detailed proof notes.

For a finite poset, let $U_x$ be its principal upset, including $x$. The investigated matrix is

$$
G_{xy}=\frac{|U_x\cap U_y|}{\sqrt{|U_x||U_y|}}.
$$

An explicit 16-element nonisomorphic pair has exactly the same $G$. Its unordered comparability-degree multisets differ. Whether adding that degree multiset restores uniqueness for every finite poset remains **unresolved in this investigation**.

Recent degree-filter closures apply to specified positive-entry, size-eight-anchor, endpoint-saturated classes: one or two base labels, and three base labels with two incomparable lower labels and one greatest. Complete coverage proofs accompany the finite checks. These are not claims about all 16- or 24-element posets. The three-chain base and broader cases remain open. No novelty or literature-wide open-problem claim is made.

## Reproduce

Extract the ZIP and run from its folder:

```sh
python3 reproduce.py
```

Python 3.10 or later; standard library only. No solver, installation or network is needed. Run without Python's `-O` option because checks use assertions.

The command verifies the counterexample, its entire original positive-entry Gram fiber, scale checks, all 4,356 recent three-base map pairs and an independent canonical-form audit. Exactly 1,068 pairs match degrees; every one has a verified isomorphism. Actual execution records and complete ledgers are included. The sharing packet passed a fresh-extraction test.

## Direct links for sharing

- [PDF preview](https://github.com/davidwbridges976-lab/Poset-gram-reconstruction/blob/main/sharing/v143/Poset_Gram_Research_Overview_v143.pdf)
- [Direct PDF](https://raw.githubusercontent.com/davidwbridges976-lab/Poset-gram-reconstruction/main/sharing/v143/Poset_Gram_Research_Overview_v143.pdf)
- [Direct ZIP download](https://raw.githubusercontent.com/davidwbridges976-lab/Poset-gram-reconstruction/main/sharing/v143/Poset_Gram_Research_Share_v143.zip)
- [Download checksums](SHA256SUMS.txt)

The files are unchanged copies of the prepared sharing edition. This page publishes that snapshot; earlier research files and benchmark records retain their original scope.

## SHA-256

```text
d3e06d54baaa409f294f78fc5870e5a94ca649fde8ebb945565f18b6fe399ae4  Poset_Gram_Research_Overview_v143.pdf
913bf45f6fa29d608246038b3b79bbbf7cf8226680dfe5f8d95c3344eee8d200  Poset_Gram_Research_Share_v143.zip
```
