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

These hashes identify the original artifacts. They must not be interpreted as a claim that every corresponding GitHub file has already been independently fetched back and shown byte-identical.

## Outstanding exact-artifact work

The largest remaining exact transfer is the original v74 `trackA_raw.jsonl`: 315 records, 45,264 bytes, original SHA-256 `429430fb...`.

It is intentionally **not** being reconstructed from aggregate statistics. Until the original bytes can be transferred through a byte-preserving route and verified after upload, the frozen archive is authoritative and the repository checksum/provenance record points to it.

Repository summary/warm-up files created during packaging are useful readable representations, but they are not labeled byte-identical to their frozen originals unless separately verified.

## Modern repository infrastructure

`tests/`, `requirements*.txt`, and `.github/workflows/` are post-experiment reproducibility infrastructure. They do not alter any frozen checkpoint and must not be cited as historical experimental evidence.
