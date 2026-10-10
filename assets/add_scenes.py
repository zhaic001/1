# -*- coding: utf-8 -*-
import io

p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

# Insert scene/empty-shot section between character assets and style matrix
anchor = '<!-- ===== STYLE MATRIX ===== -->'

scenes_html = '''<!-- ===== SCENE / EMPTY SHOTS ===== -->
<section id="scenes">
  <div class="wrap">
    <div class="sec-sub">Scene Design · 场景空镜</div>
    <h2 class="sec">沉浸式场景概念图，<span class="gold">为每个世界观搭建空间</span></h2>
    <p style="color:var(--mute);max-width:760px;margin-top:8px">
      从修仙宗门到废土舰队，从都市出租屋到集团办公厅，全流程场景概念设计与氛围定调。
    </p>
    <div class="scene-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px">
      <div class="scene-item" style="cursor:pointer" onclick="openLb('../Zhaic/场景资产/修仙/凡俗小镇铁匠铺.png')">
        <img src="../Zhaic/场景资产/修仙/凡俗小镇铁匠铺.png" alt="凡俗小镇铁匠铺" style="width:100%;height:200px;object-fit:cover;border-radius:8px">
        <div style="margin-top:8px;font-size:14px;color:var(--fg)">凡俗小镇 · 铁匠铺<small style="display:block;color:var(--mute);font-size:12px">修仙 / 市井烟火</small></div>
      </div>
      <div class="scene-item" style="cursor:pointer" onclick="openLb('../Zhaic/场景资产/修仙/秘境地下兵器库青铜阶梯通道.png')">
        <img src="../Zhaic/场景资产/修仙/秘境地下兵器库青铜阶梯通道.png" alt="秘境兵器库" style="width:100%;height:200px;object-fit:cover;border-radius:8px">
        <div style="margin-top:8px;font-size:14px;color:var(--fg)">秘境 · 地下兵器库<small style="display:block;color:var(--mute);font-size:12px">修仙 / 密室机关</small></div>
      </div>
      <div class="scene-item" style="cursor:pointer" onclick="openLb('../Zhaic/场景资产/修仙/青云宗演武场.png')">
        <img src="../Zhaic/场景资产/修仙/青云宗演武场.png" alt="青云宗演武场" style="width:100%;height:200px;object-fit:cover;border-radius:8px">
        <div style="margin-top:8px;font-size:14px;color:var(--fg)">青云宗 · 演武场<small style="display:block;color:var(--mute);font-size:12px">修仙 / 宗门大场面</small></div>
      </div>
      <div class="scene-item" style="cursor:pointer" onclick="openLb('../Zhaic/场景资产/废土风/垃圾交易点.png')">
        <img src="../Zhaic/场景资产/废土风/垃圾交易点.png" alt="垃圾交易点" style="width:100%;height:200px;object-fit:cover;border-radius:8px">
        <div style="margin-top:8px;font-size:14px;color:var(--fg)">废土 · 垃圾交易点<small style="display:block;color:var(--mute);font-size:12px">废土 / 黑市交易</small></div>
      </div>
      <div class="scene-item" style="cursor:pointer" onclick="openLb('../Zhaic/场景资产/废土风/离舰出口 舷窗.jpg')">
        <img src="../Zhaic/场景资产/废土风/离舰出口 舷窗.jpg" alt="离舰舷窗" style="width:100%;height:200px;object-fit:cover;border-radius:8px">
        <div style="margin-top:8px;font-size:14px;color:var(--fg)">废土 · 离舰舷窗<small style="display:block;color:var(--mute);font-size:12px">废土 / 太空舰舱</small></div>
      </div>
      <div class="scene-item" style="cursor:pointer" onclick="openLb('../Zhaic/场景资产/废土风/舰队通讯舱.jpg')">
        <img src="../Zhaic/场景资产/废土风/舰队通讯舱.jpg" alt="舰队通讯舱" style="width:100%;height:200px;object-fit:cover;border-radius:8px">
        <div style="margin-top:8px;font-size:14px;color:var(--fg)">废土 · 舰队通讯舱<small style="display:block;color:var(--mute);font-size:12px">废土 / 指挥中枢</small></div>
      </div>
      <div class="scene-item" style="cursor:pointer" onclick="openLb('../Zhaic/场景资产/都市爽剧/公司楼下街道.png')">
        <img src="../Zhaic/场景资产/都市爽剧/公司楼下街道.png" alt="公司楼下街道" style="width:100%;height:200px;object-fit:cover;border-radius:8px">
        <div style="margin-top:8px;font-size:14px;color:var(--fg)">都市 · 公司楼下街道<small style="display:block;color:var(--mute);font-size:12px">都市 / 通勤日常</small></div>
      </div>
      <div class="scene-item" style="cursor:pointer" onclick="openLb('../Zhaic/场景资产/都市爽剧/华腾集团一楼大办公厅.png')">
        <img src="../Zhaic/场景资产/都市爽剧/华腾集团一楼大办公厅.png" alt="华腾集团办公厅" style="width:100%;height:200px;object-fit:cover;border-radius:8px">
        <div style="margin-top:8px;font-size:14px;color:var(--fg)">都市 · 华腾集团办公厅<small style="display:block;color:var(--mute);font-size:12px">都市 / 商业权力场</small></div>
      </div>
      <div class="scene-item" style="cursor:pointer" onclick="openLb('../Zhaic/场景资产/都市爽剧/苏凡出租屋.png')">
        <img src="../Zhaic/场景资产/都市爽剧/苏凡出租屋.png" alt="苏凡出租屋" style="width:100%;height:200px;object-fit:cover;border-radius:8px">
        <div style="margin-top:8px;font-size:14px;color:var(--fg)">都市 · 苏凡出租屋<small style="display:block;color:var(--mute);font-size:12px">都市 / 主角私密空间</small></div>
      </div>
    </div>
  </div>
</section>

'''

s = s.replace(anchor, scenes_html + anchor)
io.open(p, 'w', encoding='utf-8').write(s)
print('scene section inserted')
