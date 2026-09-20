# Skills Index

本页是仓库的快速入口，区分 Core Skills（方法论）与 Skill Cases（完整项目）。

## Core Skills

| Skill | 用途 | 入口 |
|---|---|---|
| Prompt Compression | 压缩 Prompt，同时保持关键语义约束 | [skills/prompt-compression.md](skills/prompt-compression.md) |
| Prompt Optimization | 优化 Prompt 的结构、清晰度与执行稳定性 | [skills/prompt-optimization.md](skills/prompt-optimization.md) |
| Prompt Reverse Engineering | 从优秀 Prompt 中提取可复用结构 | [skills/prompt-reverse-engineering.md](skills/prompt-reverse-engineering.md) |
| Video Prompt Compression | 压缩视频 Prompt，同时保护动作、时间与镜头语义 | [skills/video-prompt-compression.md](skills/video-prompt-compression.md) |
| Video Prompt Optimization | 优化视频 Prompt 的动作、镜头与执行清晰度 | [skills/video-prompt-optimization.md](skills/video-prompt-optimization.md) |
| Web Research | 将开放式搜索转化为结构化证据研究 | [skills/web-research.md](skills/web-research.md) |
| X Research | 对 X 账号、人物、主题进行检索、核验与分析 | [skills/x-research.md](skills/x-research.md) |
| Skill Builder | 把重复工作抽象为可测试、可迭代的 Skill | [skills/skill-builder.md](skills/skill-builder.md) |

## Skill Cases

| Case | 状态 | 入口 |
|---|---|---|
| Video Prompt Compression | Active | [cases/video-prompt-compression/](cases/video-prompt-compression/) |

## 如何选择

**理解方法 → `skills/`；直接使用完整 Skill → `cases/`；创建新的 Skill → `skills/skill-builder.md` + `templates/skill-template.md`。**

## Case 标准结构

```text
Case/
├── README.md
├── SKILL.md
├── templates/
├── examples/
├── evaluation/
└── assets/
```

一个 Case 应当能够独立完成：**理解 → 执行 → 示例 → 评测 → 迭代**。
