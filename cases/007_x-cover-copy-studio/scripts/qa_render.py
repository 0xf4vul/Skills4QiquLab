#!/usr/bin/env python3
"""x-cover-copy-studio :: qa_render.py
出图后的强制质检回路。用法:
    python3 qa_render.py out1.png [out2.png ...] [--full]

检查项(历史踩坑清单,逐条来自真实事故):
    1) 列表行数是否与 payload 条目数一致(曾发生第 7 行被裁掉)
    2) 底部横幅/胶囊标签是否被画布下缘砍断(flex 高度预算不足)
    3) 元素间是否互相遮挡(收藏横幅盖住列表描述文字)
    4) 有无乱码方框(tofu)、emoji 是否彩色渲染
    5) 超粗黑体回退检查(标题过细=webfont 未加载)

默认输出需要人工/模型复核的裁片路径(PIL 区域裁切);
--full 会额外生成整图缩览。
"""
import sys
from PIL import Image

def main():
    args = [a for a in sys.argv[1:] if a != "--full"]
    if not args:
        print(__doc__); sys.exit(0)
    for path in args:
        im = Image.open(path)
        w, h = im.size
        stem = path.rsplit(".", 1)[0]
        im.crop((int(w*0.48), 0, w, h)).save(stem + "__right.png")     # 列表完整行
        im.crop((0, int(h*0.78), w, h)).save(stem + "__bottom.png")     # footer 截断
        im.crop((0, 0, int(w*0.52), h)).save(stem + "__left.png")       # 标题区
        if "--full" in sys.argv:
            im.resize((int(w*0.62), int(h*0.62))).save(stem + "__overview.png")
        print("crops ready:", stem + "__right.png", stem + "__bottom.png", stem + "__left.png")

if __name__ == "__main__":
    main()
