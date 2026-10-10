# -*- coding: utf-8 -*-
import io

p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()

# Replace REELS with all 26 videos pointing to deployed paths
old_reels_start = "const REELS = {"
old_reels_end = "};"

# Find and replace the whole REELS block
import re
pattern = r'const REELS = \{.*?\};'
new_reels = """const REELS = {
  'r-3d': {
    dir: '',
    items: [
      ['assets/deploy_assets/reels/3d_01.mp4','玄幻开场 · 01','assets/reel-covers/3d_01.jpg'],
      ['assets/deploy_assets/reels/3d_02.mp4','玄幻开场 · 02','assets/reel-covers/3d_02.jpg'],
      ['assets/deploy_assets/reels/3d_03.mp4','科幻修仙','assets/reel-covers/3d_03.jpg'],
      ['assets/deploy_assets/reels/3d_04.mp4','科幻废土','assets/reel-covers/3d_04.jpg'],
      ['assets/deploy_assets/reels/3d_05.mp4','系统穿越','assets/reel-covers/3d_05.jpg'],
      ['assets/deploy_assets/reels/3d_06.mp4','叙事感镜','assets/reel-covers/3d_06.jpg'],
      ['assets/deploy_assets/reels/3d_07.mp4','打斗 · 01','assets/reel-covers/3d_07.jpg'],
      ['assets/deploy_assets/reels/3d_08.mp4','打斗 · 02','assets/reel-covers/3d_08.jpg'],
      ['assets/deploy_assets/reels/3d_09.mp4','追逐 · 01','assets/reel-covers/3d_09.jpg'],
      ['assets/deploy_assets/reels/3d_10.mp4','追逐 · 02','assets/reel-covers/3d_10.jpg'],
      ['assets/deploy_assets/reels/3d_11.mp4','追逐 · 03','assets/reel-covers/3d_11.jpg'],
      ['assets/deploy_assets/reels/3d_12.mp4','恐怖氛围','assets/reel-covers/3d_12.jpg'],
      ['assets/deploy_assets/reels/3d_13.mp4','海外女频','assets/reel-covers/3d_13.jpg']
    ]
  },
  'r-real': {
    dir: '',
    items: [
      ['assets/deploy_assets/reels/real_01.mp4','阿嬷的清北梦 · EP20','assets/reel-covers/real_01.jpg'],
      ['assets/deploy_assets/reels/real_02.mp4','古装搞笑女','assets/reel-covers/real_07.jpg'],
      ['assets/deploy_assets/reels/real_03.mp4','现代温情','assets/reel-covers/real_05.jpg'],
      ['assets/deploy_assets/reels/real_04.mp4','现代系统','assets/reel-covers/real_04.jpg'],
      ['assets/deploy_assets/reels/real_05.mp4','古装玄幻','assets/reel-covers/real_03.jpg'],
      ['assets/deploy_assets/reels/real_06.mp4','古装搞笑','assets/reel-covers/real_06.jpg'],
      ['assets/deploy_assets/reels/real_07.mp4','海外 · 现代言情','assets/reel-covers/real_10.jpg'],
      ['assets/deploy_assets/reels/real_08.mp4','海外 · 现代玄幻言情','assets/reel-covers/real_09.jpg'],
      ['assets/deploy_assets/reels/real_09.mp4','海外 · 古西欧言情','assets/reel-covers/real_08.jpg'],
      ['assets/deploy_assets/reels/real_10.mp4','海外 · 古欧玄幻言情','assets/reel-covers/real_07.jpg']
    ]
  },
  'r-2d': {
    dir: '',
    items: [
      ['assets/deploy_assets/reels/2d_01.mp4','玄幻打斗','assets/reel-covers/2d_01.jpg'],
      ['assets/deploy_assets/reels/2d_02.mp4','现代悬疑','assets/reel-covers/2d_02.jpg'],
      ['assets/deploy_assets/reels/2d_03.mp4','现代打斗','assets/reel-covers/2d_03.jpg']
    ]
  }
};"""

s = re.sub(pattern, new_reels, s, count=1, flags=re.DOTALL)

# Update tab counts
s = s.replace('3D 漫（1）', '3D 漫（13）')
s = s.replace('伪真人（1）', '伪真人（10）')
s = s.replace('二维漫（1）', '二维漫（3）')

io.open(p, 'w', encoding='utf-8').write(s)
print('REELS updated: all 26 videos online')
