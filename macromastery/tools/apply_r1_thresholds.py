#!/usr/bin/env python3
"""Décision 3 de l'utilisateur (31/10/2026) : règle R1 appliquée aux 73 quiz listés dans
backups/_revisions_decisions_1_3/LISTE_73_QUIZ.txt (35 quiz de leçon des modules 4 à 7, 38 quiz de chapitre des modules 0 à 7).

R1 : requiredCorrect = ⌈0,8 × n⌉ (entier) ; passThreshold = requiredCorrect / n ; passRule ajoutée.
Seules les clés de seuil sont touchées : questions, énoncés, options, bonnes réponses, explications, note, titre et révision restent identiques.
Le script refuse d'écrire si le nombre exigé selon R1 diffère de celui affiché dans la note ou de celui qu'impose le seuil stocké actuel.
Usage : python3 -I tools/apply_r1_thresholds.py [--dry-run]
"""
import json, math, os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
liste = os.path.join(root, 'backups', '_revisions_decisions_1_3', 'LISTE_73_QUIZ.txt')
dry = '--dry-run' in sys.argv
files = open(liste, encoding='utf-8').read().split()
assert len(files) == 73, len(files)
SEUIL_PEDAGOGIQUE = 0.8
done = 0
for rel in files:
    p = os.path.join(root, rel)
    s = open(p, encoding='utf-8').read()
    d = json.loads(s)
    assert 'requiredCorrect' not in d and 'passRule' not in d, f'{rel} : déjà traité'
    n = len(d['questions'])
    rc = math.ceil(SEUIL_PEDAGOGIQUE * n - 1e-9)
    m = re.search(r'(\d+) (?:bonnes réponses )?sur (\d+)', d['note'])
    assert m and int(m.group(1)) == rc and int(m.group(2)) == n, f'{rel} : note incompatible avec R1'
    assert math.ceil(d['passThreshold'] * n - 1e-9) == rc, f'{rel} : effet pratique différent'
    new = {}
    for k, v in d.items():
        if k == 'passThreshold':
            new['passThreshold'] = rc / n
            new['requiredCorrect'] = rc
            new['passRule'] = f'{rc} bonnes réponses sur {n} (règle R1 : ⌈0,8 × {n}⌉ = {rc} ; seuil pédagogique provisoire)'
        else:
            new[k] = v
    out = json.dumps(new, indent=2, ensure_ascii=False) + ('\n' if s.endswith('\n') else '')
    if not dry:
        open(p, 'w', encoding='utf-8').write(out)
    done += 1
print(f'{done} quiz {"vérifiés (simulation, rien écrit)" if dry else "mis à jour"} selon R1')
