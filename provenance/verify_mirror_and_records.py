"""Executed packaging audit; never regenerates frozen benchmark outputs.

Run from repository root with optional --archives pointing to untouched v74/v80 ZIPs.
"""
import argparse
import hashlib
import io
import json
import statistics
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'results/frozen/trackA_raw_v74.jsonl'
EXPECTED = '429430fb692d2b2e36afd10da03330e93566906ae650b9362f12207f29dfcd91'

def digest(b):
    return hashlib.sha256(b).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--archives', type=Path)
    args = parser.parse_args()
    b = RAW.read_bytes()
    assert len(b) == 45264 and digest(b) == EXPECTED
    rows = [json.loads(line) for line in b.splitlines()]
    assert len(rows) == 315 and all(r['validated_correct'] is True for r in rows)
    assert {(r['rep'], r['global_instance_index']) for r in rows} == {(rep, i) for rep in range(1, 8) for i in range(45)}
    assert all(r['seconds'] >= 0 for r in rows)
    totals = [sum(r['seconds'] for r in rows if r['rep'] == rep) for rep in range(1, 8)]
    assert statistics.median(totals) == 0.051716411999223055
    expected_families = {'regular4x4': 6, 'degree2_regular5x5': 2, 'random8_3': 37}
    for rep in range(1, 8):
        for family, count in expected_families.items():
            group = [r for r in rows if r['rep'] == rep and r['family'] == family]
            assert len(group) == count and {r['family_index'] for r in group} == set(range(count))
    c = [json.loads(line) for line in (ROOT / 'results/frozen/trackC_raw_v79.jsonl').read_text().splitlines()]
    assert len(c) == 21 and {(r['rep'], r['n']) for r in c} == {(rep, n) for rep in range(1, 8) for n in (8, 10, 16)}
    assert all(r['instances'] == {8: 6, 10: 2, 16: 37}[r['n']] for r in c)
    cmedian = statistics.median(sum(r['seconds'] for r in c if r['rep'] == rep) for rep in range(1, 8))
    assert cmedian == 0.562906189999012
    assert cmedian / statistics.median(totals) == 10.884478799640405
    print('PASS: Track A exact hash/length, 315 unique calls, 45 x 7, family IDs, frozen median')
    print('PASS: Track C 21 batch records, 3 batches x 7, frozen median and descriptive quotient')
    if args.archives:
        a = args.archives / 'CS_Quarantine_Branch_TrackA-Independent-Benchmark_v74_FROZEN.zip'
        assert digest(a.read_bytes()) == 'ef276887be70162f696842fc480d3cef861c83b451ce92a205631f01b9efe2a8'
        za = zipfile.ZipFile(a); assert za.testzip() is None
        assert za.read('trackA_raw.jsonl') == b
        assert za.read('CS_TrackA_Independent_Benchmark_v74.py') == (ROOT / 'src/reconstruction/CS_TrackA_Independent_Benchmark_v74.py').read_bytes()
        summary = json.loads(za.read('trackA_summary.json'))
        assert [r['total_seconds'] for r in summary['rep_totals']] == totals
        for family, values in summary['family_summary'].items():
            group = [r['seconds'] for r in rows if r['family'] == family]
            assert values == {'records': len(group), 'median_per_instance_seconds': statistics.median(group), 'min_seconds': min(group), 'max_seconds': max(group)}
        v80 = args.archives / 'CS_Quarantine_Branch_TrackA-vs-TrackC-Descriptive-Comparison_v80_FROZEN.zip'
        assert digest(v80.read_bytes()) == 'a072083876100a48b0cd447e81b41c94821b77350a5ce487ebae277285305114'
        z80 = zipfile.ZipFile(v80); assert z80.testzip() is None
        b79 = z80.read('CS_Quarantine_Branch_TrackC-2WL-Benchmark_v79_FROZEN.zip')
        assert digest(b79) == '24f9ccb4f18197e5269c32f84aa67accef7f763d25a6541fe7eac22c916d2494'
        z79 = zipfile.ZipFile(io.BytesIO(b79)); assert z79.testzip() is None
        assert z79.read('trackC_raw.jsonl') == (ROOT / 'results/frozen/trackC_raw_v79.jsonl').read_bytes()
        assert z79.read('warmup.json') == (ROOT / 'results/frozen/trackC_warmup_v79.json').read_bytes()
        assert z79.read('CS_TrackC_2WL_Optimized_v78.py') == (ROOT / 'src/comparators/wl2/CS_TrackC_2WL_Optimized_v78.py').read_bytes()
        b78 = z79.read('CS_Quarantine_Branch_TrackC-2WL-Optimization-Equivalence_v78_FROZEN.zip')
        assert digest(b78) == 'ba0d8d0ececa299ba9b051c5ef376c292b43b9c57b0c74e5c0fa0ca0488fa737'
        z78 = zipfile.ZipFile(io.BytesIO(b78)); assert z78.testzip() is None
        assert z78.read('cs_ao4_wl_power_result.py') == (ROOT / 'src/comparators/wl2/reference/cs_ao4_wl_power_result.py').read_bytes()
        for member, path in [('CS_TrackA_Independent_Benchmark_v74.json', 'results/frozen/CS_TrackA_Independent_Benchmark_v74.json')]:
            original = json.loads(za.read(member)); represented = json.loads((ROOT / path).read_text())
            assert original['result'] == represented['result']
        print('PASS: untouched archive integrity/identity, exact source/raw/reference copies, Track A aggregate recalculation')
    print('Scope: record and packaging verification; no new theorem, historical timing run, or external review.')

if __name__ == '__main__':
    main()
