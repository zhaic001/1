# -*- coding: utf-8 -*-
import io

p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

anchor = '<!-- ===== STYLE MATRIX ===== -->'

wedding_html = '''<!-- ===== WEDDING / PHOTOGRAPHY ===== -->
<section id="wedding">
  <div class="wrap">
    <div class="sec-sub">Photography · 摄影摄像作品</div>
    <h2 class="sec">从婚礼纪实到 AI 短剧，<span class="gold">摄影基本功贯穿始终</span></h2>
    <p style="color:var(--mute);max-width:760px;margin-top:8px">
      自主承接婚庆拍摄期间，独立完成跟拍、运镜、剪辑全流程。以下为婚礼纪实短片样片。
    </p>
    <div style="margin-top:28px;max-width:800px">
      <div style="position:relative;border-radius:12px;overflow:hidden;cursor:pointer" onclick="openVideo('../Zhaic/婚庆拍摄/婚礼.mp4')">
        <img src="../Zhaic/婚庆拍摄/婚礼.mp4" alt="婚礼纪实" style="width:100%;display:block;object-fit:cover;aspect-ratio:16/9">
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.3)">
          <div style="width:64px;height:64px;border-radius:50%;background:rgba(255,255,255,0.9);display:flex;align-items:center;justify-content:center">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#1a1a1a"><path d="M8 5v14l11-7z"/></svg>
          </div>
        </div>
      </div>
      <div style="margin-top:12px;font-size:15px;color:var(--fg)">婚礼纪实短片<small style="display:block;color:var(--mute);font-size:13px;margin-top:4px">独立跟拍 · 现场运镜 · 后期剪辑</small></div>
    </div>
  </div>
</section>

'''

s = s.replace(anchor, wedding_html + anchor)
io.open(p, 'w', encoding='utf-8').write(s)
print('wedding section added')
