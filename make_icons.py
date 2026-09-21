from PIL import Image, ImageDraw

MOSS = "#3F5C46"
PAPER = "#F2ECDB"

def make_icon(size, maskable, path):
    img = Image.new("RGB", (size, size), MOSS)
    draw = ImageDraw.Draw(img)

    scale = 0.50 if maskable else 0.60
    w = size * scale
    h = w * 0.74
    cx = size / 2
    cy = size / 2 + size * 0.02

    x0 = cx - w / 2
    y0 = cy - h / 2
    x1 = cx + w / 2
    y1 = cy + h / 2
    corner = size * 0.045

    tab_w = w * 0.36
    tab_h = h * 0.26
    tab_x0 = x0 + w * 0.08
    tab_x1 = tab_x0 + tab_w
    tab_y0 = y0 - tab_h
    tab_y1 = y0 + corner

    draw.rounded_rectangle([tab_x0, tab_y0, tab_x1, tab_y1], radius=corner * 0.8, fill=PAPER)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=corner, fill=PAPER)

    img.save(path)

make_icon(192, False, "icons/icon-192.png")
make_icon(512, False, "icons/icon-512.png")
make_icon(192, True, "icons/icon-192-maskable.png")
make_icon(512, True, "icons/icon-512-maskable.png")
print("done")
