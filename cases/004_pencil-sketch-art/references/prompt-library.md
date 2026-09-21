# 铅笔素描 Prompt 库

六套笔触预设的「可直接复制改主体」的完整 prompt。替换 `[SUBJECT]` 即可复用。
统一结尾都带负面排除，实际使用时可保留。

---

## 1. 纯线稿速写 Line-art

适用：图标、小插图、流程图元素、装饰性小图。画幅多用方形。

```
A minimal graphite line-art sketch of [SUBJECT], contour only, no shading.
Medium: HB pencil on off-white sketchbook paper, thin broken lines,
slightly wobbly hand-drawn strokes, visible paper grain, faint construction lines left visible.
Background: empty paper, generous negative space.
Style: 30-second quick sketch feel, monochrome graphite, no fill, no shading,
no photorealistic rendering, no 3D, no color.
```

---

## 2. 排线明暗素描 Hatched tonal（默认）

适用：绝大多数配图。画幅通用。

```
A graphite pencil sketch of [SUBJECT], fully shaded with hatching and cross-hatching.
Medium: 2B graphite pencil on cream paper, dense cross-hatching in shadow areas,
sparse hatching in midtones, paper white reserved for highlights,
thick slightly imperfect outlines, visible paper grain texture, subtle smudging.
Lighting: single soft light source from upper left, clear three-tone structure
(light / midtone / shadow), cast shadow grounding the subject.
Background: mostly empty cream paper with a faint horizon line.
Style: hand-drawn sketchbook illustration, monochrome graphite,
no photorealistic rendering, no 3D, no glossy surface, no neon, no full color.
```

---

## 3. 炭笔粗粝 Charcoal rough

适用：沉重、冲突、批判性主题；人物肖像特写。

```
A rough charcoal sketch of [SUBJECT], heavy blacks and coarse grain.
Medium: charcoal stick and 6B pencil on textured paper,
broad smudged shadow masses, aggressive hatching, dusty paper grain,
edges dissolving into the paper, visible eraser lift-outs in highlight areas.
Lighting: dramatic single light source, deep dark shadows, high contrast.
Background: near-empty textured paper, a few scattered charcoal dust specks.
Style: expressive hand-drawn charcoal study, monochrome, raw and unfinished feel,
no photorealistic rendering, no 3D, no smooth airbrushed surface, no color.
```

---

## 4. 淡彩素描 Pencil + wash

适用：生活化、温暖、怀旧内容；食物、家居、旅途。

```
A pencil sketch of [SUBJECT] with a loose watercolor wash.
Medium: graphite line work with visible hatching, overlaid by one soft
[SEPIA / MUTED INDIGO / DUSTY RED] watercolor wash that bleeds outside the lines,
cream watercolor paper texture, slightly wobbly hand-drawn outlines.
Lighting: soft diffused daylight, gentle shading, paper white as highlight.
Background: pale wash fading into empty paper at the edges.
Style: hand-drawn sketchbook illustration, mostly monochrome with ONE muted accent color,
no photorealistic rendering, no 3D, no saturated color, no neon.
```

---

## 5. 建筑/场景透视速写 Urban sketch

适用：地点、空间、流程场景、建筑、街景。多用横版。

```
A hand-drawn urban sketch of [SUBJECT], one-point perspective.
Medium: fine liner and graphite pencil on cream sketchbook paper,
loose hatching for shade under eaves and objects, wobbly architectural lines,
visible paper grain, a few annotation marks and arrows in the margins.
Composition: wide 16:9, eye-level viewpoint, foreground detail fading to
simplified background shapes, small human figures for scale.
Style: travel-sketchbook illustration, monochrome graphite with light gray washes,
no photorealistic rendering, no 3D render, no photo texture, no full color.
```

---

## 6. 概念隐喻素描 Conceptual

适用：金句卡底图、观点配图、抽象主题。多用竖版或方形，留白大。

```
A conceptual graphite pencil sketch: [CONCRETE METAPHOR OBJECT + ACTION]
representing [ABSTRACT IDEA].
Medium: graphite pencil on cream paper, cross-hatched shading,
thick expressive outlines, visible paper grain, subtle smudging.
Composition: single centered subject occupying 60-70% of the frame,
large empty cream-paper area at the top for overlaid text,
minimal environment, one small symbolic prop.
Style: hand-drawn editorial illustration sketch, monochrome graphite,
generous negative space, no photorealistic rendering, no 3D,
no color, no text baked into the image.
```

> 概念转译示例：
> - 内卷 → 跑步机上原地跑的人，跑步机插着墙上狂转的钟
> - 信息茧房 → 一个人蜷在由无数小屏幕围成的茧里
> - 复利 → 一颗种子旁边画一条缓慢上升最终陡峭的曲线，曲线由铅笔排线加密表示
> - 中年承重 → 一个人肩上扛着一根被压弯的横梁，梁上是房子和老人小孩的剪影
> - 拖延 → 桌上一座沙漏，沙漏下半部被一只手按住

---

## 通用负面词块（任何预设都可附加）

```
Negative: photorealistic, photo, photograph, 3D render, CGI, oil painting,
plastic texture, glossy, neon, saturated full color, airbrushed, smooth vector look,
stock illustration, heavy gradient, lens flare, watermark, signature scrawl,
distorted hands, extra fingers, garbled text.
```

## 画幅速查

| 用途 | size |
|------|------|
| 文章内嵌配图 / 头像 / 方形卡片 | 1024×1024 |
| 封面 / banner / PPT / 横版信息图底 | 1536×1024 |
| 小红书 / 手机壁纸 / 金句卡 | 1024×1536 |
