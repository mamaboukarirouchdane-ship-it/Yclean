#!/usr/bin/env python3
"""Génère content/m08/assessments/EX8.exam.json. Usage: python3 -I tools/make_exam_ex8.py"""
import json, os, importlib.util, collections
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('ex8', f'{root}/tools/assessments/ex8.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
PAT = [2, 0, 3, 1, 3, 2, 0, 1, 1, 3, 0, 2, 2, 0, 3, 1, 0, 2]
qs = []
for i, (sec, p, opts, expl, tags) in enumerate(m.QCM, 1):
    tgt = PAT[i - 1]; opts = list(opts); opts[0], opts[tgt] = opts[tgt], opts[0]
    qs.append(dict(id=f'EX8-Q{i}', section=sec, type='mcq', prompt=p, options=[dict(id='abcd'[k], text=x) for k, x in enumerate(opts)], correct='abcd'[tgt], explanation=expl, tags=tags, points=2))
calc = [dict(id=f'EX8-K{i}', section=s, type='calc', prompt=p, answer=a, tolerance=t, unit=u, solution=sol, tags=tags, points=3) for i, (p, a, t, u, sol, tags, s) in enumerate(m.CALC, 1)]
ana = [dict(id=a['id'], section=a['section'], type='analysis', title=a['title'], material=a['material'], tasks=a['tasks'], expectedElements=a['expected'], points=a['points']) for a in m.ANALYSES]
tot = collections.Counter()
for x in qs + calc + ana: tot[x['section']] += x['points']
sections = [dict(id=k, title=t, points=v) for (k, t), v in zip([('A', 'Identification et qualification d\'un choc'), ('B', 'Analyse des canaux de transmission'), ('C', 'Régimes risk-on et risk-off'), ('D', 'Durée et persistance des effets'), ('E', 'Crises bancaires et souveraines'), ('F', 'Décision argumentée sur l\'or')], [tot[k] for k in 'ABCDEF'])]
d = dict(examId='EX8', module=8, title='Examen final du module 8 — Géopolitique et risques mondiaux', durationMinutes=120, passThreshold=0.7, passPoints=70,
         note='18 QCM (2 points) + 5 calculs (3 points) + 6 analyses (49 points) = 100 points ; seuil provisoire de réussite 70/100, à valider scientifiquement et pédagogiquement. Barème par section : A 20, B 20, C 15, D 15, E 15, F 15. Les données sont fictives (SIMULATION) sauf mention contraire ; aucune donnée postérieure à la date de chaque cas ne doit être utilisée. Une bonne analyse fondamentale ne garantit pas une transaction gagnante.',
         sections=sections, questions=qs, calculations=calc, analyses=ana, totalPoints=sum(tot.values()), revision=1, status='Rédigé — non validé scientifiquement')
json.dump(d, open(f'{root}/content/m08/assessments/EX8.exam.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('sections', {k: tot[k] for k in 'ABCDEF'}, 'total', d['totalPoints'], 'positions', collections.Counter(q['correct'] for q in qs))
