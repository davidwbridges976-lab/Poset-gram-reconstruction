"""Independent recursive ideal generator and rational/set-based verification."""
from pathlib import Path
from fractions import Fraction
import json,gzip,time,itertools
ROOT=Path(__file__).resolve().parent

def orders(k):
 if k==0:
  yield [];return
 for old in orders(k-1):
  for subset in range(1<<(k-1)):
   # The new last vertex's predecessors must form an ideal.
   if any((subset>>j)&1 and j in old[i] and not ((subset>>i)&1) for i in range(k-1) for j in range(k-1)):continue
   yield [r|({k-1} if (subset>>i)&1 else set()) for i,r in enumerate(old)]+[{k-1}]

def certificate(A,B):
 n=len(A)
 def sig(R,i):return (len(R[i]),sum(i in r for r in R))
 choices=[[j for j in range(n) if sig(A,i)==sig(B,j)] for i in range(n)]
 p=[]
 def go(i):
  if i==n:return p.copy()
  for j in choices[i]:
   if j in p:continue
   if any((k in A[i])!=(p[k] in B[j]) or (i in A[k])!=(j in B[p[k]]) for k in range(i)):continue
   p.append(j);found=go(i+1)
   if found is not None:return found
   p.pop()
  return None
 return go(0)

def main():
 reference=json.loads((ROOT/'exact_output.json').read_text());records=[];start=time.perf_counter()
 with gzip.open(ROOT/'independent_ledger.jsonl.gz','wt') as ledger:
  for n in range(1,9):
   count=valid=matching=noniso=0;hist={};rejections={};source_hash_sum=0
   for old in orders(n-1):
    A=[r|{n-1} for r in old]+[{n-1}];count+=1
    sizes=[len(r) for r in A]
    q=[[Fraction(len(a&b)**2,sizes[i]*sizes[j]) for j,b in enumerate(A)] for i,a in enumerate(A)]
    deg=lambda R:sorted(len(R[i])+sum(i in r for r in R)-2 for i in range(n))
    delta=deg(A);entries=[]
    for m in range(n):
     d=[1/q[i][m] for i in range(n)]
     if any(x.denominator!=1 or not 1<=x<=n for x in d):status='integer';B=None;p=None
     else:
      B=[{j for j in range(n) if q[i][j]*d[i]==d[j]} for i in range(n)]
      if any(i not in B[i] for i in range(n)) or any(i!=j and j in B[i] and i in B[j] for i in range(n) for j in range(n)) or any(not B[j]<=B[i] for i in range(n) for j in B[i]):status='poset';p=None
      elif any(len(B[i])!=d[i] for i in range(n)):status='rows';p=None
      elif any(Fraction(len(B[i]&B[j])**2,len(B[i])*len(B[j]))!=q[i][j] for i in range(n) for j in range(n)):status='gram';p=None
      else:
       status='valid';valid+=1;p=certificate(A,B)
       match=deg(B)==delta;matching+=int(match)
       noniso+=int(match and p is None)
       assert p is not None,'Unexpected G-only collision: retain and inspect'
       assert sorted(p)==list(range(n)) and all((j in A[i])==(p[j] in B[p[i]]) for i in range(n) for j in range(n))
     if status!='valid':rejections[status]=rejections.get(status,0)+1
     entries.append({'anchor':m,'status':status,'candidate':[sorted(r) for r in B] if status=='valid' else None,'isomorphism':p})
    passed=sum(e['status']=='valid' for e in entries);hist[passed]=hist.get(passed,0)+1
    assert entries[n-1]['status']=='valid'
    ledger.write(json.dumps({'n':n,'source':[sorted(r) for r in A],'anchors':entries},separators=(',',':'))+'\n')
   rec={'n':n,'transitive_sources':count,'valid_anchors':valid,'matching_degree_anchors':matching,'nonisomorphic_matching_degree_anchors':noniso,'valid_anchor_histogram':hist,'rejections':rejections}
   expected=reference['records'][n-1]
   for key in ('transitive_sources','valid_anchors','matching_degree_anchors','nonisomorphic_matching_degree_anchors'):assert rec[key]==expected[key],(n,key)
   assert {str(k):v for k,v in hist.items()}==expected['valid_anchor_histogram']
   assert all(rejections.get(key,0)==value for key,value in expected['rejections'].items())
   records.append(rec);print(json.dumps(rec),flush=True)
 (ROOT/'independent_output.json').write_text(json.dumps({'records':records,'all_checks_passed':True,'seconds':time.perf_counter()-start},indent=2)+'\n')
if __name__=='__main__':main()
