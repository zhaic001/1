path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the protection JS with stronger version
old_js_start = '<script>document.addEventListener("contextmenu"'
old_js_end = '</script>'
# Find and replace the entire protection script
import re
# Remove old protection script if exists
html = re.sub(r'<script>\s*document\.addEventListener\("contextmenu".*?</script>', '', html, flags=re.DOTALL)

# Stronger protection
new_js = '''<script>
// Full anti-download protection
document.addEventListener('contextmenu', function(e) { e.preventDefault(); return false; });
document.addEventListener('dragstart', function(e) { e.preventDefault(); return false; });
document.addEventListener('selectstart', function(e) { if(e.target.closest('video,img')) e.preventDefault(); });
// Block video-specific downloads
document.addEventListener('loadedmetadata', function(e) {
  if(e.target.tagName === 'VIDEO') {
    e.target.setAttribute('controlsList', 'nodownload noremoteplayback');
    e.target.disablePictureInPicture = true;
  }
}, true);
// Prevent Ctrl+S, Ctrl+P, F12
document.addEventListener('keydown', function(e) {
  if((e.ctrlKey && ['s','p','u'].includes(e.key.toLowerCase())) || e.key === 'F12') e.preventDefault();
});
</script>'''

html = html.replace('</body>', new_js + '\n</body>', 1)

# Also add disablePictureInPicture and nodownload to all video tags
html = html.replace('<video controlsList="nodownload" ', '<video controlsList="nodownload noremoteplayback" disablePictureInPicture ')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Strong protection applied")
