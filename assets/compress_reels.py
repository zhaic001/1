# -*- coding: utf-8 -*-
import cv2, os
import numpy as np

out_dir = r'D:\资海春\resume-website\assets\deploy_assets\reels'
os.makedirs(out_dir, exist_ok=True)

# Representative samples to compress (smaller set)
samples = [
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【玄幻开场1】.mp4', '3d_01.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【打斗1】.mp4', '3d_07.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【科幻修仙】.mp4', '3d_03.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【古装搞笑女】.mp4', 'real_02.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【现代温情】.mp4', 'real_05.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【玄幻打斗】.mp4', '2d_01.mp4'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【现代悬疑】.mp4', '2d_02.mp4'),
]

for src, outname in samples:
    outpath = os.path.join(out_dir, outname)
    if os.path.exists(outpath):
        print('SKIP:', outname, os.path.getsize(outpath)//1024, 'KB')
        continue
    if not os.path.exists(src):
        print('MISS:', outname)
        continue
    cap = cv2.VideoCapture(src)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # Target: 480p width, max 15 seconds
    new_w = 640
    new_h = int(h * new_w / w)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(outpath, fourcc, fps, (new_w, new_h))
    frame_count = 0
    max_frames = int(fps * 15)  # 15 seconds
    while frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (new_w, new_h))
        writer.write(frame)
        frame_count += 1
    cap.release()
    writer.release()
    sz = os.path.getsize(outpath) // 1024
    print(f'OK: {outname} ({sz}KB, {frame_count} frames)')

print('done')
