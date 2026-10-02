"""New reader convenience verifier, executed for this packet; not original code."""
import json
from pathlib import Path
from fractions import Fraction as F
root=Path(__file__).parent
x=json.loads((root/'core/counterexample_input.json').read_text());P=x['source_zeta'];Q=x['candidate_zeta'];n=16
for M in (P,Q):
 assert all(M[i][i] for i in range(n))
 assert all(i==j or not(M[i][j] and M[j][i]) for i in range(n) for j in range(n))
 assert all(not(M[i][j] and M[j][k]) or M[i][k] for i in range(n) for j in range(n) for k in range(n))
d=lambda M:list(map(sum,M))
p=d(P);q=d(Q)
assert all(F(sum(a*b for a,b in zip(P[i],P[j]))**2,p[i]*p[j])==F(sum(a*b for a,b in zip(Q[i],Q[j]))**2,q[i]*q[j]) for i in range(n) for j in range(n))
def cert(M):return sorted(sum(row[i] for row in M) for i in range(n) if sum(M[i])==2)
a=cert(P);b=cert(Q);assert a==[5,8,9,10] and b==[6,7,8,11]
print(json.dumps({'valid_posets':True,'all_256_Gram_entries_equal_exactly':True,'nonisomorphic_by_upset_two_downset_sizes':{'P':a,'Q':b}},indent=2))
