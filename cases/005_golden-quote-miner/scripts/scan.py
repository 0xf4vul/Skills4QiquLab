#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan.py — 金句候选扫描器（漏斗第一层：候选扫描 + 初筛打分）

只做确定性工作：断句、打标记、按词典打分、排序输出候选池。
不做的事：改写、打磨、判断传播力 —— 那些交给调用它的 agent（见 SKILL.md 第三/四节）。

用法:
  python scan.py article.txt
  python scan.py article.txt --top 15 --min-score 4
  python scan.py article.txt --json > candidates.json
  cat article.txt | python scan.py -
  python scan.py --explain        # 打印打分规则
"""

import argparse
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
LEXICON_PATH = os.path.join(HERE, "lexicon.json")

SENT_SPLIT = re.compile(r"(?<=[。！？!?；;])|\n+")
QUOTE_PAIRS = [("“", "”"), ("‘", "’"), ('"', '"'), ("《", "》")]


def load_lexicon():
    with open(LEXICON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def char_len(s):
    return len(re.sub(r"\s+", "", s))


def split_paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n|\n", text) if p.strip()]


def split_sentences(paragraph):
    parts = [s.strip() for s in SENT_SPLIT.split(paragraph) if s and s.strip()]
    return parts


def hit_count(sentence, items):
    return sum(1 for w in items if w in sentence)


def is_quoted(sentence):
    return any(sentence.startswith(a) or (a in sentence and b in sentence)
               for a, b in QUOTE_PAIRS)


def score_sentence(sentence, lex, is_first, is_last):
    reasons, score = [], 0.0

    jm = lex["judgment_markers"]
    n = hit_count(sentence, jm["items"])
    if n:
        delta = min(n * jm["weight"], jm["cap"])
        score += delta
        reasons.append("判断词×%d(+%.1f)" % (n, delta))

    sm = lex.get("soft_markers")
    if sm:
        n = hit_count(sentence, sm["items"])
        if n:
            delta = min(n * sm["weight"], sm["cap"])
            score += delta
            reasons.append("弱判断×%d(+%.1f)" % (n, delta))

    af = lex["ai_flavor"]
    n = hit_count(sentence, af["items"])
    if n:
        delta = max(n * af["weight"], af["cap"])
        score += delta
        reasons.append("AI腔×%d(%.1f)" % (n, delta))

    cl = lex["cliche"]
    n = hit_count(sentence, cl["items"])
    if n:
        delta = max(n * cl["weight"], cl["cap"])
        score += delta
        reasons.append("陈词×%d(%.1f)" % (n, delta))

    lr = lex["length_rules"]
    L = char_len(sentence)
    if L < lr["ideal_min"]:
        score += lr["score_too_short"]
        reasons.append("过短%d字(%.1f)" % (L, lr["score_too_short"]))
    elif L <= lr["ideal_max"]:
        score += lr["score_in_range"]
        reasons.append("长度%d字(+%.1f)" % (L, lr["score_in_range"]))
    elif L <= lr["hard_max"]:
        reasons.append("偏长%d字(0)" % L)
    else:
        score += lr["score_too_long"]
        reasons.append("过长%d字(%.1f)" % (L, lr["score_too_long"]))

    pos = lex["position"]
    if is_first:
        score += pos["paragraph_first"]
        reasons.append("段首(+%.1f)" % pos["paragraph_first"])
    if is_last and not is_first:
        score += pos["paragraph_last"]
        reasons.append("段尾(+%.1f)" % pos["paragraph_last"])

    if is_quoted(sentence):
        score += lex["quoted"]
        reasons.append("引语(+%.1f)" % lex["quoted"])

    dp = lex["dependency_pronouns"]
    if sentence[:1] in dp["items"]:
        score += dp["weight"]
        reasons.append("代词开头(%.1f，需补上下文)" % dp["weight"])

    return round(score, 2), reasons


def scan(text, lex):
    candidates, seen = [], set()
    total = 0
    for para in split_paragraphs(text):
        sents = split_sentences(para)
        for i, s in enumerate(sents):
            total += 1
            key = re.sub(r"\s+", "", s)
            if key in seen:
                continue
            seen.add(key)
            sc, reasons = score_sentence(
                s, lex,
                is_first=(i == 0),
                is_last=(i == len(sents) - 1 and len(sents) > 1),
            )
            candidates.append({
                "sentence": s,
                "length": char_len(s),
                "score": sc,
                "reasons": reasons,
                "is_para_first": i == 0,
                "is_para_last": i == len(sents) - 1 and len(sents) > 1,
                "quoted": is_quoted(s),
            })
    candidates.sort(key=lambda c: (-c["score"], c["length"]))
    return candidates, total


def main():
    ap = argparse.ArgumentParser(description="金句候选扫描器（漏斗第一层）")
    ap.add_argument("input", nargs="?", help="文本文件路径，或 '-' 读 stdin")
    ap.add_argument("--top", type=int, default=None, help="输出条数，默认取词典 output.default_top")
    ap.add_argument("--min-score", type=float, default=None, help="分数下限，默认 output.default_min_score")
    ap.add_argument("--json", action="store_true", help="输出 JSON 而不是 Markdown 表格")
    ap.add_argument("--all", action="store_true", help="输出全部候选（含低分），不截断")
    ap.add_argument("--explain", action="store_true", help="打印打分规则说明")
    args = ap.parse_args()

    lex = load_lexicon()
    out_cfg = lex["output"]
    top = args.top if args.top is not None else out_cfg["default_top"]
    min_score = args.min_score if args.min_score is not None else out_cfg["default_min_score"]

    if args.explain:
        print("打分规则（详见 lexicon.json）：")
        print("  判断词      %+.1f / 个，上限 %+.1f" % (lex["judgment_markers"]["weight"], lex["judgment_markers"]["cap"]))
        print("  AI 腔       %+.1f / 个，下限 %+.1f" % (lex["ai_flavor"]["weight"], lex["ai_flavor"]["cap"]))
        print("  陈词滥调    %+.1f / 个，下限 %+.1f" % (lex["cliche"]["weight"], lex["cliche"]["cap"]))
        lr = lex["length_rules"]
        print("  字数 %d-%d  %+.1f；<%d %+.1f；>%d %+.1f" % (
            lr["ideal_min"], lr["ideal_max"], lr["score_in_range"],
            lr["ideal_min"], lr["score_too_short"], lr["hard_max"], lr["score_too_long"]))
        print("  段首/段尾   %+.1f / %+.1f" % (lex["position"]["paragraph_first"], lex["position"]["paragraph_last"]))
        print("  引号引语    %+.1f" % lex["quoted"])
        print("  代词开头    %+.1f" % lex["dependency_pronouns"]["weight"])
        print("\n说明：本脚本只跑漏斗第一层，排名≠最终金句。")
        print("      第二层（密度过滤）、第三层（张力打分）、第四层（可独立检验）由 agent 完成。")
        return

    if not args.input:
        ap.error("缺少 input（或用 --explain 查看规则）")

    if args.input == "-":
        text = sys.stdin.read()
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()

    candidates, total = scan(text, lex)

    if args.all:
        picked = candidates
    else:
        picked = [c for c in candidates if c["score"] >= min_score][:top]

    if args.json:
        print(json.dumps({"total_sentences": total, "candidates": picked},
                         ensure_ascii=False, indent=2))
        return

    print("扫描句数：%d ｜ 去重候选：%d ｜ 过线(≥%.1f)：%d ｜ 输出：%d"
          % (total, len(candidates), min_score,
             len([c for c in candidates if c["score"] >= min_score]), len(picked)))
    print()
    print("| # | 候选句 | 字数 | 分数 | 打分依据 |")
    print("|---|--------|------|------|----------|")
    for i, c in enumerate(picked, 1):
        s = c["sentence"].replace("|", "\\|").replace("\n", " ")
        if len(s) > 60:
            s = s[:57] + "…"
        print("| %d | %s | %d | %.2f | %s |" % (i, s, c["length"], c["score"], "；".join(c["reasons"])))
    print()
    print("> 这是漏斗第一层的候选池，**排名不等于最终金句**。")
    print("> 接下来：密度过滤 → 张力四维打分 → 可独立检验 → 按八型骨架改写（见 SKILL.md）。")


if __name__ == "__main__":
    main()
