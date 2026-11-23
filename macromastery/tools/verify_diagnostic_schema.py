#!/usr/bin/env python3
"""Valide toutes les banques de diagnostic (content/diagnostic/banque_m*.json) contre le schéma commun
content/diagnostic/SCHEMA_BANQUE.json (version 2, décision 8 du 23/11/2026). Lecture seule, sans dépendance externe.
Usage : python3 -I tools/verify_diagnostic_schema.py
"""
import glob, json, os, re, sys
from collections import Counter

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = json.load(open(f'{root}/content/diagnostic/SCHEMA_BANQUE.json', encoding='utf-8'))
fails = total = 0
def chk(label, cond):
    global fails, total
    total += 1
    if not cond: fails += 1; print('FAIL', label)
def typ(v, t):
    return {'str': isinstance(v, str) and v.strip() != '', 'int': type(v) is int, 'bool': type(v) is bool,
            'list[str]': isinstance(v, list) and all(isinstance(x, str) and x for x in v)}.get(t, isinstance(v, list) if t.startswith('list') else True)
def check_obj(label, obj, part):
    known = set(part['required']) | set(part['optional'])
    for k, spec in part['required'].items():
        chk(f'{label} champ obligatoire {k}', k in obj and typ(obj[k], spec['type']))
    for k, spec in part['optional'].items():
        if k in obj: chk(f'{label} champ optionnel {k} de type {spec["type"]}', typ(obj[k], spec['type']))
    chk(f'{label} aucun champ hors schéma ({sorted(set(obj) - known)})', set(obj) <= known)
banks = sorted(glob.glob(f'{root}/content/diagnostic/banque_m*.json'))
chk('schéma version 2', S['schemaVersion'] == 2)
chk('au moins 5 banques', len(banks) >= 5)
for p in banks:
    name = os.path.basename(p)[:-5]; d = json.load(open(p, encoding='utf-8'))
    check_obj(name, d, S['bank'])
    chk(f'{name} banque générale « diagnostic »', d.get('bank') == 'diagnostic')
    m = d.get('module'); chk(f'{name} module 0-8 et cohérent avec le nom', type(m) is int and 0 <= m <= 8 and name.endswith(f'{m:02d}'))
    if 'revision' in d: chk(f'{name} revision ≥ 1', d['revision'] >= 1)
    items = d.get('items', []); chk(f'{name} au moins 2 items', len(items) >= 2)
    ids = Counter(it.get('id') for it in items); chk(f'{name} identifiants uniques', all(v == 1 for v in ids.values()))
    pairs = {}
    for it in items:
        lab = f"{name} {it.get('id')}"
        check_obj(lab, it, S['item'])
        chk(f'{lab} format D<module>-<forme><paire>', bool(re.fullmatch(rf"D{m}-[AB]{it.get('pair')}", str(it.get('id')))))
        chk(f'{lab} module = module de la banque', it.get('module') == m)
        chk(f'{lab} forme A ou B', it.get('form') in ('A', 'B'))
        chk(f'{lab} paire ≥ 1', type(it.get('pair')) is int and it['pair'] >= 1)
        opts = it.get('options', [])
        chk(f'{lab} 4 options a-d distinctes', [o.get('id') for o in opts] == list('abcd') and len({o.get('text') for o in opts}) == 4 and all(isinstance(o.get('text'), str) and o['text'] for o in opts))
        chk(f'{lab} bonne réponse parmi les options', it.get('correct') in [o.get('id') for o in opts])
        pairs.setdefault(it.get('pair'), []).append(it)
    for pnum, its in pairs.items():
        chk(f'{name} paire {pnum} : une forme A et une forme B', sorted(i.get('form') for i in its) == ['A', 'B'])
        chk(f'{name} paire {pnum} : même tag', len({i.get('tag') for i in its}) == 1)
    if 'prerequisites_tested' in d:
        chk(f'{name} prerequisites_tested : une description par paire', len(d['prerequisites_tested']) == len(pairs))
    for oq in d.get('open_questions', []):
        lab = f"{name} {oq.get('id')}"
        check_obj(lab, oq, S['open_question'])
        chk(f'{lab} format D<module>-O<n>', bool(re.fullmatch(rf'D{m}-O\d+', str(oq.get('id')))))
        chk(f'{lab} non notée', oq.get('graded') is False)
print(f'{total - fails}/{total} contrôles OK ; {fails} échec(s) sur {len(banks)} banque(s)')
sys.exit(1 if fails else 0)
