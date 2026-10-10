# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

# 加 CSS：样片按钮网格
css_add = '''
/* ===== REEL GRID ===== */
.reel-tabs{display:flex;gap:10px;margin:24px 0 20px;flex-wrap:wrap}
.reel-tab{
  padding:10px 20px; border-radius:999px; cursor:pointer; font-size:14px;
  background:var(--card); border:1px solid var(--line); color:var(--mute); transition:all .2s;
}
.reel-tab.on{background:var(--gold-grad); color:#1a1408; font-weight:600; border-color:transparent}
.reel-grid{display:none; grid-template-columns:repeat(auto-fill,minmax(200px,1fr)); gap:12px}
.reel-grid.on{display:grid}
.reel{
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
.reel small{color:var(--dim); font-size:11.5px}
'''
s = s.replace('/* ===== AUDIO ===== */', css_add + '\n/* ===== AUDIO ===== */', 1)

# 插入视频作品集板块（在 style matrix 之后、audio 之前）
reel_html = '''<!-- ===== REEL / SAMPLE VIDEOS ===== -->
<section id="reel">
  <div class="wrap">
    <div class="sec-sub">Showreel · 视频样片</div>
    <h2 class="sec">三种画风样片，<span class="gold">点击即播</span></h2>
    <p style="color:var(--mute);max-width:760px;margin-top:8px">
      按画风分组的代表作片段，涵盖玄幻/恐怖/追逐/打斗/系统/温情/悬疑/海外言情等题材。
    </p>
    <div class="reel-tabs">
      <div class="reel-tab on" data-t="r-3d">3D 漫（13）</div>
      <div class="reel-tab" data-t="r-real">伪真人（11）</div>
      <div class="reel-tab" data-t="r-2d">二维漫（3）</div>
    </div>
    <div class="reel-grid on" id="r-3d"></div>
    <div class="reel-grid" id="r-real"></div>
    <div class="reel-grid" id="r-2d"></div>
  </div>
</section>

<!-- ===== AUDIO ===== -->'''
s = s.replace('<!-- ===== AUDIO ===== -->', reel_html, 1)

# 在 JS 里加样片数据和渲染
old_js_end = "document.addEventListener('keydown', function(e){"
new_js = '''/* ===== 样片视频数据 ===== */
const REELS = {
  'r-3d': {
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
  },
  'r-real': {
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
  },
  'r-2d': {
    dir: '../Zhaic/DEOM/视频作品集/二维漫/',
    items: [
      ['二维漫【玄幻打斗】.mp4','玄幻打斗'],
      ['二维漫【现代悬疑】.mp4','现代悬疑'],
      ['二维漫【现代类打斗】.mp4','现代打斗']
    ]
  }
};
Object.keys(REELS).forEach(id => {
  const box = document.getElementById(id);
  REELS[id].items.forEach(([f,label]) => {
    const d = document.createElement('div');
    d.className = 'reel';
    d.innerHTML = '<div class="play"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></div><b>'+label+'</b><small>点击播放</small>';
    d.onclick = () => openVideo(REELS[id].dir + f);
    box.appendChild(d);
  });
});
document.querySelectorAll('.reel-tab').forEach(t => {
  t.onclick = () => {
    document.querySelectorAll('.reel-tab').forEach(x => x.classList.remove('on'));
    document.querySelectorAll('.reel-grid').forEach(x => x.classList.remove('on'));
    t.classList.add('on');
    document.getElementById(t.dataset.t).classList.add('on');
  };
});

document.addEventListener('keydown', function(e){'''
s = s.replace(old_js_end, new_js, 1)

io.open(p, 'w', encoding='utf-8').write(s)
print('reel section added, length=', len(s))
