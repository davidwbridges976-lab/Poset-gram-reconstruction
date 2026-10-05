# Information loss through normalization: two exact counterexamples

David Bridges · Standalone sharing edition · 5 October 2026

**[Read the seven-page PDF](Two_Counterexamples_Comparison_and_Self_Contained_Guides.pdf)** · **[Download the complete reproducible packet](https://raw.githubusercontent.com/davidwbridges976-lab/Poset-gram-reconstruction/main/sharing/counterexamples/Two_Counterexamples_Comparison_and_Self_Contained_Packet.zip)**

The ZIP is about 548 KB. The PDF begins with the comparison and invariant map, followed by the two proofs. Each counterexample has a self-contained folder with definitions, construction, certificates, recovery limits and reproduction instructions.

## Continuum example: equal observations, different causal orders

Inside the same fixed open 1+1-dimensional Minkowski diamond, one two-event sample is a chain and another is an antichain. Both give the normalized continuum future-overlap matrix

$$
K=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.
$$

In null coordinates, use $R=(0,1)^2$, metric $ds^2=-du\,dv$ and volume $dV=du\,dv/2$. The samples are

$$
P=((1/2,1/2),(3/4,3/4)),\qquad
Q=((1/2,3/4),(3/4,1/2)).
$$

For $A_x=J^+(x)\cap R$, the observation is
$$
K_{xy}=\frac{\operatorname{vol}(A_x\cap A_y)}
{\sqrt{\operatorname{vol}(A_x)\operatorname{vol}(A_y)}}.
$$

These are **full continuum future regions**, not counts of successors among the sampled events. Strict comparable-pair counts are one versus zero. The future volumes are $(1/8,1/32)$ versus $(1/16,1/16)$; individually attached volumes together with $K$ recover causal order in this fixed model.

“Information loss” here means ambiguity of order from the finite-sample normalized observation alone. This is not a claim of physical destruction of information. The full-domain result has different hypotheses and is not contradicted.

## Related finite-poset example

Two nonisomorphic 16-element posets have identical normalized principal-upset overlap matrix $G$. The packet gives the complete construction, exact zeta matrices and order-invariant certificates. Comparability-degree multisets distinguish this pair; general recovery from $G$ plus the unordered comparability-degree multiset remains unresolved in this work.

Within **each** counterexample, the two unnormalized overlap matrices differ by positive diagonal scaling that normalization cancels. This is equivalent to their normalized equality, not independent evidence of an embedding or physical connection between the examples.

## Reproduce

Extract the ZIP, open a terminal in its directory, and run:

```sh
python3 reproduce_all.py
python3 verify_manifest.py
```

Python 3.10 or later; standard library only. No solver, installation or network is needed. Run without `-O`, because verification uses assertions. The runner uses temporary copies and writes new outputs to `LOCAL_REPRODUCTION`, preserving retained evidence. It checks both witnesses, the invariant inventory and the exact scaling comparison against retained certificates.

## Direct links

- [PDF preview](https://github.com/davidwbridges976-lab/Poset-gram-reconstruction/blob/main/sharing/counterexamples/Two_Counterexamples_Comparison_and_Self_Contained_Guides.pdf)
- [Direct PDF](https://raw.githubusercontent.com/davidwbridges976-lab/Poset-gram-reconstruction/main/sharing/counterexamples/Two_Counterexamples_Comparison_and_Self_Contained_Guides.pdf)
- [Direct ZIP download](https://raw.githubusercontent.com/davidwbridges976-lab/Poset-gram-reconstruction/main/sharing/counterexamples/Two_Counterexamples_Comparison_and_Self_Contained_Packet.zip)
- [SHA-256 checksums](SHA256SUMS.txt)

## Provenance boundary

These are unchanged copies of the prepared sharing PDF and ZIP. Audit 10 v144 and E11 remain frozen. The continuum exploration and comparison remain quarantined; publication here is a sharing action, not canonical mathematical import. Original execution records and correction history retain their scope. No literature novelty, black-hole mechanism or detector claim is made.

The older [v143 sharing edition](../v143/README.md) remains available as its original historical snapshot.
