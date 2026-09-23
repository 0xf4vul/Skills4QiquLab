<!-- Part of Case 008 · IP Visual Evolution Engine · 个人 IP 视觉进化引擎
     This file is a self-contained platform adapter. You can run the whole
     6-frame continuous visual IP workflow using ONLY this file.
     Engine core + shared DNA/Continuity Contract: ../SKILL.md
     Other platform adapters: grok.md · gemini.md · seedream.md · gpt.md -->

# v1.3.1 · Seedream｜主图 + 次图 01–05 连续提示词

> **平台策略**：Master Image（完整 Creative Brief）→ Reference Image（上一张作参考）→ Sequential Generation（顺序生成）
> **产物**：小红书 / 小绿书 3:4 竖版知识卡，6 张一镜到底的连续镜头
> **本文件独立自足**：主图 + 次图 01→05 的完整连续提示词全在这里，不需要再看其它文件。

---

## 0. 怎么用（三步）

1. **先跑主图**：把 §5 的提示词整段贴进 Seedream，出图满意后**保存这张图**（它 = IMAGE 01 = 整个系列的视觉母版）。
2. **逐张顺序生成**：生成 IMAGE 02 时，把 IMAGE 01 作为参考图喂进去；生成 IMAGE 03 时，喂 IMAGE 02（或 01+02）。**不要跳序号**，Seedream 的连续生成是靠上一张锚定的。
3. **每次都带契约**：§3 的 `CONTINUITY CONTRACT` 每张图都要跟着提示词一起贴。Seedream 提示词可以很长，不要为了「简洁」把它删掉——它是保证 6 张像同一部电影而不是 6 张海报的唯一保险。

---

## 1. 变量表 FILL-IN SHEET

下面是**已经按你的 IP 填好**的默认值。换成别的 IP 时，只改这一列，然后全文替换对应英文短语即可。

| 变量 | 含义 | 当前默认值（筑基猫） | 提示词里的英文锚点 |
|---|---|---|---|
| SUBJECT | 主体 | 橘猫 + 圆眼镜 | `a calm orange tabby cat wearing round glasses` |
| IDENTITY | 身份 | 用 AI 搞钱、真交付的实战派 | `an AI practitioner who actually ships and monetizes` |
| CORE ABILITY | 核心能力 | 把 101 个散工具收敛成一条能跑通的链路 | `collapsing scattered AI tools into one pipeline that actually runs` |
| VISUAL METAPHOR | 视觉隐喻 | 道场 × 工作台；散落工具碎片 + 一条刚亮起的线 | `a quiet dojo crossed with a modern workspace` |
| CORE MESSAGE | 核心信息 | 「101 个工具在手，不如跑通一条链路。」 | `"101 个工具在手，不如跑通一条链路。"` |
| VISUAL WORLD | 视觉世界 | 克制的当代工作室 + 东方修行感（石/木/哑光金属/纸） | `restrained contemporary studio with Eastern cultivation atmosphere` |
| CORE TITLE | 主图标题 | 筑基猫｜一条链路 | `"筑基猫｜一条链路"` |
| TITLE 02 | 次图01 标题 | 我是怎么被定义的 | `"我是怎么被定义的"` |
| TITLE 03 | 次图02 标题 | 我是怎么练成的 | `"我是怎么练成的"` |
| TITLE 04 | 次图03 标题 | 为什么我还是我 | `"为什么我还是我"` |
| TITLE 05 | 次图04 标题 | 越空，越强 | `"越空，越强"` |
| TITLE 06 | 次图05 标题 | 101 个工具在手，不如跑通一条链路。 | `"101 个工具在手，不如跑通一条链路。"` |
| PALETTE | 核心色彩 | 冷蓝灰（左）→ 暖光（中）→ 象牙白 + 柔金（右） | `cool blue-grey → warm key light → ivory + soft gold` |
| ASPECT | 比例 | 3:4 竖版（小红书/小绿书） | `vertical editorial composition, 3:4` |

---

## 2. 六镜结构（不要改成 6 张并列知识卡）

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

**一句话**：每张图不是重新 Prompt，而是同一个 IP 状态机的下一次状态转移。

---

## 3. 连续性契约 CONTINUITY CONTRACT（每张图都带上）

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
```

---

## 4. Visual IP DNA（母版，可整段并入任意一条提示词）

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

Continuity:
same subject, same identity, same world, same visual language,
progressive state transformation.

The visual evolution must move from: complex → organized → structured → minimal → essential.
The emotional evolution must move from: uncertainty → learning → mastery → clarity → presence.
The visual entropy must move from: high → medium-high → medium → low → extremely low.

The visual power must increase while visual noise decreases.
```

---

## 5. 主图 MASTER｜IMAGE 01

**Seedream 用法**：当作一份完整 Creative Brief 写，不要压缩。生成后**留存本图**，它是后续 5 张的参考源。

```text
Create the MASTER IMAGE of a continuous six-frame visual IP editorial series
for Xiaohongshu / WeChat Xiaolvshu.

This is IMAGE 01 / MASTER.
It establishes the visual DNA for IMAGE 02 to IMAGE 06.
Do not depict the entire evolution here.
Establish the world in which the evolution will happen.

FORMAT
Vertical editorial composition, 3:4 aspect ratio,
premium knowledge-card cover,
designed as the opening frame of one continuous visual story.

CORE CONCEPT
Turn the identity of the subject into a visual IP evolution system:
a genuine practitioner who converts scattered AI tools into
one working, monetizable pipeline.

SUBJECT
A calm, highly recognizable orange tabby cat wearing round glasses.
Stable face structure, eye shape, muzzle, fur pattern,
body proportions and core silhouette.
The subject must be unmistakably the same character in every following image.

IDENTITY
An AI practitioner who actually ships and monetizes,
not a tool reviewer.

CORE ABILITY
Collapsing one hundred scattered AI tools into a single pipeline
that actually runs.

VISUAL METAPHOR
A quiet dojo crossed with a modern workspace:
dozens of loose tool fragments, scattered instruments,
drifting notes and half-finished mechanisms lying around the subject.
They are NOT connected yet.
One single luminous thread is only just beginning to appear.

CORE MESSAGE
"101 个工具在手，不如跑通一条链路。"

VISUAL WORLD
A restrained, contemporary studio with subtle Eastern cultivation atmosphere:
raw stone, aged wood, matte metal, paper, dust suspended in light.
This exact world will be reused in all six images.

NARRATIVE
This is the moment before transformation:
CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE
High information density, but one coherent world.
Never five separate characters.

COMPOSITION
Strong central hero subject.
Large visual hierarchy.
Clear foreground, middle ground and background.
Generous negative space reserved for typography.
A natural left-to-right visual direction implying that evolution is about to happen.

LIGHTING AND COLOR
Establish the core palette now and keep it for the whole series:
cool blue-grey on the shadow side, one warm controlled key light,
restrained saturation, no more than three dominant colors.
Soft volumetric haze, realistic contact shadows, cinematic depth.

VISUAL LANGUAGE
premium cinematic editorial,
contemporary art direction,
subtle Eastern philosophical restraint,
high-end magazine visual identity,
realistic materials,
controlled texture,
precise spatial relationships,
refined lighting.

TEXT
Only this short title, integrated into the physical world
(printed, carved, or handwritten on an object — never a floating UI label):
"筑基猫｜一条链路"

IMPORTANT
This is IMAGE 01 / MASTER.
It establishes the visual DNA for all following images.

No unrelated characters.
No unrelated environments.
No visual-style reset.
No collage-like fragmentation.
No five side-by-side stages.
No generic AI poster aesthetics.
No neon. No superhero glow. No oversized halo.
No flat lighting. No oversaturation.
```

---

## 6. 次图 01｜IDENTITY → IMAGE 02

**Seedream 用法**：上传 IMAGE 01 作为参考图。提示词前段显式声明参考图角色。

```text
Create IMAGE 02 of the same continuous visual IP editorial series.

REFERENCE
Use IMAGE 01 as the primary visual continuity reference.
Match its world, palette, lighting logic and material language exactly.

CONTINUITY CONTRACT
This is one continuous visual IP system, not a collection of unrelated images.
Preserve: the same subject identity, the same face / facial structure,
the same species, the same body proportions, the same signature features,
the same core silhouette, the same visual metaphor, the same world,
the same material language, the same core color system,
the same cinematic art direction.
Only evolve: state, action, information density, tools,
environment organization, spatial complexity, aura, visual weight, narrative meaning.
The images must feel like consecutive frames from the same visual story.
Do not redesign the subject between images. Do not reset the world between images.

NARRATIVE ROLE
IDENTITY → ESSENCE → VISUAL METAPHOR

Show the transformation:

Profession:
an AI practitioner who actually ships and monetizes

Core Ability:
collapsing one hundred scattered AI tools into a single pipeline that actually runs

Visual Metaphor:
a quiet dojo crossed with a modern workspace

The visual metaphor must be expressed through the environment,
objects, gestures and spatial relationships —
never through literal infographic diagrams.

COMPOSITION
The subject is actively interacting with the metaphorical world.
Create a clear visual relationship between subject and environment.
Visual density is still relatively high,
but noticeably more organized than IMAGE 01.

Introduce:
structured objects,
meaningful tools,
environmental clues,
controlled motion,
clear hierarchy.

LIGHT
Same lighting logic as IMAGE 01.
Slightly warmer key light than the master image.

TEXT
"我是怎么被定义的"
Optional supporting line:
"101 个工具在手，不如跑通一条链路。"
Typography must exist naturally within the physical world.

This image must feel like the immediate next scene after IMAGE 01,
not a new poster.

STYLE
same cinematic editorial system,
same color language,
same material realism,
same camera philosophy,
same visual identity.

No unrelated characters. No visual-style reset. No generic poster aesthetics.
```

---

## 7. 次图 02｜EVOLUTION → IMAGE 03

**Seedream 用法**：上传 IMAGE 02（推荐同时带上 IMAGE 01）作为连续性锚点。

```text
Create IMAGE 03, the EVOLUTION image,
as the direct continuation of IMAGE 02.

REFERENCE
Use the previous generated image as the continuity anchor.
Keep the same character, world, palette and material language.

CONTINUITY CONTRACT
Same subject identity, face, silhouette, clothing and material language.
Same world. Same core color system. Same cinematic art direction.
Only the state advances. Do not redesign anything.
Do not create five disconnected character portraits.
Do not reset the world.

CORE NARRATIVE
Evolution is STATE TRANSFORMATION, not pose replacement.

Show one continuous subject progressing through increasing mastery.

The visual narrative moves from:

CHAOS
→ FLOW
→ SYSTEM
→ SILENCE
→ PRESENCE

Instead of five separate figures,
create one continuous spatial narrative,
where traces of the previous states remain embedded in the same world.

EVOLUTION AXES
Character maturity
Movement precision
Information reduction
Tool reduction
Spatial simplification
Aura refinement

VISUAL PROGRESSION
high complexity
→ organized complexity
→ structured clarity
→ minimal environment
→ essential presence

The subject becomes calmer and more precise,
while the environment becomes cleaner and more intentional.

MOVEMENT
early motion is exploratory,
middle motion is controlled,
late motion is extremely precise,
final state approaches stillness.

AURA
0% → 25% → 50% → 75% → 100%
But do not make the final state brighter.
Make it purer.

LIGHT
Cool blue-grey still dominant on the left,
warm light-trail choreography beginning in the center.

TEXT
"我是怎么练成的"

The image should visually communicate:
"change is a change of realm, not a change of pose."

Maintain exactly the same visual IP identity as previous images.
No hard vertical seams. No panel boundaries. No numbered captions.
```

---

## 8. 次图 03｜CONTINUITY → IMAGE 04

**Seedream 用法**：这是 Seedream 最能发挥优势的一张——可同时上传 IMAGE 01/02/03 作为多重参考。

```text
Create IMAGE 04 of the same continuous visual IP story.

REFERENCE
Use IMAGE 01, IMAGE 02 and IMAGE 03 as continuity references.

PRIMARY CONCEPT
CONTINUITY.

The same identity must remain recognizable across different states.

Show three layers of continuity simultaneously:

1. IDENTITY CONTINUITY
same face,
same body proportions,
same signature features,
same silhouette,
same clothing language.

2. MOTION CONTINUITY
the current movement must logically continue from the previous image.

3. WORLD CONTINUITY
the environment is the same world,
but increasingly organized and understood.

WORLD EVOLUTION
Clutter → Organization → System → Architecture → Essence

Do not change the world abruptly.
The image should feel like the camera has simply moved forward
inside the same universe.

USE VISUAL BRIDGES
gesture,
directional energy,
objects,
light,
architecture,
surface materials,
camera movement.

COMPOSITION
Create a strong left-to-right visual flow.
The previous state should visually lead into the current state.
The current state should imply the next state.

LIGHT
Warm visual climax in the center,
cool residue on the left,
first hints of ivory on the right.

TEXT
"为什么我还是我"

No isolated infographic panels.
No separate character cards.
No hard visual borders between stages.

Same visual identity.
Same cinematic language.
Same color system.
Same material system.
Same world.
```

---

## 9. 次图 04｜ENTROPY + WEIGHT → IMAGE 05

```text
Create IMAGE 05, the VISUAL ENTROPY AND WEIGHT image,
as the direct continuation of the same visual IP series.

REFERENCE
Use the previous images as continuity references.
Keep the same identity, the same world, the same material language.

CORE FORMULA

Visual Entropy:
100 → 78 → 55 → 22 → 5 (compositional principle only, never rendered as numbers)

Visual evolution:
Complex → Simple → Minimal → Presence

Show a gradual reduction of:
information,
object count,
tool count,
movement,
particles,
background complexity,
color complexity,
typography density.

But simultaneously increase:
visual clarity,
subject authority,
spatial breathing room,
compositional precision,
emotional presence.

IMPORTANT
Visual Weight is NOT the same as physical size.

The central SYSTEM state may occupy the strongest structural area,
while the final PRESENCE state carries the strongest visual authority.

Suggested narrative weight:
CHAOS 14%
FLOW 18%
SYSTEM 28%
SILENCE 18%
PRESENCE 22%

These are compositional principles, not visible labels.
Do not display percentages.

The final subject should occupy less visual noise
but possess greater presence.

LIGHT
Shift toward warm ivory and soft gold on the right side.
Reduce contrast noise. Keep one quiet luminous source.

TEXT
"越空，越强"
Use restrained typography integrated into the environment.

The image must feel quieter than IMAGE 04,
yet visually stronger.

Maintain all previous identity and world continuity.
No infographic labels. No HUD. No floating UI text.
```

---

## 10. 次图 05｜BANNER / PRESENCE → IMAGE 06

```text
Create IMAGE 06, the FINAL PRESENCE / BANNER image.

REFERENCE
Use IMAGE 01 to IMAGE 05 as continuity references.

This is the culmination of the entire visual IP evolution.

NARRATIVE
CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE

The final state represents mastery through refinement.
The subject is calm, precise and visually undeniable.

No excessive action.
No excessive objects.
No excessive effects.
No visual clutter.

AURA
Power is expressed through purity.
Power ↑
Visual Noise ↓
Purity ↑

WORLD
The same world has now reached its essential form.

Environment:
minimal,
architectural,
spatially quiet,
materially refined,
symbolically meaningful.

SUBJECT
same exact identity,
same signature features,
same silhouette,
same core visual language.

COMPOSITION
strong cinematic horizontal visual flow,
large negative space,
clear hero zone,
strong focal hierarchy,
premium editorial composition,
with a left-to-right gradient resolving into warm ivory and soft gold.

The image should work as:
1. a standalone visual,
2. a Xiaohongshu / WeChat Xiaolvshu final card,
3. a source composition that can later be adapted into an X.com Banner.

TEXT
"101 个工具在手，不如跑通一条链路。"
Typography is a physical narrative artifact,
not a UI label.
Keep it faint and partially embedded in the environment.

FINAL FEELING
not spectacle,
not complexity,
not brightness.

Presence.
Silence.
Precision.
Authority.

No giant halo. No neon. No superhero pose.
No religious iconography. No explosive glow.

The final image must feel like the natural conclusion
of the previous five images.
```

---

## 11. Seedream 实操 SOP 与踩坑

**推荐调用顺序**

```text
IMAGE 01  纯文生图（完整 Brief）
IMAGE 02  图生图 / 参考图 = IMAGE 01
IMAGE 03  参考图 = IMAGE 02（可加 IMAGE 01 作 DNA 锚）
IMAGE 04  参考图 = IMAGE 01 + 02 + 03（多参考，最能压住漂移）
IMAGE 05  参考图 = IMAGE 04
IMAGE 06  参考图 = IMAGE 01–05 全带（或 04 + 05）
```

**常见失败与修正**

| 现象 | 原因 | 修正 |
|---|---|---|
| 6 张变成 6 个不同角色 | 没带 CONTINUITY CONTRACT，或参考图权重太低 | 契约整段保留；参考图放第一张；把「Preserve」清单前置到提示词开头 |
| 出现硬分块 / 竖光带 | 提示词里出现了 stage 并列描述 | 补 `ONE continuous long take, no panels, no vertical seams` |
| 图上冒出「1. 2. 3.」编号 | 模型把 evolution 序列当成了图表 | 负向加 `numbered captions, infographic labels, panel numbers` |
| 英文技术词像贴上去的 UI 标签 | 未指定物理载体 | 明确写 `handwritten on paper / chalk on wall / engraving / reflection`，并随阶段递减 |
| 最后一张「亮=强」 | 模型默认把 climax 做成高亮 | 强调 `do not make the final state brighter, make it purer` |
| 3:4 被裁成方形 | 比例未显式声明 | 提示词首行固定 `vertical editorial composition, 3:4 aspect ratio` |

**负向词（Seedream 若支持负向框，直接粘贴）**

```text
five separate character cards, character lineup, equal-sized stages,
hard vertical divisions, comic panels, infographic layout, numbered captions,
UI cards, HUD, floating text labels, AI-generated typography, random text blocks,
cyberpunk neon, superhero pose, giant halo, explosive magical aura, excessive golden glow,
plastic materials, 3D game asset look, cartoon mascot, chibi, kawaii,
identity drift, face drift, species drift, extra limbs, duplicate character,
watermark, logos, flat lighting, oversaturated colors
```

---

## 12. 最后一层（不要混进主图）

X Banner 的 `1500×500 / Safe Zone / Crop Simulation / Avatar Collision` 属于**独立的 Banner Adapter 层**，把它当成 IMAGE 06 之后的单独一步处理，不要写进小红书主图的提示词里。
