# -*- coding: utf-8 -*-
"""
中文字体探测器 —— 商用化关键件。

为什么需要它：
    叠字渲染唯一不可回避的外部依赖是「一个能渲染中文的字体文件」。
    硬编码某个用户目录下的字体路径，换台机器就失效，
    这个脚本让 Skill 在任何 Windows / macOS / Linux 上开箱即用。

探测优先级：
    1. 环境变量 SKILL_FONT（显式指定，最高优先级）
    2. --font 命令行参数
    3. 系统字体目录，按下面的候选表顺序找
    4. 找不到就报错，并给出「该装什么」的具体命令

误判防护：
    很多字体文件存在、但不含 CJK 字形，画出来是豆腐块（□）。
    本脚本用「私有区码位 U+E000」当对照组：如果「中」和 U+E000 渲染出的
    位图完全一致，说明该字体根本没有中文字形，直接判不合格。

用法：
    python find_font.py                    # 打印找到的字体路径
    python find_font.py --json             # 输出 JSON（含全部候选与判定）
    python find_font.py --all              # 列出系统里所有可用的中文字体
    python find_font.py --check            # 找到后实际渲染一次验证
    SKILL_FONT=/path/to.ttf python find_font.py
"""

import os
import sys
import json
import glob
import platform

try:
    from PIL import ImageFont
except ImportError:
    sys.stderr.write("[find_font] 缺少依赖：请先 pip install pillow\n")
    raise

# 对照码位：私有区，任何正常字体都不该有字形，用来识别「豆腐块」
# 注意：判等必须拿「单字 vs 单字」，长度不同 bbox 天然不等，判等会失效
TOFU_PROBE = "\ue000"
CJK_CHAR = "中"
CJK_PROBE = "中文字形检测"


def _candidates():
    """按平台返回候选字体路径列表（按推荐顺序）。"""
    system = platform.system()

    if system == "Windows":
        win = os.environ.get("WINDIR", r"C:\Windows")
        fonts = os.path.join(win, "Fonts")
        names = [
            "msyhbd.ttc",   # 微软雅黑 Bold —— 粗字重，做标题最稳
            "msyh.ttc",     # 微软雅黑
            "msyhl.ttc",    # 微软雅黑 Light
            "Dengb.ttf",    # 等线 Bold
            "Deng.ttf",     # 等线
            "simhei.ttf",   # 黑体
            "simkai.ttf",   # 楷体
            "simfang.ttf",  # 仿宋
            "simsun.ttc",   # 宋体
        ]
        out = [os.path.join(fonts, n) for n in names]
        out += sorted(glob.glob(os.path.join(fonts, "*.ttf")))
        out += sorted(glob.glob(os.path.join(fonts, "*.ttc")))
        return out

    if system == "Darwin":
        dirs = ["/System/Library/Fonts", "/Library/Fonts",
                os.path.expanduser("~/Library/Fonts")]
        dirs += glob.glob("/System/Library/Fonts/Supplemental")
        names = ["PingFang.ttc", "STHeiti Medium.ttc", "STHeiti Light.ttc",
                 "Hiragino Sans GB.ttc", "Songti.ttc", "Kaiti.ttc"]
        out = []
        for d in dirs:
            for n in names:
                out.append(os.path.join(d, n))
        for d in dirs:
            out += sorted(glob.glob(os.path.join(d, "*.ttf")))
            out += sorted(glob.glob(os.path.join(d, "*.ttc")))
        return out

    # Linux / 其它
    dirs = ["/usr/share/fonts", "/usr/local/share/fonts",
            os.path.expanduser("~/.fonts"),
            os.path.expanduser("~/.local/share/fonts")]
    out = []
    for d in dirs:
        out += sorted(glob.glob(os.path.join(d, "**", "*.ttf"), recursive=True))
        out += sorted(glob.glob(os.path.join(d, "**", "*.otf"), recursive=True))
        out += sorted(glob.glob(os.path.join(d, "**", "*.ttc"), recursive=True))
    # Noto CJK 优先
    preferred = [p for p in out if "NotoSansCJK" in p or "NotoSerifCJK" in p
                 or "WenQuanYi" in p or "SourceHan" in p]
    return preferred + [p for p in out if p not in preferred]


def has_cjk(path, size=64):
    """判定字体是否真的含中文字形。返回 (bool, 原因)。"""
    try:
        f = ImageFont.truetype(path, size)
    except Exception as e:
        return False, "load-failed: %s" % e

    try:
        b_one = f.getbbox(CJK_CHAR)      # 单字，与对照组等长
        b_tofu = f.getbbox(TOFU_PROBE)   # 单字
        b_multi = f.getbbox(CJK_PROBE)   # 多字，校验方块字宽度
    except Exception as e:
        return False, "measure-failed: %s" % e

    # 完全没有字形时 bbox 会是 (0,0,0,0)
    if not b_one or (b_one[2] - b_one[0]) <= 0:
        return False, "no-glyph-bbox"

    # 核心判定：单字「中」与 U+E000 渲染完全一致 => 走的都是 .notdef，即豆腐块
    if b_one == b_tofu:
        return False, "tofu (「中」与 U+E000 渲染一致，判定无中文字形)"

    # 汉字是方块字：单字宽应接近字号，且多字宽应接近 n * 字号
    w1 = b_one[2] - b_one[0]
    wm = b_multi[2] - b_multi[0]
    if w1 < size * 0.6:
        return False, "width-abnormal (单字 %dpx @%d，非方块字)" % (w1, size)
    if wm < size * len(CJK_PROBE) * 0.6:
        return False, "width-abnormal (多字 %dpx，疑似非等宽 CJK)" % wm
    return True, "ok"


def pick_font(preferred=None, size=64, verbose=False):
    """
    返回一个可用的中文字体路径。
    preferred 可以是单个路径、也可以用 os.pathsep 分隔多个。
    找不到返回 None。
    """
    tried = []

    sources = []
    if preferred:
        sources += [p for p in preferred.split(os.pathsep) if p]
    env = os.environ.get("SKILL_FONT")
    if env:
        sources.append(env)
    sources += _candidates()

    seen = set()
    for p in sources:
        p = os.path.abspath(os.path.expanduser(p))
        if p in seen:
            continue
        seen.add(p)
        if not os.path.exists(p):
            continue
        ok, why = has_cjk(p, size)
        if verbose:
            sys.stderr.write("  probe %-58s %s\n" % (p[-58:], "OK" if ok else why))
        if ok:
            return p
        tried.append((p, why))
    return None


def list_fonts(limit=40):
    """列出系统里所有含中文字形的字体。"""
    out = []
    seen = set()
    for p in _candidates():
        p = os.path.abspath(p)
        if p in seen or not os.path.exists(p):
            continue
        seen.add(p)
        if has_cjk(p)[0]:
            out.append(p)
        if len(out) >= limit:
            break
    return out


def main():
    import argparse
    ap = argparse.ArgumentParser(description="探测可用的中文字体")
    ap.add_argument("--font", "-f", default=None,
                    help="优先使用的字体路径（可用 os.pathsep 分隔多个）")
    ap.add_argument("--size", type=int, default=64, help="检测字号，默认 64")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--all", action="store_true", help="列出全部可用中文字体")
    ap.add_argument("--check", action="store_true", help="找到后实际渲染一次验证")
    ap.add_argument("-v", "--verbose", action="store_true", help="打印探测过程")
    a = ap.parse_args()

    if a.all:
        fonts = list_fonts()
        if a.json:
            print(json.dumps({"fonts": fonts}, ensure_ascii=False, indent=2))
        else:
            if not fonts:
                print("[find_font] 未找到任何含中文字形的字体")
                return 1
            for f in fonts:
                print(f)
        return 0

    path = pick_font(a.font, size=a.size, verbose=a.verbose)
    if a.json:
        print(json.dumps({"font": path,
                          "platform": platform.system(),
                          "has_pillow": True}, ensure_ascii=False, indent=2))
        return 0 if path else 1

    if not path:
        sys.stderr.write(
            "[find_font] 未找到可用的中文字体。\n"
            "  修法三选一：\n"
            "    1) 装字体：Windows 自带微软雅黑一般够用；Linux 执行\n"
            "       sudo apt install fonts-noto-cjk\n"
            "    2) 显式指定：SKILL_FONT=/path/to/your.ttf\n"
            "    3) 命令行传：--font /path/to/your.ttf\n"
            "  推荐可商用字体：霞鹜文楷 LXGW WenKai（SIL OFL 1.1）、思源黑体（SIL OFL 1.1）\n")
        return 1

    print(path)
    if a.check:
        from PIL import Image, ImageDraw
        f = ImageFont.truetype(path, 72)
        img = Image.new("RGB", (720, 180), (14, 26, 46))
        d = ImageDraw.Draw(img)
        d.text((40, 54), "中文字形渲染验证 OK", font=f, fill=(244, 246, 250))
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "_fontcheck.png")
        img.save(out)
        sys.stderr.write("[find_font] 渲染验证图已写入：%s\n" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
