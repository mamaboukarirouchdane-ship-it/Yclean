#!/usr/bin/env python3
"""Contrôle de la révision 3 des QCM du module 8 (décision 2). Lecture seule.
Usage : python3 -I tools/verify_quiz_rev3_m08.py [simulation.json]

1. Critère d'acceptation (décision 2) : dans chaque groupe (quiz de leçon, quiz de chapitre, QCM d'EX8), l'heuristique
   « choisir la réponse la plus longue » réussit au plus 30 % (crédit fractionnaire en cas d'égalité).
2. Indices de rang voisins, contrôlés pour ne pas déplacer le biais : « deuxième plus longue » et « plus courte » ≤ 35 %.
3. Intégrité par rapport à la sauvegarde d'avant la révision (backups/_revisions_decisions_2_8/avant) : mêmes questions,
   mêmes identifiants, même lettre et même texte de bonne réponse, mêmes explications, mêmes énoncés (sauf exceptions
   listées dans PROMPTS de tools/quizsrc_rev3_m08.py), 4 options distinctes, aucune bonne réponse raccourcie.
Indices rapportés sans seuil (information) : précision (ponctuation), mots absolus.
Ces contrôles ne remplacent pas une relecture humaine indépendante à l'aveugle.
"""
import glob, importlib.util, json, os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('rev3', f'{root}/tools/quizsrc_rev3_m08.py'); R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
bk = f'{root}/backups/_revisions_decisions_2_8/avant'
rels = [os.path.relpath(p, root) for p in sorted(glob.glob(f'{root}/content/m08/quiz/L8.*.quiz.json')) + sorted(glob.glob(f'{root}/content/m08/assessments/chap_*.quiz.json'))] + ['content/m08/assessments/EX8.exam.json']
if len(sys.argv) > 1:
    sim = json.load(open(sys.argv[1], encoding='utf-8')); cur = {r: sim[r] for r in rels}
else:
    cur = {r: json.load(open(f'{root}/{r}', encoding='utf-8')) for r in rels}
old = {r: json.load(open(f'{bk}/{r}', encoding='utf-8')) for r in rels}
ABS = re.compile(r"\b(toujours|jamais|aucun[e]?|seulement|uniquement|entièrement|exactement|tous|toutes|systématiquement|nécessairement|quel que soit|quelle que soit|totalité|garanti|dès que|même sans|n'a eu aucun|sans exception)\b", re.I)
fails = total = 0
def chk(label, cond):
    global fails, total
    total += 1
    if not cond: fails += 1; print('FAIL', label)
def credit(q, key, pick_max=True):
    sc = {o['id']: key(o) for o in q['options']}; m = (max if pick_max else min)(sc.values()); w = [k for k, v in sc.items() if v == m]
    return (1 / len(w)) if q['correct'] in w else 0.0
def second(q):
    L = sorted({len(o['text']) for o in q['options']}, reverse=True)
    if len(L) < 2: return 0.25
    w = [o['id'] for o in q['options'] if len(o['text']) == L[1]]
    return (1 / len(w)) if q['correct'] in w else 0.0
groups = {'quiz de leçon': [r for r in rels if '/quiz/' in r], 'quiz de chapitre': [r for r in rels if 'chap_' in r], 'QCM d\'EX8': [rels[-1]]}
print('Heuristiques de devinette (hasard = 25 %) :')
for g, rs in groups.items():
    qs = [q for r in rs for q in cur[r]['questions']]; n = len(qs)
    lon = 100 * sum(credit(q, lambda o: len(o['text'])) for q in qs) / n
    sec = 100 * sum(second(q) for q in qs) / n
    cou = 100 * sum(credit(q, lambda o: len(o['text']), False) for q in qs) / n
    pre = 100 * sum(credit(q, lambda o: o['text'].count(',') + o['text'].count(';') + o['text'].count(':')) for q in qs) / n
    ab_c = sum(len(ABS.findall(next(o for o in q['options'] if o['id'] == q['correct'])['text'])) for q in qs)
    ab_d = sum(len(ABS.findall(o['text'])) for q in qs for o in q['options'] if o['id'] != q['correct'])
    print(f'  {g} ({n}) : plus longue {lon:.1f} % ; deuxième plus longue {sec:.1f} % ; plus courte {cou:.1f} % ; précision {pre:.1f} % ; absolus {ab_c} (bonnes) / {ab_d} (distracteurs)')
    chk(f'{g} : plus longue ≤ 30 % ({lon:.1f} %)', lon <= 30 + 1e-9)
    chk(f'{g} : deuxième plus longue ≤ 35 % ({sec:.1f} %)', sec <= 35 + 1e-9)
    chk(f'{g} : plus courte ≤ 35 % ({cou:.1f} %)', cou <= 35 + 1e-9)
for r in rels:
    A, B = old[r]['questions'], cur[r]['questions']
    chk(f'{r} mêmes questions', [q['id'] for q in A] == [q['id'] for q in B])
    for a, b in zip(A, B):
        ca = next(o['text'] for o in a['options'] if o['id'] == a['correct']); cb = next(o['text'] for o in b['options'] if o['id'] == b['correct'])
        chk(f"{b['id']} même lettre de bonne réponse", a['correct'] == b['correct'])
        chk(f"{b['id']} même texte de bonne réponse", ca == cb)
        chk(f"{b['id']} même explication", a['explanation'] == b['explanation'])
        exp_prompt = R.PROMPTS[b['id']][1] if b['id'] in R.PROMPTS else a['prompt']
        chk(f"{b['id']} énoncé attendu", b['prompt'] == exp_prompt)
        chk(f"{b['id']} 4 options distinctes, mêmes identifiants", [o['id'] for o in b['options']] == [o['id'] for o in a['options']] and len({o['text'] for o in b['options']}) == 4)
        changed = {o['id'] for o, p in zip(b['options'], a['options']) if o['text'] != p['text']}
        chk(f"{b['id']} seuls des distracteurs modifiés", b['correct'] not in changed)
        chk(f"{b['id']} modifications = celles de la révision 3", len(changed) == len(R.REV3.get(b['id'], [])))
        for k in a:
            if k not in ('options', 'prompt') and not (k == 'points' and b['id'].startswith('EX8')):  # points d'EX8 : barème v2 (décision 4), contrôlés par verify_baremes_ex8_p8.py
                chk(f"{b['id']} champ {k} inchangé", a[k] == b.get(k))
print(f'{total - fails}/{total} contrôles OK ; {fails} échec(s)')
sys.exit(1 if fails else 0)
