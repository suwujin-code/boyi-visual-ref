# 博艺视觉参考库 V1

**用途**：给博艺装修「平面设计·内容部」做封面、片尾落版、包装元素时先看的参考库。按组横向浏览，点卡片看大图和点评，可以搜索、按标签筛选、收藏（收藏只存在本机浏览器）、切换深浅色，手机上也能看。

**网址**：https://suwujin-code.github.io/boyi-visual-ref/
**源码仓库**：https://github.com/suwujin-code/boyi-visual-ref（`main` 放源码，`gh-pages` 放部署版本）

## 分组
| 分组 id | 名称 | 放什么 |
|---|---|---|
| cover | 封面 | 博艺各期抖音封面代表作 |
| end | 片尾落版 | **只放官方红色透明 logo 原样**（博艺建筑＋「以匠心设计，筑理想工程」），不裁切、不改色、不加电话地址 |
| site | 实景空间 | 博艺自己的工地实拍 |
| pkg | 包装元素 | 字幕句型、封面模板等 |
| peer | 同行案例 | **只放链接＋点评，不下载、不托管别人的图** |

## 点评格式
每张图写一句：**元素＋手法＋连接方式**。
例：「方格纸底＋红色超大『300/400 mm』，下方主播拉卷尺量坑距，红色尺寸箭头把『数字』和『动作』直接扣在一起。」

## 怎么加图（三步）
1. 把图片放到云电脑任意位置（png/jpg 都行，脚本会自动转成 webp，长边不超过 1600，另出缩略图）。
2. 运行：
   ```bash
   cd /workspace/design_ref/boyi-visual-ref
   python3 tools/add_item.py --group cover --src /路径/第47期_封面_V1.png \
     --title "第47期标题" --episode 第47期 --tags 主播实拍,大字关键词 \
     --comment "元素＋手法＋连接方式" --source-label "Drive 第47期" --source-url "Drive 链接"
   # 同行案例只放链接：
   python3 tools/add_item.py --group peer --link https://… --title "…" --comment "…" --tags 暖色
   ```
3. 重新部署：`python3 tools/build_dist.py` 生成 `dist/`，再把 `dist/` 里新增或改动的文件（新图的 `images/*.svg`、`thumbs/*.svg` 和 `library.json`）推到仓库 `gh-pages` 分支根目录；源码改动推到 `main`。约 1 分钟后网址刷新。

> 为什么是 .svg：GitHub 连接器只能推文本，所以 `build_dist.py` 把 webp 用 base64 包成同名 svg，浏览器照常显示。源码里保留真正的 webp。

## 规矩
- 不放任何带「AI 生成」字样的图（第09期 V7 封面因左上角有该字样已排除）。
- 不放带电话、地址的图（如印有电话的保护膜照片）。
- 只加不删：旧条目不要删，原图不要移动或改名。
- 仓库里不要放任何密钥、令牌、.env 文件。

## 文件
- `index.html`：页面（样式和脚本都在里面）
- `library.json`：全部条目数据
- `images/`、`thumbs/`：webp 大图和缩略图（GitHub `main` 不放这两个文件夹；完整 webp 原件在 Drive「03_交付/博艺视觉参考库_V1」的压缩包和云电脑 `/workspace/design_ref/boyi-visual-ref/` 里）
- `tools/imgutil.py`：压图；`tools/add_item.py`：加条目；`tools/build_dist.py`：生成部署目录；`tools/seed_v1.py`：V1 初始内容
