# 發布準備

[繁體中文](publication-readiness.md) · [English](../publication-readiness.md)

## 決策

完整 evidence repository 與既有 Git history 含有不適合公開的 metadata。公開發布採用經過清理的 companion repository，完整 evidence repository 繼續保持 private。

Competition status 需要與 publication permission 分開判讀。2026-09-02 的 overview 仍顯示 `EVALUATING`；官方 Contributor Network 同時提供 `Publish Item` 流程，並公開顯示 2026-05-11 至 2026-09-01 張貼的 Stage 2 Solo／Marathon solver source。這是官方平台支持此期間分享 solver 的直接證據，沒有提供 evaluation completion、private score 或 rank。

發布風險集中在原 repository history。Git metadata 含非 noreply 的個人／本機 email；舊 commits 與 remote branches 還保留 team identifier、絕對 home path、private authorization text、credential-store metadata、provider telemetry 與 runner fingerprint。只清理 current branch 無法移除 public repository 內的舊 Git objects。

## 已完成檢查

- Current tracked tree：1,850 files，掃描常見 key、token、private key、personal path、team 與 authorization marker。
- Git patch history：1,537 commits，掃描常見 private-key 與 provider／cloud token signature。
- Strong secret signature：0。
- Current absolute home-path reference：368 個 tracked files，共 1,255 occurrences。
- Current team-identifier reference：13 個 files，共 13 occurrences。
- Git author／committer metadata：五個 unique address，包含 GitHub noreply、一個 Gmail 與一個 local machine address。
- Standard source security scan：三份獨立 review packet，找到兩個 medium 與數個 low publication risk；未找到 literal credential。

## 已驗證的發布風險

- Medium：H20–H22 historical research runner 在 permissive umask 下可能建立可被其他本機 account 讀取的 raw scratch journal。這些工具不應進入 public export；replacement 必須使用 `0700` directory 與 `0600` file。
- Medium：sealed evidence 保留 private authorization 原文與一個 source-conversation identifier。後續 deletion commit 無法從 public Git history 移除這些 bytes。
- Low：manifest、handoff 與 evidence 暴露 personal absolute path、stable team identifier、runner name、installation layout 與多餘 host fingerprint。
- Low：committed provider evidence 保留超出 public reproducibility 所需的 timing、token、spending 與 credential-store metadata。
- Low：reachable Git history 除 noreply identity 外，還含 personal Gmail 與 workstation-derived local address。

這些檢查無法保證不存在任何未知 secret。已知風險集中在 metadata／privacy 與 historical local-journal control；掃描沒有發現 live API key。

## 發布 gate

公開 companion repository 前需完成：

1. 保存 Contributor Network 的即時發布證據，並把 `EVALUATING` 限定在 private-result claim。
2. 完成 Standard security scan，關閉或記錄每項 finding。
3. 依明確 allowlist 建立 sanitized、squashed repository；private evidence repository 與 offline provenance map 維持原狀。
4. 排除 historical branches 與 tags，public repository 從一個 reviewed root commit 開始。
5. 排除 team identifier、authorization quotation、credential-store service detail、personal absolute path、source-conversation identifier 與多餘 runner／provider telemetry。
6. 確認四份 frozen solver hash 完全未變。
7. 完成 code、website、document、license、link、secret 與 metadata checks。
8. push clean snapshot，確認 repository 為 `PUBLIC`，再從 GitHub 回讀代表性檔案。
9. 部署 GitHub Pages，經匿名 HTTPS 驗證網站、assets 與 paper。

## 歷史證據政策

sealed scientific record 的 hash 與 remote readback 屬於研究紀錄，不能靜默重寫。public release 採用下列策略：

- private evidence repository 保持完整；public companion repository 只含 sanitized、provenance-linked release tree。
- 若未來必須 history rewrite，需留下書面紀錄、offline private archive 與 old-to-new evidence identity map。

使用者已授權公開 GitHub release，沒有要求 destructive force-push 或刪除 historical branches。現行方案使用 clean public export，避免改動 hash-bound private history。
