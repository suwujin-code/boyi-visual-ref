#!/usr/bin/env python3
"""生成部署目录 dist/。
GitHub 连接器只能推文本文件，所以把每张 webp 包成同名 .svg（内嵌 base64），
<img> 照常显示；源码里仍保留真正的 webp。能直接传二进制时，也可以直接部署根目录。"""
import base64, json, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
if DIST.exists(): shutil.rmtree(DIST)   # 只清理自己生成的 dist/
(DIST / "images").mkdir(parents=True); (DIST / "thumbs").mkdir()
lib = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
from PIL import Image
def wrap(rel):
    src = ROOT / rel; w, h = Image.open(src).size
    b64 = base64.b64encode(src.read_bytes()).decode()
    out = rel[:-5] + ".svg"
    (DIST / out).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><image width="{w}" height="{h}" href="data:image/webp;base64,{b64}"/></svg>')
    return out
for it in lib["items"]:
    for k in ("image", "thumb"):
        if it.get(k): it[k] = wrap(it[k])
(DIST / "library.json").write_text(json.dumps(lib, ensure_ascii=False, indent=2), encoding="utf-8")
html = (ROOT / "index.html").read_text(encoding="utf-8").replace("thumbs/end-logo-red.webp", "thumbs/end-logo-red.svg")
(DIST / "index.html").write_text(html, encoding="utf-8")
(DIST / ".nojekyll").write_text("\n")
print("dist 完成：", sum(1 for _ in DIST.rglob("*") if _.is_file()), "个文件")
