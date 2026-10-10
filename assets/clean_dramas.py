# -*- coding: utf-8 -*-
import io, re

p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()

# Replace the entire DRAMAS section with empty data (no local file references)
old_dramas = re.search(r'const DRAMAS = \{.*?\};', s, re.DOTALL).group()

new_dramas = """const DRAMAS = {};"""

s = s.replace(old_dramas, new_dramas)

# Also remove the episode toggle buttons rendering - make them no-op
old_render = """Object.keys(DRAMAS).forEach(id => {
  const box = document.getElementById(id);
  if(!box) return;
  DRAMAS[id].eps.forEach(ep => {
    const b = document.createElement('div');
    b.className = 'ep';
    b.textContent = '\\u25b6 ' + ep.label;
    b.onclick = () => openVideo(DRAMAS[id].dir + ep.file);
    box.appendChild(b);
  });
});"""

# Just replace the whole rendering block to do nothing
new_render = """// DRAMAS disabled on public site - full episodes available on request
"""

s = s.replace(old_render, new_render)

# Also hide the "展开可播放剧集" buttons since there are no episodes
# Find and neutralize toggleEps function
s = s.replace(
    "function toggleEps(id, btn){\n  const box = document.getElementById(id);\n  box.classList.toggle('on');\n  btn.textContent = box.classList.contains('on') ? '收起剧集列表 \\u25b2' : '展开可播放剧集 \\u25bc';\n}",
    "function toggleEps(id, btn){ /* disabled on public site */ }"
)

io.open(p, 'w', encoding='utf-8').write(s)

# Verify no more local refs
remaining = re.findall(r'\.\./Zhaic/', s)
print(f'Local refs remaining: {len(remaining)}')
