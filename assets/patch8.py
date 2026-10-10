# -*- coding: utf-8 -*-
import io
# HTML
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace('澳梦深蓝 → 从一到九文化传媒', '从一到九文化传媒')
io.open(p, 'w', encoding='utf-8').write(s)

# PDF
p2 = r'D:\资海春\resume-website\assets\build_pdf.py'
t = io.open(p2, encoding='utf-8').read()
t = t.replace('澳梦深蓝 → 从一到九文化传媒', '从一到九文化传媒')
io.open(p2, 'w', encoding='utf-8').write(t)
print('done')
