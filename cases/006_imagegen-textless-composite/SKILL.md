---
name: imagegen-textless-composite
description: "生成带中文大字的封面/卡片/海报/社媒图：先让图像模型出一张完全无字的底图，再用 Pillow 把中文文案精确叠加在图上。用于公众号封面、小红书/小绿书主图与细节卡、海报大字报、金句卡、数据结论卡、教程步骤卡。当用户说「做张封面」「出套竖版卡片」「大字报排版」「图上要有 44 分 / $0.71 这种数字」「中文标题别让模型画」「避免 AI 字体崩坏」时使用。硬性排除：直接让模型渲染中文大字。"
display_name: "无字底图 + 精确叠字出图法"
display_name_en: "Textless Backdrop + Precise Type Overlay"
version: 1.1.0
agent_created: true
derived_from: 2026-09-22 公众号→小绿书物料包实战（wechat-xiaolushu-material-pack 跑通后提纯）
---

# 无字底图 + 精确叠字出图法

一句话：**模型负责画面，脚本负责文字。**

让图像模型渲染中文大字，结果必然是崩字、缺笔画、多字少字、数字错。而封面上的数字（$0.71、44 分、¥0.35）错一个就是硬伤。
所以分工必须是：模型只出「没有任何文字的底图/氛围图」，全部中文和数字由 Pillow 叠加。这样数字 100% 准确、字体永远不崩、配色能精确锚定账号色板。

---

## 一、什么时候必须用这套

| 场景 | 判断 |
|------|------|
| 图上有中文标题 / 副标题 | ✅ 必须 |
| 图上有关键数字（价格、分数、百分比） | ✅ 必须 |
| 成套卡片（主图 + 2 张细节卡）需要统一配色 | ✅ 必须 |
| 纯氛围插图、无字素描、抽象纹理 | ❌ 不需要，直接出图 |
| 图内只有 ≤8 字的短词 | ⚠️ 可选，但更推荐叠字 |

---

## 二、五步流程

### 第 1 步 · 定色板（先于出图）

出图前先锁死 4 个值，全套物料共用：

```
主色（底）    #0E1A2E 深蓝 / 或账号既有底色
辅色（强调）  #E8A33D 琥珀金
点缀（正向）  #5CD6A6 薄荷绿 —— 只用于「优势/结论」
文字          #F4F6FA 近白，次级用 #96A8C6
```

**色板要写进出图 prompt**，否则模型配色会跑偏，叠上去的字就压不住。
已有账号色板就直接用，不要每次从参考库重新提炼。

### 第 2 步 · 出无字底图（ImageGen）

prompt 三段式：**主体描述 + 场景氛围 + 质感风格**，末尾**必须**带负面词块。

```
Cinematic wide tech hero background, deep midnight navy blue (#0E1A2E) gradient.
A long minimalist dark banquet table floating in a void, seen at a slight angle.
Along the tabletop runs a single thin glowing amber-gold (#E8A33D) curve.
Volumetric haze, faint blueprint grid, soft rim light, ultra clean,
high-end keynote visual, subtle depth of field.
Absolutely no text, no letters, no words, no numbers, no watermark, no logo.
```

负面词块**不可省略**（这是本套方法的地基）：
```
Absolutely no text, no letters, no words, no numbers, no watermark, no logo.
```

画幅按发布位选：`1536x1024`（横版封面）/ `1024x1024`（方形插图）/ `1024x1536`（竖版卡片），`quality=high`。

### 第 3 步 · 去水印（必做）

模型输出**右下角固定带「AI生成 <品牌>」水印**，不处理就是废图。两法：

- **能裁就裁**：水印在右下角约 90×60 px。横版 1536 宽 → 裁到 1356 宽即可整块带掉；竖版/方形用纵向裁切带掉。
- **裁不掉就补**：取水印左上方一块区域求平均色，配高斯模糊 mask 局部覆盖（见 `scripts/strip_watermark.py`）。

### 第 4 步 · 叠字（Pillow）

字体用本地字体文件（如霞鹜文楷 `LXGWWenKai.ttf`），**加粗靠 `stroke_width=1~2` + `stroke_fill=fill` 模拟**，不要找 bold 字体文件。

排版范式（大字报）：
- 左对齐、单行 **≤ 11 字**，关键字整段换成辅色
- 标题下压一条 4px 辅色短线当分隔
- 数字单独成大字块，单位/说明用次级色小字
- 底部 CTA 用实心辅色块 + 深色字，对比最强

完整可复制的工具函数见 `references/pillow-recipes.md`（`overlay` / `band` / `side_dark` / `cover` / `pill` / `text`）。

### 第 5 步 · 校验

- [ ] 图上每个数字都能在原文里找到出处
- [ ] 字号 ≥ 24px，正文区与底图亮部对比足够（必要时压暗条）
- [ ] 成套物料：同底色、同辅色、同字体、同隐喻
- [ ] 水印已清干净

---

## 三、三个必踩的坑（都已实测翻车过）

### 1. RGB 图上画半透明 = 静默失效

```python
draw.rounded_rectangle(box, fill=(232,163,61,26))   # ✗ alpha 被忽略，画成实心
```
后果：叠在色块上的字看不见，或色块死板。

**正解**：所有带 alpha 的元素画在独立 RGBA 图层上再合成。
```python
def overlay(img, fn):
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    fn(ImageDraw.Draw(ov))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
```

### 2. 双色渐变当压暗条用，会把另一头刷白

`vgrad(top, bottom)` 若 `bottom` 传白色，底部整片变白。
**压暗条一律用「纯色 + 逐行 alpha mask」**：
```python
def band(img, mask_fn, color=(5,11,22), blur=26):
    m = Image.new("L", img.size, 0)
    md = ImageDraw.Draw(m)
    for y in range(img.size[1]):
        md.line([(0,y),(img.size[0],y)], fill=min(255,int(mask_fn(y,*img.size[::-1]))))
    return Image.composite(Image.new("RGB", img.size, color), img, m.filter(ImageFilter.GaussianBlur(blur)))
```

### 3. 底图主体与标题区打架 → 用镜像，别重出图

底图主体在左下、标题要放左上时，一步解决：
```python
src = src.transpose(Image.FLIP_LEFT_RIGHT)
```
主体挪到右下，左上自然留白。比重生成便宜得多。

---

## 四、环境

managed Python 3.13 默认**没有 Pillow**。用已配好的 venv：

```bash
C:/Users/Administrator/.workbuddy/binaries/python/envs/default/Scripts/python.exe render.py
```
安装：`python -m venv <envs/default>` → `pip install pillow`（走代理 `http://127.0.0.1:7890`）。

---

## 五、交付形态

成套交付时按这个数量出，够用且不过度：

| 端 | 图 | 比例 | 尺寸 |
|---|---|---|---|
| 公众号 | 主图 | 16:9 | 1600×900 |
| 公众号 | 插图 ×2 | 1:1 | 1080×1080 |
| 小绿书/小红书 | 主图 | 3:4 | 1080×1440 |
| 小绿书/小红书 | 细节卡 ×2 | 3:4 | 1080×1440 |

配套产物：`render.py`（改参数即可复跑，禁止手改图）+ `raw/`（原始底图）+ 一张验收 HTML。
