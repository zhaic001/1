# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace(
    '<img src="../Zhaic/婚庆拍摄/婚礼.mp4" alt="婚礼纪实"',
    '<img src="../Zhaic/婚庆拍摄/婚礼封面.jpg" alt="婚礼纪实"'
)
io.open(p, 'w', encoding='utf-8').write(s)
print('cover src fixed')
