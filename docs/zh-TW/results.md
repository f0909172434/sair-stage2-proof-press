# 結果

[繁體中文](results.md) · [English](../results.md)

## 最終 released-input evaluation

本節所有輸入都來自官方公開來源，並使用官方 evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a` 與 Lean 4.33.1 檢查。

| Artifact | Rows | Accepted | 模型呼叫或 tokens | Solver wall time |
| --- | ---: | ---: | ---: | ---: |
| Solo Safe | 1,669 | 1,669 | 0 calls | aggregate row time 4,304.60 s |
| Solo Aggressive | 1,669 | 1,669 | 0 calls | aggregate row time 4,344.14 s |
| Marathon Safe | 1,669 | 1,669 | 0 tokens | 169.00 s |
| Marathon Aggressive | 1,669 | 1,669 | 0 tokens | 152.23 s |

1,669 rows 包含 `normal` 1,000 題、`hard1` 69 題、`hard2` 200 題與 `hard3` 400 題。八個 Solo family run 有時間重疊，因此加總後的 Solo row time 代表成本量，不能視為外層 wall-clock time。Marathon Aggressive 在此公開 batch 比 Safe 快 9.92%。

來源：

- [`solo-public-1669.json`](../evidence/solo-public-1669.json)
- [`marathon-public-1669.json`](../evidence/marathon-public-1669.json)

## Released Order-5 研究

| Artifact | Rows | Accepted | 未嘗試 | Tokens | Solver wall time |
| --- | ---: | ---: | ---: | ---: | ---: |
| Marathon Safe | 200 | 198 | 2 | 0 | 170.59 s |
| Marathon Aggressive | 200 | 200 | 0 | 0 | 143.30 s |

這個 +2 差異只支持 released Order-5 集合上的窄範圍聲明，無法推出 hidden-distribution gain。

來源：

- [`marathon-safe-order5-200.json`](../evidence/marathon-safe-order5-200.json)
- [`marathon-aggressive-order5-200.json`](../evidence/marathon-aggressive-order5-200.json)

## 確定性 checkpoint 進展

| Checkpoint | 主要新增內容 | `sample_200` | `hard1` | `hard2` |
| --- | --- | ---: | ---: | ---: |
| Candidate 1 | 初始確定性 solver | 162/200 | 未納入最終比較 | 未納入最終比較 |
| Candidate 2 | 擴大確定性證明／反模型覆蓋 | 172/200 | — | — |
| Candidate 3 | symbolic narrowing | 189/200 | — | — |
| Candidate 4 | goal-guided symbolic beam | 196/200 | — | — |
| Candidate 5 | proof-producing paramodulation | 197/200 | C6 前 baseline 44/69 | C6 前 baseline 156/200 |
| Candidate 6 | 645-table 公開有限 magma catalog | 197/200 | 67/69 | 192/200 |
| Candidate 7 | goal-directed paramodulation | 197/200 | 68/69 | 195/200 |

Candidate 7 另在 released `normal` 兩次得到 999/1,000，judge rejection 為零。凍結 split 記錄 development 793/794、locked aggregate 206/206。這些是歷史本機結果，沒有私人 evaluation 的證據地位。

## H 系列結果

H 系列產生一條可重用方法線、數個模型輔助研究結果、兩個範圍受限的 scientific failure，以及許多 measurement block。

- H19 通過 discovery、disjoint validation、public no-refit safety 與 released Order-5 safety。
- H20 未通過 positive calibration gate。
- H21 在 calibration timeout，沒有 rerun。
- H22 通過受治理 calibration／evaluation 與 released safety；protected promotion 沒有 terminal scientific evidence。
- H23 未通過 calibration；H24 未通過 safety timeout gate。
- H25 與 H27 通過 calibration 後未通過 disjoint evaluation；H26 未通過 calibration。
- H32 以 infrastructure-blocked、unscored 結束。
- H35、H37、H43 只有 compatibility／readiness pass。
- H45 與 H49 是各自 preregistered scope 內的 scientific failure。
- H51–H56、H58–H63 以 blocked、invalid、infeasible 或 unscored 結束。
- H57 只通過 provider-free measurement reliability 與 final-rule-DAG label capacity。

完整時間線見 [`research-timeline.md`](research-timeline.md)。

## 正式提交

上傳後，portal 顯示四筆相符 entry。Readback 把每筆可見的 track／model selection 與 file size 綁定到本機 artifact hash，證明提交確實發生。Evaluation success 仍要等待官方結果。

官方頁面在 2026-09-02 仍顯示 `EVALUATING`。目前沒有 private score、final rank 或 evaluation completion 的資料。
