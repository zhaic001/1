# -*- coding: utf-8 -*-
import os, shutil, io

ROOT = r'D:\资海春'
SRC = os.path.join(ROOT, 'Zhaic')
DST = os.path.join(ROOT, 'resume-website', 'assets', 'zhaic')
os.makedirs(DST, exist_ok=True)

# 要复制的文件列表（图片和音频，视频太大不复制）
files = [
    # 海报
    (r'母亲的枷锁.jpg', r'母亲的枷锁.jpg'),
    (r'清北梦.jpg', r'清北梦.jpg'),
    # 人物资产 - 修仙
    (r'人物资产\修仙（男女主）\张不为.png', r'renwu\xiuzhang\张不为.png'),
    (r'人物资产\修仙（男女主）\张不为战损.png', r'renwu\xiuzhang\张不为战损.png'),
    (r'人物资产\修仙（男女主）\胡瑶瑶.png', r'renwu\xiuzhang\胡瑶瑶.png'),
    (r'人物资产\修仙（男女主）\胡瑶瑶（本体）.png', r'renwu\xiuzhang\胡瑶瑶本体.png'),
    (r'人物资产\修仙（男女主）\苏也清（日常）.png', r'renwu\xiuzhang\苏也清日常.png'),
    (r'人物资产\修仙（男女主）\苏也清（日常）1.png', r'renwu\xiuzhang\苏也清日常1.png'),
    (r'人物资产\修仙（男女主）\苏也清（日常）2.jpg', r'renwu\xiuzhang\苏也清日常2.jpg'),
    # 人物资产 - 古装
    (r'人物资产\古装（男女主）\沈延.png', r'renwu\guzhuang\沈延.png'),
    (r'人物资产\古装（男女主）\苏锦宁（便服）.png', r'renwu\guzhuang\苏锦宁.png'),
    # 人物资产 - 废土
    (r'人物资产\废土科技风（男女主）\林小满.jpg', r'renwu\feitu\林小满.jpg'),
    (r'人物资产\废土科技风（男女主）\裴川.jpg', r'renwu\feitu\裴川.jpg'),
    (r'人物资产\废土科技风（男女主）\3DQ版林小满.png', r'renwu\feitu\Q版林小满.png'),
    (r'人物资产\废土科技风（男女主）\3DQ版裴川.png', r'renwu\feitu\Q版裴川.png'),
    # 人物资产 - 都市
    (r'人物资产\都市风（男女主）\苏凡正装.png', r'renwu\dushi\苏凡正装.png'),
    (r'人物资产\都市风（男女主）\苏凡.png', r'renwu\dushi\苏凡.png'),
    (r'人物资产\都市风（男女主）\苏凡（日常）.png', r'renwu\dushi\苏凡日常.png'),
    (r'人物资产\都市风（男女主）\苏凡（睡衣）.png', r'renwu\dushi\苏凡睡衣.png'),
    (r'人物资产\都市风（男女主）\秦璐.png', r'renwu\dushi\秦璐.png'),
    (r'人物资产\都市风（男女主）\秦璐（日常）.png', r'renwu\dushi\秦璐日常.png'),
    (r'人物资产\都市风（男女主）\秦璐（日常2）.png', r'renwu\dushi\秦璐日常2.png'),
    (r'人物资产\都市风（男女主）\秦璐（居家）.png', r'renwu\dushi\秦璐居家.png'),
    # 音频
    (r'音频资产\男主.mp3', r'audio\男主.mp3'),
    (r'音频资产\女-睿智女主.mp3', r'audio\女-睿智女主.mp3'),
    (r'音频资产\男-霸气.mp3', r'audio\男-霸气.mp3'),
    (r'音频资产\胡瑶瑶.mp3', r'audio\胡瑶瑶.mp3'),
]

count = 0
for rel_src, rel_dst in files:
    s = os.path.join(SRC, rel_src)
    d = os.path.join(DST, rel_dst)
    os.makedirs(os.path.dirname(d), exist_ok=True)
    if os.path.exists(s):
        shutil.copy2(s, d)
        count += 1
    else:
        print(f'MISS: {rel_src}')

print(f'copied {count} files to {DST}')
