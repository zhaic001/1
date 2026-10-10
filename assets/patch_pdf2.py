# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\assets\build_pdf.py'
s = io.open(p, encoding='utf-8').read()

# 替换整个从业经历 block
old_start = "# 从业经历\nsection('从业经历')"
old_end = "job('入行', '摄影师 / 摄影摄像', '商业摄影方向', '自带索尼相机承接人物/活动/产品拍摄，练出构图与布光功底。')"

i1 = s.index(old_start)
i2 = s.index(old_end) + len(old_end)

new_block = """# 从业经历
section('从业经历')
def job(period, title, company, desc):
    E.append(Paragraph(f'<b>{title}</b>　<font color="#888888" size=8.5>{company} · {period}</font>', s_b))
    E.append(Paragraph('　' + desc, s_s))
job('第五阶段 · 2024–至今', 'AI 短剧编导 / 总导演', '澳梦深蓝 → 从一到九文化传媒',
    '从策划师做到总导演，统筹 30+ 部 AI 短剧项目，培养 60+ 名剪辑师；以 3D 漫为核心，'
    '建立伪真人 / 3D 漫 / 二维漫三风格可复用制作标准。')
job('第四阶段', '婚庆摄影师（独立接单）', '独立摄影师',
    '独立承接婚礼跟拍与活动纪实，扛机器、布光、现场调度一把抓。')
job('第三阶段 · 在校', '小黑匣影视 · 跟组拍摄', '益阳小黑匣影视',
    '进影视组参与正片拍摄，从助理做起，熟悉剧组流程与现场导演节奏。')
job('第二阶段', '广告公司合作', '益阳本地广告公司',
    '与广告公司合作接商单，平面 + 拍摄双修，独立对接客户需求。')
job('第一阶段 · 在校起点', '平面设计 · 自主接单', '学生时代',
    '在校就接平面设计私单，做海报、物料、UI，攒下客户与作品集。')"""

s = s[:i1] + new_block + s[i2:]
io.open(p, 'w', encoding='utf-8').write(s)
print('pdf patched')
