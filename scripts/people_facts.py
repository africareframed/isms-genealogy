"""Copy checked people facts into the site: python3 scripts/people_facts.py <staging folder> [09,10,...]

The researchers write src-less staging files (<nn>.yaml, entries keyed by `person`); a separate checker
sets `status: checked` per person. Only checked entries go into src/data/people-facts/<nn>.yaml, with
`id` = the person's id, so the page never shows an unchecked fact (owner, 23 Nov 2026).
"""
import glob
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGE = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/hist-gaps/people/facts'
# only the batches whose checker has reported (a checker marks people as it goes)
ONLY = set(sys.argv[2].split(',')) if len(sys.argv) > 2 else None
OUT = os.path.join(ROOT, 'src/data/people-facts')
people = {p['id'] for p in yaml.safe_load(open(os.path.join(ROOT, 'src/data/people/people.yaml')))}
os.makedirs(OUT, exist_ok=True)

total = 0
for f in sorted(glob.glob(os.path.join(STAGE, '*.yaml'))):
    if ONLY is not None and os.path.basename(f)[:-5] not in ONLY:
        continue
    entries = yaml.safe_load(open(f)) or []
    checked = []
    for e in entries:
        if e.get('status') != 'checked':
            continue
        pid = e.pop('person')
        if pid not in people:
            print(f'{os.path.basename(f)}: unknown person {pid}, skipped')
            continue
        checked.append({'id': pid, **e})
    name = os.path.basename(f)
    dest = os.path.join(OUT, name)
    if not checked:
        if os.path.exists(dest):
            os.remove(dest)
        continue
    head = f'# People facts, batch {name[:-5]}: checked entries only, copied by scripts/people_facts.py. Do not edit here; fix the staging file and copy again.\n'
    open(dest, 'w').write(head + yaml.safe_dump(checked, allow_unicode=True, sort_keys=False, width=200))
    total += len(checked)
    print(f'{name}: {len(checked)} of {len(entries)} checked')
print('in all', total)
