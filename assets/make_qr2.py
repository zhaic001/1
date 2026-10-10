import qrcode
from PIL import Image, ImageDraw, ImageFont

url = "https://zhaic001.github.io/1/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=12,
    border=2,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#1a1a1a", back_color="white").convert('RGB')

# Add bottom area for URL text
w, h = img.size
new_h = h + 60
canvas = Image.new('RGB', (w, new_h), 'white')
canvas.paste(img, (0, 0))

draw = ImageDraw.Draw(canvas)
try:
    font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 22)
except:
    font = ImageFont.load_default()

bbox = draw.textbbox((0,0), url, font=font)
tw = bbox[2] - bbox[0]
tx = (w - tw) // 2
draw.text((tx, h + 15), url, fill="#333", font=font)

out = r"D:\资海春\gh-pages-repo\assets\qrcode.png"
canvas.save(out, "PNG")
print(f"Saved: {out}")
