# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\assets\build_pdf.py'
s = io.open(p, encoding='utf-8').read()
s = s.replace('AI 漫剧总导演', 'AI 短剧编导 / 总导演')
s = s.replace('平面设计部门主管', '平面设计师 / 设计主管')
s = s.replace('品牌视觉与物料体系。', '品牌视觉、物料与 UI 设计，带领设计部门完成平面全案。')
s = s.replace('游戏原画师', '摄影师 / 摄影摄像')
s = s.replace('广州点金坊游戏有限公司', '商业摄影方向')
s = s.replace('角色与场景原画，打下美术底子。', '自带索尼相机承接人物/活动/产品拍摄，练出构图与布光功底。')
s = s.replace('湖南工艺美术职业大学 · 视觉传播设计学院', '湖南工艺美术职业大学 · 大专 · 视觉传播设计学院')
old_award = "bullet('国家励志奖学金"
new_award = "bullet('从中专一路读到大专，系统训练平面设计、摄影摄像与 UI 设计基本功', s_s)\nbullet('国家励志奖学金"
s = s.replace(old_award, new_award, 1)
io.open(p, 'w', encoding='utf-8').write(s)
print('pdf script patched')
