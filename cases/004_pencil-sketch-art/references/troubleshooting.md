# 出图翻车对照表

现象 → 根因 → 具体改法。改 prompt 里对应的桶，不要整段重写。

| # | 现象 | 根因 | 改法（直接追加/替换） |
|---|------|------|----------------------|
| 1 | 太像照片 | 媒介桶缺失 | 加 `visible pencil strokes, cross-hatching`；负面补 `no photorealism, no photo texture` |
| 2 | 像数字绘画 / 矢量插画 | 笔触桶缺失 | 加 `slightly wobbly lines, broken outlines, sketchbook feel` |
| 3 | 太平、没立体感 | 光影桶缺失 | 加 `single light source from upper left, strong chiaroscuro, deep shadow under the subject, cast shadow` |
| 4 | 灰蒙蒙、脏 | 明暗对比不足 | 加 `strong contrast, deep blacks in shadow, paper white reserved for highlights` |
| 5 | 出现大块鲜艳颜色 | 色彩桶失效 | 加 `monochrome graphite only` 或 `desaturated, single muted accent` |
| 6 | 背景纯白、没纸纹 | 用了 white 而不是 paper | 换成 `cream sketchbook paper, visible paper grain`；负面加 `no pure white background` |
| 7 | 文字糊成一团 / 乱码 | 图内文字过多 | **删掉全部图内文字**，出无字底图，排版环节叠加 |
| 8 | 主体太小、留白过多 | 构图未约束 | 加 `subject fills 60-70% of the frame, centered composition` |
| 9 | 背景太花抢主体 | 环境元素过多 | 加 `empty cream paper background, minimal environment, no background props` |
| 10 | 人物手部崩坏 | 模型固有问题 | 负面加 `no distorted hands, no extra fingers`；或改成手部不在画面主体（插兜/背后/特写脸部） |
| 11 | 概念图看不懂 | 隐喻物选得太绕 | 换更直白的隐喻；主体必须是**一个物件 + 一个动作**，不要塞两个隐喻 |
| 12 | 整体太"干净漂亮" | 缺少未完成感 | 加 `unfinished sketchbook edges, faint construction lines, subtle smudging` |
| 13 | 想要更狠的情绪 | 预设选错了 | 从 `hatched-tonal` 换 `charcoal-rough`，光源改 `dramatic` |
| 14 | 想要更暖 | 单色太冷 | 换 `pencil-wash` 预设 + `--accent sepia` |
| 15 | 顶部留白没留出来 | 描述里的道具（时钟/云/装饰）被放到了上方，`large empty area at the top` 被忽略 | 量化并前置：改为 `the upper third of the frame is completely empty paper, absolutely no objects, props or decoration in the top area`；负面加 `no elements in the upper third, no decoration at the top`。仍无效就把主体下压到下 2/3（`subject anchored in the lower two thirds`） |
| 16 | 明暗太弱、发灰 | 光源只有一句、缺少对比要求 | 把光照行升级为 `strong directional light from upper left, deep blacks in shadow, crisp midtone hatching, paper white as the brightest highlight` |

## 迭代原则

1. **一次只改一个桶**。同时改媒介 + 光影 + 构图，无法判断是哪个起了作用。
2. **先加正向，再加负面**。负面词是刹车，不是油门；光踩刹车不会变好。
3. **连续 2 次调整无效就换预设**，不要在同一个预设上微调第五次。
4. 文字问题**永远走排版叠加**，不要试图靠改 prompt 修。
