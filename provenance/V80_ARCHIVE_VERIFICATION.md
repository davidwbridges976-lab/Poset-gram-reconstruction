# v80 frozen archive verification

The supplied historical archive `CS_Quarantine_Branch_TrackA-vs-TrackC-Descriptive-Comparison_v80_FROZEN.zip` was inspected without modifying it.

- SHA-256: `a072083876100a48b0cd447e81b41c94821b77350a5ce487ebae277285305114`
- ZIP integrity test: no corrupt member reported.
- Top-level members: 6.
- Frozen v80 result SHA-256: `72260846e719199aa733cb1e5a44c0375ab336a0dc7f9a5a7c860b53696b8b17`.
- Nested v79 frozen ZIP SHA-256: `24f9ccb4f18197e5269c32f84aa67accef7f763d25a6541fe7eac22c916d2494`; nested ZIP integrity test passed.
- Nested v78 frozen ZIP SHA-256: `ba0d8d0ececa299ba9b051c5ef376c292b43b9c57b0c74e5c0fa0ca0488fa737`; nested ZIP integrity test passed.

The nested v79 archive contains the actual optimized Track C source `CS_TrackC_2WL_Optimized_v78.py`, SHA-256 `e027b937b9b403f7f7427f22da038b8a7d3ace7f1cd2218e1e0c2b50ec4a581c`, plus raw benchmark output `trackC_raw.jsonl`, SHA-256 `69efba3f02b3dbb72f068a5d2a51838ec087e59a5876f9ebcdf3ab8e8eee316b`.

The nested v78 archive also contains the historical reference `cs_ao4_wl_power_result.py`, SHA-256 `c02dfc41a5217ee106d314f79d7cc12e2433df10bc6677850e9f3980eee78135`.

These hashes match the previously recorded provenance. This establishes that the supplied archive recovers original source/result bytes for the Track C lineage rather than reconstructed substitutes.
