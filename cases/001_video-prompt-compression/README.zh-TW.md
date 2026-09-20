<div align="center">

<img src="assets/svg/case-logo.svg" alt="001 — Video Prompt Compression" width="620">

# 001 — Video Prompt Compression

</div>

> 其他語言：[English](README.md) · [简体中文](README.zh-CN.md)

將影片提示詞壓縮得更短、更高密度，同時保留生成結果真正依賴的動作、時間、鏡頭與連續性資訊。

## 專案亮點

- **語義保真壓縮**：減少冗餘，但不把多個有意義的動作粗暴合併。
- **時間關係保護**：保留動作順序、持續時間、停頓、轉場與因果關係。
- **鏡頭邏輯保護**：將鏡頭運動、景別變化與連續性視為硬約束處理。
- **反向展開評測**：將壓縮結果重新展開，檢查關鍵原始語義是否仍可恢復。
- **失敗案例驅動**：涵蓋 Verb Collapse、Time Deletion、False Continuity 等典型失敗模式。

## 專案結構與說明

| 路徑 | 說明 |
|---|---|
| `SKILL.md` | 核心壓縮方法、邊界、Workflow、輸出契約與失敗模式 |
| `templates/` | 可複用的 Skill 範本與影片 Prompt 範本 |
| `examples/` | 基礎案例、連續動作案例與失敗案例 |
| `evaluation/` | 評測標準與反向展開檢查 |
| `assets/svg/` | 專案 Logo 與可複用 SVG 資源 |

## 儲存庫用法

**閱讀 SKILL.md → 選擇範本 → 參考案例 → 執行壓縮 → 執行評測 → 複用**

完整方法見 [SKILL.md](SKILL.md)；評測入口見 [evaluation/](evaluation/)；快速開始見 [templates/](templates/)。

## 邊界

不能為了追求更短而刪除動作語義、時間關係、鏡頭行為、因果依賴或連續性約束。