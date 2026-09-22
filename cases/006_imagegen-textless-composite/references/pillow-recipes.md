# Pillow 叠字配方（可直接 copy 进 render.py）

全部经过实战验证。依赖 `pillow`，Python 3.8+。

> **先看这个**：如果你只是想出卡片，不要手写这些函数 —— 直接用
> `scripts/render_card.py`（声明式，改 JSON 不改代码）。
> 本文件是它的「零件清单」，供你需要定制时参考。

```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # 使 find_font 可导入
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from find_font import pick_font

# 字体不要写死绝对路径 —— 换台机器就失效。
# pick_font() 会遍历系统字体目录并校验「真的含汉字字形」（不是豆腐块）。
# 需要指定字体时，设环境变量 SKILL_FONT=/path/to/your.ttf，或传入 preferred。
FONT = pick_font()
if not FONT:
    raise SystemExit("未找到中文字体：设 SKILL_FONT=/path/to/your.ttf")

DEEP, DEEP2 = (14, 26, 46), (8, 15, 29)
ACCENT      = (232, 163, 61)
INK         = (244, 246, 250)
MUTED       = (150, 168, 198)
GREEN       = (92, 214, 166)

def F(size):
    return ImageFont.truetype(FONT, size)

def tsize(d, t, font, sw=0):
    b = d.textbbox((0, 0), t, font=font, stroke_width=sw)
    return b[2] - b[0], b[3] - b[1]

def text(d, xy, t, font, fill=INK, sw=0, anchor=None):
    """sw=1~2 即模拟加粗（stroke_fill 必须与 fill 同色，否则描边显脏）"""
    d.text(xy, t, font=font, fill=fill, stroke_width=sw, stroke_fill=fill, anchor=anchor)
```

## 0. 排版护栏（自己写渲染器时最容易漏的两条）

`render_card.py` 已经内置这两条，手写时务必自己补上 —— 否则标题一长就冲出画布。

```python
def fit(d, t, size, max_w, sw=0, min_size=14):
    """字号自适应：超宽就逐级缩，绝不溢出。返回 (size, font)"""
    while size > min_size:
        f = F(size)
        if tsize(d, t, f, sw)[0] <= max_w:
            return size, f
        size -= 2
    return min_size, F(min_size)
```

折行的度量很关键：**必须最小化「最长行宽」（minimax）**，不能最小化总空白。
后者会奖励把第一行塞满，产出「600B MoE，只激活 / 27B」这种一头沉的断法。
`render_card.py` 里的 `Renderer.wrap()` 是完整实现（DP + 行首禁则），可直接复用。

另外：标题折行后会变高，必须让后续元素跟着往下走（`render_card.py` 的 `auto_flow`），
否则就会出现「标题压住数字」这种硬伤。

## 1. 半透明元素：必须走 RGBA 图层

```python
def overlay(img, fn):
    """fn 接收一个 RGBA 画布的 ImageDraw，在里面画任何带 alpha 的东西"""
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    fn(ImageDraw.Draw(ov))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

# 用法：半透明卡片底
img = overlay(img, lambda od: od.rounded_rectangle(
    (68, 590, 1012, 790), radius=24, fill=(10, 20, 38, 224),
    outline=ACCENT + (135,), width=2))
```

⚠️ 直接在 RGB 图上 `fill=(r,g,b,a)`，alpha 会被静默丢弃，画成实心。

## 2. 压暗条 / 侧边压暗：纯色 + alpha mask

```python
def band(img, mask_fn, color=(5, 11, 22), blur=26):
    """mask_fn(y, w, h) -> 0..255；用于顶部/底部压暗，保证叠字可读"""
    w, h = img.size
    m = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(m)
    for y in range(h):
        v = mask_fn(y, w, h)
        if v:
            md.line([(0, y), (w, y)], fill=min(255, int(v)))
    return Image.composite(Image.new("RGB", (w, h), color), img,
                           m.filter(ImageFilter.GaussianBlur(blur)))

# 顶部渐变压暗（520px 内最强，往下衰减）
img = band(img, lambda y, w, h: 205 * max(0.0, (520 - y) / 520) ** 1.25, (4, 9, 18), 34)
# 底部实压暗（最后 130px）
img = band(img, lambda y, w, h: 150 if y > h - 130 else 0, (5, 11, 22), 40)

def side_dark(img, x_dark, x_clear, color=(5, 11, 22), peak=200, blur=40):
    """左侧压暗、右侧保留底图，用于「左文右图」构图"""
    w, h = img.size
    m = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(m)
    for x in range(w):
        t = max(0.0, min(1.0, 1 - (x - x_dark) / max(1, x_clear - x_dark)))
        md.line([(x, 0), (x, h)], fill=int(peak * t ** 0.9))
    return Image.composite(Image.new("RGB", (w, h), color), img,
                           m.filter(ImageFilter.GaussianBlur(blur)))
```

⚠️ 不要用「深色→白色」双色渐变来做压暗条，底部会被刷白。

## 3. cover 裁切（等比填满 + 锚点控制）

```python
def cover(img, w, h, ax=0.5, ay=0.5):
    iw, ih = img.size
    s = max(w / iw, h / ih)
    nw, nh = int(iw * s + .5), int(ih * s + .5)
    img = img.resize((nw, nh), Image.LANCZOS)
    x, y = int((nw - w) * ax), int((nh - h) * ay)
    return img.crop((x, y, x + w, y + h))
```
`ay=0` 取顶部（主体在下方），`ay=1` 取底部。拿不准就两个都试一次，**看图决定**。

## 4. 去水印

```python
def patch(img, box, feather=40):
    """box=(x0,y0,x1,y1) 框住水印；用其左上方区域的平均色 + 羽化覆盖"""
    x0, y0, x1, y1 = box
    c = img.crop((max(0, x0-160), max(0, y0-160), x0, y0)).resize((1, 1), Image.LANCZOS).getpixel((0, 0))
    layer = Image.new("RGB", (x1 - x0, y1 - y0), c)
    m = Image.new("L", (x1 - x0, y1 - y0), 255).filter(ImageFilter.GaussianBlur(feather))
    img.paste(layer, (x0, y0), m)
    return img
```
优先**裁掉**水印（横版裁宽、竖版/方形裁高），裁不掉再补。

## 5. 胶囊标签 / 网格背景 / 光晕

```python
def pill(img, x, y, label, size=28, fg=ACCENT, border=ACCENT, pad=(26, 13)):
    d0 = ImageDraw.Draw(img)
    f = F(size)
    tw, th = tsize(d0, label, f)
    w, h = tw + pad[0]*2, th + pad[1]*2 + 8
    img = overlay(img, lambda od: od.rounded_rectangle(
        (x, y, x+w, y+h), radius=h//2, fill=(255,255,255,0), outline=border+(175,), width=2))
    ImageDraw.Draw(img).text((x + w//2, y + h//2 + 1), label, font=f, fill=fg, anchor="mm")
    return img

def grid(img, step=62, color=(110,150,210), alpha=13):
    def paint(od):
        w, h = img.size
        for x in range(0, w, step): od.line([(x,0),(x,h)], fill=color+(alpha,), width=1)
        for y in range(0, h, step): od.line([(0,y),(w,y)], fill=color+(alpha,), width=1)
    return overlay(img, paint)

def glow_ellipse(img, box, color, alpha=26, blur=95):
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    ImageDraw.Draw(ov).ellipse(box, fill=color+(alpha,))
    return Image.alpha_composite(img.convert("RGBA"),
                                 ov.filter(ImageFilter.GaussianBlur(blur))).convert("RGB")
```

## 6. 镜像（主体与标题区打架时的第一选择）

```python
src = src.transpose(Image.FLIP_LEFT_RIGHT)   # 主体从左下挪到右下
```

## 7. 排版速查

| 用途 | 字号（1080 宽画布） | 颜色 |
|---|---|---|
| 主标题 | 96–112 | 辅色（关键字）/ 近白 |
| 副标题 | 40–50 | 近白 |
| 说明文字 | 27–31 | MUTED |
| 大数字 | 104–112 | 辅色 |
| 胶囊标签 | 27–30 | 辅色描边 + 辅色字 |
| 底部规格行 | 26–28 | (196,209,230) |

行距经验：主标题两行间隔 ≈ 字号 × 1.15；胶囊与标题间距 ≈ 60px。
