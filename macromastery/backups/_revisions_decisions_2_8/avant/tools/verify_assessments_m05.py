import json, glob, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ok = 0; ko = 0
def chk(n, c):
    global ok, ko
    if c: ok += 1
    else: ko += 1; print('FAIL', n)
def near(a, b, t): return abs(a - b) <= t
for p in sorted(glob.glob(f'{root}/content/m05/assessments/*.json')):
    d = json.load(open(p, encoding='utf-8')); ids = set()
    for q in d['questions']:
        chk(f'{q["id"]} unique', q['id'] not in ids); ids.add(q['id'])
        chk(f'{q["id"]} 4 options', len(q['options']) == 4)
        chk(f'{q["id"]} bonne réponse présente', q['correct'] in [o['id'] for o in q['options']])
        chk(f'{q["id"]} options distinctes', len({o['text'] for o in q['options']}) == 4)
        chk(f'{q["id"]} explication', len(q['explanation']) > 20)
    for k in d.get('calculations', []):
        chk(f'{k["id"]} numérique', isinstance(k['answer'], (int, float)) and k['tolerance'] > 0 and len(k['solution']) > 10)
d = json.load(open(f'{root}/content/m05/assessments/EX5.exam.json', encoding='utf-8')); K = {k['id']: k for k in d['calculations']}
chk('K1', near(3900 * 0.025, K['EX5-K1']['answer'], .05))
chk('K2', near(4200 / 1.20, K['EX5-K2']['answer'], .5))
chk('K3', near(480e9 / (3800 * 32150.7), K['EX5-K3']['answer'], 1.5))
chk('K4', near((4000 + 4000 * 0.005 * 0.25) * 1.04 ** 0.25, K['EX5-K4']['answer'], .02))
chk('K5', near(0.5 * 3900 + 0.3 * 4000 + 0.2 * 4300, K['EX5-K5']['answer'], .5))
A = {a['id']: a for a in d['analyses']}; E1 = ' '.join(A['EX5-A1']['expectedElements']); E2 = ' '.join(A['EX5-A2']['expectedElements'])
chk('A1 âges', 15 - 0 == 15 and 15 - 10 == 5 and '15 jours' in E1 and '5 jours' in E1)
chk('A1 nominal', near(1.60 + 2.20, 3.80, 1e-9) and near(1.80 + 2.10, 3.90, 1e-9) and near(3.90 - 3.80, 0.10, 1e-9) and near(1.80 - 1.60, 0.20, 1e-9) and near(2.10 - 2.20, -0.10, 1e-9) and '+0,10 point' in E1)
chk('A1 dollar', near((98.0 / 99.2 - 1) * 100, -1.21, 0.005) and '−1,21 %' in E1)
chk('A1 note', -1 + 1 + 1 - 1 == 0 and -2 + 1 + 1 - 1 == -1 and '= 0' in E1 and '= −1' in E1)
chk('A2 EV', near(0.3 + 0.4 + 0.3, 1, 1e-9) and near(0.3 * 2700 + 0.4 * 3000 + 0.3 * 3400, 3030, 1e-9) and near((3030 / 3000 - 1) * 100, 1.0, 0.005) and '3 030' in E2 and '+1,0 %' in E2)
chk('A2 écart', near((2700 / 3030 - 1) * 100, -10.9, 0.05) and '−10,9 %' in E2)
chk('A2 brier', near((0.3 - 1) ** 2 + 0.4 ** 2 + 0.3 ** 2, 0.74, 1e-9) and '0,74' in E2 and near(2 * (1 / 3) ** 2 + (2 / 3) ** 2, 0.667, 0.0005))
chk('total points', d['totalPoints'] == len(d['questions']) + 3 * len(d['calculations']) + sum(a['points'] for a in d['analyses']))
chk('25 QCM', len(d['questions']) == 25); chk('5 calculs', len(d['calculations']) == 5); chk('2 analyses', len(d['analyses']) == 2)
chk('seuil', abs(d['passThreshold'] * d['totalPoints'] - 42) < 1e-9)
# recalcul des QCM numériques
chk('5.1 prix', near((35 / 20.67 - 1) * 100, 69.3, .05)); chk('5.1 inv', near(2175.3 / 5002.3 * 100, 43.5, .05)); chk('5.1 offre', near(3671.6 + 1404.3 - 73.6, 5002.3, .05))
chk('5.1 rec', near((4060 / 5595 - 1) * 100, -27.4, .05)); chk('5.1 bc', near(288.9 / 56.5, 5.11, .005)); chk('5.1 bij', near((278.2 / 335.3 - 1) * 100, -17.0, .05))
chk('5.2 pm', near(4.95 - 2.653, 2.297, 5e-4)); chk('5.2 fisher', near((1.0495 / 1.02653 - 1) * 100, 2.238, 5e-4)); chk('5.2 co', near(4060 * 0.0264, 107.2, .05))
chk('5.2 dr', near(2.64 - 2.04, 0.60, 1e-9)); chk('5.2 eur', near((4100 / 1.15) / (4000 / 1.10) * 100 - 100, -1.96, .005)); chk('5.2 nom', near(2.64 + 2.35, 4.99, 1e-9))
chk('5.2 poids', near(21.007, 21.0, .01)); chk('5.2 depuis mai', near(4.99 - 4.48, 0.51, 1e-9))
chk('5.3 reste', near((288.9 - 100) / 288.9 * 100, 65.4, .05)); chk('5.3 etf', near(67 / (4256 - 67) * 100, 1.6, .05))
chk('5.3 px', near(574e9 / (4256 * 32150.7), 4195, 1)); chk('5.3 sem', near(62.4 - 44.8, 17.6, 1e-9))
chk('5.4 notionnel', 100 * 4060 == 406000 and near(100 * 0.10, 10, 1e-9)); chk('5.4 base', near(4103.80 - 4081.65, 22.15, 1e-9))
chk('5.4 roll', 4141 - 4100 == 41 and near((4141 / 4100 - 1) * 100, 1.00, .005)); chk('5.4 crise', near((5182.40 / 5400 - 1) * 100, -4.0, .05)); chk('5.4 usd', near((100.5 / 96 - 1) * 100, 4.7, .05))
chk('5.5 bais', near((318 / 667 - 1) * 100, -52.3, .05)); chk('5.5 durées', near(sum([21, 21, 25, 141, 52]) / 5, 52, 0)); chk('5.5 ev', near(.3 * 2000 + .5 * 1750 + .2 * 1450, 1765, 1e-9))
chk('5.5 brier', near(.3 ** 2 + .5 ** 2 + (.2 - 1) ** 2, 0.98, 1e-9)); chk('exam 1934', near((35 / 20.67 - 1) * 100, 69.3, .05)); chk('exam 850', near((850 / 667 - 1) * 100, 27.4, .05))
chk('exam 5595', near(5595 - 5589, 6, 0) and near(6 / 5595 * 100, 0.11, .005))
for ch in ['5.1', '5.2', '5.3', '5.4', '5.5']:
    c = json.load(open(f'{root}/content/m05/assessments/chap_{ch}.quiz.json', encoding='utf-8')); chk(f'chap {ch} 6 questions', len(c['questions']) == 6)
print(f'{ok} contrôles OK ; {ko} échec(s)')
