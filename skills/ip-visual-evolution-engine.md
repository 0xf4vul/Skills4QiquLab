# IP Visual Evolution Engine｜个人 IP 视觉进化引擎

**把一个人的身份、能力、价值观与成长故事，转译为一个可持续演化的连续视觉 IP，再压缩成小红书 / 小绿书 3:4 竖版「六镜连续叙事」与可迁移的 X.com Banner。**

- **Case 008**：[cases/008_ip-visual-evolution-engine/](https://github.com/0xf4vul/Skills4QiquLab/tree/main/cases/008_ip-visual-evolution-engine)
- **类型**：image / ip-design / continuity
- **平台**：Seedream · GPT · Grok · Gemini（四条独立自包含适配器）

## Why this Skill exists

个人 IP 视觉的常见做法是「一张一张出图」：每张都重新写 Prompt、重新设计角色、重新定风格，结果六张图像六个不相关的设计师做的。本 Skill 把这件事工程化为一条**可复用的流水线**：先定义一次「视觉 IP DNA」+「连续性契约」，然后让每一张图只是**同一个 IP 状态机的下一次状态转移**。

## Pipeline（流水管道）

```
Identity → Visual IP DNA → Continuity Contract → 六镜状态机
        → Platform Adapter → Banner Adapter → Vision QC
```

## Six-Frame State Machine（六镜状态机）

| 帧 | 阶段 | 状态转移 |
|---|---|---|
| 01 | MASTER | 建立整个视觉世界 |
| 02 | IDENTITY | 职业 → 能力 → 隐喻 |
| 03 | EVOLUTION | `CHAOS→FLOW→SYSTEM→SILENCE→PRESENCE` |
| 04 | CONTINUITY | 身份 + 动作 + 世界 连续 |
| 05 | ENTROPY / WEIGHT | 熵减，视觉权重重分配 |
| 06 | PRESENCE / BANNER | 最终 Hero，可适配 X 1500×500 |

## Platform Adapters（每条线独立自包含）

| 平台 | 连续方式 | 策略 |
|---|---|---|
| Seedream | 多参考 / 连续生成 | 完整 Brief + 参考图顺序生成 |
| GPT | 对话式逐层编辑 | `KEEP EXACTLY` / `CHANGE ONLY` |
| Grok | 连续视觉导演 | Frame-to-Frame + 显式帧编号 |
| Gemini | 参考图 + 对话 | 上一张作主参考 + 角色命名 + 五维 |

## Workflow

1. 填 `Visual IP DNA`（主体 / 身份 / 能力 / 隐喻 / 世界 / 核心信息 / 调色板）。
2. 选平台适配器，按「调用节奏」逐镜生成：MASTER → 次图 01–05。
3. 收尾用 Banner Adapter 把 FRAME 06 适配成 X.com 1500×500。
4. 跑 Evaluation，低于阈值回到失效镜局部修复。

## Output contract

- 小红书 / 小绿书 3:4 竖版连续叙事卡 × 6（同一角色、同一世界、逐级收敛）。
- 一张满足 1500×500 安全区的 Banner 母版（FRAME 06 适配）。

## Failure modes

- 六镜变成六张不同风格海报 → 每镜带 Continuity Contract / 以上一镜为锚。
- 分镜感 / 硬竖线 / 编号 → 把演化写成并列列表；补 `no panels, no numbered captions`。
- 角色漂移 → 参考图未上传 / 角色未命名；补参考图 + 固定角色名（Gemini）。
- 最后一张过曝 → 强调 `do not make it brighter, make it purer`。
- 3:4 被裁成方图 → 首行固定 `3:4 vertical`。

## Evaluation

身份连续 · 叙事连续 · 熵梯度 · 平台适配 · Banner 就绪（见 Case 008 `evaluation/evaluation-schema.json`，阈值 80）。

## References

- 完整 Engine、六镜逐帧提示词、SOP 与负向词：[Case 008](https://github.com/0xf4vul/Skills4QiquLab/tree/main/cases/008_ip-visual-evolution-engine)
- 平台适配器：`seedream.md` · `gpt.md` · `grok.md` · `gemini.md`（各文件可独立跑完整流程）
- 已填示例：[examples/zhuji-mao/](https://github.com/0xf4vul/Skills4QiquLab/tree/main/cases/008_ip-visual-evolution-engine/examples/zhuji-mao)
