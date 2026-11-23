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
out.insert(2, f'**{n} points ouverts.**'); out.insert(3, '')
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
