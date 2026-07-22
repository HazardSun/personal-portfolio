"""构建脚本：压缩 CSS / JS 生成 .min 版本（index.html 引用的是 .min 文件）。

用法：python tools/build.py
依赖：pip install rcssmin rjsmin
"""
import os

import rcssmin
import rjsmin

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

JOBS = [
    ("styles.css", "styles.min.css", rcssmin.cssmin),
    ("main.js", "main.min.js", rjsmin.jsmin),
]

for src_name, out_name, minify in JOBS:
    src_path = os.path.join(ROOT, src_name)
    out_path = os.path.join(ROOT, out_name)
    with open(src_path, "r", encoding="utf-8") as f:
        source = f.read()
    result = minify(source)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(result)
    before_kb = len(source.encode("utf-8")) / 1024
    after_kb = len(result.encode("utf-8")) / 1024
    print(f"{src_name}: {before_kb:.1f}KB -> {out_name}: {after_kb:.1f}KB ({after_kb / before_kb * 100:.0f}%)")

print("构建完成")
