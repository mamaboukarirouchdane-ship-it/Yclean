#!/usr/bin/env python3
"""Génère les quiz de chapitre et les chapitres du module 8 (l'examen EX8 viendra en fin de module) depuis tools/assessments/m08.py. Usage: python3 -I tools/make_assessment_m08.py"""
import json, os, sys, importlib.util, collections
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('m', f'{root}/tools/assessments/m08.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
PAT = [2, 0, 3, 1, 3, 2, 0, 1]
def mcq(prefix, i, t, off=0):
    prompt, opts, ci, expl, tags = t
    tgt = PAT[(i - 1 + off) % 8]; opts = list(opts); opts[ci], opts[tgt] = opts[tgt], opts[ci]
    return dict(id=f'{prefix}-Q{i}', type='mcq', prompt=prompt, options=[dict(id='abcd'[k], text=x) for k, x in enumerate(opts)], correct='abcd'[tgt], explanation=expl, tags=tags)
spec_r1 = importlib.util.spec_from_file_location('r1', f'{root}/tools/r1.py'); r1 = importlib.util.module_from_spec(spec_r1); spec_r1.loader.exec_module(r1)  # règle R1 (seuils de quiz)
out = f'{root}/content/m08/assessments'; os.makedirs(out, exist_ok=True)
for ch, (title, qs) in m.CHAP.items():
    d = dict(chapterId=ch, module=8, title=f'Quiz de chapitre {ch} — {title}', **r1.seuil(len(qs)),
             note='6 questions ; seuil 80 % (au moins 5 bonnes réponses sur 6). Chiffres fictifs ou issus des leçons.',
             questions=[mcq(f'C{ch}', i, t, int(ch[-1])) for i, t in enumerate(qs, 1)], revision=(2 if ch == '8.1' else 3))  # révision 3 des QCM (23/11/2026) : +1
    json.dump(d, open(f'{out}/chap_{ch}.quiz.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('chapitres', list(m.CHAP), [len(v[1]) for v in m.CHAP.values()])
