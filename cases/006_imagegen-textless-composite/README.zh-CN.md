<div align="center">

<img src="assets/svg/case-logo.svg" alt="006 — 无字底图 + 精确叠字出图法" width="620">

# 006 — 无字底图 + 精确叠字出图法

</div>

> 其他语言：[English](README.md) · [繁體中文](README.zh-TW.md)

把任何「图上要带中文标题、关键数字或成套配色」的出图需求，做成一次合成：**模型只出无字底图，全部中文与数字由 Pillow 精确叠加**。用于公众号封面、小红书 / 小绿书主图与细节卡、海报大字报、金句卡、数据结论卡。

## 项目亮点

- **模型负责画面，脚本负责文字。** 让图像模型渲染中文大字，必然崩字、缺笔画、数字错——封面上的 `$0.71` 错一位就是硬伤。改用 Pillow 叠加后，数字 100% 准确、字体永不崩。
- **声明式卡片渲染器。** spec 是纯 JSON，坐标按 1080 宽基准写，换画布尺寸等比缩放。三条护栏：字号自适应（文案再长也不冲出画布）、minimax 均衡折行（让最长行尽可能短）、自动纵向流动（标题变高后续元素自动下移）。
- **跨平台字体探测。** 找到真实中文字体，并校验它**真的含汉字字形**（用私有区码位 `U+E000` 对照识别豆腐块）。可用 `SKILL_FONT` 或 `--font` 覆盖。
- **去水印。** 模型输出右下角固定带「AI 生成」水印；能裁就裁，裁不掉用左上方平均色 + 羽化 mask 覆盖。
- **色板锚定。** 出图前锁死 4 个十六进制值，叠上去的字永远压在账号色板上，而不是和底图打架。

## 项目结构和说明

| 路径 | 说明 |
|---|---|
| `SKILL.md` | 完整方法：定色板、出无字底图、去水印、叠字、三个必踩坑、交付形态 |
| `scripts/render_card.py` | 声明式卡片渲染器，`--demo` / `--dump-spec` / `--spec`，护栏内建 |
| `scripts/find_font.py` | 跨平台中文字体探测 + 豆腐块识别 |
| `scripts/strip_watermark.py` | 去水印 CLI，`crop` / `patch` 双模式 |
| `scripts/selftest.py` | 环境自检（14 项断言） |
| `references/pillow-recipes.md` | `overlay` / `band` / `side_dark` / `cover` / `pill` / `text` 完整源码 + 排版速查 |
| `examples/01-step5-material-pack.md` | 完整实战：一篇公众号 → 6 张双端物料 |
| `examples/demo-card.json` | 可直接改的 spec 模板 |
| `examples/demo-card.png` | `--demo` 的输出结果 |
| `templates/` | 卡片需求采集模板 |
| `evaluation/` | 验收清单 |
| `assets/svg/case-logo.svg` | Case 独立 Logo |

## 库用法

环境：Python 3 + Pillow（`pip install pillow`）。managed Python 3.13 默认没有 Pillow，用配好的 venv，或 `python -m venv` 后 `pip install pillow`（走代理 `http://127.0.0.1:7890`）。

**定色板 → 出无字底图 → 去水印 → 叠字 → 校验**

```bash
pip install pillow
python scripts/selftest.py                               # 先确认环境（14 项断言）
python scripts/render_card.py --demo -o demo.png         # 纯代码出图，不需要图像模型
python scripts/render_card.py --dump-spec > my-card.json
python scripts/render_card.py --spec my-card.json -o out.png
```

参数速记：`--demo` 渲染示例卡 · `--dump-spec` 导出 spec 模板 · `--spec` 按 JSON 渲染 · `--font` 覆盖字体路径 · `--out` 输出文件。

脚本只做**确定性拼装**（算布局、缩字号、合成图层），创意判断（色板、隐喻、文案）留给调用方。

## 三条硬约束

- 图像模型 prompt **必须**带：`Absolutely no text, no letters, no words, no numbers, no watermark, no logo`
- 全部中文与数字由 Pillow 叠加，**禁止让模型渲染中文大字**
- 半透明元素画在 RGBA 图层上再 `alpha_composite`；压暗条只用纯色 + alpha mask，**禁止深色→白色双色渐变**

## 核心原则

模型负责画面，脚本负责文字。凡是**画出来**（而非生成出来）的，才稳——封面上一个数字错一位就是硬伤。

## 来源

提纯自 2026-09-22 公众号→小绿书双端物料包实战（`wechat-xiaolushu-material-pack` 跑通后）：把「无字底图 + 精确叠字」这一步单独抽出来独立运行。MIT License。
