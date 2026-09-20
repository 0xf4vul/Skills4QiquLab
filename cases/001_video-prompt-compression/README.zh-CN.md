<div align="center">

<img src="assets/svg/case-logo.svg" alt="001 — Video Prompt Compression" width="620">

# 001 — Video Prompt Compression

</div>

> 其他语言：[English](README.md) · [繁體中文](README.zh-TW.md)

将视频提示词压缩得更短、更高密度，同时保留生成结果真正依赖的动作、时间、镜头与连续性信息。

## 项目亮点

- **语义保真压缩**：减少冗余，但不把多个有意义的动作粗暴合并。
- **时间关系保护**：保留动作顺序、持续时间、停顿、转场与因果关系。
- **镜头逻辑保护**：把镜头运动、景别变化与连续性作为硬约束处理。
- **反向展开评测**：将压缩结果重新展开，检查关键源语义是否仍可恢复。
- **失败案例驱动**：覆盖 Verb Collapse、Time Deletion、False Continuity 等典型失败模式。

## 项目结构和说明

| 路径 | 说明 |
|---|---|
| `SKILL.md` | 核心压缩方法、边界、Workflow、输出契约与失败模式 |
| `templates/` | 可复用的 Skill 模板与视频 Prompt 模板 |
| `examples/` | 基础案例、连续动作案例与失败案例 |
| `evaluation/` | 评测标准与反向展开检查 |
| `assets/svg/` | 项目 Logo 与可复用 SVG 资源 |

## 库用法

**阅读 SKILL.md → 选择模板 → 参考案例 → 执行压缩 → 运行评测 → 复用**

完整方法见 [SKILL.md](SKILL.md)；评测入口见 [evaluation/](evaluation/)；快速开始见 [templates/](templates/)。

## 边界

不能为了追求更短而删除动作语义、时间关系、镜头行为、因果依赖或连续性约束。