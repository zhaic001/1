# -*- coding: utf-8 -*-
import cv2, os, numpy as np

ROOT = r'D:\资海春\resume-website\assets\zhaic'
count = 0
for dirpath, dirs, files in os.walk(ROOT):
    for f in files:
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            path = os.path.join(dirpath, f)
            data = np.fromfile(path, dtype=np.uint8)
            img = cv2.imdecode(data, cv2.IMREAD_COLOR)
            if img is None:
                print(f'FAIL {path}')
                continue
            h, w = img.shape[:2]
            if w > 800:
                img = cv2.resize(img, (800, int(h*800/w)))
            new_path = os.path.splitext(path)[0] + '.jpg'
            ok, buf = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 78])
            buf.tofile(new_path)
            if new_path != path:
                os.remove(path)
            count += 1
            print(f'{os.path.basename(new_path)}: {os.path.getsize(new_path)//1024}KB')

print(f'compressed {count} images')
