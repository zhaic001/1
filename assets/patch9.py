# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

# 第五阶段职位改为全流程抽卡师
s = s.replace(
    '''          <div class="when">第五阶段 · 2025–至今</div>
          <h4>AI 短剧编导 / 总导演</h4>
          <div class="co">从一到九文化传媒</div>
          <p>从视频摄影切入 AI 短剧编导，统筹 30+ 部项目，培养 60+ 名剪辑师；
          以 3D 漫为核心，建立伪真人 / 3D 漫 / 二维漫三风格可复用制作标准。</p>''',
    '''          <div class="when">第五阶段 · 2025–至今</div>
          <h4>全流程抽卡师 · AI 短剧编导</h4>
          <div class="co">从一到九文化传媒</div>
          <p>抽卡、剪辑、提示词、拆分一体的全流程岗位；统筹 30+ 部 AI 短剧项目，
          培养 60+ 名剪辑师；以 3D 漫为核心，建立伪真人 / 3D 漫 / 二维漫三风格制作标准。</p>''')

io.open(p, 'w', encoding='utf-8').write(s)

# PDF 同步
p2 = r'D:\资海春\resume-website\assets\build_pdf.py'
t = io.open(p2, encoding='utf-8').read()
t = t.replace("job('第五阶段 · 2025–至今', 'AI 短剧编导 / 总导演', '从一到九文化传媒',",
              "job('第五阶段 · 2025–至今', '全流程抽卡师 / AI 短剧编导', '从一到九文化传媒',")
t = t.replace('从视频摄影切入 AI 短剧编导，统筹 30+ 部项目，培养 60+ 名剪辑师；以 3D 漫为核心，',
              '抽卡、剪辑、提示词、拆分一体的全流程岗位；统筹 30+ 部项目，培养 60+ 名剪辑师；以 3D 漫为核心，')
io.open(p2, 'w', encoding='utf-8').write(t)
print('done')
