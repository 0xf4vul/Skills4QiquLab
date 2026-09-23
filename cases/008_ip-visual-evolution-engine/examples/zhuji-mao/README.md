# Example · 筑基猫（Zhuji Mao）

本文件是 Case 008 的**已填好默认值**示例，来自「用 AI 搞钱、真交付的实战派」橘猫 IP。
把它当作变量表，换 IP 时只改这一列即可。完整逐平台提示词见 `../../references/adapters/`。

## FILL-IN SHEET（筑基猫默认值）

| 变量 | 含义 | 筑基猫默认值 | 英文锚点 |
|---|---|---|---|
| SUBJECT | 主体 | 橘猫 + 圆眼镜 | `an orange tabby cat wearing round glasses` |
| IDENTITY | 身份 | 用 AI 搞钱、真交付的实战派 | `an AI practitioner who actually ships and monetizes` |
| CORE ABILITY | 核心能力 | 把散落的 AI 工具收敛成一条能跑通的链路 | `turning / collapsing scattered AI tools into one pipeline that actually runs` |
| VISUAL METAPHOR | 视觉隐喻 | 道场 × 工作台 | `a quiet dojo crossed with a modern workspace` |
| CORE MESSAGE | 核心信息 | 「101 个工具在手，不如跑通一条链路。」 | `"101 个工具在手，不如跑通一条链路。"` |
| VISUAL WORLD | 视觉世界 | 克制的当代工作室 + 东方修行感 | `restrained contemporary studio with Eastern cultivation atmosphere` |
| PALETTE | 核心色彩 | 冷蓝灰 → 暖光 → 象牙白 + 柔金 | `cool blue-grey → warm key light → ivory + soft gold` |
| ASPECT | 比例 | 3:4 竖版 | `3:4 vertical` |

### 六镜标题

| 帧 | 阶段 | 标题 |
|---|---|---|
| FRAME 01 / IMAGE 01 | MASTER | 筑基猫｜一条链路 |
| FRAME 02 / IMAGE 02 | IDENTITY | 我是怎么被定义的 |
| FRAME 03 / IMAGE 03 | EVOLUTION | 我是怎么练成的 |
| FRAME 04 / IMAGE 04 | CONTINUITY | 为什么我还是我 |
| FRAME 05 / IMAGE 05 | ENTROPY / WEIGHT | 越空，越强 |
| FRAME 06 / IMAGE 06 | PRESENCE / BANNER | 101 个工具在手，不如跑通一条链路。 |

## 怎么用

1. 选定平台适配器：`grok.md` / `gemini.md` / `seedream.md` / `gpt.md`。
2. 把上面这套默认值替换进该适配器的 `FILL-IN SHEET`（或保留筑基猫直接跑）。
3. 按适配器里的「调用节奏」逐帧生成：MASTER → 次图 01–05。
4. 最后用 `../../SKILL.md` 的 **Banner Adapter** 把 FRAME 06 适配成 X.com 1500×500。

> 四条平台线共享同一套 `Visual IP DNA` 与 `Continuity Contract`，区别只在「怎么驱动模型」：
> Seedream = 完整 Brief + 参考图顺序生成；GPT = 单会话 KEEP/CHANGE ONLY；
> Grok = 连续视觉导演 + 帧编号；Gemini = 上一张作主参考 + 角色命名 + 五维。
