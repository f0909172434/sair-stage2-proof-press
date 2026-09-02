# 方法論

[繁體中文](methodology.md) · [English](../methodology.md)

## 任務契約

每筆輸入包含兩條 magma 等式。`True` 判定必須附上 Lean 程式，證明任何滿足第一條等式的 magma 都滿足第二條。`False` 判定必須附上 Lean 可檢查的反模型。官方 judge 只接受證書；模型信心與 heuristic 分數不會直接計分。

最終 artifact 對應兩種執行契約：

- Solo 每題啟動一個全新的 solver process，以標準輸入與輸出的 JSON lines 通訊。
- Marathon 把整批題目的 manifest 交給單一常駐 process。solver 共用全域時間與 token 預算，並把答案追加到 JSONL 檔案。

兩條賽道都提交一個小於 500 KB 的 `solver.py`。

## 證書管線

solver 先把等式解析成抽象語法樹，統一變數名稱與等式方向，再依固定順序執行一組有界策略。每個策略只會回傳可重放的證書候選或放棄。

### 直接證明規則

第一條路線處理自反性、直接代入、singleton／constant consequence 與固定 rewrite template。這些檢查成本低，產生的證明也較短。

### 有限反模型

solver 窮舉 `Fin 2` 與 `Fin 3` 上的小型運算，再測試較大有限 carrier 上的結構化運算。一個重要家族是：

```text
x * y = a x + b y + c (mod n).
```

Candidate 6 從公開且 revision-pinned 的 Equational Theories 來源加入 645 個去重複有限 magma。builder 移除等式 ID 與 implication mapping，只嵌入運算表並記錄 provenance hash。solver 會先直接檢查一張表是否滿足 hypothesis 且推翻 goal，通過後才會使用。

### 產生證明的搜尋

Candidate 5 加入有界 paramodulation。它會將 parent variables 標準化分離、保留 proof DAG，並限制深度、term size、保留規則數、處理候選數與 queue size。系統推導出通用 target 且能重放每條 proof edge 後，才渲染 Lean。

Candidate 7 加入 goal-directed paramodulation。搜尋會尋找直接或對稱的 target instance，並從 AST parent 重放每個證明步驟。固定 scoring 與 serial tie-break 維持確定性。

Paramodulation 路線結束後，solver 還會執行 symbolic narrowing 與 goal-guided beam。兩者都使用 occurs-checked unification、有界 symbolic depth、proof-edge revalidation 與固定 pruning rules。

### H19 去模目標 paramodulation

H19 結合 expanded replay-checked search、排序後的 forward／backward demodulation、tautology deletion、unit-equation subsumption 與確定性 goal-distance selection。它通過 discovery、一次性 disjoint validation、1,669-row 公開 no-refit safety gate 與 released Order-5 no-refit safety gate。這些結果支持在最終譜系重用此機制；私人結果仍須由官方評測提供。

### H22 waypoint controller

H22 測試一個有界 controller：模型提出具型別的 proof waypoints，compiler 把回應轉成受限制的 plan，只有產生出的證書會送進 Lean。治理流程中的 calibration、evaluation 與 released-input safety gates 均有通過紀錄。後續 protected promotion 因執行容量耗盡而停止，沒有 terminal scientific evidence。

最終 Aggressive artifact 保留這個有界 fallback。Safe artifact 不依賴它。最終 released-input 執行中，確定性路線解完所有題目，因此模型呼叫數為零。

## Safe 與 Aggressive

Safe 保留保守的確定性 production path，缺少已驗證證書時會 fail closed。Aggressive 加入已通過驗證的確定性 payload 與有界 H22 fallback。兩者都以同一個 Lean judge 為裁決者，未驗證的模型文字無法直接成為 accepted result。

在 released Order-5 Marathon 研究中，Safe 接受 198/200 並在兩題放棄；Aggressive 接受 200/200。兩者在合併後的 1,669 個公開輸入都接受 1,669 題，token 使用量為零。

## Marathon 適配

Marathon 讓同一個 process 處理完整 manifest。Aggressive adapter 會去除重複 ID、先跑確定性第一輪、排序 residuals、保留時間與 token 預算，並在追加答案前用 Lean 驗證模型衍生證書。Safe adapter 只執行確定性嘗試。

process 追加答案後會 flush 並同步檔案，讓 termination 發生時仍能保留已完成進度。批次執行也允許跨題重用 cache 與匯入的 proof payload。

## 受治理研究流程

Candidate 26 採用順序式 gate：

1. 寫下 hypothesis、source roles、caps、splits、metrics 與 terminal rule。
2. commit、push，並從遠端讀回凍結紀錄。
3. 完成不呼叫 provider 的 implementation 與 contract tests。
4. 只 materialize 已授權的 source 或 fixture。
5. calibration 只執行一次。
6. frozen gate 允許後，才開啟 disjoint evaluation。
7. 保留 failure、invalid instrumentation、timeout 與 source shortage 的原始分類。

這套流程降低了事後調整空間，也揭露 measurement infrastructure 的成本。H51–H63 多數在測試另一個 ranking mechanism 前，先追問是否存在可靠且 identity-bound 的 trace data。大部分研究以 blocked 或 unscored 結束；H57 只通過 measurement reliability 與 label-capacity 問題。

## 成本與模型使用

確定性 Candidate 1–19 與最終 released-public 執行的紀錄中沒有付費 provider 呼叫。Provider-backed H20–H27 有十筆正成本 ledger entry，合計 `US$0.918012780`。模型選擇、request count 與 gate outcome 保存在私有治理證據中。整個研究計畫沒有零成本證據。

## Soundness 邊界

官方 Lean judge 是結果裁決者。Search heuristics、模型輸出、cached tables 與公開 implication data 都只產生候選。一次執行若沒有收到 accepted judge response，就不會增加 solved row，即使 heuristic verdict 剛好正確也相同。
