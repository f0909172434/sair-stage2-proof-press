# 重現說明

[繁體中文](reproducibility.md) · [English](../reproducibility.md)

## 凍結 identity

重現 final artifact 時，請核對完整 SHA-256：

| Artifact | SHA-256 |
| --- | --- |
| Solo Safe | `a81025ac454e964365f5b53b1928af3d4e4276f374d62d5b05f34264afada85a` |
| Solo Aggressive | `faf8468e6183638d35607c3bf1ae0685da838f3bfed7009c9bd5b6402071e70a` |
| Marathon Safe | `05e3b837d8cdac8a0299fe66592bde787e57b10c50a0eefe24d6fdf9ae4f3d5c` |
| Marathon Aggressive | `c87e44bda89f08dad7a8a12147b28ba77a2fe288c3c3947c4dfe06b2154b8c21` |

final audit 使用：

- 官方 evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a`；
- Lean 4.33.1；
- Python 3.11 執行 packet 與 contract checks；
- repository branch `agent/final-24h-dual-track-sprint`，pre-publication audit base 為 `56684f74569d21da043d4dc4a40e47ff9bae80bd`。

## 驗證順序

1. clone 官方 evaluator，checkout 上述精確 commit。
2. 安裝 evaluator pin 住的 Lean／Mathlib toolchain。
3. 對照 `dist/final/FINAL_ARTIFACT_MANIFEST.json`，驗證每份 final solver hash 與 byte count。
4. 執行 `scripts/verify_final_upload_packet.py`。該 script 檢查 identity 與 packaging；其中 pre-submission state field 是歷史值。
5. 執行 post-submission audit 列出的 final-artifact、layout、fast-path 與 note contract tests。
6. 每份 Solo file 執行官方 Solo harness；每份 Marathon file 執行官方 Marathon scorer。
7. 記錄 input source hash、row count、environment version、accepted status count、model／token use、output hash；需要主張 determinism 時，再記錄第二次執行 projection。

macOS 上曾有一次官方 `lake env` discovery path 停滯。通過驗證的 workaround 使用 direct Lean／Lake 4.33.1 binaries，並從官方 checkout 的 built dependencies 組合明確 `JUDGE_LEAN_PATH`。這是 environment entry-path 調整，沒有改動 solver。

## 公開來源

合併後的 1,669-row study 包含：

| Family | Rows |
| --- | ---: |
| `normal` | 1,000 |
| `hard1` | 69 |
| `hard2` | 200 |
| `hard3` | 400 |

Order-5 是另一個公開的 200-row source。source role 與 opened／blind state 記錄在 `experiments/DATASET_ROLE_REGISTRY.json`。

## 只靠本 repository 無法重現的項目

- 主辦方 private evaluation inputs。
- production portal 與 provider routing。
- private score 或 rank。
- 每次 local macOS run 與 Docker resource 的精確等價性。
- 刻意保留在 repository 外的 raw protected journals。

## 證據衛生

請勿 commit raw private row、prompt、model response、request identifier、browser state、credential 或 local scratch journal。新的 summary 應使用 repository-relative path，移除 team／account identifier，只保留支持指定聲明所需的最少 provider telemetry。

較早的 sealed evidence 含 absolute host path。這些紀錄保留 historical reproducibility，公開前仍需要明確的 sanitization 或 history strategy。
