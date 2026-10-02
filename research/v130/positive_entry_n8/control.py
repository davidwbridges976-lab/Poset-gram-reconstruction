"""Known-collision control for the exact candidate and isomorphism tests."""
from pathlib import Path
import json
from check import anchors,iso,degrees
ROOT=Path(__file__).resolve().parent
phi=json.loads((ROOT/'counterexample_input.json').read_text())['phi']
subset=lambda a,b:a&b==a
P=[];Q=[]
for i in range(16):
 p=q=0
 for j in range(16):
  a,b=i%8,j%8
  if i//8==j//8:
   rp=subset(a,b);rq=subset(b,a)
  elif i<8<=j:
   rp=subset(phi[a],b);rq=subset(b,phi[a])
  else:rp=rq=False
  if rp:p|=1<<j
  if rq:q|=1<<j
 P.append(p);Q.append(q)
found,rejected=anchors(P)
assert len(found)==2 and dict(found)[8]==Q and dict(found)[15]==P
assert iso(P,Q) is None and degrees(P)!=degrees(Q)
out={'known_G_only_collision_detected':True,'nonisomorphism_detected':True,'degree_difference_detected':True,'valid_anchors':[m for m,_ in found],'rejections':rejected,'P_degrees':degrees(P),'Q_degrees':degrees(Q)}
(ROOT/'control_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
