# Track C archive verification — v76 through v80

The supplied frozen Track C archives were independently inspected as ZIP containers. No corrupt member was reported.

## v76 — Track C 2-WL protocol

- Archive SHA-256: `9c21c8f4f9416c8a5358c407b85d334d3c19ba882c16863979044a170b2988f6`
- Protocol JSON SHA-256: `3711e0c096a7da70579cbc90acdd475150458e03dada1a8e2be47dcff0e1375f`
- Contains nested frozen v75 predecessor.

## v77 — 2-WL implementation audit

- Archive SHA-256: `4c8c25c28b21bb39106df0327ae0660922259e0bb582a79276d73b1eb8dc6cfb`
- Audit JSON SHA-256: `0a7c4a27ad34483566a85536ffddc6519db0863954b063c14993ce5318ea81b2`
- Historical reference source `cs_ao4_wl_power_result.py`: `c02dfc41a5217ee106d314f79d7cc12e2433df10bc6677850e9f3980eee78135`
- Contains nested frozen v76 predecessor.

## v78 — optimized 2-WL equivalence

- Archive SHA-256: `ba0d8d0ececa299ba9b051c5ef376c292b43b9c57b0c74e5c0fa0ca0488fa737`
- Result JSON SHA-256: `04cd3eeeabeb62587a1b63dcedd704d495e79c67618154138b001033c9fe70d5`
- Optimized executed source `CS_TrackC_2WL_Optimized_v78.py`: `e027b937b9b403f7f7427f22da038b8a7d3ace7f1cd2218e1e0c2b50ec4a581c`
- Historical reference source: `c02dfc41a5217ee106d314f79d7cc12e2433df10bc6677850e9f3980eee78135`
- Contains nested frozen v77 predecessor.

## v80 duplicate verification

The newly supplied v80 archive hashes to `a072083876100a48b0cd447e81b41c94821b77350a5ce487ebae277285305114`, identical to the previously verified v80 frozen archive.

Together these independently supplied archives reproduce the nested v76 → v77 → v78 → v79 → v80 lineage and confirm the previously recorded Track C source/result hashes. They are retained as provenance evidence; individual repository copies should not be described as byte-identical unless their bytes have separately been verified.
