# Changelog · pencil-sketch-art

## 1.2.0 — 2026-09-22

### 修正
- `scripts/crop.py` 移除 numpy 依赖：改用 Pillow `Image.resize(..., Image.BOX)` 求逐行/逐列平均墨量，等价 numpy 的 `mean(axis)` 但只需 Pillow 一个包
- 墨量极性自动判定：用整图亮度中位数判断亮底/暗底，深底图（如深蓝海报）不会被判成「整幅全是主体」
- 新增 `scripts/selftest.py`（环境/裁切 14 项断言）与 `requirements.txt`（pillow>=9.0）
- `_meta.json` 运行依赖移除 numpy，仅留 pillow

## 1.0.0 — 2026-09-22

### 新增
- 从 `infographic-maker` 的手绘风格层提纯为独立技能，剥离排版/构图/分栏等所有信息图约束
- SKILL.md：六秒决策法（主体/画幅/笔触）+ 6 种笔触预设 + 五段式 prompt 模板 + 8 条出图自检 + 返工修法表
- `references/prompt-library.md`：6 套可复制的完整 prompt、通用负面词块、画幅速查、5 组概念转译示例
- `references/style-tokens.md`：9 个 token 桶速查
- `references/troubleshooting.md`：14 种翻车现象对照表 + 4 条迭代原则
- `scripts/build_prompt.py` + `scripts/presets.json`：prompt 构造器 CLI，支持数字/key/中文名三种预设写法、画幅/点缀色/光源组合、图内文字长度硬校验
- `examples/`：概念隐喻、观点文配图、场景速写三个完整案例
- README / CHANGELOG / LICENSE(MIT) / _meta.json 工程元信息齐备

## 1.1.0 — 2026-09-22

### 新增
- `scripts/crop.py`：按目标比例智能裁切。用**逐行墨量**定位主体（背景取中位数作基准，纸纹不会被误判成墨迹），
  支持 `--ratio` 目标比例、`--bottom-safe` / `--top-safe` 两端标题安全区、`--width` 输出宽度、`--dry-run` 打印墨量剖面。
  解决的核心问题：**在无法读图的会话里也能安全裁图**，不必凭 prompt 猜构图。
  剖面还能反过来用：找「干净带」决定标题叠加在百分之几的高度（实测主图顶部只有 125px 空白，
  靠剖面发现干净带其实在 19%–41%，标题因此下移，没压到主体）。
- `examples/04-quote-card-series.md`：成套金句卡配图工作流（意象设计口诀 / 批量构造 prompt / 卡片内嵌 CSS 要点）

### 修正
- 执行流程补入「裁切成发布尺寸」步骤与常用平台比例表（公众号封面 2.35、正文 ≤1080 宽、小红书 3:4、视频号 9:16、金句卡 2:3）
- 记录两条实测坑：预设 key 是 `hatched-tonal` 不是 `hatched`（写错时 stdout 全空、提示只在 stderr，批量脚本必须查 `returncode`）；
  卡片内嵌底图必须加 `mask-image:radial-gradient(...)`，否则纸色底图边缘会露出一圈方框
