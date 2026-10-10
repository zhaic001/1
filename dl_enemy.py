import urllib.request, os

out_dir = r'C:\Users\Administrator\resume-restore\assets\enemy\images'
os.makedirs(out_dir, exist_ok=True)

imgs = [
    "enemy-001-7c054c99d035.webp","enemy-002-59770486e1df.webp",
    "enemy-003-380bc6a3e19d.webp","enemy-004-302db049cd33.webp",
    "enemy-005-6096d7264b15.webp","enemy-006-3938491a7763.webp",
    "enemy-007-a6e9afde3de.webp","enemy-008-bbfa18ab133e.webp",
    "enemy-009-5adfdde6dcef.webp","enemy-010-2e88df8a6471.webp",
    "enemy-011-77b7add2fb5e.webp","enemy-012-5f893783e8c6.webp",
    "enemy-013-807630241127.webp","enemy-014-c970ed94e40c.webp",
    "enemy-015-6e575c66c1ac.webp","enemy-016-65f769cb2f4b.webp",
    "enemy-017-34cab1bdcb2f.webp","enemy-018-8b6ec4fc9bcc.webp",
    "enemy-019-2f1e27aaf3d2.webp","enemy-020-9171f3d984d4.webp",
    "enemy-021-11fa892bb340.webp","enemy-022-956a2df51c48.webp",
    "enemy-023-1d9c911862f6.webp","enemy-024-d1796a28db3e.webp",
]

base = "https://zhc2004411.github.io/New-zihai-chun-resume/assets/enemy/images/"
ok = 0
for img in imgs:
    out = os.path.join(out_dir, img)
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        ok += 1
        continue
    try:
        urllib.request.urlretrieve(base + img, out)
        ok += 1
    except Exception as e:
        print(f"FAIL {img}: {e}")

print(f"Downloaded: {ok}/24")
