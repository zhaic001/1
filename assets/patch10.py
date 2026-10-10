# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

# 1. 改 CSS：reel 卡片带封面图
old_css = '''.reel{
  padding:14px; background:var(--card); border:1px solid var(--line); border-radius:10px;
  cursor:pointer; transition:all .15s;
}
.reel:hover{border-color:var(--accent); transform:translateY(-2px)}
.reel .play{
  width:32px; height:32px; border-radius:50%; background:var(--gold-grad);
  display:flex; align-items:center; justify-content:center; margin-bottom:10px;
}
.reel .play svg{width:14px; height:14px; fill:#1a1408; margin-left:2px}
.reel b{font-size:13.5px; display:block; margin-bottom:4px}
.reel small{color:var(--dim); font-size:11.5px}'''

new_css = '''.reel{
  background:var(--card); border:1px solid var(--line); border-radius:10px;
  cursor:pointer; transition:all .15s; overflow:hidden; padding:0;
}
.reel:hover{border-color:var(--accent); transform:translateY(-2px)}
.reel .thumb{
  position:relative; width:100%; aspect-ratio:16/9; overflow:hidden; background:#000;
}
.reel .thumb img{
  width:100%; height:100%; object-fit:cover; display:block;
  transition:transform .3s;
}
.reel:hover .thumb img{transform:scale(1.05)}
.reel .thumb::after{
  content:''; position:absolute; inset:0;
  background:linear-gradient(180deg, transparent 50%, rgba(0,0,0,.5));
}
.reel .play{
  position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
  width:40px; height:40px; border-radius:50%; background:rgba(184,134,11,.9);
  display:flex; align-items:center; justify-content:center; z-index:2;
  transition:all .2s;
}
.reel:hover .play{background:var(--gold-grad); transform:translate(-50%,-50%) scale(1.1)}
.reel .play svg{width:16px; height:16px; fill:#1a1408; margin-left:2px}
.reel .meta{padding:10px 12px 12px}
.reel b{font-size:13px; display:block; margin-bottom:3px}
.reel small{color:var(--dim); font-size:11px}'''
assert old_css in s
s = s.replace(old_css, new_css)

# 2. 改 JS：每个 item 加 cover 字段
old_3d = """  'r-3d': {
    dir: '../Zhaic/DEOM/视频作品集/3D漫/3D漫【水印】/',
    items: [
      ['3D【玄幻开场1】.mp4','玄幻开场 · 01'],
      ['3D【玄幻开场2】.mp4','玄幻开场 · 02'],
      ['3D【科幻修仙】.mp4','科幻修仙'],
      ['3D【科幻废土风格】.mp4','科幻废土'],
      ['3D【系统穿越】.mp4','系统穿越'],
      ['3D【叙事】.mp4','叙事感镜'],
      ['3D【打斗1】.mp4','打斗 · 01'],
      ['3D【打斗2】.mp4','打斗 · 02'],
      ['3D【追逐1】.mp4','追逐 · 01'],
      ['3D【追逐2】.mp4','追逐 · 02'],
      ['3D【追逐3】.mp4','追逐 · 03'],
      ['3D【恐怖】.mp4','恐怖氛围'],
      ['3D【海外女频同性】.mp4','海外女频']
    ]
  }"""
new_3d = """  'r-3d': {
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
  }"""
assert old_3d in s
s = s.replace(old_3d, new_3d)

old_real = """  'r-real': {
    dir: '../Zhaic/DEOM/视频作品集/伪真人/',
    items: [
      ['阿嫲的清北梦-第20集.mp4','阿嬷的清北梦 · EP20'],
      ['伪真人【现代悬疑】.mp4','现代悬疑'],
      ['伪真人【现代温情】.mp4','现代温情'],
      ['伪真人【现代系统】.mp4','现代系统'],
      ['伪真人【古装玄幻】.mp4','古装玄幻'],
      ['伪真人【古装搞笑】.mp4','古装搞笑'],
      ['伪真人【古装搞笑女】.mp4','古装搞笑女'],
      ['海外伪真人【现代言情】.mp4','海外 · 现代言情'],
      ['海外伪真人【现代玄幻言情】.mp4','海外 · 现代玄幻言情'],
      ['海外伪真人【古西欧言情】.mp4','海外 · 古西欧言情'],
      ['海外伪真人【古欧玄幻言情】.mp4','海外 · 古欧玄幻言情']
    ]
  }"""
new_real = """  'r-real': {
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
  }"""
assert old_real in s
s = s.replace(old_real, new_real)

old_2d = """  'r-2d': {
    dir: '../Zhaic/DEOM/视频作品集/二维漫/',
    items: [
      ['二维漫【玄幻打斗】.mp4','玄幻打斗'],
      ['二维漫【现代悬疑】.mp4','现代悬疑'],
      ['二维漫【现代类打斗】.mp4','现代打斗']
    ]
  }"""
new_2d = """  'r-2d': {
    dir: '../Zhaic/DEOM/视频作品集/二维漫/',
    items: [
      ['二维漫【玄幻打斗】.mp4','玄幻打斗','assets/reel-covers/2d_01.jpg'],
      ['二维漫【现代悬疑】.mp4','现代悬疑','assets/reel-covers/2d_02.jpg'],
      ['二维漫【现代类打斗】.mp4','现代打斗','assets/reel-covers/2d_03.jpg']
    ]
  }"""
assert old_2d in s
s = s.replace(old_2d, new_2d)

# 3. 改渲染函数：用封面图
old_render = """Object.keys(REELS).forEach(id => {
  const box = document.getElementById(id);
  REELS[id].items.forEach(([f,label]) => {
    const d = document.createElement('div');
    d.className = 'reel';
    d.innerHTML = '<div class="play"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></div><b>'+label+'</b><small>点击播放</small>';
    d.onclick = () => openVideo(REELS[id].dir + f);
    box.appendChild(d);
  });
});"""
new_render = """Object.keys(REELS).forEach(id => {
  const box = document.getElementById(id);
  REELS[id].items.forEach(([f,label,cover]) => {
    const d = document.createElement('div');
    d.className = 'reel';
    d.innerHTML = '<div class="thumb"><img src="'+cover+'" loading="lazy" alt="'+label+'"><div class="play"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></div></div><div class="meta"><b>'+label+'</b><small>点击播放</small></div>';
    d.onclick = () => openVideo(REELS[id].dir + f);
    box.appendChild(d);
  });
});"""
assert old_render in s
s = s.replace(old_render, new_render)

io.open(p, 'w', encoding='utf-8').write(s)
print('reel covers wired up, length=', len(s))
