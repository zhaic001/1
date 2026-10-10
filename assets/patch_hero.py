# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

s = s.replace('AI 漫剧总导演 · PORTFOLIO 2026', 'AI 短剧抽卡师 · PORTFOLIO 2026')
s = s.replace('AI 漫剧总导演 / 项目负责人', 'AI 短剧抽卡师 / 全流程制作')
s = s.replace('2 年 AI 漫剧垂直经验，历任策划师到总导演', '视觉设计垂直经验，从平面设计、摄影到 AI 短剧制作')

io.open(p, 'w', encoding='utf-8').write(s)
print('hero text updated')
