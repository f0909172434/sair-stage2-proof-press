# 聲明邊界

[繁體中文](claim-boundaries.md) · [English](../claim-boundaries.md)

## 證據層級

所有敘述都採用能被證據支持的最窄標籤。

| 標籤 | 必要證據 | 可使用的聲明 |
| --- | --- | --- |
| Released-public verified | 精確 solver hash、公開來源 identity、官方 evaluator identity、Lean-accepted output | 指定 solver 接受指定公開 rows。 |
| Compatibility pass | 精確 toolchain／protocol／package contract | artifact 能在該環境或契約下執行。 |
| Measurement-only pass | 凍結的 instrumentation question 與有效結果 | measurement substrate 回答該有界問題。 |
| Scientific fail | Preregistered scientific metric、有效 source、有效 execution、terminal gate | 指定範圍的 mechanism 未通過 gate。 |
| Governance blocked | 缺少或互相矛盾的 authority／identity／gate | 沒有科學結論。 |
| Source or capacity blocked | 必要 rows 或 labels 不存在 | 無法對 mechanism 下科學結論。 |
| Instrumentation invalid | Observer、identity 或 schema 未測量凍結 target | 沒有科學結論。 |
| Preregistration-only | 已遠端封存的 plan，尚未授權 execution | 只能確認 planned hypothesis 與 decision rule。 |
| Formal submission readback | Portal 顯示相符 entry | entry 已提交。 |
| Official result | 主辦方發布 score 或 rank | 目前沒有此類證據。 |

## 目前有證據支持的聲明

- 四份精確 final artifact 已提交，之後也出現在 portal。
- 四份 artifact 在記錄中的官方本機 evaluator 接受 1,669/1,669 個公開 rows，模型使用量為零。
- Marathon Aggressive 接受 200/200 個 released Order-5 rows；Marathon Safe 接受 198/200 並放棄兩題。
- H45 與 H49 是有效且範圍受限的 scientific negative results。
- H57 通過有界 measurement-reliability 與 label-capacity 問題。
- Candidate 28 完成 preregistration 與 remote readback，沒有 implementation 或 evaluation。

## 目前缺少證據的聲明

- 任何 private score、rank、prize 或 final leaderboard position。
- 官方頁面顯示 `EVALUATING` 期間的 evaluation completion、private score 或 rank。官方 Contributor Network 另有 Stage 2 solver 分享介面，因此 solver publication 需單獨判讀。
- Aggressive 對 Safe 的一般 hidden-distribution superiority。
- Candidate 28 帶來 positive solver gain。
- 從 H10、H21、H22 protected promotion、H32 或任何 invalid／blocked execution 推出 model-capability conclusion。
- 整個研究計畫零成本。
- 本機 compatibility smoke 與 production sandbox 完全等價。

## 負結果完整性

Source shortage、timeout、governance contradiction 或 invalid observer 只記錄對應的 operational failure。這些事件沒有測得 proposed mathematical mechanism，因此不能標成該機制的 scientific failure。ledger 與論文都保留這項區分。

Compatibility pass 也維持窄範圍。H35、H37 與 H43 顯示特定 evaluator、dependency 或 Marathon path 能運作，未測量 hidden rows 的 accepted count。

## Submission state 的優先來源

`dist/final/FINAL_ARTIFACT_MANIFEST.json` 與 `dist/final/SUBMISSION_HANDOFF.md` 在正式提交前凍結，當中的 `external_actions` 欄位描述較早時間點。正式提交是否發生，以 `dist/final/benchmarks/formal_submission_readback_20260830_2023.json` 為 authoritative repository record。
