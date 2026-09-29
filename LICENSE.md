# Licensing

Copyright © 2026 David Bridges.

This repository uses different licenses for different categories of material. A license applies only to material for which the licensor holds the rights necessary to grant that license.

## Software — GNU GPL v3.0 only

Unless a file is expressly excluded below or carries a different notice, project-owned software under the following paths is licensed under the **GNU General Public License, version 3 only (GPL-3.0-only)**:

- `src/reconstruction/`
- `src/comparators/wl2/CS_TrackC_2WL_Optimized_v78.py`
- `historical-source/`
- `tests/`
- `provenance/verify_mirror_and_records.py`
- `.github/workflows/`

The complete GPLv3 text is in `COPYING`.

The GPL designation here is **version 3 only**, not “version 3 or any later version.”

## Documentation and research exposition — CC BY-SA 4.0

Unless otherwise indicated, project-owned original prose and research exposition in the following locations is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**:

- `README.md`
- `REPRODUCING.md`
- `docs/`
- project-created explanatory/provenance prose in `provenance/`
- `src/comparators/wl2/reference/README.md`

Canonical license:
https://creativecommons.org/licenses/by-sa/4.0/

## Original experimental records — CC BY 4.0

To the extent copyright or similar rights apply and David Bridges has authority to license them, project-owned original experimental/result records under the following locations are licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**:

- `results/frozen/`
- `results/historical/`
- `results/pre-freeze/`

Canonical license:
https://creativecommons.org/licenses/by/4.0/

This license does not alter evidentiary status. “Frozen,” “historical,” and “pre-freeze” retain their research meanings.

## Explicit exclusion — historical 2-WL reference source

The following file is **not licensed under GPLv3, CC BY-SA 4.0, or CC BY 4.0 by this repository**:

`src/comparators/wl2/reference/cs_ao4_wl_power_result.py`

Its provenance is preserved for research reproducibility, but the recovered record does not establish authorship or authority to relicense it. No license grant is made for that file here. Any rights a user may have in it must arise independently of this repository's license grants.

## Metadata, facts, and third-party material

`CITATION.cff`, `requirements*.txt`, checksum lists, hashes, numerical facts, mathematical facts, and other factual metadata are included for identification and reproducibility. Nothing in this licensing notice claims copyright ownership over facts, mathematical ideas, theorems, abstract algorithms, or material outside the licensor's rights.

External dependencies such as Python, NumPy, NetworkX, cvc5, and other third-party software remain governed by their own licenses. This repository does not relicense them.

## Attribution

Where attribution is required for material licensed here, credit:

**David Bridges — Poset Gram Reconstruction**

and identify modifications when the applicable license requires it.

## Provenance

For the ownership review supporting this split-license structure, see:

`provenance/OWNERSHIP_LICENSING_AUDIT_2026-09-29.md`
