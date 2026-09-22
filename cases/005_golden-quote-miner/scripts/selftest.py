#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
golden-quote-miner 自检 —— 装完先跑这个。

本技能是三个里唯一「零第三方依赖」的（纯标准库），所以自检主要验证：
  1. Python 版本
  2. scan.py 能跑通示例长文，输出条数与格式正确
  3. --json 输出是合法 JSON 且字段齐全
  4. 打分规则可解释（--explain）
  5. 边界输入不崩：空文件、超短文本、中文标点、全英文
  6. stdin 管道输入可用

用法：
    python selftest.py
    python selftest.py --keep
"""

import os
import sys
import json
import shutil
import tempfile
import subprocess
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PY = sys.executable
SCAN = os.path.join(HERE, "scan.py")
SAMPLE = os.path.join(ROOT, "examples", "sample-article.txt")

results = []


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -> " + detail) if detail else ""))
    return ok


def run(args, stdin_text=None):
    p = subprocess.run([PY] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", input=stdin_text)
    return p.returncode, (p.stdout or ""), (p.stderr or "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep", action="store_true", help="保留中间产物")
    ap.add_argument("--outdir", default=None, help="中间产物目录，默认系统临时目录")
    a = ap.parse_args()

    # 中间产物写到系统临时目录，不污染仓库、也不触发文件保护
    outdir = a.outdir or tempfile.mkdtemp(prefix="skill-selftest-gqm-")
    os.makedirs(outdir, exist_ok=True)

    print("=" * 62)
    print("golden-quote-miner 自检")
    print("=" * 62)

    # 1 环境
    check("Python >= 3.8", sys.version_info >= (3, 8),
          "当前 %d.%d.%d" % sys.version_info[:3])
    check("零第三方依赖（仅标准库）", True, "无需 pip install")

    # 2 示例文件在位
    if not os.path.exists(SAMPLE):
        check("示例长文存在", False, SAMPLE)
        return finish(a, outdir)
    check("示例长文存在", True, "%d 字节"
          % os.path.getsize(SAMPLE))

    # 3 基本跑通
    rc, so, se = run([SCAN, SAMPLE])
    check("scan.py 跑通示例长文", rc == 0 and len(so.strip()) > 50,
          (se or "").strip()[:90] if rc else "%d 字符输出" % len(so))
    n_rows = len([l for l in so.split("\n") if l.strip().startswith("|")
                  and "---" not in l])
    check("输出了候选清单（表格行 > 2）", n_rows > 2, "%d 行" % n_rows)

    # 4 JSON 模式
    rc, so, se = run([SCAN, SAMPLE, "--json"])
    try:
        data = json.loads(so)
        ok_json = True
        detail = "顶层 %s" % (list(data)[:5] if isinstance(data, dict) else "list")
    except Exception as e:
        ok_json, data, detail = False, None, "JSON 解析失败: %s" % e
    check("--json 输出合法 JSON", ok_json, detail)

    if ok_json and data is not None:
        items = data.get("candidates") if isinstance(data, dict) else data
        items = items or []
        check("JSON 含候选条目", len(items) > 0, "%d 条" % len(items))
        if items:
            keys = set(items[0].keys())
            check("条目字段齐全 (sentence/score/reasons)",
                  {"sentence", "score", "reasons"} <= keys,
                  "实际字段 %s" % sorted(keys))
            texts = [it.get("sentence", "") for it in items]
            check("候选句长度均在合理区间 (8-90 字)",
                  all(8 <= len(t) <= 90 for t in texts),
                  "最短 %d / 最长 %d" % (min(len(t) for t in texts),
                                        max(len(t) for t in texts)))
            scores = [it.get("score", 0) for it in items]
            check("候选按分数降序排列",
                  all(scores[i] >= scores[i + 1] for i in range(len(scores) - 1)),
                  "%.1f .. %.1f" % (scores[0], scores[-1]))
            check("总句数统计存在", isinstance(data.get("total_sentences"), int),
                  "total_sentences=%s" % data.get("total_sentences"))

    # 5 可解释
    rc, so, se = run([SCAN, SAMPLE, "--explain"])
    check("--explain 打印打分规则", rc == 0 and len(so) > 100,
          "%d 字符" % len(so))

    # 6 边界输入
    cases = [
        ("空文件", ""),
        ("超短文本", "今天天气不错。"),
        ("中文标点密集", "他说：「你以为是 A，其实是 B。」——这句话对吗？是的。"),
        ("全英文", "The point is not that you are wrong. It is that nobody cares. "
                   "Time is the only currency that does not inflate."),
        ("含 emoji", "家人们，这次真上桌了🪑 便宜到你不再算它的价钱，才算真的到你手里。"),
        ("单行无标点", "这就够了"),
    ]
    for label, text in cases:
        f = os.path.join(outdir, "_edge.txt")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(text)
        rc, so, se = run([SCAN, f])
        check("边界输入不崩：%s" % label, rc == 0,
              ("rc=%d " % rc) + (se or "").strip()[:80])

    # 7 stdin 管道
    rc, so, se = run([SCAN, "-"], stdin_text=open(SAMPLE, encoding="utf-8").read())
    check("stdin 管道输入可用", rc == 0 and len(so.strip()) > 50,
          (se or "").strip()[:80] if rc else "%d 字符" % len(so))

    return finish(a, outdir)


def finish(a, outdir):
    print("-" * 62)
    fails = [n for n, ok, _ in results if not ok]
    print("通过 %d / %d" % (len(results) - len(fails), len(results)))
    if fails:
        print("失败项：")
        for f in fails:
            print("  -", f)
        print("\n结论：环境未就绪。")
        return 1
    print("结论：golden-quote-miner 就绪，可以开始提金句。")
    if not a.keep:
        shutil.rmtree(outdir, ignore_errors=True)  # 临时目录，删不掉也无妨
    else:
        print("中间产物保留在：%s" % outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
