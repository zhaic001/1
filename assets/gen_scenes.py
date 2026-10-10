# -*- coding: utf-8 -*-
import cv2, os

out_dir = r'D:\资海春\resume-website\assets\deploy_assets\scenes'
os.makedirs(out_dir, exist_ok=True)

scenes = [
    (r'D:\资海春\Zhaic\场景资产\修仙\凡俗小镇铁匠铺.png', 'xiuzhen_smithy.jpg', '凡俗小镇 · 铁匠铺'),
    (r'D:\资海春\Zhaic\场景资产\修仙\秘境地下兵器库青铜阶梯通道.png', 'xiuzhen_armory.jpg', '秘境 · 地下兵器库'),
    (r'D:\资海春\Zhaic\场景资产\修仙\青云宗演武场.png', 'xiuzhen_ground.jpg', '青云宗 · 演武场'),
    (r'D:\资海春\Zhaic\场景资产\废土风\垃圾交易点.png', 'feitu_market.jpg', '废土 · 垃圾交易点'),
    (r'D:\资海春\Zhaic\场景资产\废土风\离舰出口 舷窗.jpg', 'feitu_hatch.jpg', '废土 · 离舰舷窗'),
    (r'D:\资海春\Zhaic\场景资产\废土风\舰队通讯舱.jpg', 'feitu_comms.jpg', '废土 · 舰队通讯舱'),
    (r'D:\资海春\Zhaic\场景资产\都市爽剧\公司楼下街道.png', 'dushi_street.jpg', '都市 · 公司楼下街道'),
    (r'D:\资海春\Zhaic\场景资产\都市爽剧\华腾集团一楼大办公厅.png', 'dushi_office.jpg', '都市 · 华腾集团办公厅'),
    (r'D:\资海春\Zhaic\场景资产\都市爽剧\苏凡出租屋.png', 'dushi_rental.jpg', '都市 · 苏凡出租屋'),
]

for src, outname, label in scenes:
    if not os.path.exists(src):
        print(f'MISS: {outname}')
        continue
    outpath = os.path.join(out_dir, outname)
    if os.path.exists(outpath):
        print(f'SKIP: {outname}')
        continue
    # Read with Chinese path support
    data = np.fromfile(src, dtype=np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if img is None:
        print(f'DECODE FAIL: {outname}')
        continue
    h, w = img.shape[:2]
    scale = 900 / w
    img = cv2.resize(img, (900, int(h * scale)))
    ok, buf = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 78])
    if ok:
        buf.tofile(outpath)
        sz = os.path.getsize(outpath) // 1024
        print(f'OK: {outname} ({sz}KB) - {label}')

print('done')
