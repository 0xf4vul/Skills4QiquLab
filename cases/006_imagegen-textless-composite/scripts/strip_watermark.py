# -*- coding: utf-8 -*-
"""
strip_watermark.py —— 清掉文生图右下角的「AI生成 <品牌>」水印

两种模式：
  crop   裁掉右下角（横版裁宽 / 竖版裁高），最干净，优先用
  patch  用周边平均色 + 羽化 mask 局部覆盖，裁不掉时用

用法：
  python strip_watermark.py in.png --mode crop  --w 90 --h 60 -o out.png
  python strip_watermark.py in.png --mode patch --box 670,830,1024,1024 -o out.png
  python strip_watermark.py in.png --mode patch --auto -o out.png     # 自动按右下角 20% 估算
"""
import argparse
import os
import sys

from PIL import Image, ImageFilter


def do_crop(img, w, h):
    iw, ih = img.size
    # 裁掉右下角 w x h
    return img.crop((0, 0, iw - w, ih - h))


def do_patch(img, box, feather=40, sample=160):
    x0, y0, x1, y1 = box
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(img.size[0], x1), min(img.size[1], y1)
    if x1 <= x0 or y1 <= y0:
        raise SystemExit("box 无效，检查坐标是否在图内")
    # 取水印块左上方的干净区域求平均色
    sx0, sy0 = max(0, x0 - sample), max(0, y0 - sample)
    patch_ref = img.crop((sx0, sy0, max(sx0 + 1, x0), max(sy0 + 1, y0)))
    if patch_ref.size[0] < 1 or patch_ref.size[1] < 1:
        raise SystemExit("取样区为空，改用 --box 手动指定或先 crop")
    color = patch_ref.resize((1, 1), Image.LANCZOS).getpixel((0, 0))

    pw, ph = x1 - x0, y1 - y0
    layer = Image.new("RGB", (pw, ph), color)
    mask = Image.new("L", (pw, ph), 255).filter(ImageFilter.GaussianBlur(feather))
    img = img.copy()
    img.paste(layer, (x0, y0), mask)
    return img


def main():
    ap = argparse.ArgumentParser(description="清除文生图右下角水印")
    ap.add_argument("input")
    ap.add_argument("--mode", choices=["crop", "patch"], default="crop")
    ap.add_argument("--w", type=int, default=90, help="crop 模式：从右侧裁掉的像素宽度")
    ap.add_argument("--h", type=int, default=60, help="crop 模式：从底部裁掉的像素高度")
    ap.add_argument("--box", type=str, default="", help="patch 模式：x0,y0,x1,y1")
    ap.add_argument("--auto", action="store_true", help="patch 模式：按右下角 20%% 自动估算 box")
    ap.add_argument("--feather", type=int, default=40)
    ap.add_argument("-o", "--out", default="", help="输出路径，默认 <原名>_clean.png")
    a = ap.parse_args()

    if not os.path.exists(a.input):
        raise SystemExit("文件不存在: " + a.input)

    img = Image.open(a.input).convert("RGB")
    print("源图:", img.size)

    if a.mode == "crop":
        if a.w >= img.size[0] or a.h >= img.size[1]:
            raise SystemExit("裁掉的尺寸超过原图，请调小 --w/--h")
        out = do_crop(img, a.w, a.h)
    else:
        if a.box:
            box = tuple(int(v) for v in a.box.split(","))
            if len(box) != 4:
                raise SystemExit("--box 需为 x0,y0,x1,y1")
        elif a.auto:
            w, h = img.size
            box = (int(w * 0.65), int(h * 0.80), w, h)
        else:
            raise SystemExit("patch 模式需要 --box 或 --auto")
        print("覆盖区域:", box)
        out = do_patch(img, box, a.feather)

    dst = a.out or (os.path.splitext(a.input)[0] + "_clean.png")
    out.save(dst, "PNG", optimize=True)
    print("已输出:", dst, out.size)


if __name__ == "__main__":
    sys.exit(main())
