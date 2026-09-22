# -*- coding: utf-8 -*-
"""
声明式卡片渲染器 —— 本 Skill 的「开箱验证件」。

价值：
    买家用不着先调图像模型，一条命令就能证明「底图 + 精确叠字」这条流水线
    在他自己的机器上跑得通、中文字体不崩、数字 100% 准确。
    同时它本身就是一个可复用的生产工具：改 JSON 不改代码，批量出成套卡片。

两种底图：
    bg.type = "image"    —— 用模型出的无字底图（cover 裁切 + 可选压暗）
    bg.type = "gradient" —— 纯代码生成的渐变底（零外部依赖，用于自检/兜底）

用法：
    python render_card.py --demo -o demo.png          # 内置示例，无需底图
    python render_card.py --spec card.json -o out.png # 用自定义 spec
    python render_card.py --spec card.json --font /path/x.ttf
    python render_card.py --dump-spec > card.json     # 导出示例 spec 当模板

spec 结构见 --dump-spec 输出，或 examples/demo-card.json。
"""

import os
import sys
import json
import argparse

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
except ImportError:
    sys.stderr.write("[render_card] 缺少依赖：pip install pillow\n")
    raise

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from find_font import pick_font  # noqa: E402

# ---------- 默认色板（与 SKILL.md 一致） ----------
PALETTE = {
    "deep":    (14, 26, 46),
    "deep2":   (8, 15, 29),
    "accent":  (232, 163, 61),
    "positive": (92, 214, 166),
    "ink":     (244, 246, 250),
    "muted":   (150, 168, 198),
}

DEMO_SPEC = {
    "canvas": {"w": 1080, "h": 1440, "margin": 72, "auto_flow": True},
    "bg": {"type": "gradient", "c1": "#0E1A2E", "c2": "#070D18", "grid": True,
           "glow": {"box": [120, 780, 980, 1400], "color": "#E8A33D", "alpha": 30}},
    "blocks": [
        {"kind": "pill", "x": 72, "y": 150, "text": "AI 实测 · 第 5 期", "size": 30,
         "gap_after": 60},
        {"kind": "title", "x": 72, "y": 260, "size": 92, "wrap": True, "max_lines": 2,
         "gap": 1.18, "gap_after": 72,
         "lines": [["600B MoE，只激活 27B", "ink"], ["100 万上下文，真的上桌了", "accent"]]},
        {"kind": "number", "x": 72, "y": 660, "text": "$0.71", "size": 116,
         "color": "accent", "gap_after": 26},
        {"kind": "text", "x": 72, "y": 830, "size": 31, "color": "ink", "gap_after": 72,
         "text": "单任务平均成本，是 Opus 5 的 1/8"},
        {"kind": "list", "x": 72, "y": 930, "size": 30, "gap": 64, "bullet": "accent",
         "items": ["3D 火山喷发：一次直出", "网页复刻 Windows：18 个应用",
                   "《牛来》三件套：PPT / Excel / Word"]},
        {"kind": "footer", "x": 72, "y": 1328, "size": 27, "pin": True,
         "text": "数据来源：官方技术报告 · 10 月 15 日权重开源"}
    ]
}


# ---------- 基础工具 ----------
def hex2rgb(s, default=(255, 255, 255)):
    if not s:
        return default
    s = s.lstrip("#")
    if len(s) == 3:
        s = "".join(c * 2 for c in s)
    try:
        return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))
    except Exception:
        return default


def color_of(v):
    """接受 '#RRGGBB' 或色板名，返回 RGB。"""
    if isinstance(v, str) and v.startswith("#"):
        return hex2rgb(v)
    return PALETTE.get(v, PALETTE["ink"])


def overlay(img, fn):
    """半透明元素必须画在 RGBA 图层上再合成，直接画在 RGB 上 alpha 会被静默丢弃。"""
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    fn(ImageDraw.Draw(ov))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")


def band(img, mask_fn, color=(5, 11, 22), blur=26):
    """压暗条：纯色 + 逐行 alpha mask。禁止用双色渐变，否则另一头会被刷白。"""
    w, h = img.size
    m = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(m)
    for y in range(h):
        v = mask_fn(y, w, h)
        if v:
            md.line([(0, y), (w, y)], fill=min(255, int(v)))
    return Image.composite(Image.new("RGB", (w, h), color), img,
                           m.filter(ImageFilter.GaussianBlur(blur)))


def cover(img, w, h, ax=0.5, ay=0.5):
    """等比填满裁切。ay=0 取顶部，ay=1 取底部。"""
    iw, ih = img.size
    s = max(w / iw, h / ih)
    nw, nh = int(iw * s + .5), int(ih * s + .5)
    img = img.resize((nw, nh), Image.LANCZOS)
    x, y = int((nw - w) * ax), int((nh - h) * ay)
    return img.crop((x, y, x + w, y + h))


def glow(img, box, color, alpha=26, blur=95):
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(ov).ellipse(box, fill=tuple(color) + (alpha,))
    return Image.alpha_composite(img.convert("RGBA"),
                                 ov.filter(ImageFilter.GaussianBlur(blur))).convert("RGB")


def grid(img, step=62, color=(110, 150, 210), alpha=13):
    def paint(od):
        w, h = img.size
        for x in range(0, w, step):
            od.line([(x, 0), (x, h)], fill=tuple(color) + (alpha,), width=1)
        for y in range(0, h, step):
            od.line([(0, y), (0 + w, y)], fill=tuple(color) + (alpha,), width=1)
    return overlay(img, paint)


# ---------- 渲染 ----------
# 中英混排换行：汉字可在任意处断行，拉丁单词必须整体保留，标点不出现在行首
NO_LINE_START = "，。、！？；：）】》」』%,.!?;:)]}"


class Renderer:
    def __init__(self, font_path, canvas_w):
        self.font_path = font_path
        self.base_w = canvas_w  # 用于按比例换算字号
        self._cache = {}
        self._d = ImageDraw.Draw(Image.new("RGB", (8, 8)))

    def f(self, size):
        key = int(size)
        if key not in self._cache:
            self._cache[key] = ImageFont.truetype(self.font_path, key)
        return self._cache[key]

    def width(self, text, font, sw=0):
        b = self._d.textbbox((0, 0), text, font=font, stroke_width=sw)
        return b[2] - b[0]

    def fit(self, text, size, max_w, sw=0, min_size=14):
        """字号自适应：文字超宽就逐级缩，绝不溢出画布。返回 (size, font)。"""
        size = int(size)
        while size > min_size:
            f = self.f(size)
            if self.width(text, f, sw) <= max_w:
                return size, f
            size -= 2
        return min_size, self.f(min_size)

    def wrap(self, text, size, max_w, sw=0, max_lines=6):
        """
        均衡折行（中英混排）：在 max_lines 行内，让「最长行」尽可能短。
        度量必须是 minimax（最小化最长行宽）而不是最小化总空白 ——
        后者会奖励把第一行塞满，产出「600B MoE，只激活 / 27B」这种断法。
        返回行列表。
        """
        f = self.f(size)
        tokens = self._tokenize(text)
        ws = [self.width(t, f, sw) for t in tokens]
        n = len(tokens)
        if n == 0:
            return []
        if sum(ws) <= max_w:
            return [text]

        INF = float("inf")
        # dp[i][k] = 前 i 个 token 用 k 行时，「最长行宽」的最小可能值
        dp = [[INF] * (max_lines + 1) for _ in range(n + 1)]
        prev = [[-1] * (max_lines + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for k in range(1, max_lines + 1):
            for i in range(1, n + 1):
                wsum = 0
                for j in range(i - 1, -1, -1):
                    wsum += ws[j]
                    if wsum > max_w:
                        break
                    if dp[j][k - 1] == INF:
                        continue
                    cand = max(dp[j][k - 1], wsum)
                    if cand < dp[i][k]:
                        dp[i][k] = cand
                        prev[i][k] = j

        # 选能达到最小最长行宽的最少行数
        best_k, best_v = None, INF
        for k in range(1, max_lines + 1):
            if dp[n][k] < best_v:
                best_v, best_k = dp[n][k], k
        if best_k is None:
            # 给定行数装不下：先放宽行数上限再试，最后才退回整段（交给 fit 缩字号）
            if max_lines < 12:
                return self.wrap(text, size, max_w, sw, min(12, max_lines * 2 + 2))
            return [text]

        cuts, i, kk = [], n, best_k
        while i > 0 and kk > 0:
            j = prev[i][kk]
            if j < 0:
                break
            cuts.append((j, i))
            i, kk = j, kk - 1
        cuts.reverse()

        lines = []
        for a, b in cuts:
            seg = "".join(tokens[a:b]).strip()
            # 行首禁则：标点不能落在行首，回吸到上一行
            if lines and seg and seg[0] in NO_LINE_START:
                lines[-1] += seg[0]
                seg = seg[1:]
            if seg:
                lines.append(seg)
        return lines or [text]

    @staticmethod
    def _tokenize(text):
        """汉字逐字成 token；拉丁词/数字整体成 token，保证不拆词。"""
        tokens, buf = [], ""
        for ch in text:
            if ch.isascii() and (ch.isalnum() or ch in "-_.$%/+&"):
                buf += ch
            elif ch == " " and buf:
                buf += ch
            else:
                if buf:
                    tokens.append(buf)
                    buf = ""
                tokens.append(ch)
        if buf:
            tokens.append(buf)
        return tokens

    def draw_text(self, img, xy, text, font, fill, sw=0, anchor=None):
        d = ImageDraw.Draw(img)
        d.text(xy, text, font=font, fill=fill, stroke_width=sw,
               stroke_fill=fill, anchor=anchor)


def make_bg(spec):
    c = spec["canvas"]
    w, h = c["w"], c["h"]
    bg = spec.get("bg", {}) or {}
    pal = spec.get("palette") or {}
    PALETTE.update({k: hex2rgb(v, PALETTE.get(k, (0, 0, 0)))
                    for k, v in pal.items() if isinstance(v, str)})

    if bg.get("type") == "image" and bg.get("path") and os.path.exists(bg["path"]):
        img = Image.open(bg["path"]).convert("RGB")
        img = cover(img, w, h, bg.get("ax", 0.5), bg.get("ay", 0.5))
        if bg.get("flip"):
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        if bg.get("grid"):
            img = grid(img, bg.get("grid_step", 62))
        # 顶部/底部压暗，保证叠字可读
        if bg.get("dark_top"):
            n = float(bg["dark_top"])
            img = band(img, lambda y, ww, hh: 205 * max(0.0, (n - y) / n) ** 1.25,
                       bg.get("dark_color", "#04090F") and
                       hex2rgb(bg.get("dark_color", "#04090F")), 34)
        if bg.get("dark_bottom"):
            n = float(bg["dark_bottom"])
            img = band(img, lambda y, ww, hh: 150 if y > hh - n else 0,
                       hex2rgb(bg.get("dark_color", "#050B16")), 40)
    else:
        c1 = hex2rgb(bg.get("c1", "#0E1A2E"), PALETTE["deep"])
        c2 = hex2rgb(bg.get("c2", "#070D18"), PALETTE["deep2"])
        g = Image.new("RGB", (w, 1))
        gd = ImageDraw.Draw(g)
        for y in range(h):
            t = y / max(1, h - 1)
            gd.point((0, y), fill=tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
        img = g.resize((w, h), Image.LANCZOS)
        if bg.get("grid"):
            img = grid(img, bg.get("grid_step", 62))

    gl = bg.get("glow")
    if gl:
        img = glow(img, gl["box"], hex2rgb(gl.get("color", "#E8A33D")),
                   gl.get("alpha", 26), gl.get("blur", 95))
    return img


def render(spec, font_path):
    img = make_bg(spec)
    W = spec["canvas"]["w"]
    r = Renderer(font_path, W)
    scale = W / 1080.0  # spec 里的坐标按 1080 宽基准写，自动适配其它画布
    MR = int(spec["canvas"].get("margin", 72) * scale)

    # 自动纵向流动：每个块的 y 视为「最小 y」，实际位置取 max(声明 y, 光标)。
    # 这样标题折行变高时，下面的块会被自动推开，永远不会撞在一起。
    # 需要钉死在固定位置的块（页脚、右下角角标）写 "pin": true。
    auto_flow = spec["canvas"].get("auto_flow", True)
    flow_y = 0

    for b in spec.get("blocks", []):
        kind = b.get("kind", "text")
        x = int(b.get("x", 72) * scale)
        y = int(b.get("y", 100) * scale)
        size = int(b.get("size", 30) * scale)
        avail = b.get("max_w")
        avail = int(avail * scale) if avail else (W - x - MR)

        if auto_flow and not b.get("pin"):
            y = max(y, flow_y)

        bottom = y + int(size * 1.35)  # 默认兜底

        if kind == "pill":
            txt = b["text"]
            size, f = r.fit(txt, size, avail)
            px, py = int(26 * scale), int(13 * scale)
            tw = r.width(txt, f)
            th = f.getbbox(txt)[3]
            bw, bh = tw + px * 2, th + py * 2 + int(8 * scale)
            col = color_of(b.get("color", "accent"))
            img = overlay(img, lambda od, _b=(x, y, bw, bh), _c=col: od.rounded_rectangle(
                (_b[0], _b[1], _b[0] + _b[2], _b[1] + _b[3]),
                radius=_b[3] // 2, fill=(0, 0, 0, 0), outline=_c + (175,),
                width=max(1, int(2 * scale))))
            ImageDraw.Draw(img).text((x + bw // 2, y + bh // 2 + 1), txt, font=f,
                                     fill=col, anchor="mm")
            bottom = y + bh

        elif kind == "title":
            do_wrap = bool(b.get("wrap", False))
            gap_ratio = b.get("gap", 1.15)
            cur_y = y
            for item in b["lines"]:
                if isinstance(item, (list, tuple)):
                    txt, cname = item[0], item[1]
                else:
                    txt, cname = item, "ink"
                col = color_of(cname)
                sw = max(1, int(2 * scale))

                if do_wrap:
                    sub = r.wrap(txt, size, avail, sw, b.get("max_lines", 4))
                    f = r.f(size)
                    # 折行后若仍超宽，再整体缩一档
                    longest = max(sub, key=lambda s: r.width(s, f, sw))
                    if r.width(longest, f, sw) > avail:
                        size, f = r.fit(longest, size, avail, sw)
                    line_h = int(size * gap_ratio)
                    for s in sub:
                        r.draw_text(img, (x, cur_y), s, f, col, sw=sw)
                        cur_y += line_h
                else:
                    size2, f = r.fit(txt, size, avail, sw)
                    r.draw_text(img, (x, cur_y), txt, f, col, sw=sw)
                    cur_y += int(size2 * gap_ratio)
            bottom = cur_y - int(size * (gap_ratio - 1.0) * 0.5)

        elif kind == "number":
            sw = max(1, int(3 * scale))
            _, f = r.fit(b["text"], size, avail, sw)
            r.draw_text(img, (x, y), b["text"], f,
                        color_of(b.get("color", "accent")), sw=sw)
            bottom = y + f.getbbox(b["text"])[3]

        elif kind == "list":
            gap = int(b.get("gap", 62) * scale)
            ind = int(28 * scale)
            bullet = color_of(b.get("bullet", "accent"))
            rows = []
            for it in b["items"]:
                if b.get("wrap"):
                    rows.append(r.wrap(it, size, avail - ind,
                                       max_lines=b.get("max_lines", 2)))
                else:
                    rows.append([it])
            for i, sub in enumerate(rows):
                for j, s in enumerate(sub):
                    yy = y + int(i * gap) + int(j * size * 1.2) if j else y + i * gap
                    size2, f = r.fit(s, size, avail - ind)
                    if j == 0:
                        ImageDraw.Draw(img).ellipse(
                            (x, yy + int(size2 * .38),
                             x + int(10 * scale), yy + int(size2 * .38) + int(10 * scale)),
                            fill=bullet)
                    r.draw_text(img, (x + ind, yy), s, f,
                                color_of(b.get("color", "ink")))
            bottom = y + int((len(rows) - 1) * gap) + int(size * 1.35)

        elif kind == "footer":
            _, f = r.fit(b["text"], size, avail)
            r.draw_text(img, (x, y), b["text"], f,
                        color_of(b.get("color", "muted")))
            bottom = y + f.getbbox(b["text"])[3]

        else:  # text
            sw = int(b.get("stroke", 0) * scale)
            txt = b.get("text", "")
            col = color_of(b.get("color", "ink"))
            if b.get("wrap"):
                sub = r.wrap(txt, size, avail, sw, b.get("max_lines", 4))
                f = r.f(size)
                longest = max(sub, key=lambda s: r.width(s, f, sw))
                if r.width(longest, f, sw) > avail:
                    size, f = r.fit(longest, size, avail, sw)
                lh = int(size * b.get("gap", 1.45))
                for j, s in enumerate(sub):
                    r.draw_text(img, (x, y + j * lh), s, f, col, sw=sw)
                bottom = y + (len(sub) - 1) * lh + f.getbbox(txt)[3]
            else:
                _, f = r.fit(txt, size, avail, sw)
                r.draw_text(img, (x, y), txt, f, col, sw=sw)
                bottom = y + f.getbbox(txt)[3]

        if auto_flow and not b.get("pin"):
            flow_y = bottom + int(b.get("gap_after", 46) * scale)
    return img


def main():
    ap = argparse.ArgumentParser(description="声明式卡片渲染器（底图 + 精确叠字）")
    ap.add_argument("--spec", help="卡片 spec JSON 路径")
    ap.add_argument("--demo", action="store_true", help="用内置示例 spec，无需底图")
    ap.add_argument("--font", "-f", default=None, help="字体路径，缺省自动探测")
    ap.add_argument("-o", "--out", default="card.png", help="输出路径")
    ap.add_argument("--dump-spec", action="store_true", help="打印内置示例 spec 并退出")
    a = ap.parse_args()

    if a.dump_spec:
        print(json.dumps(DEMO_SPEC, ensure_ascii=False, indent=2))
        return 0

    if a.spec:
        with open(a.spec, encoding="utf-8") as fh:
            spec = json.load(fh)
    elif a.demo:
        spec = DEMO_SPEC
    else:
        ap.error("需要 --spec 或 --demo（或用 --dump-spec 导出模板）")
        return 2

    font = pick_font(a.font)
    if not font:
        sys.stderr.write(
            "[render_card] 未找到可用中文字体。设置 SKILL_FONT=/path/x.ttf 或用 --font 指定。\n")
        return 1

    img = render(spec, font)
    out = os.path.abspath(a.out)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    img.save(out)
    sys.stderr.write("[render_card] font=%s\n[render_card] saved=%s (%dx%d)\n"
                     % (font, out, img.size[0], img.size[1]))
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
