# Artifact Status Guide

This repository preserves artifacts at different evidentiary stages. Their location is intentional.

## results/frozen

Artifacts whose supplied records identify them as frozen/completed checkpoints.

Currently represented here:

- v74: frozen Track A benchmark result, preserved executable source, repository summary/warm-up representations, and checksum/provenance records.
- v75: frozen but incomplete cvc5 Track B result.
- v76: frozen Track C protocol.
- v77: frozen Track C implementation/timing-boundary audit.
- v78: optimized 2-WL finite semantic-equivalence verification.
- v79: frozen optimized 2-WL benchmark, including a raw JSONL repository copy plus summary/warm-up representations.
- v80: frozen descriptive Track A/Track C comparison.

The untouched frozen archives remain the byte-authoritative source whenever a repository copy has not itself been independently hash-verified.

## results/historical

Earlier executed experimental records retained to show development of the reconstruction engine.

- v56 router integration evidence.
- v57 whole-engine optimized benchmark.

These records are historical evidence; placement here does not promote them to the current frozen checkpoint.

## historical-source

Source retained for provenance but not presented as current executable release code.

The supplied v56 source explicitly labels itself "ATTACK — not frozen". It is therefore archived with a .txt suffix to reduce the chance that a reader mistakes it for the current supported implementation.

## results/pre-freeze

Artifacts produced before their corresponding freeze.

The supplied v80 pre-freeze comparison is preserved separately and must not be substituted for the later frozen v80 result.

## Exact-byte status

The preserved archives establish the following original SHA-256 identities:

- v74 executed Track A source: `ef5a91e87597da0cfaa2869d10f8aae0978d3880123db5ae40d6d7a085de4040`
- v74 raw Track A output: `429430fb692d2b2e36afd10da03330e93566906ae650b9362f12207f29dfcd91`
- v74 summary: `895557c213894f4e5f0e71de26fc65cd688049da04e06d46f74f49db5cd73597`
- v74 warm-up: `5d6c8aa6af652454158092c1cf7d9325e67efbf70dcad6a1237a80c4ade132a5`
- historical/reference directed 2-WL source: `c02dfc41a5217ee106d314f79d7cc12e2433df10bc6677850e9f3980eee78135`
- v78 optimized Track C source: `e027b937b9b403f7f7427f22da038b8a7d3ace7f1cd2218e1e0c2b50ec4a581c`
- v79 raw Track C output: `69efba3f02b3dbb72f068a5d2a51838ec087e59a5876f9ebcdf3ab8e8eee316b`

These hashes identify the original artifacts.

### Repository byte-verification pass — 2026-09-29

For files whose authoritative original bytes were available, repository Git blob identities were compared against Git blob identities independently computed from those original bytes. Because a Git blob ID hashes the exact byte length and byte content (with Git's blob header), equality establishes byte identity without relying on rendered text.

Verified byte-identical repository copies:

- `src/reconstruction/CS_TrackA_Independent_Benchmark_v74.py` — repository blob `a4f95e4a3020550e86af1cae8f7478056381cee4`; exact match to the authoritative v74 source (SHA-256 `ef5a91e87597da0cfaa2869d10f8aae0978d3880123db5ae40d6d7a085de4040`).
- `src/comparators/wl2/CS_TrackC_2WL_Optimized_v78.py` — repository blob `b4dab718b70264f1547ab4729360b7614a57d581`; exact match to the authoritative v78 source (SHA-256 `e027b937b9b403f7f7427f22da038b8a7d3ace7f1cd2218e1e0c2b50ec4a581c`).
- `src/comparators/wl2/reference/cs_ao4_wl_power_result.py` — repository blob `cf00018457481897672c74319d4e96712f957800`; exact match to the preserved historical reference source (SHA-256 `c02dfc41a5217ee106d314f79d7cc12e2433df10bc6677850e9f3980eee78135`). This byte verification does **not** change its ownership/licensing exclusion.
- `results/frozen/trackC_raw_v79.jsonl` — repository blob `b766f9d734e68cf85beed7c91d9b735af005d641`; exact match to the authoritative v79 raw output (SHA-256 `69efba3f02b3dbb72f068a5d2a51838ec087e59a5876f9ebcdf3ab8e8eee316b`).
- `results/frozen/trackC_warmup_v79.json` — repository blob `2aaefe9340fb54150f41573317e0ee68d1ef3ed7`; exact match to the preserved v79 warm-up bytes available in the verified archive chain (SHA-256 `10d5e81e63dd110e5e58e354ed1810e652f42b6af26839675943e1450897edf0`).

Readable packaging representations that are **not** byte-identical to the authoritative originals remain labeled as representations. In particular, the repository v74 summary/warm-up representations do not have the authoritative originals' Git blob identities, and the repository v79 summary representation likewise differs from the preserved original. No research values are promoted on the basis of those representations.

## Completed Track A raw mirror — 2026-09-29

The original v74 raw output is now stored at `results/frozen/trackA_raw_v74.jsonl` in mirror commit `aed80c604e34a0e952aa1e9e9f9064a14b21b089`.

- Original archive member: `trackA_raw.jsonl`.
- Bytes: 45,264; records: 315.
- SHA-256: `429430fb692d2b2e36afd10da03330e93566906ae650b9362f12207f29dfcd91`.
- Git blob: `d09cad54369597fe1d9423d54836ab93b96abd31`.
- The blob was created from original bytes using base64, committed without normalization, fetched back, decoded, and compared directly to the archive member. Exact equality passed.
- The raw records reproduce all seven workload totals and the frozen median.

The previous outstanding-transfer statement is preserved in the parent commit `fa7af522776c3fddde7c1ba237be272f7d49129d`. Its issue is now resolved; no original output was regenerated.

Repository summary/warm-up representations retain their earlier classifications.

## Modern repository infrastructure

`tests/`, `requirements*.txt`, `.github/workflows/`, and `provenance/verify_mirror_and_records.py` are post-experiment infrastructure. They do not alter frozen checkpoints. The new verification script is licensed under the existing GPL-3.0-only software terms; its factual output is verification metadata.
