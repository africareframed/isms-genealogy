"""The link previews (owner, 26 Nov 2026): the image a messaging app or social site shows when a page is shared.

python3 scripts/share-images.py   ->  public/images/share/<page>.jpg, 1200 x 630

- home.jpg, for the home page and the general pages: the home page in miniature, the name, the headline and the
  subtitle on the left, the six families as their twelve card strips on the right, and along the bottom a ruler from
  today back to the oldest root on the site, with each movement's oldest root as a square in its family's colour.
- <movement>.jpg and <key word>.jpg: the site's name, the family (or 'Key word') and the page's name on the left,
  the whole card collage on the right, uncut, so its type and its object stay whole (type is never cut).
"""
import os, re, glob
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'public/images/')
OUT = os.path.join(IMG, 'share/')
FONTS = os.path.join(ROOT, 'scripts/collage-fonts/')
W, H = 1200, 630
INK, MUTED = (17, 17, 17), (90, 90, 90)
FAMILIES = [('transhumanism', 'singularitarianism'), ('techno-optimism', 'american-dynamism'), ('ai-safety', 'pause'),
            ('pro-human', 'ai-ethics'), ('digital-sovereignty', 'neo-luddism'), ('normal-technology', 'ai-skepticism')]


COLOURS = {'transcend': (201, 242, 91), 'accelerate': (255, 159, 79), 'prevent': (245, 163, 188),
           'protect': (115, 199, 242), 'reclaim': (195, 166, 255), 'doubt': (46, 230, 200)}
FAMILY_OF = {m: f for f, pair in zip(COLOURS, FAMILIES) for m in pair}
NOW = 2026


def roots():
    """Each movement's oldest documented root, from its own history (src/data/entries)."""
    import yaml
    out = []
    for pair in FAMILIES:
        for m in pair:
            es = yaml.safe_load(open(os.path.join(ROOT, f'src/data/entries/{m}.yaml')))['entries']
            o = min(es, key=lambda e: e['year'])
            out.append((m, o['year'], o.get('yearLabel') or str(o['year'])))
    return out


def home():
    s = 2                                   # drawn at twice the size, then scaled down
    img = Image.new('RGB', (W * s, H * s), 'white'); d = ImageDraw.Draw(img)
    sans = lambda n: ImageFont.truetype(FONTS + 'InterTight-600.ttf', n * s)
    mono = lambda n: ImageFont.truetype(FONTS + 'PlexMono-500.ttf', n * s)
    m = 64 * s
    d.text((m, 52 * s), 'Radical Romance', font=sans(28), fill=INK)
    y = 132 * s
    for line in ['ChatGPT felt like', 'year zero.', 'It wasn’t.']:
        f, x = sans(84), m
        for ch in line:                     # the headline's tight tracking, as on the page
            d.text((x, y), ch, font=f, fill=INK); x += f.getlength(ch) - 0.035 * 84 * s
        y += 80 * s
    d.text((m, 426 * s), 'A GENEALOGY OF THE IDEAS AROUND THE RISE OF AI', font=mono(15), fill=MUTED)
    # the six families as the closed families show them: the top strip of each card
    x0 = 760 * s; colw = (1136 * s - x0 - 12 * s) // 2; rowh, gap = 60 * s, 13 * s; y0 = 52 * s
    for k, pair in enumerate(FAMILIES):
        for j, name in enumerate(pair):
            c = Image.open(IMG + f'collage-{name}.jpg').convert('RGB')
            c = c.resize((colw, round(c.height * colw / c.width)), Image.LANCZOS).crop((0, 0, colw, rowh))
            img.paste(c, (x0 + j * (colw + 12 * s), y0 + k * (rowh + gap)))
    # the ruler: from today back to the oldest root on the site, spaced by years before today on a log scale
    # (most roots fall in the last 450 years, one reaches back to Gilgamesh), with faint marks at 1900, 1500 and 1 CE;
    # each movement's oldest root is a square
    # in its family's colour
    rs = roots(); oldest = min(rs, key=lambda r: r[1])
    import math
    x1, x2, ly = m, 1136 * s, 566 * s
    k0 = 30                                 # the scale starts a little before today, where no root is, so the twelve spread out
    lg = lambda year: math.log10(NOW - year + k0)
    pos = lambda year: x1 + (x2 - x1) * (lg(year) - lg(NOW)) / (lg(oldest[1]) - lg(NOW))
    d.line((x1, ly, x2, ly), fill=INK, width=2 * s // 2 + 1)
    for year, label in ((1900, '1900'), (1500, '1500'), (1, '1 CE')):
        x = pos(year); d.line((x, ly, x, ly + 6 * s), fill=MUTED, width=s)
        f = mono(12); d.text((x - f.getlength(label) / 2, ly + 12 * s), label, font=f, fill=MUTED)
    seen = {}
    for name, year, label in sorted(rs, key=lambda r: -r[1]):
        x = pos(year); stack = seen.get(round(x / (10 * s)), 0); seen[round(x / (10 * s))] = stack + 1
        q = 11 * s; top = ly - q - stack * (q + 3 * s)
        d.rectangle((x - q / 2, top, x + q / 2, top + q), fill=COLOURS[FAMILY_OF[name]])
    f = mono(14)
    d.text((x1, ly + 12 * s), str(NOW), font=f, fill=INK)
    end = oldest[2].upper(); d.text((x2 - f.getlength(end), ly + 12 * s), end, font=f, fill=INK)
    img.resize((W, H), Image.LANCZOS).save(OUT + 'home.jpg', quality=88, optimize=True, progressive=True)


def card(page, title, kicker, colour, image):
    """A movement's or key word's preview: the site's name, the page's family (or 'Key word') and name on the left,
    the whole card collage on the right, uncut, so its type and its object stay whole."""
    s = 2
    img = Image.new('RGB', (W * s, H * s), 'white'); d = ImageDraw.Draw(img)
    sans = lambda n: ImageFont.truetype(FONTS + 'InterTight-600.ttf', round(n * s))
    mono = lambda n: ImageFont.truetype(FONTS + 'PlexMono-500.ttf', n * s)
    m = 64 * s
    c = Image.open(IMG + image).convert('RGB')
    cw = 680 * s; ch = round(c.height * cw / c.width)
    img.paste(c.resize((cw, ch), Image.LANCZOS), (1136 * s - cw, (H * s - ch) // 2))
    col = 1136 * s - cw - 40 * s - m                      # the text column's width
    d.text((m, 52 * s), 'Radical Romance', font=sans(24), fill=INK)
    # the name, as large as 46 px allows: its longest word fits the column, lines break at spaces
    size = 46
    while size > 28 and max(sans(size).getlength(w) for w in title.split()) > col: size -= 1
    f = sans(size); lines, cur = [], ''
    for w in title.split():
        t = (cur + ' ' + w).strip()
        if f.getlength(t) <= col or not cur: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur)
    lh = round(size * 1.08 * s); y = 470 * s - lh * len(lines)
    k = mono(14); q = 16 * s
    d.rectangle((m, y - 44 * s, m + q, y - 44 * s + q), fill=colour)
    d.text((m + q + 12 * s, y - 44 * s - 1 * s), kicker, font=k, fill=INK)
    for line in lines:
        x = m
        for ch_ in line:                                  # the site's tight tracking for large type
            d.text((x, y), ch_, font=f, fill=INK); x += f.getlength(ch_) - 0.02 * size * s
        y += lh
    sm = mono(12)
    d.text((m, 536 * s), 'A GENEALOGY OF THE IDEAS', font=sm, fill=MUTED)
    d.text((m, 556 * s), 'AROUND THE RISE OF AI', font=sm, fill=MUTED)
    img.resize((W, H), Image.LANCZOS).save(OUT + f'{page}.jpg', quality=88, optimize=True, progressive=True)


if __name__ == '__main__':
    import yaml
    os.makedirs(OUT, exist_ok=True)
    home(); made = ['home']
    for kind in ('isms', 'themes'):
        for md in sorted(glob.glob(os.path.join(ROOT, f'src/content/{kind}/*.md'))):
            fm = yaml.safe_load(open(md).read().split('---')[1])
            if not fm.get('ready') or not fm.get('image') or not os.path.exists(IMG + fm['image'] + '.jpg'):
                continue
            page = os.path.splitext(os.path.basename(md))[0]
            if kind == 'isms':
                fam = fm.get('family', '')
                kicker = f"{fam.upper()} · {fm.get('order', 0):02d}"; colour = COLOURS.get(fam, (190, 188, 182))
            else:
                kicker, colour = 'KEY WORD', (190, 188, 182)
            card(page, fm['title'], kicker, colour, fm['image'] + '.jpg'); made.append(page)
    print('made', len(made), 'share images:', ', '.join(made))
