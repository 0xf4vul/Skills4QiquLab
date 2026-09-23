<!-- Part of Case 008 · IP Visual Evolution Engine · 个人 IP 视觉进化引擎
     This file is a self-contained platform adapter. You can run the whole
     6-frame continuous visual IP workflow using ONLY this file.
     Engine core + shared DNA/Continuity Contract: ../SKILL.md
     Other platform adapters: grok.md · gemini.md · seedream.md · gpt.md -->

# v1.3.1 · Gemini｜主图 + 次图 01–05 连续提示词

> **平台策略**：Previous Image as Primary Reference → Subject / Composition / Action / Location / Style
> **产物**：小红书 / 小绿书 3:4 竖版知识卡，6 张一镜到底的连续镜头
> **本文件独立自足**：主图 + 次图 01→05 的完整连续提示词全在这里。

---

## 0. 怎么用（Gemini 版的关键差异）

Google 官方对 Gemini 图像生成的建议非常明确，这也决定了 Gemini 版的写法：

1. **先上传上一张，再让它做下一张**。这是 Gemini 最强的连续性手段——参考图的权重比文字描述高得多。所以生成 IMAGE 02 时先上传 IMAGE 01，**再**贴提示词。
2. **给角色起固定名字**。官方明确建议给角色/对象命名。本文件统一叫这只猫 **「筑基猫」（Zhuji Mao）**。每一轮提示词里都重复这个名字——命名是 Gemini 维持主体一致的关键线索。
3. **按五维写**：`SUBJECT / COMPOSITION / ACTION / LOCATION / STYLE`。这是官方推荐的结构，不要打乱。每张图都写全五个维度，但**只在变化的那一维上改动**。
4. **明确「保持一致」清单**。Gemini 对「Keep the same: ...」从句执行得不错，每轮都带上。
5. **中文标题用引号单独一行**，并补充「让文字成为物理环境的一部分」，否则会出现莫名其妙的字体风格。

**调用节奏**

```text
IMAGE 01  纯文生图（§5）
IMAGE 02  + 上传 IMAGE 01（§6）
IMAGE 03  + 上传 IMAGE 02（§7）
IMAGE 04  + 上传 IMAGE 03（§8）
IMAGE 05  + 上传 IMAGE 04（§9）
IMAGE 06  + 上传 IMAGE 05（或 01–05 全带）（§10）
```

---

## 1. 变量表 FILL-IN SHEET

已按你的 IP 填好默认值；换 IP 时改这一列 + 全文替换英文锚点。

| 变量 | 含义 | 当前默认值（筑基猫） | 提示词里的英文锚点 |
|---|---|---|---|
| CHARACTER NAME | 角色固定名 | 筑基猫 / Zhuji Mao | `Zhuji Mao` |
| SUBJECT | 主体 | 橘猫 + 圆眼镜 | `an orange tabby cat wearing round glasses` |
| IDENTITY | 身份 | 用 AI 搞钱、真交付的实战派 | `an AI practitioner who actually ships and monetizes` |
| CORE ABILITY | 核心能力 | 把散落的 AI 工具收敛成一条能跑通的链路 | `turning scattered AI tools into one pipeline that actually runs` |
| VISUAL METAPHOR | 视觉隐喻 | 道场 × 工作台 | `a quiet dojo crossed with a modern workspace` |
| CORE MESSAGE | 核心信息 | 「101 个工具在手，不如跑通一条链路。」 | `"101 个工具在手，不如跑通一条链路。"` |
| LOCATION | 场景 | 克制的当代工作室 + 东方修行感 | `restrained contemporary studio with Eastern cultivation atmosphere` |
| CORE TITLE | 主图标题 | 筑基猫｜一条链路 | `"筑基猫｜一条链路"` |
| TITLE 02 | 次图01 标题 | 我是怎么被定义的 | `"我是怎么被定义的"` |
| TITLE 03 | 次图02 标题 | 我是怎么练成的 | `"我是怎么练成的"` |
| TITLE 04 | 次图03 标题 | 为什么我还是我 | `"为什么我还是我"` |
| TITLE 05 | 次图04 标题 | 越空，越强 | `"越空，越强"` |
| TITLE 06 | 次图05 标题 | 101 个工具在手，不如跑通一条链路。 | `"101 个工具在手，不如跑通一条链路。"` |
| PALETTE | 核心色彩 | 冷蓝灰 → 暖光 → 象牙白 + 柔金 | `cool blue-grey → warm key light → ivory and soft gold` |
| ASPECT | 比例 | 3:4 竖版 | `vertical 3:4 card` |

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

## 3. 连续性契约 CONTINUITY CONTRACT（每轮都带上）

### 3.1 完整版

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

### 3.2 Gemini 压缩版（贴在每轮末尾）

```text
Keep the same character, the same character name,
the same location, the same lighting language,
the same color palette, the same materials and the same art direction
as the previous image.
Change only the action and the state described above.
```

---

## 4. Visual IP DNA（母版）

```text
VISUAL IP DNA

Character name: Zhuji Mao
Subject: an orange tabby cat wearing round glasses
Identity: an AI practitioner who actually ships and monetizes
Core Ability: turning scattered AI tools into one pipeline that actually runs
Visual Metaphor: a quiet dojo crossed with a modern workspace
Core Message: "101 个工具在手，不如跑通一条链路。"
Visual World / Location: restrained contemporary studio with subtle Eastern cultivation atmosphere

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

```text
Create the master image for a continuous six-image visual IP story
for Xiaohongshu / WeChat Xiaolvshu knowledge cards.

The character's name is Zhuji Mao.
Always use this exact name and the same character in every following image.

SUBJECT
Zhuji Mao, an orange tabby cat wearing round glasses.
Clearly define the character's appearance: distinctive facial features,
eye shape, muzzle, fur pattern, body proportions, silhouette,
clothing and materials.
The character represents an AI practitioner who actually ships and monetizes,
whose core ability is turning one hundred scattered AI tools
into a single pipeline that actually runs.

COMPOSITION
A wide-feeling editorial composition inside a vertical 3:4 card.
Strong focal point, layered depth, controlled negative space
reserved for typography.
A natural left-to-right visual direction that implies the story will travel rightward.

ACTION
The character is in the first state of a longer evolution:
surrounded by dozens of loose tool fragments, instruments, drifting notes and
half-finished mechanisms, not yet connected,
with one single luminous thread only just beginning to appear.
This is the moment before transformation.

LOCATION
A restrained contemporary studio with a subtle Eastern cultivation atmosphere:
raw stone, aged wood, matte metal, paper, dust suspended in light.
This is the visual world that will be reused in all following images.

STYLE
Cinematic, premium editorial, sophisticated, restrained,
realistic materials, controlled color palette,
subtle cinematic lighting, high material realism.
Core palette: cool blue-grey shadows with one warm controlled key light.
No more than three dominant colors.

VISUAL METAPHOR
A quiet dojo crossed with a modern workspace.

TEXT
"筑基猫｜一条链路"
Make the text part of the physical environment —
printed, carved, or hand-written inside the scene — not a floating UI element.

This image establishes the visual identity for five subsequent images.

Keep the same:
character identity,
character name,
visual world,
lighting language,
color palette,
materials,
camera language,
and visual metaphor.

The story will evolve through:
CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE

CONTINUITY CONTRACT
This is one continuous visual IP system, not a collection of unrelated images.
Preserve the same subject identity, face, species, body proportions,
signature features, silhouette, visual metaphor, world, material language,
core color system and cinematic art direction across every image.
Only evolve: state, action, information density, tools, environment organization,
spatial complexity, aura, visual weight and narrative meaning.
Do not redesign the subject between images.
Do not reset the world between images.
Do not create six unrelated poster designs.

AVOID
Unrelated characters, unrelated environments, style resets,
collage fragmentation, five side-by-side stages,
generic AI poster aesthetics, neon, flat lighting, oversaturation.
```

---

## 6. 次图 01｜IDENTITY → IMAGE 02

> **先上传 IMAGE 01，再贴这段。**

```text
Use the previous image as the primary visual reference.

Keep the exact same main subject and visual identity.
The character is Zhuji Mao, the same orange tabby cat with round glasses.
Do not redesign the character.
Do not change the character's name.

Now create the next scene in the same visual story.

SUBJECT
Zhuji Mao, identical face, eye shape, muzzle, fur pattern,
body proportions, signature features, silhouette and clothing language.
The character embodies the identity:
an AI practitioner who actually ships and monetizes.

COMPOSITION
Same camera language and framing logic as the previous image.
Clear focal hierarchy, layered depth,
negative space preserved for typography,
left-to-right directional energy maintained.
Visual density slightly more organized than the previous image.

ACTION
Stage: IDENTITY → ESSENCE → VISUAL METAPHOR
Zhuji Mao is no longer merely surrounded by tools —
the character is actively working with them.
Deliberate, still exploratory gestures.
A clear visual relationship between the character and the environment.
The visual metaphor is expressed through objects, gestures and
spatial relationships, never through literal diagrams.

LOCATION
The same studio. The same world, one increment more organized.
Introduce structured objects, meaningful tools, environmental clues
and a clearer hierarchy.

STYLE
Same cinematic editorial system, same color language,
same material realism, same lighting logic, same visual identity.
Aura barely perceptible — no glow, no halo.

TEXT
"我是怎么被定义的"
Optional supporting line embedded in the scene:
"101 个工具在手，不如跑通一条链路。"
Make the text part of the physical environment.

Keep the same character, the same character name, the same location,
the same lighting language, the same color palette, the same materials
and the same art direction as the previous image.
Change only the action and the state described above.

The result must look like the immediate next scene in the same visual story.
No unrelated characters. No style reset. No generic social-media template.
```

---

## 7. 次图 02｜EVOLUTION → IMAGE 03

> **先上传 IMAGE 02（可同时带上 IMAGE 01），再贴这段。**

```text
Use the previous image as the primary reference.

Continue the same visual story.
The character is Zhuji Mao, the same orange tabby cat with round glasses.
Do not create a new character or a new visual world.

SUBJECT
Zhuji Mao, one continuous character progressing through increasing mastery.
Identity completely consistent with the previous image.
Evolution is state transformation, not pose replacement.

COMPOSITION
One continuous spatial narrative with a strong left-to-right flow.
Same camera language as before.
Do not place five equal figures side by side.
Do not create a character lineup.
No hard vertical seams. No panel boundaries.

ACTION
Transform the character from:
the exploratory state of the previous image
to:
a more controlled, more precise state of mastery.

Show evolution through:
- more precise movement
- fewer unnecessary tools
- clearer spatial organization
- reduced visual noise
- increased mastery

Movement progression: early motion exploratory → middle motion controlled →
late motion extremely precise → final state approaching stillness.

The narrative direction is:

CHAOS → FLOW → SYSTEM → SILENCE → PRESENCE

This image represents:
the FLOW → SYSTEM transition.

Aura: 0% → 25% → 50% → 75% → 100%
Do not make the final state brighter. Make it purer.

LOCATION
The same studio, now cleaner and more intentional.
Traces of the earlier states remain embedded in the same world.

STYLE
Warm light-trail choreography bridging the poses in the centre,
cool blue-grey still present on the left.
Same cinematic editorial system and material language.

TEXT
"我是怎么练成的"

Keep the same character, the same character name, the same location,
the same lighting language, the same color palette, the same materials
and the same art direction as the previous image.

No numbered captions. No infographic labels. No style reset.
```

---

## 8. 次图 03｜CONTINUITY → IMAGE 04

> **先上传 IMAGE 03，再贴这段。**

```text
Continue from the previous image.

Keep the exact same main subject.
The character is Zhuji Mao, the same orange tabby cat with round glasses.

SUBJECT
Zhuji Mao, same face, same body proportions, same signature features,
same silhouette, same clothing language.
Preserve the same subject identity, world and visual language.

COMPOSITION
Create a strong left-to-right visual flow.
The previous state visually leads into the current state.
The current state implies the next state.
The camera has simply moved forward inside the same universe.
No isolated infographic panels. No separate character cards.
No hard visual borders between stages.

ACTION
Focus specifically on continuity. Show:
Identity Continuity
+ Motion Continuity
+ World Continuity

The current movement should feel like a direct continuation
of the previous movement.
Use visual bridges: gesture, directional energy, objects, light,
architecture, surface materials, camera movement.

LOCATION
The environment should not suddenly change.
Instead, the same world becomes more organized
and more deeply understood.

World evolution:
Clutter → Organization → System → Architecture → Essence

STYLE
Warm visual climax in the centre,
cool residue on the left,
first hints of ivory on the right.
Same cinematic language, same materials, same color system.

TEXT
"为什么我还是我"

Keep the same character, the same character name, the same location,
the same lighting language, the same color palette, the same materials
and the same art direction as the previous image.
```

---

## 9. 次图 04｜ENTROPY + WEIGHT → IMAGE 05

> **先上传 IMAGE 04，再贴这段。**

```text
Continue from the previous image.

Keep the exact same main subject.
The character is Zhuji Mao, the same orange tabby cat with round glasses.

SUBJECT
Zhuji Mao, unchanged identity, features, proportions and silhouette.

COMPOSITION
Fewer elements, stronger hierarchy, more air in the frame.
Preserve the same camera philosophy, with less foreground clutter.
The image must feel quieter than the previous image,
yet visually stronger.

ACTION
Now reduce visual entropy.

Reduce:
objects,
tools,
movement,
particles,
background complexity,
color complexity,
typography density.

Increase:
clarity,
negative space,
compositional precision,
subject presence.

Visual entropy as a compositional principle:
100 → 78 → 55 → 22 → 5
Do not display these numbers anywhere in the image.

Visual weight is NOT physical size.
The final subject should not necessarily become larger.
Instead, make the subject more visually important through
space, contrast, isolation and compositional hierarchy.

LOCATION
The same world, now quiet, architectural and materially refined,
with large calm areas of negative space.

STYLE
Shift toward warm ivory and soft gold.
Reduce contrast noise. Keep one quiet luminous source.
Aura strong but silent — power through purity, not brightness.

TEXT
"越空，越强"
Make the text part of the physical environment.

Keep the same character, the same character name, the same location,
the same lighting language, the same color palette, the same materials
and the same art direction as the previous image.

Do not display percentages. No HUD. No infographic labels.
```

---

## 10. 次图 05｜PRESENCE → IMAGE 06

> **先上传 IMAGE 05（推荐把 IMAGE 01–05 一起带上），再贴这段。**

```text
Use all previous images as continuity references.

The character is Zhuji Mao, the same orange tabby cat with round glasses.

SUBJECT
Zhuji Mao.
Keep the same identity.
Keep the same signature features.
Keep the same silhouette.
Keep the same core visual language.

COMPOSITION
Strong cinematic horizontal visual flow,
large negative space,
clear hero zone,
strong focal hierarchy,
premium editorial composition.
Keep the face, head and key hands inside a banner-safe zone
away from the top and bottom edges.

ACTION
Create the final state:

PRESENCE.

The character has reached mastery through refinement.
No excessive action.
No excessive objects.
No excessive effects.
No visual clutter.

Reduce visual noise dramatically.

Aura:
Power ↑
Visual Noise ↓
Purity ↑

Do not make the final image brighter simply to make it feel powerful.
Instead, create authority through:
stillness,
negative space,
precision,
material quality,
composition,
and presence.

LOCATION
The same world, now in its essential form:
minimal,
quiet,
precise,
architectural,
materially refined,
symbolically meaningful.

STYLE
Resolve the left-to-right gradient into warm ivory and soft gold.
Quiet luminous presence. One light source. No bloom.
Same cinematic editorial system as the whole series.

Create a premium editorial final card
that can also serve as the source artwork for an X.com Banner.

TEXT
"101 个工具在手，不如跑通一条链路。"
Keep the text faint and partially hidden in the environment.
Typography is a physical narrative artifact, not a UI label.

FINAL FEELING
not spectacle, not complexity, not brightness.
Presence. Silence. Precision. Authority.

Keep the same character name, the same world,
the same lighting language, the same materials and the same art direction.

The image must feel like the inevitable final frame of the previous images.

No giant halo. No neon. No superhero pose. No religious iconography.
```

---

## 11. Gemini 实操 SOP 与踩坑

| 现象 | 原因 | 修正 |
|---|---|---|
| 每轮角色都换样 | 没上传上一张，或没重复角色名 | **务必先上传上一张**，并在提示词里反复写 `Zhuji Mao` |
| 五维写全了但它全改了 | 五项都描述得像新要求 | 五维照写，但只在**变化的那一维**上给新内容，其余维写 `same as the previous image` |
| 出现分栏 / 图表感 | 把 evolution 写成了列表 | 补 `one continuous scene, no panels, no infographic labels, no numbered captions` |
| 中文标题字体诡异 | 未指定文字载体 | 明确 `part of the physical environment — printed, carved, handwritten` |
| 场景突变 | LOCATION 描述过强 | 写成 `the same studio, one increment more organized` 而不是新场景 |
| 最后一张过曝 | 模型把 climax 理解成「更亮」 | 强调 `do not make it brighter, create authority through stillness and space` |
| 3:4 变方图 | 比例未声明 | 明确 `vertical 3:4 card`；漂移时补 `keep the 3:4 vertical aspect ratio` |

**Gemini 专属小技巧**

- **命名 > 形容**：`Zhuji Mao` 这个名字本身就是最强的连续性锚，比堆十个形容词有效。
- **参考图优先**：文字与参考图冲突时，Gemini 倾向参考图。所以「Keep the same」清单要写得比「Change only」短——你想改的东西写在前面更醒目。
- **多参考**：IMAGE 04 和 IMAGE 06 建议一次上传多张历史图（01+02+03 / 01–05），显著压住漂移。

---

## 12. 最后一层（不要混进主图）

X Banner 的 `1500×500 / Safe Zone / Crop Simulation / Avatar Collision` 是独立的 **Banner Adapter 层**，在 IMAGE 06 之后单独处理，不要写进小红书主图提示词。
