"""Repository smoke tests.

These tests are new reproducibility infrastructure. They are not part of the
historical frozen v74 execution and must not be cited as frozen evidence.
"""
import importlib.util
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "reconstruction" / "CS_TrackA_Independent_Benchmark_v74.py"


def load_track_a():
    spec = importlib.util.spec_from_file_location("track_a_v74", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_two_element_chain_reconstructs():
    m = load_track_a()
    Z = np.array([[1, 1], [0, 1]], dtype=np.int8)
    _, G = m.exact_q_and_G(Z)
    assert m.optimized_engine_from_G(G, Z)


def test_height2_shape_and_diagonal():
    m = load_track_a()
    B = np.array([[1, 0], [0, 1]], dtype=np.int8)
    Z = m.height2(B)
    assert Z.shape == (4, 4)
    assert np.array_equal(np.diag(Z), np.ones(4, dtype=np.int8))
