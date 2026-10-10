# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

# 1. 时间改 2025
s = s.replace('第五阶段 · 2024–至今', '第五阶段 · 2025–至今')

# 2. 第五阶段描述改为"从视频摄影到 AI 编导"
s = s.replace(
    '从策划师做到总导演，统筹 30+ 部 AI 短剧项目，培养 60+ 名剪辑师；\n          以 3D 漫为核心，建立伪真人 / 3D 漫 / 二维漫三风格可复用制作标准。',
    '从视频摄影切入 AI 短剧编导，统筹 30+ 部项目，培养 60+ 名剪辑师；\n          以 3D 漫为核心，建立伪真人 / 3D 漫 / 二维漫三风格可复用制作标准。')

io.open(p, 'w', encoding='utf-8').write(s)

# 同步 PDF
p2 = r'D:\资海春\resume-website\assets\build_pdf.py'
t = io.open(p2, encoding='utf-8').read()
t = t.replace('第五阶段 · 2024–至今', '第五阶段 · 2025–至今')
t = t.replace('从策划师做到总导演，统筹 30+ 部 AI 短剧项目，培养 60+ 名剪辑师；以 3D 漫为核心，',
              '从视频摄影切入 AI 短剧编导，统筹 30+ 部项目，培养 60+ 名剪辑师；以 3D 漫为核心，')
io.open(p2, 'w', encoding='utf-8').write(t)
print('done')
