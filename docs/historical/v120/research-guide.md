# Research guide: abstract, open problems and reading routes

This is a documentation bridge to the separately frozen Audit 10 mathematical packet (v120). The packet/PDF maps below refer to that external research packet, not files included in this repository. They do not amend or promote the repository's frozen v74–v80 computational results.

Documentation companion to frozen mathematics v120, prepared 2026-10-01. No new attack, theorem promotion, or source correction. Repository sources were fetched for this guide; no benchmarks were rerun.

## Abstract

This research program investigates whether a finite poset is determined, up to isomorphism, by the normalized intersection Gram matrix of its principal upsets. For a zeta matrix Z, define K=ZZ^T, d_x=|U_x| and G_xy=|U_x intersect U_y|/sqrt(d_x d_y). The unnormalized matrix K recovers order by saturation, while normalization conceals the individual upset sizes. The retained audit develops conditional Cholesky reconstruction, principal-minor characterizations, intrinsic maximal-layer reductions, and exact diagonal-transport constraints. The larger research record reports collision-free exhaustive checks through n<=8; the public repository separately preserves a finite reconstruction benchmark, an incomplete solver experiment, directed 2-WL records, and bounded n15 tests. These computations do not establish arbitrary-n injectivity. At frozen v120, the active First Saturation-Deletion Defect analysis has reduced one exterior antichain subcase to mutually closed common-upper/common-lower-bound attachment pairs with reciprocal cardinalities. Full intermediate mixed-Gram compatibility and other coverage cases remain unresolved. The program has not established general normalized-poset injectivity, and this summary makes no certified novelty or literature-wide open-problem claim.

## Construction and established scope

U_x={y:x<=y}; Z_xy=1[x<=y]; K=ZZ^T; d_x=K_xx; Delta=diag(d_x); G=Delta^(-1/2)KDelta^(-1/2). The diagonal is called Delta here to avoid confusion with the later witness profile D. Exact K recovers x<=y iff K_xy=K_yy. The audit retains conditional Cholesky reconstruction with a supplied linear extension, principal-minor ideal/filter characterizations, comparability-component recovery and maximal-basis/full-closure reductions. The repaired q=2 result applies to its exact two-sided extremal branch. None is presented as general normalized injectivity.

## Open problems

### P1 - General normalized reconstruction

Given two finite posets P,Q, prove that G_Q=Pi G_P Pi^T for a permutation matrix Pi implies P is isomorphic to Q, or construct a nonisomorphic counterexample satisfying the full definition. Status: not established by this program. Finite evidence and conditional results do not settle it. Source: original PDF pp.1-6; repository docs/problem.md.

### P2 - Exact-closure diagonal orbit rigidity

For fixed G, let a positive candidate diagonal Delta produce K_Delta=Delta^(1/2) G Delta^(1/2), and define (Z_Delta)_xy=1[(K_Delta)_xy=(K_Delta)_yy]. A valid realization requires a poset zeta matrix and K_Delta=Z_Delta Z_Delta^T. Determine whether every such realization has Delta=Pi Delta_0 Pi^T for some Pi in Aut(G), where Delta_0 is a known source realization. That would recover only symmetry-related scales and orders. Status: OPEN in the audit. Use the original exact-closure hypotheses; integrality or cardinality self-consistency alone is insufficient. Source: original pp.4-6.

### P3 - First Saturation-Deletion Defect

In competing exact realizations K'=SKS, with S=diag(s_x), examine an original relation u<P v that is deleted at the first defect on the retained transport route. The strict branch has 1<q=s_v/s_u<rho=d_u/d_v and u incomparable v in P'. Can the full transitivity, intersection, boundary and principal-minor constraints coexist, or must the defect be excluded? Source: original pp.185-188 and later attacks. Do not assume an arbitrary predecessor chain or cover not licensed by the source. Status: OPEN; v120 is a conditional subcase, not closure of this entire problem.

### P4 - Immediate frontier: intermediate attachment compatibility

Under the later threshold hypotheses q=L/(L-1), L>2, an exterior residual atomic witness and antichain witness profile, v120 proves H_a(u)=LB_a(T_a(u)), T_a(u)=UB_a(H_a(u)), and |T_a(u)||H_a(u)|=L. Lower/upper bounds are taken within the paired block W_a. Test whether the full intermediate mixed-Gram equations force exclusion or an appropriate global symmetry, or whether additional constraints are needed. NEXT / NOT RUN. Source: original pp.277-279. Reciprocal sizes and mutual bound closure establish necessary constraints, not full Gram completion.

### P5 - Coverage cases beyond the antichain reduction

Preserved gaps: general non-antichain profiles; surviving internal atomic cones with L>=8 divisible by 4 and their external attachments; L=4 local diamond attachments; empty J_x replacement sectors and empty reversing classes. Each needs its own applicability/existence analysis. No assertion that an atomic witness always exists, or that local self-duality implies global isomorphism, is available. Source: original pp.263-279, especially v116-v120 scope/roadmaps.

### P6 - Other retained branches and proof audit

L=2 pure-C-addition remains unresolved. Strict q>L/(L-1) is NOT RUN. Mixed-terminal/all-joint-replacement cases remain OPEN. The full dependency audit is deferred: verify retained hypotheses, correction precedence and complete case coverage before promoting an overarching theorem. These are preserved roadmap entries, not attacks performed for this guide. Source: v120 ROADMAP_STATUS.txt and current-state guide.

### Exact equation at the immediate frontier

For u in E, b in W_a, e_u=|U_u intersect E| and f_b=|U_b|, full transport requires:

e_u f_b |H_a(u) intersect Down_Wa(b)| = L |T_a(u) intersect U_b|.

For u,v in E it additionally requires:

e_u e_v [ell_E(u,v)+sum_a |H_a(u) intersect H_a(v)|] = L [k_E(u,v)+sum_a |T_a(u) intersect T_a(v)|].

Here k_E counts common original E-successors and ell_E counts common original E-predecessors. Saturation does not by itself verify nonsaturated overlaps.

## Packet map

| Location | Purpose |
|---|---|
| READ_ME_FIRST.md | Entry point for the approved v120 readability refresh. |
| 00_START_HERE/READABILITY_GUIDE/ | Current state, notation/scope, reading routes, 90-entry historical addendum index and source catalog. |
| 02_CURRENT_CANONICAL_AUDIT/ | Original v120 PDF and navigated readability PDF; original historical PDFs also retained. |
| 04_ADDENDA/ | Individual historical addendum PDFs; use the index for exact canonical page locations. |
| 09_EXPERIMENTAL_NOTES/ | Recent attack reports, roadmaps, provenance and executed artifact-production code. Read the exact scope in each report. |
| 10_FINAL_MANUSCRIPT_ROUGH_DRAFT_DOWNSTREAM/ | Structural supplements and exposition plan. Not promotion of the main theorem. |
| Audit10_Poset_Reconstruction_Research/ | Retained nested historical packet: earlier code, provenance, citations, version history, historical and separate branches. |
| 09_EXPERIMENTAL_NOTES_SEPARATE/ and 11_QUARANTINED_OUTWARD_BRANCHES/ | Separate material. No import into the proof without the required audit. |
| v120_READABILITY_REFRESH_SHA256.txt | Current refreshed-packet manifest. Older manifests describe earlier freezes. |

## Canonical PDF map

Original v120 has 279 pages. Approved readability PDF has nine front-matter pages followed by those 279 preserved pages. Add 9 to an original PDF physical page to locate it in the readability PDF. Historical printed page labels may differ; use physical pages/bookmarks.

| Topic | Original physical pages | Readability physical pages |
|---|---|---|
| Reader guide and summary | Not part of original | 1-9 |
| Origin and central question | 1 | 10 |
| Conditional reconstruction and finite evidence | 2-4 | 11-13 |
| Maximal-basis/full-closure reduction | 6 | 15 |
| v28 transparency correction | 74 | 83 |
| v30 repaired q=2 branch | 77-78 | 86-87 |
| First deletion-defect formulation | 185-188 | 194-197 |
| v112 repeated-pattern correction | 256-258 | 265-267 |
| v116 atomic-witness scope | 263-266 | 272-275 |
| v117 mixed-Gram dichotomy | 267-269 | 276-278 |
| v118 full-closure test | 270-272 | 279-281 |
| v119 antichain attachment closure | 273-276 | 282-285 |
| v120 current mutual-bound closure | 277-279 | 286-288 |

## Repository map

https://github.com/davidwbridges976-lab/Poset-gram-reconstruction

| Location | Purpose |
|---|---|
| README.md | Quick orientation and claim boundaries. |
| docs/problem.md and docs/mathematics.md | Normalized reconstruction question and unnormalized principal-minor foundation. |
| docs/algorithm.md | Preserved reconstruction path; see REPRODUCING.md for validation limits. |
| REPRODUCING.md | Environment, exact-source identity, reproduction instructions and missing replay information. |
| src/reconstruction/ | Track A v74 executed implementation. |
| src/comparators/wl2/ | Optimized directed 2-WL and historical reference; reference licensing exclusion remains controlling. |
| results/frozen/ and results/checksums/ | Raw mirrors and artifact identities. |
| provenance/ | Artifact status, frozen-checkpoint map, archive checks, history and packaging audit. |
| docs/experimental-method.md and docs/limitations.md | Protocol, distinct benchmark tasks and evidence limits. |
| tests/ and GitHub Actions | Modern executability checks; not retroactive historical experiments. |
| results/experimental/n15/ | Two bounded n15 packets and their exact evidence boundary. |
| LICENSE.md and COPYING | Controlling split-license scope and GPL text. |

## What the repository does and does not establish

Track A v74 reports 315/315 target-validated reconstructions on 45 structures over seven repetitions. Its measured function includes target-isomorphism validation; success does not certify unique recovery or correctness of every retained candidate. Track B v75 executed 10 of 315 planned calls, all timeouts; 305 were never run. Track C v79 measures directed batch 2-WL, a different output task. The v80 timing quotient is descriptive, not a same-task speedup or asymptotic claim.

Bounded n15: 34 base inputs and one relabeling of each, 68/68 target matches in each of two runs. This is neither exhaustive n15 coverage nor uniqueness. The larger audit reports exhaustive n<=8 evidence; the repository packaging audit does not include or independently revalidate its full enumerator and outputs. Exact historical package versions/hardware and a complete original v79 benchmark driver remain unavailable in the curated replay.

Version numbers refer to different histories: Audit 10 v120 is the mathematical checkpoint; repository v74-v80 is the curated computational chain. They are not interchangeable, and later math is not back-imported into those experiments.

## Suggested reading routes

New mathematical reader: abstract -> construction -> P1/P2 -> canonical pp.1-6 -> latest v120 scope.

Proof reviewer: corrected sources (v28 notice and v112) -> linked attack reports -> current equation/gaps -> dependency audit when authorized.

Code reviewer: repository README -> REPRODUCING.md -> limitations -> source/raw/provenance -> optional bounded n15 packet.

## Source and preservation note

Packet source: verified v120 readability-refresh ZIP, CRC and all hashes PASS. PDF positions and early definitions checked against original canonical pages; v75-v77 defect definitions read directly. Repository snapshot: README.md, docs/problem.md, docs/mathematics.md, REPRODUCING.md, docs/limitations.md and results/experimental/n15/README.md, with GitHub blob SHAs retained in the companion source snapshot. Repository map paths beyond those fetched texts are referenced by the current README, not recursively audited. No full literature or novelty audit was performed. Existing wording that a question is open is interpreted here as unresolved in this program. Historical mathematical sources remain unchanged. This integrated edition places the guide in the packet and PDF; the repository receives a documentation-only reading guide.
