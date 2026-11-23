#!/usr/bin/env python3
"""Ajoute/met à jour une entrée de leçon dans registry/lessons.json (n'altère jamais les autres entrées).
Usage: python3 -I tools/register.py <ID> <json_partiel>"""
import json, sys, os, datetime
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = f'{root}/registry/lessons.json'; d = json.load(open(p, encoding='utf-8'))
lid = sys.argv[1]; upd = json.loads(sys.argv[2])
e = next((x for x in d['lessons'] if x['id'] == lid), None)
if e is None:
    cur = {l['id']: l for l in json.load(open(f'{root}/registry/curriculum.json', encoding='utf-8'))['lessons']}
    e = dict(id=lid, module=cur[lid]['module'], title=cur[lid]['title_initial'], duration_hours=cur[lid]['duration_hours_initial'],
             files=[], sources=[], states=dict(planned=True, written=False, sourced=False, assessed=False, integrated=False, tested=False, validated=False),
             open_points=[], revision=0)
    d['lessons'].append(e)
for k, v in upd.items():
    if k == 'states': e['states'].update(v)
    else: e[k] = v
e['updated'] = str(datetime.date.today())
d['lessons'].sort(key=lambda x: (int(x['id'][1:].split('.')[0]), int(x['id'].split('.')[1])))
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('ok', lid)
