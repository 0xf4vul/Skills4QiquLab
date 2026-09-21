# 案例 02 · 观点文配图 → 中年承重

## 需求
「一篇中年公众号文章的配图，情绪偏沉，方形。」

## 六秒决策
- **主体**：抽象概念 → **一个人肩扛被压弯的横梁，梁上是房子与老人小孩的剪影**
- **画幅**：文章内嵌 → `square` 1024×1024
- **笔触**：情绪沉 → `charcoal-rough`（第 3 号），光源自动落到 `dramatic`

## 命令
```bash
python build_prompt.py \
  --subject "a man carrying a sagging beam on his shoulders, silhouettes of a house and two small figures sitting on top of the beam" \
  --preset charcoal-rough --aspect square
```

## 生成的 prompt（节选关键段）
```
Medium: charcoal stick and 6B pencil on textured paper, broad smudged shadow masses,
aggressive hatching, dusty paper grain, edges dissolving into the paper, visible eraser
lift-outs in highlight areas.
Shading: dramatic high contrast, deep dark shadows, dramatic single light source, deep
dark shadows, high contrast.
Composition/background: near-empty textured paper, a few scattered charcoal dust specks,
raw and unfinished feel, square composition.
```

## 生成参数
`size=1024x1024` · `quality=high` · `style=natural`

## 关键点
- 沉重主题**不要用淡彩**，用了会稀释情绪
- `charcoal-rough` 默认光源就是 dramatic，不用手动加
- 剪影（silhouettes）是素描里最稳的处理方式：既避开人物面部崩坏，又有分量

## 常见返工
若出图「太黑看不清主体」→ 只改一个桶：把 `deep dark shadows` 换成
`deep shadows with visible midtone hatching`，保留炭笔颗粒。
