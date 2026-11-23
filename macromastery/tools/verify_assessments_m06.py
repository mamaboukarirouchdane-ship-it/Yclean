import json, glob, os, math, statistics as st
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ok = 0; ko = 0
def chk(n, c):
    global ok, ko
    if c: ok += 1
    else: ko += 1; print('FAIL', n)
def near(a, b, t): return abs(a - b) <= t
for p in sorted(glob.glob(f'{root}/content/m06/assessments/*.json')):
    d = json.load(open(p, encoding='utf-8')); ids = set()
    for q in d['questions']:
        chk(f'{q["id"]} unique', q['id'] not in ids); ids.add(q['id'])
        chk(f'{q["id"]} 4 options', len(q['options']) == 4)
        chk(f'{q["id"]} bonne réponse présente', q['correct'] in [o['id'] for o in q['options']])
        chk(f'{q["id"]} options distinctes', len({o['text'] for o in q['options']}) == 4)
        chk(f'{q["id"]} explication', len(q['explanation']) > 20)
    for k in d.get('calculations', []):
        chk(f'{k["id"]} numérique', isinstance(k['answer'], (int, float)) and k['tolerance'] > 0 and len(k['solution']) > 10)
d = json.load(open(f'{root}/content/m06/assessments/EX6.exam.json', encoding='utf-8')); K = {k['id']: k for k in d['calculations']}
chk('K1', near(25 - 0.30 * 25, K['EX6-K1']['answer'], .05))
start = (3.70 - 0.5 * 3.90) / 0.5
chk('K2', near((3.90 - start) * 100, K['EX6-K2']['answer'], .5) and near(start, 3.50, 1e-9))
chk('K3', near((0.4 - 1) ** 2 + 0.4 ** 2 + 0.2 ** 2, K['EX6-K3']['answer'], .005))
chk('K4', near(0.90 * math.sqrt(252), K['EX6-K4']['answer'], .05))
chk('K5', near((4 + 0.3) / (6 + 4) * 100, K['EX6-K5']['answer'], .5))
A = {a['id']: a for a in d['analyses']}; E1 = ' '.join(A['EX6-A1']['expectedElements']); E2 = ' '.join(A['EX6-A2']['expectedElements'])
chk('A1 surprise', near(0.5 - 0.3, 0.2, 1e-9) and near((0.5 - 0.3) / 0.10, 2.0, 1e-9) and '2,0' in E1)
chk('A1 proba', near(80 - 60, 20, 0) and near(0.20 * 25, 5, 1e-9) and '+5 pb' in E1)
chk('A1 or', near(4000 * -0.012, -48, 1e-9) and near(4000 - 48, 3952, 0) and '−48 $' in E1 and '3 952' in E1)
chk('A2 somme', 45 + 35 + 25 == 105 and 40 + 35 + 25 == 100 and '105 %' in E2)
ev = 0.40 * 2.0 + 0.35 * 0 + 0.25 * -3.0
chk('A2 ev', near(ev, 0.05, 1e-9) and near(ev - 0.2, -0.15, 1e-9) and '+0,05 %' in E2 and '−0,15 %' in E2)
chk('A2 chrono', 14 - 12 == 2 and '2 jours' in E2)
br = 0.40 ** 2 + 0.35 ** 2 + (0.25 - 1) ** 2
chk('A2 brier', near(br, 0.845, 1e-9) and '0,845' in E2 and near(2 * (1 / 3) ** 2 + (2 / 3) ** 2, 0.667, 0.0005))
chk('total points', d['totalPoints'] == len(d['questions']) + 3 * len(d['calculations']) + sum(a['points'] for a in d['analyses']))
chk('25 QCM', len(d['questions']) == 25); chk('5 calculs', len(d['calculations']) == 5); chk('2 analyses', len(d['analyses']) == 2)
chk('seuil', abs(d['passThreshold'] * d['totalPoints'] - 42) < 1e-9)
# recalcul des QCM numériques
chk('6.1 surprise', near(0 - 0.38 * 25, -9.5, 1e-9)); chk('6.1 zq', near(100 - 96.94, 3.06, 1e-9))
chk('6.1 depart', near((2.5525 - 9 / 30 * 3.06) / (21 / 30), 2.335, 1e-9) and near(3.06 - 2.335, 0.725, 1e-9)); chk('6.1 z', near((3.3 - 3.0) / 0.15, 2.0, 1e-9))
x = [-1.40, -0.94, 1.30, 0.38, -0.60]
chk('6.2 moy', near(st.mean(x), -0.252, 1e-9)); chk('6.2 perm', near(1 / 5, 0.20, 1e-12)); chk('6.2 sens', near(-0.6 / 5, -0.12, 1e-9) and near(0.2 / -2, -0.10, 1e-9))
ref = [-18, -15, -12, -10, -8, -6, -5, -3, -2, 0, 1, 2, 4, 5, 7, 8, 10, 12, 15, 20]; k = 0.75 * 19; f = int(k)
chk('6.2 q3', near(ref[f] + (k - f) * (ref[f + 1] - ref[f]), 7.25, 1e-9)); chk('6.2 mixte', 3 / 12 == 0.25)
chk('6.3 laplace', near((3 + 1) / (4 + 2) * 100, 66.7, .05) and near((30 + 1) / (40 + 2) * 100, 73.8, .05))
e = 0.35 * 8 + 0.4 * 0 + 0.25 * -5; chk('6.3 ev', near(e, 1.55, 1e-9) and near(e - 0.2, 1.35, 1e-9))
chk('6.3 pstar', near((5 + 0.2) / 13, 0.40, 1e-9)); chk('6.3 ann', near(0.517 * math.sqrt(252), 8.2, .05)); chk('6.3 z', near(-2.0 / 0.8, -2.5, 1e-9)); chk('6.3 taille', near(100 / 10, 10, 0) and near(100 / 16, 6.25, 1e-9))
chk('6.4 s92', near(25 - 0.92 * 25, 2.0, 1e-9)); chk('6.4 s664', near(25 - 0.664 * 25, 8.4, 1e-9)); chk('6.4 somme', 50 + 20 + 25 + 8 == 103)
chk('6.4 ev', near(0.55 * .3 + .15 * -2 + .22 * 1.8 + .08 * -.5, 0.221, 1e-9))
for ch in ['6.1', '6.2', '6.3', '6.4']:
    c = json.load(open(f'{root}/content/m06/assessments/chap_{ch}.quiz.json', encoding='utf-8')); chk(f'chap {ch} 6 questions', len(c['questions']) == 6)
print(f'{ok} contrôles OK ; {ko} échec(s)')
