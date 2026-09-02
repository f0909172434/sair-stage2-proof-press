# Proof Press — SAIR Stage 2 Lean 證書型 Solver

[繁體中文](#繁體中文) · [English](#english) · [互動網站](https://f0909172434.github.io/sair-stage2-proof-press/) · [繁體中文論文](paper/main.zh-TW.md) · [英文論文 PDF](https://f0909172434.github.io/sair-stage2-proof-press/paper/sair_stage2_solver_research.pdf) · [官方 Contributor Network](https://competition.sair.foundation/contributor-network?competition=mathematics-distillation-challenge-equational-theories-stage2)

> 把猜想壓成證明。Search 可以提出候選，只有 Lean 接受的證書能成為結果。

## 繁體中文

### 專案概覽

這是 SAIR Mathematics Distillation Challenge — Equational Theories Stage 2 的研究與最終提交紀錄。任務要求 solver 判定一條 magma 等式是否蘊含另一條；`True` 必須附上 Lean 可重放的通用證明，`False` 必須附上 Lean 可檢查的有限反模型。

專案從七個確定性 checkpoint，推進到 H1–H63 的受治理研究，再凍結四份 Solo／Marathon × Safe／Aggressive solver。公開版本保留方法、程式、聚合結果、負結果與聲明邊界；含個人路徑、授權原文、對話 ID、runner 指紋與細粒度 provider telemetry 的雜湊綁定歷史不在公開快照中。

### 目前能確認的結果

| 證據層級 | 結果 | 可以怎麼說 |
| --- | --- | --- |
| Released-public local evaluation | 四份 artifact 都在 1,669/1,669 個已公開 Normal／Hard 輸入上 accepted；最終執行為零模型呼叫 | 精確 artifact 與指定官方 evaluator／Lean 組合通過這些公開輸入 |
| Released Order-5 | Marathon Safe 198/200；Aggressive 200/200 | Aggressive 在這個已公開集合多取得兩份 Lean 證書 |
| Marathon 公開批次時間 | Safe 169.00 s；Aggressive 152.23 s（−9.92%） | 指定 workload 的描述性 wall-time 測量 |
| Formal submission readback | 入口顯示 4 份 participation | 四份 solver 曾成功送達並由入口讀回 |
| Private evaluation | 尚無 organizer-published score／rank | 不宣稱私人分數、名次或隱藏分布提升 |

以上 released-public 結果綁定官方 evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a` 與 Lean `4.33.1`。1,669/1,669 是很強的公開相容性與覆蓋證據，但不是私人排行榜成績。

### 四份凍結 artifact

| Track | Variant | 入口模型槽位 | Bytes | SHA-256 |
| --- | --- | --- | ---: | --- |
| Solo | Safe | Google Gemma 4 31B | 268,763 | `a81025ac454e964365f5b53b1928af3d4e4276f374d62d5b05f34264afada85a` |
| Solo | Aggressive | OpenAI gpt-oss-120b · low | 360,443 | `faf8468e6183638d35607c3bf1ae0685da838f3bfed7009c9bd5b6402071e70a` |
| Marathon | Safe | Google Gemma 4 31B | 272,898 | `05e3b837d8cdac8a0299fe66592bde787e57b10c50a0eefe24d6fdf9ae4f3d5c` |
| Marathon | Aggressive | OpenAI gpt-oss-120b · low | 366,197 | `c87e44bda89f08dad7a8a12147b28ba77a2fe288c3c3947c4dfe06b2154b8c21` |

下載原始檔：

- [Solo Safe](dist/final/solo_safe/solver.py)
- [Solo Aggressive](dist/final/solo_aggressive/solver.py)
- [Marathon Safe](dist/final/marathon_safe/solver.py)
- [Marathon Aggressive](dist/final/marathon_aggressive/solver.py)

模型配對是 slot allocation，不是公開 benchmark 的模型勝負。Aggressive 版本具有較大的有界模型輔助面，配置給 final-sprint probe 選出的 GPT-OSS；Safe 版本保持保守確定性路徑並配置不同模型家族，以降低 fallback 的相關風險。最終 1,669-row 執行沒有實際呼叫任何模型。

### 方法：證書優先的 portfolio

每題都經過固定、可重放的候選生成路線：

`正規化 → 短證明 → 小型／結構化有限反模型 → proof-producing paramodulation → symbolic narrowing／goal-guided beam → H19 去模目標搜尋 → 有界 H22 waypoint fallback → Lean judge`

核心原則：

- 題目結構選擇路線，不以 private row identity 路由。
- Fin 2／Fin 3 窮舉、結構化有限運算與 645 個具 provenance 的公開有限 magma 只負責產生候選。
- Paramodulation、narrowing 與 beam search 保留 proof DAG，不能直接輸出未驗證信念。
- H22 可讓模型提議型別化 waypoint，但文字必須先經 bounded compiler 並交給 Lean。
- Marathon 先做便宜的確定性工作，保留全域時間／token 預算，append 並同步已驗證答案，絕不以較差答案覆寫可信答案。

完整說明見 [繁體中文方法論](docs/zh-TW/methodology.md)。

### 研究歷程與負結果

Candidate 1–7 建立確定性主幹；H1–H63 依序測試效能、來源、LLM 證書、Marathon contract、殘差分群、因果策略價值與 proof-ancestry 測量。

- H19 通過 discovery、獨立 validation 與兩個 released-input no-regression gates，進入最終方法譜系。
- H22 的 bounded waypoint controller 通過其治理流程，保留為 Aggressive fail-closed fallback。
- H45 與 H49 是有效、範圍受限的 scientific fail。
- H57 只通過測量可靠性與 label capacity；不代表 ranking 或 solved-count gain。
- Candidate 28 只完成 preregistration 與 remote readback；沒有 implementation，也沒有科學結果。
- 其他許多記錄是 source shortage、governance block、instrumentation invalid 或 infrastructure stop；不能改寫成「方法被證偽」。

詳見 [H1–H63 繁體中文時間線](docs/zh-TW/research-timeline.md)、[繁體中文結果](docs/zh-TW/results.md) 與 [繁體中文聲明邊界](docs/zh-TW/claim-boundaries.md)。

### 成本

確定性 Candidate 1–19 與最終 released-public runs 在其記錄執行中沒有付費 provider 呼叫。H20–H27 有十筆正成本紀錄，合計 `US$0.918012780`。因此「整個研究零成本」不是合法聲明。

### 公開政策與安全邊界

2026-09-02 的即時讀回顯示官方頁面仍標示 `EVALUATING`；同時，官方 Contributor Network 提供 `Publish Item`，並自 2026-05-11 至 2026-09-01 持續公開 Stage 2 Solo／Marathon solver 原始碼。這支持發布 solver 與研究材料，但不支持宣稱評估完成、私人分數或名次。

公開倉庫採 allowlist 式乾淨快照。完整 evidence Git 歷史仍保持私有，因為舊 commit 含非必要的個人 email、絕對路徑、team／conversation identifier、授權文字與 host 指紋；普通刪除 commit 無法從 Git history 移除那些 bytes。

詳見 [繁體中文發布準備](docs/zh-TW/publication-readiness.md)、[繁體中文安全稽核](docs/zh-TW/security-audit-2026-09-02.md) 與 [繁體中文重現說明](docs/zh-TW/reproducibility.md)。安全問題請依 [繁體中文安全政策](SECURITY.zh-TW.md) 私下回報。

### 網站與論文

- [Proof Press 互動網站](https://f0909172434.github.io/sair-stage2-proof-press/)：拖動壓力桿，體驗 conjecture → candidate → Lean judge → claimable fact；可篩選 H1–H63 並切換中英文。
- [繁體中文研究論文](paper/main.zh-TW.md)：完整整理 solver 架構、治理方法、結果、成本、限制與重現資訊。
- [英文研究論文 PDF](https://f0909172434.github.io/sair-stage2-proof-press/paper/sair_stage2_solver_research.pdf)：可下載的六頁英文論文。
- 網站原始碼在 [`site/`](site/)；本地執行：`cd site && npm ci && npm run build`。

---

## English

### Overview

This repository records the research and final submission for the SAIR Mathematics Distillation Challenge — Equational Theories Stage 2. A solver decides whether one magma identity implies another. A `True` answer needs a replayable Lean proof; a `False` answer needs a Lean-checkable finite countermodel.

The project advanced through seven deterministic checkpoints, the governed H1–H63 program, and four frozen Solo/Marathon × Safe/Aggressive artifacts. The public release retains methods, source, aggregate results, negative results, and claim boundaries. Hash-bound history containing personal paths, private authorization text, conversation IDs, runner fingerprints, and fine-grained provider telemetry remains outside the public snapshot.

### What the evidence currently establishes

| Evidence class | Result | Supported claim |
| --- | --- | --- |
| Released-public local evaluation | All four artifacts accepted 1,669/1,669 released Normal/Hard inputs with zero model calls | The exact artifacts passed those inputs under the named evaluator and Lean toolchain |
| Released Order-5 | Marathon Safe 198/200; Aggressive 200/200 | Aggressive produced two additional Lean certificates on this released set |
| Released Marathon batch time | Safe 169.00 s; Aggressive 152.23 s (−9.92%) | Descriptive wall-time result for this workload |
| Formal submission readback | Four participation entries were visible | Four solvers reached the portal and were read back |
| Private evaluation | No organizer-published score or rank | No private-score, rank, or hidden-distribution claim |

Released results are bound to official evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a` and Lean `4.33.1`. The 1,669/1,669 result is strong evidence of released-input compatibility and coverage. It is not a private leaderboard result.

### Frozen artifacts

| Track | Variant | Portal model slot | Bytes | SHA-256 |
| --- | --- | --- | ---: | --- |
| Solo | Safe | Google Gemma 4 31B | 268,763 | `a81025ac454e964365f5b53b1928af3d4e4276f374d62d5b05f34264afada85a` |
| Solo | Aggressive | OpenAI gpt-oss-120b · low | 360,443 | `faf8468e6183638d35607c3bf1ae0685da838f3bfed7009c9bd5b6402071e70a` |
| Marathon | Safe | Google Gemma 4 31B | 272,898 | `05e3b837d8cdac8a0299fe66592bde787e57b10c50a0eefe24d6fdf9ae4f3d5c` |
| Marathon | Aggressive | OpenAI gpt-oss-120b · low | 366,197 | `c87e44bda89f08dad7a8a12147b28ba77a2fe288c3c3947c4dfe06b2154b8c21` |

Source files: [Solo Safe](dist/final/solo_safe/solver.py) · [Solo Aggressive](dist/final/solo_aggressive/solver.py) · [Marathon Safe](dist/final/marathon_safe/solver.py) · [Marathon Aggressive](dist/final/marathon_aggressive/solver.py)

The model pairing is a slot-allocation decision, not a public model bake-off. Aggressive variants expose the larger bounded model-assisted surface and use the GPT-OSS profile selected by final-sprint probes. Safe variants keep the conservative deterministic path and use another model family to reduce correlated fallback risk. None of the final 1,669-row runs invoked either model.

### Certificate-first portfolio

Each row follows a fixed, replayable candidate-generation pipeline:

`normalization → short proofs → small/structured finite countermodels → proof-producing paramodulation → symbolic narrowing/goal-guided beam → H19 demodulating goal search → bounded H22 waypoint fallback → Lean judge`

Structure selects routes; private row identity does not. Finite models, public tables, heuristics, caches, and model text are candidate generators only. Marathon performs cheap deterministic work first, reserves global time and token budget, appends and synchronizes verified answers, and never overwrites a trusted answer with a weaker one. See [Methodology](docs/methodology.md).

### Research record and negative results

Candidate 1–7 built the deterministic backbone. H1–H63 tested runtime changes, sources, model-assisted certificates, Marathon contracts, residual clustering, causal strategy value, and proof-ancestry measurement.

- H19 entered the final method lineage after discovery, disjoint validation, and two released-input no-regression gates.
- H22 survives as a bounded, fail-closed Aggressive fallback.
- H45 and H49 are valid scoped scientific failures.
- H57 passed measurement reliability and label capacity only; it established no ranking or solved-count gain.
- Candidate 28 reached preregistration and remote readback only. It has no implementation or scientific result.
- Source shortages, governance blocks, invalid instrumentation, and infrastructure stops retain their recorded operational labels. They do not become falsified methods.

See the [H1–H63 timeline](docs/research-timeline.md), [Results](docs/results.md), and [Claim boundaries](docs/claim-boundaries.md).

### Cost

Recorded deterministic Candidate 1–19 and final released-input executions used no paid provider calls. H20–H27 contain ten positive-cost records totaling `US$0.918012780`. A repository-wide zero-cost claim would therefore be false.

### Publication and security boundary

On 2026-09-02 the competition page still showed `EVALUATING`. At the same time, the official Contributor Network exposed a `Publish Item` flow and publicly displayed Stage 2 Solo and Marathon solver source posted from 2026-05-11 through 2026-09-01. That supports sharing solver and research materials; it does not establish evaluation completion, a private score, or rank.

The public repository is an allowlisted clean snapshot. The complete evidence Git history stays private because old commits contain unnecessary personal email, absolute paths, team/conversation identifiers, authorization prose, and host fingerprints. A normal deletion commit would not remove those bytes from Git history.

See [Publication readiness](docs/publication-readiness.md), [Security audit](docs/security-audit-2026-09-02.md), and [Reproducibility](docs/reproducibility.md). Please report security issues privately as described in [SECURITY.md](SECURITY.md).

### Website and paper

- [Proof Press](https://f0909172434.github.io/sair-stage2-proof-press/) turns conjecture → candidate → Lean judge → claimable fact into an interactive bilingual experience.
- [Research paper PDF](https://f0909172434.github.io/sair-stage2-proof-press/paper/sair_stage2_solver_research.pdf) covers architecture, governance, results, cost, limitations, and reproduction.
- Website source lives in [`site/`](site/). Build locally with `cd site && npm ci && npm run build`.

## Citation / 引用

```bibtex
@misc{wang2026proofpress,
  author       = {Chih-Kai Wang},
  title        = {Proof Press: Lean-Certified Portfolio Solving for Equational Implication},
  year         = {2026},
  howpublished = {GitHub repository and research artifact},
  url          = {https://github.com/f0909172434/sair-stage2-proof-press}
}
```

## License and attribution / 授權與出處

Code and original documentation are released under [Apache-2.0](LICENSE). Upstream SAIR and Equational Theories material, pinned revisions, embedded notices, and modifications are described in [NOTICE](NOTICE). Official names and trademarks remain the property of their respective owners.
