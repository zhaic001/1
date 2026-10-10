# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

career_html = '''<!-- ===== CAREER TIMELINE ===== -->
<section id="career">
  <div class="wrap">
    <div class="sec-sub">Career · 从业经历</div>
    <h2 class="sec">从游戏原画到 AI 漫剧总导演</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:36px">
      <div class="tl">
        <div class="tl-item">
          <div class="when">最新 · 2025–2026</div>
          <h4>AI 漫剧总导演</h4>
          <div class="co">广州从一到九文化传媒有限公司</div>
          <p>统筹 30+ 部 AI 漫剧项目全局质量与排期，覆盖都市、玄幻、逆袭、古风题材；
          培养 60+ 名跨行剪辑师从流水线新手成长为专业剪辑师；
          建立标准化制作流程与质量验收体系。</p>
        </div>
        <div class="tl-item">
          <div class="when">前一段</div>
          <h4>AI 漫剧策划师</h4>
          <div class="co">广州澳梦深蓝科技有限公司</div>
          <p>从选题、剧本、分镜到 AI 生成全链路参与，以 3D 漫为核心竞争力，
          建立伪真人 / 3D 漫 / 二维漫三种风格可复用的制作标准与爆款方法论。</p>
        </div>
        <div class="tl-item">
          <div class="when">更早</div>
          <h4>平面设计部门主管</h4>
          <div class="co">广州九圆塑业有限公司</div>
          <p>带领设计部门完成品牌视觉与物料体系。</p>
        </div>
        <div class="tl-item">
          <div class="when">入行起点</div>
          <h4>游戏原画师</h4>
          <div class="co">广州点金坊游戏有限公司</div>
          <p>角色与场景原画训练，打下美术底子。</p>
        </div>
      </div>
      <div>
        <div class="sec-sub" style="margin-bottom:14px">核心职责</div>
        <p style="color:var(--mute);font-size:14.5px;line-height:2;margin-bottom:16px">
          负责公司 AI 漫剧项目组<b style="color:var(--text)">全局质量把控与统筹工作</b>，
          覆盖都市、玄幻、逆袭、古风等题材，主攻<b style="color:var(--accent)">伪真人、3D 漫、二维漫三种视觉风格</b>，
          以 3D 漫为核心竞争力。
        </p>
        <p style="color:var(--mute);font-size:14.5px;line-height:2;margin-bottom:16px">
          从<b style="color:var(--text)">选题、剧本、分镜、AI 生成、动态制作、配音、音效到成片发布</b>全链路把控。
          制定排期表、里程碑节点与质检标准；管理编剧、画面美术、前期 AI 资产、剪辑、配音、后期高清等协作环节，
          建立反馈与修改机制，减少无效返工。
        </p>
        <div class="skill-tags">
          <span class="tag g">0→1 团队搭建</span>
          <span class="tag g">60+ 人培养体系</span>
          <span class="tag">标准化流程</span>
          <span class="tag">质量验收门</span>
          <span class="tag">排期与里程碑</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===== WORKS ===== -->'''

old = '<!-- ===== WORKS ===== -->'
assert s.count(old) == 1, f'count={s.count(old)}'
s = s.replace(old, career_html, 1)

io.open(p, 'w', encoding='utf-8').write(s)
print('career inserted, length=', len(s))
