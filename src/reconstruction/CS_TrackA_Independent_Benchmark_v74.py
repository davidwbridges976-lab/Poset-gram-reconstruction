import itertools,time,json,hashlib,sys,statistics,os,csv,argparse
from pathlib import Path
from fractions import Fraction
import numpy as np, networkx as nx
SEED=20260935; TLIMIT_MS=10000

def height2(B):
 a,b=B.shape; Z=np.eye(a+b,dtype=np.int8); Z[:a,a:]=B; return Z

def iso(Z1,Z2):
 G1=nx.from_numpy_array(np.asarray(Z1,dtype=np.int8),create_using=nx.DiGraph); G2=nx.from_numpy_array(np.asarray(Z2,dtype=np.int8),create_using=nx.DiGraph); return nx.is_isomorphic(G1,G2)
def dedup(graphs):
 reps=[]; seen=set(); perm_cache={}
 for Z in graphs:
  n=len(Z); m=n//2; B=np.asarray(Z[:m,m:],dtype=np.uint8)
  if m not in perm_cache: perm_cache[m]=np.array(list(itertools.permutations(range(m))),dtype=np.int16)
  P=perm_cache[m]; BP=B[P,:]  # (#perm,m,m)
  weights=(1<<np.arange(m,dtype=np.uint64)).reshape(1,m,1)
  colcodes=(BP.astype(np.uint64)*weights).sum(axis=1)
  colcodes.sort(axis=1)
  # lexicographically minimal sorted-column code row
  order=np.lexsort(tuple(colcodes[:,j] for j in range(m-1,-1,-1)))
  best=tuple(int(x) for x in colcodes[order[0]])
  if best not in seen:
   seen.add(best); reps.append(Z)
 return reps
def exact_q_and_G(Z):
 Zi=Z.astype(int); K=Zi@Zi.T; d=np.diag(K).astype(int); n=len(Z); q=[[Fraction(int(K[i,j]*K[i,j]),int(d[i]*d[j])) for j in range(n)] for i in range(n)]; G=K/np.sqrt(np.outer(d,d)); return q,G
def maxorth_clique(G,tol=1e-12):
 n=len(G); H=nx.Graph(); H.add_nodes_from(range(n))
 for i in range(n):
  for j in range(i+1,n):
   if abs(G[i,j])<=tol:H.add_edge(i,j)
 cl=list(nx.find_cliques(H)); m=max(map(len,cl)) if cl else 0; return [sorted(C) for C in cl if len(C)==m]
def optimized_engine_from_G(G,target_Z):
 n=len(G); gi=np.diag(np.linalg.inv(G)); recovered=[]
 for J in maxorth_clique(G):
  ds=[]; ok=True
  for x in range(n):
   v=[G[x,j] for j in J if G[x,j]>1e-9]
   if not v or max(v)-min(v)>1e-9:ok=False;break
   q=1/v[0]**2; qi=int(round(q))
   if abs(q-qi)>1e-7 or not 1<=qi<=n:ok=False;break
   ds.append(qi)
  if not ok:continue
  if any(di>g+1e-7 or abs(g/di-round(g/di))>1e-7 for g,di in zip(gi,ds)):continue
  target=1/np.linalg.det(G)
  if abs(np.prod(ds)-target)>1e-6*max(1,abs(target)):continue
  Kf=G*np.sqrt(np.outer(ds,ds)); K=np.rint(Kf).astype(int)
  if np.max(np.abs(Kf-K))>1e-7:continue
  Zr=(K==np.diag(K)[None,:]).astype(np.int8)
  if np.array_equal(K,Zr.astype(int)@Zr.astype(int).T):recovered.append(Zr)
 return any(iso(target_Z,R) for R in recovered)

def population():
 rng=np.random.default_rng(SEED); raw4=[]
 for mask in range(1<<16):
  B=np.array([(mask>>i)&1 for i in range(16)],dtype=np.int8).reshape(4,4); rs=B.sum(1);cs=B.sum(0)
  if len(set(map(int,rs)))==1 and len(set(map(int,cs)))==1 and rs[0]==cs[0]:raw4.append(height2(B))
 g4=dedup(raw4); rows=list(itertools.combinations(range(5),2));raw5=[]
 for choices in itertools.product(rows,repeat=5):
  B=np.zeros((5,5),dtype=np.int8)
  for i,cols in enumerate(choices):B[i,list(cols)]=1
  if np.all(B.sum(0)==2):raw5.append(height2(B))
 g5=dedup(raw5)
 def rr(m=8,dg=3):
  for _ in range(10000):
   B=np.zeros((m,m),dtype=np.int8);ok=True
   for _ in range(dg):
    p=rng.permutation(m)
    if any(B[i,p[i]] for i in range(m)):ok=False;break
    B[np.arange(m),p]=1
   if ok:return height2(B)
  raise RuntimeError
 g8=dedup([rr() for _ in range(120)]); assert [len(g4),len(g5),len(g8)]==[6,2,37]
 arr=[]
 for fam,gs in [('regular4x4',g4),('degree2_regular5x5',g5),('random8_3',g8)]:
  for fi,Z in enumerate(gs):q,G=exact_q_and_G(Z);arr.append((fam,fi,Z,q,G))
 return arr

def main():
    arr=population()
    assert len(arr)==45
    outdir=Path("/mnt/data/v74_trackA_results")
    outdir.mkdir(exist_ok=True)
    warm=[]
    for fam in ["regular4x4","degree2_regular5x5","random8_3"]:
        _,fi,Z,q,G=next(x for x in arr if x[0]==fam)
        t=time.perf_counter()
        ok=optimized_engine_from_G(G,Z)
        sec=time.perf_counter()-t
        warm.append({"family":fam,"family_index":fi,"seconds":sec,"validated_correct":bool(ok)})
    (outdir/"warmup.json").write_text(json.dumps(warm,indent=2)+"\n")

    raw=outdir/"trackA_raw.jsonl"
    records=[]
    with raw.open("w") as f:
        for rep in range(1,8):
            for gi,(fam,fi,Z,q,G) in enumerate(arr):
                t=time.perf_counter()
                ok=optimized_engine_from_G(G,Z)
                sec=time.perf_counter()-t
                rec={"rep":rep,"global_instance_index":gi,"family":fam,"family_index":fi,
                     "seconds":sec,"validated_correct":bool(ok)}
                f.write(json.dumps(rec)+"\n"); f.flush(); os.fsync(f.fileno())
                records.append(rec)
    assert len(records)==315
    assert all(r["validated_correct"] for r in records)
    fam_summary={}
    for fam in ["regular4x4","degree2_regular5x5","random8_3"]:
        rs=[r for r in records if r["family"]==fam]
        fam_summary[fam]={
          "records":len(rs),
          "median_per_instance_seconds":statistics.median(r["seconds"] for r in rs),
          "min_seconds":min(r["seconds"] for r in rs),
          "max_seconds":max(r["seconds"] for r in rs)
        }
    rep_totals=[]
    for rep in range(1,8):
        rs=[r for r in records if r["rep"]==rep]
        rep_totals.append({"rep":rep,"total_seconds":sum(r["seconds"] for r in rs)})
    summary={
      "track":"A","method":"v56/v57 optimized whole-engine path",
      "population":{"regular4x4":6,"degree2_regular5x5":2,"random8_3":37,"total":45,"seed":SEED},
      "measured_repetitions":7,"measured_records":315,
      "correct_records":sum(r["validated_correct"] for r in records),
      "all_correct":all(r["validated_correct"] for r in records),
      "warmup":warm,"family_summary":fam_summary,
      "rep_totals":rep_totals,
      "median_45_instance_total_seconds":statistics.median(x["total_seconds"] for x in rep_totals),
      "raw_sha256":hashlib.sha256(raw.read_bytes()).hexdigest()
    }
    (outdir/"trackA_summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps(summary,indent=2))
if __name__=="__main__":
    main()
