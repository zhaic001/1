# -*- coding: utf-8 -*-
import os, shutil, io, cv2, numpy as np

# 把 zhaic 目录里的文件全部改成英文文件名，同步更新 deploy.html
SRC = r'D:\资海春\resume-website\assets\zhaic'
DST = r'D:\资海春\resume-website\assets\deploy_assets'
if os.path.exists(DST):
    shutil.rmtree(DST)
os.makedirs(DST, exist_ok=True)

# 映射：中文路径 -> 英文文件名
name_map = {}

# 遍历收集所有文件
for dirpath, dirs, files in os.walk(SRC):
    for f in files:
        old = os.path.join(dirpath, f)
        rel = os.path.relpath(old, SRC).replace('\\', '/')
        # 生成英文名
        # 分类
        parts = rel.split('/')
        ext = os.path.splitext(f)[1].lower()
        if rel.startswith('renwu/xiuzhang/'):
            base = parts[-1].rsplit('.',1)[0]
            en = {
                '张不为':'zhangbuwei','张不为战损':'zhangbuwei_dmg',
                '胡瑶瑶':'huyaoyao','胡瑶瑶本体':'huyaoyao_orig',
                '苏也清日常':'suyeqing','苏也清日常1':'suyeqing_b',
                '苏也清日常2':'suyeqing_c'
            }.get(base, base)
            new = f'renwu/xiuzhang/{en}.jpg'
        elif rel.startswith('renwu/guzhuang/'):
            base = parts[-1].rsplit('.',1)[0]
            en = {'沈延':'shenyan','苏锦宁':'sujinning'}.get(base, base)
            new = f'renwu/guzhuang/{en}.jpg'
        elif rel.startswith('renwu/feitu/'):
            base = parts[-1].rsplit('.',1)[0]
            en = {'林小满':'linxiaoman','裴川':'peichuan',
                  'Q版林小满':'linxiaoman_chibi','Q版裴川':'peichuan_chibi'}.get(base, base)
            new = f'renwu/feitu/{en}.jpg'
        elif rel.startswith('renwu/dushi/'):
            base = parts[-1].rsplit('.',1)[0]
            en = {'苏凡正装':'sufan_suit','苏凡':'sufan','苏凡日常':'sufan_casual',
                  '苏凡睡衣':'sufan_pajama','秦璐':'qinlu','秦璐日常':'qinlu_casual',
                  '秦璐日常2':'qinlu_casual2','秦璐居家':'qinlu_home'}.get(base, base)
            new = f'renwu/dushi/{en}.jpg'
        elif rel.startswith('audio/'):
            en = {'男主':'male_lead','女-睿智女主':'female_wise',
                  '男-霸气':'male_boss','胡瑶瑶':'huyaoyao'}.get(parts[-1].rsplit('.',1)[0], parts[-1])
            new = f'audio/{en}'
        elif rel == '母亲的枷锁.jpg':
            new = 'mama.jpg'
        elif rel == '清北梦.jpg':
            new = 'qingbei.jpg'
        else:
            new = rel

        dst_path = os.path.join(DST, new.replace('/', os.sep))
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.copy2(old, dst_path)
        # 记录映射：HTML 里旧路径 -> 新路径
        old_html = 'assets/zhaic/' + rel
        new_html = 'assets/deploy_assets/' + new
        name_map[old_html] = new_html
        print(f'{rel} -> {new}')

# 更新 deploy.html
p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()
for old, new in name_map.items():
    s = s.replace(old, new)
io.open(p, 'w', encoding='utf-8').write(s)
print('deploy.html updated with English paths')
