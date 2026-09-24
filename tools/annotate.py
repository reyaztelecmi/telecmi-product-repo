"""Draw numbered markers on a screenshot.

Usage:
    python tools/annotate.py docs/connle/home/img/apps-home.markers.json

The JSON file lists the clean screenshot and marker positions in percent:
    {"image": "apps-home.png", "markers": [{"n": 1, "x": 4.8, "y": 19.3}]}

Writes <image>-annotated.png next to the clean screenshot.
Requires: pip install pillow
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ORANGE = (224, 81, 43)

def font(size):
    for name in ("DejaVuSans-Bold.ttf", "arialbd.ttf", "Arial Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()

def main(spec_path):
    spec_path = Path(spec_path)
    spec = json.loads(spec_path.read_text())
    src = spec_path.parent / spec["image"]
    im = Image.open(src).convert("RGB")
    d = ImageDraw.Draw(im)
    r = max(13, round(im.width / 95))
    f = font(round(r * 1.05))
    for m in spec["markers"]:
        x, y = m["x"] / 100 * im.width, m["y"] / 100 * im.height
        d.ellipse([x - r - 2, y - r - 2, x + r + 2, y + r + 2], fill="white")
        d.ellipse([x - r, y - r, x + r, y + r], fill=ORANGE)
        d.text((x, y), str(m["n"]), fill="white", font=f, anchor="mm")
    out = src.with_name(src.stem + "-annotated.png")
    im.save(out, optimize=True)
    print(f"Wrote {out}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
