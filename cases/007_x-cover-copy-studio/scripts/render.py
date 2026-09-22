#!/usr/bin/env python3
"""x-cover-copy-studio :: render.py
Payload(JSON) -> HTML 模板填充 -> Playwright 2x 高清出图.

用法:
    python3 render.py payload.json out_dir [--playwright /path/to/playwright]

payload 关键字段:
    theme: "paper" (2000x830, 2.41:1) 或 "dark" (1600x900, 16:9)
    通用: meta_l, meta_r, save
    paper: kick, title_html, take_html, hand, specs[], corner, rows[{n,dom,desc_html}], tags[{t,hot?}]
    dark:  title_html, sub_html, watermark, ws, cards[{n,dom,desc_html}], tags[{t}], bonus{dom,desc_html} (可选)

TITLE/cards.desc_html 允许内联 HTML(如 <span class="pin">、<em>),其余为纯文本。
"""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TPL_DIR = os.path.join(HERE, "..", "templates")
SIZES = {"paper": (2000, 830), "dark": (1600, 900)}


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def fill(html, mapping):
    for k, v in mapping.items():
        html = html.replace("{{%s}}" % k.upper(), str(v))
    return html


def build_paper(p, tpl):
    rows_data = p.get("rows", [])
    if len(rows_data) > 7:
        raise SystemExit(
            "FAIL: 纸感横幅(paper)设计契约上限 7 行, 当前 %d 行。确定性优先, 不自动撑高。\n"
            "  选项 A: 改用 16:9 dark 版式(最多 7 条 + 1 张 BONUS 卡)\n"
            "  选项 B: 拆分为两张 paper(如 01-04 / 05-08...)\n"
            "  选项 C: 合并同类项压缩到 7 行" % len(rows_data))
    if p.get("specs") and len(p["specs"]) > 6:
        p["specs"] = p["specs"][:6]
        print("WARN: specs 超过 6 条, 已截断(2列x3行预算)")
    specs = "".join("<div><i>■</i>%s</div>" % s for s in p.get("specs", []))
    rows = "".join(
        '<div class="row"><div class="num mono">{n}</div><div class="dom mono">{dom}</div>'
        '<div class="desc">{desc_html}</div><div class="arr mono">{arr}</div></div>'.format(
            arr=p.get("arr", "→"), **r)
        for r in p.get("rows", []))
    tags = "".join('<span class="tag%s">%s</span>' % (" hot" if t.get("hot") else "", t["t"])
                   for t in p.get("tags", []))
    return fill(tpl, dict(META_L=p["meta_l"], META_R=p["meta_r"], KICK=p.get("kick", ""),
                          TITLE=p["title_html"], TAKE=p["take_html"], HAND=p.get("hand", "👇"),
                          SPECS=specs, CORNER=p.get("corner", ""), ROWS=rows, TAGS=tags,
                          SAVE=p["save"], SAVE_EN=p.get("save_en", "")))


def build_dark(p, tpl):
    n = len(p.get("cards", [])) + (1 if p.get("bonus") else 0)
    if n > 8:
        raise SystemExit("FAIL: 深色图鉴(dark)上限 7 条 + 1 BONUS, 当前 %d 张卡片。拆分或改用 paper。" % n)
    def bonus_row(b):
        return ('<div class="card" style="border-style:dashed;background:transparent;">'
                '<div class="n" style="background:var(--amber);">★</div>'
                '<div class="info"><div class="d" style="color:var(--amber);">{m}</div>'
                '<div class="t">{desc_html}</div></div><div class="plus">↗</div></div>').format(m=b.get("mark", "BONUS"), **b)
    cards = "".join(
        '<div class="card"><div class="n">{n}</div><div class="info"><div class="d">{dom}</div>'
        '<div class="t">{desc_html}</div></div><div class="plus">↗</div></div>'.format(**c)
        for c in p.get("cards", []))
    if p.get("bonus"):
        cards += bonus_row(p["bonus"])
    tags = "".join('<span class="tag">%s</span>' % t["t"] for t in p.get("tags", []))
    return fill(tpl, dict(META_L=p["meta_l"], META_R=p["meta_r"], TITLE=p["title_html"],
                          SUB=p["sub_html"], WATERMARK=p.get("watermark", ""),
                          WS=p.get("ws", ""), CARDS=cards, TAGS=tags, SAVE=p["save"]))


def screenshot(html_path, out_png, w, h, pw_bin):
    return subprocess.run([
        pw_bin, "screenshot",
        "--viewport-size=%d,%d" % (w * 2, h * 2),
        "--wait-for-timeout=7000",
        "file://" + os.path.abspath(html_path),
        out_png], capture_output=True, text=True)


def main():
    args = sys.argv[1:]
    if not args or "--help" in args:
        print(__doc__)
        sys.exit(0)
    payload_path = args[0]
    out_dir = args[1] if len(args) > 1 else "."
    pw = "playwright"
    if "--playwright" in args:
        pw = args[args.index("--playwright") + 1]
    p = json.loads(read(payload_path))
    theme = p.get("theme", "paper")
    tpl = read(os.path.join(TPL_DIR, "poster-%s.html" % theme))
    html = (build_paper if theme == "paper" else build_dark)(p, tpl)
    html = html.replace("</head>", "<style>body{zoom:2}</style></head>", 1)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        tmp_html = f.name
    os.makedirs(out_dir, exist_ok=True)
    out_png = os.path.join(out_dir, p.get("out", "poster-%s@2x.png" % theme))
    w, h = SIZES[theme]
    r = screenshot(tmp_html, out_png, w, h, pw)
    if r.returncode != 0 or not os.path.exists(out_png):
        print(r.stderr[-800:], file=sys.stderr)
        sys.exit(1)
    print("OK ->", out_png)


if __name__ == "__main__":
    main()
