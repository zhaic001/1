# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

# 1. 改标题
s = s.replace(
    '<h2 class="sec">从游戏原画到 AI 漫剧总导演</h2>',
    '<h2 class="sec">从摄影师、平面设计师到 AI 短剧编导</h2>')

# 2. 时间轴：入行起点改为摄影师
s = s.replace(
    '''          <h4>游戏原画师</h4>
          <div class="co">广州点金坊游戏有限公司</div>
          <p>角色与场景原画训练，打下美术底子。</p>''',
    '''          <h4>摄影师 / 摄影摄像</h4>
          <div class="co">商业摄影 / 活动拍摄方向</div>
          <p>自带索尼相机，承接人物、活动、产品与新媒体素材拍摄，练出构图与布光功底。</p>''')

# 3. 平面设计主管加 UI 设计
s = s.replace(
    '''          <h4>平面设计部门主管</h4>
          <div class="co">广州九圆塑业有限公司</div>
          <p>带领设计部门完成品牌视觉与物料体系。</p>''',
    '''          <h4>平面设计师 / 设计部门主管</h4>
          <div class="co">广州九圆塑业有限公司</div>
          <p>负责品牌视觉、物料与 UI 设计，带领设计部门完成平面设计全案。</p>''')

# 4. tags 加摄影/平面/UI
s = s.replace(
    '''        <div class="skill-tags">
          <span class="tag g">0→1 团队搭建</span>
          <span class="tag g">60+ 人培养体系</span>
          <span class="tag">标准化流程</span>
          <span class="tag">质量验收门</span>
          <span class="tag">排期与里程碑</span>
        </div>''',
    '''        <div class="skill-tags">
          <span class="tag g">摄影摄像</span>
          <span class="tag g">平面设计</span>
          <span class="tag g">UI 设计</span>
          <span class="tag">0→1 团队搭建</span>
          <span class="tag">60+ 人培养</span>
          <span class="tag">标准化流程</span>
        </div>''')

# 5. 教育背景：大专 + 中专升大专
s = s.replace(
    '<h4>湖南工艺美术职业大学</h4>',
    '<h4>湖南工艺美术职业大学 · 大专</h4>')
s = s.replace(
    '系统学习视觉传达、广告创意、新媒体策划与内容生产，毕业设计聚焦现实主义电影级分镜，\n          具备从创意到成片的完整训练。',
    '从中专一路读到大专，系统训练平面设计、摄影摄像与 UI 设计基本功；\n          毕业设计聚焦现实主义电影级分镜，具备从创意到成片的完整训练。')

io.open(p, 'w', encoding='utf-8').write(s)
print('OK')
