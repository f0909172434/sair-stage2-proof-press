# Results

[繁體中文](zh-TW/results.md) · [English](results.md)

## Final released-input evaluation

All rows in this section came from released official sources and were checked with official evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a` and Lean 4.33.1.

| Artifact | Rows | Accepted | Model calls or tokens | Solver wall time |
| --- | ---: | ---: | ---: | ---: |
| Solo Safe | 1,669 | 1,669 | 0 calls | aggregate row time 4,304.60 s |
| Solo Aggressive | 1,669 | 1,669 | 0 calls | aggregate row time 4,344.14 s |
| Marathon Safe | 1,669 | 1,669 | 0 tokens | 169.00 s |
| Marathon Aggressive | 1,669 | 1,669 | 0 tokens | 152.23 s |

The 1,669 rows combine `normal` (1,000), `hard1` (69), `hard2` (200), and `hard3` (400). Eight Solo family runs overlapped. Summed Solo row time therefore measures cost and does not represent outer wall-clock time. Marathon Aggressive was 9.92% faster than Marathon Safe on this released batch.

Sources:

- [`solo-public-1669.json`](evidence/solo-public-1669.json)
- [`marathon-public-1669.json`](evidence/marathon-public-1669.json)

## Released Order-5 study

| Artifact | Rows | Accepted | Not attempted | Tokens | Solver wall time |
| --- | ---: | ---: | ---: | ---: | ---: |
| Marathon Safe | 200 | 198 | 2 | 0 | 170.59 s |
| Marathon Aggressive | 200 | 200 | 0 | 0 | 143.30 s |

The +2 difference supports a narrow claim about the released Order-5 set. Hidden-distribution gain remains unmeasured.

Sources:

- [`marathon-safe-order5-200.json`](evidence/marathon-safe-order5-200.json)
- [`marathon-aggressive-order5-200.json`](evidence/marathon-aggressive-order5-200.json)

## Deterministic checkpoint progression

| Checkpoint | Main addition | `sample_200` | `hard1` | `hard2` |
| --- | --- | ---: | ---: | ---: |
| Candidate 1 | initial deterministic solver | 162/200 | not used for the final comparison | not used for the final comparison |
| Candidate 2 | expanded deterministic proof/countermodel coverage | 172/200 | - | - |
| Candidate 3 | symbolic narrowing | 189/200 | - | - |
| Candidate 4 | goal-guided symbolic beam | 196/200 | - | - |
| Candidate 5 | proof-producing paramodulation | 197/200 | 44/69 baseline before C6 | 156/200 baseline before C6 |
| Candidate 6 | 645-table public finite-magma catalog | 197/200 | 67/69 | 192/200 |
| Candidate 7 | goal-directed paramodulation | 197/200 | 68/69 | 195/200 |

Candidate 7 also recorded 999/1,000 on released `normal`, twice, with zero judge rejections. The frozen split reported development 793/794 and locked aggregate 206/206. These are historical local results and not the final private evaluation.

## H-series outcomes

The H-series produced one reusable method line, several model-assisted research results, two scoped scientific failures, and many blocked measurements.

- H19 passed discovery, disjoint validation, public no-refit safety, and released Order-5 safety.
- H20 failed its positive calibration gate.
- H21 timed out in calibration and was not rerun.
- H22 passed governed calibration/evaluation and released safety, but its protected promotion attempt produced no terminal scientific evidence.
- H23 failed calibration; H24 failed a safety timeout gate.
- H25 and H27 passed calibration but failed their disjoint evaluations; H26 failed calibration.
- H32 ended infrastructure-blocked and unscored.
- H35, H37, and H43 are compatibility/readiness passes only.
- H45 and H49 are scientific failures within their preregistered scopes.
- H51-H56 and H58-H63 ended blocked, invalid, infeasible, or unscored.
- H57 passed only provider-free measurement reliability and final-rule-DAG label capacity.

The full chronology and source links are in [`research-timeline.md`](research-timeline.md).

## Formal submission

The portal displayed four matching entries after upload. The readback binds each visible track/model selection and file size to a local artifact hash. It establishes that submission occurred, not that evaluation succeeded.

The official page remained `EVALUATING` on 2026-09-02. Private score, final rank, and evaluation completion remain unavailable.
