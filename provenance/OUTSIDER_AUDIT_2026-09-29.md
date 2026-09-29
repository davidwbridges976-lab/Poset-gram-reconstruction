> Historical packaging-audit snapshot, retained without rewriting its findings. Its license and missing-artifact statements are superseded by LICENSE.md and FINAL_OUTSIDER_AUDIT_2026-09-29.md. It is not the current release assessment.

# Outsider audit — 2026-09-29

This is a repository-packaging audit, not a new mathematical or computational research checkpoint.

## Scope

The repository was inspected from the perspective of a skeptical outside reader: tree organization, README claims, mathematical status, experimental claims, reproducibility instructions, provenance records, tests, CI, and artifact presence.

## Checks that passed

- The normalized (G\to P) arbitrary-(n) question is stated as open.
- The all-(n) unnormalized reconstruction layer is kept distinct from the normalized problem.
- v74 finite correctness is described as finite benchmark evidence, not theorem closure.
- v75 is explicitly incomplete: 10 measured calls executed, 305 never executed, timeout treated as unresolved.
- v78 finite implementation-equivalence evidence is not promoted to universal equivalence.
- v80's `10.884478799640405` value is consistently classified as a descriptive quotient, not same-task speedup.
- Historical, pre-freeze, frozen, and modern repository infrastructure are separated.
- The checksum ledger states that a recorded original hash does not imply the original bytes are stored in GitHub.
- The preserved Track A and Track C source paths are present.
- Modern smoke tests are explicitly non-canonical.
- GitHub Actions smoke tests have completed successfully on the configured modern Python matrix.

## Problems found and repaired

1. **README had become stale.** It said source would be added in the future even though verified source files were already present.
   - Repaired by rewriting the README around the mathematical problem, status boundary, navigation, current artifact state, and private/no-license status.

2. **README navigation was too weak for an outsider.**
   - Repaired with direct paths to the mathematical, algorithmic, experimental, reproducibility, checksum, and provenance layers.

3. **Display mathematics in three documentation files used malformed bracket delimiters.**
   - Repaired in `docs/problem.md`, `docs/mathematics.md`, and `docs/algorithm.md` using GitHub-compatible display-math blocks.
   - This was presentation-only; mathematical claims were not changed.

4. **REPRODUCING.md no longer reflected the current tree.**
   - Repaired to acknowledge the present Track C raw copy, readable summary/warm-up representations, successful modern CI, and the still-unresolved v74 raw exact transfer.

## Remaining release blockers / cautions

### 1. v74 raw artifact

The original `trackA_raw.jsonl` is not yet in the curated GitHub tree.

Original identity:

- records: 315
- bytes: 45,264
- SHA-256: `429430fb692d2b2e36afd10da03330e93566906ae650b9362f12207f29dfcd91`

It must not be reconstructed from summaries and presented as original.

### 2. Repository-copy byte verification

Several files correspond to original artifacts whose SHA-256 identities are known, but the GitHub copies have not all been independently fetched and SHA-256-checked after transfer. The frozen archives therefore remain byte-authoritative.

### 3. License

No software license has been selected. A `LICENSE` file should not be added until the author explicitly chooses one.

### 4. Historical environment

Exact historical NumPy and NetworkX versions are not established by the recovered records. Current CI success demonstrates modern executability, not historical environment identity.

## Release assessment

The repository is structurally coherent and its major scientific claim boundaries are visible. It should remain private until the unresolved exact-artifact/byte-verification work is either completed or deliberately accepted as a documented limitation, and until the author makes an explicit license decision.

No mathematical result was promoted, demoted, or reclassified by this audit.
