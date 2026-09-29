import json, random, time, hashlib
from pathlib import Path
import numpy as np
import importlib.util

SEED=20260935
REPS=7
OUT=Path("v74_trackA_results")
OUT.mkdir(exist_ok=True)

# Load the frozen v56 optimized engine source directly from the frozen predecessor chain.
spec=importlib.util.spec_from_file_location("router","CS_Candidate_Optimized_Router_v56.py")
router=importlib.util.module_from_spec(spec); spec.loader.exec_module(router)

def tc_from_edges(n, edges):
    Z=np.eye(n,dtype=np.int64)
    for i,j in edges: Z[i,j]=1
    for k in range(n):
        for i in range(n):
            if Z[i,k]:
                Z[i,:] |= Z[k,:]
    return Z

def regular_posets(m):
    out=[]
    for mask in range(1<<(m*m)):
        B=np.array([(mask>>k)&1 for k in range(m*m)],dtype=np.int64).reshape(m,m)
        if np.all(B.sum(0)==2) and np.all(B.sum(1)==2):
            Z=np.eye(2*m,dtype=np.int64); Z[:m,m:]=B; out.append(Z)
    return out

def random_height2(n=8,p=.3):
    m=n//2
    B=(np.random.random((m,n-m))<p).astype(np.int64)
    Z=np.eye(n,dtype=np.int64); Z[:m,m:]=B
    return Z

def key(Z): return bytes(Z.astype(np.uint8).ravel())

random.seed(SEED); np.random.seed(SEED)
reg4=regular_posets(4)
reg5=[Z for Z in regular_posets(5) if np.all(Z[:5,5:].sum(0)==2) and np.all(Z[:5,5:].sum(1)==2)]
# deduplicate under raw labelled matrices only, preserving protocol population construction.
seen=set(); rnd=[]
while len(rnd)<37:
    Z=random_height2(16,.3); k=key(Z)
    if k not in seen: seen.add(k); rnd.append(Z)
pop=[("regular4x4",Z) for Z in reg4]+[("degree2_regular5x5",Z) for Z in reg5]+[("random8_3",Z) for Z in rnd]

def one(Z):
    G=router.gram(Z)
    t=time.perf_counter()
    R=router.route_certified_state(G)
    dt=time.perf_counter()-t
    ok=bool(R.get("pass")) and np.array_equal(R["Z"],Z)
    return dt,ok,R.get("route")

# one untimed warm-up per family
warm=[]
for fam in ["regular4x4","degree2_regular5x5","random8_3"]:
    Z=next(Z for f,Z in pop if f==fam)
    dt,ok,route=one(Z); warm.append({"family":fam,"ok":ok,"route":route})
(OUT/"warmup.json").write_text(json.dumps(warm,indent=2))

raw=[]
rep_totals=[]
for rep in range(REPS):
    total=0.0
    for idx,(fam,Z) in enumerate(pop):
        dt,ok,route=one(Z); total+=dt
        rec={"rep":rep+1,"index":idx,"family":fam,"n":len(Z),"seconds":dt,"ok":ok,"route":route}
        raw.append(rec)
    rep_totals.append(total)

with (OUT/"trackA_raw.jsonl").open("w") as f:
    for r in raw: f.write(json.dumps(r)+"\n")
summary={
    "seed":SEED,"repetitions":REPS,"population":len(pop),
    "family_counts":{fam:sum(1 for f,_ in pop if f==fam) for fam in sorted(set(f for f,_ in pop))},
    "correct":sum(r["ok"] for r in raw),"total":len(raw),
    "rep_totals":rep_totals,"median_total":float(np.median(rep_totals)),
}
(OUT/"trackA_summary.json").write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
