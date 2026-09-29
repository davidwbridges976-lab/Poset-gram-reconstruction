# Experimental Method

The v74-v80 comparison sequence uses a fixed population of 45 structures generated with seed `20260935`: 6 regular4x4, 2 degree2_regular5x5, and 37 random8_3 structures.

## Track A

Track A takes G as input and performs independently validated poset reconstruction. At frozen checkpoint v74 there were 45 instances and 7 measured repetitions, giving 315 validated executions. All 315 returned a successful target-isomorphism validation. The measured call includes this final validation, and success certifies that at least one retained candidate matches the target; it does not establish uniqueness. One untimed warm-up per family was excluded from measured data. The median complete 45-instance workload was `0.051716411999223055 s`. The warm-up was a timing-control step, not an algorithmic prerequisite.

## Track B: historical incomplete branch

Track B used cvc5 1.4.1 with QF_NIA, a 10,000 ms internal time limit, and a 10 s external watchdog. Of 315 planned measured calls, exactly 10 were executed and all 10 timed out. The remaining 305 were never executed. No 315-call result or exact Track-A/cvc5 ratio is reported. TIMEOUT means unresolved.

## Track C: 2-WL

Track C uses directed ordered pairs V^2, an initial shared palette encoding equality and directed Z-relations, iterative replacement-color refinement, and a shared palette across each compared same-n batch. Before benchmark timing, the optimized implementation was checked against the historical reference. Exact outputs, rounds, and state counts matched on the specified historical controls and all frozen same-n workload batches. This equivalence statement is limited to those executed finite tests.

## Comparison boundary

Track A and Track C use the same frozen 45-structure population and seven measured repetitions, but compute different defined outputs. The v80 quotient `0.562906189999012 / 0.051716411999223055 = 10.884478799640405` is reported only as a descriptive quotient of separately executed medians.
