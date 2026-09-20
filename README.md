# Skills4QiquLab

> 一个面向 AI 工作流的可复用 Skill 实验室：把反复出现的 AI 任务，沉淀成**可执行、可复用、可评测、可迭代**的 Skill。

[![Skills](https://img.shields.io/badge/Skills-8-blue)](#skills-技能) [![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**问题 → Skill → 模板 → 示例 → 评测 → 迭代**

Skills4QiquLab 不只是提示词收藏夹。它关注的是：如何把一次性的「会用 AI」，变成一套可以重复调用、迁移到不同模型、持续优化的工作方法。

---

## 目录

**[Skills 是什么](#skills-是什么) · [Skills 技能](#skills-技能) · [快速开始](#快速开始) · [核心方法](#核心方法) · [视频提示词压缩](#特别关注视频提示词压缩) · [仓库结构](#仓库结构) · [如何贡献](#如何贡献) · [路线图](#路线图) · [License](#license)**

---

<a id="skills-是什么"></a>

## Skills 是什么

这里的 **Skill** 不是一段孤立 Prompt，而是一层可复用的任务执行规范。

一个完整 Skill 通常包含：

**任务边界 → 输入理解 → 执行流程 → 约束条件 → 输出契约 → 评测方式 → 失败案例 → 模型适配**

因此，Skill 的目标不是让 Prompt 看起来更长，而是让 AI 在同一类任务上表现得**更稳定、更可控、更容易复用**。

### Prompt 与 Skill 的区别

| Prompt | Skill |
|---|---|
| 描述一次任务 | 定义一类任务的执行方法 |
| 通常一次性使用 | 可以重复调用 |
| 重点是“怎么说” | 重点是“怎么做” |
| 往往缺少边界 | 明确适用范围与失败边界 |
| 很少有评测机制 | 可以通过案例持续回归测试 |

---

<a id="skills-技能"></a>

## Skills 技能

当前仓库包含 8 个核心 Skill：

| Skill | 解决什么问题 | 入口 |
|---|---|---|
| Prompt Compression | 在不破坏语义约束的情况下压缩 Prompt | [查看](skills/prompt-compression.md) |
| Prompt Optimization | 在保持原始意图的前提下优化 Prompt | [查看](skills/prompt-optimization.md) |
| Prompt Reverse Engineering | 从优秀 Prompt 中反向提取可复用结构 | [查看](skills/prompt-reverse-engineering.md) |
| Video Prompt Compression | 压缩视频 Prompt，同时保留动作、时间与镜头语义 | [查看](skills/video-prompt-compression.md) |
| Video Prompt Optimization | 优化视频 Prompt 的动作、镜头与执行清晰度 | [查看](skills/video-prompt-optimization.md) |
| Web Research | 将开放式搜索转化为结构化证据研究流程 | [查看](skills/web-research.md) |
| X Research | 对 X 账号、人物、主题进行检索、核验与分析 | [查看](skills/x-research.md) |
| Skill Builder | 从重复工作中设计、测试和迭代新的 Skill | [查看](skills/skill-builder.md) |

### 推荐使用顺序

**刚开始使用 → Prompt Compression → Prompt Optimization → Prompt Reverse Engineering**

**主要做 AI 视频 → Video Prompt Compression → Video Prompt Optimization**

**主要做信息搜集 → Web Research → X Research**

**想自己构建 Skill → Skill Builder → Examples → Evaluation → Iteration**

---

<a id="快速开始"></a>

## 快速开始

### 1. 选择 Skill

先判断任务属于哪一类，而不是直接修改 Prompt。

**“这个 Prompt 太长了，但不能改变动作和镜头。” → Video Prompt Compression**

**“这个 Prompt 效果不稳定，但原始意图不能改变。” → Prompt Optimization**

**“我想研究一个 X 账号近 30 天到底发了什么。” → X Research**

### 2. 阅读 Skill

每个 Skill 都尽量回答：

**解决什么问题？ → 什么时候使用？ → 怎么执行？ → 什么不能改变？ → 什么时候不要用？ → 如何评测？**

### 3. 执行

**选择 Skill → 填写输入 → 执行 → 检查约束 → 对照失败案例 → 反向评测 → 迭代**

---

<a id="核心方法"></a>

## 核心方法

### 1. 语义优先，而不是字数优先

压缩的目标不是“越短越好”，而是：

**更少的冗余 + 更高的信息密度 + 不损失关键语义**

尤其涉及动作、时间顺序、因果关系、空间关系、镜头连续性的任务，不能为了缩短文本而删除决定结果的语义。

### 2. 把隐性经验显式化

**经验 → 规则 → 流程 → 模板 → 案例 → 失败模式 → 评测**

这样别人才能真正“抄作业”，而不是只能复制一句 Prompt。

### 3. 模型适配与核心逻辑分离

尽可能保持：

**稳定任务逻辑 + 独立模型适配层**

让同一 Skill 能迁移到不同模型，而不需要每次重新设计。

### 4. 失败案例和成功案例同样重要

一个 Skill 不应该只告诉你“应该怎么做”，还应该告诉你：

**哪些不能压缩 / 哪些容易歧义 / 哪些情况下会误解 / 什么属于过度优化 / 什么任务根本不适合**

---

<a id="特别关注视频提示词压缩"></a>

## 特别关注：视频提示词压缩

视频 Prompt 与图片 Prompt 最大的区别之一，是**时间维度**。

例如：

**reach → grip → lift → pause → drink**

如果直接压成：

**drink**

文字虽然大幅减少，但动作语义、因果关系和过程表达也一起消失了。

因此，本项目采用一个核心原则：

> **Compression is not deletion. It is semantic re-encoding.**

即：

**压缩表达方式，而不是删除视频本身需要表达的语义。**

### 优先保护的语义

**时间关系 > 动作因果 > 主体身份 > 镜头逻辑 > 空间构图 > 外观细节 > 装饰性形容词**

默认压缩等级为保守的 **L1**，只有在明确允许的情况下才进一步压缩。

### 视频压缩还需要考虑

**主体连续性 / 动作连续性 / 时间顺序 / 镜头运动 / 因果关系 / 场景一致性 / 音频提示 / 转场逻辑**

这也是本仓库与单纯“删 Prompt 字数”工具的核心区别。

---

<a id="仓库结构"></a>

## 仓库结构

```text
Skills4QiquLab/
├── README.md
├── skills.md
├── templates.md
├── LICENSE
├── skills/
│   ├── prompt-compression.md
│   ├── prompt-optimization.md
│   ├── prompt-reverse-engineering.md
│   ├── video-prompt-compression.md
│   ├── video-prompt-optimization.md
│   ├── web-research.md
│   ├── x-research.md
│   └── skill-builder.md
└── examples/
    └── README.md
```

**想直接用 → `skills/` · 想自己写 Skill → `templates.md` + `skills/skill-builder.md` · 想研究评测 → `examples/` · 想了解整体设计 → `skills.md`**

---

## 一个 Skill 的最小结构

推荐至少包含：

```text
# Skill Name

## Mission
解决什么问题？

## When to use
什么时候使用？

## When not to use
什么时候不要使用？

## Workflow
具体执行步骤。

## Constraints
哪些信息必须保留？

## Output
最终应该输出什么？

## Evaluation
如何判断结果合格？

## Failure cases
哪些情况下容易失败？
```

目标是让 Skill 从“经验总结”变成可以持续维护的工程资产。

---

<a id="如何贡献"></a>

## 如何贡献

欢迎提交新的 Skill、案例、失败模式和评测方法。

推荐流程：

**发现重复任务 → 抽象任务边界 → 编写 Skill → 添加模板 → 添加正反案例 → 建立评测 → 实际使用 → 迭代版本**

提交新 Skill 时，优先确认：

**真实重复问题 · 明确适用边界 · 不可破坏语义 · 可复制模板 · 正反案例 · 可执行评测 · 模型差异**

---

<a id="路线图"></a>

## 路线图

**V1 Skill Collection** → 核心 Skill 集合

**V2 Skill Registry** → Skill 元数据、分类、检索与路由

**V3 Evaluation / Benchmark** → 标准测试集、回归测试与评测机制

**V4 Web Interface** → 可视化选择、执行与评测

**V5 Skill Ecosystem** → Skill 分享、组合、版本化与生态协作

---

## 致谢与参考

本项目的文档组织方式参考了开源社区中的优秀 Prompt 模板项目，包括 [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)。

这里借鉴的是**“分类 → 模板 → 示例 → 避坑 / 约束 → 可直接使用”**的知识组织思路，而不是复制其具体内容。

---

<a id="license"></a>

## License

[MIT](LICENSE)
