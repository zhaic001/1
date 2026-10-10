# -*- coding: utf-8 -*-
import cv2, os, numpy as np

out_dir = r'D:\资海春\resume-website\assets\reel-covers'
os.makedirs(out_dir, exist_ok=True)

# Map: (video_path, output_name)
videos = [
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【玄幻开场1】.mp4', '3d_01.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【玄幻开场2】.mp4', '3d_02.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【科幻修仙】.mp4', '3d_03.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【科幻废土风格】.mp4', '3d_04.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【系统穿越】.mp4', '3d_05.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【叙事】.mp4', '3d_06.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【打斗1】.mp4', '3d_07.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【打斗2】.mp4', '3d_08.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【追逐1】.mp4', '3d_09.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【追逐2】.mp4', '3d_10.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【追逐3】.mp4', '3d_11.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【恐怖】.mp4', '3d_12.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】\3D【海外女频同性】.mp4', '3d_13.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【水印】\伪真人【古装搞笑】.mp4', 'real_01.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【水印】\伪真人【古装搞笑女】.mp4', 'real_02.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【水印】\伪真人【古装玄幻】.mp4', 'real_03.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【水印】\伪真人【现代悬疑】.mp4', 'real_04.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【水印】\伪真人【现代温情】.mp4', 'real_05.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\伪真人【水印】\伪真人【现代系统】.mp4', 'real_06.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【水印】\海外伪真人【古欧玄幻言情】.mp4', 'real_07.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【水印】\海外伪真人【古西欧言情】.mp4', 'real_08.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【水印】\海外伪真人【现代玄幻言情】.mp4', 'real_09.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人\海外伪真人【水印】\海外伪真人【现代言情】.mp4', 'real_10.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【水印】\二维漫【玄幻打斗】.mp4', '2d_01.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【水印】\二维漫【现代悬疑】.mp4', '2d_02.jpg'),
    (r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫\二维漫【水印】\二维漫【现代类打斗】.mp4', '2d_03.jpg'),
]

for vpath, outname in videos:
    if not os.path.exists(vpath):
        print(f'MISS: {vpath}')
        continue
    outpath = os.path.join(out_dir, outname)
    if os.path.exists(outpath):
        print(f'SKIP: {outname}')
        continue
    # Use np.fromfile for Chinese path support
    try:
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
            # Encode as JPG and write with Chinese path support
            ok, buf = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 75])
            if ok:
                buf.tofile(outpath)
                print(f'OK: {outname}')
            else:
                print(f'ENCODE FAIL: {outname}')
        else:
            print(f'READ FAIL: {outname}')
    except Exception as e:
        print(f'ERROR {outname}: {e}')

print('done')
