"""The collage set: 6 isms (family colour) and 7 themes (black and grey).
Deterministic image processing of real archive images and type; no generative model.
Rules: archive fragments are cut along a square grid (shifted, inverted or removed squares);
bold colour fields sit under them slightly out of register; type, when used, stays whole."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy import ndimage

import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'public/images/')
OUT = os.path.join(ROOT, 'public/images/')
M = 100
PAPER = np.array([226, 223, 215], float) / 255
INK = np.array([20, 19, 19], float) / 255
GREEN, PINK, ORANGE, GREY = '#C9F25B', '#F5A3BC', '#D8461C', '#B7B3AA'
SANS = os.path.join(ROOT, 'scripts/collage-fonts/InterTight-600.ttf')
MONO = os.path.join(ROOT, 'scripts/collage-fonts/PlexMono-500.ttf')


def hexrgb(h):
    return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], float) / 255


def gray(name, box, crop=None, channel=None, detail=0):
    im = Image.open(IMG + name).convert('RGB')
    im = im.getchannel(channel) if channel else im.convert('L')   # a colour channel works like a filter in black-and-white photography
    if crop:
        w, h = im.size
        im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
    im = im.resize(box, Image.LANCZOS)
    a = np.asarray(im, float) / 255
    if detail:                                            # local contrast, so fine ribs and grooves survive
        a = a + detail * (a - ndimage.gaussian_filter(a, 4))
    lo, hi = np.percentile(a, 2), np.percentile(a, 98)
    return np.clip((a - lo) / max(hi - lo, 1e-3), 0, 1)


def render(spec):
    W, H = spec['size']
    rng = np.random.default_rng(spec.get('seed', 3))

    def screen(g, level=0.5, grain=0.09, blur=1.1):
        g = ndimage.gaussian_filter(g, blur) + rng.normal(0, grain, g.shape)
        return (g < level).astype(float)

    def halftone(g, period=9, angle=45):
        h, w = g.shape
        y, x = np.mgrid[0:h, 0:w].astype(float)
        t = np.deg2rad(angle)
        u = (x * np.cos(t) + y * np.sin(t)) / period
        v = (-x * np.sin(t) + y * np.cos(t)) / period
        d = np.hypot(u - np.round(u), v - np.round(v))
        dark = ndimage.gaussian_filter(1 - g, period / 3)
        return (d < 0.72 * np.sqrt(np.clip(dark, 0, 1))).astype(float)

    def place(mask, x, y):
        out = np.zeros((H, W)); h, w = mask.shape
        x0, y0 = max(x, 0), max(y, 0); x1, y1 = min(x + w, W), min(y + h, H)
        if x1 > x0 and y1 > y0:
            out[y0:y1, x0:x1] = mask[y0 - y:y1 - y, x0 - x:x1 - x]
        return out

    def rect(c, r, w, h):
        m = np.zeros((H, W)); m[r * M:(r + h) * M, c * M:(c + w) * M] = 1
        return m

    def textmask(txt, font, size, x, y):
        t = Image.new('L', (W, H), 0)
        ImageDraw.Draw(t).text((x, y), txt, font=ImageFont.truetype(font, size), fill=255)
        return np.asarray(t, float) / 255

    canvas = np.ones((H, W, 3)) * PAPER * (1 + rng.normal(0, 0.015, (H, W, 1)))

    def paint(mask, rgb):
        nonlocal canvas
        canvas = canvas * (1 - mask[..., None]) + rgb * mask[..., None]

    col = hexrgb(spec['colour'])
    for c, r, w, h in spec.get('fields', []):            # bold colour fields, misregistered
        m = np.roll(np.roll(rect(c, r, w, h), 6, axis=0), -5, axis=1)
        edge = ndimage.gaussian_filter(m, 2.2) + rng.normal(0, 0.06, m.shape)
        paint((edge > 0.5).astype(float), col)
    for c, r, w, h in spec.get('black', []):
        paint(rect(c, r, w, h), INK)

    ink = np.zeros((H, W))
    for f in spec['fragments']:
        g = gray(f['img'], f['box'], f.get('crop'), f.get('channel'), f.get('detail', 0))
        m = halftone(g, f.get('period', 9)) if f['how'] == 'halftone' else screen(g, f.get('level', 0.5), blur=f.get('blur', 1.1))
        ink = np.clip(ink + place(m, *f['at']), 0, 1)
    base = ink.copy()
    for c, r, w, h, dx, dy in spec.get('shift', []):      # cut-up squares
        m = rect(c, r, w, h)
        ink = ink * (1 - m) + np.roll(np.roll(base, dy * M, axis=0), dx * M, axis=1) * m
    canvas = canvas * (1 - ink[..., None] * 0.95) + canvas * INK * ink[..., None] * 0.95
    for c, r, w, h in spec.get('invert', []):             # negative squares
        m = rect(c, r, w, h)
        paint(m, INK); paint(m * ink, PAPER)
    for c, r, w, h in spec.get('remove', []):             # a missing square
        paint(rect(c, r, w, h), PAPER)
    for t in spec.get('type', []):                        # whole type, on a paper slab
        if t.get('slab'):
            paint(rect(*t['slab']), PAPER * 1.03)
        for txt, size, x, y in t['parts']:
            m = textmask(txt, SANS, size, x, y)
            paint(m, INK)
    for txt, x, y in spec.get('labels', []):           # small labels on their own paper strip
        f = ImageFont.truetype(MONO, 22); l, t, r, b = f.getbbox(txt)
        strip = np.zeros((H, W)); strip[max(y + t - 7, 0):min(y + b + 7, H), max(x - 10, 0):min(x + r + 10, W)] = 1
        paint(strip, PAPER * 1.03)
        paint(textmask(txt, MONO, 22, x, y), INK)

    img = Image.fromarray((np.clip(canvas, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.UnsharpMask(1, 40))
    img.save(OUT + spec['id'] + '.jpg', quality=86, optimize=True, progressive=True)
    return img


ISM, THEME = (1600, 1200), (1500, 1000)
SPECS = [
    dict(id='collage-transhumanism', size=ISM, colour=GREEN,
         fields=[(0, 1, 8, 9), (9, 0, 7, 6)], black=[(8, 0, 1, 2), (0, 10, 1, 2), (15, 7, 1, 1)],
         fragments=[dict(img='gilgamesh-tablet-xi.jpg', box=(900, 1000), crop=(0.05, 0.04, 0.95, 0.96), how='screen', level=0.43, at=(0, 150)),
                    dict(img='tsiolkovsky-free-space.jpg', box=(760, 690), how='halftone', period=9, at=(820, 0))],
         shift=[(4, 4, 2, 2, 1, -1), (2, 7, 2, 1, -1, 0), (13, 0, 1, 3, 0, 1)], invert=[(11, 2, 2, 2)],
         type=[dict(slab=(7, 8, 8, 3), parts=[('2045', 330, 760, 790)])],
         labels=[('C. 1800 BCE · GILGAMESH', 130, 1150), ('1883 · TSIOLKOVSKY', 1230, 700), ('2045 · KURZWEIL', 1230, 742)]),
    dict(id='collage-singularitarianism', size=ISM, colour=GREEN, seed=5,
         fields=[(0, 5, 7, 7), (9, 0, 7, 5)], black=[(7, 0, 1, 1), (15, 10, 1, 2), (0, 0, 1, 2)],
         fragments=[dict(img='moores-law-chart.jpg', box=(1180, 980), crop=(0.16, 0.2, 0.92, 0.86), how='screen', level=0.8, at=(420, 20)),
                    dict(img='sing-ias-computer.jpg', box=(760, 510), crop=(0.0, 0.05, 1.0, 0.95), how='screen', level=0.5, at=(0, 600))],
         shift=[(11, 3, 2, 2, 0, -1), (8, 6, 2, 1, 1, 0), (2, 8, 2, 2, 1, 0)], invert=[(13, 7, 2, 2)],
         labels=[('TRANSISTORS PER CHIP · 1970–2020', 990, 1150), ('THE IAS MACHINE · PRINCETON', 40, 1150)]),
    dict(id='collage-rationalism', size=ISM, colour=PINK, seed=8,
         fields=[(0, 0, 6, 8), (10, 6, 6, 6)], black=[(6, 10, 2, 2), (15, 0, 1, 1), (9, 0, 1, 2)],
         fragments=[dict(img='frankenstein-1831.jpg', box=(840, 1080), crop=(0.0, 0.2, 1.0, 0.98), how='screen', level=0.5, at=(0, 120)),
                    dict(img='sorcerers-apprentice-1882.jpg', box=(760, 840), crop=(0.05, 0.0, 1.0, 0.95), how='halftone', period=8, at=(840, 0))],
         shift=[(2, 3, 2, 2, 1, 0), (11, 2, 2, 2, 0, 1), (5, 8, 1, 2, 0, -1)], invert=[(8, 4, 2, 2)],
         labels=[('1831 · FRANKENSTEIN', 40, 1150), ("C. 1882 · THE SORCERER'S APPRENTICE", 1040, 1150)]),
    dict(id='collage-effective-altruism', size=ISM, colour=PINK, seed=13,
         fields=[(0, 2, 5, 8), (11, 0, 5, 5)], black=[(5, 0, 1, 1), (15, 9, 1, 3)],
         fragments=[dict(img='blue-marble-1972.jpg', box=(1000, 1000), how='halftone', period=10, at=(300, 100))],
         shift=[(8, 2, 2, 2, 1, 0), (4, 7, 2, 1, 0, 1), (10, 8, 1, 2, -1, 0)], remove=[(6, 4, 1, 1)], invert=[(7, 6, 1, 1)],
         labels=[('1972 · APOLLO 17', 40, 1150), ('THE LONG FUTURE', 1300, 1150)]),
    dict(id='collage-effective-accelerationism', size=ISM, colour=ORANGE, seed=21,
         fields=[(0, 6, 9, 6), (12, 0, 4, 4)], black=[(9, 0, 1, 3), (15, 6, 1, 1)],
         fragments=[dict(img='boccioni-city-rises.jpg', box=(1240, 830), how='screen', level=0.52, at=(0, 0))],
         shift=[(3, 2, 2, 2, 1, 0), (6, 4, 2, 2, 0, -1), (10, 1, 2, 2, -1, 0)], invert=[(1, 4, 2, 2)],
         type=[dict(slab=(8, 8, 8, 3), parts=[('e/acc', 300, 830, 800)])],
         labels=[('1910 · BOCCIONI, THE CITY RISES', 40, 1150), ('2022 · EFFECTIVE ACCELERATIONISM', 1160, 760)]),
    dict(id='collage-techno-optimism', size=ISM, colour=ORANGE, seed=34,
         fields=[(0, 0, 7, 7), (11, 8, 5, 4)], black=[(7, 0, 1, 2), (0, 7, 1, 1)],
         fragments=[dict(img='hoover-dam-1934.jpg', box=(1000, 860), how='screen', level=0.5, at=(600, 0))],
         shift=[(9, 3, 2, 2, 0, 1), (12, 1, 2, 1, -1, 0), (7, 5, 1, 2, 1, 0)], invert=[(13, 5, 2, 2)],
         type=[dict(slab=(0, 8, 10, 3), parts=[('BUILD', 300, 40, 790)])],
         labels=[("2020 · IT'S TIME TO BUILD", 40, 1150), ('1934 · HOOVER DAM', 1350, 1150)]),
    # Themes: black and grey only
    dict(id='collage-abundance', size=THEME, colour=GREY, seed=55,
         fields=[(0, 0, 8, 9)], black=[(8, 0, 1, 2), (14, 3, 1, 1)],
         fragments=[dict(img='electricity-meter.jpg', box=(760, 760), crop=(0.04, 0.06, 0.96, 0.86), how='screen', level=0.5, at=(40, 60))],
         shift=[(3, 3, 2, 2, 1, 0), (6, 1, 1, 2, 0, 1)], invert=[(1, 6, 1, 1)],
         type=[dict(slab=(8, 5, 7, 4), parts=[('0', 330, 860, 520), ('kWh', 150, 1080, 690)])],
         labels=[('1954 · "TOO CHEAP TO METER" · LEWIS STRAUSS', 820, 930), ('AN ELECTRICITY METER', 40, 960)]),
    dict(id='collage-power', size=THEME, colour=GREY, seed=89,
         fields=[(1, 1, 8, 7)], black=[(9, 0, 1, 1), (14, 2, 1, 1)],
         fragments=[dict(img='gpu-h100.jpg', box=(840, 563), crop=(0.065, 0.13, 0.775, 0.945), how='screen', level=0.55, detail=3, blur=0.5, at=(30, 110))],
         shift=[(3, 2, 2, 2, 1, 0), (6, 4, 1, 2, 0, 1)], invert=[(1, 5, 1, 1)],
         type=[dict(slab=(9, 5, 6, 4), parts=[('$500', 230, 915, 545), ('billion', 100, 925, 790)])],
         labels=[('UP TO', 925, 530), ('21 JAN 2025 · STARGATE, AT THE WHITE HOUSE', 850, 930), ('2023 · NVIDIA H100 AI CHIPS', 40, 960)]),
    dict(id='collage-the-tool', size=THEME, colour=GREY, seed=144,
         fields=[(0, 0, 6, 6), (10, 6, 5, 4)], black=[(6, 0, 1, 1), (14, 9, 1, 1)],
         fragments=[dict(img='engelbart-1968.jpg', box=(1240, 820), crop=(0.12, 0.34, 0.88, 0.92), how='screen', level=0.42, at=(130, 120))],
         shift=[(8, 3, 2, 2, 1, 0), (4, 6, 2, 1, 0, 1)], invert=[(11, 2, 1, 1)],
         labels=[('1964 · THE FIRST MOUSE', 40, 960)]),
    dict(id='collage-scale', size=THEME, colour=GREY, seed=233,
         fields=[(0, 0, 8, 7)], black=[(8, 0, 1, 2), (14, 4, 1, 1)],
         fragments=[dict(img='perceptron-1958.jpg', box=(900, 730), how='screen', level=0.55, at=(0, 140))],
         shift=[(3, 2, 2, 2, 1, 0), (5, 5, 2, 1, -1, 0)],
         type=[dict(slab=(8, 5, 7, 4), parts=[('10', 300, 850, 560), ('25', 140, 1210, 540)])],
         labels=[('1960 · MARK I PERCEPTRON', 40, 960), ('FLOP · THE EU AI ACT THRESHOLD', 850, 900)]),
    dict(id='collage-rights-and-dignity', size=THEME, colour=GREY, seed=377,
         fields=[(0, 2, 8, 7)], black=[(8, 1, 1, 1), (14, 8, 1, 1)],
         fragments=[dict(img='facial-recognition-camera.jpg', box=(860, 460), crop=(0.23, 0.69, 0.79, 0.90), channel='B', how='screen', level=0.42, at=(0, 300))],
         shift=[(3, 6, 1, 1, -1, 0)], invert=[(6, 3, 1, 1)],
         type=[dict(slab=(9, 4, 6, 3), parts=[('2.2.2025', 130, 920, 455)])],
         labels=[("2 FEB 2025 · THE EU AI ACT'S BANS APPLY", 918, 640), ('POLICE FACIAL-RECOGNITION CAMERA · LONDON · 2026', 40, 960)]),
    dict(id='collage-self-determination', size=THEME, colour=GREY, seed=610,
         fields=[(0, 3, 6, 7), (11, 0, 4, 4)], black=[(6, 8, 1, 2), (14, 6, 1, 1)],
         fragments=[dict(img='kleroterion.jpg', box=(1200, 790), how='screen', level=0.47, at=(150, 100))],
         shift=[(5, 2, 2, 2, 1, 0), (9, 5, 2, 2, 0, 1)], invert=[(3, 1, 2, 2)],
         labels=[('4TH CENTURY BCE · KLEROTERION, ATHENS', 40, 960)]),
    dict(id='collage-critique', size=THEME, colour=GREY, seed=987,
         fields=[(0, 0, 7, 10), (10, 0, 5, 4)], black=[(7, 0, 1, 2), (14, 4, 1, 1)],
         fragments=[dict(img='luddites-1812.jpg', box=(760, 1000), crop=(0.05, 0.04, 0.95, 0.86), how='screen', level=0.55, at=(0, 0)),
                    dict(img='sing-ias-computer.jpg', box=(760, 510), crop=(0.0, 0.05, 1.0, 0.95), how='screen', level=0.5, at=(740, 330))],
         shift=[(2, 3, 2, 2, 1, 0), (4, 6, 2, 2, 0, -1)], invert=[(5, 1, 1, 1)],
         labels=[('1812 · THE LEADER OF THE LUDDITES', 780, 880)]),
]

if __name__ == '__main__':
    import os, sys
    os.makedirs(OUT, exist_ok=True)
    only = sys.argv[1:]
    for s in SPECS:
        if not only or s['id'] in only:
            render(s); print('made', s['id'])
