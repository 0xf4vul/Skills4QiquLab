---
name: pencil-sketch-art
description: "把任意主题、文字描述、概念或参考图，生成一张铅笔素描手绘风插画/配图。石墨铅笔排线、纸张纹理、手绘抖动线条、明确明暗调子，单色为主、可淡彩点缀。用于文章配图、金句卡底图、人物/物品/场景速写、概念隐喻图、封面与社媒配图。当用户说「画一张素描」「手绘配图」「铅笔风插画」「素描示意图」「pencil sketch」「sketch illustration」「pencil drawing」「给这段话配个手绘图」「画张手绘封面」时使用。硬性排除写实渲染、3D、油画、照片感、塑料质感。"
display_name: "铅笔素描手绘图"
display_name_en: "Pencil Sketch Art"
version: 1.1.0
agent_created: true
---

# 铅笔素描手绘图

把「文字 → 一张手绘素描」这件事做成独立能力。不依赖任何信息图/排版流程，单图交付。

---

## 一、先判断：这次要画什么

拿到需求后先定三件事，不要直接开写 prompt。

| 决策项 | 选项 | 默认值 |
|--------|------|--------|
| **主体** | 人物 / 物件 / 场景 / 抽象概念（需用隐喻物替代） | 按输入推断 |
| **画幅** | 方形 1024×1024（配图、头像、卡片）<br>横版 1536×1024（封面、banner、PPT 配图）<br>竖版 1024×1536（小红书、手机壁纸、金句卡）<br>宽幅 1536×1024 同上 | **1024×1024** |
| **笔触预设** | 见下方 6 选 1 | **2. 排线明暗素描** |

**抽象概念必须转译成具象物件**（素描画不出「内卷」，但画得出「跑步机上停不下来的人」）。这一步没做，出图必然是空泛的装饰画。

---

## 二、六种笔触预设（选一种，写进 prompt）

1. **纯线稿速写 Line-art** — 只有轮廓，无明暗，30 秒速写感，线条断续、有飞白。适合图标、小插图、流程图元素。
2. **排线明暗素描 Hatched tonal**（默认）— 轮廓 + 排线铺调子，三大面五大调完整，留白当高光。最通用。
3. **炭笔粗粝 Charcoal rough** — 6B/炭精条，粗颗粒、重黑、擦抹感强，情绪重。适合主题沉重的内容。
4. **淡彩素描 Pencil + wash** — 铅笔线稿 + 一层水彩淡彩（只允许 1 个色相）。适合温暖、生活化内容。
5. **建筑/场景透视速写 Urban sketch** — 有透视、有环境（街道、家具、植物）、带手绘标注线。适合地点、空间、流程场景。
6. **概念隐喻素描 Conceptual** — 单一主体 + 夸张变形 + 隐喻道具，构图中心化，留白大。适合金句卡、观点配图。

---

## 三、风格铁律（每条都必须进 prompt）

### 必须有的（正向）

```
graphite pencil sketch, hand-drawn with visible pencil strokes,
cross-hatching and hatching for shading, visible paper grain texture,
slightly wobbly imperfect hand-drawn lines, sketchbook aesthetic,
strong chiaroscuro with a single light source, white space used as highlight,
subtle pencil smudging, unfinished sketchbook edges
```

### 必须排除的（负向）

```
no photorealistic rendering, no 3D render, no CGI, no oil painting,
no plastic or glossy surface, no neon colors, no hard gradients,
no airbrushed smoothness, no stock photo look, no heavy digital filters,
no full saturated color, no comic-book flat color fill
```

### 色彩规则

- 默认**单色石墨**：炭黑 → 中灰 → 浅灰 → 纸白，四级足够。
- 需要点缀时只允许 **1 个色相 + 低饱和**：赭石（sepia）、淡靛蓝、暗红。
- 背景一律用**纸色**：cream / off-white / light gray paper，**不要纯白 #ffffff**，那会失去纸纹。

### 文字规则

图像模型渲染文字不可靠，遵守：
1. 图内文字总量 **≤ 8 个字**，且必须是 1 个短词或数字。
2. 标题用手写体（hand-lettered），不要用印刷体描述。
3. 需要大段文字时 → 出**无字底图**，文字交给排版环节叠加，不要塞进 prompt 赌模型。

---

## 四、Prompt 构造模板

主体用英文写（模型响应更稳），结构固定为五段：

```
[1] 主体 + 动作/状态 + 构图
[2] 素描媒介与笔触（从第二节选一个预设的完整描述）
[3] 光影与调子
[4] 背景与留白
[5] 风格约束 + 负面排除
```

**完整示例（概念隐喻 / 竖版 / 排线明暗）：**

```
A graphite pencil sketch of a man running on a treadmill that is plugged into a wall clock,
the clock hands spinning fast while the man stays in place, sweat drawn with short hatched strokes.
Medium: graphite pencil on cream sketchbook paper, visible cross-hatching for shading,
thick slightly wobbly outlines, paper grain texture, subtle pencil smudging at the edges.
Lighting: single soft light source from upper left, strong contrast, paper white left as highlight.
Background: mostly empty cream paper, a few light construction lines and a faint horizon line.
Style: hand-drawn sketchbook illustration, monochrome graphite with one muted sepia accent,
portrait 9:16 composition, generous negative space, no photorealistic rendering,
no 3D, no glossy surface, no neon, no full color.
```

---

## 五、执行流程

1. **解析意图** → 填好第一节的三项决策（主体/画幅/笔触）。主体缺信息就按最合理假设补，并在回复里说明「我假设了 X」。
2. **抽象概念转译** → 概念 → 具象物件 + 一个动作。
3. **构造 prompt** → 优先用脚本，别手搓：

```bash
cd scripts
python build_prompt.py --list                       # 查预设
python build_prompt.py -s "<主体英文描述>" -p <1-6|key|中文名> -a <square|landscape|portrait|wide> \
                       [--accent none|sepia|indigo|red] [--light upper-left|upper-right|dramatic|diffuse] \
                       [-t "≤8字"] [-o prompt.txt]
```

脚本输出「生成参数 JSON + 完整 prompt」，直接拿去生成即可；`--accent` 会同时改 Style 段的色彩规则，`-t` 超过 8 字会直接报错拦下。
需要精细微调时再按第四节模板手改，token 参考 `references/style-tokens.md`。

4. **生成** → 调用图片生成能力；`size` 取脚本输出的 `size`；`quality=high`；`style=natural`（不要 vivid，会破坏铅笔质感）。
5. **裁切成发布尺寸** → 生成尺寸只有 1024²/1536×1024/1024×1536 三种，交付到具体平台前用 `crop.py` 裁：

```bash
python crop.py --in raw.png --ratio 2.35 --bottom-safe 0.26 --out cover.png
python crop.py --in raw.png --ratio 2.35 --width 900 --out cover-900.png
python crop.py --in raw.png --ratio 0.75 --top-safe 0.18 --width 1080 --out xhs.png
python crop.py --in raw.png --ratio 2.35 --dry-run     # 只看墨量剖面与裁切决策，不落盘
```

`--bottom-safe` / `--top-safe` 是两端必须保留的空白比例，用于叠加标题（横版封面叠底部，竖版首图叠顶部）。
`crop.py` 靠**每行的平均墨量**定位主体，因此**看不到图也能安全裁**——这一点在无法读图的会话里尤其关键，禁止凭 prompt 语义猜构图。

同一套思路还能反着用：**打印墨量剖面找「干净带」**，就能知道标题该叠在百分之几的高度，而不是拍脑袋放顶部。
（`--dry-run` 会打印每 1/12 高度的墨量柱状图，主体偏上偏下、留白够不够一目了然。）

常用发布比例：公众号封面 **2.35**（900×383）· 公众号正文图 **3:2 或 16:9，宽 ≤1080** · 小绿书 / 小红书 **3:4**（1080×1440）· 视频号封面 **9:16** · 金句卡 **2:3**。

6. **自检 + 迭代** → 过一遍下方清单；不合格查 `references/troubleshooting.md` 对号入座改，不要凭感觉重写。

### 工程目录

```
pencil-sketch-art/
├── SKILL.md                    入口（本文件）
├── README.md / CHANGELOG.md / LICENSE / _meta.json
├── references/  prompt-library.md · style-tokens.md · troubleshooting.md
├── scripts/     build_prompt.py · presets.json · crop.py
└── examples/    01-concept-metaphor · 02-column-illustration · 03-urban-scene · 04-quote-card-series
```

只有需要改预设数据（新增笔触、调整负面词块）时才动 `scripts/presets.json`，改完跑一次 `--list` 验证。
`crop.py` 依赖 Pillow + numpy（已装在 `~/.workbuddy/binaries/python/envs/default`）。

---

## 六、出图自检清单（8 条）

- [ ] 一眼能看出是**铅笔/炭笔**画的，不是数字绘画
- [ ] 能看见**排线**或笔触方向，不是平滑色块
- [ ] 有明确**光源和调子**，不是平涂线稿
- [ ] **纸纹**可见，背景是纸色不是纯白
- [ ] 线条**略有抖动/断续**，不是矢量般完美
- [ ] 无塑料感、无 3D 渲染、无油画笔触
- [ ] 色彩 ≤ 1 个色相（或全单色）
- [ ] 图内文字 ≤ 8 字且没有错别字/乱码

---

## 七、常见返工与修法

| 问题 | 修法 |
|------|------|
| 太像照片 | 加 `visible pencil strokes`、`cross-hatching`；负面加 `no photorealism` |
| 太平、没立体感 | 补 `single light source from upper left, strong chiaroscuro, deep shadow under the object` |
| 线条太干净像矢量 | 加 `slightly wobbly lines, broken outlines, sketchbook feel` |
| 出现大块鲜艳颜色 | 加 `monochrome graphite only` 或 `desaturated, single muted accent` |
| 文字糊成一团 | 删掉图内文字，改出无字底图 |
| 主体太小、留白太多 | 加 `subject fills 70% of the frame, centered composition` |
| 背景太花抢主体 | 加 `empty cream paper background, minimal environment` |

---

## 八、独立运行说明

本技能不依赖其他任何技能，输入一段话即可出图。
如需把金句做成卡片图，可先由文本侧产出文案，再用本技能出**无字底图**叠加。
本技能源自手绘信息图体系中的「手绘风格层」，已剥离所有排版/构图/信息图约束，可单独调用。
