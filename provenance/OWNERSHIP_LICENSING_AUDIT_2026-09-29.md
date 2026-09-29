# Ownership and licensing audit — 2026-09-29

This audit classifies the current repository by provenance and copyright/licensing confidence. It does not itself grant a license and does not change any frozen research checkpoint.

## Classification standard

A verified research provenance chain establishes artifact identity and research history. It does not, by itself, establish copyright authorship. Accordingly, this audit separates:

- material created for the present repository;
- preserved project source/results with strong project provenance;
- factual/checksum metadata;
- historical/reference material whose copyright authorship is not directly established by the recovered record.

## A. Repository-created material — clear project ownership basis

The following material was created as repository documentation or reproducibility infrastructure during packaging of this project:

- `README.md`
- `REPRODUCING.md`
- `CITATION.cff`
- `docs/`
- `provenance/` documentation created for repository packaging
- `tests/`
- `.github/workflows/`
- `requirements.txt`
- `requirements-dev.txt`

Proposed licensing treatment:

- executable/test/workflow material: GPLv3;
- original prose/documentation: CC BY-SA 4.0;
- citation/dependency metadata: treated as metadata, with no attempt to manufacture additional ownership claims over factual content.

## B. Preserved project software — strong provenance, suitable for GPLv3 subject to final author grant

### Track A v74

`src/reconstruction/CS_TrackA_Independent_Benchmark_v74.py`

The frozen archive identifies this as the executed Track A source and records original SHA-256:

`ef5a91e87597da0cfaa2869d10f8aae0978d3880123db5ae40d6d7a085de4040`

No third-party source attribution or embedded license notice was found in the inspected source header. Its imports of Python/NumPy/NetworkX do not transfer ownership of those dependencies into this repository.

### Track C optimized v78

`src/comparators/wl2/CS_TrackC_2WL_Optimized_v78.py`

The frozen archive identifies this as the executed optimized Track C source and records original SHA-256:

`e027b937b9b403f7f7427f22da038b8a7d3ace7f1cd2218e1e0c2b50ec4a581c`

No third-party source attribution or embedded license notice was found in the inspected source header.

### Historical v56 source

`historical-source/v56_candidate_router_ATTACK.py.txt`

This is preserved project engineering source explicitly labeled `ATTACK — not frozen`. Its research status must remain historical even if the copyright holder later licenses the code under GPLv3.

No third-party source attribution or embedded license notice was found in the inspected header.

## C. Project-generated experimental records

The JSON/JSONL/TXT artifacts under:

- `results/frozen/`
- `results/historical/`
- `results/pre-freeze/`

are preserved or repository-represented research records from the project lineage.

Their evidentiary status is independent of their copyright license. A frozen result remains frozen, a historical result remains historical, and a pre-freeze result remains pre-freeze regardless of reuse permission.

Proposed treatment: a separate data/artifact license rather than GPLv3. CC BY 4.0 is the current candidate for original experimental records, subject to the author's final decision and any file-specific ownership exception.

## D. Factual verification metadata

`results/checksums/SHA256SUMS.txt` and factual hash/provenance fields primarily record artifact identities and verification facts.

They should remain freely usable for verification. A copyright notice should not be used to imply ownership over underlying facts, hashes, mathematical facts, or third-party material.

## E. Unresolved ownership — EXCLUDE FROM BLANKET LICENSE

### Historical directed 2-WL reference

`src/comparators/wl2/reference/cs_ao4_wl_power_result.py`

Verified identity:

`c02dfc41a5217ee106d314f79d7cc12e2433df10bc6677850e9f3980eee78135`

Recovered provenance establishes that the file came from:

`recursive/z28/CS_AO4_WL_PowerToResult/cs_ao4_wl_power_result.py`

and the frozen record calls its origin the `frozen CS-AO4 WL Power-to-Result branch`.

The recovered records establish that it was used as the historical reference implementation for v77/v78. They do **not** contain a direct authorship statement, an original copyright notice, a license notice, or a record proving that David Bridges personally authored the file or acquired the right to relicense it.

No evidence of third-party import was found either. The correct status is therefore **ownership unresolved**, not `third-party` and not `owned`.

Until authorship/right-to-license is established, this file must be explicitly excluded from any blanket GPLv3 grant. Preservation for provenance is not treated as proof of relicensing authority.

The accompanying `src/comparators/wl2/reference/README.md` is repository-created explanatory material and can be licensed separately from the reference source itself.

## F. Dependencies are not relicensed

The project imports or refers to external software including Python, NumPy, NetworkX, and cvc5. A repository license applies only to material for which the licensor has the necessary rights. It does not relicense those external projects.

## G. Mathematical ideas and facts

No proposed copyright license is represented as ownership of mathematical facts, theorems, algorithms as abstract ideas, numerical facts, or the underlying reconstruction problem. Licenses govern copyrightable expression and other rights actually covered by their terms.

## Final inventory result

The current tree supports a split-license plan with one material ownership exception:

1. **GPLv3 candidate:** project-owned software, tests, and executable infrastructure.
2. **CC BY-SA 4.0 candidate:** project-owned documentation and research exposition.
3. **CC BY 4.0 candidate:** project-owned experimental/result artifacts.
4. **Metadata/facts:** verification use should remain unobstructed; do not imply copyright ownership of facts.
5. **Explicit exclusion:** `src/comparators/wl2/reference/cs_ao4_wl_power_result.py` until authorship/right-to-license is established.

No license files should imply that the unresolved reference source is covered.

## Remaining ownership question

The recovered project record is insufficient to determine who holds copyright in `cs_ao4_wl_power_result.py`. Resolving that one file requires an independent authorship/right-to-license basis, such as an original creation record, an existing license/copyright notice, or another reliable record identifying its author.

This audit found no other current repository file requiring the same ownership quarantine based on the materials inspected.
