# Proof Press：SAIR Stage 2 Lean 證書型 Solver

[繁體中文](#繁體中文) · [English](#english) · [互動網站](https://chih-kai-wang.github.io/sair-stage2-proof-press/) · [英文研究論文 PDF](https://chih-kai-wang.github.io/sair-stage2-proof-press/paper/sair_stage2_solver_research.pdf) · [官方 Contributor Network](https://competition.sair.foundation/contributor-network?competition=mathematics-distillation-challenge-equational-theories-stage2)

> 搜尋可以提出候選答案，但只有 Lean 接受的證書才算結果。

## 繁體中文

### 專案概覽

這個 repo 記錄 SAIR Mathematics Distillation Challenge 中 Equational Theories Stage 2 的研究過程與最終提交。任務要求 solver 判斷一條 magma 等式是否蘊含另一條。回答 `True` 時必須附上 Lean 可以重放的通用證明，回答 `False` 時必須附上 Lean 可以檢查的有限反模型。

專案先建立七個確定性 checkpoint，接著進行 H1–H63 的研究計畫，每個假設都依事先寫定的關卡判定。最後凍結四份 solver：Solo 與 Marathon 兩條賽道，各有 Safe 與 Aggressive 兩個版本。

公開版本保留方法、程式碼、彙總結果、負結果與聲明邊界。另有一批以雜湊綁定的歷史紀錄，內含個人路徑、授權原文、對話 ID、runner 指紋與細粒度的 provider telemetry，這批紀錄不在公開快照中。

### 目前能確認的結果

| 證據層級 | 結果 | 可以怎麼說 |
| --- | --- | --- |
| Released-public local evaluation | 四份 artifact 都在 1,669/1,669 個已公開 Normal／Hard 輸入上 accepted；最終執行為零模型呼叫 | 精確 artifact 與指定官方 evaluator／Lean 組合通過這些公開輸入 |
| Released Order-5 | Marathon Safe 198/200；Aggressive 200/200 | Aggressive 在這個已公開集合多取得兩份 Lean 證書 |
| Marathon 公開批次時間 | Safe 169.00 s；Aggressive 152.23 s（−9.92%） | 指定 workload 的描述性 wall-time 測量 |
| Formal submission readback | 入口顯示 4 份 participation | 四份 solver 曾成功送達並由入口讀回 |
| Official Main Leaderboard（2026-10-04 公布；2026-11-11 讀取） | 四份 solver 都是 193/200：Solo Safe（Gemma 4 31B）第 20 名／294、Solo Aggressive（gpt-oss-120b）第 18 名／294、Marathon Safe（Gemma 4 31B）第 16 名／294、Marathon Aggressive（gpt-oss-120b）第 14 名／294；四組都與其他隊同分並列 | 官方公布的 Main Leaderboard 名次；共294隊參加。比賽頁仍標示 `EVALUATING`，所以不宣稱這是最終名次或獎項 |
| Official Research Leaderboard（2026-09-18 公布） | 四份 solver 都記為 0 分，許多隊伍也是 0 | 本 repo 尚未分析這個榜的計分方式，不據此做任何主張 |

表中的公開輸入結果都綁定官方 evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a` 與 Lean `4.33.1`。1,669/1,669 有力地說明四份 solver 與公開輸入相容，而且涵蓋了全部公開輸入，但它不是私人排行榜的成績；正式評估成績見上表的官方 Main Leaderboard。

### 四份最終 solver

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

表中的模型欄是每份提交在入口網站上選的模型槽位。這是配置上的決定，不代表兩個模型在公開 benchmark 上比過高下。Aggressive 版本允許較多有界的模型輔助，因此配上最後衝刺階段探測所選出的 GPT-OSS。Safe 版本走保守的確定性路徑，並配上另一個模型家族，以降低兩邊 fallback 同時出錯的風險。最終 1,669 筆的執行完全沒有呼叫任何模型。

### 方法：證書優先的 portfolio

每一題都走同一條固定、可重放的候選生成路線：

`正規化 → 短證明 → 小型／結構化有限反模型 → proof-producing paramodulation → symbolic narrowing／goal-guided beam → H19 去模目標搜尋 → 有界 H22 waypoint fallback → Lean judge`

核心原則如下：

- 路線由題目的結構決定，不依私人題目的身分選路。
- Fin 2／Fin 3 窮舉、結構化有限運算，以及 645 個附來源紀錄的公開有限 magma，都只負責產生候選。
- Paramodulation、narrowing 與 beam search 會保留 proof DAG，不能直接輸出未經驗證的判斷。
- H22 允許模型提出有型別的 waypoint，但模型輸出的文字必須先經過有界的 compiler，再交給 Lean 檢查。
- Marathon 先做成本低的確定性工作，並保留全域的時間與 token 預算。已驗證的答案會追加寫入並同步，較差的答案永遠不會覆寫已經可信的答案。

完整說明見 [繁體中文方法論](docs/zh-TW/methodology.md)。

### 研究歷程與負結果

Candidate 1–7 建立了確定性的主幹。H1–H63 接著依序測試效能、來源、LLM 證書、Marathon contract、殘差分群、因果策略價值與 proof-ancestry 測量。

- H19 通過探索、獨立驗證與兩道「公開輸入不退步」關卡，成為最終方法的一部分。
- H22 的有界 waypoint controller 通過了它的審核流程，保留為 Aggressive 版本的 fail-closed fallback。
- H45 與 H49 是有效的科學負結果，範圍限於各自的預先登記設定。
- H57 只通過測量可靠性與 label capacity 兩個問題，不代表排序能力或解題數有所提升。
- Candidate 28 只完成預先登記與遠端讀回，沒有實作，也沒有科學結果。
- 其他許多紀錄停在來源不足、治理阻擋、量測無效或基礎設施中止。這些紀錄不能改寫成「方法被證偽」。

詳見 [H1–H63 繁體中文時間線](docs/zh-TW/research-timeline.md)、[繁體中文結果](docs/zh-TW/results.md) 與 [繁體中文聲明邊界](docs/zh-TW/claim-boundaries.md)。

### 這份紀錄不主張什麼

- 名次只引用官方 Main Leaderboard（2026-10-04 公布）。比賽頁在 2026-11-11 仍標示 `EVALUATING`，因此不主張最終名次或任何獎項。
- 不主張 Aggressive 在隱藏題目分布上普遍優於 Safe。Aggressive 多解出的兩題，只是在公開的 Order-5 集合上量到的。
- 不主張本地相容性測試等同於正式比賽的沙盒環境。

### 成本

確定性的 Candidate 1–19 與最終的公開輸入執行，在有紀錄的執行中都沒有付費的 provider 呼叫。H20–H27 有十筆成本大於零的紀錄，合計 `US$0.918012780`。所以不能說整個研究零成本。

### 公開政策與安全邊界

2026-09-02 讀回時，官方頁面仍標示 `EVALUATING`。同一時間，官方 Contributor Network 提供 `Publish Item` 功能，而且從 2026-05-11 到 2026-09-01 一直公開展示 Stage 2 Solo 與 Marathon 的 solver 原始碼。這可以作為發布 solver 與研究材料的依據，但不能用來宣稱評估已經完成，也不能用來宣稱私人分數或名次。2026-11-11 再查：官方已於 2026-10-04 公布 Main Leaderboard（見上方結果表），比賽頁仍標示 `EVALUATING`。

公開 repo 是依白名單挑選檔案後重新建立的乾淨快照。完整的研究證據 Git 歷史仍然保持私有，因為舊 commit 含有不必要的個人 email、絕對路徑、team 與 conversation identifier、授權文字與主機指紋。一般的刪除 commit 無法把這些 bytes 從 Git 歷史中移除。

詳見 [繁體中文發布準備](docs/zh-TW/publication-readiness.md)、[繁體中文安全稽核](docs/zh-TW/security-audit-2026-09-02.md) 與 [繁體中文重現說明](docs/zh-TW/reproducibility.md)。發現安全問題時，請依 [繁體中文安全政策](SECURITY.zh-TW.md) 私下回報。

### 網站與論文

- [Proof Press 互動網站](https://chih-kai-wang.github.io/sair-stage2-proof-press/)：拖動頁面上的控制桿，可以看到一個猜想如何變成候選答案、交給 Lean judge 檢查，最後成為可以主張的事實。網站可以篩選 H1–H63，也可以切換中英文。
- [英文研究論文 PDF](https://chih-kai-wang.github.io/sair-stage2-proof-press/paper/sair_stage2_solver_research.pdf)：用六頁整理 solver 架構、治理方法、結果、成本、限制與重現資訊。
- 網站原始碼在 [`site/`](site/)，本地建置的指令是 `cd site && npm ci && npm run build`。

---

## English

### Overview

This repository records the research and the final submission for Equational Theories Stage 2 of the SAIR Mathematics Distillation Challenge. A solver must decide whether one magma identity implies another. A `True` answer needs a replayable Lean proof, and a `False` answer needs a finite countermodel that Lean can check.

The project went through seven deterministic checkpoints and then the H1–H63 research program, in which each hypothesis was judged against gates written down in advance. It ended with four final solvers: a Safe and an Aggressive variant for each of the Solo and Marathon tracks.

The public release keeps the methods, source code, aggregate results, negative results and claim boundaries. A hash-bound history that contains personal paths, private authorization text, conversation IDs, runner fingerprints and fine-grained provider telemetry is not part of the public snapshot.

### What the evidence currently establishes

| Evidence class | Result | Supported claim |
| --- | --- | --- |
| Released-public local evaluation | All four artifacts accepted 1,669/1,669 released Normal/Hard inputs with zero model calls | The exact artifacts passed those inputs under the named evaluator and Lean toolchain |
| Released Order-5 | Marathon Safe 198/200; Aggressive 200/200 | Aggressive produced two additional Lean certificates on this released set |
| Released Marathon batch time | Safe 169.00 s; Aggressive 152.23 s (−9.92%) | Descriptive wall-time result for this workload |
| Formal submission readback | Four participation entries were visible | Four solvers reached the portal and were read back |
| Official Main Leaderboard (published 2026-10-04; read 2026-11-11) | All four solvers scored 193/200: Solo Safe (Gemma 4 31B) rank 20 of 294, Solo Aggressive (gpt-oss-120b) rank 18 of 294, Marathon Safe (Gemma 4 31B) rank 16 of 294, Marathon Aggressive (gpt-oss-120b) rank 14 of 294; each rank is shared with other teams on the same score | Organizer-published Main Leaderboard ranks; 294 teams took part. The competition page still shows `EVALUATING`, so no final-rank or prize claim |
| Official Research Leaderboard (published 2026-09-18) | All four solvers are listed at 0, as are many other teams | This repository has not analysed how that board is scored and makes no claim from it |

All released-input results are tied to official evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a` and Lean `4.33.1`. The 1,669/1,669 result is strong evidence that the solvers are compatible with the released inputs and cover all of them. It is not a private leaderboard result; the official evaluation result is the Main Leaderboard row in the table above.

### The four final solvers

| Track | Variant | Portal model slot | Bytes | SHA-256 |
| --- | --- | --- | ---: | --- |
| Solo | Safe | Google Gemma 4 31B | 268,763 | `a81025ac454e964365f5b53b1928af3d4e4276f374d62d5b05f34264afada85a` |
| Solo | Aggressive | OpenAI gpt-oss-120b · low | 360,443 | `faf8468e6183638d35607c3bf1ae0685da838f3bfed7009c9bd5b6402071e70a` |
| Marathon | Safe | Google Gemma 4 31B | 272,898 | `05e3b837d8cdac8a0299fe66592bde787e57b10c50a0eefe24d6fdf9ae4f3d5c` |
| Marathon | Aggressive | OpenAI gpt-oss-120b · low | 366,197 | `c87e44bda89f08dad7a8a12147b28ba77a2fe288c3c3947c4dfe06b2154b8c21` |

Source files:

- [Solo Safe](dist/final/solo_safe/solver.py)
- [Solo Aggressive](dist/final/solo_aggressive/solver.py)
- [Marathon Safe](dist/final/marathon_safe/solver.py)
- [Marathon Aggressive](dist/final/marathon_aggressive/solver.py)

The model column records which model slot each portal entry selected. That was an allocation decision, not a public comparison between models. The Aggressive variants allow more bounded model assistance, so they use the GPT-OSS profile that final-sprint probes selected. The Safe variants keep the conservative deterministic path and use a different model family, which lowers the risk that both fallbacks fail together. None of the final 1,669-row runs called either model.

### Method: certificate-first portfolio

Every row goes through the same fixed, replayable candidate-generation pipeline:

`normalization → short proofs → small/structured finite countermodels → proof-producing paramodulation → symbolic narrowing/goal-guided beam → H19 demodulating goal search → bounded H22 waypoint fallback → Lean judge`

The structure of a problem chooses its route; the identity of a private row never does. Finite models, public tables, heuristics, caches and model text only generate candidates, and only Lean decides. Marathon does the cheap deterministic work first and reserves a global budget of time and tokens. It appends and synchronizes verified answers, and it never overwrites a trusted answer with a weaker one. See [Methodology](docs/methodology.md).

### Research record and negative results

Candidate 1–7 built the deterministic backbone. H1–H63 then tested runtime changes, sources, model-assisted certificates, Marathon contracts, residual clustering, causal strategy value and proof-ancestry measurement.

- H19 joined the final method after it passed discovery, a disjoint validation and two no-regression gates on released inputs.
- H22 remains in the Aggressive variants as a bounded fallback that fails closed.
- H45 and H49 are valid scientific failures, each limited to its preregistered scope.
- H57 passed only its measurement-reliability and label-capacity questions. It showed no gain in ranking or in the number of solved problems.
- Candidate 28 reached preregistration and remote readback only. It has no implementation and no scientific result.
- Many other records ended in a source shortage, a governance block, invalid instrumentation or an infrastructure stop. They keep those operational labels and are not reported as falsified methods.

See the [H1–H63 timeline](docs/research-timeline.md), [Results](docs/results.md), and [Claim boundaries](docs/claim-boundaries.md).

### What this record does not claim

- Ranks are quoted only from the official Main Leaderboard (published 2026-10-04). The competition page still showed `EVALUATING` on 2026-11-11, so the record claims no final rank and no prize.
- It does not claim that Aggressive beats Safe on the hidden distribution. Its two extra accepted rows were measured only on the released Order-5 set.
- It does not claim that a local compatibility check is equivalent to the production sandbox.

### Cost

The recorded deterministic runs of Candidate 1–19 and the final released-input runs used no paid provider calls. H20–H27 contain ten records with a positive cost, totaling `US$0.918012780`. A claim that the whole project cost nothing would therefore be false.

### Publication and security boundary

On 2026-09-02 the competition page still showed `EVALUATING`. At the same time, the official Contributor Network offered a `Publish Item` flow and publicly displayed Stage 2 Solo and Marathon solver source posted from 2026-05-11 through 2026-09-01. That supports sharing the solvers and research materials. It does not show that evaluation has finished, and it gives no private score or rank. Rechecked on 2026-11-11: the organizers published the Main Leaderboard on 2026-10-04 (see the results table above), and the competition page still shows `EVALUATING`.

The public repository is a clean snapshot built from an explicit allowlist of files. The complete Git history of the evidence repository stays private, because old commits contain unnecessary personal email, absolute paths, team and conversation identifiers, authorization text and host fingerprints. A normal deletion commit would not remove those bytes from Git history.

See [Publication readiness](docs/publication-readiness.md), [Security audit](docs/security-audit-2026-09-02.md), and [Reproducibility](docs/reproducibility.md). Please report security issues privately as described in [SECURITY.md](SECURITY.md).

### Website and paper

- [Proof Press](https://chih-kai-wang.github.io/sair-stage2-proof-press/) is an interactive bilingual site. It shows how a conjecture becomes a candidate, goes to the Lean judge and ends as a fact you can claim.
- The [research paper PDF](https://chih-kai-wang.github.io/sair-stage2-proof-press/paper/sair_stage2_solver_research.pdf) covers the architecture, governance, results, cost, limitations and reproduction.
- The website source lives in [`site/`](site/). Build it locally with `cd site && npm ci && npm run build`.

## Citation / 引用

```bibtex
@misc{wang2026proofpress,
  author       = {Chih-Kai Wang},
  title        = {Proof Press: Lean-Certified Portfolio Solving for Equational Implication},
  year         = {2026},
  howpublished = {GitHub repository and research artifact},
  url          = {https://github.com/Chih-Kai-Wang/sair-stage2-proof-press}
}
```

## License and attribution / 授權與出處

Code and original documentation are released under [Apache-2.0](LICENSE). Upstream SAIR and Equational Theories material, pinned revisions, embedded notices, and modifications are described in [NOTICE](NOTICE). Official names and trademarks remain the property of their respective owners.
