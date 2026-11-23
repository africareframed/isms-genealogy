"""Build src/data/people/people.yaml (python3 scripts/people.py <portraits.csv>): who is on the People page, with portrait and credit.

Sources: the owner's portraits.csv (213 cleared portraits) and the movements' notable figures.
Identity only; researched facts live in src/data/people-facts/ and are checked separately.
"""
import csv, glob, re, unicodedata, urllib.parse
import yaml

import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# the owner's portraits.csv, staged from his folder isms-genealogy-images/portraits/
CSV = sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/uploads/isms-genealogy-images/portraits/portraits.csv'
WEB = set(f[:-4] for f in __import__('os').listdir(f'{ROOT}/public/portraits'))

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def clean_name(n):
    return re.sub(r'\s*\(.*?\)\s*', ' ', n).strip()

def clean_author(a):
    a = (a or '').strip().strip('"').strip()
    if not a or re.search(r'unknown|not given|anonymous|^see title', a, re.I):
        return ''
    a = re.sub(r'\s*\[\s*\d+\s*\]', '', a)
    a = re.sub(r'^The original uploader was (\S+).*', r'\1', a)
    a = re.sub(r'\s+', ' ', a)
    return a[:70]

# Name variants used in the history and the vocabulary, so a person's moments are found.
ALIASES = {
    'herbert-a-simon': ['Herbert Simon', 'Herbert A. Simon'],
    'fei-fei-li': ['Li Fei-Fei'],
    'chris-olah': ['Christopher Olah'],
    'jeff-dean': ['Jeffrey Dean'],
    'james-lighthill': ['Sir James Lighthill', 'Lighthill'],
    'nicolas-de-condorcet': ['Condorcet', 'Marquis de Condorcet'],
    'giovanni-pico-della-mirandola': ['Pico della Mirandola'],
    'gottfried-wilhelm-leibniz': ['Leibniz', 'Gottfried Leibniz'],
    'wolfgang-von-kempelen': ['Kempelen'],
    'stanislaw-ulam': ['Stanislaw Ulam', 'Stan Ulam'],
    'john-von-neumann': ['von Neumann'],
    'yann-lecun': ['Yann Le Cun'],
    'jurgen-schmidhuber': ['Jurgen Schmidhuber'],
    'rene-descartes': ['Descartes'],
    'pope-leo-xiv': ['Leo XIV'],
    'william-macaskill': ['Will MacAskill'],
    'emile-p-torres': ['Émile Torres'],
    'emily-m-bender': ['Emily Bender'],
    'leonardo-torres-quevedo': ['Torres Quevedo'],
    'i-j-good': ['Irving John Good', 'Jack Good'],
    'j-c-r-licklider': ['Licklider'],
    'ronald-j-williams': ['Ronald Williams'],
    'tomas-mikolov': ['Tomáš Mikolov'],
    'donald-trump': ['President Trump', 'Trump'],
    'joe-biden': ['President Biden', 'Biden'],
    'xi-jinping': ['Xi'],
    'vladimir-putin': ['Putin'],
    'karel-capek': ['Karel Capek'],
    'josef-capek': ['Josef Capek'],
    'filippo-tommaso-marinetti': ['Marinetti'],
    'david-pearce': ['David Pearce'],
    'kevin-kelly': ['Kevin Kelly'],
    'margaret-mitchell': ['Margaret Mitchell'],
    'samuel-butler': ['Samuel Butler'],
    'nikolai-fedorov': ['Nikolai Fyodorov', 'Fedorov'],
}

people, seen = [], {}
for r in csv.DictReader(open(CSV, encoding='utf-8')):
    stem = r['filename'].rsplit('.', 1)[0]
    name = clean_name(r['name'])
    url = r['commons_file_page_url'].strip()
    host = urllib.parse.urlparse(url).netloc.replace('www.', '') if url.startswith('http') else ''
    lic = r['licence'].strip()
    commons = 'commons.wikimedia.org' in host or 'wikipedia.org' in host
    if lic in ('External web source (check rights)', 'Fair use', ''):
        licence = host or 'source unknown'
    elif commons:
        licence = f'{lic}, Wikimedia Commons'
    else:
        licence = f'{lic}, {host}' if host else lic
    p = {'id': stem, 'name': name}
    if stem in ALIASES:
        p['aliases'] = [a for a in ALIASES[stem] if a != name]
    if stem in WEB:
        p['portrait'] = {'file': f'{stem}.jpg', 'credit': clean_author(r['author_or_artist']), 'licence': licence, 'sourceUrl': url}
        if not p['portrait']['credit']:
            del p['portrait']['credit']
        if stem == 'thomas-bayes':
            p['portrait']['caveat'] = 'The only portrait in circulation; historians doubt it shows Bayes.'
    people.append(p)
    seen[slug(name)] = p

# Notable figures with no portrait in the folder still get a tile.
for f in sorted(glob.glob(f'{ROOT}/src/data/figures/*.yaml')):
    for x in yaml.safe_load(open(f)) or []:
        n = clean_name(x['name'])
        known = {slug(a) for q in people for a in q.get('aliases', [])}
        if slug(n) not in seen and slug(n) not in known:
            p = {'id': slug(n), 'name': n}
            people.append(p); seen[slug(n)] = p

# Not (or no longer) named on the site for what they did: no tile until they are (23 Nov 2026).
DROP = {'anthony-albanese', 'terence-tao'}
people = [p for p in people if p['id'] not in DROP]
people.sort(key=lambda p: p['id'])
head = ('# The People page (owner, 23 Nov 2026): who is on it, with portrait and credit. Identity only:\n'
        '# researched facts (roles, labs, connections and so on) live in src/data/people-facts/ and are checked separately.\n'
        '# Portraits are the owner\'s, all cleared (23 Nov 2026); `licence` is the visible credit, naming the source.\n'
        '# A person without `portrait` is shown with their name on a plain field (wrong photo or none yet).\n')
out = yaml.safe_dump(people, allow_unicode=True, sort_keys=False, width=200)
import os
os.makedirs(f'{ROOT}/src/data/people', exist_ok=True)
open(f'{ROOT}/src/data/people/people.yaml', 'w').write(head + out)
print(len(people), 'people;', sum(1 for p in people if 'portrait' in p), 'with portrait')
print('no portrait:', [p['name'] for p in people if 'portrait' not in p])
