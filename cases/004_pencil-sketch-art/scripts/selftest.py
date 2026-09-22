#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pencil-sketch-art 自检 —— 装完先跑这个。

它会：
  1. 检查 Python 版本与 Pillow 是否就位
  2. 调 build_prompt.py 出一份 prompt，校验正/负面词块齐全
  3. 造一张合成「铅笔画」（浅纸底 + 居中深色主体）喂给 crop.py，
     校验裁切结果尺寸正确、且没有把主体切掉
  4. 再造一张深色底图，校验极性自动判定生效（不反向误判）

全绿才算能交付。任何一项 FAIL 都会让退出码非 0。

用法：
    python selftest.py
    python selftest.py --keep      # 保留中间产物到 _selftest_out/
"""

import os
import sys
import shutil
import tempfile
import subprocess
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PY = sys.executable

results = []


def run(args, expect_rc=0):
    p = subprocess.run([PY] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or ""), (p.stderr or "")


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -> " + detail) if detail else ""))
    return ok


def make_sketch(path, w=800, h=800, dark_bg=False):
    """合成一张拟真铅笔画：粗颗粒纸底 + 居中椭圆主体。"""
    from PIL import Image, ImageDraw, ImageFilter
    import random
    random.seed(7)
    base = (18, 22, 30) if dark_bg else (243, 240, 232)
    ink = (200, 214, 235) if dark_bg else (46, 44, 42)
    im = Image.new("RGB", (w, h), base)
    d = ImageDraw.Draw(im)
    # 居中主体，纵向占 30%~70%
    d.ellipse((w * 0.28, h * 0.30, w * 0.72, h * 0.70), fill=ink)
    # 纸纹噪点
    px = im.load()
    for _ in range(w * h // 12):
        x, y = random.randrange(w), random.randrange(h)
        r, g, b = px[x, y]
        n = random.randint(-14, 14)
        px[x, y] = (max(0, min(255, r + n)), max(0, min(255, g + n)),
                    max(0, min(255, b + n)))
    im = im.filter(ImageFilter.GaussianBlur(1.2))
    im.save(path)
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep", action="store_true", help="保留中间产物")
    ap.add_argument("--outdir", default=None, help="中间产物目录，默认系统临时目录")
    a = ap.parse_args()

    # 中间产物写到系统临时目录，不污染仓库、也不触发文件保护
    outdir = a.outdir or tempfile.mkdtemp(prefix="skill-selftest-psa-")
    os.makedirs(outdir, exist_ok=True)

    print("=" * 62)
    print("pencil-sketch-art 自检")
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
        has_pil = False

    # 2 build_prompt
    rc, so, se = run([os.path.join(HERE, "build_prompt.py"), "--list"])
    check("build_prompt.py --list", rc == 0 and len(so) > 50,
          (se or "").strip()[:90] if rc else "列出预设成功")

    rc, so, se = run([os.path.join(HERE, "build_prompt.py"),
                      "-s", "an old typewriter on a wooden desk",
                      "-p", "hatched-tonal", "-a", "square"])
    neg_ok = "no text" in so.lower() or "no letters" in so.lower()
    ink_ok = "pencil" in so.lower()
    check("build_prompt 生成 prompt", rc == 0 and len(so) > 200,
          (se or "").strip()[:90] if rc else "%d 字符" % len(so))
    check("prompt 含负面词块（禁文字）", neg_ok)
    check("prompt 含铅笔风格词", ink_ok)

    rc, so2, se = run([os.path.join(HERE, "build_prompt.py"),
                       "-s", "test", "-p", "hatched-tonal", "--params-only"])
    check("--params-only 只输出参数", rc == 0 and "prompt" not in so2.lower()
          and len(so2) < len(so), "%d 字符" % len(so2))

    rc, so3, se = run([os.path.join(HERE, "build_prompt.py"),
                       "-s", "x", "-p", "no-such-preset"])
    check("错误预设能报错（退出码非 0）", rc != 0, "rc=%d" % rc)

    if not has_pil:
        return finish(a, outdir)

    # 3 crop：浅底
    light = make_sketch(os.path.join(outdir, "sketch_light.png"), dark_bg=False)
    rc, so, se = run([os.path.join(HERE, "crop.py"), "-i", light,
                      "-r", "2.35", "-w", "1175",
                      "-o", os.path.join(outdir, "cut_light.png")])
    from PIL import Image
    ok_rc = rc == 0 and os.path.exists(os.path.join(outdir, "cut_light.png"))
    check("crop.py 浅底裁切成功", ok_rc, (se or "").strip()[:90] if rc else "")
    if ok_rc:
        im = Image.open(os.path.join(outdir, "cut_light.png"))
        check("裁切输出尺寸正确 (1175x500)", abs(im.size[0] - 1175) <= 2
              and abs(im.size[1] - 500) <= 2, "实际 %dx%d" % im.size)
        check("极性判定为 light-bg", "light-bg" in so, so.split("\n")[1] if "\n" in so else "")
        # 主体应仍大致居中：取裁切图中心列的亮度，应明显暗于边缘
        g = im.convert("L")
        W, H = g.size
        cx = g.getpixel((W // 2, H // 2))
        edge = (g.getpixel((8, H // 2)) + g.getpixel((W - 8, H // 2))) / 2
        check("主体未丢（中心比边缘暗）", cx < edge - 20,
              "中心 %d / 边缘 %d" % (cx, edge))

    # 4 crop：深底极性
    dark = make_sketch(os.path.join(outdir, "sketch_dark.png"), dark_bg=True)
    rc, so, se = run([os.path.join(HERE, "crop.py"), "-i", dark,
                      "-r", "1", "--dry-run"])
    check("crop.py 深底极性自动纠正", "dark-bg" in so,
          [l for l in so.split("\n") if l.startswith("极性")][:1].__str__()[:80])

    return finish(a, outdir)


def finish(a, outdir):
    print("-" * 62)
    fails = [n for n, ok, _ in results if not ok]
    print("通过 %d / %d" % (len(results) - len(fails), len(results)))
    if fails:
        print("失败项：")
        for f in fails:
            print("  -", f)
        print("\n结论：环境未就绪，先按上面的提示修，再重跑。")
        return 1
    print("结论：pencil-sketch-art 就绪，可以开始出图。")
    if not a.keep:
        shutil.rmtree(outdir, ignore_errors=True)  # 临时目录，删不掉也无妨
    else:
        print("中间产物保留在：%s" % outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
