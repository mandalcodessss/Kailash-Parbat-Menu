# Usage: python make_stand.py "Kailash Parbat" MENU_URL REVIEW_URL INSTAGRAM_URL [logo.png]
import sys, qrcode
from PIL import Image, ImageDraw, ImageFont

name, menu, review, insta = sys.argv[1:5]
logo = sys.argv[5] if len(sys.argv) > 5 else None

def font(size, bold=False):
    try: return ImageFont.truetype("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", size)
    except OSError: return ImageFont.load_default(size=size)

W, H = 1600, 1000
img = Image.new("RGB", (W, H), "#fbf6ec"); d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 150], fill="#5b2a6e"); d.rectangle([0, 150, W, 162], fill="#c9962b")
d.text((W / 2, 75), name, font=font(64, True), fill="white", anchor="mm")
if logo:
    lg = Image.open(logo).convert("RGBA"); lg.thumbnail((110, 110)); img.paste(lg, (30, 20), lg)
for i, (label, url) in enumerate([("Scan for Menu", menu), ("Rate us on Google", review), ("Follow us on Instagram", insta)]):
    x = 85 + i * 505
    img.paste(qrcode.make(url, box_size=10, border=1).convert("RGB").resize((420, 420)), (x, 260))
    d.text((x + 210, 740), label, font=font(34, True), fill="#5b2a6e", anchor="mm")
d.text((W / 2, 900), "Thank you for visiting!", font=font(30), fill="#7a6f7c", anchor="mm")
out = name.replace(" ", "_") + "_stand.png"; img.save(out); print("Saved", out)
