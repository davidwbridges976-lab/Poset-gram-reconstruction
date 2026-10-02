# Reproduce the key results

Requires Python 3.10 or later; standard library only. No installation, solver, network, NumPy or SciPy is needed.

From the packet root run:

```sh
python3 03_REPRODUCE/run_all.py
```

The runner locates its files relative to itself. It verifies the valid 16-element orders, exact equality of all normalized Gram entries, the nonisomorphism certificate, the scale-filter examples, all 16 maximum anchors, and the independent integer anchor audit.

Expected final line: PASS: counterexample, scale audit, complete anchor enumeration, independent anchor audit.

EXECUTED_READER_RUN.json is actual output from executing this runner while producing the packet. run_all.py and verify_counterexample.py are new reader convenience scripts, executed for this edition; they are not mislabeled as original historical scripts. The core/08... and core/09... scripts and input are retained original sources. They regenerate their exact JSON outputs when run.

This reproduces the current core, not the entire historical research program or the larger quarantined generator searches. Those remain in the full archive.
