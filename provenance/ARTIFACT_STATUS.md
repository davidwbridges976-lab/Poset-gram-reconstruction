# Artifact Status Guide

This repository preserves artifacts at different evidentiary stages. Their location is intentional.

## results/frozen

Artifacts whose supplied records identify them as frozen/completed checkpoints.

- v78: optimized 2-WL semantic-equivalence verification.
- v79: fresh optimized 2-WL benchmark.

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

The supplied v80 comparison identifies its status as awaiting freeze. It is preserved exactly as a pre-freeze historical artifact and must not be substituted for the later frozen v80 result identified by the provenance record.

## Missing artifacts

A hash or filename in the provenance record does not imply that the corresponding bytes are present in this repository. Missing executed source or raw output will not be reconstructed and presented as original evidence.
