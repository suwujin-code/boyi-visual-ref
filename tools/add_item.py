#!/usr/bin/env python3
"""往参考库加一张图（或一条同行链接）。

用法（图片）：
  python3 tools/add_item.py --group cover --src /path/第47期_封面_V1.png \
     --title "标题" --episode 第47期 --tags 主播实拍,大字关键词 \
     --comment "元素＋手法＋连接方式" --source-label "Drive 第47期" --source-url https://...
用法（同行案例，只放链接不放图）：
  python3 tools/add_item.py --group peer --link https://example.com --title "…" --comment "…" --tags 暖色
分组：cover 封面 / end 片尾落版 / site 实景空间 / pkg 包装元素 / peer 同行案例
加完后运行 python3 tools/build_dist.py 再部署（见 README）。
"""
import argparse, datetime, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from imgutil import make_webp, ROOT

ap = argparse.ArgumentParser()
ap.add_argument("--group", required=True, choices=["cover", "end", "site", "pkg", "peer"])
ap.add_argument("--title", required=True)
ap.add_argument("--comment", required=True, help="一句点评：元素＋手法＋连接方式")
ap.add_argument("--src"); ap.add_argument("--link")
ap.add_argument("--episode", default=""); ap.add_argument("--tags", default="")
ap.add_argument("--date"); ap.add_argument("--id")
ap.add_argument("--source-label", default=""); ap.add_argument("--source-url")
a = ap.parse_args()

lib_p = ROOT / "library.json"
lib = json.loads(lib_p.read_text(encoding="utf-8"))
ids = {i["id"] for i in lib["items"]}
iid = a.id or f"{a.group}-{datetime.datetime.now():%Y%m%d%H%M%S}"
iid = re.sub(r"[^A-Za-z0-9_-]", "-", iid)
if iid in ids: sys.exit(f"id 已存在：{iid}（换一个 --id）")
if "AI生成" in a.comment.replace(" ", "") or "AI生成" in a.title.replace(" ", ""):
    sys.exit("标题/点评不能出现「AI生成」字样")
item = {"id": iid, "group": a.group, "title": a.title, "episode": a.episode,
        "tags": [t.strip() for t in re.split(r"[,，]", a.tags) if t.strip()], "comment": a.comment}
if a.group == "peer":
    if not a.link: sys.exit("同行案例只放链接：请给 --link，不要下载别人的图")
    item.update(link=a.link, date=a.date or datetime.date.today().isoformat(),
                source={"label": a.source_label or a.link.split("/")[2], "url": a.link})
else:
    if not a.src: sys.exit("请给 --src 图片路径")
    item.update(make_webp(a.src, iid, lossless=(a.group == "end")))
    item["date"] = a.date or datetime.date.fromtimestamp(os.path.getmtime(a.src)).isoformat()
    item["source"] = {"label": a.source_label or "博艺内部素材", "url": a.source_url}
lib["items"].append(item)
lib["site"]["updated"] = datetime.date.today().isoformat()
lib_p.write_text(json.dumps(lib, ensure_ascii=False, indent=2), encoding="utf-8")
print("已加入：", iid, item.get("image", item.get("link")))
