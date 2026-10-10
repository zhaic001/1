# -*- coding: utf-8 -*-
import io

p = r'D:\资海春\resume-website\index.html'
s = io.open(p, encoding='utf-8').read()

path_map = {
    '../Zhaic/母亲的枷锁.jpg': 'assets/zhaic/母亲的枷锁.jpg',
    '../Zhaic/清北梦.jpg': 'assets/zhaic/清北梦.jpg',
    '../Zhaic/人物资产/修仙（男女主）/张不为.png': 'assets/zhaic/renwu/xiuzhang/张不为.jpg',
    '../Zhaic/人物资产/修仙（男女主）/张不为战损.png': 'assets/zhaic/renwu/xiuzhang/张不为战损.jpg',
    '../Zhaic/人物资产/修仙（男女主）/胡瑶瑶.png': 'assets/zhaic/renwu/xiuzhang/胡瑶瑶.jpg',
    '../Zhaic/人物资产/修仙（男女主）/胡瑶瑶（本体）.png': 'assets/zhaic/renwu/xiuzhang/胡瑶瑶本体.jpg',
    '../Zhaic/人物资产/修仙（男女主）/苏也清（日常）.png': 'assets/zhaic/renwu/xiuzhang/苏也清日常.jpg',
    '../Zhaic/人物资产/修仙（男女主）/苏也清（日常）1.png': 'assets/zhaic/renwu/xiuzhang/苏也清日常1.jpg',
    '../Zhaic/人物资产/修仙（男女主）/苏也清（日常）2.jpg': 'assets/zhaic/renwu/xiuzhang/苏也清日常2.jpg',
    '../Zhaic/人物资产/古装（男女主）/沈延.png': 'assets/zhaic/renwu/guzhuang/沈延.jpg',
    '../Zhaic/人物资产/古装（男女主）/苏锦宁（便服）.png': 'assets/zhaic/renwu/guzhuang/苏锦宁.jpg',
    '../Zhaic/人物资产/废土科技风（男女主）/林小满.jpg': 'assets/zhaic/renwu/feitu/林小满.jpg',
    '../Zhaic/人物资产/废土科技风（男女主）/裴川.jpg': 'assets/zhaic/renwu/feitu/裴川.jpg',
    '../Zhaic/人物资产/废土科技风（男女主）/3DQ版林小满.png': 'assets/zhaic/renwu/feitu/Q版林小满.jpg',
    '../Zhaic/人物资产/废土科技风（男女主）/3DQ版裴川.png': 'assets/zhaic/renwu/feitu/Q版裴川.jpg',
    '../Zhaic/人物资产/都市风（男女主）/苏凡正装.png': 'assets/zhaic/renwu/dushi/苏凡正装.jpg',
    '../Zhaic/人物资产/都市风（男女主）/苏凡.png': 'assets/zhaic/renwu/dushi/苏凡.jpg',
    '../Zhaic/人物资产/都市风（男女主）/苏凡（日常）.png': 'assets/zhaic/renwu/dushi/苏凡日常.jpg',
    '../Zhaic/人物资产/都市风（男女主）/苏凡（睡衣）.png': 'assets/zhaic/renwu/dushi/苏凡睡衣.jpg',
    '../Zhaic/人物资产/都市风（男女主）/秦璐.png': 'assets/zhaic/renwu/dushi/秦璐.jpg',
    '../Zhaic/人物资产/都市风（男女主）/秦璐（日常）.png': 'assets/zhaic/renwu/dushi/秦璐日常.jpg',
    '../Zhaic/人物资产/都市风（男女主）/秦璐（日常2）.png': 'assets/zhaic/renwu/dushi/秦璐日常2.jpg',
    '../Zhaic/人物资产/都市风（男女主）/秦璐（居家）.png': 'assets/zhaic/renwu/dushi/秦璐居家.jpg',
    '../Zhaic/音频资产/男主.mp3': 'assets/zhaic/audio/男主.mp3',
    '../Zhaic/音频资产/女-睿智女主.mp3': 'assets/zhaic/audio/女-睿智女主.mp3',
    '../Zhaic/音频资产/男-霸气.mp3': 'assets/zhaic/audio/男-霸气.mp3',
    '../Zhaic/音频资产/胡瑶瑶.mp3': 'assets/zhaic/audio/胡瑶瑶.mp3',
}

for old, new in path_map.items():
    s = s.replace(old, new)

out = r'D:\资海春\resume-website\deploy.html'
io.open(out, 'w', encoding='utf-8').write(s)
print('deploy.html ready')
