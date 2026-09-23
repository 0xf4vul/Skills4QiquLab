# IP Visual Evolution Engine｜个人 IP 视觉进化引擎

> **Case 008** · 把一个人的身份、能力、价值观与成长故事，转译为一个**可持续演化的连续视觉 IP**，再压缩成小红书 / 小绿书 3:4 竖版「六镜连续叙事」与可迁移的 X.com Banner。
> **流水线（Pipeline）**：`Identity → Visual IP DNA → Continuity Contract → 六镜状态机 → 平台适配器 → Banner Adapter → Vision QC`。
> **四条平台线各自独立成文件**：[`references/adapters/grok.md`](references/adapters/grok.md) · [`gemini.md`](references/adapters/gemini.md) · [`seedream.md`](references/adapters/seedream.md) · [`gpt.md`](references/adapters/gpt.md)。每个适配器文件都可以**单独拿来跑完整个六镜流程**。

---

## 1. Purpose｜解决什么重复问题

很多人做个人 IP 视觉，是一张一张出图：今天一张头像、明天一张海报、后天一张 Banner。**每张都重新写 Prompt、重新设计角色、重新定风格**——结果六张图像六个不相关的设计师做的。

本 Engine 把这件事变成一条**可复用的流水线**：先定义一次「视觉 IP DNA」和「连续性契约」，然后让每一张图只是**同一个 IP 状态机的下一次状态转移**，而不是一次新的创作。换主体、换职业、换隐喻、换平台，Engine 都能重新推导，而不重画。

**产物**：小红书 / 小绿书 3:4 竖版知识卡 × 6（一镜到底的连续镜头）+ 一张可适配 X.com 的 Banner 母版。

---

## 2. Scope｜范围

### In scope
- 个人 / 角色 IP 的**连续视觉叙事**（不是单张海报）。
- 小红书 / 小绿书 3:4 竖版「六镜」知识卡。
- 跨平台一致性：Seedream / GPT / Grok / Gemini（四个适配器）。
- 最终 Banner 适配（X.com 1500×500）。

### Out of scope
- 真实摄影 / 实拍素材处理。
- 视频分镜（本 Engine 只产出静态连续帧；若需视频见 Video Prompt Compression 等 Case）。
- 商用版权与肖像权合规判定（使用前请自行核验）。

---

## 3. Pipeline｜流水管道

```
┌──────────────────────────────────────────────────────────────┐
│  STAGE 0   IDENTITY EXTRACTION  (输入：身份 / 能力 / 价值观)    │
└───────────────────────────────┬──────────────────────────────┘
                                  ▼
┌──────────────────────────────────────────────────────────────┐
│  STAGE 1   VISUAL IP DNA        (母版：主体/身份/能力/隐喻/世界) │
│            → templates/fill-in-sheet.md                       │
└───────────────────────────────┬──────────────────────────────┘
                                  ▼
┌──────────────────────────────────────────────────────────────┐
│  STAGE 2   CONTINUITY CONTRACT  (共享护栏：保留什么/只演化什么)  │
└───────────────────────────────┬──────────────────────────────┘
                                  ▼
┌──────────────────────────────────────────────────────────────┐
│  STAGE 3   SIX-FRAME STATE MACHINE  (六镜状态机，见 §5)        │
│   MASTER → IDENTITY → EVOLUTION → CONTINUITY → ENTROPY → PRESENCE│
└───────────────────────────────┬──────────────────────────────┘
                                  ▼
┌──────────────────────────────────────────────────────────────┐
│  STAGE 4   PLATFORM ADAPTER     (选一条平台线，见 §6)           │
│   Seedream / GPT / Grok / Gemini  ← 每条线都是独立自包含文件     │
└───────────────────────────────┬──────────────────────────────┘
                                  ▼
┌──────────────────────────────────────────────────────────────┐
│  STAGE 5   BANNER ADAPTER         (X.com 1500×500，独立层)     │
└───────────────────────────────┬──────────────────────────────┘
                                  ▼
┌──────────────────────────────────────────────────────────────┐
│  STAGE 6   VISION QC → LOCAL REPAIR → FINAL QA                 │
└──────────────────────────────────────────────────────────────┘
```

**工程化心法**（不要把流水线退化成「主图 Prompt + 次图 Prompt + …」）：

```
MASTER DNA
     + CONTINUITY CONTRACT
     + STAGE DELTA            (每一镜只改这一层状态)
     + PLATFORM ADAPTER       (决定怎么驱动模型)
     ↓
FINAL IMAGE PROMPT
```

> 每张图不是重新 Prompt，而是**同一个 IP 状态机的下一次状态转移**。

---

## 4. Visual IP DNA（母版）｜Stage 1

这是整条流水线的「一次定义」。填好 [`templates/fill-in-sheet.md`](templates/fill-in-sheet.md) 里的变量表，后续六镜**都从这套值推导**，不重述世界观。

```
VISUAL IP DNA

Subject:        [SUBJECT]
Identity:       [IDENTITY]
Core Ability:   [CORE ABILITY]
Visual Metaphor:[VISUAL METAPHOR]
Core Message:   [CORE MESSAGE]
Visual World:   [VISUAL WORLD]

Evolution:  CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE
Visual Direction: cinematic, intelligent, restrained, premium editorial,
  high visual coherence, sophisticated spatial composition, strong material
  realism, controlled color palette, subtle cinematic lighting, visual storytelling.

The visual evolution must move from: complex → organized → structured → minimal → essential.
The emotional evolution must move from: uncertainty → learning → mastery → clarity → presence.
The visual entropy must move from: high → medium-high → medium → low → extremely low.
The visual power must increase while visual noise decreases.
```

### 核心公式（Engine Formula）
`IP VISUAL EVOLUTION = Identity Continuity × Narrative Continuity × Motion Continuity × Entropy Gradient × Visual Weight × Spatial Continuity × Aura Refinement × Platform Adaptation`

**换主体，不换 Engine。** Skill 自动重新推导隐喻、成长、动作、世界、熵、权重与 Banner 构图。

---

## 5. Six-Frame State Machine｜Stage 3（六镜状态机）

六镜是一条**连续视觉叙事**被拆成的 6 个连续镜头，**不是 6 张知识卡**。每一镜 = 状态机的下一次转移：

| 帧 | 阶段 | 承担的任务 | 状态转移（STAGE DELTA） |
|---|---|---|---|
| FRAME 01 / IMAGE 01 | **MASTER** | 建立整个视觉世界（最高信息量，但只埋下演化的种子） | 定义主世界，不画完五阶段 |
| FRAME 02 / IMAGE 02 | **IDENTITY** | 职业 → 能力 → 隐喻 | `Profession → Core Ability → Visual Metaphor` |
| FRAME 03 / IMAGE 03 | **EVOLUTION** | `CHAOS→FLOW→SYSTEM→SILENCE→PRESENCE` | 状态转换，不是姿势替换 |
| FRAME 04 / IMAGE 04 | **CONTINUITY** | 身份连续 + 动作连续 + 世界连续 | 同一世界被理解得更深 |
| FRAME 05 / IMAGE 05 | **ENTROPY / WEIGHT** | 熵减：视觉权重重新分配 | `信息/物体/动作/工具 ↓`，`清晰/留白/存在感 ↑` |
| FRAME 06 / IMAGE 06 | **PRESENCE / BANNER** | 最终 Hero，可适配 X Banner | `Power↑ / Noise↓ / Purity↑`，不靠更亮 |

**连续性契约（每镜都生效，护栏）**

```
CONTINUITY CONTRACT
This is one continuous visual IP system, not a collection of unrelated images.
Preserve: subject identity, face/facial structure, species, body proportions,
  signature features, core silhouette, visual metaphor, world, material language,
  core color system, cinematic art direction.
Only evolve: state, action, information density, tools, environment organization,
  spatial complexity, aura, visual weight, narrative meaning.
Do not redesign the subject between images. Do not reset the world between images.
Do not create six unrelated poster designs.
```

### 十条原则（必须遵守）
1. 职业只是输入，能力才是视觉主题。
2. 进化是境界转换，不是姿势替换。
3. 阶段不是五张卡，而是一条连续时间轴。
4. 主体不是多个相似角色，而是同一个人的多个状态。
5. 世界不是不断换场景，而是同一个世界逐渐被理解。
6. 信息减法不是少写文字，而是减少认知噪音。
7. 气场进化不是越来越亮，而是越来越纯。
8. 最终强度来自 Presence，而不是视觉噪音。
9. Banner 不是做完再裁，而是从一开始就为平台裁切机制设计。
10. 最终产品不是一张图片，而是一套可迁移的视觉 IP 系统。

---

## 6. Platform Adapter｜Stage 4（选一条平台线）

四条平台线**共享同一套 DNA 与契约**，区别只在「怎么驱动模型」。每个适配器文件都自包含（主图 + 次图 01–05 + SOP + 负向词）。**打开对应文件即可跑完整流程。**

| Engine | 最适合的连续方式 | Prompt 策略 | 适配器文件 |
|---|---|---|---|
| **Seedream** | 多参考 / 连续生成 | 完整 Creative Brief + Reference Role + Sequential Generation | [`seedream.md`](references/adapters/seedream.md) |
| **GPT** | 对话式逐层编辑 | `KEEP EXACTLY` / `CHANGE ONLY` | [`gpt.md`](references/adapters/gpt.md) |
| **Grok** | 连续视觉导演 | Frame-to-Frame Narrative + 显式帧编号 | [`grok.md`](references/adapters/grok.md) |
| **Gemini** | Reference + conversational | 上一张作主参考 + 角色命名 + 五维（SUBJECT/COMPOSITION/ACTION/LOCATION/STYLE） | [`gemini.md`](references/adapters/gemini.md) |

> Seedream 的多图/连续生成最适合直接做成「系列生产器」；Gemini 特别适合把上一张作为下一张的视觉锚点；GPT 适合在接近目标后逐层修；Grok 适合把整个系列作为连续视觉叙事来导演。

---

## 7. Banner Adapter｜Stage 5（独立层，不要混进主图）

X Banner 的 `1500×500 / Safe Zone / Crop Simulation / Avatar Collision` 是**独立的适配层**，在 FRAME 06 之后单独处理，**不要写进小红书主图提示词**。

- Banner 是响应式视觉画布，不是普通横图。
- 目标画布 1500×500；考虑上下显示裁切与头像遮挡。
- 设计原则：**先设计「被裁剪以后仍然成立」的画面，再设计原图**。
- 把 FRAME 06 的脸 / 头 / 关键手部放进 safe zone，远离上下边缘。

---

## 8. Vision QC & Repair｜Stage 6

**QC 目标**：身份一致性 / 叙事连续性 / 动作连续性 / 世界连续性 / 熵梯度 / 视觉权重 / 安全区 / 头像遮挡 / 文字空间融合。

**修复原则**：先定位具体失效点，再**局部修复**而不是整张重做。例如某镜脸崩 → 只重生成那一镜并要求「脸/眼型/毛色/轮廓与上一镜完全一致」。

---

## 9. Evaluation

见 [`evaluation/evaluation-schema.json`](evaluation/evaluation-schema.json)（启发式本地评测）。核心维度：
- **Identity continuity**（身份连续）：六镜是否为同一角色。
- **Narrative continuity**（叙事连续）：是否一条连续时间轴而非五张卡。
- **Entropy gradient**（熵梯度）：信息量是否逐镜收敛。
- **Platform adaptation**（平台适配）：是否尊重所选模型的连续性机制。
- **Banner readiness**（Banner 就绪）：FRAME 06 是否满足 1500×500 安全区。

评分阈值 80（heuristic-local）。低于阈值 → 回到失效那一镜局部修复。

---

## 10. Failure Modes｜失败模式

- **六镜变成六张不同风格海报** → 每镜没带 Continuity Contract / 没以上一镜为锚。
- **出现分镜感 / 硬竖线 / 编号** → 把 `CHAOS→PRESENCE` 写成了并列列表；补 `ONE continuous long take, no panels, no numbered captions`。
- **角色漂移（毛色/眼镜/脸变了）** → 参考图未上传或角色未命名；补参考图 + 显式重述主体 +（Gemini）固定角色名。
- **最后一张过曝** → 模型把 climax 理解成「更亮」；强调 `do not make it brighter, make it purer`。
- **3:4 被裁成方图** → 比例未声明；首行固定 `3:4 vertical`。
- **中文标题像贴上去的 UI 标签** → 未指定物理载体；明确 `printed / carved / handwritten inside the world`。

---

## 11. Entry Point｜怎么开始

1. 填 [`templates/fill-in-sheet.md`](templates/fill-in-sheet.md)（或直接用 [`examples/zhuji-mao/`](examples/zhuji-mao/) 的默认值）。
2. 选平台：打开 [`references/adapters/`](references/adapters/) 里对应的一条线。
3. 按该适配器的「调用节奏」逐镜生成：MASTER → 次图 01–05。
4. 收尾用 §7 Banner Adapter 把 FRAME 06 适配成 X.com 1500×500。
5. 跑 Evaluation，低于阈值回到失效镜局部修复。
