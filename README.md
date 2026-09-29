# Poset–Gram Reconstruction

Reproducibility repository for a finite-order reconstruction project.

## Problem

The computational direction studied here is `G -> Z`, where G is normalized Gram-type data derived from a finite order structure and Z denotes the underlying order/incidence structure.

## Current frozen computational evidence

The current packaged checkpoint is v80. On a frozen 45-structure population (seed `20260935`), Track A performed independently validated G-to-poset reconstruction over 7 repetitions: 315/315 validated reconstructions, with median complete 45-instance workload `0.051716411999223055 s`. Track C performed directed batch 2-WL refinement with shared palettes on same-n batches over 7 repetitions, with median complete 45-structure workload `0.562906189999012 s`.

The numerical quotient of those separately executed medians is `10.884478799640405`.

## Critical interpretation boundary

That quotient is descriptive only. It is not evidence of a same-task speedup because Track A and Track C do not have an established common output/task criterion. This repository does not claim general expressive equivalence, asymptotic superiority, or expressive dominance.

## Experimental discipline

The underlying research record uses frozen checkpoints. Optimization, semantic-equivalence checks, and timing are separated so implementations are not tuned after comparative timing is observed. Track C's optimized 2-WL implementation was checked against the preserved reference before timing. On the specified historical controls and frozen workload, exact outputs, stabilization rounds, and state counts matched. This is a finite executed equivalence check, not a proof for arbitrary inputs.

The cvc5 branch is retained as an incomplete historical experiment: 10 of 315 planned measured calls were executed and all 10 hit the external timeout. The remaining 305 were never executed, and no extrapolation is made.

## Status

This repository packages existing frozen evidence. Repository construction does not alter the frozen v80 research checkpoint. Source code will be added only from preserved executable artifacts whose provenance can be verified.
