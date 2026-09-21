#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_prompt.py — 铅笔素描手绘图 prompt 构造器

把「主体 + 笔触预设 + 画幅 + 点缀色 + 光源」拼装成一段可直接投喂给图片模型的 prompt。
只做确定性的拼装，不做创意判断 —— 判断在调用它的 agent 那一侧。

用法:
  python build_prompt.py --subject "一个在跑步机上原地跑的人" --preset conceptual --aspect portrait
  python build_prompt.py --subject "老式打字机" --preset 2 --accent sepia --text "1998"
  python build_prompt.py --subject "街角咖啡馆" -p urban-sketch -a landscape --light dramatic --out prompt.txt
  python build_prompt.py --list
  python build_prompt.py --subject "x" -p 2 --params-only
"""

import argparse
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS_PATH = os.path.join(HERE, "presets.json")

MAX_TEXT_CHARS = 8  # 图内文字硬上限，超过会渲染糊掉


def load_presets():
    with open(PRESETS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def resolve_preset(data, key):
    """支持 3 种写法：数字编号 '2'、预设 key 'hatched-tonal'、中文名 '排线明暗素描'。"""
    presets = data["presets"]
    k = str(key).strip()
    if k in presets:
        return k, presets[k]
    for name, cfg in presets.items():
        if k == str(cfg["id"]) or k == cfg["name_zh"]:
            return name, cfg
    raise SystemExit(
        "未知笔触预设: %s\n可用: %s"
        % (key, ", ".join("%s(%s)" % (n, c["id"]) for n, c in presets.items()))
    )


def build(data, subject, preset_key, aspect, accent, light, text):
    presets = data["presets"]
    pname, p = resolve_preset(data, preset_key)

    if aspect is None:
        aspect = p["default_aspect"]
    if aspect not in data["aspects"]:
        raise SystemExit("未知画幅: %s\n可用: %s" % (aspect, ", ".join(data["aspects"])))

    if accent is None:
        accent = "none"
    if accent not in data["accents"]:
        raise SystemExit("未知点缀色: %s\n可用: %s" % (accent, ", ".join(data["accents"])))

    if light is None:
        light = "dramatic" if pname == "charcoal-rough" else "upper-left"
    if light not in data["lighting"]:
        raise SystemExit("未知光源: %s\n可用: %s" % (light, ", ".join(data["lighting"])))

    accent_token = data["accents"][accent]["token"]
    medium = p["medium"]
    if "{accent}" in medium:
        # 淡彩预设必须有色相，用户没给就退回赭石
        if not accent_token:
            accent = "sepia"
            accent_token = data["accents"]["sepia"]["token"]
        medium = medium.replace("{accent}", accent_token)

    color_rule = data["color_rules"]["default"]
    if accent_token:
        color_rule = data["color_rules"]["with_accent"].replace("{accent}", accent_token)

    size = data["aspects"][aspect]["size"]

    lines = []
    lines.append("A graphite pencil sketch of %s." % subject.strip().rstrip("."))
    lines.append("")
    lines.append("Medium: %s." % medium)
    # 预设自带光影的（lock_lighting）不再叠加 --light，避免出现重复矛盾的光照描述
    shading = p["shading"]
    light_locked = p.get("lock_lighting", False) or "light source" in shading
    if not light_locked:
        shading = "%s, %s" % (shading, data["lighting"][light])
    lines.append("Shading: %s." % shading)
    lines.append("Composition/background: %s, %s composition." % (
        p["composition"], data["aspects"][aspect]["en"]))
    lines.append("Style: %s, %s, background %s, %s." % (
        data["quality_block"], color_rule, data["color_rules"]["background"], data["negative_block"]))

    if text:
        if len(text) > MAX_TEXT_CHARS:
            raise SystemExit("图内文字 %d 字，超过 %d 字上限 —— 请缩短，或改为出无字底图后排版叠加"
                             % (len(text), MAX_TEXT_CHARS))
        lines.append('Text: hand-lettered "%s" only, no other text in the image.' % text)
    else:
        lines.append("Text: no text baked into the image.")

    prompt = "\n".join(lines)

    params = {
        "preset": pname,
        "preset_zh": p["name_zh"],
        "size": size,
        "aspect": aspect,
        "aspect_use": data["aspects"][aspect]["use"],
        "accent": accent,
        "light": light,
        "quality": "high",
        "style": "natural",
    }
    return prompt, params


def main():
    ap = argparse.ArgumentParser(description="铅笔素描手绘图 prompt 构造器")
    ap.add_argument("--subject", "-s", help="画面主体（中文或英文描述，抽象概念请先转译成具象物件）")
    ap.add_argument("--preset", "-p", default="hatched-tonal", help="笔触预设：1-6 / key / 中文名，默认 2 排线明暗素描")
    ap.add_argument("--aspect", "-a", default=None, help="画幅：square/landscape/portrait/wide，默认跟随预设")
    ap.add_argument("--accent", default=None, help="点缀色：none/sepia/indigo/red，默认 none")
    ap.add_argument("--light", default=None, help="光源：upper-left/upper-right/dramatic/diffuse")
    ap.add_argument("--text", "-t", default=None, help="图内文字，最多 8 字（可省略，建议省略）")
    ap.add_argument("--out", "-o", default=None, help="把 prompt 写入文件而不是只打印")
    ap.add_argument("--params-only", action="store_true", help="只打印生成参数（size/quality/style），不打印 prompt")
    ap.add_argument("--list", action="store_true", help="列出全部预设/画幅/点缀色/光源")
    args = ap.parse_args()

    data = load_presets()

    if args.list:
        print("笔触预设:")
        for n, c in data["presets"].items():
            print("  %d. %-16s %-22s %s" % (c["id"], n, c["name_zh"], c["best_for"]))
        print("\n画幅:")
        for k, v in data["aspects"].items():
            print("  %-10s %-12s %s" % (k, v["size"], v["use"]))
        print("\n点缀色:")
        for k, v in data["accents"].items():
            print("  %-8s %s" % (k, v["zh"]))
        print("\n光源:")
        for k, v in data["lighting"].items():
            print("  %-12s %s" % (k, v))
        return

    if not args.subject:
        ap.error("缺少 --subject（或用 --list 查看预设）")

    prompt, params = build(data, args.subject, args.preset, args.aspect,
                           args.accent, args.light, args.text)

    if args.params_only:
        print(json.dumps(params, ensure_ascii=False, indent=2))
        return

    print("=== 生成参数 ===")
    print(json.dumps(params, ensure_ascii=False, indent=2))
    print("\n=== PROMPT ===")
    print(prompt)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(prompt + "\n")
        print("\n[已写入] %s" % args.out)


if __name__ == "__main__":
    main()
