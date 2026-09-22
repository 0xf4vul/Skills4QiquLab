#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
按目标比例智能裁切生成图 —— 看不见图也能安全裁。

原理：铅笔画是纸色底 + 石墨墨迹，用「每行的平均墨量」就能定位主体在纵向的位置，
从而决定裁切窗口，避免把主体切掉或把留白带切没了。

用法:
  python crop.py --in raw.png --ratio 2.35 --out cover.png
  python crop.py --in raw.png --ratio 2.35 --width 900 --out cover-900.png
  python crop.py --in raw.png --ratio 2.35 --bottom-safe 0.28 --out cover.png
  python crop.py --in raw.png --ratio 2.35 --dry-run          # 只打印墨量剖面与裁切决策

参数:
  --ratio        目标 宽/高，如 2.35(公众号封面) / 1.78(16:9) / 1(方形) / 0.75(3:4竖版)
  --width        输出宽度（可选，等比缩放）
  --bottom-safe  底部必须保留的空白比例（相对输出高度），用于叠加标题，默认 0.0
  --top-pad      主体上方额外保留的空白像素，默认 40
  --dry-run      只分析不落盘
"""

import argparse
import os
import statistics
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("需要 Pillow：pip install pillow")


def ink_profile(path):
    """
    返回 (W, H, row_ink, col_ink, polarity)。

    用 Pillow 的 BOX 缩放求「整行/整列平均」——等价于 numpy 的 mean(axis)，
    但省掉 numpy 依赖，让本技能只需要 Pillow 一个包。

    极性自动判定：铅笔画是「浅纸底 + 深墨迹」，但深色底图（如深蓝海报）
    必须反过来算。这里用整图亮度中位数判断：亮底取 255-L（越暗越有墨），
    暗底取 L（越亮越有内容）。否则深底图会被判成「整幅全是主体」。
    """
    im = Image.open(path).convert("L")
    W, H = im.size
    row_img = im.resize((1, H), Image.BOX)
    col_img = im.resize((W, 1), Image.BOX)

    lum = [row_img.getpixel((0, y)) for y in range(H)]
    dark_bg = statistics.median(lum) < 128.0

    if dark_bg:
        row = [row_img.getpixel((0, y)) / 255.0 for y in range(H)]
        col = [col_img.getpixel((x, 0)) / 255.0 for x in range(W)]
        polarity = "dark-bg (明亮处视为内容)"
    else:
        row = [(255.0 - row_img.getpixel((0, y))) / 255.0 for y in range(H)]
        col = [(255.0 - col_img.getpixel((x, 0))) / 255.0 for x in range(W)]
        polarity = "light-bg (暗处视为内容)"
    return W, H, row, col, polarity


def content_span(profile, k=0.30):
    """用背景中位数做基准，避免把纸纹误判成墨迹。"""
    bg = statistics.median(profile)
    mx = max(profile)
    thr = bg + (mx - bg) * k
    idx = [i for i, v in enumerate(profile) if v > thr]
    if not idx:
        return 0, len(profile) - 1, bg, mx
    return idx[0], idx[-1], bg, mx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", "-i", dest="inp", required=True, help="源图路径")
    ap.add_argument("--ratio", "-r", type=float, required=True, help="目标 宽/高")
    ap.add_argument("--out", "-o", default="", help="输出路径（--dry-run 时可省）")
    ap.add_argument("--width", "-w", type=int, default=0, help="输出宽度，等比缩放")
    ap.add_argument("--bottom-safe", type=float, default=0.0)
    ap.add_argument("--top-safe", type=float, default=0.0, help="顶部必须保留的空白比例，用于顶部叠加标题")
    ap.add_argument("--top-pad", type=int, default=40)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(args.inp):
        sys.exit("找不到文件: %s" % args.inp)

    W, H, row, col, polarity = ink_profile(args.inp)
    top, bot, bg, mx = content_span(row)

    # 目标框：在原始尺寸内取满足比例的最大框
    if W / float(H) >= args.ratio:      # 原图偏宽 → 裁宽度
        tw = int(round(H * args.ratio))
        th = H
    else:                                # 原图偏高 → 裁高度
        tw = W
        th = int(round(W / args.ratio))

    safe_b = int(round(th * args.bottom_safe))
    safe_t = int(round(th * args.top_safe))
    content_h = bot - top + 1

    if content_h + safe_t + safe_b <= th:
        # 顶部安全区 + 主体 + 底部安全区都装得下：富余空间再补一点到主体上方
        spare = th - content_h - safe_t - safe_b
        start = top - safe_t - min(args.top_pad, spare)
    elif content_h <= th - safe_b:
        # 顶部留白放不下，优先保住主体完整（裁掉的是上方空白）
        start = max(top - safe_t, bot + safe_b - th)
    else:
        # 主体装不下：以主体中心对齐，尽量保住视觉重心
        start = (top + bot) // 2 - th // 2
        start = max(0, min(start, H - th))
    start = max(0, min(start, H - th))

    # 横向：内容居中
    c_left, c_right, _, _ = content_span(col)
    cx = (c_left + c_right) // 2
    left = max(0, min(cx - tw // 2, W - tw))

    print("源图 %dx%d  目标比例 %.2f  目标框 %dx%d" % (W, H, args.ratio, tw, th))
    print("极性: %s" % polarity)
    print("墨量: bg=%.3f max=%.3f  主体纵向 %d-%d (高 %d)" % (bg, mx, top, bot, content_h))
    print("决策: 裁切窗口 x=%d..%d  y=%d..%d  顶部留白 %dpx / 底部留白 %dpx" % (
        left, left + tw, start, start + th, max(0, top - start), max(0, (start + th) - bot)))
    if content_h + safe_t + safe_b > th:
        print("  ⚠ 主体 %dpx + 安全区 %dpx > 窗口 %dpx，已优先保住主体完整" % (content_h, safe_t + safe_b, th))
    if safe_b and (start + th) - bot < safe_b:
        print("  ⚠ 实际底部空白 %dpx < 要求 %dpx，主体可能被底部标题压住" % ((start + th) - bot, safe_b))
    if safe_t and top - start < safe_t:
        print("  ⚠ 实际顶部空白 %dpx < 要求 %dpx，主体可能被顶部标题压住" % (top - start, safe_t))

    if args.dry_run:
        step = max(H // 12, 1)
        print("--- 纵向墨量剖面 ---")
        for i in range(0, H, step):
            seg = sum(row[i:i + step]) / max(1, len(row[i:i + step]))
            bar = "#" * int((seg - bg) / max(mx - bg, 1e-6) * 40)
            print("  %4d %-40s %.3f" % (i, bar, seg))
        return

    if not args.out:
        sys.exit("需要 --out 或用 --dry-run")

    im = Image.open(args.inp).convert("RGB").crop((left, start, left + tw, start + th))
    if args.width and args.width != tw:
        im = im.resize((args.width, int(round(args.width / args.ratio))), Image.LANCZOS)
    im.save(args.out)
    print("已保存 %s  %dx%d  %.0f KB" % (args.out, im.size[0], im.size[1], os.path.getsize(args.out) / 1024.0))


if __name__ == "__main__":
    main()
