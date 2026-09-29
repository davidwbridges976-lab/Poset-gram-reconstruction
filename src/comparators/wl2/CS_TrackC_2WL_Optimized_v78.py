import itertools
from collections import Counter, defaultdict
import numpy as np

def batch_2wl_optimized(graphs, max_rounds=30):
    """Semantics-identical implementation of the preserved directed batch 2-WL."""
    if not graphs:
        return [], 0, 0
    n=len(graphs[0])
    if any(len(Z)!=n for Z in graphs):
        raise ValueError("shared batch palette requires equal n")
    # Historical tuple order for k=2: (0,0),(0,1),...,(n-1,n-1)
    T=[(i,j) for i in range(n) for j in range(n)]
    # Exact historical atomic features: equality bit + all four directed tuple relations.
    atoms=[]
    per=[]
    for Z in graphs:
        feats=[]
        for i,j in T:
            feat=((int(i==j),),(int(Z[i,i]),int(Z[i,j]),int(Z[j,i]),int(Z[j,j])))
            feats.append(feat); atoms.append(feat)
        per.append(feats)
    pal={x:i for i,x in enumerate(sorted(set(atoms),key=repr))}
    colors=[np.array([pal[x] for x in feats],dtype=np.int64) for feats in per]

    for rnd in range(1,max_rounds+1):
        all_feats=[]; grouped=[]
        for c in colors:
            C=c.reshape(n,n)
            gf=[]
            for i,j in T:
                # Exact historical neighbor list for k=2:
                # v -> ( color(v,j), color(i,v) ), sorted as a multiset.
                neigh=tuple(sorted((int(C[v,j]),int(C[i,v])) for v in range(n)))
                gf.append((int(C[i,j]),neigh))
            grouped.append(gf); all_feats.extend(gf)
        pal={x:i for i,x in enumerate(sorted(set(all_feats),key=repr))}
        new=[np.array([pal[x] for x in gf],dtype=np.int64) for gf in grouped]
        stable=True
        for old,nc in zip(colors,new):
            by=defaultdict(set)
            for a,b in zip(old,nc): by[int(a)].add(int(b))
            if any(len(v)>1 for v in by.values()):
                stable=False; break
        colors=new
        if stable: break
    return [tuple(sorted(Counter(map(int,c)).items())) for c in colors],rnd,n*n
