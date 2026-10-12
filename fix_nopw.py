path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove password gate HTML
import re
html = re.sub(r'<div id="pwgate">.*?</div>\s*', '', html, flags=re.DOTALL)
# Remove password gate CSS
html = re.sub(r'#pwgate \{[^}]*\}\s*#pwgate input \{[^}]*\}\s*#pwgate button \{[^}]*\}\s*#pwgate \.err \{[^}]*\}\s*#pwgate h2 \{[^}]*\}\s*', '', html)
# Remove password JS
html = re.sub(r'<script>\s*function checkPw\(\).*?</script>', '', html, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Password gate removed")
