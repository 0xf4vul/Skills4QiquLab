<!-- Part of Case 008 · IP Visual Evolution Engine · 个人 IP 视觉进化引擎
     This file is a self-contained platform adapter. You can run the whole
     6-frame continuous visual IP workflow using ONLY this file.
     Engine core + shared DNA/Continuity Contract: ../SKILL.md
     Other platform adapters: grok.md · gemini.md · seedream.md · gpt.md -->

# v1.3.1 · GPT｜主图 + 次图 01–05 连续提示词

> **平台策略**：Master → `KEEP EXACTLY` → `CHANGE ONLY` → 逐层迭代
> **产物**：小红书 / 小绿书 3:4 竖版知识卡，6 张一镜到底的连续镜头
> **本文件独立自足**：主图 + 次图 01→05 的完整连续提示词全在这里。

---

## 0. 怎么用（GPT 版的关键差异）

GPT Image 的工作方式是**对话式逐层编辑**，官方建议明确「保留什么 / 修改什么」并逐层迭代。所以这里的策略和 Seedream 完全不同：

1. **全程待在同一个会话里**。生成 IMAGE 02 时不要新开对话——上一张图就是上下文，新会话 = 丢掉连续性。
2. **主图说全，次图说少**。主图第一次完整描述世界；之后**绝对不要重新描述世界观**，只声明「保留 + 改这一层」。GPT 重述越多，漂移越大。
3. **固定句式**：`Continue from the previous image.` → `KEEP EXACTLY:` → `CHANGE ONLY:`。这三行是 GPT 版连续性的骨架，不要改顺序。
4. **一次只改一层**。一轮里同时改动作+环境+光+构图，GPT 会顺手把脸也改了。拆两轮：先改状态，再微调构图。

**会话节奏模板**

```text
[第 1 轮]  §5 主图完整 Brief        → 得到 IMAGE 01
[第 2 轮]  §6 IMAGE 02              → 得到 IMAGE 02
[第 3 轮]  §7 IMAGE 03              → 得到 IMAGE 03
[第 4 轮]  §8 IMAGE 04              → 得到 IMAGE 04
[第 5 轮]  §9 IMAGE 05              → 得到 IMAGE 05
[第 6 轮]  §10 IMAGE 06             → 得到 IMAGE 06
```

若某轮脸崩了，不要往下走，先补一句：

```text
Regenerate, but keep the face structure, eye shape, muzzle,
fur pattern and silhouette identical to the previous image.
Change nothing else.
```

---

## 1. 变量表 FILL-IN SHEET

已按你的 IP 填好默认值；换 IP 时改这一列 + 全文替换英文锚点。

| 变量 | 含义 | 当前默认值（筑基猫） | 提示词里的英文锚点 |
|---|---|---|---|
| SUBJECT | 主体 | 橘猫 + 圆眼镜 | `a calm orange tabby cat wearing round glasses` |
| IDENTITY | 身份 | 用 AI 搞钱、真交付的实战派 | `an AI practitioner who actually ships and monetizes` |
| CORE ABILITY | 核心能力 | 把散落的 AI 工具收敛成一条能跑通的链路 | `collapsing scattered AI tools into one pipeline that actually runs` |
| VISUAL METAPHOR | 视觉隐喻 | 道场 × 工作台；散落工具碎片 + 一条刚亮起的线 | `a quiet dojo crossed with a modern workspace` |
| CORE MESSAGE | 核心信息 | 「101 个工具在手，不如跑通一条链路。」 | `"101 个工具在手，不如跑通一条链路。"` |
| VISUAL WORLD | 视觉世界 | 克制的当代工作室 + 东方修行感 | `restrained contemporary studio with Eastern cultivation atmosphere` |
| CORE TITLE | 主图标题 | 筑基猫｜一条链路 | `"筑基猫｜一条链路"` |
| TITLE 02 | 次图01 标题 | 我是怎么被定义的 | `"我是怎么被定义的"` |
| TITLE 03 | 次图02 标题 | 我是怎么练成的 | `"我是怎么练成的"` |
| TITLE 04 | 次图03 标题 | 为什么我还是我 | `"为什么我还是我"` |
| TITLE 05 | 次图04 标题 | 越空，越强 | `"越空，越强"` |
| TITLE 06 | 次图05 标题 | 101 个工具在手，不如跑通一条链路。 | `"101 个工具在手，不如跑通一条链路。"` |
| PALETTE | 核心色彩 | 冷蓝灰 → 暖光 → 象牙白 + 柔金 | `cool blue-grey → warm key light → ivory + soft gold` |
| ASPECT | 比例 | 3:4 竖版 | `Aspect ratio: 3:4 vertical` |

---

## 2. 六镜结构

```text
主图 MASTER        IMAGE 01  建立整个视觉世界
  ↓
次图01 IDENTITY    IMAGE 02  职业 → 能力 → 隐喻
  ↓
次图02 EVOLUTION   IMAGE 03  CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE
  ↓
次图03 CONTINUITY  IMAGE 04  身份连续 + 动作连续 + 世界连续
  ↓
次图04 ENTROPY     IMAGE 05  熵减：视觉权重重新分配
  ↓
次图05 PRESENCE    IMAGE 06  最终 Hero / Banner-ready
```

---

## 3. 连续性契约 CONTINUITY CONTRACT

GPT 版**不需要**每轮把契约全文重贴（重贴会让它重绘）。契约只在**主图那一轮贴一次**，之后靠 `KEEP EXACTLY` 清单承接。

### 3.1 主图轮使用（完整版，已并入 §5，此处供单独调用）

```text
CONTINUITY CONTRACT

This is one continuous visual IP system, not a collection of unrelated images.
The same visual identity must remain recognizable across every image.

Preserve:
- the same subject identity
- the same face / facial structure
- the same species or character type
- the same body proportions
- the same signature features
- the same core silhouette
- the same visual metaphor
- the same world
- the same material language
- the same core color system
- the same cinematic art direction

Only evolve:
- state
- action
- information density
- tools
- environment organization
- spatial complexity
- aura
- visual weight
- narrative meaning

The images must feel like consecutive frames from the same visual story.
Do not redesign the subject between images.
Do not reset the world between images.
Do not create six unrelated poster designs.

From now on, every following image in this conversation must follow this contract.
When I say "continue from the previous image",
keep everything above and change only what I explicitly specify.
```

### 3.2 次图轮使用（压缩版，已并入各 KEEP 块）

```text
Same subject identity, face, silhouette, clothing language,
material language, color palette, lighting logic, visual world
and overall art direction as the previous image.
```

---

## 4. Visual IP DNA（仅主图轮贴一次）

```text
VISUAL IP DNA

Subject: a calm orange tabby cat wearing round glasses
Identity: an AI practitioner who actually ships and monetizes
Core Ability: collapsing scattered AI tools into one pipeline that actually runs
Visual Metaphor: a quiet dojo crossed with a modern workspace
Core Message: "101 个工具在手，不如跑通一条链路。"
Visual World: restrained contemporary studio with subtle Eastern cultivation atmosphere

Evolution: CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE

Visual Direction:
cinematic, intelligent, restrained, premium editorial,
high visual coherence, sophisticated spatial composition,
strong material realism, controlled color palette,
subtle cinematic lighting, visual storytelling,
high-end contemporary visual identity design.

The visual evolution must move from: complex → organized → structured → minimal → essential.
The emotional evolution must move from: uncertainty → learning → mastery → clarity → presence.
The visual entropy must move from: high → medium-high → medium → low → extremely low.

The visual power must increase while visual noise decreases.
```

---

## 5. 主图 MASTER｜IMAGE 01

> 这是**唯一一次**完整描述世界。之后所有轮次都不再重述。

```text
Create the master image for a continuous six-image visual IP editorial series
for Xiaohongshu / WeChat Xiaolvshu.

Aspect ratio: 3:4 vertical.

The subject is a calm orange tabby cat wearing round glasses.
The character represents an AI practitioner who actually ships and monetizes.
Their core ability is collapsing one hundred scattered AI tools into a single
pipeline that actually runs.
Use a quiet dojo crossed with a modern workspace as the central visual metaphor.

CORE MESSAGE
"101 个工具在手，不如跑通一条链路。"

VISUAL WORLD
A restrained contemporary studio with subtle Eastern cultivation atmosphere:
raw stone, aged wood, matte metal, paper, dust suspended in light.
This exact world will be reused in all following images.

The master image should establish:
- the subject's identity
- the visual metaphor
- the world
- the color palette
- the material language
- the lighting
- the camera language
- the typography language

The visual story will later evolve through:

CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE

Do not show these five stages literally.
This first image establishes the world in which the evolution will happen.

NARRATIVE STATE
The moment before transformation.
High information density but one coherent world:
dozens of loose tool fragments, scattered instruments, drifting notes and
half-finished mechanisms around the subject, not yet connected,
with one single luminous thread only just beginning to appear.

COMPOSITION
Strong central hero subject, clear spatial hierarchy,
distinct foreground / middle ground / background,
generous negative space for typography,
natural left-to-right visual direction implying future evolution.

LIGHTING AND COLOR
Establish the palette now and keep it for the whole series:
cool blue-grey shadows, one warm controlled key light,
restrained saturation, at most three dominant colors,
soft volumetric haze, realistic contact shadows.

STYLE
Premium cinematic editorial art direction,
restrained color palette, realistic materials,
sophisticated composition, high visual coherence.

TITLE
"筑基猫｜一条链路"
Make the typography part of the physical visual world
(a printed object, a carving, or handwriting in the scene)
rather than a generic UI element.

CONTINUITY CONTRACT
This is one continuous visual IP system, not a collection of unrelated images.
Preserve across all following images:
subject identity, face and facial structure, species, body proportions,
signature features, core silhouette, visual metaphor, world, material language,
core color system and cinematic art direction.
Only evolve: state, action, information density, tools, environment organization,
spatial complexity, aura, visual weight and narrative meaning.
The images must feel like consecutive frames from the same visual story.
Do not redesign the subject between images.
Do not reset the world between images.
Do not create six unrelated poster designs.

AVOID
No unrelated characters. No unrelated environments. No visual-style reset.
No collage fragmentation. No five side-by-side stages.
No generic AI poster aesthetics. No neon. No flat lighting. No oversaturation.
```

---

## 6. 次图 01｜IDENTITY → IMAGE 02

> 从这一轮开始**只贴这一块**。GPT 会自己带着上一张的上下文。

```text
Continue from the previous image.
Do not redesign anything.

KEEP EXACTLY
- subject identity
- facial structure, eye shape, muzzle, fur pattern
- body proportions
- signature features
- silhouette
- clothing language
- material language
- color palette
- lighting logic
- visual world
- overall art direction

CHANGE ONLY

Profession:
an AI practitioner who actually ships and monetizes

Core Ability:
collapsing one hundred scattered AI tools into a single pipeline that actually runs

Visual Metaphor:
a quiet dojo crossed with a modern workspace

Narrative stage:
IDENTITY → ESSENCE → VISUAL METAPHOR

State:
The subject is now actively interacting with the metaphorical world,
physically engaging with the tools and materials around it.

Action:
Deliberate, still exploratory gestures.
Clear visual relationship between subject and environment.

Environment evolution:
The same room, but slightly more organized than the master image.
Introduce structured objects, meaningful tools,
environmental clues and a clear hierarchy.
The visual metaphor must be expressed through
objects, gestures and spatial relationships,
not through literal infographic diagrams.

Information density:
Still relatively high, but more organized than IMAGE 01.

Aura:
Barely perceptible. Do not add glow or halo.

Composition:
Keep the same camera philosophy and framing logic as the previous image.
Clear focal hierarchy, generous negative space preserved.

Typography:
"我是怎么被定义的"
Optional supporting line:
"101 个工具在手，不如跑通一条链路。"
Typography must exist naturally within the physical world.

The result must look like the next frame in the same visual story,
not a redesigned poster.

Do not change the character design.
Do not change the visual world.
Do not introduce a new visual style.
Do not reset the composition language.
```

---

## 7. 次图 02｜EVOLUTION → IMAGE 03

```text
Continue from the previous image.
Do not redesign anything.

KEEP EXACTLY
- subject identity
- facial structure, eye shape, muzzle, fur pattern
- body proportions
- signature features
- silhouette
- clothing language
- material language
- color palette
- lighting logic
- visual world
- overall art direction

CHANGE ONLY
Identity state → Evolution state

Narrative stage:
CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE

State:
One continuous subject progressing through increasing mastery.
Evolution is STATE TRANSFORMATION, not pose replacement.

Action:
Early motion is exploratory, middle motion is controlled,
late motion is extremely precise, final state approaches stillness.
Movement precision increases across the image.

Environment evolution:
Same world. Traces of previous states remain embedded in it.
Visual progression: high complexity → organized complexity →
structured clarity → minimal environment → essential presence.
The environment becomes cleaner and more intentional.

Information density:
Reduced. Fewer tools, fewer objects, less visual noise.
The subject stays calmer and more precise.

Aura:
0% → 25% → 50% → 75% → 100%
But do not make the final state brighter. Make it purer.

Composition:
One continuous spatial narrative with a strong left-to-right flow.
Do not create five disconnected character portraits.
Do not place five equal figures side by side.
No hard vertical seams. No panel boundaries.

Typography:
"我是怎么练成的"

The image must visually communicate:
"change is a change of realm, not a change of pose."

Do not change the character design.
Do not change the visual world.
Do not introduce a new visual style.
```

---

## 8. 次图 03｜CONTINUITY → IMAGE 04

```text
Continue from the previous image.
Do not redesign anything.

KEEP EXACTLY
- subject identity
- facial structure, eye shape, muzzle, fur pattern
- body proportions
- signature features
- silhouette
- clothing language
- material language
- color palette
- lighting logic
- visual world
- overall art direction

CHANGE ONLY
Motion continuity → World continuity

Narrative stage:
CONTINUITY.

Show three layers of continuity simultaneously:

1. IDENTITY CONTINUITY
same face, same body proportions, same signature features,
same silhouette, same clothing language.

2. MOTION CONTINUITY
the current movement must logically continue from the previous image.

3. WORLD CONTINUITY
the environment is the same world,
but increasingly organized and understood.

Environment evolution:
Clutter → Organization → System → Architecture → Essence
Do not change the world abruptly.
The image should feel like the camera has simply moved forward
inside the same universe.

Use visual bridges:
gesture, directional energy, objects, light,
architecture, surface materials, camera movement.

Information density:
Medium. Ordered, not sparse.

Aura:
Steady, restrained, no bloom.

Composition:
Strong left-to-right visual flow.
The previous state visually leads into the current state.
The current state implies the next state.
No isolated infographic panels.
No separate character cards.
No hard visual borders between stages.

Typography:
"为什么我还是我"

Do not change the character design.
Do not change the visual world.
Do not introduce a new visual style.
```

---

## 9. 次图 04｜ENTROPY + WEIGHT → IMAGE 05

```text
Continue from the previous image.
Do not redesign anything.

KEEP EXACTLY
- subject identity
- facial structure, eye shape, muzzle, fur pattern
- body proportions
- signature features
- silhouette
- clothing language
- material language
- color palette family
- lighting logic
- visual world
- overall art direction

CHANGE ONLY
Entropy reduction → Visual weight redistribution

Narrative stage:
ENTROPY + VISUAL WEIGHT

REDUCE
- information
- object count
- tool count
- movement
- particles
- background complexity
- color complexity
- typography density

INCREASE
- visual clarity
- subject authority
- spatial breathing room
- compositional precision
- emotional presence

Visual entropy as a compositional principle:
100 → 78 → 55 → 22 → 5
Do not display these numbers anywhere in the image.

IMPORTANT
Visual weight is NOT physical size.
The subject should not simply become larger.
Make the subject more visually important through
space, contrast, isolation and compositional hierarchy.

Suggested narrative weight:
CHAOS 14% / FLOW 18% / SYSTEM 28% / SILENCE 18% / PRESENCE 22%
These are compositional principles, not visible labels.

Environment evolution:
Same world, now quiet, architectural and materially refined.
Large areas of calm negative space.

Colour:
Shift toward warm ivory and soft gold.
Reduce contrast noise. Keep one quiet luminous source.

Information density:
Low.

Aura:
Strong but silent. Power through purity, not brightness.

Composition:
Fewer elements, stronger hierarchy, more air.
The image must feel quieter than the previous image,
yet visually stronger.

Typography:
"越空，越强"
Restrained typography integrated into the environment.

Do not change the character design.
Do not change the visual world.
Do not display percentages. No HUD. No infographic labels.
```

---

## 10. 次图 05｜BANNER / PRESENCE → IMAGE 06

```text
Continue from the previous image.

KEEP EXACTLY
- subject identity
- facial structure, eye shape, muzzle, fur pattern
- body proportions
- signature features
- silhouette
- clothing language
- material language
- core color system
- lighting logic
- visual world
- overall art direction

CHANGE ONLY
Final Presence → Banner-ready composition

Narrative stage:
PRESENCE. The culmination of the entire visual IP evolution.
Mastery through refinement.
The subject is calm, precise and visually undeniable.

Action:
No excessive action.
No excessive objects.
No excessive effects.
No visual clutter.

Environment evolution:
The same world has reached its essential form:
minimal, architectural, spatially quiet,
materially refined, symbolically meaningful.

Aura:
Power ↑
Visual Noise ↓
Purity ↑
Do not make the final image brighter simply to feel powerful.
Create authority through stillness, negative space, precision,
material quality and composition.

Colour:
Resolve the left-to-right gradient into warm ivory and soft gold.
Quiet luminous presence.

Composition:
Strong cinematic horizontal visual flow,
large negative space,
clear hero zone,
strong focal hierarchy,
premium editorial composition.
Keep faces, head and key hands inside a banner-safe zone
away from the top and bottom edges.

This image must work as:
1. a standalone visual,
2. a Xiaohongshu / WeChat Xiaolvshu final card,
3. a source composition that can later be adapted into an X.com Banner.

Typography:
"101 个工具在手，不如跑通一条链路。"
Typography is a physical narrative artifact, not a UI label.
Keep it faint and partially embedded in the environment.

FINAL FEELING
not spectacle, not complexity, not brightness.
Presence. Silence. Precision. Authority.

The final image must feel like the natural conclusion
of the previous five images.

Do not change the character design.
Do not reset the visual style.
No giant halo. No neon. No superhero pose. No religious iconography.
```

---

## 11. GPT 实操 SOP 与踩坑

| 现象 | 原因 | 修正 |
|---|---|---|
| 每轮脸都变 | 每轮把世界重述了一遍 | **删掉重述**，只留 `KEEP EXACTLY / CHANGE ONLY`；脸崩即重生成，不要继续往下 |
| 一次改动导致整图重绘 | 一轮里塞了动作+环境+光+构图 | 拆成两轮：先改状态，下一轮再微调构图 |
| 出现「1. 2. 3.」或图表感 | 提示词把 evolution 写成了列表 | 补 `no infographic panels, no numbered captions, no labels` |
| 5 个人物排排站 | 模型把 CHAOS→PRESENCE 理解成 5 个角色 | 强调 `one continuous subject, state transformation not pose replacement` |
| 最后一张过曝 / 发光 | 模型默认把 climax 做成「更亮」 | 强调 `do not make the final state brighter, make it purer` |
| 3:4 变方图 | 比例未声明或漂移 | 首轮写明 `Aspect ratio: 3:4 vertical`；漂移时补 `keep the 3:4 vertical aspect ratio` |
| 文字变成 UI 标签 | 未指定物理载体 | 明确 `printed / carved / handwritten inside the world` |

**快速补救指令（任一轮出问题时贴在会话里）**

```text
Regenerate this image only.
Keep everything from the previous image identical,
including face structure, eye shape, muzzle, fur pattern and silhouette.
Change only the following: [你的单点修改]
Do not redesign the character. Do not reset the world.
```

---

## 12. 最后一层（不要混进主图）

X Banner 的 `1500×500 / Safe Zone / Crop Simulation / Avatar Collision` 是独立的 **Banner Adapter 层**，在 IMAGE 06 之后单独处理，不要写进小红书主图提示词。
