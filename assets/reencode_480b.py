import subprocess, os

out_dir = r'D:\资海春\resume-website\assets\deploy_assets\reels'
ffmpeg = r'C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe'

jobs = []

# 3D samples (12 already done 3d_01-3d_11, redo 12,13)
d3 = r'D:\资海春\Zhaic\DEOM\视频作品集\3D漫\3D漫【水印】'
d3_map = [
    ('3D【恐怖】.mp4', '3d_12.mp4'),
    ('3D【海外女频同性】.mp4', '3d_13.mp4'),
]
for src, out in d3_map:
    jobs.append((os.path.join(d3, src), os.path.join(out_dir, out)))

# 2D
d2 = r'D:\资海春\Zhaic\DEOM\视频作品集\二维漫'
for src, out in [('二维漫【玄幻打斗】.mp4','2d_01.mp4'),('二维漫【现代悬疑】.mp4','2d_02.mp4'),('二维漫【现代类打斗】.mp4','2d_03.mp4')]:
    jobs.append((os.path.join(d2, src), os.path.join(out_dir, out)))

# Real
dr = r'D:\资海春\Zhaic\DEOM\视频作品集\伪真人'
real_files = sorted([f for f in os.listdir(dr) if f.endswith('.mp4') and '清北梦' not in f])
real_names = ['real_01.mp4','real_02.mp4','real_03.mp4','real_04.mp4','real_05.mp4','real_06.mp4','real_07.mp4','real_08.mp4','real_09.mp4','real_10.mp4']
for i, rf in enumerate(real_files[:10]):
    jobs.append((os.path.join(dr, rf), os.path.join(out_dir, real_names[i])))

# Wedding
jobs.append((r'D:\资海春\Zhaic\婚庆拍摄\婚礼.mp4', os.path.join(out_dir, 'other_white.mp4')))

# 古装
dzg = r'D:\资海春\Zhaic\成片\古装'
for i, f in enumerate(sorted([f for f in os.listdir(dzg) if f.endswith('.mp4')])):
    jobs.append((os.path.join(dzg, f), os.path.join(out_dir, f'ep_guzhuang_{41+i}.mp4')))

# 现代
dxd = r'D:\资海春\Zhaic\成片\现代'
xd_map = {
    '《重返80：从破产川菜馆到国宴主厨》35集（无字幕）.mp4': 'ep_xiandai_35.mp4',
    '《重返80：从破产川菜馆到国宴主厨》36集（无字幕）.mp4': 'ep_xiandai_36.mp4',
    '《重返80：从破产川菜馆到国宴主厨》37集（有字幕）.mp4': 'ep_xiandai_37.mp4',
    '《重返80：从破产川菜馆到国宴主厨》38集（无字幕）.mp4': 'ep_xiandai_38.mp4',
    '《重返80：从破产川菜馆到国宴主厨》39集（无字幕）.mp4': 'ep_xiandai_39.mp4',
    '《重返80：从破产川菜馆到国宴主厨》40集（无字幕）.mp4': 'ep_xiandai_40.mp4',
    '《重返80：从破产川菜馆到国宴主厨》41集（无字幕）.mp4': 'ep_xiandai_41.mp4',
}
for src, out in xd_map.items():
    p = os.path.join(dxd, src)
    if os.path.exists(p): jobs.append((p, os.path.join(out_dir, out)))

# 都市爽文
dd = r'D:\资海春\Zhaic\成片\都市爽文'
for src, out in [
    ('《直言不讳系统》-15集.mp4','ep_dou_15.mp4'),('《直言不讳系统》-16集.mp4','ep_dou_16.mp4'),
    ('《直言不讳系统》-17集.mp4','ep_dou_17.mp4'),('《直言不讳系统》-18集.mp4','ep_dou_18.mp4'),
    ('《直言不讳系统》-19集.mp4','ep_dou_19.mp4'),('《直言不讳系统》-20集.mp4','ep_dou_20.mp4'),
    ('《直言不讳系统》-21集.mp4','ep_dou_21.mp4'),('直言不讳-32集.mp4','ep_dou_32.mp4'),
    ('直言不讳-33集.mp4','ep_dou_33.mp4'),('直言不讳-34集.mp4','ep_dou_34.mp4')]:
    p = os.path.join(dd, src)
    if os.path.exists(p): jobs.append((p, os.path.join(out_dir, out)))

# 废土
df = r'D:\资海春\Zhaic\成片\废土'
for src, out in [
    ('第八集.mp4','ep_feitu_08.mp4'),('第九集.mp4','ep_feitu_09.mp4'),
    ('10（修改）.mp4','ep_feitu_10.mp4'),('14.mp4','ep_feitu_14.mp4'),
    ('15.mp4','ep_feitu_15.mp4'),('23.mp4','ep_feitu_23.mp4'),('24.mp4','ep_feitu_24.mp4')]:
    p = os.path.join(df, src)
    if os.path.exists(p): jobs.append((p, os.path.join(out_dir, out)))

print(f'Remaining: {len(jobs)}')
for i, (src, out) in enumerate(jobs):
    if not os.path.exists(src):
        print(f'[{i+1}] MISSING: {src}'); continue
    # Skip if already > 1MB (already converted at 480p)
    if os.path.exists(out) and os.path.getsize(out) > 1024*1024:
        print(f'[{i+1}/{len(jobs)}] SKIP {os.path.basename(out)} ({os.path.getsize(out)//1024}KB)')
        continue
    tmp = out + '.tmp.mp4'
    cmd = [ffmpeg, '-y', '-i', src, '-vf', 'scale=-2:480',
           '-c:v', 'libx264', '-preset', 'fast', '-crf', '28',
           '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', tmp]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 1000:
        os.replace(tmp, out)
        print(f'[{i+1}/{len(jobs)}] OK {os.path.basename(out)} ({os.path.getsize(out)//1024}KB)')
    else:
        print(f'[{i+1}/{len(jobs)}] FAIL {os.path.basename(out)}: {r.stderr[-200:]}')
        if os.path.exists(tmp): os.remove(tmp)
print('Done!')
