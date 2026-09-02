# 以 Lean 證書為核心的等式蘊含 Portfolio Solver

## 方法、受治理實驗與 SAIR Stage 2 四份正式提交

[繁體中文讀者版](main.zh-TW.md) · [English PDF](https://f0909172434.github.io/sair-stage2-proof-press/paper/sair_stage2_solver_research.pdf) · [English LaTeX source](main.tex)

作者：Chih-Kai Wang

日期：2026-09-02

## 摘要

本文整理 SAIR Mathematics Distillation Challenge，Equational Theories Stage 2 的一套確定性優先 solver。每個計分答案都需要 Lean 可檢查的 implication proof 或 countermodel certificate。系統結合直接證明模板、小型與結構化有限模型、645 個具 revision provenance 的公開有限 magma、proof-producing paramodulation、symbolic narrowing、goal-guided beam search，以及有界的 model-assisted waypoint compiler。我們在 Solo 與 Marathon 各提交 Safe、Aggressive 兩種版本。

四份 artifact 在 pinned official evaluator 與 Lean 4.33.1 下，接受 1,669/1,669 個 released Normal／Hard rows，全程沒有模型呼叫。另一個公開 200-row Order-5 集合上，Marathon Safe 接受 198 題，Aggressive 接受 200 題。Marathon Aggressive 完成 1,669-row batch 的 solver wall time 為 152.23 秒，比 Safe 快 9.92%。

本文也記錄 artifact 背後的受治理研究：一條可重用 proof-search 方法線、兩個範圍受限的 scientific negative result、數個 model-assisted gate，以及多個 source、instrumentation、infrastructure、governance stop。十筆正成本 provider record 合計 `US$0.918012780`。論文完成時官方頁面仍顯示 `EVALUATING`，因此 private score 與 rank 留白。

## 1. 任務與證據邊界

Stage 2 要求 solver 判定一條 magma equation 是否在所有 magma 中蘊含另一條。`True` answer 必須提供 Lean code，證明 implication 對所有 magma 成立。`False` answer 必須提供 Lean 可檢查的 witness，使 hypothesis 成立而 goal 失敗。Deterministic judge 只接受有效證書；heuristic confidence 不會增加 score。

比賽提供兩種 execution contract：

- Solo 每題啟動一個 fresh solver process，每題 wall budget 為 3,600 秒。
- Marathon 將 N 題 manifest 交給單一 process，共用 `N × 300` 秒 wall budget 與 `N × 32,768` model-token budget。

兩條賽道都提交單一 `solver.py`，大小上限 500 KB，並使用同一套 Lean judge。

本文使用下列 evidence class：

| Evidence class | 定義 |
| --- | --- |
| released-public verified | 精確 artifact 在 identified released rows 上由 pinned official local evaluator 接受。 |
| compatibility／measurement pass | 有界 protocol、environment 或 instrumentation question 通過。 |
| scientific fail | 有效的 preregistered mechanism 未通過 terminal scientific gate。 |
| blocked／invalid | source、governance、identity、instrumentation 或 infrastructure 阻止 inference。 |
| formal readback | portal 顯示相符 submitted entry。 |
| official result | organizer-published private score 或 rank；論文完成時尚未取得。 |

這套分類限制每個結論的範圍。本機 smoke test 只提供 compatibility evidence；infrastructure error 只記錄 execution outcome。

## 2. Solver 架構

### 2.1 證書優先路由

solver 將每條等式解析為 abstract syntax tree，依變數首次出現順序重新命名，統一 orientation，再執行固定順序的 bounded certificate generators。每條 lane 只會回傳可重放 proof／countermodel candidate 或 abstain。Lean 4 負責最終裁決。

第一批 lanes 實作 reflexivity、substitution instance、constant／singleton consequence 與 fixed rewrite template。這些短路徑處理常見 structural implication，通常不需要搜尋。

### 2.2 有限反模型

False portfolio 先枚舉 `Fin 2`、`Fin 3` 上的小型 operation，再測試較大的 structured carrier。一個實用家族是：

```text
x * y = a x + b y + c (mod n).
```

Candidate 6 加入 645 個去重 operation table，來源是 revision-pinned 的公開 Equational Theories data。builder 移除 equation ID 與 implication mapping。runtime 會直接確認 table 滿足 hypothesis 且推翻 goal，通過後才產生 countermodel certificate。

### 2.3 產生證明的搜尋

Candidate 5 加入 bounded paramodulation，採用 standardization-apart、occurs-checked unification、proof DAG，並限制 term size、depth、retained rules、processed candidates 與 queue size。target 推導完成且每條 proof edge 都可重放後，系統才輸出 Lean proof。

Candidate 7 將 paramodulation 改為 goal-directed。固定 structural score 與 serial tie-break 尋找直接或對稱 target instance，同時維持 deterministic output。Paramodulation lanes 後面還有 symbolic narrowing 與 goal-guided beam，作為有界 alternatives。

H19 新增 expanded goal-paramodulation、排序後的 forward／backward demodulation、tautology deletion、unit-equation subsumption 與 deterministic goal-distance selection。discovery 得到 15 個 candidate-only accepted certificates，one-shot validation 得到 5 個。它之後在 1,669 個 released rows 與 200-row Order-5 safety set 保留所有 solved row 與 certificate projection。

### 2.4 有界模型輔助

H22 讓模型提出 typed proof waypoints。compiler 將 response 解析成 bounded plan，限制可用 proof action，只有產生出的 Lean certificate 才會送交 judge。H22 lineage 的 calibration、disjoint evaluation 與 released safety gates 均有通過紀錄。後續 protected promotion 因 execution capacity 耗盡而停止，沒有 terminal scientific evidence。

Aggressive artifact 保留 controller 作為 fail-closed fallback。Safe artifact 不依賴模型。最終 released-input run 由 deterministic lanes 解完所有 rows，因此未呼叫模型。

### 2.5 Marathon execution

Marathon adapter 讓 certificate machinery 留在一個 persistent process。Aggressive implementation 先 deduplicate IDs，完成 deterministic first pass，再排序 residuals 並保留 time／model budget。答案會 append 並同步到檔案，termination 發生時仍能保留已完成進度。Persistent state 也允許重用 cached table 與 imported proof payload。

## 3. 研究治理

Candidate 26 採用 sequential gate discipline。每個 hypothesis 在開啟 scientific output 前先凍結 source role、identity、work cap、metric 與 terminal decision。source materialization 前只允許 static implementation 與 contract test。frozen calibration gate 通過後才能開啟 disjoint evaluation。重要 phase 之間會 commit、push，再從 GitHub read back。

這個流程限制了 post-hoc threshold movement，也讓 measurement defect 清楚出現。H51–H63 在 fitting ranking model 前，反覆檢查 exact production path 是否能產生 proof-ancestry labels。H57 得到窄範圍 measurement result：1,024 個 stable final-rule-DAG snapshots，其中 997 rows 含 materialized noninitial rule。這項結果沒有提供 predictive signal、ranking value 或 solved-count gain。後續 hypotheses 分別停在 total-order infeasibility、identity mismatch、schema cap、source shortage、root binding 或 Python-version mismatch。

Candidate 28 開啟獨立 lineage。preregistration 凍結一個 label-free structural-family predicate，並在四個既有 goal-directed paramodulation lanes 間重新分配 budget。baseline 與 treatment 的總量相同，都是 1,424 rules 與 4,784 candidates。remote readback 完成後，沒有 implementation 或 scientific run。

## 4. Released-input 結果

本節所有結果使用官方 evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a` 與 Lean 4.33.1。1,669-row set 包含 Normal 1,000 題、Hard1 69 題、Hard2 200 題、Hard3 400 題。

| Artifact | Accepted | Model use | Time (s) | Size (bytes) |
| --- | ---: | ---: | ---: | ---: |
| Solo Safe | 1,669/1,669 | 0 calls | 4,304.60 | 268,763 |
| Solo Aggressive | 1,669/1,669 | 0 calls | 4,344.14 | 360,443 |
| Marathon Safe | 1,669/1,669 | 0 tokens | 169.00 | 272,898 |
| Marathon Aggressive | 1,669/1,669 | 0 tokens | 152.23 | 366,197 |

Solo time 是 per-row solver elapsed time 的加總；Marathon time 是 batch solver wall time。Marathon Aggressive 在 paired released batch 快 9.92%。這是指定 workload 的 runtime measurement，不能推廣到 private inputs。

### 4.1 Released Order-5

| Artifact | Accepted | Abstained | Tokens | Time (s) |
| --- | ---: | ---: | ---: | ---: |
| Marathon Safe | 198/200 | 2 | 0 | 170.59 |
| Marathon Aggressive | 200/200 | 0 | 0 | 143.30 |

兩份 Aggressive-only certificate 都來自 released-public deterministic recovery：一份較深的 right-branch H19 proof，以及一份 singleton-forcing source proof。current official judge 接受兩者，`axioms=[]`。

### 4.2 確定性 checkpoint progression

| Checkpoint | 主要新增內容 | Sample-200 | Hard1 | Hard2 |
| --- | --- | ---: | ---: | ---: |
| Candidate 1 | 初始 deterministic portfolio | 162/200 | — | — |
| Candidate 2 | 擴充 templates 與 finite search | 172/200 | — | — |
| Candidate 3 | symbolic narrowing | 189/200 | — | — |
| Candidate 4 | goal-guided beam | 196/200 | — | — |
| Candidate 5 | proof-producing paramodulation | 197/200 | 44/69 | 156/200 |
| Candidate 6 | public finite-magma catalog | 197/200 | 67/69 | 192/200 |
| Candidate 7 | goal-directed paramodulation | 197/200 | 68/69 | 195/200 |

Candidate 7 也在 released Normal 兩次得到 999/1,000，judge rejection 為零。這些 checkpoints 早於 final four artifacts。

## 5. Negative 與 blocked 結果

H45 與 H49 是 late research program 的兩個 scoped scientific failure。H45 的 preregistered residual-cluster mechanism 未通過 frozen scientific gate。H49 在 verified source identity 下找到的 causal strategy value 不足。這兩項結果只否定各自的 bounded mechanism 與 population。

其他 terminal record 回答 operational question。H20、H23 未通過 positive calibration gate；H25、H27 通過 calibration 後未通過 disjoint evaluation；H29 通過 provider-free total-response robustness test；H35、H37、H43 通過 local compatibility question。H32、H38–H42、H47、H63 停在 infrastructure。H36、H48、H51、H55 停在 governance 或 identity。H50、H61 遇到 source capacity shortage。H52–H54、H56 遇到 invalid instrumentation 或 schema condition。

完整 H1–H63 terminal map 見[繁體中文研究時間線](../docs/zh-TW/research-timeline.md)。

## 6. 成本與模型選擇

final released-input evaluation 的模型呼叫數為零。broader project 仍有 provider cost：H20–H27 含十筆 positive-cost ledger entry，合計 `US$0.918012780`。

四筆 portal entry 將 Aggressive artifact 配給 `openai/gpt-oss-120b`、reasoning effort low；Safe artifact 配給 `google/gemma-4-31b-it`。這是 slot allocation decision。Aggressive 有較大的 bounded model-assisted surface，使用 final-sprint public probe 選出的 model profile。Safe 強調 conservative deterministic path，採用另一個 model family 以降低 correlated fallback risk。released final runs 沒有觸發任何模型，因此 1,669-row result 無法衡量兩個 portal model 的增益。

## 7. Submission integrity 與重現

四份 artifact 以完整 SHA-256 綁定：

| Artifact | SHA-256 |
| --- | --- |
| Solo Safe | `a81025ac454e964365f5b53b1928af3d4e4276f374d62d5b05f34264afada85a` |
| Solo Aggressive | `faf8468e6183638d35607c3bf1ae0685da838f3bfed7009c9bd5b6402071e70a` |
| Marathon Safe | `05e3b837d8cdac8a0299fe66592bde787e57b10c50a0eefe24d6fdf9ae4f3d5c` |
| Marathon Aggressive | `c87e44bda89f08dad7a8a12147b28ba77a2fe288c3c3947c4dfe06b2154b8c21` |

post-submission audit 通過 final packet verifier、九個 focused contract tests、兩份 Solo 的 sample-20、兩份 Marathon 的 normal-5。portal 顯示四筆 entry，其 track、model、file size 與 local hash binding 全部相符。readback 證明 submission 發生，evaluation success 仍待官方結果。

重現需要上述 official evaluator revision、Lean 4.33.1、exact solver hashes 與 released source identities。private evaluation inputs 與 organizer routing 無法取得。macOS 上一次 `lake env` discovery path 曾停滯；成功 run 使用 direct Lean／Lake 4.33.1 binary 與明確 judge search path。workaround 只調整 environment entry path。

## 8. 限制

released benchmark 範圍廣，但沒有 hidden-set 性質；它可能與 public data、finite-magma catalog 共享 structural regularity。兩個 Order-5 gains 是窄範圍、known-source recovery。Safe 與 Aggressive 在 code size、deterministic lanes、scheduling 與 fallback behavior 都有差異，因此 runtime comparison 只能做 descriptive interpretation。

本機測試無法完整複製 organizer sandbox、private distribution、provider routing 或 production scheduling。論文完成時 portal 尚未發布 score 或 rank。本文只報告精確 released-input acceptance 與 formal readback，competition outcome 維持空白。

H-series 的 governance record 數量遠多於 scientific trial。Preregistration 降低 researcher degrees of freedom，也讓小型 identity／environment defect 形成 terminal stop。後續 protocol 可以把 immutable scientific decision 與 replaceable execution-substrate identity 分層，同時保留 scientific data 的 one-shot rule。

## 9. 結論

deterministic-first、certificate-producing portfolio 讓四份 final artifact 在沒有模型呼叫的情況下，解完所有 released Normal／Hard rows。公開有限模型與 proof-producing search 提供互補 coverage；H19 是受治理研究中最強的 proof-search addition。Aggressive final lineage 解出兩個剩餘 released Order-5 rows，並在 1,669-row Marathon batch 降低 wall time。

研究紀錄同時保留清楚的界線：compatibility evidence 只支持指定環境，blocked run 只描述 operational outcome，portal readback 只確認 submission。private leaderboard result 需要 organizer-published score 或 rank。

## Repository evidence map

| Path | 角色 |
| --- | --- |
| `dist/final/FINAL_ARTIFACT_MANIFEST.json` | exact bytes、hashes、evaluator identity 與 final artifact notes。 |
| `dist/final/benchmarks/formal_submission_readback_20260830_2023.json` | portal-visible four-entry readback 與 track／model binding。 |
| `dist/final/benchmarks/post_submission_final_audit_20260831_0435.json` | packet、focused contract、Solo、Marathon post-submission checks。 |
| `dist/final/benchmarks/solo_public1669_current_official_20260830.json` | final Solo released 1,669-row results。 |
| `dist/final/benchmarks/marathon_public1669_current_official_20260830.json` | final Marathon results 與同一 union 的 runtime。 |
| `experiments/RANK1_EXPERIMENT_LEDGER.jsonl` | chronological governed experiment record 與 provider cost fields。 |
| `docs/zh-TW/research-timeline.md` | H1–H63 每個 hypothesis 的 terminal interpretation。 |

private evidence history 還含 personal path、author email metadata、authorization 原文、conversation identifier、runner fingerprint 與 provider-use telemetry。public release 使用 sanitized、squashed export，hash-bound evidence repository 保持 private。
