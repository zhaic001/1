# -*- coding: utf-8 -*-
import cv2, os
import numpy as np

video = r'D:\资海春\Zhaic\婚庆拍摄\婚礼.mp4'
out_cover = r'D:\资海春\resume-website\assets\deploy_assets\wedding_cover.jpg'

# Extract cover
cap = cv2.VideoCapture(video)
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cap.set(cv2.CAP_PROP_POS_FRAMES, min(total // 3, 200))
ret, frame = cap.read()
cap.release()
if ret:
    h, w = frame.shape[:2]
    scale = 900 / w
    frame = cv2.resize(frame, (900, int(h * scale)))
    ok, buf = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
    if ok:
        buf.tofile(out_cover)
        print('cover saved:', os.path.getsize(out_cover)//1024, 'KB')
    else:
        print('encode failed')
else:
    print('read failed')

# Copy video to deploy assets
import shutil
dst = r'D:\资海春\resume-website\assets\deploy_assets\wedding.mp4'
shutil.copy2(video, dst)
print('video copied:', os.path.getsize(dst)//1024, 'KB')
