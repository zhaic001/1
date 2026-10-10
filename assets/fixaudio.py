# -*- coding: utf-8 -*-
import io
p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace('../Zhaic/音频资产/男主.mp3', 'assets/deploy_assets/audio/male_lead')
s = s.replace('../Zhaic/音频资产/女-睿智女主.mp3', 'assets/deploy_assets/audio/female_wise')
s = s.replace('../Zhaic/音频资产/男-霸气.mp3', 'assets/deploy_assets/audio/male_boss')
s = s.replace('../Zhaic/音频资产/胡瑶瑶.mp3', 'assets/deploy_assets/audio/huyaoyao')
io.open(p, 'w', encoding='utf-8').write(s)
print('audio paths fixed')
