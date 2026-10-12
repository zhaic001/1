path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove existing closed div if present
import re
html = re.sub(r'<div id="closed">.*?</div>\s*', '', html, flags=re.DOTALL)

# Add fresh closed page
close_html = '''<div id="closed" style="position:fixed;inset:0;z-index:99999;background:#0a0a0a;display:flex;flex-direction:column;align-items:center;justify-content:center">
<h1 style="color:#b8860b;font-family:serif;font-size:28px;margin-bottom:12px;letter-spacing:3px">Website Closed</h1>
<p style="color:#888;font-size:15px">Under maintenance</p>
</div>
'''
html = html.replace('<body>', '<body>\n' + close_html, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
