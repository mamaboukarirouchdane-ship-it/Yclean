"""Audit des seuils de tous les quiz (modules 0 à 8). Aucune modification. Usage: python3 -I tools/audit_thresholds.py > sortie"""
import json, glob, re, math
root = __file__.rsplit('/tools/', 1)[0]
rows = []
files = sorted(glob.glob(f'{root}/content/m*/quiz/L*.quiz.json')) + sorted(glob.glob(f'{root}/content/m*/assessments/chap_*.quiz.json'))
for f in files:
    d = json.load(open(f, encoding='utf-8')); n = len(d['questions']); thr = d['passThreshold']
    note = d.get('note', ''); m = re.search(r'(\d+) (?:bonnes réponses )?sur (\d+)', note); k = int(m.group(1)) if m else None; nn = int(m.group(2)) if m else None
    eff = math.ceil(thr * n - 1e-9)           # bonnes réponses exigées par le seuil stocké
    ref = math.ceil(0.8 * n - 1e-9)            # règle commune proposée : 80 % arrondi à l'entier supérieur
    mod = re.search(r'/content/(m\d+)/', f).group(1); name = f.split('/')[-1].replace('.quiz.json', '')
    rows.append(dict(mod=mod, name=name, n=n, thr=thr, eff=eff, k=k, nn=nn, ref=ref, note=note, rule=d.get('passRule')))
bad = [r for r in rows if (r['k'] is not None and (r['k'] != r['eff'] or r['nn'] != r['n']))]
num = [r for r in rows if r['k'] is not None and abs(r['k'] / r['nn'] - r['thr']) > 1e-9]
print(f'quiz audités : {len(rows)} ; incohérences entre seuil stocké (réponses exigées) et note affichée : {len(bad)}')
from collections import Counter
print('répartition par nombre de questions :', dict(Counter(r['n'] for r in rows)))
print('répartition par seuil stocké :', dict(Counter(r['thr'] for r in rows)))
print(f'seuil stocké ≠ k/n affiché (écart numérique, y compris quand le nombre de réponses exigées est identique) : {len(num)}')
print('\n| Quiz | Module | Q | Seuil stocké | Exigé (stocké) | Affiché dans la note | Règle commune proposée (⌈0,8×n⌉) | Écart |')
print('|---|---|---|---|---|---|---|---|')
for r in num:
    print(f"| {r['name']} | {r['mod']} | {r['n']} | {r['thr']:.4g} | {r['eff']} sur {r['n']} | {r['k']} sur {r['nn']} | {r['ref']} sur {r['n']} | {'même effet pratique' if r['k']==r['eff'] else 'EFFET DIFFÉRENT'}; proposé : stocker {r['ref']}/{r['n']} = {r['ref']/r['n']:.4g} |")
print('\nQuiz dont le seuil stocké diffère de la règle commune proposée mais cohérents avec leur note :')
for r in rows:
    if r not in bad and r['eff'] != r['ref']: print(' ', r['name'], r['n'], r['thr'], r['eff'], 'vs', r['ref'])
print('\nRépartition des écarts numériques par module :', dict(Counter(r['mod'] for r in num)))
