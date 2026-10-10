# -*- coding: utf-8 -*-
import io

p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()

# Replace REELS data with 3 online samples
old_reels = """const REELS = {
  'r-3d': {
    dir: '../Zhaic/DEOM/视频作品集/3D漫/3D漫【水印】/',
    items: [
      ['3D【玄幻开场1】.mp4','玄幻开场 · 01','assets/reel-covers/3d_01.jpg'],
      ['3D【玄幻开场2】.mp4','玄幻开场 · 02','assets/reel-covers/3d_02.jpg'],
      ['3D【科幻修仙】.mp4','科幻修仙','assets/reel-covers/3d_03.jpg'],
      ['3D【科幻废土风格】.mp4','科幻废土','assets/reel-covers/3d_04.jpg'],
      ['3D【系统穿越】.mp4','系统穿越','assets/reel-covers/3d_05.jpg'],
      ['3D【叙事】.mp4','叙事感镜','assets/reel-covers/3d_06.jpg'],
      ['3D【打斗1】.mp4','打斗 · 01','assets/reel-covers/3d_07.jpg'],
      ['3D【打斗2】.mp4','打斗 · 02','assets/reel-covers/3d_08.jpg'],
      ['3D【追逐1】.mp4','追逐 · 01','assets/reel-covers/3d_09.jpg'],
      ['3D【追逐2】.mp4','追逐 · 02','assets/reel-covers/3d_10.jpg'],
      ['3D【追逐3】.mp4','追逐 · 03','assets/reel-covers/3d_11.jpg'],
      ['3D【恐怖】.mp4','恐怖氛围','assets/reel-covers/3d_12.jpg'],
      ['3D【海外女频同性】.mp4','海外女频','assets/reel-covers/3d_13.jpg']
    ]
  },
  'r-real': {
    dir: '../Zhaic/DEOM/视频作品集/伪真人/',
    items: [
      ['阿嫲的清北梦-第20集.mp4','阿嬷的清北梦 · EP20','assets/reel-covers/real_01.jpg'],
      ['伪真人【现代悬疑】.mp4','现代悬疑','assets/reel-covers/real_02.jpg'],
      ['伪真人【现代温情】.mp4','现代温情','assets/reel-covers/real_03.jpg'],
      ['伪真人【现代系统】.mp4','现代系统','assets/reel-covers/real_04.jpg'],
      ['伪真人【古装玄幻】.mp4','古装玄幻','assets/reel-covers/real_05.jpg'],
      ['伪真人【古装搞笑】.mp4','古装搞笑','assets/reel-covers/real_06.jpg'],
      ['伪真人【古装搞笑女】.mp4','古装搞笑女','assets/reel-covers/real_07.jpg'],
      ['海外伪真人【现代言情】.mp4','海外 · 现代言情','assets/reel-covers/real_08.jpg'],
      ['海外伪真人【现代玄幻言情】.mp4','海外 · 现代玄幻言情','assets/reel-covers/real_09.jpg'],
      ['海外伪真人【古西欧言情】.mp4','海外 · 古西欧言情','assets/reel-covers/real_10.jpg'],
      ['海外伪真人【古欧玄幻言情】.mp4','海外 · 古欧玄幻言情','assets/reel-covers/real_11.jpg']
    ]
  },
  'r-2d': {
    dir: '../Zhaic/DEOM/视频作品集/二维漫/',
    items: [
      ['二维漫【玄幻打斗】.mp4','玄幻打斗','assets/reel-covers/2d_01.jpg'],
      ['二维漫【现代悬疑】.mp4','现代悬疑','assets/reel-covers/2d_02.jpg'],
      ['二维漫【现代类打斗】.mp4','现代打斗','assets/reel-covers/2d_03.jpg']
    ]
  }
};"""

new_reels = """const REELS = {
  'r-3d': {
    dir: '',
    items: [
      ['assets/deploy_assets/reels/3d_01.mp4','3D漫 · 玄幻开场','assets/reel-covers/3d_01.jpg']
    ]
  },
  'r-real': {
    dir: '',
    items: [
      ['assets/deploy_assets/reels/real_02.mp4','伪真人 · 古装搞笑','assets/reel-covers/real_07.jpg']
    ]
  },
  'r-2d': {
    dir: '',
    items: [
      ['assets/deploy_assets/reels/2d_01.mp4','二维漫 · 玄幻打斗','assets/reel-covers/2d_01.jpg']
    ]
  }
};"""

assert old_reels in s, 'old REELS not found'
s = s.replace(old_reels, new_reels)

# Update tab counts
s = s.replace('3D 漫（13）', '3D 漫（1）')
s = s.replace('伪真人（11）', '伪真人（1）')
s = s.replace('二维漫（3）', '二维漫（1）')

io.open(p, 'w', encoding='utf-8').write(s)
print('deploy.html: 3 online samples, direct paths')
