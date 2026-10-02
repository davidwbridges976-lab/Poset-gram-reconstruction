# Exact mathematical evidence at frozen v130

All checks below use Python 3.10+ and the standard library only. They are separate from the frozen v74-v80 computational benchmark chain. No new mathematical attack was performed for this repository update.

## Counterexample, scale audit and full original fiber

From the repository root:

```sh
python3 research/v130/core/run_all.py
```

The runner checks the exact normalized Gram collision, order axioms, nonisomorphism certificate, degree/scale examples, all 16 original maximum anchors, and their independent verification. Original relative input layout is preserved. The reader runner is an executed convenience script from the earlier reader edition, not the original historical attack implementation.

## Complete positive-entry verification through eight elements

```sh
python3 research/v130/positive_entry_n8/check.py
python3 research/v130/positive_entry_n8/verify.py
python3 research/v130/positive_entry_n8/control.py
```

The primary integer/bitset generator checks all transitive upper-triangular orders below an appended greatest element. The independent generator uses predecessor ideals and exact rational/set-based closure. Every source and anchor outcome, valid candidate and isomorphism certificate is retained in independent_ledger.jsonl.gz. The control must detect the known 16-element nonisomorphic G-only collision and its degree difference.

Frozen results: 101,660 orders in compatible labelings; 807,571 anchor checks; 103,562 valid anchors; zero nonisomorphic survivors. These counts are not unlabeled-poset counts or distinct Gram matrices. The scope is positive-entry G only, through eight elements. General G-plus-degree injectivity is unresolved.

Scripts overwrite their own generated outputs on rerun. Timing fields and gzip timestamp bytes can change; compare mathematical counts and certificates, not timing-dependent byte identities. Frozen original records and SHA256.json are retained for inspection. Parent checkpoint names/paths in original reports refer to the separately preserved full historical packet. pack.py was a workspace packaging script, not required to reproduce mathematics, and is not included here.

The publication-import checksums are in SHA256SUMS.txt. Copies are byte-identical to their supplied frozen or reader-edition sources unless specifically described as new documentation.
