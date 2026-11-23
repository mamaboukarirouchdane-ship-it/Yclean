#!/usr/bin/env python3
"""Produit le dossier de relecture indépendante à l'aveugle des QCM du module 8 (décision 2) :
- registry/relecture_aveugle_m08/FEUILLE_RELECTEUR.md : les 106 questions SANS clé, ordre des options conservé, avec grille de réponse ;
- registry/relecture_aveugle_m08/CLE_A_NE_PAS_TRANSMETTRE.json : clés et explications, à remettre seulement après la relecture.
La feuille ne contient ni explication, ni étiquette, ni indication de la bonne réponse. Usage : python3 -I tools/make_blind_review_kit_m08.py
"""
import glob, hashlib, json, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = f'{root}/registry/relecture_aveugle_m08'; os.makedirs(out, exist_ok=True)
files = sorted(glob.glob(f'{root}/content/m08/quiz/L8.*.quiz.json')) + sorted(glob.glob(f'{root}/content/m08/assessments/chap_*.quiz.json')) + [f'{root}/content/m08/assessments/EX8.exam.json']
lines = ['# Module 8 — Relecture indépendante à l\'aveugle des QCM (feuille du relecteur)', '',
         '**Consignes.** Pour chaque question : (1) choisis la réponse que tu juges correcte **sans consulter les leçons** si tu veux mesurer la devinabilité, ou **avec les leçons** si tu évalues la justesse ; indique le mode choisi en tête. (2) Coche « plusieurs défendables » si plus d\'une option peut être défendue ; « aucune » si aucune n\'est juste. (3) Signale tout indice de forme (longueur, précision, mots absolus, répétition de l\'énoncé) qui trahit la réponse. (4) Note la clarté de 1 à 3.',
         '', '**Le relecteur ne doit pas avoir rédigé les questions.** La clé (`CLE_A_NE_PAS_TRANSMETTRE.json`) est remise seulement après le retour de cette feuille.', '',
         'Mode : ☐ sans les leçons (devinabilité) ☐ avec les leçons (justesse)  —  Relecteur : ________  —  Date : ________', '']
key = {}
for p in files:
    d = json.load(open(p, encoding='utf-8')); name = os.path.basename(p).replace('.quiz.json', '').replace('.exam.json', '')
    lines += [f'## {name}', '']
    for q in d['questions']:
        lines.append(f"**{q['id']}.** {q['prompt']}")
        lines.append('')
        for o in q['options']: lines.append(f"- ({o['id']}) {o['text']}")
        lines += ['', 'Réponse : ☐a ☐b ☐c ☐d · ☐ plusieurs défendables · ☐ aucune · Indice de forme : ________ · Clarté : 1 2 3', '']
        key[q['id']] = dict(correct=q['correct'], explanation=q['explanation'])
open(f'{out}/FEUILLE_RELECTEUR.md', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
open(f'{out}/CLE_A_NE_PAS_TRANSMETTRE.json', 'w', encoding='utf-8').write(json.dumps(key, indent=2, ensure_ascii=False) + '\n')
feuille = open(f'{out}/FEUILLE_RELECTEUR.md', encoding='utf-8').read()
assert not any(w in feuille for w in ('"correct"', 'explanation', 'Explication')), 'la feuille contient une clé'
print(len(key), 'questions ;', hashlib.sha256(feuille.encode()).hexdigest()[:16], '(empreinte de la feuille)')
