# -*- coding: utf-8 -*-
import io, re

p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()

# The compressed reels map: original filename -> deployed path
# 3D: 玄幻开场1, 打斗1, 科幻修仙
# Real: 古装搞笑女, 现代温情
# 2D: 玄幻打斗, 现代悬疑

# Replace the dir paths and filenames in REELS data
# Instead of complex regex, let's modify the openVideo function to check for deployed files

# Add a mapping in JS: compressed reels that are available online
old_openvideo = '''function openVideo(src){
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}'''

new_openvideo = '''const DEPLOYED_VIDEOS = {
  '3D【玄幻开场1】.mp4': 'assets/deploy_assets/reels/3d_01.mp4',
  '3D【打斗1】.mp4': 'assets/deploy_assets/reels/3d_07.mp4',
  '3D【科幻修仙】.mp4': 'assets/deploy_assets/reels/3d_03.mp4',
  '伪真人【古装搞笑女】.mp4': 'assets/deploy_assets/reels/real_02.mp4',
  '伪真人【现代温情】.mp4': 'assets/deploy_assets/reels/real_05.mp4',
  '二维漫【玄幻打斗】.mp4': 'assets/deploy_assets/reels/2d_01.mp4',
  '二维漫【现代悬疑】.mp4': 'assets/deploy_assets/reels/2d_02.mp4',
};

function openVideo(src){
  // Check if this is a local Zhaic path - extract filename
  if(src.includes('../Zhaic/')){
    const fname = src.split('/').pop();
    if(DEPLOYED_VIDEOS[fname]){
      src = DEPLOYED_VIDEOS[fname];
    } else {
      alert('此样片完整版请联系获取，本地预览版请打开 index.html');
      return;
    }
  }
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}'''

assert old_openvideo in s, 'openVideo not found'
s = s.replace(old_openvideo, new_openvideo)

io.open(p, 'w', encoding='utf-8').write(s)
print('deploy.html updated with reel video mapping')
