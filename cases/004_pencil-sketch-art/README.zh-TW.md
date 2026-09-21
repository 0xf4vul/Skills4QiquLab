<div align="center">

<img src="assets/svg/case-logo.svg" alt="004 — 鉛筆素描手繪圖" width="620">

# 004 — 鉛筆素描手繪圖

</div>

> 其他語言：[English](README.md) · [简体中文](README.zh-CN.md)

把任意主題、文字描述或抽象概念，生成一張**石墨鉛筆素描手繪風**插畫。單圖交付，不依賴任何資訊圖或排版流程。

## 項目亮點

- **抽象概念先轉譯，再落筆**。「內捲」畫不出來，但「一個人在跑步機上原地跑，跑步機插著一面狂轉的鐘」畫得出來。`references/prompt-library.md` 裡給了五組現成轉譯。
- **六種筆觸預設**：純線稿 / 排線明暗 / 炭筆粗礪 / 淡彩素描 / 場景透視 / 概念隱喻。
- **兩個可跑的腳本**：`build_prompt.py` 組裝 prompt，並硬攔圖內文字超過 8 字；`crop.py` 用逐行墨量定位主體，**看不到圖也能安全裁切**——封面臨時改比例不必重跑生圖。
- **文字絕不進 prompt**。底圖一律生成為無字圖，文案在排版環節疊加。圖內燒字是毀掉一張好素描最常見的方式。
- **背景必須是紙色，不能純白**。米白紙紋是區分「素描」與「數位繪畫」最快的訊號。

## 項目結構和說明

| 路徑 | 說明 |
|---|---|
| `SKILL.md` | 完整方法：主體決策、畫幅規則、筆觸預設、prompt 組裝、8 條自檢清單 |
| `scripts/build_prompt.py` | prompt 建構器，`--list` 查預設，校驗文字長度 / 畫幅 / 點綴色 / 光源 |
| `scripts/crop.py` | 墨量裁切器，支援 `--ratio` `--top-safe` `--bottom-safe` `--dry-run` |
| `scripts/presets.json` | 預設資料：筆觸 / 媒介 / 明暗 / 構圖 / 負面詞。改資料不改程式碼 |
| `references/prompt-library.md` | 概念轉譯表 + 分主體 prompt 範式 |
| `references/style-tokens.md` | 9 個 token 桶：媒介 / 筆觸 / 光影 / 紙 / 色 / 品質 / 負面 / 畫幅 / 參數 |
| `references/troubleshooting.md` | 16 種翻車現象 → 根因 → 改法 |
| `examples/` | 四個完整案例，含八張成套金句卡 |
| `templates/` | 需求採集範本 |
| `assets/gallery/` | 已發布成品 |

## 庫用法

**定主體 → 選畫幅 → 選筆觸 → 建構 prompt → 出圖 → 裁切 → 自檢**

```bash
python scripts/build_prompt.py --list
python scripts/build_prompt.py -s "a paper boat drifting on a sea of folded resumes" -p 3 -a portrait
python scripts/crop.py --in raw.png --ratio 2.35 --bottom-safe 0.26 --width 900 --out cover.png
```

參數速記：`-s` 主體 / `-p` 筆觸（1-6 或 key 或中文名）/ `-a` 畫幅 / `--accent` 點綴色 / `--light` 光源 / `-t` 圖內文字（≤8 字）/ `-o` 輸出檔案。

腳本只做**確定性組裝**（拼 token、算 size、校驗長度），創意判斷留給呼叫方。

## 三條硬約束

- 圖內文字 **≤ 8 字**，大段文字一律走無字底圖 + 排版疊加
- 色彩 **≤ 1 個低飽和色相**，背景必須紙色，**禁用純白**
- 生成參數固定 `quality=high`、`style=natural`（vivid 會毀掉石墨質感）

## 發布比例

公眾號封面 **2.35**（900×383）· 正文圖 **寬 ≤1080** · 小紅書 **3:4** · 視頻號 **9:16** · 金句卡 **2:3**

## 核心原則

做減法，不做加法。畫面裡**少了什麼**，往往才是意思所在——算盤要扣下，水表要缺席，檯燈要關掉。

## 來源

提純自 `infographic-maker`：剝掉資訊圖的排版與構圖約束，把手繪風格層單獨抽出來獨立運行。原技能未改動。MIT License。
