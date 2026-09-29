# Final outsider-perspective packaging audit — 2026-09-29

## Disposition

**Exact Track A raw mirror: PASS. Final repository-packaging review: COMPLETE WITH DOCUMENTED LIMITATIONS.**

This is an assistant-performed skeptical-reader review, not an independent external specialist review, a new research checkpoint, or publication approval. Repository visibility remains private. No mathematical or experimental result is promoted.

## Record and scope

The restart was anchored to actual repository commit `fa7af522776c3fddde7c1ba237be272f7d49129d`, the untouched v74 and v80 archives, their freeze/status/roadmap records, and the nested Track C archive chain. The preserved history and existing source, result, claim, reproduction, and licensing documents were read before edits. This review covers the curated computational packaging through v80. It does not resume the wider mathematical audit.

The original v74 raw mirror was completed first in commit `aed80c604e34a0e952aa1e9e9f9064a14b21b089`; this final review follows that mirror.

## Verified evidence

| Check | Result |
| --- | --- |
| v74 ZIP SHA-256 and ZIP integrity | PASS; `ef276887be70162f696842fc480d3cef861c83b451ce92a205631f01b9efe2a8`; no corrupt member |
| v80 ZIP SHA-256 and ZIP integrity | PASS; `a072083876100a48b0cd447e81b41c94821b77350a5ce487ebae277285305114`; no corrupt member |
| Nested v79/v78 ZIP identities and integrity | PASS against recorded hashes |
| Track A raw mirror | PASS; 45,264 bytes; 315 records; SHA-256 `429430fb692d2b2e36afd10da03330e93566906ae650b9362f12207f29dfcd91` |
| Post-commit GitHub readback | PASS; decoded bytes equal original archive member; Git blob `d09cad54369597fe1d9423d54836ab93b96abd31` |
| Track A record keys and family counts | PASS; unique 45 × 7 calls; family counts 42/14/259; all 315 validation flags true |
| Track A frozen aggregate recalculation | PASS; seven totals, family summaries, median `0.051716411999223055 s` agree with archive |
| Track C records | PASS; 21 batch records, three same-n batches × seven repetitions; median `0.562906189999012 s` |
| Descriptive quotient recalculation | PASS; `10.884478799640405` |
| Source/raw/reference archive comparisons | PASS for Track A source, Track C optimized source, historical reference, Track C raw and warm-up |
| Existing modern smoke tests | PASS; two tests under Python 3.12 in this review |

The executed record-verification routine and its output are retained as `verify_mirror_and_records.py` and `FINAL_AUDIT_EXECUTION.txt`. It reads records; it never reruns or replaces frozen timing outputs.

## Findings and corrections

1. README still claimed no software license had been selected, despite the controlling split-license notice. Corrected to the existing notice. No license choice was made by this review.
2. README, reproduction guidance, and artifact status still described the Track A transfer as outstanding. Updated to the verified mirror and readback evidence.
3. Display equations used bare brackets or single-dollar delimiters spanning multiple lines; several commands lacked their backslashes. Corrected the delimiters and commands in current exposition. This is a syntax repair, not a proof change.
4. Track A's timing boundary needed explicit explanation: the timer surrounds `optimized_engine_from_G(G, target_Z)`, including final isomorphism validation. Candidate construction uses G; target_Z is consulted only in the final validation. The boolean establishes existence of a matching candidate, not uniqueness or correctness of every candidate. Documented this boundary.
5. The old outsider-audit snapshot contained superseded transfer and license assessments. Retained it with a historical/superseded banner rather than replacing its findings.
6. The curated tree lacks a standalone original v79 benchmark driver. Documented this as a historical replay limitation; no substitute driver was created.

## Claim-boundary assessment

The normalized arbitrary-n injectivity question remains explicitly open. The principal-minor reconstruction statements remain separate from normalized reconstruction. Track A's finite workload is not an all-n proof. Track B remains incomplete: ten executed timeouts, 305 unexecuted calls. v78 equivalence remains finite executed evidence. v80 remains a quotient of different defined tasks; it is not a same-task speedup or dominance claim.

The existing all-n proof exposition was inspected for consistency, but this review does not certify novelty or replace a manuscript proof audit. The reported exhaustive normalized-G verification through n <= 8 is not independently revalidated here; its complete enumerator/output package is outside this curated tree.

## Remaining limitations

- Exact historical package versions and hardware are not established. The present environment must not be substituted for them.
- Track A summary/warm-up and Track C summary repository files remain readable representations rather than exact original byte copies.
- Historical v79 timing replay is incomplete without its original standalone driver. Source and frozen outputs remain inspectable.
- The historical 2-WL reference retains its explicit licensing exclusion and unresolved right-to-license status. Hash identity resolves no ownership question.
- No independent external expert review, universal implementation-equivalence proof, certified novelty claim, or normalized theorem closure is established by this audit.

The significant outstanding Track A exact-transfer issue is resolved. The remaining limits are stated openly; no release or visibility change was performed.
