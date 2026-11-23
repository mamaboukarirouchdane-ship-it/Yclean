#!/usr/bin/env python3
"""Génère content/m08/assessments/EX8.exam.json. Usage: python3 -I tools/make_exam_ex8.py"""
import json, os, importlib.util, collections
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('ex8', f'{root}/tools/assessments/ex8.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
PAT = [2, 0, 3, 1, 3, 2, 0, 1, 1, 3, 0, 2, 2, 0, 3, 1, 0, 2]
qs = []
for i, (sec, p, opts, expl, tags) in enumerate(m.QCM, 1):
    tgt = PAT[i - 1]; opts = list(opts); opts[0], opts[tgt] = opts[tgt], opts[0]
    qs.append(dict(id=f'EX8-Q{i}', section=sec, type='mcq', prompt=p, options=[dict(id='abcd'[k], text=x) for k, x in enumerate(opts)], correct='abcd'[tgt], explanation=expl, tags=tags, points=1))
calc = [dict(id=f'EX8-K{i}', section=s, type='calc', prompt=p, answer=a, tolerance=t, unit=u, solution=sol, tags=tags, points=3) for i, (p, a, t, u, sol, tags, s) in enumerate(m.CALC, 1)]
ana = [dict(id=a['id'], section=a['section'], type='analysis', title=a['title'], material=a['material'], tasks=a['tasks'], expectedElements=a['expected'], points=a['points'], taskPoints=a['taskPoints']) for a in m.ANALYSES]
assert all(len(a['taskPoints']) == len(a['tasks']) and sum(a['taskPoints']) == a['points'] for a in ana)
tot = collections.Counter()
for x in qs + calc + ana: tot[x['section']] += x['points']
sections = [dict(id=k, title=t, points=v) for (k, t), v in zip([('A', 'Identification et qualification d\'un choc'), ('B', 'Analyse des canaux de transmission'), ('C', 'Régimes risk-on et risk-off'), ('D', 'Durée et persistance des effets'), ('E', 'Crises bancaires et souveraines'), ('F', 'Décision argumentée sur l\'or')], [tot[k] for k in 'ABCDEF'])]
d = dict(examId='EX8', module=8, title='Examen final du module 8 — Géopolitique et risques mondiaux', durationMinutes=120,
         durationStatus='Hypothèse non validée : durée à fixer après essais chronométrés (registry/M8_PROTOCOLE_ESSAIS_CHRONOMETRES.md)',
         passThreshold=0.7, passPoints=70, sectionMinimums=dict(A=10, D=8, F=8),
         passRule='Réussite : total ≥ 70/100 ET minimum atteint dans chacune des sections A (10/20), D (8/15) et F (8/15) ; aucun minimum pour B, C et E.',
         scoringRules=['Chaque tâche d\'analyse est notée 0, moitié ou plein, selon des descripteurs écrits avant la correction.', 'Une erreur de calcul reportée dans une étape suivante correcte n\'est pas sanctionnée deux fois.', 'Toute réponse qui présente une prévision de prix ou une certitude de gain perd les points de la tâche de conclusion concernée.', 'L\'usage de données postérieures à la date du cas est interdit.'],
         note='Barème v2 (23/11/2026) : 18 QCM (1 point) + 5 calculs (3 points) + 6 analyses (67 points) = 100 points ; réussite provisoire : 70/100 et minima A 10/20, D 8/15, F 8/15, à valider scientifiquement et pédagogiquement. Durée de 120 minutes : hypothèse non validée. Barème par section : A 20, B 20, C 15, D 15, E 15, F 15. Les données sont fictives (SIMULATION) sauf mention contraire ; aucune donnée postérieure à la date de chaque cas ne doit être utilisée. Une bonne analyse fondamentale ne garantit pas une transaction gagnante.',
         sections=sections, questions=qs, calculations=calc, analyses=ana, totalPoints=sum(tot.values()), revision=3, status='Rédigé — non validé scientifiquement')
json.dump(d, open(f'{root}/content/m08/assessments/EX8.exam.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('sections', {k: tot[k] for k in 'ABCDEF'}, 'total', d['totalPoints'], 'positions', collections.Counter(q['correct'] for q in qs))
