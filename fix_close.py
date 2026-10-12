path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add closed page CSS
close_css = '''
#closed { position:fixed; inset:0; z-index:99999; background:#0a0a0a; display:flex; flex-direction:column; align-items:center; justify-content:center; }
#closed h1 { color:#b8860b; font-family:'Noto Serif SC',serif; font-size:28px; margin-bottom:12px; letter-spacing:3px; }
#closed p { color:#888; font-size:15px; }
'''
html = html.replace('</style>', close_css + '</style>', 1)

# Add closed HTML right after <body>
close_html = '''
<div id="closed">
  <h1>网站暂时关闭</h1>
  <p>维护中，请稍后访问</p>
</div>
'''
html = html.replace('<body>', '<body>\n' + close_html, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Closed page added")
