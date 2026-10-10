# -*- coding: utf-8 -*-
"""生成 A4 PDF 简历：资海春 - AI 短剧编导 / 总导演"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, PageBreak)
from reportlab.lib.styles import ParagraphStyle

pdfmetrics.registerFont(TTFont('CN', r'C:\Windows\Fonts\msyh.ttc'))
pdfmetrics.registerFont(TTFont('CNB', r'C:\Windows\Fonts\msyhbd.ttc'))

INK = HexColor('#1a1a1a')
MUTE = HexColor('#555555')
ACCENT = HexColor('#b8860b')
LINE = HexColor('#d9d9d9')

doc = SimpleDocTemplate(
    r'D:\资海春\resume-website\assets\resume.pdf',
    pagesize=A4,
    leftMargin=16*mm, rightMargin=16*mm,
    topMargin=14*mm, bottomMargin=12*mm,
    title='资海春-AI漫剧总导演简历', author='资海春')

s_name = ParagraphStyle('name', fontName='CNB', fontSize=22, leading=26, textColor=INK)
s_role = ParagraphStyle('role', fontName='CN', fontSize=10.5, leading=14, textColor=ACCENT)
s_h = ParagraphStyle('h', fontName='CNB', fontSize=11, leading=15, textColor=INK,
                     spaceBefore=7, spaceAfter=2)
s_b = ParagraphStyle('b', fontName='CN', fontSize=9, leading=13, textColor=INK)
s_s = ParagraphStyle('s', fontName='CN', fontSize=8.4, leading=12, textColor=MUTE)
s_contact = ParagraphStyle('c', fontName='CN', fontSize=8.6, leading=11, textColor=MUTE)

E = []
E.append(Paragraph('资海春', s_name))
E.append(Paragraph('AI 短剧编导 / 总导演 / 项目负责人 · 3D 漫为核心 · 伪真人 / 二维漫全能', s_role))
E.append(Spacer(1, 3))
contact = Table([[
    Paragraph('电话 18273496710', s_contact),
    Paragraph('18273496710@163.com', s_contact),
    Paragraph('微信同电话', s_contact),
    Paragraph('广州', s_contact),
]], colWidths=[45*mm, 55*mm, 30*mm, 25*mm])
contact.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
E.append(contact)
E.append(HRFlowable(width='100%', thickness=0.6, color=ACCENT, spaceBefore=4, spaceAfter=2))

def section(title):
    E.append(Paragraph(title, s_h))
    E.append(HRFlowable(width='100%', thickness=0.3, color=LINE, spaceBefore=1, spaceAfter=2))

def bullet(text, style=s_b):
    E.append(Paragraph('• ' + text, style))

# 战绩
section('导演战绩 · 三部千万热度爆款')
bullet('<b>《炼体狂人一锤砸穿修真界》</b> 红果 2000 万热度 · 全网超 <b>10 亿</b> 播放（玄幻逆袭）', s_b)
bullet('<b>《我在三界送外卖》</b> 红果 1183 万热度 · 全网超 <b>8 亿</b> 播放（都市奇幻）', s_b)
bullet('<b>《红白新娘》</b> 现映 50 万+ 点赞收藏 · 全网累计 <b>16 亿</b> 播放（民俗悬疑）', s_b)
bullet('统筹 <b>30+</b> 部 AI 漫剧项目；培养 <b>60+</b> 名跨行剪辑师从流水线新手成长为专业剪辑师。', s_s)

# 核心能力
section('核心能力')
bullet('全流程操盘：选题 → 剧本 → 分镜 → AI 生成 → 动态制作 → 配音 → 音效 → 成片发布', s_b)
bullet('三种画风：伪真人 / 3D 漫（核心）/ 二维漫，人物三视图 + 场景四视图标准化产出', s_b)
bullet('画质把控：自主改前置与全局组提示词，解决 AI "油脸"问题，保证皮肤肌理与光追关系', s_b)
bullet('团队管理：0→1 搭建生图 / 分镜 / 美术 / 后期剪辑核心岗位，建立排期表、里程碑与质检门', s_b)
bullet('工具链：即梦 / 海螺 / 小云雀 / seedance / kling / Codex / Pencil / PR / AE / 剪映 / 索尼相机', s_s)

# 从业经历
section('从业经历')
def job(period, title, company, desc):
    E.append(Paragraph(f'<b>{title}</b>　<font color="#888888" size=8.5>{company} · {period}</font>', s_b))
    E.append(Paragraph('　' + desc, s_s))
job('第五阶段 · 2025–至今', '全流程抽卡师 / AI 短剧编导', '从一到九文化传媒',
    '抽卡、剪辑、提示词、拆分一体的全流程岗位；统筹 30+ 部项目，培养 60+ 名剪辑师；以 3D 漫为核心，'
    '建立伪真人 / 3D 漫 / 二维漫三风格可复用制作标准。')
job('第四阶段', '婚庆摄影师（独立接单）', '独立摄影师',
    '独立承接婚礼跟拍与活动纪实，扛机器、布光、现场调度一把抓。')
job('第三阶段 · 在校', '小黑匣影视 · 跟组拍摄', '益阳小黑匣影视',
    '进影视组参与正片拍摄，从助理做起，熟悉剧组流程与现场导演节奏。')
job('第二阶段', '广告公司合作', '益阳本地广告公司',
    '与广告公司合作接商单，平面 + 拍摄双修，独立对接客户需求。')
job('第一阶段 · 在校起点', '平面设计 · 自主接单', '学生时代',
    '在校就接平面设计私单，做海报、物料、UI，攒下客户与作品集。')

# 已上线/在制项目
section('参与项目题材库（部分）')
bullet('已上线爆款：炼体狂人 / 三界送外卖 / 红白新娘 / 清风渡我濯罪孽(999万热度)', s_s)
bullet('在制储备：殡仪馆保安·白班两百夜班两万 / 穿越冰棺世界 / 掀翻豆腐摊 / 东北渔场 / 绝对占有 / '
       '公爵的禁忌 / 皇后王座赤龙女 / 神仙饭店 / 富家少爷重生败家系统 / 我的狼人丈夫', s_s)

# 教育
section('教育背景')
bullet('湖南工艺美术职业大学 · 大专 · 视觉传播设计学院 · 广告艺术设计（新媒体传播与策划方向）', s_b)
bullet('从中专一路读到大专，系统训练平面设计、摄影摄像与 UI 设计基本功', s_s)
bullet('国家励志奖学金 ×1 · 二等综合奖学金 ×2 · 校级三好学生 ×2 · 校级优秀学生干部 ×3', s_s)

doc.build(E)
print('PDF OK')
