# Research timeline

[繁體中文](zh-TW/research-timeline.md) · [English](research-timeline.md)

This chronology is a reading guide to the machine records. It separates scientific outcomes from compatibility checks, source failures, and governance stops. The authoritative records are `experiments/RANK1_EXPERIMENT_LEDGER.jsonl`, the H-series evidence files, and the final artifact manifest.

## Deterministic solver checkpoints

| Checkpoint | Main change | Recorded released result | Disposition |
| --- | --- | --- | --- |
| Candidate 1 | Initial deterministic proof and countermodel portfolio | 162/200 on `sample_200` | Historical baseline |
| Candidate 2 | Broader proof templates and finite search | 172/200 | Replaced by Candidate 3 |
| Candidate 3 | Symbolic narrowing | 189/200 | Replaced by Candidate 4 |
| Candidate 4 | Goal-guided symbolic beam | 196/200 | Replaced by Candidate 5 |
| Candidate 5 | Proof-producing paramodulation | 197/200; 44/69 on `hard1`; 156/200 on `hard2` | Replaced by Candidate 6 |
| Candidate 6 | Revision-bound catalog of 645 public finite magmas | 197/200; 67/69; 192/200 | Replaced by Candidate 7 |
| Candidate 7 | Goal-directed paramodulation | 197/200; 68/69; 195/200; 999/1,000 on `normal` | Historical production checkpoint |

These checkpoints used released inputs. They are not private leaderboard results.

## H1-H19: deterministic cost, sources, and a reusable proof lane

| Hypothesis | Question | Terminal interpretation |
| --- | --- | --- |
| H1 | Repair a structural false-certificate wrapper | Promotion orchestration failed; no candidate was promoted. |
| H2 | Lower the extended-paramodulation rule cap | Coverage was stable, but every cap missed frozen timeout or runtime-margin gates. Scientific promotion was rejected. |
| H3 | Cache pure AST traversals and ordering keys | Public speedup missed the preregistered gate; rejected before reusable calibration. |
| H4 | Share resolution work and defer proof payload construction | Public speed gate passed; reusable 20k runtime gate failed. |
| H5 | Lazily canonicalize equation orientation | Public speed gate passed; reusable 20k runtime gate failed. |
| H6 | Reuse canonical name maps and defer metadata | Public speed gate passed; reusable 20k runtime gate failed. |
| H7 | Match goals without a binder traversal | Public speed gate passed; reusable 20k runtime gate failed. |
| H8 | Add indexed canonicalization and runtime-core caching | Public speed gate passed; reusable 20k runtime gate failed. |
| H9 | Pre-resolve symbolic meets | Public speed gate passed. The governed calibration lineage did not justify production replacement. |
| H10 | Exercise the organizer-proxy late LLM path | The official run ended `SOLVER_ERROR`; run-card and expanded telemetry disagreed. No model-capability conclusion is valid. |
| H11 | Compile PGAP semantic hits into certificates | All 68 semantic hits were already covered by the deterministic finite-model lane; zero candidate-only opportunity. |
| H12 | Ground e-graph absorption for True tails | After source correction, the parent solved all 1,000 rows before the new lane. Zero candidate-only gain; terminal reject. |
| H13 | Ordered critical-pair completion | The source generator found zero parent abstentions; source-infeasible. |
| H14 | Bidirectional weighted-A* rewriting | The generated long-walk goals were already solved or too expensive; source-infeasible. |
| H15 | External-oracle residual source | Nine clean abstentions were found, below the frozen minimum of 12; source-infeasible. |
| H16 | Minimum-order-4 Z3 countermodels | Seventeen independently revalidated rows were found, below the frozen minimum of 32; oracle source-infeasible. |
| H17 | Public-hardness-conditioned residual source | The residual source passed, but only 10 of 12 fixed oracle rows confirmed; no mechanism implementation opened. |
| H18 | Vampire transitive-proof residual source | Source and oracle gates passed, yielding a disjoint 27/9 discovery-validation split and the H19 mechanism proposal. |
| H19 | Demodulating goal paramodulation | Passed discovery (15 candidate-only accepts), one-shot validation (5), 1,669-row public no-refit safety, and 200-row Order-5 no-refit safety. Reused in the final lineage. |

H3-H9 contain real optimization measurements, but their terminal selection gates rejected production promotion. A fast microbenchmark was not treated as solved-count evidence.

## H20-H35: model-assisted certificates, robustness, and evaluator compatibility

| Hypothesis | Question | Terminal interpretation |
| --- | --- | --- |
| H20 | Structured certificate generation by an LLM | Positive calibration gate failed. |
| H21 | Model-proposed verified waypoints | Calibration timed out; no rerun and no scientific conclusion. |
| H22 | Budgeted waypoint controller | Calibration, disjoint evaluation, and released safety gates passed. A later protected promotion exhausted infrastructure capacity and produced no terminal scientific result. The bounded controller remained an Aggressive fallback. |
| H23 | Verified-frontier ranking | Calibration failed; evaluation stayed closed. |
| H24 | Frozen-frontier deployment under Gemma | The H19 safety filter timed out; terminal safety failure before split and calibration. |
| H25 | Timeout-ineligible disjoint frontier validation | Calibration passed; disjoint evaluation failed. |
| H26 | Timeout-local quarantine with shared-response verification | Calibration failed; evaluation stayed closed. |
| H27 | Proof-backed waypoint graph closure | Calibration passed; disjoint evaluation failed. |
| H28 | Monotone multiphase certificate cascade | Calibration solver exited nonzero. The attempt was unscored and not rerun. |
| H29 | Total-response boundary and terminal capsule | Provider-free parser, solver-sequence, runner-fault, and official-fixture robustness gate passed. Reliability evidence only. |
| H30 | Council-ranked certificate portfolio | Public source filter found 22 clean abstentions, below the frozen minimum of 24; terminal source failure. |
| H31 | Maximal disjoint council source | Nested selector requested more rows than its frozen heap could contain; terminal static capacity shortfall. |
| H32 | Capacity-proved disjoint council portfolio | Source and provider-free implementation gates passed. Calibration preflight found the frozen public audit stale and stopped before inference; infrastructure-blocked and unscored. |
| H33 | Public Stage 1 method-representation census | Frozen census found no eligible representation gap under its gates; terminal `NO_JUSTIFIED_SUCCESSOR`, not a solver failure. |
| H34 | Lean 4.33.1 compatibility audit | Official modules built, but the self-harness lacked a declared Python dependency; infrastructure-blocked and unscored. |
| H35 | Dependency-complete Lean 4.33.1 compatibility | Official harness and two 20-row public replays passed. Compatibility evidence only. |

The H20-H27 paid ledger contains ten positive-cost records totaling US$0.918012780. H29 and the compatibility studies were provider-free.

## H36-H49: protocol adaptation and causal diagnosis

| Hypothesis | Question | Terminal interpretation |
| --- | --- | --- |
| H36 | Extend the public method census with new sources | Method-bearing content became visible before the frozen manifest. Governance-blocked and unscored. |
| H37 | Dual-protocol Marathon certificate harvesting | Local public Marathon compatibility passed. No hidden-distribution claim. |
| H38 | Current-contract H22 Marathon adapter | Infrastructure-blocked before candidate execution. |
| H39 | Path-identity-proved H22 Marathon adapter | Infrastructure-blocked before a correctness verdict. |
| H40 | Direct-toolchain-identity H22 adapter | Direct Lean and Solo paths worked; the Marathon invocation failed before candidate execution. |
| H41 | Single-value Marathon CLI correction | Parser boundary passed; full provider-free compatibility remained infrastructure-blocked. |
| H42 | Dependency closure and preimport | Packages materialized, but dependency readiness did not complete; infrastructure-blocked. |
| H43 | Network-denied, preimported H22 adapter | Current-official dependency-complete local Marathon compatibility passed. Compatibility evidence only. |
| H44 | Content-blind public method-delta census | No justified successor under the frozen gates. |
| H45 | Disjoint full-pipeline residual-cluster census | The preregistered cluster mechanism failed its scientific gate. This is a scoped scientific negative result. |
| H46 | Public-source-expansion method-delta census | No justified successor under the frozen gates. |
| H47 | Strategy-outcome stability | Discovery association was positive, but independent confirmation never ran; infrastructure-blocked and unscored. |
| H48 | Causal strategy value with a fresh source | Frozen source-path identity was defective; governance-blocked before implementation. |
| H49 | Verified-source causal strategy value | Calibration found insufficient causal value under the frozen gate. This is a scoped scientific negative result. |

## H50-H63: measuring proof ancestry before ranking it

| Hypothesis | Question | Terminal interpretation |
| --- | --- | --- |
| H50 | Passive bounded-paramodulation proof-ancestry census | Frozen source capacity was statically insufficient; unscored. |
| H51 | Ancestry-distilled fixed-cap frontier priority | Governance contradiction blocked the run; unscored. |
| H52 | Dense bounded-progress labels | The fixture-equivalence observer was invalid; unscored. |
| H53 | Exact-production passive trace equivalence | Code-identity validity failed before equivalence inference; unscored. |
| H54 | Process-invariant code-locator traces | Observer errors invalidated 983 rows; unscored. |
| H55 | Repair the H54 identity binding | Never preregistered: a new runner could not preserve an identity core that included the old runner hash. Governance-infeasible. |
| H56 | Runner-bound monotone causal traces | Two rows exceeded the trace-schema cap and five mismatched; unscored. |
| H57 | Return-only final-rule-DAG snapshots | Provider-free measurement reliability and label-capacity questions passed: 1,024 stable snapshots and 997 noninitial-rule rows. No ranking or solved-count claim. |
| H58 | Learned score as the final tie-breaker | Existing production priority was already total, so the new field had no reachable decision surface. Never implemented; governance-infeasible. |
| H59 | Learned score before the representation tie-breaker | The sole zero-row preflight failed an identity-key binding; unscored and not rerun. |
| H60 | Canonical freeze manifest for the same ranking question | Source materialized, but two rows invalidated the observer/schema/infrastructure gate before capacity evaluation; unscored. |
| H61 | Fresh-family production-abstention capacity | The frozen enumerator hit a source-capacity shortfall before candidate execution; unscored. |
| H62 | Flat-global hardness-conditioned abstention capacity | Repository root and official evaluator root were confused before source enumeration; execution substrate invalid. |
| H63 | Official-root-bound flat-global capacity | The sole preflight used Python 3.9.6; the frozen contract required Python 3.11.16. It stopped before source access; incumbent locked and lineage closed. |

H57 answered the measurement question it preregistered. Ancestry-feature predictive value remained unmeasured. H58-H63 therefore retain their governance, identity, source, or execution classifications and provide no learned-ranking evidence.

## Candidate 28 and the final sprint

Candidate 28 opened a separate lineage after H63. It compared five aggregate-only directions and selected a family-conditional reallocation of four existing goal-directed paramodulation lane budgets. The preregistration fixed equal totals in both arms (`max_rules = 1424`, `max_candidates = 4784`), fresh predecessor-excluded sources, disjoint calibration and evaluation, and zero-regression gates. The preregistration and remote readback completed. No implementation, source execution, or scientific A/B result followed.

The final sprint froze four artifacts for two independent execution contracts. Aggressive variants incorporated released-public deterministic recoveries and a bounded H22 fallback; Safe variants kept the conservative path. All four accepted all 1,669 released Normal/Hard rows under official evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a` and Lean 4.33.1 with zero model use. On released Order-5, Marathon Safe accepted 198/200 and Aggressive accepted 200/200. The portal later displayed four matching participation entries.

The official page still reported `EVALUATING` on 2026-09-02. The record therefore contains no private score, rank, or organizer-published result.
