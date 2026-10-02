"""New reader runner, executed during packet production."""
from pathlib import Path
import subprocess,sys,json
root=Path(__file__).parent
scripts=['verify_counterexample.py','core/08_DEGREE_SCALE_RECONSTRUCTION_AUDIT/check.py','core/09_ORIGINAL_FIBER_MAXIMUM_ANCHOR/check.py','core/09_ORIGINAL_FIBER_MAXIMUM_ANCHOR/verify.py']
results=[]
for script in scripts:
 p=subprocess.run([sys.executable,str(root/script)],capture_output=True,text=True)
 results.append({'script':script,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 assert p.returncode==0,p.stderr
(root/'EXECUTED_READER_RUN.json').write_text(json.dumps(results,indent=2)+'\n')
print('PASS: counterexample, scale audit, complete anchor enumeration, independent anchor audit')
