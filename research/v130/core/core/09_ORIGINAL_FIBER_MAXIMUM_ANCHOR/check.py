"""Executed complete maximum-anchor enumeration for the original labeled G."""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import json
root=Path(__file__).parent;x=json.loads((root.parent/'counterexample_input.json').read_text());P=x['source_zeta'];Q=x['candidate_zeta'];n=len(P);dp=list(map(sum,P))
q=[[F(sum(a*b for a,b in zip(P[i],P[j]))**2,dp[i]*dp[j]) for j in range(n)] for i in range(n)]
assert all(v>0 for row in q for v in row)
def signature(Z):return [(sum(Z[i]),sum(r[i] for r in Z)) for i in range(n)]
def iso(A,B):
 ca=signature(A);cb=signature(B)
 if Counter(ca)!=Counter(cb):return None
 opts={i:[j for j in range(n) if ca[i]==cb[j]] for i in range(n)};used=set();assigned={}
 def dfs():
  if len(assigned)==n:return [assigned[i] for i in range(n)]
  choices={i:[j for j in opts[i] if j not in used and all(A[i][a]==B[j][b] and A[a][i]==B[b][j] for a,b in assigned.items())] for i in opts if i not in assigned}
  i=min(choices,key=lambda i:len(choices[i]))
  for j in choices[i]:
   assigned[i]=j;used.add(j);r=dfs()
   if r is not None:return r
   used.remove(j);del assigned[i]
  return None
 r=dfs()
 if r is not None:assert all(A[i][j]==B[r[i]][r[j]] for i in range(n) for j in range(n))
 return r
records=[];valid=[]
for m in range(n):
 ds=[1/q[i][m] for i in range(n)];r={'maximum_label':m,'sizes':[str(v) for v in ds]}
 if any(v.denominator!=1 or not 1<=v<=n for v in ds):r['status']='integer_size_rejected';records.append(r);continue
 d=[int(v) for v in ds];Z=[[int(q[i][j]*d[i]==d[j]) for j in range(n)] for i in range(n)]
 axioms=all(Z[i][i] for i in range(n)) and all(not(Z[i][j] and Z[j][i]) for i in range(n) for j in range(n) if i!=j) and all(not(Z[i][j] and Z[j][k]) or Z[i][k] for i in range(n) for j in range(n) for k in range(n))
 if not axioms:r['status']='order_axioms_rejected'
 elif list(map(sum,Z))!=d:r['status']='row_sizes_rejected'
 elif not all(q[i][j]*d[i]*d[j]==sum(a*b for a,b in zip(Z[i],Z[j]))**2 for i in range(n) for j in range(n)):r['status']='Gram_closure_rejected'
 else:
  deg=sorted(a+b-2 for a,b in signature(Z));p=iso(Z,P);c=iso(Z,Q)
  r.update({'status':'valid','Z':Z,'degree_multiset':deg,'P_isomorphism':p,'Q_isomorphism':c});valid.append(r)
 records.append(r)
pdeg=sorted(a+b-2 for a,b in signature(P));qdeg=sorted(a+b-2 for a,b in signature(Q))
out={'scope':'All 16 maximum anchors; complete labeled realization fiber of original positive-entry G','status_counts':dict(Counter(r['status'] for r in records)),'valid_anchor_count':len(valid),'valid_P_degree_count':sum(v['degree_multiset']==pdeg for v in valid),'valid_Q_degree_count':sum(v['degree_multiset']==qdeg for v in valid),'records':records}
assert all(v['P_isomorphism'] is not None or v['Q_isomorphism'] is not None for v in valid)
(root/'exact_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2));print([(v['maximum_label'],'P' if v['P_isomorphism'] is not None else 'Q') for v in valid])
