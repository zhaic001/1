# -*- coding: utf-8 -*-
import io, re

p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()

# Keep everything visible, but make openVideo handle local paths gracefully
# Replace the openVideo function to check if src is a local path
old_openvideo = """function openVideo(src){
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}"""

new_openvideo = """function openVideo(src){
  // If it's a local Zhaic path, don't try to load on public site
  if(src && src.indexOf('../Zhaic/') === 0){
    alert('完整剧集请联系获取，当前展示为精选样片');
    return;
  }
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}"""

assert old_openvideo in s
s = s.replace(old_openvideo, new_openvideo)

io.open(p, 'w', encoding='utf-8').write(s)
remaining = re.findall(r'\.\./Zhaic/', s)
print(f'Done. Local refs kept in data but guarded by openVideo: {len(remaining)}')
