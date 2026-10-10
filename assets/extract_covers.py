# -*- coding: utf-8 -*-
import cv2, os, io, json

ROOT = r'D:\资海春\Zhaic\DEOM\视频作品集'
OUT = r'D:\资海春\resume-website\assets\reel-covers'
os.makedirs(OUT, exist_ok=True)

# (subdir, output_prefix, list of filenames)
groups = [
    ('3D漫/3D漫【水印】', '3d', [
        '3D【玄幻开场1】.mp4','3D【玄幻开场2】.mp4','3D【科幻修仙】.mp4',
        '3D【科幻废土风格】.mp4','3D【系统穿越】.mp4','3D【叙事】.mp4',
        '3D【打斗1】.mp4','3D【打斗2】.mp4','3D【追逐1】.mp4',
        '3D【追逐2】.mp4','3D【追逐3】.mp4','3D【恐怖】.mp4','3D【海外女频同性】.mp4'
    ]),
    ('伪真人', 'real', [
        '阿嫲的清北梦-第20集.mp4','伪真人【现代悬疑】.mp4','伪真人【现代温情】.mp4',
        '伪真人【现代系统】.mp4','伪真人【古装玄幻】.mp4','伪真人【古装搞笑】.mp4',
        '伪真人【古装搞笑女】.mp4','海外伪真人【现代言情】.mp4',
        '海外伪真人【现代玄幻言情】.mp4','海外伪真人【古西欧言情】.mp4',
        '海外伪真人【古欧玄幻言情】.mp4'
    ]),
    ('二维漫', '2d', [
        '二维漫【玄幻打斗】.mp4','二维漫【现代悬疑】.mp4','二维漫【现代类打斗】.mp4'
    ]),
]

results = {}
for sub, prefix, files in groups:
    results[prefix] = []
    for i, fn in enumerate(files, 1):
        path = os.path.join(ROOT, sub, fn)
        out_name = f'{prefix}_{i:02d}.jpg'
        out_path = os.path.join(OUT, out_name)
        cap = cv2.VideoCapture(path)
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS) or 25
        # 抽 20% 位置的帧（开头有黑场，中间偏前比较有代表性）
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(total * 0.15))
        ok, frame = cap.read()
        if not ok:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ok, frame = cap.read()
        if ok:
            # 缩放到宽 480
            h, w = frame.shape[:2]
            new_w = 480
            new_h = int(h * new_w / w)
            frame = cv2.resize(frame, (new_w, new_h))
            cv2.imwrite(out_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            results[prefix].append(out_name)
            print(f'OK {out_name} <- {fn}')
        else:
            print(f'FAIL {fn}')
        cap.release()

# 保存映射给后续 patch 用
io.open(r'D:\资海春\resume-website\assets\covers_map.json', 'w', encoding='utf-8').write(
    json.dumps(results, ensure_ascii=False, indent=2))
print('done, total:', sum(len(v) for v in results.values()))
