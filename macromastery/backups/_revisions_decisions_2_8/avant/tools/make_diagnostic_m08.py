#!/usr/bin/env python3
"""Génère content/diagnostic/banque_m08.json (PROPOSITION). Usage: python3 -I tools/make_diagnostic_m08.py"""
import json, datetime as dt
root = __file__.rsplit('/tools/', 1)[0]
# (paire, forme, tag, énoncé, [bonne réponse, d1, d2, d3], calcul de contrôle -> valeur attendue)
d1 = (dt.date(2027, 5, 25) - dt.date(2027, 4, 2)).days
d2 = (dt.date(2027, 11, 5) - dt.date(2027, 9, 10)).days
assert (d1, d2) == (53, 56)
assert abs((2100 / 2000 - 1) * 100 - 5.0) < 1e-9 and abs((2450 / 2500 - 1) * 100 + 2.0) < 1e-9
assert round((3.85 - 4.05) * 100) == -20 and round((3.95 - 3.60) * 100) == 35
assert 215000 - 180000 == 35000 and abs((3.0 - 3.2) + 0.2) < 1e-9
ITEMS = [
 (1, 'A', 'variation en %', "Deux fixings du même instrument et du même horaire : 2 000 $ puis 2 100 $. Quelle est la variation ?", ["+5,0 %", "+4,8 %", "−4,8 %", "+100 %"]),
 (1, 'B', 'variation en %', "Deux fixings du même instrument et du même horaire : 2 500 $ puis 2 450 $. Quelle est la variation ?", ["−2,0 %", "+2,0 %", "−2,04 %", "−50 %"]),
 (2, 'A', 'délai en jours', "Une décision est publiée le 02/04 et une donnée de suivi le 25/05 de la même année (non bissextile). Combien de jours les séparent ?", ["53 jours", "52 jours", "54 jours", "51 jours"]),
 (2, 'B', 'délai en jours', "Une décision est publiée le 10/09 et une donnée de suivi le 05/11 de la même année (non bissextile). Combien de jours les séparent ?", ["56 jours", "55 jours", "57 jours", "54 jours"]),
 (3, 'A', 'écart à l\'attendu', "Le consensus documenté de la veille attendait 180 000 créations d'emplois ; 215 000 sont publiées. Quel est l'écart à l'attendu ?", ["+35 000", "−35 000", "+215 000", "+180 000"]),
 (3, 'B', 'écart à l\'attendu', "Le consensus documenté de la veille attendait une inflation annuelle de 3,2 % ; 3,0 % est publiée. Quel est l'écart en points ?", ["−0,2 point", "+0,2 point", "−3,2 points", "−3,0 points"]),
 (4, 'A', 'points de base', "Le rendement d'une obligation passe de 4,05 % à 3,85 %. Quelle est la variation ?", ["−20 pb", "−0,2 pb", "−5 pb", "+20 pb"]),
 (4, 'B', 'points de base', "Le rendement d'une obligation passe de 3,60 % à 3,95 %. Quelle est la variation ?", ["+35 pb", "+0,35 pb", "+3,5 pb", "−35 pb"]),
]
PAT = [0, 2, 3, 1, 1, 3, 2, 0]
items = []
for i, (pair, form, tag, prompt, opts) in enumerate(ITEMS):
    t = PAT[i]; o = list(opts); o[0], o[t] = o[t], o[0]
    items.append(dict(id=f'D8-{form}{pair}', module=8, form=form, pair=pair, tag=tag, prompt=prompt, options=[dict(id='abcd'[k], text=x) for k, x in enumerate(o)], correct='abcd'[t], prerequisite=True))
d = dict(bank='diagnostic', module=8, status='PROPOSITION — non validée, non intégrée', revision=1,
 note="Banque progressive : 4 paires de QCM parallèles (forme A = diagnostic initial, forme B = version finale alternative), même schéma que banque_m04 à banque_m07. Niveau : accessible avant le cours ; chaque item ne mobilise qu'un prérequis (pourcentage, délai en jours, écart à l'attendu, points de base), sans notion enseignée dans le module 8 (statuts, canaux, régimes, horizons, protocole). Diagnostic non noté : il sert à orienter la révision, pas à autoriser ou interdire l'accès. Les modules 0 à 3 restent à alimenter dans le diagnostic général.",
 items=items,
 open_questions=[
  dict(id='D8-O1', prompt="En quelques lignes : quelle est la différence entre une donnée observée et une prévision ? Donne un exemple tiré d'un marché.", graded=False, prerequisite_of="distinction observé / prévu, utilisée dans toutes les leçons du module"),
  dict(id='D8-O2', prompt="Cite deux facteurs, autres qu'un événement géopolitique, qui peuvent faire varier le prix de l'or au cours de la même journée.", graded=False, prerequisite_of="facteurs simultanés (dollar, taux réels, publications macroéconomiques) vus aux modules 5 et 6")],
 prerequisites_tested=["calcul d'un pourcentage de variation entre deux cotations comparables", "calcul d'un délai en jours entre deux dates", "écart entre une valeur publiée et une attente documentée", "variation d'un rendement en points de base"],
 competences_to_acquire_not_tested=["qualifier un événement (statut possible / probable / confirmé ; fait, déclaration, hypothèse)", "appliquer la grille G8 et les sept canaux avec deux directions pour l'or", "distinguer annoncé, appliqué et effet observé", "appliquer une matrice risk-on / risk-off fixée d'avance", "remplir une grille d'horizons sans reconstituer de prix", "distinguer liquidité et solvabilité", "appliquer le protocole de décision (agir, attendre, ne pas intervenir) avec l'information disponible à la date"])
json.dump(d, open(f'{root}/content/diagnostic/banque_m08.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(len(items), 'items ;', [it['correct'] for it in items])
