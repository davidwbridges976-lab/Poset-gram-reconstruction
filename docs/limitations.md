# Limitations

This repository separates finite computational evidence from general mathematical conclusions.

* Track A and Track C have different defined outputs. The v80 timing quotient is descriptive and is not a same-task speedup claim.
* The optimized 2-WL implementation matched its reference on specified historical controls and the frozen workload. This is finite executed evidence, not an arbitrary-input theorem.
* The v80 benchmark population is finite and fixed; it does not establish asymptotic superiority.
* Timing does not establish expressive dominance.
* The cvc5 branch is incomplete: exactly 10 of 315 planned measured calls were executed. No behavior is inferred for the 305 unexecuted calls.
* TIMEOUT is treated as unresolved, not UNSAT and not an incorrect result.
* Computational benchmark results do not replace mathematical proof.
