<div align="center">

<img src="assets/qiqulab-logo.png" alt="Qiqu.Lab — 奇趣实验室" width="760">

# Skills4QiquLab

**一个面向实践的 AI Skill 仓库，将有效的 AI 工作方法整理为可复用的 Skill 与配套资源。**

<p>
  <img src="https://img.shields.io/github/stars/0xf4vul/Skills4QiquLab?style=flat-square&label=Stars">
  <img src="https://img.shields.io/github/forks/0xf4vul/Skills4QiquLab?style=flat-square&label=Forks">
  <img src="https://img.shields.io/badge/Skills-8-4c9aff?style=flat-square">
  <img src="https://img.shields.io/badge/Cases-2-7c5cff?style=flat-square">
  <img src="https://img.shields.io/github/license/0xf4vul/Skills4QiquLab?style=flat-square&label=License">
</p>

[English](README.md) · **简体中文** · [繁體中文](README.zh-TW.md)

</div>

## 交流群

目前未公开独立交流群。讨论、反馈与需求可通过 [Issues](https://github.com/0xf4vul/Skills4QiquLab/issues) 进行；贡献代码、文档或 Skill 请使用 [Pull Requests](https://github.com/0xf4vul/Skills4QiquLab/pulls)。

## 新增 Skill

- [Video Prompt Compression](skills/video-prompt-compression.md) — 压缩视频 Prompt，同时保护动作顺序、时间关系、镜头行为与主体连续性。
- [Video Prompt Optimization](skills/video-prompt-optimization.md) — 优化视频 Prompt 的动作、时间、镜头与主体连续性。
- [X Research](skills/x-research.md) — 以可复现、基于证据的方式研究 X 账号与信息源。

## 精选项目

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="cases/001_video-prompt-compression/"><img src="cases/001_video-prompt-compression/assets/svg/case-logo.svg" alt="Video Prompt Compression" width="88%"></a>
<br><strong>Video Prompt Compression</strong><br>
压缩视频 Prompt，同时保留有意义的动作链、时间关系、镜头逻辑与主体连续性。
<br><a href="cases/001_video-prompt-compression/">Case</a> · <a href="skills/video-prompt-compression.md">Skill</a>
</td>
<td width="50%" valign="top" align="center">
<a href="cases/002_source-to-kol-research/"><img src="cases/002_source-to-kol-research/assets/svg/case-logo.svg" alt="Source-to-KOL Research" width="88%"></a>
<br><strong>Source-to-KOL Research</strong><br>
将任意输入转化为可验证、可审计的 KOL / 信息源研究流程。
<br><a href="cases/002_source-to-kol-research/">Case</a> · <a href="skills/x-research.md">Skill</a>
</td>
</tr>
</table>

## Skill 入口

| | Skill | 作用 |
|---|---|---|
| 🧩 | [Prompt Compression](skills/prompt-compression.md) | 减少 Prompt 冗余，同时保留意图与硬约束 |
| ✨ | [Prompt Optimization](skills/prompt-optimization.md) | 提升清晰度、结构与执行稳定性 |
| 🔬 | [Prompt Reverse Engineering](skills/prompt-reverse-engineering.md) | 从优秀 Prompt 中提取可复用的决策结构 |
| 🎬 | [Video Prompt Compression](skills/video-prompt-compression.md) | 压缩视频 Prompt，同时保护时间语义 |
| 🎥 | [Video Prompt Optimization](skills/video-prompt-optimization.md) | 优化动作、时间、镜头与主体连续性 |
| 🌐 | [Web Research](skills/web-research.md) | 将开放问题转化为可追溯、可交叉验证的证据 |
| 𝕏 | [X Research](skills/x-research.md) | 研究 X 账号、人物、帖子与近期活动 |
| 🛠️ | [Skill Builder](skills/skill-builder.md) | 将重复工作沉淀为可复用、可测试的 Skill |

→ [完整 Skill 索引](skills.md)

## 库用法

仓库分为两层：**Core Skills** 提供可复用的方法论；**Skill Cases** 将方法论组织成完整、可执行的实战案例。

**选择 Skill → 打开对应 Skill 文件 → 按 Workflow 执行 → 使用模板 / 示例 → 运行 Evaluation → 修改复用。**

每个 Skill 都应具备统一的实用契约：

| Skill | Purpose | Workflow | Evaluation |
|---|---|---|---|
| Prompt Compression | 在删除冗余的同时保留意图 | 提取目标 → 约束 → 冗余 → 合并 → 验证 | 意图 / 约束 / 关系 / 清晰度 / 压缩率 |
| Prompt Optimization | 不改变意图的前提下提升执行效果 | 意图 → 约束 → 歧义 → 重构 → 验证 | 保真 / 覆盖 / 歧义 / 稳定性 |
| Prompt Reverse Engineering | 将优秀 Prompt 转化为可复用结构 | 观察 → 变量 → 结构 → 模板 → 测试 | 可迁移性 / 可控性 / 清晰度 |
| Video Prompt Compression | 缩短视频 Prompt，同时保护运动语义 | 解析 → 语义单元 → 分类 → 合并 → 验证 | 语义 / 时间连贯 / 动作连续 |
| Video Prompt Optimization | 让视频动作与镜头指令更容易执行 | 意图 → 主体 → 动作 → 时间 → 镜头 → 约束 | 动作 / 时间 / 镜头 / 一致性 |
| Web Research | 从开放问题生成可追溯答案 | 范围 → 搜索 → 筛选 → 交叉验证 → 综合 → 引用 | 相关性 / 来源质量 / 新鲜度 / 引用 |
| X Research | 按明确标准核验并分析 X 活动 | 发现 → 核验 → 检查 → 筛选 → 比较 | 身份 / 时效 / 证据 / 一致性 |
| Skill Builder | 将重复工作沉淀为可维护 Skill | 触发 → 边界 → Workflow → 输出契约 → 测试 → 迭代 | 一致性 / 可迁移 / 可检查 |

需要完整实战流程时进入 [cases/](cases/)；需要创建新 Skill 时，从 [Skill Builder](skills/skill-builder.md) 与 [templates/skill-template.md](templates/skill-template.md) 开始。

## 声明

本仓库用于学习、实验与可复用的 AI 工作流实践。示例及第三方引用仍受其原始来源、许可证与平台规则约束；用于商业场景前请自行核验相关权利与使用条款。

## Star 趋势

[![Star History](https://api.star-history.com/svg?repos=0xf4vul/Skills4QiquLab&type=Date)](https://star-history.com/#0xf4vul/Skills4QiquLab&Date)

## 开源协议

[MIT License](LICENSE)
