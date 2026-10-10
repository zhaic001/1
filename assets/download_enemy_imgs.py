import re, os, urllib.request

html_path = r'D:\资海春\gh-pages-repo\assets\enemy\enemy-system.html'
img_dir = r'D:\资海春\gh-pages-repo\assets\enemy\images'
os.makedirs(img_dir, exist_ok=True)

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all image references
imgs = re.findall(r'src="(images/[^"]+)"', html)
imgs = list(set(imgs))
print(f"Found {len(imgs)} images")

base = "https://zhc2004411.github.io/New-zihai-chun-resume/assets/enemy/"
for img in imgs:
    fname = img.split('/')[-1]
    out = os.path.join(img_dir, fname)
    if os.path.exists(out): continue
    url = base + img
    try:
        urllib.request.urlretrieve(url, out)
        print(f"  OK {fname} ({os.path.getsize(out)//1024}KB)")
    except Exception as e:
        print(f"  FAIL {fname}: {e}")

print("Done!")
