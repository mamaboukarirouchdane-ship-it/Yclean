#!/usr/bin/env python3
"""Tableau de suivi : fusionne registry/curriculum.json (architecture) et registry/lessons.json (états réels). Usage: python3 -I tools/status.py"""
import json, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cur = json.load(open(f'{root}/registry/curriculum.json', encoding='utf-8'))
reg = {e['id']: e for e in json.load(open(f'{root}/registry/lessons.json', encoding='utf-8'))['lessons']}
steps = ['planned', 'written', 'sourced', 'assessed', 'integrated', 'tested', 'validated']
tot = {s: 0 for s in steps}; hrs = 0
print(f"{'Module':<8}{'Leçons':>7}{'Heures':>8}" + ''.join(f"{s[:5]:>7}" for s in steps))
for m in cur['modules']:
    ls = [l for l in cur['lessons'] if l['module'] == m['module']]
    c = {s: 0 for s in steps}
    for l in ls:
        st = reg.get(l['id'], {}).get('states', {'planned': True})
        for s in steps:
            if st.get(s): c[s] += 1; tot[s] += 1
    h = sum(l['duration_hours_initial'] for l in ls); hrs += h
    print(f"{m['module']:<8}{len(ls):>7}{h:>8.1f}" + ''.join(f"{c[s]:>7}" for s in steps))
print(f"{'Total':<8}{len(cur['lessons']):>7}{hrs:>8.1f}" + ''.join(f"{tot[s]:>7}" for s in steps))
