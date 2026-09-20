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
    └── 001_video-prompt-compression/
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

## Case 命名规则

`cases/` 下的所有 Case **必须按 Skill 建立顺序使用三位数字前缀**：

**001_video-prompt-compression → 002_xxx → 003_xxx → …**

数字代表 Case 的创建顺序；名称主体保持简洁、稳定、可读。今后新增 Case 自动沿用该规则，不再创建无序或无编号目录。

## 两层架构

**skills/** 只负责可迁移的 Core Skill 方法论；**cases/** 负责将一个成熟 Skill 完整落地为可使用、可测试、可评测、可迭代的项目。

Case 目录使用顺序编号，使 Skill 的演进顺序、项目索引与长期维护路径保持一致。Case 内的模板、示例、评测和视觉资产保持自包含。

## 使用方式

查找方法论 → `skills.md` → 进入对应 Core Skill。

直接使用完整项目 → `cases/` → 按编号找到 Case → 阅读对应 Case 的 `README.md` / `SKILL.md`。

创建新的 Skill → `skills/skill-builder.md` + `templates/skill-template.md` → 按下一个顺序编号建立新的 Case。

## 设计原则

- **方法论与案例分离**：Core Skill 保持抽象，Case 负责具体落地。
- **Case 顺序稳定**：Case 目录统一采用 `NNN_skill-name`，编号只表示建立顺序，不承担语义分类。
- **语义与结果优先**：不要为了形式上的压缩或简化破坏任务本身的关键约束。
- **可评测**：通过示例、失败案例和 Evaluation 验证 Skill，而不是只看文档是否完整。
- **可迭代**：Case 是持续测试和升级的最小工程单元。

## 路线图

**V1** Core Skills + Cases → **V2** Skill Registry → **V3** Evaluation / Benchmark → **V4** Web Interface → **V5** Skill Ecosystem

## License

[MIT](LICENSE)
