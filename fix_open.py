path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove closed page div
import re
html = re.sub(r'<div id="closed".*?</div>\s*', '', html, flags=re.DOTALL)
# Remove closed CSS
html = re.sub(r'#closed \{[^}]*\}\s*#closed h1 \{[^}]*\}\s*#closed p \{[^}]*\}\s*', '', html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Closed page removed")
