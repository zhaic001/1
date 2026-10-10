# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

# 替换都市爽文 eps 列表（修正34集命名，加直言不讳-34集）
old_dou = """  'eps-dou': {
    dir: '../Zhaic/成片/都市爽文/',
    eps: [
      ['《直言不讳系统》-15集.mp4','EP15'],['《直言不讳系统》-16集.mp4','EP16'],
      ['《直言不讳系统》-17集.mp4','EP17'],['《直言不讳系统》-18集.mp4','EP18'],
      ['《直言不讳系统》-19集.mp4','EP19'],['《直言不讳系统》-20集.mp4','EP20'],
      ['《直言不讳系统》-21集.mp4','EP21'],['直言不讳-32集.mp4','EP32'],
      ['直言不讳-33集.mp4','EP33'],['34.mp4','EP34']
    ].map(([f,l]) => ({file:f, label:l}))
  }"""
new_dou = """  'eps-dou': {
    dir: '../Zhaic/成片/都市爽文/',
    eps: [
      ['《直言不讳系统》-15集.mp4','EP15'],['《直言不讳系统》-16集.mp4','EP16'],
      ['《直言不讳系统》-17集.mp4','EP17'],['《直言不讳系统》-18集.mp4','EP18'],
      ['《直言不讳系统》-19集.mp4','EP19'],['《直言不讳系统》-20集.mp4','EP20'],
      ['《直言不讳系统》-21集.mp4','EP21'],['直言不讳-32集.mp4','EP32'],
      ['直言不讳-33集.mp4','EP33'],['直言不讳-34集.mp4','EP34']
    ].map(([f,l]) => ({file:f, label:l}))
  }"""
assert old_dou in s, 'dou block not found'
s = s.replace(old_dou, new_dou)

# 替换现代 eps 列表（加40无字幕版）
old_xd = """  'eps-xiandai': {
    dir: '../Zhaic/成片/现代/',
    eps: [
      ['35集（无字幕）','EP35'],['36集（无字幕）','EP36'],['37集（有字幕）','EP37'],
      ['38集（无字幕）','EP38'],['39集（无字幕）','EP39'],['40集（有字幕）','EP40'],
      ['41集（无字幕）','EP41']
    ].map(([f,l]) => ({file:`《重返80：从破产川菜馆到国宴主厨》${f}.mp4`, label:l}))
  }"""
new_xd = """  'eps-xiandai': {
    dir: '../Zhaic/成片/现代/',
    eps: [
      ['35集（无字幕）','EP35'],['36集（无字幕）','EP36'],['37集（有字幕）','EP37'],
      ['38集（无字幕）','EP38'],['39集（无字幕）','EP39'],['40集（无字幕）','EP40'],
      ['40集（有字幕）','EP40 有字幕'],['41集（无字幕）','EP41']
    ].map(([f,l]) => ({file:`《重返80：从破产川菜馆到国宴主厨》${f}.mp4`, label:l}))
  }"""
assert old_xd in s, 'xiandai block not found'
s = s.replace(old_xd, new_xd)

io.open(p, 'w', encoding='utf-8').write(s)
print('dramas updated')
