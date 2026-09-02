# 安全政策

[繁體中文](SECURITY.zh-TW.md) · [English](SECURITY.md)

## 支援範圍

安全修正涵蓋 current default publication branch 與四份 frozen final artifact。Historical experiment code 為重現研究而保留，其中部分已停用。回報 historical code 時，請說明該 path 是否仍可從 current workflow 到達。

## 回報方式

請勿在 public issue 張貼 credential、private competition row、personal identifier 或可直接利用的細節。先透過本 repository 所屬 GitHub account 聯絡 owner 並要求 private channel。GitHub private vulnerability reporting 啟用後，可直接使用該介面。

回報請包含 affected path、revision、entry point、realistic attacker、data flow、impact 與安全的 reproduction steps。請勿附上 live key、raw private dataset、browser session 或 provider journal。

## 安全 invariant

- solved row 由 Lean acceptance 決定，model output 只提供候選。
- Provider credential 只存在 organizer-managed routing、approved secret store 或 process environment，不能 commit。
- Private evaluation row 與 raw provider journal 留在 repository 外，permission 限定 owner。
- 可能含 row、prompt、model response、certificate 或 judge feedback 的 research scratch root 必須是 owner-only directory。Sensitive file 只能由 owner read／write，caller 也不能把它放在 shared 或 symlink-controlled path。
- Public evidence 使用 repository-relative path，排除 team／account identifier、authorization quotation 與多餘 host／provider telemetry。
- 具 write permission 的 self-hosted workflow 只能執行 trusted、hash-bound source。
- Final artifact hash 與 portal mapping 必須持續綁定同四個檔案。

## 發布邊界

private evidence repository 含 historical authorization text、operational metadata、host path 與 personal Git metadata。public release 必須使用 sanitized tree 與 sanitized 或 squashed history。較晚的 cleanup commit 無法移除舊 Git objects 內的欄位。
