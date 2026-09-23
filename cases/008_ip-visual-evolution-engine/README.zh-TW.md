# Case 008 · 個人 IP 視覺進化引擎（IP Visual Evolution Engine）

**把一個人的身份、能力、價值觀與成長故事，轉譯為一個可持續演化的連續視覺 IP，再壓縮成小紅書 / 小綠書 3:4 直版「六鏡連續敘事」與可遷移的 X.com Banner。**

[English](README.md) · [簡體中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

## 它解決什麼

多數個人 IP 視覺做法是「一張一張出圖」：今天一張頭像、明天一張海報、後天一張 Banner，每張都重新寫 Prompt、重新設計角色、重新定風格——結果六張圖像六個不相關的設計師做的。

本 Engine 把它工程化為一條可複用流水線：先定義一次「視覺 IP DNA」與「連續性契約」，然後讓每一張圖只是**同一個 IP 狀態機的下一步狀態轉移**，而不是一次新的創作。

**產物**：小紅書 / 小綠書 3:4 直版「六鏡」知識卡 × 6（一鏡到底的連續鏡頭）+ 一張可適配 X.com 的 Banner 母版（FRAME 06 適配 1500×500）。

## 流水管道

```
身份 → 視覺 IP DNA → 連續性契約 → 六鏡狀態機 → 平台適配器 → Banner 適配器 → 視覺質檢
```

## 六鏡狀態機

| 鏡 | 階段 | 狀態轉移 |
|---|---|---|
| 01 | MASTER（主圖） | 建立整個視覺世界 |
| 02 | IDENTITY | 職業 → 能力 → 隱喻 |
| 03 | EVOLUTION | `混沌→流動→系統→靜默→存在` |
| 04 | CONTINUITY | 身份 + 動作 + 世界 連續 |
| 05 | ENTROPY / WEIGHT | 熵減，視覺權重重分配 |
| 06 | PRESENCE / BANNER | 最終 Hero，可適配 X 1500×500 |

## 平台適配器（每條線獨立自包含）

| 平台 | 連續方式 | 策略 |
|---|---|---|
| Seedream | 多參考 / 連續生成 | 完整 Creative Brief + 參考圖順序生成 |
| GPT | 對話式逐層編輯 | `KEEP EXACTLY` / `CHANGE ONLY` |
| Grok | 連續視覺導演 | 連續分鏡敘事 + 顯式鏡編號 |
| Gemini | 參考圖 + 對話 | 上一張作主參考 + 角色命名 + 五維 |

每條適配器檔案都可以**單獨拿來跑完整個六鏡流程**：

- [`references/adapters/seedream.md`](references/adapters/seedream.md)
- [`references/adapters/gpt.md`](references/adapters/gpt.md)
- [`references/adapters/grok.md`](references/adapters/grok.md)
- [`references/adapters/gemini.md`](references/adapters/gemini.md)

## 怎麼開始

1. 填 [`templates/fill-in-sheet.md`](templates/fill-in-sheet.md)（或直接用已填範例 [`examples/zhuji-mao/`](examples/zhuji-mao/)）。
2. 選一條平台適配器，按「呼叫節奏」逐鏡生成：MASTER → 次圖 01–05。
3. 收尾用 **Banner 適配器**（[`SKILL.md`](SKILL.md) 第 7 節）把 FRAME 06 適配成 X.com 1500×500。
4. 跑 [`evaluation/evaluation-schema.json`](evaluation/evaluation-schema.json)；低於門檻回到失效鏡局部修復。

## 檔案結構

- `SKILL.md` — Engine 內核：公式、流水線、DNA、連續性契約、六鏡狀態機、適配器選型、Banner 適配器、質檢、評測。
- `references/adapters/*.md` — 四條自包含平台流程。
- `templates/fill-in-sheet.md` — 一次性 DNA 定義（空白範本）。
- `examples/zhuji-mao/` — 已填好的「築基貓」範例。
- `evaluation/evaluation-schema.json` — 啟發式本地評測。

## 核心公式

`IP 視覺演化 = 身份連續性 × 敘事連續性 × 動作連續性 × 視覺熵梯度 × 視覺權重 × 空間連續性 × 氣場精煉 × 平台適配`

**換主體，不換 Engine。**
