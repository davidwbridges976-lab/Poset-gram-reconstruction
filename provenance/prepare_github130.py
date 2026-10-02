from pathlib import Path
import shutil,json,hashlib
r=Path('github_update_v130');history=r/'docs/historical/v120';history.mkdir(parents=True)
for name in ['README.md','docs/research-guide.md','docs/problem.md','docs/mathematics.md','docs/limitations.md']:
 shutil.copy(r/name,history/Path(name).name)
read=(r/'README.md').read_text()
read=read.replace('Start with [the abstract, open problems and reading map](docs/research-guide.md). It distinguishes the external mathematical audit at v120 from this repository\'s preserved computational checkpoints.','Start with the [10-page current mathematics PDF](docs/current/Audit10_Current_Mathematics_v130.pdf) or the [research guide](docs/research-guide.md). The mathematical record is frozen at v130; the older v74-v80 computational benchmarks remain separate historical experiments.\n\n**Current status:** normalized Gram data $G$ alone do **not** determine every finite poset. An exact 16-element nonisomorphic pair has identical $G$. For this entire Gram fiber, the comparability-degree multiset separates the two realizations. Whether $G$ together with the unordered comparability-degree multiset determines every finite poset remains **unresolved in this project**. No literature-wide open-problem or novelty claim is made.\n\n[Counterexample note](docs/current/Counterexample_Note.pdf) · [Exact verification](research/v130/README.md) · [Historical v120 guide](docs/historical/v120/research-guide.md)')
read=read.replace('The central question is whether $G$, considered without a supplied labeling or compatible linear extension, determines the finite poset up to isomorphism.','The original question was whether $G$, considered up to simultaneous row and column permutation and without a supplied compatible linear extension, determines the finite poset up to isomorphism. The verified counterexample answers this in the negative. The current target adds the unordered comparability-degree multiset.')
read=read.replace('The corresponding unnormalized products $M^T M$, where $M=Z^{-1}$, and $ZZ^T$ have all-$n$ reconstruction results through determinant-one principal minors. The additional diagonal normalization is the harder problem and **arbitrary-$n$ injectivity remains open**.','The unnormalized matrix $K=ZZ^T$ recovers order directly by $x\\le y$ iff $K_{xy}=K_{yy}$. Labeled upset sizes together with $G$ also recover order. The historical principal-minor results are preserved in [the mathematical foundation](docs/mathematics.md); they do not establish uniqueness for normalized $G$.')
read=read.replace('3. open normalized-reconstruction questions;','3. the refuted general $G$-only claim and unresolved richer-invariant questions;')
read+='\n## Current mathematical evidence (v130)\n\nThe repository now includes the exact counterexample, complete original-fiber anchor enumeration, approved degree/scale audit, and independent exhaustive positive-entry verification through eight elements. The latter covers 101,660 orders in compatible labelings and 807,571 anchor checks; these are not counts of unlabeled posets or distinct Gram matrices. Every valid anchor is isomorphic to its source. This independently confirms older finite evidence and does not narrow the general larger-n obstruction.\n\nSee [the current reproduction map](research/v130/README.md) and [update provenance](provenance/MATHEMATICAL_STATUS_UPDATE_v130.md). The old computational records and licensing exclusion remain unchanged.\n'
(r/'README.md').write_text(read)
(r/'docs/problem.md').write_text(r'''# Reconstruction problem and current status

For a finite poset, let $U_x=\{y:x\le y\}$, including $x$ itself. Set $Z_{xy}=\mathbf{1}[x\le y]$, $K=ZZ^T$, $d_x=|U_x|$, $D=\mathrm{diag}(d)$, and

$$G=D^{-1/2}KD^{-1/2},\qquad G_{xy}=\frac{|U_x\cap U_y|}{\sqrt{d_xd_y}}.$$

## Original question: answered negatively

Does $G$, up to simultaneous row/column permutation, determine the order up to isomorphism? **No.** The verified 16-element pair consists of nonisomorphic orders with identical normalized principal-upset Gram matrices. This is an exact collision. Relabelings of the same order are not counterexamples.

Read the [counterexample note](current/Counterexample_Note.pdf), then run the [exact checks](../research/v130/README.md). All 16 possible maximum anchors were checked for this positive-entry matrix: exactly two pass, producing the original P and Q. Their comparability-degree multisets differ.

## Current question: unresolved in this project

Let $\Delta$ be the unordered multiset of comparability degrees, where the degree of $x$ counts other elements comparable to $x$. Does $(G,\Delta)$ determine every finite poset up to isomorphism?

No general theorem or counterexample for this richer invariant is established here. The known original fiber is separated by degree data; that scoped success does not answer the universal question. Degree values are not assumed to be assigned to Gram rows.

## What survives

- $K$ recovers order by $x\le y$ iff $K_{xy}=K_{yy}$.
- $G$ with labeled upset sizes recovers $K$ and the order.
- $\det G=1/\prod_xd_x$; zero-overlap data recover the number of maxima and comparability components.
- A supplied compatible linear extension permits conditional Cholesky reconstruction.
- Exact candidate-validity tests and maximal-layer reductions enumerate realizations without asserting uniqueness.
- For positive-entry $G$, all realizations occur among its $n$ maximum anchors, with $d_i=1/G_{im}^2$.

The [current PDF](current/Audit10_Current_Mathematics_v130.pdf) provides proofs, assumptions, scope boundaries and open problems.

## Finite evidence

The complete positive-entry class through eight elements has been independently checked by two generators. No nonisomorphic alternatives occur, even without degree data. This is finite computational verification, not arbitrary-size injectivity. It is separate from the older Track A/B/C benchmarks and bounded n15 runs.

## Historical preservation

The [v120 problem statement](historical/v120/problem.md) records the earlier open G-only target. That status is superseded. Historical failures and conditional results remain preserved; they are not rewritten as current general theorems. Novelty and priority remain unresolved.
''')
(r/'docs/research-guide.md').write_text('''# Current research guide - frozen mathematics v130

## Abstract and status

The program studies order information retained by normalized principal-upset overlap matrices. Universal reconstruction from G alone is false: an exact nonisomorphic 16-element pair shares the same G. Exact recovery identities, candidate-validity reductions, degree/scale constraints and positive-entry maximum-anchor enumeration survive. For the original G, the full realization fiber consists of the two original orders; their degree multisets distinguish them. General reconstruction from G plus the unordered comparability-degree multiset remains unresolved in this project.

## Suggested reading order

1. [Current mathematics PDF](current/Audit10_Current_Mathematics_v130.pdf), 10 pages.
2. [Counterexample note](current/Counterexample_Note.pdf), for the construction.
3. [Reproduction map](../research/v130/README.md), for exact code and outputs.
4. [Preliminary novelty audit](current/Standalone_Novelty_Audit.pdf), for bounded prior-art comparisons and unresolved priority.
5. [Historical v120 guide](historical/v120/research-guide.md), only for the older program state.

## Current PDF map

| Pages | Content |
|---|---|
| 1 | Abstract, definitions, reading map and claim boundaries |
| 2 | Direct surviving recovery identities |
| 3 | Exact candidate, maximal-layer and anchor machinery |
| 4 | Open problems, historical scope and evidence map |
| 5-7 | Approved v129 degree/scale and anchor audit; historical physical pages 311-313 |
| 8-10 | Complete v130 positive-entry finite verification; historical physical pages 314-316 |

The extracted pages retain their original addendum footers. Use PDF viewer page numbers and bookmarks for this map. Source paths printed on extracted pages refer to the full historical packet; use the local repository reproduction map for runnable files.

## Evidence boundaries

The new n<=8 test exhausts the positive-entry class only. It independently confirms a portion of the older finite evidence and does not advance the arbitrary-n boundary. Historical q=2 and L=4 branches retain their exact assumptions and pending dependency review. Refuted general diagonal-orbit rigidity and decorated confluence are not current theorems. Dirac explorations are quarantined and supply no physics claim or premise here.

## Repository map

| Location | Purpose |
|---|---|
| docs/current/ | Current 10-page document, construction note and standalone novelty audit |
| research/v130/core/ | Exact counterexample, degree audit and original full-fiber sources/outputs |
| research/v130/positive_entry_n8/ | Primary and independent finite enumerators, control and full certificates |
| provenance/MATHEMATICAL_STATUS_UPDATE_v130.md | Source identities, status correction and history preservation |
| docs/historical/v120/ | Unchanged superseded public-facing documents |
| src/, results/frozen/, provenance/ | Older benchmark sources, records and audit history |

The earlier computational chain ends at v80; mathematical v130 is a different version history. No later finding is back-imported into the earlier experiments. The full cumulative historical packet is preserved separately; the public-facing current document is intentionally concise.
''')
math=(r/'docs/mathematics.md').read_text()
math=math.replace('Diagonal normalization removes directly visible absolute cone sizes. Establishing that this normalized data still forces the poset for arbitrary finite (n) is the open problem.','Diagonal normalization removes directly visible absolute cone sizes. The verified 16-element counterexample now shows that normalized G does not determine every finite poset. The current unresolved question adds the unordered comparability-degree multiset. See [the current problem statement](problem.md).')
math=math.replace('This note records the proved principal-minor reconstruction layer that sits beneath the harder normalized reconstruction problem.','This note preserves the historical principal-minor foundation. The current directly justified surviving results and review boundaries are in [the 10-page PDF](current/Audit10_Current_Mathematics_v130.pdf). The mathematical status was corrected at v130: universal G-only injectivity is false; general G-plus-degree injectivity remains unresolved in this project. This update does not globally re-audit the historical principal-minor proof.')
(r/'docs/mathematics.md').write_text(math)
limits=(r/'docs/limitations.md').read_text()
limits+='\n## Mathematical status update at v130\n\nUniversal G-only injectivity is false by the exact 16-element counterexample. General G-plus-degree injectivity is unresolved in this project. The newer repository addition includes an exhaustive positive-entry-only n<=8 generator and independent verifier; the historical limitation above refers to the earlier broader enumeration and its original packaging audit. The new finite test is not an all-n theorem. The old Track A/B/C sources and timing records are unchanged.\n'
(r/'docs/limitations.md').write_text(limits)
with (r/'REPRODUCING.md').open('a') as f:f.write('\n## Current mathematics at v130\n\nFor the exact counterexample, complete original-fiber audit, degree/scale checks and complete positive-entry n<=8 verification, use [research/v130/README.md](research/v130/README.md). These newly included sources use Python standard library only and are separate from the frozen benchmarks described above.\n')
current=r/'docs/current';current.mkdir()
for name in ['Audit10_Current_Mathematics_v130.pdf','Audit10_Standalone_Novelty_and_Prior_Art_Audit.pdf']:
 shutil.copy(Path('output')/name,current/('Standalone_Novelty_Audit.pdf' if 'Standalone' in name else name))
shutil.copy('reader_packet_v129/01_PROBLEM_AND_COUNTEREXAMPLE/Counterexample_Note.pdf',current/'Counterexample_Note.pdf')
dest=r/'research/v130';dest.mkdir(parents=True)
shutil.copytree('reader_packet_v129/03_REPRODUCE',dest/'core')
shutil.copytree('work_next/Positive_Entry_Degree_Filter_Exhaustive_n8',dest/'positive_entry_n8',ignore=shutil.ignore_patterns('__pycache__','pack.py'))
(dest/'README.md').write_text('''# Exact mathematical evidence at frozen v130

All checks below use Python 3.10+ and the standard library only. They are separate from the frozen v74-v80 computational benchmark chain. No new mathematical attack was performed for this repository update.

## Counterexample, scale audit and full original fiber

From the repository root:

```sh
python3 research/v130/core/run_all.py
```

The runner checks the exact normalized Gram collision, order axioms, nonisomorphism certificate, degree/scale examples, all 16 original maximum anchors, and their independent verification. Original relative input layout is preserved. The reader runner is an executed convenience script from the earlier reader edition, not the original historical attack implementation.

## Complete positive-entry verification through eight elements

```sh
python3 research/v130/positive_entry_n8/check.py
python3 research/v130/positive_entry_n8/verify.py
python3 research/v130/positive_entry_n8/control.py
```

The primary integer/bitset generator checks all transitive upper-triangular orders below an appended greatest element. The independent generator uses predecessor ideals and exact rational/set-based closure. Every source and anchor outcome, valid candidate and isomorphism certificate is retained in independent_ledger.jsonl.gz. The control must detect the known 16-element nonisomorphic G-only collision and its degree difference.

Frozen results: 101,660 orders in compatible labelings; 807,571 anchor checks; 103,562 valid anchors; zero nonisomorphic survivors. These counts are not unlabeled-poset counts or distinct Gram matrices. The scope is positive-entry G only, through eight elements. General G-plus-degree injectivity is unresolved.

Scripts overwrite their own generated outputs on rerun. Timing fields and gzip timestamp bytes can change; compare mathematical counts and certificates, not timing-dependent byte identities. Frozen original records and SHA256.json are retained for inspection. Parent checkpoint names/paths in original reports refer to the separately preserved full historical packet. pack.py was a workspace packaging script, not required to reproduce mathematics, and is not included here.

The publication-import checksums are in SHA256SUMS.txt. Copies are byte-identical to their supplied frozen or reader-edition sources unless specifically described as new documentation.
''')
(dest/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(dest))+'\n' for p in sorted(dest.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.txt'))
provenance='''# Mathematical status update - frozen v130

Prepared 2 October 2026. This repository update corrects current-facing status and publishes previously executed evidence; no new attack or benchmark result is created.

## Status correction

The former public text said general normalized injectivity was unresolved at mathematical v120. The later exact 16-element nonisomorphic collision refutes universal G-only injectivity. This correction is prominently recorded in README, the problem statement and current guide. General reconstruction from G plus an unordered comparability-degree multiset remains unresolved in this project.

## Preservation

The previous README, research guide, problem statement, mathematical foundation and limitations are copied unchanged to docs/historical/v120. Their status claims are historical. Existing frozen benchmarks, timing evidence, source exclusions and license scope are not altered. The earlier mathematical cumulative PDF and full ZIP remain preserved separately, with their source digests below. No 316-page cumulative document is used as the current reader entry.

## Source and scope

Current PDF: 10 pages, four introduction/survivor pages followed by unchanged historical physical pages 311-316. The counterexample note remains standalone. The preliminary novelty audit is bounded and does not certify novelty or priority.

Exact code and frozen outputs are copied under research/v130; the portable reader runner is explicitly a later convenience script. The independent finite ledger records every generated order and anchor certificate. SHA256SUMS.txt records the imported file bytes. Reruns may update timings; their results must not replace frozen history silently.

The n<=8 positive-entry check independently confirms historical finite evidence, without narrowing the general larger-n obstruction. Conditional q=2/L=4 branches are not broadly promoted. Dirac work remains quarantined. No claimed universal uniqueness depends on finite testing.

## Source archive identities

Full frozen v130 ZIP SHA256: 7559af0a4c2daec43938d9bfd91aaf99a00bd5c65bee84f021058f55aaed2c2f.

The current reader-packet organization verification is copied below. This document update does not re-license excluded third-party historical source.
'''
(r/'provenance/MATHEMATICAL_STATUS_UPDATE_v130.md').write_text(provenance)
shutil.copy('current_packet_v130/03_OPEN_PROBLEMS_AND_PROVENANCE/ORGANIZATION_VERIFICATION.json',r/'provenance/CURRENT_READER_ORGANIZATION_v130.json')
shutil.copy(__file__,r/'provenance/prepare_github130.py')
print('Prepared current status, preserved historical docs, exact evidence and three PDFs.')
