---
name: x-cover-copy-studio
description: 商用级 X.com(Twitter) 推文封面海报 + 推文文案变体工坊。当用户提供一条推文(含编号列表/工具清单/资源合集)并要求制作"推文封面、X 海报、广告配图、promoted poster"或要求"推文变体/改写/换个发布风格"时使用。产出 2.41:1 复古纸感与 16:9 深色图鉴双封面(HTML→Playwright 2x 出图)及结构化文案变体, 内置防裁切布局预算与出图质检回路。
---

# X Cover & Copy Studio

一条推文 → 两款可直接投放的 X 封面 + 一条近似风格变体推文。

## 工作流(按序执行, 禁止跳过第 5 步)

0. **适用性门禁(先判再做)** — 按 `references/fit-guide.md` §四判定:
   清单体且可压缩为「名称+≤14 字价值点」→ 继续; 无清单骨架/超上限/需嵌图/主英文
   → 按边界条款降级(拆图、换 dark、或明示不适用), 不硬出。

1. **解构参考图(如有)** — 用 media-read 批量读参考图, 强制输出结构化字段:
   文字转录 / 背景色 hex / 字体层级 / 宽高比例 / 布局分区 / 装饰元素 / 气质关键词,
   归纳共同设计语言后再动手。参考图与本次产出对照见 `examples/case-pinterest-tools/refs/`。

2. **提炼推文骨架** — 开场钩子 emoji、数字承诺(N 个工具)、列表条目(URL+一句话价值)、
   结尾收藏钩子。封面上的每一条价值点必须与推文原文事实一致, 只做压缩。

3. **写文案变体** — 按 `references/copy-formulas.md` 的"保留骨架、只换血肉"配方输出:
   痛点反问开场 → N 条编号(域名+破折号+利益句) → 收藏 CTA 收尾; 域名/数量/事实不许改。

4. **填充 payload 并渲染** — 复制 `examples/.../payload.paper.json` 与 `payload.dark.json`
   改文案, 然后:
   ```bash
   python3 scripts/render.py payload.paper.json out/   # 2.41:1 纸感光 poster-paper@2x.png (4000×1660)
   python3 scripts/render.py payload.dark.json  out/   # 16:9 深色   poster-dark@2x.png  (3200×1800)
   ```
   前置依赖: `playwright`(CLI) + chromium、Google Fonts 可达、
   `--wait-for-timeout=7000` 等待 webfont; 若 chromium 报 "Executable doesn't exist",
   将缺失版本目录软链到已安装版本(见 README 故障排查)。

5. **出图质检回路(强制)** — `python3 scripts/qa_render.py out/*.png`, 把裁片交给
   media-read 逐条回答: 行数完整 / footer 未砍断 / 无遮挡 / 无 tofu / 标题为超粗黑体。
   **任何一项 FAIL → 回到布局预算表(第 6 步)修正后重渲, 直到 PASS 才可交付。**

6. **布局高度预算(paper 模板的核心约束)** — canvas 内可用 = 画布高 − 上下 padding;
   自上而下: 元信息条(~36) + `.main`(固定 height, 勿用 flex 撑开) + `.foot`(~72,
   `margin-top:auto`)。**列表行数 × 行高(≈54px) + 间距必须 ≤ .main 内高**,
   超了先减字号/内边距, 再不够就把画布加高(如 800→830), 严禁把 `.foot` 挤出画布。

## 规格速查

| 主题     | 逻辑画布      | 出图尺寸(2x)  | 比例   | 用途                        |
|----------|---------------|---------------|--------|-----------------------------|
| paper    | 2000×830      | 4000×1660     | 2.41:1 | 贴合复古横幅参考图风格      |
| dark     | 1600×900      | 3200×1800     | 16:9   | X 时间流不裁切的安全比例    |

## 资产清单

- `templates/poster-paper.html` / `templates/poster-dark.html` — token 占位模板, 可独立微调 CSS 不改脚本
- `scripts/render.py` — payload → HTML → Playwright 截图
- `scripts/qa_render.py` — 质检裁片生成 + 检查清单
- `references/design-language.md` — 配色/字体/纹理/装饰配方与通用设计语言规律
- `references/copy-formulas.md` — 标题钩子库、条目改写句式、变体红线
- `references/fit-guide.md` — 适用情况、使用边界、质量杠杆、调用门禁(配合工作流第 0 步)
- `examples/case-pinterest-tools/` — 完整实例: 7 张参考图(refs/)、双封面成图(out/)、原推/变体文案 md、双 payload

## 交付物

两款 PNG(2x) + 变体推文文本(含原始结构保留声明)。商用授权与限制见 LICENSE.md / README.md。
