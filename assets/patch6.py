# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

# 替换整个时间轴
old_tl_start = '<div class="tl">'
old_tl_end = '''      </div>
      <div>
        <div class="sec-sub" style="margin-bottom:14px">核心职责</div>'''

i1 = s.index(old_tl_start)
i2 = s.index(old_tl_end) + len(old_tl_end)

new_tl = '''<div class="tl">
        <div class="tl-item">
          <div class="when">第五阶段 · 2024–至今</div>
          <h4>AI 短剧编导 / 总导演</h4>
          <div class="co">澳梦深蓝 → 从一到九文化传媒</div>
          <p>从策划师做到总导演，统筹 30+ 部 AI 短剧项目，培养 60+ 名剪辑师；
          以 3D 漫为核心，建立伪真人 / 3D 漫 / 二维漫三风格可复用制作标准。</p>
        </div>
        <div class="tl-item">
          <div class="when">第四阶段</div>
          <h4>自主承接婚庆拍摄</h4>
          <div class="co">独立摄影师</div>
          <p>独立接单婚礼跟拍、活动纪实，扛机器、布光、现场调度一把抓，练出扛压能力与现场叙事感。</p>
        </div>
        <div class="tl-item">
          <div class="when">第三阶段 · 在校期间</div>
          <h4>益阳市小黑匣影视 · 参与拍摄</h4>
          <div class="co">实习 / 跟组</div>
          <p>进影视组参与正片拍摄，从助理做起，熟悉剧组流程、机位调度与现场导演节奏。</p>
        </div>
        <div class="tl-item">
          <div class="when">第二阶段</div>
          <h4>益阳本地广告公司 · 合作</h4>
          <div class="co">广告片 / 商单合作</div>
          <p>与益阳不知名广告公司合作接商单，平面 + 拍摄双修，开始独立对接客户需求。</p>
        </div>
        <div class="tl-item">
          <div class="when">第一阶段 · 在校起点</div>
          <h4>平面设计 · 自主接单</h4>
          <div class="co">学生时代</div>
          <p>在校就开始自己接平面设计私单，做海报、物料、UI 设计，攒下第一笔客户与作品集。</p>
        </div>
      </div>
      <div>
        <div class="sec-sub" style="margin-bottom:14px">核心职责</div>'''

s = s[:i1] + new_tl + s[i2:]

# 标题也改
s = s.replace(
    '<h2 class="sec">从摄影师、平面设计师到 AI 短剧编导</h2>',
    '<h2 class="sec">从在校接单平面设计，到 AI 短剧编导</h2>')

io.open(p, 'w', encoding='utf-8').write(s)
print('career 5 stages done, length=', len(s))
