# -*- coding: utf-8 -*-
import cv2, os

out_dir = r'D:\资海春\resume-website\assets\deploy_assets\reels'
os.makedirs(out_dir, exist_ok=True)

# All 26 reel videos
videos = [
    # 3D漫 (13)
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【玄幻开场1】.mp4', '3d_01.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【玄幻开场2】.mp4', '3d_02.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【科幻修仙】.mp4', '3d_03.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【科幻废土风格】.mp4', '3d_04.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【系统穿越】.mp4', '3d_05.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【叙事】.mp4', '3d_06.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【打斗1】.mp4', '3d_07.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【打斗2】.mp4', '3d_08.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【追逐1】.mp4', '3d_09.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【追逐2】.mp4', '3d_10.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【追逐3】.mp4', '3d_11.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【恐怖】.mp4', '3d_12.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【海外女频同性】.mp4', '3d_13.mp4'),
    # 伪真人 (10)
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\阿嫲的清北梦-第20集.mp4', 'real_01.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【古装搞笑女】.mp4', 'real_02.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【现代温情】.mp4', 'real_03.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【现代系统】.mp4', 'real_04.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【古装玄幻】.mp4', 'real_05.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【古装搞笑】.mp4', 'real_06.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【现代言情】.mp4', 'real_07.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【现代玄幻言情】.mp4', 'real_08.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【古西欧言情】.mp4', 'real_09.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【古欧玄幻言情】.mp4', 'real_10.mp4'),
    # 二维漫 (3)
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【玄幻打斗】.mp4', '2d_01.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【现代悬疑】.mp4', '2d_02.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【现代类打斗】.mp4', '2d_03.mp4'),
]

total_size = 0
for src, outname in videos:
    outpath = os.path.join(out_dir, outname)
    if os.path.exists(outpath) and os.path.getsize(outpath) > 100000:
        sz = os.path.getsize(outpath) // 1024
        total_size += sz
        print(f'SKIP: {outname} ({sz}KB)')
        continue
    if not os.path.exists(src):
        print(f'MISS: {outname}')
        continue
    cap = cv2.VideoCapture(src)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    new_w = 480
    new_h = int(h * new_w / w)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(outpath, fourcc, fps, (new_w, new_h))
    max_frames = int(fps * 10)  # 10 seconds
    fc = 0
    while fc < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (new_w, new_h))
        writer.write(frame)
        fc += 1
    cap.release()
    writer.release()
    sz = os.path.getsize(outpath) // 1024
    total_size += sz
    print(f'OK: {outname} ({sz}KB, {fc} frames)')

print(f'\nTotal: {total_size//1024}MB across {len(videos)} videos')
