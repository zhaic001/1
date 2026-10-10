# -*- coding: utf-8 -*-
import io

p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()

old = """function openVideo(src){
  // If it's a local Zhaic path, don't try to load on public site
  if(src && src.indexOf('../Zhaic/') === 0){
    alert('完整剧集请联系获取，当前展示为精选样片');
    return;
  }
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}"""

new = """function openVideo(src){
  if(src && src.indexOf('../Zhaic/') === 0) return;
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}"""

assert old in s
s = s.replace(old, new)
io.open(p, 'w', encoding='utf-8').write(s)
print('alert removed, silent guard')
