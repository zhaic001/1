# -*- coding: utf-8 -*-
import io

p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

# Add role tags to each work card
# Card 1: 炼体狂人
s = s.replace(
    '<div class="wc-meta" style="color:var(--accent);letter-spacing:2px">红果 2000 万热度</div>\n          <h3 style="font-size:24px;margin:8px 0">炼体狂人一锤砸穿修真界</h3>',
    '<div class="wc-meta" style="color:var(--accent);letter-spacing:2px">红果 2000 万热度</div>\n          <div style="margin:6px 0"><span style="display:inline-block;padding:3px 10px;border:1px solid var(--accent);border-radius:4px;font-size:12px;color:var(--accent)">参与剪辑 · 抽卡</span></div>\n          <h3 style="font-size:24px;margin:8px 0">炼体狂人一锤砸穿修真界</h3>'
)

# Card 2: 三界送外卖
s = s.replace(
    '<div class="wc-meta" style="color:var(--accent);letter-spacing:2px">红果 1183 万热度</div>\n          <h3 style="font-size:24px;margin:8px 0">我在三界送外卖</h3>',
    '<div class="wc-meta" style="color:var(--accent);letter-spacing:2px">红果 1183 万热度</div>\n          <div style="margin:6px 0"><span style="display:inline-block;padding:3px 10px;border:1px solid var(--accent);border-radius:4px;font-size:12px;color:var(--accent)">参与剪辑 · 抽卡</span></div>\n          <h3 style="font-size:24px;margin:8px 0">我在三界送外卖</h3>'
)

# Card 3: 红白新娘
s = s.replace(
    '<div class="wc-meta" style="color:var(--accent);letter-spacing:2px">现映期 · 50万+ 点赞收藏</div>\n          <h3 style="font-size:24px;margin:8px 0">红白新娘</h3>',
    '<div class="wc-meta" style="color:var(--accent);letter-spacing:2px">现映期 · 50万+ 点赞收藏</div>\n          <div style="margin:6px 0"><span style="display:inline-block;padding:3px 10px;border:1px solid var(--accent);border-radius:4px;font-size:12px;color:var(--accent)">参与剪辑 · 抽卡</span></div>\n          <h3 style="font-size:24px;margin:8px 0">红白新娘</h3>'
)

io.open(p, 'w', encoding='utf-8').write(s)
print('role tags added to all 3 hit dramas')
