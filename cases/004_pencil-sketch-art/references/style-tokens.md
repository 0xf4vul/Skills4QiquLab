# 风格 Token 速查

写 prompt 时从下面各桶里各取 1-3 个词，不要整桶倒进去（堆砌关键词会互相打架）。
脚本 `scripts/build_prompt.py` 已内置这套 token，手动微调 prompt 时再查这里。

## 1. 媒介桶（必备，至少 1 个）

| Token | 含义 | 适用预设 |
|-------|------|----------|
| `graphite pencil sketch` | 石墨铅笔素描 | 全部 |
| `HB / 2B / 6B pencil` | 铅笔硬度，数字越大越黑越软 | 线稿用 HB，通用 2B，重情绪 6B |
| `charcoal stick` | 炭精条，粗颗粒 | 炭笔粗粝 |
| `fine liner` | 针管笔，线均匀 | 场景速写 |
| `pencil + watercolor wash` | 铅笔淡彩 | 淡彩素描 |

## 2. 笔触桶（决定"像不像手绘"，最关键）

```
visible pencil strokes        cross-hatching / hatching
slightly wobbly lines         broken / sketchy outlines
faint construction lines      subtle pencil smudging
eraser lift-outs              unfinished sketchbook edges
```

> 出图不像手绘时，**先加这个桶的词**，不要先加负面词。

## 3. 光影桶（决定"有没有立体感"）

| Token | 效果 |
|-------|------|
| `single soft light source from upper left` | 默认，稳 |
| `dramatic single light source, high contrast` | 戏剧化，重情绪 |
| `soft diffused daylight` | 平柔，食物/家居 |
| `chiaroscuro, deep shadow under the subject` | 强明暗，主体脱离背景 |
| `cast shadow grounding the subject` | 落地，不漂浮 |
| `paper white reserved for highlights` | 用纸白当高光（素描核心） |

## 4. 纸与背景桶

```
cream sketchbook paper        off-white paper
light gray paper              textured watercolor paper
visible paper grain           empty paper background
generous negative space       paper white as highlight
```

⚠️ **禁用纯白 `#ffffff` 背景** —— 会吃掉纸纹，整张图立刻变成数字绘画。

## 5. 色彩桶

- 默认：`monochrome graphite`（炭黑 → 中灰 → 浅灰 → 纸白，四级）
- 点缀（**最多 1 个**）：`sepia` 赭石 / `muted indigo` 淡靛蓝 / `dusty red` 暗红
- 写法：`monochrome graphite with one muted sepia accent color`

## 6. 质量桶（收尾追加）

```
hand-drawn sketchbook illustration, clean composition,
balanced visual weight, editorial illustration quality
```

## 7. 负面桶（每次必带）

```
no photorealistic rendering, no 3D render, no CGI, no oil painting,
no plastic or glossy surface, no neon colors, no hard gradients,
no airbrushed smoothness, no stock photo look, no heavy digital filters,
no full saturated color, no comic-book flat color fill,
no watermark, no garbled text
```

人物图额外追加：`no distorted hands, no extra fingers`

## 8. 画幅 × size 速查

| 用途 | aspect | size |
|------|--------|------|
| 文章内嵌配图 / 头像 / 方形卡片 | `square` | 1024×1024 |
| 封面 / banner / PPT / 横版底图 | `landscape` | 1536×1024 |
| 小红书 / 手机壁纸 / 金句卡 | `portrait` | 1024×1536 |
| 横向流程图 / 全景速写 | `wide` | 1536×1024 |

## 9. 生成参数固定值

```
quality = high      # 笔触细节需要高画质
style   = natural   # 不要 vivid，会破坏石墨质感、把灰色提到饱和
```
