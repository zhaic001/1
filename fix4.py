import re

path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove native controls from all videos, add custom play overlay
# Replace <video controlsList=... controls > with <video controlsList="nodownload" ... > (keep controls for desktop but add protection)
# Actually, let's keep controls but add a transparent overlay that blocks long-press

# Add CSS for video protection overlay
protect_css = """
.video-wrap { position: relative; display: block; }
.video-wrap video { width: 100%; display: block; }
.video-protect {
  position: absolute; top: 0; left: 0; right: 0; bottom: 0;
  z-index: 2; cursor: pointer;
  -webkit-touch-callout: none;
  -webkit-user-select: none; user-select: none;
}
.video-wrap.playing .video-protect { display: none; }
"""
html = html.replace('</style>', protect_css + '</style>', 1)

# 2. Wrap each video in a .video-wrap div with a protect overlay
# Find all <video ...> tags and wrap them
def wrap_video(match):
    tag = match.group(0)
    # Already wrapped?
    return f'<div class="video-wrap">{tag}<div class="video-protect"></div></div>'

html = re.sub(r'<video [^>]*>', wrap_video, html)

# 3. Add JS to handle play on overlay click
play_js = '''<script>
document.addEventListener('click', function(e) {
  var p = e.target.closest('.video-protect');
  if(p) {
    var v = p.parentElement.querySelector('video');
    if(v) { v.play(); p.parentElement.classList.add('playing'); }
  }
  // Click outside to pause and show overlay again
});
document.addEventListener('visibilitychange', function(){});
// When video ends, show overlay again
document.addEventListener('ended', function(e) {
  if(e.target.tagName === 'VIDEO') {
    e.target.parentElement.classList.remove('playing');
  }
}, true);
</script>'''
html = html.replace('</body>', play_js + '\n</body>', 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Videos wrapped. Size: {len(html)}")
# Count
print(f"Video wraps: {html.count('video-wrap')}")
