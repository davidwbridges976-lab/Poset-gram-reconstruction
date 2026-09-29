import itertools, time, json, hashlib, platform, sys
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np
import networkx as nx

SEED=20260929
rng=np.random.default_rng(SEED)

# Formal AO4: current partial optimized engine vs directed 2-WL/3-WL.
# No new mathematics is added to the engine.

def height2(B):
    a,b=B.shape; Z=np.eye(a+b,dtype=np.int8); Z[:a,a:]=B; return Z

def incidence_population(a,b):
    out=[]
    for mask in range(1<<(a*b)):
        B=np.zeros((a,b),dtype=np.int8)
        for bit in range(a*b): B[bit//b,bit%b]=(mask>>bit)&1
        out.append(height2(B))
    return out

def batch_kwl(graphs,k,max_rounds=30):
    n=len(graphs[0]); T=list(itertools.product(range(n),repeat=k)); tid={t:i for i,t in enumerate(T)}
    atoms=[]
    for Z in graphs:
        for t in T:
            eq=tuple(int(t[i]==t[j]) for i in range(k) for j in range(i+1,k))
            rel=tuple(int(Z[t[i],t[j]]) for i in range(k) for j in range(k))
            atoms.append((eq,rel))
    pal={x:i for i,x in enumerate(sorted(set(atoms),key=repr))}
    colors=[]
    for Z in graphs:
        c=[]
        for t in T:
            eq=tuple(int(t[i]==t[j]) for i in range(k) for j in range(i+1,k))
            rel=tuple(int(Z[t[i],t[j]]) for i in range(k) for j in range(k))
            c.append(pal[(eq,rel)])
        colors.append(np.array(c,dtype=np.int64))
    for rnd in range(1,max_rounds+1):
        feats=[]; pg=[]
        for c in colors:
            gf=[]
            for z,t in enumerate(T):
                neigh=[]
                for v in range(n):
                    neigh.append(tuple(int(c[tid[t[:p]+(v,)+t[p+1:]]]) for p in range(k)))
                gf.append((int(c[z]),tuple(sorted(neigh))))
            pg.append(gf); feats.extend(gf)
        pal={x:i for i,x in enumerate(sorted(set(feats),key=repr))}
        new=[np.array([pal[x] for x in gf],dtype=np.int64) for gf in pg]
        stable=True
        for old,nc in zip(colors,new):
            # refinement stabilization: no old color class split further
            by=defaultdict(set)
            for a,b in zip(old,nc): by[int(a)].add(int(b))
            if any(len(v)>1 for v in by.values()): stable=False; break
        colors=new
        if stable: break
    # signature uses final color counts; shared palette across population
    return [tuple(sorted(Counter(map(int,c)).items())) for c in colors],rnd,len(T)

def random_poset(n,p):
    Z=np.eye(n,dtype=np.int8)
    for i in range(n):
        for j in range(i+1,n):
            if rng.random()<p: Z[i,j]=1
    for k in range(n):
        for i in range(n):
            if Z[i,k]: Z[i,:] |= Z[k,:]
    return Z

def iso(Z1,Z2):
    if len(Z1)!=len(Z2): return False
    G1=nx.from_numpy_array(Z1,create_using=nx.DiGraph); G2=nx.from_numpy_array(Z2,create_using=nx.DiGraph)
    return nx.is_isomorphic(G1,G2)

def dedup(graphs):
    reps=[]
    for Z in graphs:
        if not any(iso(Z,R) for R in reps): reps.append(Z)
    return reps

def gram(Z):
    K=Z.astype(int)@Z.astype(int).T; d=np.diag(K); return K/np.sqrt(np.outer(d,d))

def maxorth(G):
    n=len(G); best=0; out=[]
    for mask in range(1,1<<n):
        I=[i for i in range(n) if mask>>i&1]
        if len(I)<best: continue
        if all(abs(G[a,b])<1e-12 for a,b in itertools.combinations(I,2)):
            if len(I)>best: best=len(I); out=[]
            out.append(I)
    return out

def engine_run(Z):
    G=gram(Z); n=len(G); gi=np.diag(np.linalg.inv(G)); cand=rej22=rej19=closure=0; recovered=[]
    for J in maxorth(G):
        ds=[]; ok=True
        for x in range(n):
            v=[G[x,j] for j in J if G[x,j]>1e-9]
            if not v or max(v)-min(v)>1e-9: ok=False; break
            q=1/v[0]**2; qi=int(round(q))
            if abs(q-qi)>1e-7 or not 1<=qi<=n: ok=False; break
            ds.append(qi)
        if not ok: continue
        cand+=1
        if any(di>g+1e-7 or abs(g/di-round(g/di))>1e-7 for g,di in zip(gi,ds)):
            rej22+=1; continue
        target=1/np.linalg.det(G)
        if abs(np.prod(ds)-target)>1e-6*max(1,abs(target)):
            rej19+=1; continue
        Kf=G*np.sqrt(np.outer(ds,ds)); K=np.rint(Kf).astype(int)
        if np.max(np.abs(Kf-K))>1e-7: continue
        Zr=(K==np.diag(K)[None,:]).astype(np.int8)
        if np.array_equal(K,Zr.astype(int)@Zr.astype(int).T):
            closure+=1; recovered.append(Zr)
    correct=any(iso(Z,R) for R in recovered)
    return dict(candidates=cand,rejected_A22=rej22,rejected_A19=rej19,closure_valid=closure,correct_reconstruction=correct)

def collision_stats(graphs,sigs):
    buckets=defaultdict(list)
    for i,s in enumerate(sigs): buckets[repr(s)].append(i)
    coll=[]
    for ids in buckets.values():
        if len(ids)>1:
            # population deduped, so every pair here is nonisomorphic
            coll.append(ids)
    return dict(classes=len(buckets),collision_classes=len(coll),structures_in_collisions=sum(map(len,coll)),collision_pairs=sum(len(x)*(len(x)-1)//2 for x in coll))

# Stage 1 historical controls
controls={}
for a,b,expect in [(3,3,36),(3,4,87),(4,3,87)]:
    gs=incidence_population(a,b); t=time.perf_counter(); sig,r,states=batch_kwl(gs,2); dt=time.perf_counter()-t
    controls[f'{a}x{b}']=dict(matrices=len(gs),expected_classes=expect,recovered_classes=len(set(sig)),rounds=r,pass_control=len(set(sig))==expect,seconds=dt)
assert all(x['pass_control'] for x in controls.values())

# Stage 2 controlled broader population: n=8, same seed and 160 p-grid draws as v28 benchmark.
raw=[random_poset(8,float(p)) for p in np.linspace(.12,.72,160)]
graphs=dedup(raw)

# Engine timing and correctness
engine=[]; t=time.perf_counter()
for Z in graphs: engine.append(engine_run(Z))
engine_seconds=time.perf_counter()-t

# WL timing
t=time.perf_counter(); s2,r2,st2=batch_kwl(graphs,2); sec2=time.perf_counter()-t
t=time.perf_counter(); s3,r3,st3=batch_kwl(graphs,3); sec3=time.perf_counter()-t

result={
 'attack':'CS-AO4 — WL Power-to-Result Benchmark',
 'status':'FORMAL ATTACK COMPLETE — AWAITING USER REVIEW; NOT FROZEN',
 'seed':SEED,
 'environment':{'python':sys.version.split()[0],'numpy':np.__version__,'platform':platform.platform()},
 'firewall':[
  'Current v28 partial optimized engine only; no additional mathematics added.',
  'Historical commentary outputs are not imported as evidence; controls are rerun here.',
  'Finite populations do not establish general WL dominance/equivalence.',
  'Python wall time is implementation-specific, not an asymptotic or hardware theorem.',
  'Common comparison layer is distinguishability; exact reconstruction/certification is reported separately.'
 ],
 'historical_2wl_controls':controls,
 'population':{'generated':len(raw),'nonisomorphic_after_exact_dedup':len(graphs),'n':8,'p_range':[.12,.72]},
 'partial_engine':{
   'correct_reconstructions':sum(x['correct_reconstruction'] for x in engine),
   'failures':sum(not x['correct_reconstruction'] for x in engine),
   'candidate_total':sum(x['candidates'] for x in engine),
   'A22_reject_total':sum(x['rejected_A22'] for x in engine),
   'A19_reject_total':sum(x['rejected_A19'] for x in engine),
   'closure_valid_total':sum(x['closure_valid'] for x in engine),
   'seconds':engine_seconds
 },
 '2WL':{**collision_stats(graphs,s2),'rounds':r2,'states_per_structure':st2,'total_tuple_states':st2*len(graphs),'seconds':sec2},
 '3WL':{**collision_stats(graphs,s3),'rounds':r3,'states_per_structure':st3,'total_tuple_states':st3*len(graphs),'seconds':sec3},
}
# Power-to-result descriptors only; no generalized claim.
result['observed_ratios']={
 '2WL_time_over_engine':sec2/engine_seconds if engine_seconds else None,
 '3WL_time_over_engine':sec3/engine_seconds if engine_seconds else None,
 '3WL_tuple_states_over_2WL':(st3/st2),
}

out=Path('/mnt/data/CS_AO4_WL_PowerToResult'); out.mkdir(exist_ok=True)
js=out/'AO4_results.json'; js.write_text(json.dumps(result,indent=2),encoding='utf-8')
script=Path('/mnt/data/cs_ao4_wl_power_result.py')
manifest={'AO4_results.json':hashlib.sha256(js.read_bytes()).hexdigest(),'cs_ao4_wl_power_result.py':hashlib.sha256(script.read_bytes()).hexdigest()}
(out/'SHA256.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
print('RESULT_SHA256',manifest['AO4_results.json'])
print('SCRIPT_SHA256',manifest['cs_ao4_wl_power_result.py'])
