<div align="center">

<img src="assets/qiqulab-logo.png" alt="Qiqu.Lab — 奇趣實驗室" width="760">

# Skills4QiquLab

**一個面向實踐的 AI Skill 儲存庫，將有效的 AI 工作方法整理為可複用的 Skill 與配套資源。**

<p>
  <img src="https://img.shields.io/github/stars/0xf4vul/Skills4QiquLab?style=flat-square&label=Stars">
  <img src="https://img.shields.io/github/forks/0xf4vul/Skills4QiquLab?style=flat-square&label=Forks">
  <img src="https://img.shields.io/badge/Skills-8-4c9aff?style=flat-square">
  <img src="https://img.shields.io/badge/Cases-2-7c5cff?style=flat-square">
  <img src="https://img.shields.io/github/license/0xf4vul/Skills4QiquLab?style=flat-square&label=License">
</p>

[English](README.md) · [简体中文](README.zh-CN.md) · **繁體中文**

</div>

## 交流群

目前未公開獨立交流群。討論、回饋與需求可透過 [Issues](https://github.com/0xf4vul/Skills4QiquLab/issues) 進行；貢獻程式碼、文件或 Skill 請使用 [Pull Requests](https://github.com/0xf4vul/Skills4QiquLab/pulls)。

## 新增 Skill

- [Video Prompt Compression](skills/video-prompt-compression.md) — 壓縮影片 Prompt，同時保護動作順序、時間關係、鏡頭行為與主體連續性。
- [Video Prompt Optimization](skills/video-prompt-optimization.md) — 優化影片 Prompt 的動作、時間、鏡頭與主體連續性。
- [X Research](skills/x-research.md) — 以可複現、基於證據的方式研究 X 帳號與資訊源。

## 精選專案

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="cases/001_video-prompt-compression/"><img src="cases/001_video-prompt-compression/assets/svg/case-logo.svg" alt="Video Prompt Compression" width="88%"></a>
<br><strong>Video Prompt Compression</strong><br>
壓縮影片 Prompt，同時保留有意義的動作鏈、時間關係、鏡頭邏輯與主體連續性。
<br><a href="cases/001_video-prompt-compression/">Case</a> · <a href="skills/video-prompt-compression.md">Skill</a>
</td>
<td width="50%" valign="top" align="center">
<a href="cases/002_source-to-kol-research/"><img src="cases/002_source-to-kol-research/assets/svg/case-logo.svg" alt="Source-to-KOL Research" width="88%"></a>
<br><strong>Source-to-KOL Research</strong><br>
將任意輸入轉化為可驗證、可稽核的 KOL / 資訊源研究流程。
<br><a href="cases/002_source-to-kol-research/">Case</a> · <a href="skills/x-research.md">Skill</a>
</td>
</tr>
</table>

## Skill 入口

| | Skill | 作用 |
|---|---|---|
| 🧩 | [Prompt Compression](skills/prompt-compression.md) | 減少 Prompt 冗餘，同時保留意圖與硬約束 |
| ✨ | [Prompt Optimization](skills/prompt-optimization.md) | 提升清晰度、結構與執行穩定性 |
| 🔬 | [Prompt Reverse Engineering](skills/prompt-reverse-engineering.md) | 從優秀 Prompt 中提取可複用的決策結構 |
| 🎬 | [Video Prompt Compression](skills/video-prompt-compression.md) | 壓縮影片 Prompt，同時保護時間語義 |
| 🎥 | [Video Prompt Optimization](skills/video-prompt-optimization.md) | 優化動作、時間、鏡頭與主體連續性 |
| 🌐 | [Web Research](skills/web-research.md) | 將開放問題轉化為可追溯、可交叉驗證的證據 |
| 𝕏 | [X Research](skills/x-research.md) | 研究 X 帳號、人物、貼文與近期活動 |
| 🛠️ | [Skill Builder](skills/skill-builder.md) | 將重複工作沉澱為可複用、可測試的 Skill |

→ [完整 Skill 索引](skills.md)

## 儲存庫用法

儲存庫分為兩層：**Core Skills** 提供可複用的方法論；**Skill Cases** 將方法論組織成完整、可執行的實戰案例。

**選擇 Skill → 開啟對應 Skill 檔案 → 按 Workflow 執行 → 使用範本 / 範例 → 執行 Evaluation → 修改複用。**

每個 Skill 都應具備統一的實用契約：

| Skill | Purpose | Workflow | Evaluation |
|---|---|---|---|
| Prompt Compression | 在刪除冗餘的同時保留意圖 | 提取目標 → 約束 → 冗餘 → 合併 → 驗證 | 意圖 / 約束 / 關係 / 清晰度 / 壓縮率 |
| Prompt Optimization | 不改變意圖的前提下提升執行效果 | 意圖 → 約束 → 歧義 → 重構 → 驗證 | 保真 / 覆蓋 / 歧義 / 穩定性 |
| Prompt Reverse Engineering | 將優秀 Prompt 轉化為可複用結構 | 觀察 → 變數 → 結構 → 範本 → 測試 | 可遷移性 / 可控性 / 清晰度 |
| Video Prompt Compression | 縮短影片 Prompt，同時保護運動語義 | 解析 → 語義單元 → 分類 → 合併 → 驗證 | 語義 / 時間連貫 / 動作連續 |
| Video Prompt Optimization | 讓影片動作與鏡頭指令更容易執行 | 意圖 → 主體 → 動作 → 時間 → 鏡頭 → 約束 | 動作 / 時間 / 鏡頭 / 一致性 |
| Web Research | 從開放問題產生可追溯答案 | 範圍 → 搜尋 → 篩選 → 交叉驗證 → 綜合 → 引用 | 相關性 / 來源品質 / 新鮮度 / 引用 |
| X Research | 按明確標準核驗並分析 X 活動 | 發現 → 核驗 → 檢查 → 篩選 → 比較 | 身份 / 時效 / 證據 / 一致性 |
| Skill Builder | 將重複工作沉澱為可維護 Skill | 觸發 → 邊界 → Workflow → 輸出契約 → 測試 → 迭代 | 一致性 / 可遷移 / 可檢查 |

需要完整實戰流程時進入 [cases/](cases/)；需要建立新 Skill 時，從 [Skill Builder](skills/skill-builder.md) 與 [templates/skill-template.md](templates/skill-template.md) 開始。

## 聲明

本儲存庫用於學習、實驗與可複用的 AI 工作流實踐。範例及第三方引用仍受其原始來源、授權與平台規則約束；用於商業場景前請自行核驗相關權利與使用條款。

## Star 趨勢

[![Star History](https://api.star-history.com/svg?repos=0xf4vul/Skills4QiquLab&type=Date)](https://star-history.com/#0xf4vul/Skills4QiquLab&Date)

## 開源協議

[MIT License](LICENSE)
