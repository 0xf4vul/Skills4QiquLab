# Skills4QiquLab

> 一个面向 AI 工作流的可复用 Skill 实验室：将重复任务沉淀为可执行、可复用、可评测、可迭代的工程资产。

**Core Skill → Case → Template → Example → Evaluation → Iteration**

## 项目结构

```text
Skills4QiquLab/
├── README.md
├── LICENSE
├── skills.md
│
├── skills/                         # Core Skills：通用方法论
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
└── cases/                          # 完整、可独立维护的 Skill Case
    └── video-prompt-compression/
        ├── README.md
        ├── SKILL.md
        ├── templates/
        │   ├── skill-template.md
        │   └── video-prompt-template.md
        ├── examples/
        │   ├── basic.md
        │   ├── continuous-action.md
        │   └── failure-cases.md
        ├── evaluation/
        │   ├── evaluation-rubric.md
        │   └── reverse-expansion.md
        └── assets/
            └── svg/
                ├── video-prompt-compression.svg
                └── template.svg
```

## 两层架构

**skills/** 只负责可迁移的 Core Skill 方法论；**cases/** 负责将一个成熟 Skill 完整落地为可使用、可测试、可评测、可迭代的项目。

因此，通用规则不与具体案例混在一起；Case 内的模板、示例、评测和视觉资产也保持自包含。

## 使用方式

查找方法论 → `skills.md` → 进入对应 Core Skill。

直接使用完整项目 → `cases/` → 阅读 Case 的 `README.md` / `SKILL.md`。

创建新的 Skill → `skills/skill-builder.md` + `templates/skill-template.md` → 建立新的 Case。

## 设计原则

- **方法论与案例分离**：Core Skill 保持抽象，Case 负责具体落地。
- **语义与结果优先**：不要为了形式上的压缩或简化破坏任务本身的关键约束。
- **可评测**：通过示例、失败案例和 Evaluation 验证 Skill，而不是只看文档是否完整。
- **可迭代**：Case 是持续测试和升级的最小工程单元。

## 路线图

**V1** Core Skills + Cases → **V2** Skill Registry → **V3** Evaluation / Benchmark → **V4** Web Interface → **V5** Skill Ecosystem

## License

[MIT](LICENSE)
