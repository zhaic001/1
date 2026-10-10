# -*- coding: utf-8 -*-
import io

p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()

# Replace the openVideo function - remove alert, direct play
old_func = '''const DEPLOYED_VIDEOS = {
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

new_func = '''function openVideo(src){
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}'''

assert old_func in s, 'old func not found'
s = s.replace(old_func, new_func)

io.open(p, 'w', encoding='utf-8').write(s)
print('alert removed, direct play restored')
