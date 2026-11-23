#!/usr/bin/env python3
"""Génère registry/POINTS_A_VERIFIER.md (depuis les open_points de lessons.json) et registry/EMPREINTES.sha256 (content, tools, registry hors fichiers générés). Usage: python3 -I tools/consolidate.py"""
import json, os, hashlib
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(f'{root}/registry/lessons.json', encoding='utf-8'))
out = ['# Registre des points à vérifier', '', 'Généré depuis `registry/lessons.json` (champ `open_points`). Les contrôles automatiques sont des contrôles techniques, pas une validation scientifique définitive.', '']
n = 0
for e in d['lessons']:
    pts = e.get('open_points') or []
    if not pts: continue
    out.append(f'## {e["id"]} — {e["title"]}')
    for p in pts: out.append(f'- [ ] {p}'); n += 1
    out.append('')
import collections
sev = collections.Counter(); crit = []
for e in d['lessons']:
    for p in e.get('open_points') or []:
        k = next((s for s in ('critique', 'importante', 'mineure') if p.startswith(f'[{s}]')), 'non classé')
        sev[k] += 1
        if k == 'critique': crit.append(f'- {e["id"]} : {p}')
head = [f'**{n} points ouverts.**', '', '**Gravité** (classement obligatoire à partir du module 4 ; les points des modules 0 à 3 sont **non classés** et à classer lors de l\'audit) : ' + ' ; '.join(f'{k} : {sev[k]}' for k in ('critique', 'importante', 'mineure', 'non classé')) + '.', '']
if crit: head += ['**Points critiques (à résoudre avant la validation scientifique des leçons concernées) :**'] + crit + ['']
out[2:2] = head
open(f'{root}/registry/POINTS_A_VERIFIER.md', 'w', encoding='utf-8').write('\n'.join(out))
lines = []
for base in ['content', 'tools', 'registry']:
    for dp, dn, fn in os.walk(f'{root}/{base}'):
        dn[:] = [x for x in dn if x != '__pycache__']
        for f in sorted(fn):
            if f in ('EMPREINTES.sha256', 'POINTS_A_VERIFIER.md'): continue
            p = os.path.join(dp, f); lines.append(hashlib.sha256(open(p, 'rb').read()).hexdigest() + '  ' + os.path.relpath(p, root))
open(f'{root}/registry/EMPREINTES.sha256', 'w').write('\n'.join(sorted(lines, key=lambda x: x.split('  ')[1])) + '\n')
print(n, 'points ;', len(lines), 'empreintes')
