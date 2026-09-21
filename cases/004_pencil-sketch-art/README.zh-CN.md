<div align="center">

<img src="assets/svg/case-logo.svg" alt="004 — 铅笔素描手绘图" width="620">

# 004 — 铅笔素描手绘图

</div>

> 其他语言：[English](README.md) · [繁體中文](README.zh-TW.md)

把任意主题、文字描述或抽象概念，生成一张**石墨铅笔素描手绘风**插画。单图交付，不依赖任何信息图或排版流程。

## 项目亮点

- **抽象概念先转译，再落笔**。「内卷」画不出来，但「一个人在跑步机上原地跑，跑步机插着一面狂转的钟」画得出来。`references/prompt-library.md` 里给了五组现成转译。
- **六种笔触预设**：纯线稿 / 排线明暗 / 炭笔粗粝 / 淡彩素描 / 场景透视 / 概念隐喻。
- **两个可跑的脚本**：`build_prompt.py` 拼装 prompt，并硬拦图内文字超 8 字；`crop.py` 用逐行墨量定位主体，**看不到图也能安全裁切**——封面临时改比例不用重跑生图。
- **文字绝不进 prompt**。底图一律生成为无字图，文案在排版环节叠加。图内烧字是毁掉一张好素描最常见的方式。
- **背景必须是纸色，不能纯白**。米白纸纹是区分「素描」和「数字绘画」最快的信号。

## 项目结构和说明

| 路径 | 说明 |
|---|---|
| `SKILL.md` | 完整方法：主体决策、画幅规则、笔触预设、prompt 组装、8 条自检清单 |
| `scripts/build_prompt.py` | prompt 构造器，`--list` 查预设，校验文字长度 / 画幅 / 点缀色 / 光源 |
| `scripts/crop.py` | 墨量裁切器，支持 `--ratio` `--top-safe` `--bottom-safe` `--dry-run` |
| `scripts/presets.json` | 预设数据：笔触 / 媒介 / 明暗 / 构图 / 负面词。改数据不改代码 |
| `references/prompt-library.md` | 概念转译表 + 分主体 prompt 范式 |
| `references/style-tokens.md` | 9 个 token 桶：媒介 / 笔触 / 光影 / 纸 / 色 / 质量 / 负面 / 画幅 / 参数 |
| `references/troubleshooting.md` | 16 种翻车现象 → 根因 → 改法 |
| `examples/` | 四个完整案例，含八张成套金句卡 |
| `templates/` | 需求采集模板 |
| `assets/gallery/` | 已发布成品 |

## 库用法

**定主体 → 选画幅 → 选笔触 → 构造 prompt → 出图 → 裁切 → 自检**

```bash
python scripts/build_prompt.py --list
python scripts/build_prompt.py -s "a paper boat drifting on a sea of folded resumes" -p 3 -a portrait
python scripts/crop.py --in raw.png --ratio 2.35 --bottom-safe 0.26 --width 900 --out cover.png
```

参数速记：`-s` 主体 / `-p` 笔触（1-6 或 key 或中文名）/ `-a` 画幅 / `--accent` 点缀色 / `--light` 光源 / `-t` 图内文字（≤8 字）/ `-o` 输出文件。

脚本只做**确定性拼装**（拼 token、算 size、校验长度），创意判断留给调用方。

## 三条硬约束

- 图内文字 **≤ 8 字**，大段文字一律走无字底图 + 排版叠加
- 色彩 **≤ 1 个低饱和色相**，背景必须纸色，**禁用纯白**
- 生成参数固定 `quality=high`、`style=natural`（vivid 会毁掉石墨质感）

## 发布比例

公众号封面 **2.35**（900×383）· 正文图 **宽 ≤1080** · 小红书 **3:4** · 视频号 **9:16** · 金句卡 **2:3**

## 核心原则

做减法，不做加法。画面里**少了什么**，往往才是意思所在——算盘要扣下，水表要缺席，台灯要关掉。

## 来源

提纯自 `infographic-maker`：剥掉信息图的排版与构图约束，把手绘风格层单独抽出来独立运行。原技能未改动。MIT License。
