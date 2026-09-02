# 研究時間線

[繁體中文](research-timeline.md) · [English](../research-timeline.md)

這份時間線協助讀者理解 machine records，並將 scientific outcome、compatibility check、source failure 與 governance stop 分開。authoritative records 是 `experiments/RANK1_EXPERIMENT_LEDGER.jsonl`、H-series evidence files 與 final artifact manifest。

## 確定性 solver checkpoints

| Checkpoint | 主要變更 | 公開輸入紀錄 | 最終處置 |
| --- | --- | --- | --- |
| Candidate 1 | 初始確定性 proof／countermodel portfolio | `sample_200` 162/200 | 歷史 baseline |
| Candidate 2 | 擴充 proof templates 與有限搜尋 | 172/200 | 被 Candidate 3 取代 |
| Candidate 3 | symbolic narrowing | 189/200 | 被 Candidate 4 取代 |
| Candidate 4 | goal-guided symbolic beam | 196/200 | 被 Candidate 5 取代 |
| Candidate 5 | proof-producing paramodulation | 197/200；`hard1` 44/69；`hard2` 156/200 | 被 Candidate 6 取代 |
| Candidate 6 | revision-bound 的 645 個公開有限 magma catalog | 197/200；67/69；192/200 | 被 Candidate 7 取代 |
| Candidate 7 | goal-directed paramodulation | 197/200；68/69；195/200；`normal` 999/1,000 | 歷史 production checkpoint |

這些 checkpoints 使用 released inputs，沒有 private leaderboard result 的證據地位。

## H1–H19：確定性成本、來源與可重用 proof lane

| Hypothesis | 問題 | Terminal interpretation |
| --- | --- | --- |
| H1 | 修復 structural false-certificate wrapper | promotion orchestration 失敗，沒有 candidate 被 promoted。 |
| H2 | 降低 extended-paramodulation rule cap | coverage 穩定，但每個 cap 都未通過 frozen timeout 或 runtime-margin gate；scientific promotion rejected。 |
| H3 | cache 純 AST traversal 與 ordering key | public speedup 未通過 preregistered gate，未進入 reusable calibration。 |
| H4 | 共用 resolution work，延後 proof payload construction | public speed gate 通過；reusable 20k runtime gate 失敗。 |
| H5 | lazy canonicalization of equation orientation | public speed gate 通過；reusable 20k runtime gate 失敗。 |
| H6 | 重用 canonical name map 並延後 metadata | public speed gate 通過；reusable 20k runtime gate 失敗。 |
| H7 | 不經 binder traversal 進行 goal match | public speed gate 通過；reusable 20k runtime gate 失敗。 |
| H8 | indexed canonicalization 與 runtime-core caching | public speed gate 通過；reusable 20k runtime gate 失敗。 |
| H9 | pre-resolve symbolic meets | public speed gate 通過；受治理 calibration lineage 未支持 production replacement。 |
| H10 | 測試 organizer-proxy late LLM path | 官方 run 以 `SOLVER_ERROR` 結束，run-card 與 expanded telemetry 互相矛盾；沒有 model-capability conclusion。 |
| H11 | 把 PGAP semantic hit 編譯成證書 | 68 個 semantic hits 全被確定性 finite-model lane 覆蓋，candidate-only opportunity 為零。 |
| H12 | 對 True tail 做 ground e-graph absorption | source correction 後，parent 在新 lane 前解完 1,000 rows；candidate-only gain 為零，terminal reject。 |
| H13 | ordered critical-pair completion | source generator 找到零個 parent abstention；source-infeasible。 |
| H14 | bidirectional weighted-A* rewriting | long-walk goal 已被解出或成本過高；source-infeasible。 |
| H15 | external-oracle residual source | 找到 9 個 clean abstention，低於 frozen minimum 12；source-infeasible。 |
| H16 | minimum-order-4 Z3 countermodel | 找到 17 個 independently revalidated rows，低於 frozen minimum 32；oracle source-infeasible。 |
| H17 | public-hardness-conditioned residual source | residual source 通過，但 12 個 fixed oracle rows 只確認 10 個；沒有開啟 mechanism implementation。 |
| H18 | Vampire transitive-proof residual source | source 與 oracle gates 通過，得到 disjoint 27/9 discovery-validation split，形成 H19 proposal。 |
| H19 | demodulating goal paramodulation | discovery 有 15 個 candidate-only accept、one-shot validation 有 5 個；通過 1,669-row public no-refit 與 200-row Order-5 safety，進入 final lineage。 |

H3–H9 包含真實 optimization measurement；frozen terminal selection gate 都沒有支持 production promotion。快速 microbenchmark 不會轉換成 solved-count evidence。

## H20–H35：模型輔助證書、robustness 與 evaluator compatibility

| Hypothesis | 問題 | Terminal interpretation |
| --- | --- | --- |
| H20 | LLM structured certificate generation | positive calibration gate 失敗。 |
| H21 | model-proposed verified waypoints | calibration timeout，沒有 rerun，也沒有 scientific conclusion。 |
| H22 | budgeted waypoint controller | calibration、disjoint evaluation、released safety gates 通過；後續 protected promotion 耗盡 infrastructure capacity，沒有 terminal scientific result；bounded controller 保留為 Aggressive fallback。 |
| H23 | verified-frontier ranking | calibration 失敗，evaluation 維持 closed。 |
| H24 | Gemma 下的 frozen-frontier deployment | H19 safety filter timeout，在 split 與 calibration 前 terminal safety failure。 |
| H25 | timeout-ineligible disjoint frontier validation | calibration 通過，disjoint evaluation 失敗。 |
| H26 | timeout-local quarantine 與 shared-response verification | calibration 失敗，evaluation 維持 closed。 |
| H27 | proof-backed waypoint graph closure | calibration 通過，disjoint evaluation 失敗。 |
| H28 | monotone multiphase certificate cascade | calibration solver nonzero exit；unscored，沒有 rerun。 |
| H29 | total-response boundary 與 terminal capsule | provider-free parser、solver-sequence、runner-fault、official-fixture robustness gate 通過；只有 reliability evidence。 |
| H30 | council-ranked certificate portfolio | public source filter 找到 22 個 clean abstention，低於 frozen minimum 24；terminal source failure。 |
| H31 | maximal disjoint council source | nested selector 要求的 rows 超過 frozen heap capacity；terminal static capacity shortfall。 |
| H32 | capacity-proved disjoint council portfolio | source 與 provider-free implementation gates 通過；calibration preflight 發現 frozen public audit stale，在 inference 前停止；infrastructure-blocked、unscored。 |
| H33 | public Stage 1 method-representation census | frozen census 在其 gates 下沒有 eligible representation gap；terminal `NO_JUSTIFIED_SUCCESSOR`。 |
| H34 | Lean 4.33.1 compatibility audit | 官方 modules build 成功，self-harness 缺 declared Python dependency；infrastructure-blocked、unscored。 |
| H35 | dependency-complete Lean 4.33.1 compatibility | official harness 與兩個 20-row public replay 通過；只有 compatibility evidence。 |

H20–H27 paid ledger 有十筆 positive-cost records，合計 `US$0.918012780`。H29 與 compatibility studies 為 provider-free。

## H36–H49：protocol adaptation 與 causal diagnosis

| Hypothesis | 問題 | Terminal interpretation |
| --- | --- | --- |
| H36 | 用新 source 擴充 public method census | method-bearing content 在 frozen manifest 前可見；governance-blocked、unscored。 |
| H37 | dual-protocol Marathon certificate harvesting | local public Marathon compatibility 通過；沒有 hidden-distribution claim。 |
| H38 | current-contract H22 Marathon adapter | candidate execution 前 infrastructure-blocked。 |
| H39 | path-identity-proved H22 Marathon adapter | correctness verdict 前 infrastructure-blocked。 |
| H40 | direct-toolchain-identity H22 adapter | direct Lean 與 Solo path 可運作；Marathon invocation 在 candidate execution 前失敗。 |
| H41 | single-value Marathon CLI correction | parser boundary 通過；full provider-free compatibility 仍 infrastructure-blocked。 |
| H42 | dependency closure 與 preimport | packages 已 materialized，dependency readiness 未完成；infrastructure-blocked。 |
| H43 | network-denied、preimported H22 adapter | current-official dependency-complete local Marathon compatibility 通過；只有 compatibility evidence。 |
| H44 | content-blind public method-delta census | frozen gates 下沒有 justified successor。 |
| H45 | disjoint full-pipeline residual-cluster census | preregistered cluster mechanism 未通過 scientific gate；屬 scoped scientific negative result。 |
| H46 | public-source-expansion method-delta census | frozen gates 下沒有 justified successor。 |
| H47 | strategy-outcome stability | discovery association 為 positive，independent confirmation 未執行；infrastructure-blocked、unscored。 |
| H48 | fresh source 下的 causal strategy value | frozen source-path identity defective；implementation 前 governance-blocked。 |
| H49 | verified-source causal strategy value | calibration 在 frozen gate 下找到的 causal value 不足；屬 scoped scientific negative result。 |

## H50–H63：在 ranking 前測量 proof ancestry

| Hypothesis | 問題 | Terminal interpretation |
| --- | --- | --- |
| H50 | passive bounded-paramodulation proof-ancestry census | frozen source capacity 靜態不足；unscored。 |
| H51 | ancestry-distilled fixed-cap frontier priority | governance contradiction 阻止 execution；unscored。 |
| H52 | dense bounded-progress labels | fixture-equivalence observer invalid；unscored。 |
| H53 | exact-production passive trace equivalence | code-identity validity 在 equivalence inference 前失敗；unscored。 |
| H54 | process-invariant code-locator traces | observer errors 使 983 rows 無效；unscored。 |
| H55 | 修復 H54 identity binding | 沒有 preregistration：new runner 無法保留包含 old runner hash 的 identity core；governance-infeasible。 |
| H56 | runner-bound monotone causal traces | 2 rows 超過 trace-schema cap，5 rows mismatch；unscored。 |
| H57 | return-only final-rule-DAG snapshots | provider-free measurement reliability 與 label-capacity 通過：1,024 stable snapshots，其中 997 rows 有 noninitial rules；沒有 ranking 或 solved-count claim。 |
| H58 | learned score 作為 final tie-breaker | existing production priority 已是 total order，新 field 沒有 reachable decision surface；未 implementation，governance-infeasible。 |
| H59 | learned score 放在 representation tie-breaker 前 | 唯一 zero-row preflight 未通過 identity-key binding；unscored，沒有 rerun。 |
| H60 | 同一 ranking question 的 canonical freeze manifest | source 已 materialized；2 rows 在 capacity evaluation 前使 observer／schema／infrastructure gate 無效；unscored。 |
| H61 | fresh-family production-abstention capacity | frozen enumerator 在 candidate execution 前遇到 source-capacity shortfall；unscored。 |
| H62 | flat-global hardness-conditioned abstention capacity | source enumeration 前混淆 repository root 與 official evaluator root；execution substrate invalid。 |
| H63 | official-root-bound flat-global capacity | 唯一 preflight 使用 Python 3.9.6，frozen contract 指定 3.11.16；source access 前停止，incumbent locked，lineage closed。 |

H57 回答了 preregistered measurement question，沒有測得 ancestry feature 的 predictive signal。H58–H63 只支持各自的 governance、identity、source 或 execution outcome。

## Candidate 28 與 final sprint

Candidate 28 在 H63 後開啟獨立 lineage。它比較五個 aggregate-only direction，最後選擇對四個既有 goal-directed paramodulation lane 做 family-conditional budget reallocation。Preregistration 將 baseline 與 treatment 的總量固定為 `max_rules = 1424`、`max_candidates = 4784`，並凍結 predecessor-excluded fresh sources、disjoint calibration／evaluation 與 zero-regression gates。Preregistration 與 remote readback 完成後，沒有 implementation、source execution 或 scientific A/B result。

final sprint 為兩種 execution contract 凍結四份 artifact。Aggressive 納入 released-public deterministic recovery 與 bounded H22 fallback；Safe 保留 conservative path。四份 artifact 在 evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a`、Lean 4.33.1 下接受全部 1,669 個 released Normal／Hard rows，模型使用量為零。released Order-5 上，Marathon Safe 接受 198/200，Aggressive 接受 200/200。portal 後來顯示四筆相符 participation entry。

官方頁面在 2026-09-02 仍顯示 `EVALUATING`，目前沒有 private score、rank 或 organizer-published result。
