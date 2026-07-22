"""One-off asset optimizer: resize + recompress JPEGs in assets/.

avatar.jpg  -> max 480px (displayed at 120px, covers 4x retina)
others      -> max 1200px longest side, quality 82, progressive
Prints a JSON report of final dimensions for use in <img width/height>.
"""
import json
import os
from PIL import Image

ASSETS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
RULES = {"avatar.jpg": 480}
DEFAULT_MAX = 1200
QUALITY = 82

report = {}
total_before = total_after = 0

for name in sorted(os.listdir(ASSETS)):
    if not name.lower().endswith((".jpg", ".jpeg")):
        continue
    path = os.path.join(ASSETS, name)
    before = os.path.getsize(path)
    img = Image.open(path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    max_side = RULES.get(name, DEFAULT_MAX)
    w, h = img.size
    resized = max(w, h) > max_side
    if resized:
        scale = max_side / max(w, h)
        img = img.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
    tmp = path + ".tmp"
    img.save(tmp, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    new_size = os.path.getsize(tmp)
    if resized or new_size < before:
        os.replace(tmp, path)
        after = new_size
    else:
        os.remove(tmp)
        after = before
        img = Image.open(path)
    total_before += before
    total_after += after
    report[name] = {"width": img.size[0], "height": img.size[1],
                    "before_kb": round(before / 1024, 1), "after_kb": round(after / 1024, 1)}
    print(f"{name}: {w}x{h} -> {img.size[0]}x{img.size[1]}, {before//1024}KB -> {after//1024}KB")

print(f"\nTOTAL: {total_before/1024/1024:.1f}MB -> {total_after/1024/1024:.1f}MB")
with open(os.path.join(ASSETS, "dims.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
