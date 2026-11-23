"""Audit 'à l'aveugle' automatisé : heuristiques de devinette sans connaître la clé. Usage: python3 -I tools/blind_audit_quizzes_m08.py"""
import json, glob, re, collections, itertools
root = __file__.rsplit('/tools/', 1)[0]
ABS = re.compile(r"\b(toujours|jamais|aucun[e]?|seulement|uniquement|entièrement|exactement|tous|toutes|systématiquement|nécessairement|quel que soit|quelle que soit|totalité|garanti|dès que|même sans|n'a eu aucun|sans exception)\b", re.I)
def toks(t): return set(w for w in re.findall(r"[a-zàâçéèêëîïôûùüœ0-9]{4,}", t.lower()))
def load():
    out = []
    for p in sorted(glob.glob(f'{root}/content/m08/quiz/L8.*.quiz.json')) + sorted(glob.glob(f'{root}/content/m08/assessments/chap_*.quiz.json')):
        d = json.load(open(p, encoding='utf-8'))
        for q in d['questions']: out.append((p.split('/')[-1], q))
    d = json.load(open(f'{root}/content/m08/assessments/EX8.exam.json', encoding='utf-8'))
    for q in d['questions']: out.append(('EX8.exam.json', q))
    return out
def pick(q, f):
    sc = {o['id']: f(q, o) for o in q['options']}
    m = max(sc.values()); w = [k for k, v in sc.items() if v == m]
    return (1.0 / len(w)) if q['correct'] in w else 0.0   # crédit fractionnaire en cas d'égalité
H = {
 'plus longue': lambda q, o: len(o['text']),
 'plus de chiffres': lambda q, o: sum(c.isdigit() for c in o['text']),
 'recouvrement avec l\'énoncé': lambda q, o: len(toks(o['text']) & toks(q['prompt'])),
 'plus proche des autres options': lambda q, o: sum(len(toks(o['text']) & toks(x['text'])) for x in q['options'] if x is not o),
 'moins d\'absolus': lambda q, o: -len(ABS.findall(o['text'])),
 'plus de virgules/point-virgule (précision)': lambda q, o: o['text'].count(',') + o['text'].count(';') + o['text'].count(':'),
}
groups = collections.OrderedDict([('quiz de leçon (64)', lambda n: n.startswith('L8.')), ('quiz de chapitre (24)', lambda n: n.startswith('chap_')), ('QCM EX8 (18)', lambda n: n.startswith('EX8'))])
data = load()
print('Taux de réussite de chaque heuristique de devinette (hasard = 25 %) :')
for g, sel in groups.items():
    qs = [q for n, q in data if sel(n)]
    print(f'\n{g}:', len(qs), 'questions')
    for h, f in H.items():
        print(f'  {h:45s} {100*sum(pick(q, f) for q in qs)/len(qs):5.1f} %')
    ab_c = sum(len(ABS.findall(next(o for o in q["options"] if o["id"] == q["correct"])["text"])) for q in qs)
    ab_d = sum(len(ABS.findall(o['text'])) for q in qs for o in q['options'] if o['id'] != q['correct'])
    print(f'  marqueurs absolus : {ab_c} dans les bonnes réponses ; {ab_d} dans les distracteurs ({ab_d/(3*len(qs)):.2f} par distracteur)')
flag = []
for n, q in data:
    L = {o['id']: len(o['text']) for o in q['options']}; others = [v for k, v in L.items() if k != q['correct']]
    r = L[q['correct']] / (sum(others) / 3)
    ab_c = len(ABS.findall(next(o for o in q['options'] if o['id'] == q['correct'])['text'])); ab_d = [len(ABS.findall(o['text'])) for o in q['options'] if o['id'] != q['correct']]
    if r >= 1.35 or (ab_c == 0 and sum(1 for a in ab_d if a) == 3):
        flag.append((n, q['id'], round(r, 2), ab_c, ab_d))
print('\nQuestions signalées (rapport de longueur ≥ 1,35, ou absolus dans les trois distracteurs et aucun dans la bonne réponse) :', len(flag))
for x in flag: print(' ', x)
