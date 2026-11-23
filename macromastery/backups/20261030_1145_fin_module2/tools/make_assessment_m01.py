#!/usr/bin/env python3
"""Génère les quiz de chapitre et l'examen du module 1 depuis tools/assessments/m01.py. Usage: python3 -I tools/make_assessment_m01.py"""
import json, os, sys, importlib.util, collections
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('m', f'{root}/tools/assessments/m01.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
PAT = [2, 0, 3, 1, 3, 2, 0, 1]
def mcq(prefix, i, t, off=0):
    prompt, opts, ci, expl, tags = t
    tgt = PAT[(i - 1 + off) % 8]; opts = list(opts); opts[ci], opts[tgt] = opts[tgt], opts[ci]
    return dict(id=f'{prefix}-Q{i}', type='mcq', prompt=prompt, options=[dict(id='abcd'[k], text=x) for k, x in enumerate(opts)], correct='abcd'[tgt], explanation=expl, tags=tags)
out = f'{root}/content/m01/assessments'; os.makedirs(out, exist_ok=True)
for ch, (title, qs) in m.CHAP.items():
    d = dict(chapterId=ch, module=1, title=f'Quiz de chapitre {ch} — {title}', passThreshold=0.8,
             note='6 questions ; seuil 80 % (au moins 5 bonnes réponses sur 6). Chiffres fictifs ou issus des leçons.',
             questions=[mcq(f'C{ch}', i, t, int(ch[-1])) for i, t in enumerate(qs, 1)], revision=1)
    json.dump(d, open(f'{out}/chap_{ch}.quiz.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
qs = [mcq('EX1', i, t) for i, t in enumerate(m.EXAM, 1)]
calc = [dict(id=f'EX1-K{i}', type='calc', prompt=p, answer=a, tolerance=tol, unit=u, solution=sol, tags=tags, points=3) for i, (p, a, tol, u, sol, tags) in enumerate(m.CALC, 1)]
d = dict(examId='EX1', module=1, title='Examen du module 1 — Macroéconomie appliquée aux marchés', durationMinutes=120, passThreshold=0.7,
         note='25 QCM (1 point) + 5 calculs (3 points) = 40 points ; seuil de réussite 28/40. Les données sont fictives (SIMULATION) sauf mention contraire.',
         questions=qs, calculations=calc, totalPoints=25 + 15, revision=1)
json.dump(d, open(f'{out}/EX1.exam.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('chap', len(m.CHAP), 'examen', len(qs), 'QCM +', len(calc), 'calculs;', collections.Counter(q['correct'] for q in qs))
