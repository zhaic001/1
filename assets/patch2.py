# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

style_html = '''<!-- ===== STYLE MATRIX ===== -->
<section id="styles">
  <div class="wrap">
    <div class="sec-sub">Style Matrix · 视觉风格掌控</div>
    <h2 class="sec">三种画风无缝切换，<span class="gold">3D 漫为核心竞争力</span></h2>
    <p style="color:var(--mute);max-width:760px;margin-top:8px">
      具备 0→1 搭建成熟制作团队的经验，可快速组建并培养生图、分镜、美术、后期剪辑等核心岗位。
      在角色建模、光影渲染、镜头语言及战斗场面制作上具一流水准。
    </p>
    <div class="style-grid">
      <div class="style-card">
        <span class="sc-tag real">核心 · CORE</span>
        <h4>3D 漫</h4>
        <ul>
          <li>人物三视图 / 场景四视图标准化产出</li>
          <li>日常化剧本 → A 风格细腻表情</li>
          <li>架空玄幻剧本 → B 风格电影质感</li>
          <li>角色建模、光影渲染、战斗场面一流</li>
        </ul>
        <div class="core">★ 主力画风 · 以此承接绝大多数项目</div>
      </div>
      <div class="style-card">
        <span class="sc-tag real">写实 · REAL</span>
        <h4>伪真人</h4>
        <ul>
          <li>皮肤肌理把控，解决 AI "油脸"问题</li>
          <li>自主改前置 + 全局组提示词</li>
          <li>人物与场景建立真实光追关系</li>
          <li>从源头保证不假、不油、整体质感</li>
        </ul>
        <div class="core">适合：都市 / 现实主义 / 犯罪题材</div>
      </div>
      <div class="style-card">
        <span class="sc-tag anime">二次元 · 2D</span>
        <h4>二维漫</h4>
        <ul>
          <li>玄幻 / 日漫 / 赛博题材风格化产出</li>
          <li>《神仙饭店》《富家少爷重生败家系统》</li>
          <li>人物设定 + 场景概念图全套</li>
        </ul>
        <div class="core">适合：二次元玄幻 / 游戏改编</div>
      </div>
    </div>
  </div>
</section>

<!-- ===== AUDIO ===== -->'''

old = '<!-- ===== AUDIO ===== -->'
assert s.count(old) == 1, f'count={s.count(old)}'
s = s.replace(old, style_html, 1)

# 网盘链接加进 footer
old_footer = '      <a href="assets/resume.pdf" download="资海春-简历.pdf">下载 PDF 简历</a>'
new_footer = '''      <a href="https://pan.baidu.com/s/1cj88w34roJMMi8BdWxvBDg?pwd=hqxd" target="_blank" rel="noopener">百度网盘 · 视频作品集 (提取码 hqxd)</a>
      <a href="assets/resume.pdf" download="资海春-简历.pdf">下载 PDF 简历</a>'''
assert s.count(old_footer) == 1
s = s.replace(old_footer, new_footer, 1)

# nav 加导演战绩链接
old_nav = '<a href="#about">关于</a>\n      <a href="#works">作品</a>'
new_nav = '<a href="#about">关于</a>\n      <a href="#hits">战绩</a>\n      <a href="#career">经历</a>\n      <a href="#works">作品</a>'
s = s.replace(old_nav, new_nav, 1)

io.open(p, 'w', encoding='utf-8').write(s)
print('style+footer+nav inserted, length=', len(s))
