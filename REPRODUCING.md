# Reproducing the frozen computational evidence

This document describes the reproducibility boundary of the curated repository. It distinguishes original executed artifacts from documentation and historical records.

## Core environment

The verified Track A v74 source imports:

- Python 3
- NumPy
- NetworkX

Track B v75 additionally records cvc5 version 1.4.1, QF_NIA, a 10,000 ms internal time limit, and a 10.0 second external watchdog. Track B was stopped after 10 measured calls and is not a completed benchmark.

The verified Track C v78 optimized source imports Python standard-library collections and NumPy.

Exact package versions for NumPy and NetworkX are not established by the currently recovered checkpoint records. Do not infer them.

## Track A — v74

Canonical executed source:

`src/reconstruction/CS_TrackA_Independent_Benchmark_v74.py`

Original source SHA-256:

`ef5a91e87597da0cfaa2869d10f8aae0978d3880123db5ae40d6d7a085de4040`

The frozen protocol uses seed `20260935`, 45 structures, seven measured repetitions, and one untimed warm-up per family. The frozen result reports 315/315 validated reconstructions and median complete-workload time `0.051716411999223055 s`.

The original source writes its results under `/mnt/data/v74_trackA_results`. That path reflects the environment in which the frozen run was executed; users reproducing locally may need to change only the output path. Such a change creates a reproduction variant and must not be described as the byte-identical frozen source.

The source is self-contained for its reconstruction routine; it does not require the historical v56 source at runtime.

## Track C — v78/v79

Canonical optimized source:

`src/comparators/wl2/CS_TrackC_2WL_Optimized_v78.py`

Original source SHA-256:

`e027b937b9b403f7f7427f22da038b8a7d3ace7f1cd2218e1e0c2b50ec4a581c`

v78 verified finite output equivalence against the preserved historical directed 2-WL reference on the specified controls and frozen workload. This is finite executed equivalence, not a universal proof of implementation equivalence.

v79 then measured seven complete frozen-workload repetitions. Its frozen median was `0.562906189999012 s`.

Track C computes directed batch 2-WL refinement signatures with shared palettes on same-n batches. It is not the same output task as Track A reconstruction.

## v80 comparison

The frozen descriptive quotient is:

`0.562906189999012 / 0.051716411999223055 = 10.884478799640405`

This is a descriptive quotient between separately executed frozen measurements on the same 45-structure population.

It is **not**:

- a same-task speedup;
- proof that reconstruction and 2-WL compute equivalent outputs;
- an asymptotic complexity comparison;
- a general expressive-dominance result.

## Integrity verification

Original artifact identities are recorded in:

`results/checksums/SHA256SUMS.txt`

To verify a locally recovered original artifact on common Unix-like systems:

```sh
sha256sum FILE
```

or on macOS:

```sh
shasum -a 256 FILE
```

Compare the result with the corresponding entry in `results/checksums/SHA256SUMS.txt`.

## Reproduction versus replication

A rerun on another machine can test whether the correctness results reproduce. Wall-clock timings should be expected to vary with hardware, operating system, Python build, package versions, background load, and timer behavior.

Accordingly, a fresh timing run should be reported as a new replication measurement rather than silently replacing the frozen timing record.

## Modern smoke-test status

The repository's GitHub Actions smoke-test workflow has completed successfully after installation from `requirements-dev.txt`. The workflow currently exercises Python 3.11 and 3.12.

This is a present-day executability check only. It is not part of the frozen v74 timing experiment and does not establish historical package-version identity.

## Exact raw mirror and remaining reproduction limits

The original v74 `trackA_raw.jsonl` is now mirrored at `results/frozen/trackA_raw_v74.jsonl`: 315 records, 45,264 bytes, SHA-256 `429430fb692d2b2e36afd10da03330e93566906ae650b9362f12207f29dfcd91`. The committed copy was fetched and compared directly with the untouched archive bytes.

Track C raw output and warm-up, both executed sources, and the historical reference have verified exact copies. Track A summary/warm-up and Track C summary files remain readable representations, as recorded in `provenance/ARTIFACT_STATUS.md`.

The Track A measured function returns a boolean and includes the final target-isomorphism validation within its timer. Candidate generation uses G; the known target is used only for final validation. A successful boolean does not certify that every retained candidate is isomorphic to the target, nor that the candidate is unique.

The Track C optimized function is present, but the curated tree does not contain a standalone original v79 benchmark driver. The archived v79 records and source permit inspection; they do not provide a complete one-command historical benchmark replay. No driver has been fabricated or labeled original.

Verify the mirrored raw records and frozen descriptive medians with:

```sh
python provenance/verify_mirror_and_records.py
```

Optionally supply `--archives DIRECTORY` containing the untouched v74 and v80 ZIPs for archive-to-repository byte checks. The archive basenames required are recorded in that script. This is a modern packaging verification, not a new historical measurement.

Exact historical package versions and hardware remain unestablished. Missing original bytes are never reconstructed from aggregate statistics and presented as historical artifacts.
