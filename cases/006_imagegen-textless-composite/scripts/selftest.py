#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
imagegen-textless-composite 自检 —— 装完先跑这个。

这是三个技能里外部依赖最多（Pillow + 一个中文字体）的一个，
所以自检的重点是「换台机器还能不能跑」：

  1. Python 版本 + Pillow
  2. 中文字体探测：找得到，且找到的字体真能渲染汉字（不是豆腐块）
  3. 豆腐块识别器本身准确：拿纯拉丁字体必须判 false
  4. render_card 零底图渲染出一条完整流水线
  5. 排版护栏：超长标题不得溢出画布（自动缩字号 / 均衡折行）
  6. strip_watermark 的 crop 与 patch 两种模式
  7. 输出图确实不含半透明被丢弃的痕迹（alpha 图层回归测试）

用法：
    python selftest.py
    python selftest.py --keep
    python selftest.py --font /path/to/your.ttf
"""

import os
import sys
import json
import glob
import shutil
import tempfile
import subprocess
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PY = sys.executable

results = []


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -> " + detail) if detail else ""))
    return ok


def run(args):
    p = subprocess.run([PY] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or ""), (p.stderr or "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep", action="store_true", help="保留中间产物")
    ap.add_argument("--outdir", default=None, help="中间产物目录，默认系统临时目录")
    ap.add_argument("--font", "-f", default=None)
    a = ap.parse_args()

    # 中间产物写到系统临时目录，不污染仓库、也不触发文件保护
    outdir = a.outdir or tempfile.mkdtemp(prefix="skill-selftest-ite-")
    os.makedirs(outdir, exist_ok=True)

    print("=" * 62)
    print("imagegen-textless-composite 自检")
    print("=" * 62)

    # 1 环境
    check("Python >= 3.8", sys.version_info >= (3, 8),
          "当前 %d.%d.%d" % sys.version_info[:3])
    try:
        import PIL
        check("Pillow 可用", True, "Pillow %s" % PIL.__version__)
        has_pil = True
    except ImportError:
        check("Pillow 可用", False, "pip install pillow")
        return finish(a, outdir, False)

    sys.path.insert(0, HERE)
    from find_font import pick_font, has_cjk, list_fonts  # noqa

    # 2 字体探测
    rc, so, se = run([os.path.join(HERE, "find_font.py")])
    fp = so.strip().splitlines()[-1].strip() if so.strip() else ""
    check("find_font.py 找到中文字体", rc == 0 and os.path.exists(fp),
          fp or (se or "").strip()[:90])

    if not fp:
        check("后续渲染测试", False, "无中文字体，跳过")
        return finish(a, outdir, False)
    check("找到的字体确实含汉字字形", has_cjk(fp)[0], os.path.basename(fp))

    # 3 豆腐块识别器准确性 —— 拿字体目录里的拉丁字体当反例
    latin_neg = []
    for pat in ("Bebas*", "Bangers*", "Impact*", "Arial*", "consola*"):
        hits = glob.glob(os.path.join(os.environ.get("WINDIR", r"C:\Windows"),
                                      "Fonts", pat))
        latin_neg += hits[:1]
    # 跨平台兜底：macOS/Linux 上的纯拉丁字体
    if not latin_neg:
        for d in ("/System/Library/Fonts/Supplemental", "/usr/share/fonts"):
            for pat in ("Arial*", "Impact*", "DejaVuSans.ttf", "LiberationSans*"):
                latin_neg += glob.glob(os.path.join(d, "**", pat), recursive=True)[:1]
    if latin_neg:
        wrong = [p for p in latin_neg if has_cjk(p)[0]]
        check("豆腐块识别器不误判纯拉丁字体", not wrong,
              "测试 %d 个拉丁字体，误判 %d 个" % (len(latin_neg), len(wrong)))
    else:
        check("豆腐块识别器不误判纯拉丁字体", True, "本机无纯拉丁字体样本，跳过")

    # 4 零底图渲染（端到端）
    demo = os.path.join(outdir, "demo.png")
    cmd = [os.path.join(HERE, "render_card.py"), "--demo", "-o", demo]
    if a.font:
        cmd += ["--font", a.font]
    rc, so, se = run(cmd)
    check("render_card --demo 端到端跑通", rc == 0 and os.path.exists(demo),
          (se or "").strip()[:90] if rc else "")
    if rc != 0:
        return finish(a, outdir, False)

    from PIL import Image
    im = Image.open(demo)
    check("输出尺寸 = 1080x1440", im.size == (1080, 1440), "%dx%d" % im.size)

    # 5 排版护栏：超长文案不得溢出
    spec = {
        "canvas": {"w": 1080, "h": 1440, "margin": 72, "auto_flow": True},
        "bg": {"type": "gradient", "c1": "#0E1A2E", "c2": "#070D18"},
        "blocks": [
            {"kind": "title", "x": 72, "y": 200, "size": 96, "wrap": True,
             "max_lines": 2, "gap_after": 60,
             "lines": [["这是一句特别特别长的中文标题用来测试自动缩放与均衡折行是否可靠", "ink"]]},
            {"kind": "text", "x": 72, "y": 600, "size": 30, "wrap": True, "max_lines": 4,
             "text": "Supercalifragilisticexpialidocious_and_a_very_long_english_token_"
                     "that_should_never_overflow_the_canvas_because_we_auto_fit_it"},
            {"kind": "list", "x": 72, "y": 1000, "size": 30, "gap": 62, "wrap": True,
             "items": ["这是一条很长很长的清单项需要折行处理否则会冲出画布右边界的保护",
                       "短的一条"]},
        ]
    }
    sp = os.path.join(outdir, "stress.json")
    with open(sp, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, ensure_ascii=False)
    stress = os.path.join(outdir, "stress.png")
    rc, so, se = run([os.path.join(HERE, "render_card.py"), "--spec", sp, "-o", stress])
    check("极端长文案渲染不崩", rc == 0 and os.path.exists(stress),
          (se or "").strip()[:120] if rc else "")

    if rc == 0:
        g = Image.open(stress).convert("L")
        W, H = g.size
        # 右边界 8px 内不应有非背景像素（背景是纯渐变，亮度极低）
        right = g.crop((W - 8, 0, W, H))
        rmax = right.getextrema()[1]
        check("长文案未溢出右边界", rmax < 90,
              "最右侧 8px 最大亮度 %d（背景基准 < 60）" % rmax)

    # 6 去水印
    src = stress if rc == 0 else demo
    cut = os.path.join(outdir, "cut.png")
    rc, so, se = run([os.path.join(HERE, "strip_watermark.py"), src,
                      "--mode", "crop", "--w", "90", "--h", "60", "-o", cut])
    ok = rc == 0 and os.path.exists(cut)
    check("strip_watermark crop 模式", ok, (se or "").strip()[:90] if rc else "")
    if ok:
        a0 = Image.open(src).size
        a1 = Image.open(cut).size
        check("crop 后尺寸按参数收缩", (a1[0], a1[1]) == (a0[0] - 90, a0[1] - 60),
              "%dx%d -> %dx%d" % (a0 + a1))

    pat = os.path.join(outdir, "patched.png")
    rc, so, se = run([os.path.join(HERE, "strip_watermark.py"), src,
                      "--mode", "patch", "--auto", "-o", pat])
    ok = rc == 0 and os.path.exists(pat)
    check("strip_watermark patch 模式", ok, (se or "").strip()[:90] if rc else "")
    if ok:
        check("patch 不改变画布尺寸",
              Image.open(pat).size == Image.open(src).size,
              "%dx%d" % Image.open(pat).size)

    # 7 alpha 图层回归测试：半透明卡片的四角必须没被填成实心
    sys.path.insert(0, HERE)
    from render_card import overlay as ov_fn, PALETTE
    from PIL import ImageDraw
    base_im = Image.new("RGB", (200, 100), (0, 0, 0))
    out = ov_fn(base_im, lambda od: od.rectangle((0, 0, 199, 99), fill=(255, 255, 255, 128)))
    mid = out.getpixel((100, 50))[0]
    check("半透明图层真的生效（RGB 上会被静默丢弃）",
          100 < mid < 160, "预期 ~128，实际 %d" % mid)

    return finish(a, outdir, True)


def finish(a, outdir, env_ok):
    print("-" * 62)
    fails = [n for n, ok, _ in results if not ok]
    print("通过 %d / %d" % (len(results) - len(fails), len(results)))
    if fails:
        print("失败项：")
        for f in fails:
            print("  -", f)
        print("\n结论：环境未就绪，先按上面的提示修，再重跑。")
        return 1
    print("结论：imagegen-textless-composite 就绪，可以开始出封面与卡片。")
    if not a.keep:
        shutil.rmtree(outdir, ignore_errors=True)  # 临时目录，删不掉也无妨
    else:
        print("中间产物保留在：%s" % outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
