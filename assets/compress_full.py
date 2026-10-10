# -*- coding: utf-8 -*-
import cv2, os

out_dir = r'D:\资海春\resume-website\assets\deploy_assets\reels'
os.makedirs(out_dir, exist_ok=True)

videos = [
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第41集.mp4', 'ep_guzhuang_41.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第42集.mp4', 'ep_guzhuang_42.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第43集.mp4', 'ep_guzhuang_43.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第44集.mp4', 'ep_guzhuang_44.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第45集.mp4', 'ep_guzhuang_45.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第46集.mp4', 'ep_guzhuang_46.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第47集.mp4', 'ep_guzhuang_47.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第48集.mp4', 'ep_guzhuang_48.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第49集.mp4', 'ep_guzhuang_49.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第50集.mp4', 'ep_guzhuang_50.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第51集.mp4', 'ep_guzhuang_51.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第52集.mp4', 'ep_guzhuang_52.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第53集.mp4', 'ep_guzhuang_53.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第54集.mp4', 'ep_guzhuang_54.mp4'),
    (r'D:\资海春\Zhaic\成片\古装\假婚之后，我跟我爹的马甲要掉了-第55集.mp4', 'ep_guzhuang_55.mp4'),
    (r'D:\资海春\Zhaic\成片\现代\《重返80：从破产川菜馆到国宴主厨》35集（无字幕）.mp4', 'ep_xiandai_35.mp4'),
    (r'D:\资海春\Zhaic\成片\现代\《重返80：从破产川菜馆到国宴主厨》36集（无字幕）.mp4', 'ep_xiandai_36.mp4'),
    (r'D:\资海春\Zhaic\成片\现代\《重返80：从破产川菜馆到国宴主厨》37集（有字幕）.mp4', 'ep_xiandai_37.mp4'),
    (r'D:\资海春\Zhaic\成片\现代\《重返80：从破产川菜馆到国宴主厨》38集（无字幕）.mp4', 'ep_xiandai_38.mp4'),
    (r'D:\资海春\Zhaic\成片\现代\《重返80：从破产川菜馆到国宴主厨》39集（无字幕）.mp4', 'ep_xiandai_39.mp4'),
    (r'D:\资海春\Zhaic\成片\现代\《重返80：从破产川菜馆到国宴主厨》40集（无字幕）.mp4', 'ep_xiandai_40.mp4'),
    (r'D:\资海春\Zhaic\成片\现代\《重返80：从破产川菜馆到国宴主厨》41集（无字幕）.mp4', 'ep_xiandai_41.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\《直言不讳系统》-15集.mp4', 'ep_dou_15.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\《直言不讳系统》-16集.mp4', 'ep_dou_16.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\《直言不讳系统》-17集.mp4', 'ep_dou_17.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\《直言不讳系统》-18集.mp4', 'ep_dou_18.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\《直言不讳系统》-19集.mp4', 'ep_dou_19.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\《直言不讳系统》-20集.mp4', 'ep_dou_20.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\《直言不讳系统》-21集.mp4', 'ep_dou_21.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\直言不讳-32集.mp4', 'ep_dou_32.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\直言不讳-33集.mp4', 'ep_dou_33.mp4'),
    (r'D:\资海春\Zhaic\成片\都市爽文\34.mp4', 'ep_dou_34.mp4'),
    (r'D:\资海春\Zhaic\成片\废土\第八集.mp4', 'ep_feitu_08.mp4'),
    (r'D:\资海春\Zhaic\成片\废土\第九集.mp4', 'ep_feitu_09.mp4'),
    (r'D:\资海春\Zhaic\成片\废土\10（修改）.mp4', 'ep_feitu_10.mp4'),
    (r'D:\资海春\Zhaic\成片\废土\14.mp4', 'ep_feitu_14.mp4'),
    (r'D:\资海春\Zhaic\成片\废土\15.mp4', 'ep_feitu_15.mp4'),
    (r'D:\资海春\Zhaic\成片\废土\23.mp4', 'ep_feitu_23.mp4'),
    (r'D:\资海春\Zhaic\成片\废土\24.mp4', 'ep_feitu_24.mp4'),
    (r'D:\资海春\Zhaic\深度视频\white_model.mp4', 'other_white.mp4'),
]

total = 0
for i, (src, outname) in enumerate(videos):
    outpath = os.path.join(out_dir, outname)
    if not os.path.exists(src):
        print(f'MISS {outname}')
        continue
    # Full duration, 240p width, 15fps
    cap = cv2.VideoCapture(src)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    new_w = 426  # 240p
    new_h = int(h * new_w / w)
    out_fps = 15
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(outpath, fourcc, out_fps, (new_w, new_h))
    fc = 0
    while True:
        ret, frame = cap.read()
        if not ret: break
        frame = cv2.resize(frame, (new_w, new_h))
        writer.write(frame)
        fc += 1
    cap.release()
    writer.release()
    sz = os.path.getsize(outpath) // 1024
    total += sz
    print(f'[{i+1}/{len(videos)}] {outname}: {sz}KB ({fc} frames)')

print(f'\nTotal: {total//1024}MB across {len(videos)} full-length episodes')
