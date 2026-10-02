"""Executed independent integer cross-multiplication anchor audit."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json
root=Path(__file__).parent;x=json.loads((root.parent/'counterexample_input.json').read_text());out=json.loads((root/'exact_output.json').read_text());P=x['source_zeta'];Q=x['candidate_zeta'];n=16
bits=[sum(v<<j for j,v in enumerate(row)) for row in P];d=list(map(sum,P));counts=Counter()
for m,rec in enumerate(out['records']):
 assert rec['maximum_label']==m
 size=[F(d[i]*d[m],(bits[i]&bits[m]).bit_count()**2) for i in range(n)]
 assert list(map(str,size))==rec['sizes']
 if any(v.denominator!=1 or not 1<=v<=n for v in size):status='integer_size_rejected'
 else:
  ds=list(map(int,size));Z=[[int((bits[i]&bits[j]).bit_count()**2*ds[i]==d[i]*d[j]*ds[j]) for j in range(n)] for i in range(n)]
  assert all(Z[i][i] for i in range(n))
  assert all(i==j or not(Z[i][j] and Z[j][i]) for i in range(n) for j in range(n))
  assert all(not(Z[i][j] and Z[j][k]) or Z[i][k] for i in range(n) for j in range(n) for k in range(n))
  if list(map(sum,Z))!=ds:status='row_sizes_rejected'
  else:
   zb=[sum(v<<j for j,v in enumerate(row)) for row in Z]
   assert all((zb[i]&zb[j]).bit_count()**2*d[i]*d[j]==(bits[i]&bits[j]).bit_count()**2*ds[i]*ds[j] for i in range(n) for j in range(n))
   assert Z==rec['Z'];assert Z==(Q if m==8 else P);status='valid'
 assert rec['status']==status;counts[status]+=1
r={'all_16_anchors_independently_verified':True,'status_counts':dict(counts),'valid_matrices_exactly_original_Q_at_8_and_P_at_15':True}
(root/'independent_output.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
