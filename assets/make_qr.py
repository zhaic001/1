import qrcode
from PIL import Image, ImageDraw, ImageFont

url = "https://zhaic001.github.io/1/"

# Generate QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=2,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#1a1a1a", back_color="white").convert('RGB')

w, h = img.size
draw = ImageDraw.Draw(img)

# Add center white box with text
box_w = 320
box_h = 100
box_x = (w - box_w) // 2
box_y = (h - box_h) // 2
draw.rectangle([box_x, box_y, box_x+box_w, box_y+box_h], fill="white", outline="#b8860b", width=4)

# Add text
try:
    font = ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", 36)
except:
    font = ImageFont.load_default()

text = "资海春个人简历"
bbox = draw.textbbox((0,0), text, font=font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
tx = (w - tw) // 2
ty = (h - th) // 2 - bbox[1]
draw.text((tx, ty), text, fill="#b8860b", font=font)

out = r"D:\资海春\gh-pages-repo\assets\qrcode.png"
img.save(out, "PNG")
print(f"Saved: {out} ({img.size[0]}x{img.size[1]})")
