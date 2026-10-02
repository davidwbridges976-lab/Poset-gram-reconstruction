"""Executed exact scale-filter audit; tiny example exhaustive, original pair scoped."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
root=Path(__file__).parent
q2=[[F(1),F(1,2)],[F(1,2),F(1)]]
def evaluate(q,d):
 n=len(d);Z=[[int(q[i][j]*d[i]==d[j]) for j in range(n)] for i in range(n)]
 axioms=all(Z[i][i] for i in range(n)) and all(not(Z[i][j] and Z[j][i]) for i in range(n) for j in range(n) if i!=j) and all(not(Z[i][j] and Z[j][k]) or Z[i][k] for i in range(n) for j in range(n) for k in range(n))
 if not axioms or list(map(sum,Z))!=list(d):return None
 if not all(q[i][j]*d[i]*d[j]==sum(a*b for a,b in zip(Z[i],Z[j]))**2 for i in range(n) for j in range(n)):return None
 deg=[sum(Z[i])+sum(row[i] for row in Z)-2 for i in range(n)]
 assert sum(d)==n+sum(deg)//2 and sum(deg)%2==0
 assert all(d[i]<=deg[i]+1 for i in range(n))
 return {'sizes':d,'Z':Z,'degree_multiset':sorted(deg),'degree_vector':deg}
candidates=[r for d in product(range(1,3),repeat=2) if (r:=evaluate(q2,d)) is not None and r['degree_multiset']==[1,1]]
assert len(candidates)==2
assert candidates[0]['Z'][0][1]==candidates[1]['Z'][1][0] and candidates[0]['Z'][1][0]==candidates[1]['Z'][0][1]
x=json.loads((root.parent/'counterexample_input.json').read_text());P=x['source_zeta'];Q=x['candidate_zeta'];n=16
dP=list(map(sum,P));dQ=list(map(sum,Q));q=[[F(sum(a*b for a,b in zip(P[i],P[j]))**2,dP[i]*dP[j]) for j in range(n)] for i in range(n)]
p=evaluate(q,dP);c=evaluate(q,dQ);assert p and c and p['Z']==P and c['Z']==Q
out={'two_chain_exhaustive_size_vectors_checked':4,'two_chain_passing_candidates':candidates,'two_chain_distinct_labeled_sizes_but_isomorphic':True,'original_pair_only':{'P_sizes_sum':sum(dP),'Q_sizes_sum':sum(dQ),'both_valid_for_same_q':True,'P_degree_multiset':p['degree_multiset'],'Q_degree_multiset':c['degree_multiset'],'same_degrees':p['degree_multiset']==c['degree_multiset'],'candidates_from_original_pair_surviving_P_degree_data':1},'scope':'n=2 size enumeration exhaustive; n=16 only original two candidates evaluated, not entire fiber'}
(root/'exact_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
