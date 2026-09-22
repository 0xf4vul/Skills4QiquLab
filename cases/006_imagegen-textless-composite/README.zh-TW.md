<div align="center">

<img src="assets/svg/case-logo.svg" alt="006 — 無字底圖 + 精確疊字出圖法" width="620">

# 006 — 無字底圖 + 精確疊字出圖法

</div>

> 其他語言：[English](README.md) · [简体中文](README.zh-CN.md)

把任何「圖上要帶中文標題、關鍵數字或成套配色」的出圖需求，做成一次合成：**模型只出無字底圖，全部中文與數字由 Pillow 精確疊加**。用於公眾號封面、小紅書 / 小綠書主圖與細節卡、海報大字報、金句卡、數據結論卡。

## 項目亮點

- **模型負責畫面，腳本負責文字。** 讓圖像模型渲染中文大字，必然崩字、缺筆畫、數字錯——封面上的 `$0.71` 錯一位就是硬傷。改用 Pillow 疊加後，數字 100% 準確、字體永不崩。
- **宣告式卡片渲染器。** spec 是純 JSON，座標按 1080 寬基準寫，換畫布尺寸等比縮放。三條護欄：字號自適應（文案再長也不衝出畫布）、minimax 均衡折行（讓最長行盡可能短）、自動縱向流動（標題變高後續元素自動下移）。
- **跨平台字體探測。** 找到真實中文字體，並校驗它**真的含漢字字形**（用私有區碼位 `U+E000` 對照識別豆腐塊）。可用 `SKILL_FONT` 或 `--font` 覆蓋。
- **去浮水印。** 模型輸出右下角固定帶「AI 生成」浮水印；能裁就裁，裁不掉用左上方平均色 + 羽化 mask 覆蓋。
- **色板錨定。** 出圖前鎖死 4 個十六進位值，疊上去的字永遠壓在帳號色板上，而不是和底圖打架。

## 項目結構和說明

| 路徑 | 說明 |
|---|---|
| `SKILL.md` | 完整方法：定色板、出無字底圖、去浮水印、疊字、三個必踩坑、交付形態 |
| `scripts/render_card.py` | 宣告式卡片渲染器，`--demo` / `--dump-spec` / `--spec`，護欄內建 |
| `scripts/find_font.py` | 跨平台中文字體探測 + 豆腐塊識別 |
| `scripts/strip_watermark.py` | 去浮水印 CLI，`crop` / `patch` 雙模式 |
| `scripts/selftest.py` | 環境自檢（14 項斷言） |
| `references/pillow-recipes.md` | `overlay` / `band` / `side_dark` / `cover` / `pill` / `text` 完整源碼 + 排版速查 |
| `examples/01-step5-material-pack.md` | 完整實戰：一篇公眾號 → 6 張雙端物料 |
| `examples/demo-card.json` | 可直接改的 spec 模板 |
| `examples/demo-card.png` | `--demo` 的輸出結果 |
| `templates/` | 卡片需求採集範本 |
| `evaluation/` | 驗收清單 |
| `assets/svg/case-logo.svg` | Case 獨立 Logo |

## 庫用法

環境：Python 3 + Pillow（`pip install pillow`）。managed Python 3.13 預設沒有 Pillow，用配好的 venv，或 `python -m venv` 後 `pip install pillow`（走代理 `http://127.0.0.1:7890`）。

**定色板 → 出無字底圖 → 去浮水印 → 疊字 → 校驗**

```bash
pip install pillow
python scripts/selftest.py                               # 先確認環境（14 項斷言）
python scripts/render_card.py --demo -o demo.png         # 純程式碼出圖，不需要圖像模型
python scripts/render_card.py --dump-spec > my-card.json
python scripts/render_card.py --spec my-card.json -o out.png
```

參數速記：`--demo` 渲染範例卡 · `--dump-spec` 匯出 spec 範本 · `--spec` 按 JSON 渲染 · `--font` 覆蓋字體路徑 · `--out` 輸出檔案。

腳本只做**確定性組裝**（算佈局、縮字號、合成圖層），創意判斷（色板、隱喻、文案）留給呼叫方。

## 三條硬約束

- 圖像模型 prompt **必須**帶：`Absolutely no text, no letters, no words, no numbers, no watermark, no logo`
- 全部中文與數字由 Pillow 疊加，**禁止讓模型渲染中文大字**
- 半透明元素畫在 RGBA 圖層上再 `alpha_composite`；壓暗條只用純色 + alpha mask，**禁止深色→白色雙色漸變**

## 核心原則

模型負責畫面，腳本負責文字。凡是**畫出來**（而非生成出來）的，才穩——封面上一個數字錯一位就是硬傷。

## 來源

提純自 2026-09-22 公眾號→小綠書雙端物料包實戰（`wechat-xiaolushu-material-pack` 跑通後）：把「無字底圖 + 精確疊字」這一步單獨抽出來獨立運行。MIT License。
