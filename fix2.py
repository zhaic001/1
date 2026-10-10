import re

path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add controlsList="nodownload" to all video tags
html = html.replace('<video ', '<video controlsList="nodownload" ')

# 2. Add CSS to hide download button
html = html.replace('</style>', '''
video::-internal-media-controls-download-button { display:none !important; }
video::-webkit-media-controls-enclosure { overflow:hidden !important; }
video::-webkit-media-controls-panel { width: calc(100% + 32px) !important; }
</style>''', 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Video download button hidden")
