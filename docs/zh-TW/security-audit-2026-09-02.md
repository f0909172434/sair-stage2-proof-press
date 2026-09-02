# 安全與發布稽核，2026-09-02

[繁體中文](security-audit-2026-09-02.md) · [English](../security-audit-2026-09-02.md)

## 範圍與結果

Standard Codex Security review 針對 repository revision `56684f74569d21da043d4dc4a40e47ff9bae80bd` 的 publication risk 進行稽核。1,850 個 tracked files 全部接受 pattern scan；與發布相關的 runner、governance record、manifest、workflow、provider evidence 與 final artifact contract 接受 focused source review。

掃描得到五項 reportable finding：

| 嚴重度 | Finding | 現況與處置 |
| --- | --- | --- |
| Medium | H20–H22 historical raw scratch journal 繼承 process permission，在 permissive umask 下可能被另一個 local account 讀取。 | Historical tools 已停用且 hash-bound。private repository 可保留，public export 應排除；replacement 使用 `0700` directories 與 `0600` files。 |
| Medium | Governance evidence 包含 private authorization 原文與一個 conversation identifier。 | 公開前需要 sanitized 或 rewritten history。 |
| Low | Manifest、handoff 與 readback 含 personal absolute path 與 stable team identifier。 | clean public export 改用 relative path。 |
| Low | Self-hosted evidence 暴露 runner name、installation layout 與完整 platform fingerprint。 | public export 只保留 normalized reproducibility field。 |
| Low | Provider evidence 保留過多 timestamp、latency、token、spending 與 credential-store metadata。 | 只發布最小 allowlisted projection。 |

掃描沒有找到 literal API key、provider token、private key、password 或 private evaluation row。Repository 含有大量 generated evidence blob，因此 semantic coverage 仍屬 partial；每個 tracked path 都經 pattern scan，部分 blob 沒有完整 semantic review。

## Git history 獨立稽核

current private history 含 personal email 與 workstation-derived Git metadata。一般 cleanup commit 或 `.mailmap` 不會移除 raw commit-object field；remote branches 與 tags 也保留舊 evidence bytes。

發布路徑採用：

1. hash-bound evidence repository 保持 private。
2. 官方 Contributor Network 的 live solver-sharing surface 作為 publication authority；`EVALUATING` 只限制 private-result claim。
3. 從 allowlisted tree 建立新的 squashed public repository。
4. private provenance map 記錄 public file 與 original evidence hash 的對應。
5. sanitized repository 通過相同的 secret、metadata、license、link、hash 與 test gate 後，再驗證 anonymous access。

重寫原 repository history 會改變 sealed commit identity，需要另行做出 destructive-change 決策。

## 聲明邊界

本稽核確認已知 publication risks，也確認 reviewed material 未出現常見 literal-secret signature。它無法證明所有未知 secret 都不存在，亦未提供 private competition score 或 rank。
