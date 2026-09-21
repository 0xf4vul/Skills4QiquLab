# 案例 01 · 概念隐喻 → 金句卡底图

## 需求
「给『内卷』这个概念画一张金句卡底图，竖版。」

## 六秒决策
- **主体**：抽象概念 → 转译为具象物件。内卷 = 拼命努力但不前进 → **跑步机上原地跑的人 + 跑步机插着墙上狂转的钟**
- **画幅**：金句卡 → `portrait` 1024×1536
- **笔触**：观点配图 → `conceptual`（第 6 号）

## 命令
```bash
python build_prompt.py \
  --subject "a man running on a treadmill, the treadmill plugged into a wall clock whose hands are spinning fast, sweat drawn with short hatched strokes" \
  --preset conceptual --aspect portrait
```

## 生成的 prompt
```
A graphite pencil sketch of a man running on a treadmill, the treadmill plugged into a wall clock whose hands are spinning fast, sweat drawn with short hatched strokes.

Medium: graphite pencil on cream paper, cross-hatched shading, thick expressive outlines, visible paper grain, subtle smudging.
Shading: single light source, strong contrast, deep shadow under the subject.
Composition/background: single centered subject occupying 60-70% of the frame, large empty cream-paper area at the top for overlaid text, minimal environment, one small symbolic prop, portrait 9:16 composition.
Style: hand-drawn sketchbook illustration, clean composition, balanced visual weight, editorial illustration quality, monochrome graphite, background cream / off-white / light gray paper (never pure white #ffffff), no photorealistic rendering, no 3D render, no CGI, no oil painting, no plastic or glossy surface, no neon colors, no hard gradients, no airbrushed smoothness, no stock photo look, no heavy digital filters, no full saturated color, no comic-book flat color fill, no watermark, no garbled text.
Text: no text baked into the image.
```

## 生成参数
`size=1024x1536` · `quality=high` · `style=natural`

## 关键点
- **没有把「内卷」两个字写进图**——文字走排版叠加，模型渲染中文极易糊
- 隐喻只保留**一个主体 + 一个动作**，没有同时塞「沙漏」「齿轮」第二个隐喻
- 顶部留白是刻意的：给标题文字预留位置

## 后续
底图出完 → `golden-quote-miner` 出的金句在排版环节叠加到顶部留白区 → 成品金句卡。
