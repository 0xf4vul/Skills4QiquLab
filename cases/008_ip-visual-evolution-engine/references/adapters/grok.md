<!-- Part of Case 008 · IP Visual Evolution Engine · 个人 IP 视觉进化引擎
     This file is a self-contained platform adapter. You can run the whole
     6-frame continuous visual IP workflow using ONLY this file.
     Engine core + shared DNA/Continuity Contract: ../SKILL.md
     Other platform adapters: grok.md · gemini.md · seedream.md · gpt.md -->

# v1.3.1 · Grok｜主图 + 次图 01–05 连续提示词

> **平台策略**：Frame 01 → Frame-to-Frame Narrative（连续视觉导演）
> **产物**：小红书 / 小绿书 3:4 竖版知识卡，6 张一镜到底的连续镜头
> **本文件独立自足**：主图 + 次图 01→05 的完整连续提示词全在这里。

---

## 0. 怎么用（Grok 版的关键差异）

Grok Image 强调 instruction following、复杂布局、Typography 与跨生成保持。所以**不要**把它当成参数化 Prompt 写，而要把它当成一位**视觉导演**来下指令：

1. **用镜头语言说话**。写「Frame 01 of a six-frame sequence」「the camera has moved forward」「the last frame of this film」，比写一堆形容词更能锁住连续性——Grok 对叙事指令的服从度高于对参数堆叠的服从度。
2. **每一帧都显式编号**。`FRAME 01 / 06`、`FRAME 04 / 06` 这种标记要留在提示词里。这是 Grok 保持系列感最有效的手段之一。
3. **上一帧作为输入图**。Grok 支持参考图上传；生成 FRAME N 时上传 FRAME N-1。若平台不支持图生图，就在提示词第一句写 `Continue directly from the previous frame in this conversation.`
4. **Typography 单独交代**。Grok 对中文/CJK 排版的还原较好，但要明确「物理载体」——纸片手写、墙面粉笔、雕刻，否则会变成贴上去的 UI 标签。
5. **不要一次要 6 张**。一帧一帧来。一次要 6 张 = 得到 6 张互不相关的海报。

**调用节奏**

```text
FRAME 01 / 06  纯文生图（§5）
FRAME 02 / 06  + 上传 FRAME 01（§6）
FRAME 03 / 06  + 上传 FRAME 02（§7）
FRAME 04 / 06  + 上传 FRAME 03（§8）
FRAME 05 / 06  + 上传 FRAME 04（§9）
FRAME 06 / 06  + 上传 FRAME 05（§10）
```

---

## 1. 变量表 FILL-IN SHEET

已按你的 IP 填好默认值；换 IP 时改这一列 + 全文替换英文锚点。

| 变量 | 含义 | 当前默认值（筑基猫） | 提示词里的英文锚点 |
|---|---|---|---|
| SUBJECT | 主体 | 橘猫 + 圆眼镜 | `an orange tabby cat with round glasses` |
| IDENTITY | 身份 | 用 AI 搞钱、真交付的实战派 | `an AI practitioner who actually ships and monetizes` |
| CORE ABILITY | 核心能力 | 把散落的 AI 工具收敛成一条能跑通的链路 | `turning scattered AI tools into one pipeline that actually runs` |
| VISUAL METAPHOR | 视觉隐喻 | 道场 × 工作台；散落工具碎片 + 一条刚亮起的线 | `a quiet dojo / workspace` |
| CORE MESSAGE | 核心信息 | 「101 个工具在手，不如跑通一条链路。」 | `"101 个工具在手，不如跑通一条链路。"` |
| VISUAL WORLD | 视觉世界 | 克制的当代工作室 + 东方修行感 | `restrained studio with Eastern cultivation atmosphere` |
| CORE TITLE | FRAME 01 标题 | 筑基猫｜一条链路 | `"筑基猫｜一条链路"` |
| TITLE 02 | FRAME 02 标题 | 我是怎么被定义的 | `"我是怎么被定义的"` |
| TITLE 03 | FRAME 03 标题 | 我是怎么练成的 | `"我是怎么练成的"` |
| TITLE 04 | FRAME 04 标题 | 为什么我还是我 | `"为什么我还是我"` |
| TITLE 05 | FRAME 05 标题 | 越空，越强 | `"越空，越强"` |
| TITLE 06 | FRAME 06 标题 | 101 个工具在手，不如跑通一条链路。 | `"101 个工具在手，不如跑通一条链路。"` |
| PALETTE | 核心色彩 | 冷蓝灰（左）→ 暖光（中）→ 象牙白 + 柔金（右） | `cool blue-grey → warm → ivory and soft gold` |
| ASPECT | 比例 | 3:4 竖版 | `3:4 vertical editorial frame` |

---

## 2. 六镜结构

```text
FRAME 01 / 06   MASTER       建立整个视觉世界
  ↓
FRAME 02 / 06   IDENTITY     职业 → 能力 → 隐喻
  ↓
FRAME 03 / 06   EVOLUTION    CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE
  ↓
FRAME 04 / 06   CONTINUITY   身份连续 + 动作连续 + 世界连续
  ↓
FRAME 05 / 06   ENTROPY      熵减：视觉权重重新分配
  ↓
FRAME 06 / 06   PRESENCE     最终 Hero / Banner-ready
```

**导演视角一句话**：这不是六张配图，是同一部片子的六个连续镜头，摄影机一直在同一空间里向前推。

---

## 3. 连续性契约 CONTINUITY CONTRACT（每帧都带上，可压缩成导演口吻）

### 3.1 完整版（首次或需要强约束时用）

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

### 3.2 导演压缩版（贴在每一帧开头）

```text
Same film, same cat, same world, same light.
Do not recast. Do not relocate. Do not restyle.
Advance the story by exactly one step.
```

---

## 4. Visual IP DNA（母版）

```text
VISUAL IP DNA

Subject: an orange tabby cat with round glasses
Identity: an AI practitioner who actually ships and monetizes
Core Ability: turning scattered AI tools into one pipeline that actually runs
Visual Metaphor: a quiet dojo / workspace
Core Message: "101 个工具在手，不如跑通一条链路。"
Visual World: restrained studio with subtle Eastern cultivation atmosphere

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

## 5. 主图 MASTER｜FRAME 01 / 06

```text
FRAME 01 / 06 — the opening frame.

Imagine the opening frame of a premium visual identity story.

This is NOT a single poster.
It is the first frame of one continuous six-frame narrative,
shot in a single location with a stable camera.

Aspect ratio: 3:4 vertical editorial frame.
Platform: Xiaohongshu / WeChat Xiaolvshu knowledge-card series.

SUBJECT
An orange tabby cat with round glasses.
Unmistakably recognizable:
same face, eye shape, muzzle, fur pattern, body proportions and silhouette.
This exact character must appear in all six frames.

IDENTITY
An AI practitioner who actually ships and monetizes.

CORE ABILITY
Turning one hundred scattered AI tools into a single pipeline that actually runs.

VISUAL METAPHOR
A quiet dojo crossed with a modern workspace.

CORE IDEA
"101 个工具在手，不如跑通一条链路。"

Create a sophisticated cinematic editorial scene
that establishes the entire visual universe.

The story will evolve from:

CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE

Do not show these five stages as separate characters.
The opening frame should contain the highest information density,
but everything must already belong to one coherent world:
dozens of loose tool fragments, instruments, drifting notes and
half-finished mechanisms lying around, not yet connected,
with one single luminous thread only just beginning to appear.

SCENE
A restrained contemporary studio with subtle Eastern cultivation atmosphere:
raw stone, aged wood, matte metal, paper, dust suspended in light.

CAMERA
A stable wide editorial camera. Full depth of field layering:
foreground fragments, middle-ground subject, background architecture.
Generous negative space reserved for typography.
A natural left-to-right visual direction that hints the story will travel rightward.

LIGHT
One warm controlled key light against cool blue-grey shadow.
Soft volumetric haze. At most three dominant colors.

USE
premium cinematic photography / editorial art direction,
controlled lighting,
realistic materials,
strong depth,
subtle atmosphere,
carefully designed negative space,
refined typography integrated into the environment.

TITLE
"筑基猫｜一条链路"
Typography must be a physical artifact in the world —
printed, carved, or hand-written — never a floating UI label.

The visual world, subject identity, palette, materials and lighting
must remain stable throughout the following frames.

Think of this as Frame 01 of a single long visual sequence.

AVOID
No unrelated characters. No unrelated setting. No style reset.
No five side-by-side panels. No hard vertical seams.
No numbered stage captions. No infographic layout.
No neon. No superhero glow. No giant halo. No flat lighting. No oversaturation.
```

---

## 6. 次图 01｜IDENTITY → FRAME 02 / 06

```text
FRAME 02 / 06.

Continue directly from the previous frame.
Same film, same cat, same world, same light.
Do not recast. Do not relocate. Do not restyle.

Preserve:
the same character,
the same identity,
the same visual metaphor,
the same world,
the same materials,
the same palette,
the same cinematic language,
the same camera philosophy.

Now advance the story by exactly one conceptual step:

STAGE
IDENTITY → ESSENCE → VISUAL METAPHOR

STATE CHANGE
The cat is no longer merely surrounded by tools —
it is actively working with them.
Deliberate, still exploratory gestures.

The previous state should visually lead into this state.

MOTION CHANGE
Controlled, purposeful, slightly more precise than Frame 01.

WORLD CHANGE
The same room, one increment more organized.
Structured objects, meaningful tools, environmental clues,
a clearer hierarchy. The tool fragments begin to relate to each other.
The metaphor is expressed through objects, gestures and spatial
relationships — never through literal diagrams.

INFORMATION DENSITY
Still high, but visibly more ordered than Frame 01.

AURA LEVEL
Barely perceptible. No glow, no halo, no bloom.

COMPOSITION
Same camera language as the previous frame.
Clear focal hierarchy. Negative space preserved for typography.
Keep the left-to-right directional energy.

TEXT
"我是怎么被定义的"
Optional supporting line embedded in the scene:
"101 个工具在手，不如跑通一条链路。"

The image must feel like the next frame of one continuous film.

No unrelated new character.
No unrelated setting.
No style reset.
No generic social-media template.
```

---

## 7. 次图 02｜EVOLUTION → FRAME 03 / 06

```text
FRAME 03 / 06 — the evolution frame.

Continue directly from the previous frame.
Same film, same cat, same world, same light.
Do not recast. Do not relocate. Do not restyle.

Preserve the same character, identity, visual metaphor,
world, materials, palette and cinematic language.

EVOLUTION
CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE

This is STATE TRANSFORMATION, not pose replacement.

Show ONE continuous subject moving through increasing mastery
inside one continuous space.
Traces of the earlier states remain embedded in the same world.

Do NOT stage five disconnected figures.
Do NOT create a character lineup.
Do NOT put five equal silhouettes side by side.

EVOLUTION AXES
Character maturity
Movement precision
Information reduction
Tool reduction
Spatial simplification
Aura refinement

VISUAL PROGRESSION
high complexity → organized complexity → structured clarity →
minimal environment → essential presence

MOTION
Early motion is exploratory.
Middle motion is controlled.
Late motion is extremely precise.
The final state approaches stillness.

The subject becomes calmer and more precise
while the environment becomes cleaner and more intentional.

AURA
0% → 25% → 50% → 75% → 100%
But do not make the final state brighter.
Make it purer.

LIGHT
Cool blue-grey still dominant on the left.
Warm light-trail choreography bridging the poses in the centre.

CAMERA
A long take. The camera has moved forward, not cut away.
No hard vertical seams. No panel boundaries.

TEXT
"我是怎么练成的"

The frame should communicate visually:
"change is a change of realm, not a change of pose."

No numbered captions. No infographic labels.
Same visual identity as all previous frames.
```

---

## 8. 次图 03｜CONTINUITY → FRAME 04 / 06

```text
FRAME 04 / 06 — the continuity frame.

Continue directly from the previous frame.
Same film, same cat, same world, same light.

PRIMARY CONCEPT
CONTINUITY.

Show three layers of continuity at the same time:

1. IDENTITY CONTINUITY
same face, same body proportions, same signature features,
same silhouette, same clothing language.

2. MOTION CONTINUITY
the current movement is a direct continuation of the previous movement —
the same gesture, one beat later.

3. WORLD CONTINUITY
the environment is the same world,
but more organized and more deeply understood.
Clutter → Organization → System → Architecture → Essence

Do not change the world abruptly.
The audience should feel the camera has simply kept moving forward
inside the same universe.

VISUAL BRIDGES
gesture, directional energy, objects, light,
architecture, surface materials, camera movement.

CAMERA
A strong left-to-right flow across the frame.
The previous state visually leads into the current state.
The current state implies the next state.

LIGHT
Warm visual climax in the centre.
Cool residue on the left. First hints of ivory on the right.

TEXT
"为什么我还是我"

No isolated infographic panels.
No separate character cards.
No hard visual borders between stages.
No style reset.

Same visual identity. Same cinematic language.
Same color system. Same material system. Same world.
```

---

## 9. 次图 04｜ENTROPY + WEIGHT → FRAME 05 / 06

```text
FRAME 05 / 06 — the entropy frame.

Continue directly from the previous frame.
Same film, same cat, same world, same light.

CORE IDEA
Why does a quieter frame feel stronger?

REDUCE
information
object count
tool count
movement
particles
background complexity
color complexity
typography density

INCREASE
visual clarity
subject authority
spatial breathing room
compositional precision
emotional presence

VISUAL ENTROPY (compositional principle only)
100 → 78 → 55 → 22 → 5
Do not display these numbers anywhere in the image.

VISUAL WEIGHT
Visual weight is NOT physical size.
The subject should not simply become larger.
Make it more important through space, contrast, isolation
and compositional hierarchy.

Suggested narrative weight:
CHAOS 14% / FLOW 18% / SYSTEM 28% / SILENCE 18% / PRESENCE 22%
These are compositional principles, not visible labels.

SCENE
The same world, now quiet, architectural and materially refined.
Large calm areas. Fewer objects, each more meaningful.

LIGHT
Drifting toward warm ivory and soft gold.
Reduce contrast noise. Keep one quiet luminous source.

CAMERA
Same lens philosophy, more air in the frame.
Fewer foreground elements.

TEXT
"越空，越强"
Restrained typography, embedded physically in the environment.

This frame must feel quieter than the previous frame,
yet visually stronger.

No percentages displayed. No HUD. No infographic labels.
No style reset. Same visual identity.
```

---

## 10. 次图 05｜PRESENCE → FRAME 06 / 06

```text
FRAME 06 / 06 — the final frame.

This is the culmination of the entire visual sequence.
The last frame of this film, and the hero image of the series.

Continue from the previous frame.
Same film, same cat, same world.

NARRATIVE
CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE

The subject has reached mastery through refinement.
Calm, precise, visually undeniable.

ACTION
No excessive action.
No excessive objects.
No excessive effects.
No visual clutter.

SCENE
The same world has reached its essential form:
minimal, architectural, spatially quiet,
materially refined, symbolically meaningful.

AURA
Power ↑
Visual Noise ↓
Purity ↑
Do not make this frame brighter simply to feel powerful.
Create authority through stillness, negative space, precision,
material quality and composition.

LIGHT
The left-to-right gradient resolves into warm ivory and soft gold.
Quiet luminous presence. One source. No bloom.

CAMERA
Strong cinematic horizontal flow.
Large negative space.
Clear hero zone.
Strong focal hierarchy.
Premium editorial composition.
Keep the face, head and key hands inside a banner-safe zone
away from the top and bottom edges.

This frame must work as:
1. a standalone visual,
2. a Xiaohongshu / WeChat Xiaolvshu final card,
3. a source composition that can later be adapted into an X.com Banner.

TEXT
"101 个工具在手，不如跑通一条链路。"
Typography is a physical narrative artifact, not a UI label.
Keep it faint and partially hidden in the environment.

FINAL FEELING
not spectacle, not complexity, not brightness.
Presence. Silence. Precision. Authority.

This frame must feel like the inevitable final frame
of the previous five.

No giant halo. No neon. No superhero pose.
No religious iconography. No explosive aura. No style reset.
```

---

## 11. Grok 实操 SOP 与踩坑

| 现象 | 原因 | 修正 |
|---|---|---|
| 六帧变成六张不同风格海报 | 每帧都在重新描述世界 | 每帧首行固定写 `Same film, same cat, same world, same light. Do not recast. Do not relocate. Do not restyle.` |
| 出现分镜感 / 硬竖线 | 把 CHAOS→PRESENCE 写成了分栏 | 补 `ONE continuous long take, no panels, no vertical seams` |
| 底部冒出「1.~5.」编号文案 | Grok 倾向把序列做成信息图 | 负向补 `numbered captions, infographic labels, stage numbers` |
| 英文技术词像贴上去的 UI | 未给物理载体 | 明确 `handwritten on paper / chalk on wall / engraving / reflection`，并要求随 mastery 递减 |
| 最后一张过曝 | 模型把 climax 理解成「更亮」 | 强调 `do not make it brighter, make it purer` |
| 角色漂移（毛色/眼镜变了） | 参考图未上传或编号缺失 | 上传上一帧；提示词里保留 `FRAME N / 06` 编号；把 `orange tabby cat with round glasses` 显式重述一次 |
| 中文排版崩 | 载体未指定 | 明确 `physical artifact — printed, carved, handwritten`，并要求遵守透视与景深虚化 |

**负向词（Grok 支持负向框时直接粘）**

```text
five separate character cards, character lineup, equal-sized stages,
hard vertical divisions, comic panels, infographic layout,
numbered captions, UI cards, HUD, floating text labels,
cyberpunk neon, superhero pose, giant halo, explosive magical aura, excessive golden glow,
plastic materials, 3D game asset look, cartoon mascot, chibi, kawaii,
identity drift, face drift, species drift, extra limbs, duplicate character,
watermark, logos, flat lighting, oversaturated colors
```

---

## 12. 最后一层（不要混进主图）

X Banner 的 `1500×500 / Safe Zone / Crop Simulation / Avatar Collision` 是独立的 **Banner Adapter 层**，在 FRAME 06 之后单独处理，不要写进小红书主图提示词。
