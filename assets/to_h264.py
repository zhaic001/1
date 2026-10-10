import subprocess, os, glob, time

reel_dir = r'D:\资海春\resume-website\assets\deploy_assets\reels'
ffmpeg = r'C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe'
if not os.path.exists(ffmpeg):
    # try other paths
    for p in [r'C:\Program Files\ffmpeg\bin\ffmpeg.exe', 'ffmpeg']:
        if os.path.exists(p) or p == 'ffmpeg':
            ffmpeg = p
            break

videos = glob.glob(os.path.join(reel_dir, '*.mp4'))
print(f'Converting {len(videos)} videos to H.264...')

for i, v in enumerate(videos):
    tmp = v + '.tmp.mp4'
    # Check if already H.264
    probe = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', 
                           '-show_entries', 'stream=codec_name', '-of', 'csv=p=0', v],
                          capture_output=True, text=True)
    codec = probe.stdout.strip()
    if codec == 'h264':
        print(f'[{i+1}/{len(videos)}] SKIP {os.path.basename(v)} (already h264)')
        continue
    
    cmd = [ffmpeg, '-y', '-i', v, '-c:v', 'libx264', '-preset', 'fast', 
           '-crf', '28', '-an', '-movflags', '+faststart', tmp]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 1000:
        os.replace(tmp, v)
        sz = os.path.getsize(v)//1024
        print(f'[{i+1}/{len(videos)}] OK {os.path.basename(v)} ({sz}KB)')
    else:
        print(f'[{i+1}/{len(videos)}] FAIL {os.path.basename(v)}: {r.stderr[-200:]}')
        if os.path.exists(tmp): os.remove(tmp)

print('Done!')
