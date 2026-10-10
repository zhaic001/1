# -*- coding: utf-8 -*-
import cv2, os
import numpy as np

out_dir = r'D:\资海春\resume-website\assets\deploy_assets\scenes'
os.makedirs(out_dir, exist_ok=True)

scenes = [
    (r'D:\资海春\Zhaic\场景资产\修仙\凡俗小镇铁匠铺.png', 'xiuzhen_smithy.jpg'),
    (r'D:\资海春\Zhaic\场景资产\修仙\秘境地下兵器库青铜阶梯通道.png', 'xiuzhen_armory.jpg'),
    (r'D:\资海春\Zhaic\场景资产\修仙\青云宗演武场.png', 'xiuzhen_ground.jpg'),
    (r'D:\资海春\Zhaic\场景资产\废土风\垃圾交易点.png', 'feitu_market.jpg'),
    (r'D:\资海春\Zhaic\场景资产\废土风\离舰出口 舷窗.jpg', 'feitu_hatch.jpg'),
    (r'D:\资海春\Zhaic\场景资产\废土风\舰队通讯舱.jpg', 'feitu_comms.jpg'),
    (r'D:\资海春\Zhaic\场景资产\都市爽剧\公司楼下街道.png', 'dushi_street.jpg'),
    (r'D:\资海春\Zhaic\场景资产\都市爽剧\华腾集团一楼大办公厅.png', 'dushi_office.jpg'),
    (r'D:\资海春\Zhaic\场景资产\都市爽剧\苏凡出租屋.png', 'dushi_rental.jpg'),
]

for src, outname in scenes:
    if not os.path.exists(src):
        print('MISS:', outname)
        continue
    outpath = os.path.join(out_dir, outname)
    if os.path.exists(outpath):
        print('SKIP:', outname)
        continue
    data = np.fromfile(src, dtype=np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if img is None:
        print('DECODE FAIL:', outname)
        continue
    h, w = img.shape[:2]
    scale = 900 / w
    img = cv2.resize(img, (900, int(h * scale)))
    ok, buf = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 78])
    if ok:
        buf.tofile(outpath)
        print('OK:', outname, os.path.getsize(outpath)//1024, 'KB')
print('done')
