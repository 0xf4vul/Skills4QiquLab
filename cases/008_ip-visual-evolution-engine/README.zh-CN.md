# Case 008 · 个人 IP 视觉进化引擎（IP Visual Evolution Engine）

**把一个人的身份、能力、价值观与成长故事，转译为一个可持续演化的连续视觉 IP，再压缩成小红书 / 小绿书 3:4 竖版「六镜连续叙事」与可迁移的 X.com Banner。**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

## 它解决什么

多数个人 IP 视觉做法是「一张一张出图」：今天一张头像、明天一张海报、后天一张 Banner，每张都重新写 Prompt、重新设计角色、重新定风格——结果六张图像六个不相关的设计师做的。

本 Engine 把它工程化为一条可复用流水线：先定义一次「视觉 IP DNA」与「连续性契约」，然后让每一张图只是**同一个 IP 状态机的下一次状态转移**，而不是一次新的创作。

**产物**：小红书 / 小绿书 3:4 竖版「六镜」知识卡 × 6（一镜到底的连续镜头）+ 一张可适配 X.com 的 Banner 母版（FRAME 06 适配 1500×500）。

## 流水管道

```
身份 → 视觉 IP DNA → 连续性契约 → 六镜状态机 → 平台适配器 → Banner 适配器 → 视觉质检
```

## 六镜状态机

| 帧 | 阶段 | 状态转移 |
|---|---|---|
| 01 | MASTER（主图） | 建立整个视觉世界 |
| 02 | IDENTITY | 职业 → 能力 → 隐喻 |
| 03 | EVOLUTION | `混沌→流动→系统→静默→存在` |
| 04 | CONTINUITY | 身份 + 动作 + 世界 连续 |
| 05 | ENTROPY / WEIGHT | 熵减，视觉权重重分配 |
| 06 | PRESENCE / BANNER | 最终 Hero，可适配 X 1500×500 |

## 平台适配器（每条线独立自包含）

| 平台 | 连续方式 | 策略 |
|---|---|---|
| Seedream | 多参考 / 连续生成 | 完整 Creative Brief + 参考图顺序生成 |
| GPT | 对话式逐层编辑 | `KEEP EXACTLY` / `CHANGE ONLY` |
| Grok | 连续视觉导演 | 连续分镜叙事 + 显式帧编号 |
| Gemini | 参考图 + 对话 | 上一张作主参考 + 角色命名 + 五维 |

每条适配器文件都可以**单独拿来跑完整个六镜流程**：

- [`references/adapters/seedream.md`](references/adapters/seedream.md)
- [`references/adapters/gpt.md`](references/adapters/gpt.md)
- [`references/adapters/grok.md`](references/adapters/grok.md)
- [`references/adapters/gemini.md`](references/adapters/gemini.md)

## 怎么开始

1. 填 [`templates/fill-in-sheet.md`](templates/fill-in-sheet.md)（或直接用已填示例 [`examples/zhuji-mao/`](examples/zhuji-mao/)）。
2. 选一条平台适配器，按「调用节奏」逐镜生成：MASTER → 次图 01–05。
3. 收尾用 **Banner 适配器**（[`SKILL.md`](SKILL.md) 第 7 节）把 FRAME 06 适配成 X.com 1500×500。
4. 跑 [`evaluation/evaluation-schema.json`](evaluation/evaluation-schema.json)；低于阈值回到失效镜局部修复。

## 文件结构

- `SKILL.md` — Engine 内核：公式、流水线、DNA、连续性契约、六镜状态机、适配器选型、Banner 适配器、质检、评测。
- `references/adapters/*.md` — 四条自包含平台流程。
- `templates/fill-in-sheet.md` — 一次性 DNA 定义（空白模板）。
- `examples/zhuji-mao/` — 已填好的「筑基猫」示例。
- `evaluation/evaluation-schema.json` — 启发式本地评测。

## 核心公式

`IP 视觉演化 = 身份连续性 × 叙事连续性 × 动作连续性 × 视觉熵梯度 × 视觉权重 × 空间连续性 × 气场精炼 × 平台适配`

**换主体，不换 Engine。**
