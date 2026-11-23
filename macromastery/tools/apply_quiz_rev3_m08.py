#!/usr/bin/env python3
"""Applique la révision 3 des QCM du module 8 (tools/quizsrc_rev3_m08.py) aux fichiers JSON et à leurs sources
(tools/quizsrc/L8.0x.py, tools/assessments/m08.py, tools/assessments/ex8.py), pour que la régénération reste cohérente.
Garanties vérifiées avant écriture : chaque texte remplacé est un distracteur (jamais la bonne réponse) présent une seule fois
dans la question et une seule fois dans sa source ; lettres des bonnes réponses, bonnes réponses, explications inchangées.
Usage : python3 -I tools/apply_quiz_rev3_m08.py [--dry-run]
"""
import glob, importlib.util, json, os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('rev3', f'{root}/tools/quizsrc_rev3_m08.py'); R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
dry = '--dry-run' in sys.argv
files = sorted(glob.glob(f'{root}/content/m08/quiz/L8.*.quiz.json')) + sorted(glob.glob(f'{root}/content/m08/assessments/chap_*.quiz.json')) + [f'{root}/content/m08/assessments/EX8.exam.json']
def source_of(qid):
    if qid.startswith('L8.'): return f'{root}/tools/quizsrc/{qid[:5]}.py'
    if qid.startswith('C8.'): return f'{root}/tools/assessments/m08.py'
    return f'{root}/tools/assessments/ex8.py'
def lit(s, text):
    """Trouve la forme littérale Python de text dans s (guillemets simples ou doubles) ; renvoie (forme, quote)."""
    for q in ('"', "'"):
        form = q + (text.replace(q, '\\' + q) if q in text else text) + q
        if s.count(form) == 1: return form, q
    raise AssertionError(f'littéral introuvable ou ambigu : {text[:60]}')
seen = set(); out = {}; src_edits = {}
for p in files:
    d = json.load(open(p, encoding='utf-8')); changed = False
    for q in d['questions']:
        qid = q['id']
        if qid in R.PROMPTS:
            old, new = R.PROMPTS[qid]; assert q['prompt'] == old, qid
            q['prompt'] = new; changed = True; seen.add(('P', qid)); src_edits.setdefault(source_of(qid), []).append((old, new))
        for old, new in R.REV3.get(qid, []):
            hits = [o for o in q['options'] if o['text'] == old]
            assert len(hits) == 1, f'{qid} : distracteur introuvable : {old[:50]}'
            assert hits[0]['id'] != q['correct'], f'{qid} : tentative de modifier la bonne réponse'
            assert new != old, qid
            hits[0]['text'] = new; changed = True; seen.add(('O', qid, old)); src_edits.setdefault(source_of(qid), []).append((old, new))
    if changed:
        if '/quiz/' in p: d['revision'] = 3
        elif 'chap_' in p: d['revision'] = 2
        else: d['revision'] = 3
    out[p] = d
assert len([k for k in seen if k[0] == 'O']) == sum(len(v) for v in R.REV3.values()), 'des remplacements n\'ont pas été appliqués'
# sources
new_src = {}
for sp, edits in src_edits.items():
    s = open(sp, encoding='utf-8').read()
    for old, new in edits:
        form, q = lit(s, old)
        s = s.replace(form, q + (new.replace(q, '\\' + q) if q in new else new) + q)
    new_src[sp] = s
if dry:
    print(f'simulation : {sum(len(v) for v in R.REV3.values())} distracteurs et {len(R.PROMPTS)} énoncé ; sources : {len(new_src)} fichiers ; rien écrit')
    json.dump({os.path.relpath(k, root): v for k, v in out.items()}, open(os.environ.get('REV3_SIM', '/dev/null'), 'w', encoding='utf-8'), ensure_ascii=False)
    sys.exit(0)
for p, d in out.items():
    s = open(p, encoding='utf-8').read()
    open(p, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + ('\n' if s.endswith('\n') else ''))
for sp, s in new_src.items():
    open(sp, 'w', encoding='utf-8').write(s)
print(f'{sum(len(v) for v in R.REV3.values())} distracteurs et {len(R.PROMPTS)} énoncé appliqués ; {len(new_src)} fichiers sources mis à jour')
