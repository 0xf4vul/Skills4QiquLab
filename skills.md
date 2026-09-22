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
| Pencil Sketch Art | 把主题或抽象概念转为石墨铅笔素描手绘插画 | [skills/pencil-sketch-art.md](skills/pencil-sketch-art.md) |
| Golden Quote Miner | 把长内容提炼为可脱离原文独立传播的金句 | [skills/golden-quote-miner.md](skills/golden-quote-miner.md) |
| Skill Builder | 把重复工作抽象为可测试、可迭代的 Skill | [skills/skill-builder.md](skills/skill-builder.md) |
| Textless Backdrop | 生成无字底图，再用 Pillow 精确叠加中文与大字 | [skills/imagegen-textless-composite.md](skills/imagegen-textless-composite.md) |

## Skill Cases

| 编号 | Case | 状态 | 入口 |
|---:|---|---|---|
| 001 | Video Prompt Compression | Active | [001_video-prompt-compression/](cases/001_video-prompt-compression/) |
| 002 | Source-to-KOL Research | Active | [002_source-to-kol-research/](cases/002_source-to-kol-research/) |
| 004 | Pencil Sketch Art | Active | [004_pencil-sketch-art/](cases/004_pencil-sketch-art/) |
| 005 | Golden Quote Miner | Active | [005_golden-quote-miner/](cases/005_golden-quote-miner/) |
| 006 | Textless Backdrop | Active | [006_imagegen-textless-composite/](cases/006_imagegen-textless-composite/) |

## Case 命名规则

所有 Case 目录统一采用：

~~~text
cases/
└── NNN_skill-name/
    ├── README.md
    ├── SKILL.md
    ├── templates/
    ├── examples/
    ├── evaluation/
    └── assets/
        └── svg/
            └── case-logo.svg
~~~

其中 NNN 为三位顺序编号，从 001 开始，按 Case 首次建立的顺序递增；名称主体使用稳定的 kebab-case。**今后新增 Case 自动使用下一个编号。**

## Case 标识规则

每个 Case 必须提供一个**独立的 Case Logo**，用于表达该 Case 的核心主题；Case Logo 不得使用根仓库 Logo 替代。

## Case 标准结构

一个 Case 应当能够独立完成：**理解 → 执行 → 示例 → 评测 → 迭代**。

## 如何选择

**理解方法 → skills/；直接使用完整 Skill → cases/；创建新的 Skill → skills/skill-builder.md + templates/skill-template.md。**