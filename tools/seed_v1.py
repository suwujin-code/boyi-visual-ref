"""V1 种子内容（只跑一次）。以后加图用 add_item.py。"""
import json, os, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from imgutil import make_webp, ROOT

W = "/workspace"
D46 = "https://drive.google.com/drive/folders/1bi7gmS44YyjJGibMVQsNqnK4RE-zY0YO"
def d(p): return datetime.date.fromtimestamp(os.path.getmtime(p)).isoformat()

S = [
# ---------- 封面 ----------
("cover-ep46","cover",f"{W}/director/episodes/第46期_120平9.28万套餐/接手/第46期_封面_V1_9x16.png","四房两厅套餐包了什么","第46期",["纸底排版","数字钩子","主播实拍"],
 "米白方格纸底＋红色大号「9.28万」和「120㎡」两组数字，右下主播站在等轴测户型图旁，用「数字→户型→人」的斜向视线把价格和空间连成一条线。",
 ("Drive 第46期_120平四房两厅9.28万套餐", D46)),
("cover-ep45","cover","/workspace/design_ref/_work/drive/ep45_cover_V1.png","燃气定电？热水器拣错冲凉冇热水","第45期",["主播实拍","大字关键词"],
 "浅色室内虚化背景＋怀抱文件夹的主播占据上半部，黄色「燃气定电？」加白色结果句放在下半，上图下文的两段式让人物和问题各占一块，红色 logo 压在右上角收口。",
 ("Drive 第45期_封面_V1_1080x1920.png","https://drive.google.com/file/d/1-h6eBHi-_UMlY3qpkzntzBVDi2k4X1xC/view")),
("cover-ep44","cover","/workspace/design_ref/_work/drive/ep44_cover_D_V3.png","马桶装不上？先量对坑距","第44期",["纸底排版","数字钩子","标注线"],
 "方格纸底＋红色超大「300/400 mm」，下方剖切墙体模型和主播拉卷尺量坑距，红色尺寸箭头把「数字」和「动作」直接扣在一起，信息一眼看完。",
 ("Drive 第44期_马桶坑距怎么量_封面D_V3","https://drive.google.com/file/d/1rgRzmKPrBqbHRUhvvjYgYfQfjJXmmmvC/view")),
("cover-ep42","cover",f"{W}/publish/ep42/第42期_门窗分类_动作表情封面_V6_9x16.png","平开、推拉、断桥先分清两种分类","第42期",["纸底排版","线稿图解","主播实拍"],
 "浅灰纸底＋黑色标题里只把「两种分类」标红，左下门窗开启方式线稿、右侧主播做手势，用细线框把图解分区，画面干净像一页说明书。",
 ("box：/workspace/publish/ep42/",None)),
("cover-ep18","cover",f"{W}/reno_series/第18期_水电前定8件家电/交付/v2/BOSS-COVER-EP18-01_9x16.png","水电进场前，先定8件家电","第18期",["主播实拍","大字关键词"],
 "真实室内背景＋居中主播，白字铺垫句加蓝色超大「8件家电」，上下两段文字夹住人物，视线从标题落到人再落到底部品牌条。",
 ("box：reno_series/第18期_水电前定8件家电/交付/v2",None)),
("cover-ep15","cover",f"{W}/reno_series/第15期_收楼验5样/交付/v2/BOSS-COVER-15V2-01_封面9x16.png","毛坯房收楼签字前先验5样","第15期",["主播实拍","大字关键词"],
 "毛坯房实景＋站姿主播，黄色描边大字「先验5样」压在胸口位置，白字前置条件做引子，人物和关键词上下叠放形成一个视觉中心。",
 ("box：reno_series/第15期_收楼验5样/交付/v2",None)),
("cover-ep14","cover",f"{W}/reno_series/第14期_报价单漏项/交付/v7/BOSS-COVER-14V7-01_封面9x16.png","报价单漏了这5项","第14期",["主播实拍","数字钩子"],
 "暖色实景＋侧身主播，黄色巨型「5项」配白字「后期一定加钱」，小字列出漏项名称，用数字大小反差把焦虑点放到最大。",
 ("box：reno_series/第14期_报价单漏项/交付/v7",None)),
("cover-ep13","cover",f"{W}/reno_series/第13期_低价全包/交付/v1/BOSS-COVER-13V1-01_封面9x16.png","8万全包是大坑？","第13期",["纸底排版","警示条","数字钩子"],
 "上半浅蓝纸底放黑色巨型「8万」，下半黄黑警示斜条托住「大坑」，主播从右侧切入，靠警示条把「价格」和「风险」分成上下两层。",
 ("box：reno_series/第13期_低价全包/交付/v1",None)),
("cover-ep11","cover",f"{W}/reno_series/第11期_装修钱分4块/交付/v1/BOSS-COVER-11V1-01_封面9x16.png","高州100平装修钱分四块","第11期",["主播实拍","大字关键词"],
 "实景书房＋坐姿主播，白字地域和面积在上、黄色「四块」紧跟其下，本地地名直接写进标题，靠「地名＋面积＋数字」拉近同城观众。",
 ("box：reno_series/第11期_装修钱分4块/交付/v1",None)),
("cover-ep10","cover",f"{W}/reno_series/第10期_物业报备/交付/v4/BOSS-COVER-10V4-01_封面9x16.png","开工前先去物业报备","第10期",["色块撞色","大字关键词"],
 "黑字巨型「报备」＋蓝色方块框住主播，下方黑底黄字再重复一次「报备」，同一个词上下呼应，蓝黑撞色让缩略图里也很醒目。",
 ("box：reno_series/第10期_物业报备/交付/v4",None)),
("cover-ep34","cover",f"{W}/reno_series/第34期_封阳台通风/交付/v2/BOSS-COVER-34V2-01_封面9x16.png","封阳台前先算账：通风","第34期",["纸底排版","大字关键词","主播实拍"],
 "白纸底＋黑色宋体「通风」做主标题，蓝色「先算账」压在主播左侧，右下黄色小方块和页码做落点，留白多、像杂志内页。",
 ("box：reno_series/第34期_封阳台通风/交付/v2",None)),
("cover-ep30","cover",f"{W}/reno_series/第30期_空调冷凝水/交付/v2/BOSS-COVER-30V2-01_封面9x16.png","空调冷凝水开工前定","第30期",["暗底","抠像白边","大字关键词"],
 "深色网格底＋白边抠像主播，白色宋体「冷凝水」顶天，黄色「开工前定」配黄色角标线框，暗底让白边人物像贴纸一样跳出来。",
 ("box：reno_series/第30期_空调冷凝水/交付/v2",None)),
("cover-ep22","cover",f"{W}/reno_series/第22期_户门过道尺寸/交付/v7/BOSS-COVER-22V7-04_封面9x16.png","户门过道尺寸：3个数","第22期",["纸底排版","大字关键词"],
 "与第34期同一套白纸杂志版式：黑色「尺寸」＋蓝色「3个数」，主播居右、小字「沙发抬不进门？」做痛点，系列化版式让多期封面放在主页上排得整齐。",
 ("box：reno_series/第22期_户门过道尺寸/交付/v7",None)),
("cover-cab01","cover",f"{W}/claude_code_video_templates/episodes/定制柜投影展开面积/deliver/BOSS-COV-CAB-01_定制柜投影展开面积_封面_1080x1920_v2c.png","定制柜点样计面积：投影展开","专题",["主播实拍","大字关键词"],
 "柜体样板间实景＋倚柜主播，黄色大字「投影展开」放在胸口位置，人物和柜子同框，直接用场景说明主题，不需要额外图解。",
 ("box：claude_code_video_templates/episodes/定制柜投影展开面积/deliver",None)),
("cover-gd01","cover",f"{W}/reno_series/手绘描边风_照片卡点/out/BOSS-VID-GD01V2-01_手绘描边卡点_v2_待审_封面_9x16.png","博艺工地：师傅在干活","日常视频",["工地实拍","手绘描边"],
 "工地实拍照片＋黄色手绘描边框和手写「Work」，白色粗体标题叠在墙面上，手绘线把真实工地变成有温度的日常记录。",
 ("box：reno_series/手绘描边风_照片卡点/out",None)),
# ---------- 片尾落版 ----------
("end-logo-red","end","/workspace/logo_check/logo_H_red_drive.png","官方红色透明 logo（横版）","通用",["品牌","落版"],
 "官方原版：房子图标＋「博艺建筑」＋「以匠心设计，筑理想工程」，透明底原样使用，不裁切、不改色、不加电话地址；片尾落版统一用它收口。",
 ("Drive logo_H_red.png","https://drive.google.com/file/d/1yAuJEZcc64N1XTqhYH9vLWdX5vEBPxBp/view")),
# ---------- 实景空间 ----------
] + [
("site-"+n.lower().replace("img_",""),"site",f"{W}/boyi_heic_new/jpg/{n}.jpg",t,"工地实拍",tags,c,("box：/workspace/boyi_heic_new/jpg",None))
for n,t,tags,c in [
 ("IMG_6163","窗边水电管线走向",["工地实拍","水电"],"毛坯墙地＋红色电管沿地面成排走向窗边，窗外绿网做背景，管线的引导线让人一眼看懂走向，适合做水电讲解的开场底图。"),
 ("IMG_6164","毛坯卧室全景",["工地实拍","空间"],"方正毛坯房＋单窗自然光，地面散放的管材和板材交代施工阶段，空间干净留白，适合叠大字标题。"),
 ("IMG_6165","卫生间排水管预埋",["工地实拍","水电"],"白色 PVC 排水管＋红色管帽在灰地面上转折，俯拍角度把管路结构看得很清楚，适合配防水、地漏类话题。"),
 ("IMG_6167","墙角立管与红色管帽",["工地实拍","水电"],"竖向白色立管＋红色保护帽贴着窗边墙角，竖构图天然适合 9:16，线条硬朗，可作手绘描边标注的底图。"),
 ("IMG_6168","过道全景与红色横幅",["工地实拍","空间","品牌"],"横向长过道＋右侧红色施工横幅，透视线把视线带向尽头，红色横幅顺手带出博艺品牌色。"),
 ("IMG_6169","过道地面红蓝管线",["工地实拍","水电"],"一点透视长过道＋地面红蓝两色管并行，消失点在画面中央，非常适合做「顺着管线往前走」的推镜开场。"),
 ("IMG_6171","门洞与红蓝管入户",["工地实拍","空间"],"门洞框中框构图＋红蓝管从门槛穿过，前后两层空间叠在一起，有纵深，适合做转场的「穿门」镜头。"),
 ("IMG_6174","弱电箱强电箱标识",["工地实拍","水电","品牌"],"灰墙面上博艺红色「弱电箱／强电箱」标识牌＋预留管线，品牌物料和施工细节同框，是证明「规范施工」的好素材。"),
]] + [
# ---------- 包装元素 ----------
("pkg-s02","pkg",f"{W}/subtitle_pack_gpt_v2/samples/BOSS-SUB-GPT2-02_S02_纸底标题封面_防潮四步全片_粤语_样片_20261025_封面.png","S02 纸底标题封面","字幕包",["纸底排版","字幕样式"],
 "浅蓝网格纸底＋蓝色房子图标，黑色「防潮」配蓝色「四样嘢」两行大字，无人物纯排版，适合系列合集或不出镜的知识类。",
 ("box：subtitle_pack_gpt_v2/samples",None)),
("pkg-e02","pkg",f"{W}/subtitle_pack_gpt_v2/samples/BOSS-SUB-GPT2-04_E02_引导加关键词_粤语_样片_20261025_封面.png","E02 引导句＋关键词","字幕包",["字幕样式","大字关键词"],
 "白色黑体引导句＋黄色宋体超大关键词，胸口位置、无底框只用柔投影，一句最多一个关键词，口播里最常用的句型。",
 ("box：subtitle_pack_gpt_v2/samples",None)),
("pkg-e04","pkg",f"{W}/subtitle_pack_gpt_v2/samples/BOSS-SUB-GPT2-06_E04_错对纠正_粤语_样片_20261025_封面.png","E04 错对纠正","字幕包",["字幕样式","大字关键词"],
 "白字说明场景＋黄色大字给结论，靠上下两行的大小反差表达「先说问题再给答案」，适合纠正误区的句子。",
 ("box：subtitle_pack_gpt_v2/samples",None)),
("pkg-e06","pkg",f"{W}/subtitle_pack_gpt_v2/samples/BOSS-SUB-GPT2-08_E06_警示词_粤语_样片_20261025_封面.png","E06 警示词","字幕包",["字幕样式","大字关键词"],
 "地名白字＋黄色警示大字「墙身出水」，配主播正在开口讲的表情，表情和警示词一起放大情绪，用在风险提醒句。",
 ("box：subtitle_pack_gpt_v2/samples",None)),
("pkg-tpl1","pkg",f"{W}/boyi_brand/cover_templates_v1/BOSS-COVER-TPL1-01_9x16.png","封面模板 TPL1 上标题","封面模板",["封面模板","大字关键词"],
 "标题顶在上三分之一、白字问句＋黄色大字答案，主播坐姿在下，是最稳的通用封面骨架，换文字就能出新一期。",
 ("box：boyi_brand/cover_templates_v1",None)),
("pkg-tpl4","pkg",f"{W}/boyi_brand/cover_templates_v1/BOSS-COVER-TPL4-01_9x16.png","封面模板 TPL4 角框标题","封面模板",["封面模板","大字关键词"],
 "黄色直角括号框住标题＋主播居中，括号像取景框一样把视线圈进文字区，比纯文字多一点设计感又不抢人物。",
 ("box：boyi_brand/cover_templates_v1",None)),
]

LINKS = [
("ref-azivor","AI 大厂视觉参考图库（azivor）","https://azivor.github.io/reference",["结构参考","点评写法"],
 "本库的结构样板：按来源分行横滑、大图查看器、搜索筛选收藏；每张图一句「元素＋手法＋连接方式」的点评写法值得照抄。图片版权归原作者，只看不用。"),
("ref-anthropic","Anthropic 官方文章封面（纸张拼贴）","https://www.anthropic.com/news",["纸张拼贴","暖色"],
 "米白纸张颗粒＋手撕拼贴＋实物与几何图并置，适合借鉴到「设计稿→实景」对比封面的质感层，只能局部借鉴手法。"),
("ref-perplexity","Perplexity 品牌海报（暖色大标题）","https://www.perplexity.ai/hub",["暖色","大字标题"],
 "暖色大面积底＋超大标题字，排版极简，可参考做博艺品牌形象图；风格偏国际化，不要整套照搬到抖音口播封面。"),
("ref-openai","OpenAI 发布主视觉（冷暖撞色）","https://openai.com/news/",["冷暖撞色","渐变"],
 "柔和渐变＋冷暖撞色＋大量留白，适合借鉴到片头转场的色彩过渡；版权归原公司，只做手法参考。"),
]

def main():
    items = []
    for sid, grp, src, title, ep, tags, comment, (slabel, surl) in S:
        r = make_webp(src, sid, lossless=(grp == "end"))
        items.append({"id": sid, "group": grp, "title": title, "episode": ep, "date": d(src),
            "tags": tags, "comment": comment, **r,
            "source": {"label": slabel, "url": surl}})
    for sid, title, url, tags, comment in LINKS:
        items.append({"id": sid, "group": "peer", "title": title, "episode": "外部参考",
            "date": "2026-10-29", "tags": tags, "comment": comment, "link": url,
            "source": {"label": url.split('/')[2], "url": url}})
    lib = {
      "site": {"name": "博艺视觉参考库", "version": "V1", "updated": datetime.date.today().isoformat(),
               "owner": "平面设计·内容部"},
      "groups": [
        {"id": "cover", "name": "封面", "desc": "博艺各期抖音封面代表作（第0帧即封面）"},
        {"id": "end", "name": "片尾落版", "desc": "只用官方红色透明 logo 原样，不裁切、不加电话地址"},
        {"id": "site", "name": "实景空间", "desc": "博艺自己的工地实拍，可做底图和 B-roll"},
        {"id": "pkg", "name": "包装元素", "desc": "字幕句型、封面模板等可复用包装"},
        {"id": "peer", "name": "同行案例", "desc": "外部参考只放链接和点评，不托管原图（版权归原作者）"}],
      "items": items}
    (ROOT / "library.json").write_text(json.dumps(lib, ensure_ascii=False, indent=2), encoding="utf-8")
    from collections import Counter
    print(len(items), Counter(i["group"] for i in items))

if __name__ == "__main__":
    main()
