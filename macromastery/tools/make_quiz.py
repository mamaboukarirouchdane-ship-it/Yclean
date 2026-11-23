#!/usr/bin/env python3
"""Génère content/m00/quiz/<ID>.quiz.json depuis tools/quizsrc/<ID>.py. Usage: python3 -I tools/make_quiz.py L0.04 "Titre" "note" """
import sys, json, importlib.util, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lid, title, note = sys.argv[1], sys.argv[2], sys.argv[3]
mod = sys.argv[4] if len(sys.argv) > 4 else 'm00'
spec = importlib.util.spec_from_file_location('q', f'{root}/tools/quizsrc/{lid}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
spec_r1 = importlib.util.spec_from_file_location('r1', f'{root}/tools/r1.py'); r1 = importlib.util.module_from_spec(spec_r1); spec_r1.loader.exec_module(r1)  # règle R1 (seuils de quiz)
qs = []
PATTERN = [2, 0, 3, 1, 3, 2, 0, 1]  # positions cibles de la bonne réponse (répartition équilibrée)
for i, (prompt, opts, ci, expl, tags) in enumerate(m.Q, 1):
    ids = 'abcd'
    t = PATTERN[(i - 1) % len(PATTERN)]
    opts = list(opts); opts[ci], opts[t] = opts[t], opts[ci]; ci = t
    qs.append(dict(id=f'{lid}-Q{i}', type='mcq', prompt=prompt, options=[dict(id=ids[k], text=t) for k, t in enumerate(opts)], correct=ids[ci], explanation=expl, tags=tags))
d = dict(lessonId=lid, title=f'Quiz — {title}', **r1.seuil(len(qs)), note=note, questions=qs, revision=1)
os.makedirs(f'{root}/content/{mod}/quiz', exist_ok=True)
json.dump(d, open(f'{root}/content/{mod}/quiz/{lid}.quiz.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
import collections; print(lid, len(qs), 'questions; bonnes réponses:', collections.Counter(q['correct'] for q in qs))
