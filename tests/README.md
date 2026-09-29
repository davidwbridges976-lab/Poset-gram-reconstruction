# Tests

The tests in this directory are **new repository reproducibility infrastructure**. They were not executed as part of the frozen historical checkpoints and are not evidence for those checkpoint results.

The initial smoke tests exercise the preserved v74 Track A source on a tiny poset and verify a basic height-two construction invariant.

Run from the repository root with:

```sh
python -m pytest
```

Pytest itself is a repository-development dependency; the preserved v74 executable source requires NumPy and NetworkX.

A successful smoke test means the preserved code imports and executes in the current environment. It does not reproduce the frozen v74 timing measurement or prove arbitrary-n injectivity.
