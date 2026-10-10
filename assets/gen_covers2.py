# -*- coding: utf-8 -*-
import cv2, os

out_dir = r'D:\资海春\resume-website\assets\reel-covers'

videos = [
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【古装搞笑】.mp4', 'real_01.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【古装搞笑女】.mp4', 'real_02.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【古装玄幻】.mp4', 'real_03.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【现代悬疑】.mp4', 'real_04.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【现代温情】.mp4', 'real_05.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【现代系统】.mp4', 'real_06.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【古欧玄幻言情】.mp4', 'real_07.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【古西欧言情】.mp4', 'real_08.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【现代玄幻言情】.mp4', 'real_09.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【现代言情】.mp4', 'real_10.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【玄幻打斗】.mp4', '2d_01.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【现代悬疑】.mp4', '2d_02.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【现代类打斗】.mp4', '2d_03.jpg'),
]

for vpath, outname in videos:
    outpath = os.path.join(out_dir, outname)
    if os.path.exists(outpath):
        print(f'SKIP: {outname}')
        continue
    if not os.path.exists(vpath):
        print(f'MISS: {outname}')
        continue
    cap = cv2.VideoCapture(vpath)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.set(cv2.CAP_PROP_POS_FRAMES, min(total // 4, 120))
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 30)
        ret, frame = cap.read()
    cap.release()
    if ret:
        h, w = frame.shape[:2]
        scale = 800 / w
        frame = cv2.resize(frame, (800, int(h*scale)))
        ok, buf = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 75])
        if ok:
            buf.tofile(outpath)
            print(f'OK: {outname}')
    else:
        print(f'FAIL: {outname}')
print('done')
