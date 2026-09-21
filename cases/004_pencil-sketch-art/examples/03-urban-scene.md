# 案例 03 · 场景速写 → 老巷咖啡馆

## 需求
「画一张老巷子里的咖啡馆，做公众号封面，横版，想带点暖色。」

## 六秒决策
- **主体**：具体场景（不是抽象概念，不需要隐喻转译）
- **画幅**：封面 → `landscape` 1536×1024
- **笔触**：有透视、有环境 → `urban-sketch`（第 5 号）；要暖 → 叠加 `--accent sepia`

## 命令
```bash
python build_prompt.py \
  --subject "a small corner cafe in an old alley, awning, two round tables on the sidewalk, a bicycle leaning on the wall" \
  --preset urban-sketch --aspect landscape --accent sepia
```

## 生成参数
`size=1536x1024` · `accent=sepia` · `quality=high` · `style=natural`

## 关键点
- 场景速写默认带**小人物做尺度参照**（`small human figures for scale`），别删，删了空间感会塌
- 点缀色只加在 Style 段末尾：`monochrome graphite with one muted sepia accent color`，不会覆盖单色基调
- 横版封面要注意：标题通常在左或上方，可用 `--light upper-right` 把视觉重心让出来

## 常见返工
| 现象 | 改法 |
|------|------|
| 建筑线太直、像 CAD | 加 `wobbly architectural lines, hand-drawn perspective` |
| 招牌上出现乱码字 | 负面加 `no text on signs, blank signage` |
| 环境元素太杂乱 | 加 `simplified background shapes, only three foreground objects` |
