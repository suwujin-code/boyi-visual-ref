"""图片压缩工具：原图 -> images/<id>.webp（长边≤1600）+ thumbs/<id>.webp（长边≤560）"""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
MAX_FULL, MAX_THUMB = 1600, 560

def make_webp(src, item_id, lossless=False):
    im = ImageOps.exif_transpose(Image.open(src))
    has_alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
    im = im.convert("RGBA" if has_alpha else "RGB")
    out = {}
    for sub, lim, q in (("images", MAX_FULL, 82), ("thumbs", MAX_THUMB, 74)):
        c = im.copy()
        c.thumbnail((lim, lim), Image.LANCZOS)  # 只缩放，不裁切
        p = ROOT / sub / f"{item_id}.webp"
        if lossless:
            c.save(p, "WEBP", lossless=True, method=6)
        else:
            c.save(p, "WEBP", quality=q, method=6)
        out[sub] = (f"{sub}/{item_id}.webp", c.size)
    return {"image": out["images"][0], "thumb": out["thumbs"][0],
            "width": out["images"][1][0], "height": out["images"][1][1],
            "orig": list(Image.open(src).size)}
