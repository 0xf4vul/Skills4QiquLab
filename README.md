# Skills4QiquLab

> 一个面向 AI 工作流的可复用 Skill 实验室：把反复出现的任务沉淀为可执行、可复用、可评测、可迭代的 Skill。

**Skill 方法论 → Case 完整项目 → 模板 → 示例 → Evaluation → 迭代**

## 项目定位

Skills4QiquLab 不做简单的 Prompt 收藏，而是把重复出现的 AI 工作转化为可维护的工程资产。

一个成熟的 Skill 分为两层：

- Core Skill / 方法论：抽象任务的原则、边界、流程与评测方法，位于 skills/
- Skill Case / 完整项目：把某个 Skill 落地成可直接使用、测试和迭代的项目，位于 cases/

因此，skills/ 负责“方法论”，cases/ 负责“工程化落地”。

## 核心工作流

**发现重复任务 → 抽象 Skill → 建立 Case → 添加模板 → 添加示例 → Evaluation → 迭代**

## 快速开始

### 1. 查找方法论

进入 skills.md 查看 Core Skills 索引。

### 2. 直接使用完整 Case

成熟项目位于 cases/。当前第一个完整 Case：

cases/video-prompt-compression/

### 3. 创建新的 Skill

推荐顺序：

**明确问题 → 定义边界 → 编写 Core Skill → 创建 Case → 模板化 → 示例化 → 建立 Evaluation → 实际测试 → 迭代**

## 仓库结构

~~~text
Skills4QiquLab/
├── README.md
├── LICENSE
├── skills.md
│
├── skills/                         # Skill 方法论 / Core Skills
│   ├── prompt-compression.md
│   ├── prompt-optimization.md
│   ├── prompt-reverse-engineering.md
│   ├── video-prompt-compression.md
│   ├── video-prompt-optimization.md
│   ├── web-research.md
│   ├── x-research.md
│   └── skill-builder.md
│
├── templates/                      # 全仓库通用模板
│   └── skill-template.md
│
└── cases/                          # 完整 Skill 项目
    └── video-prompt-compression/
        ├── README.md
        ├── SKILL.md
        ├── templates/
        ├── examples/
        ├── evaluation/
        └── assets/
            └── svg/
~~~

## 设计原则

**方法论与案例分离**：Core Skill 保持抽象，Case 负责具体落地。

**语义优先**：优化目标不是“越短越好”，而是以任务结果和关键约束为先。

**可评测**：成功案例、失败案例、Evaluation 与实际执行结果共同构成 Skill 的质量依据。

**可迭代**：Case 是持续测试与升级的最小工程单元。

## 如何贡献

新增 Skill 时，优先判断它是否具有稳定的输入、输出、边界和可重复流程。满足条件后，先建立 Core Skill，再建立对应 Case。

## 路线图

**V1** Core Skills + Cases → **V2** Skill Registry → **V3** Evaluation / Benchmark → **V4** Web Interface → **V5** Skill Ecosystem

## License

[MIT](LICENSE)
