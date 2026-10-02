"""Executed finite exhaustive attack. Standard library; exact integer arithmetic."""
from pathlib import Path
import json,time,hashlib

ROOT=Path(__file__).resolve().parent

def iso(A,B):
 n=len(A)
 sig=lambda R:[(R[i].bit_count(),sum((r>>i)&1 for r in R)) for i in range(n)]
 sa,sb=sig(A),sig(B)
 choices=[[j for j in range(n) if sa[i]==sb[j]] for i in range(n)]
 mapping={};used=set()
 def go():
  if len(mapping)==n:return [mapping[i] for i in range(n)]
  i=min((i for i in range(n) if i not in mapping),key=lambda i:sum(j not in used for j in choices[i]))
  for j in choices[i]:
   if j in used:continue
   if any(((A[i]>>k)&1)!=((B[j]>>v)&1) or ((A[k]>>i)&1)!=((B[v]>>j)&1) for k,v in mapping.items()):continue
   mapping[i]=j;used.add(j)
   ans=go()
   if ans is not None:return ans
   used.remove(j);del mapping[i]
  return None
 return go()

def degrees(R):
 return sorted(r.bit_count()+sum((s>>i)&1 for s in R)-2 for i,r in enumerate(R))

def anchors(R):
 n=len(R);d=[r.bit_count() for r in R]
 K=[[(a&b).bit_count() for b in R] for a in R]
 answers=[];rejects={'integer':0,'poset':0,'rows':0,'gram':0}
 for m in range(n):
  sizes=[]
  for i in range(n):
   num=d[i]*d[m];den=K[i][m]**2
   if num%den or not 1<=num//den<=n:break
   sizes.append(num//den)
  if len(sizes)!=n:rejects['integer']+=1;continue
  Z=[sum(1<<j for j in range(n) if K[i][j]**2*sizes[i]==d[i]*d[j]*sizes[j]) for i in range(n)]
  if any(not ((Z[i]>>i)&1) for i in range(n)) or any(i!=j and ((Z[i]>>j)&1) and ((Z[j]>>i)&1) for i in range(n) for j in range(n)) or any(((Z[i]>>j)&1) and (Z[j]&~Z[i]) for i in range(n) for j in range(n)):
   rejects['poset']+=1;continue
  if any(Z[i].bit_count()!=sizes[i] for i in range(n)):rejects['rows']+=1;continue
  if any((Z[i]&Z[j]).bit_count()**2*d[i]*d[j]!=K[i][j]**2*sizes[i]*sizes[j] for i in range(n) for j in range(n)):
   rejects['gram']+=1;continue
  assert Z[m]==1<<m and all((r>>m)&1 for r in Z)
  answers.append((m,Z))
 return answers,rejects

def enumerate_top(n):
 """All upper-triangular transitive orders on n-1 labels, then append top."""
 k=n-1;pairs=[(i,j) for i in range(k) for j in range(i+1,k)]
 for mask in range(1<<len(pairs)):
  R=[1<<i for i in range(k)]
  for bit,(i,j) in enumerate(pairs):
   if (mask>>bit)&1:R[i]|=1<<j
  if any(((R[i]>>j)&1) and (R[j]&~R[i]) for i in range(k) for j in range(i+1,k)):continue
  yield mask,[r|(1<<k) for r in R]+[1<<k]

def main():
 start=time.perf_counter();records=[];witnesses=[]
 for n in range(1,9):
  t=time.perf_counter();count=0;checked=0;valid=0;same_deg=0;different_deg=0;noniso=0;hist={};rej={};digest=hashlib.sha256()
  for mask,R in enumerate_top(n):
   count+=1;ans,rejections=anchors(R);checked+=n;valid+=len(ans)
   hist[len(ans)]=hist.get(len(ans),0)+1
   for key,v in rejections.items():rej[key]=rej.get(key,0)+v
   assert any(Z==R for _,Z in ans)
   delta=degrees(R)
   ledger=[]
   for m,Z in ans:
    match=degrees(Z)==delta
    perm=iso(R,Z)
    if perm is not None:
     assert sorted(perm)==list(range(n))
     assert all(((R[i]>>j)&1)==((Z[perm[i]]>>perm[j])&1) for i in range(n) for j in range(n))
    if match:same_deg+=1
    else:different_deg+=1
    if match and perm is None:
     noniso+=1;witnesses.append({'n':n,'mask':mask,'anchor':m,'source':R,'candidate':Z,'degrees':delta})
    ledger.append([m,Z,match,perm])
   digest.update((json.dumps([mask,R,ledger,rejections],separators=(',',':'))+'\n').encode())
  rec={'n':n,'raw_masks':1<<((n-1)*(n-2)//2),'transitive_sources':count,'anchors_checked':checked,'valid_anchors':valid,'matching_degree_anchors':same_deg,'different_degree_anchors':different_deg,'nonisomorphic_matching_degree_anchors':noniso,'valid_anchor_histogram':hist,'rejections':rej,'ledger_sha256':digest.hexdigest(),'seconds':time.perf_counter()-t}
  records.append(rec);print(json.dumps(rec),flush=True)
 result={'scope':'All positive-entry finite-poset Gram inputs through n=8, via all compatible linear extensions; no general-n claim','records':records,'counterexamples':witnesses,'total_seconds':time.perf_counter()-start}
 (ROOT/'exact_output.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
