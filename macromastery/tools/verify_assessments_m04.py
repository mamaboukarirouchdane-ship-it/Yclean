import json, glob, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ok = 0; ko = 0
def chk(n, c):
    global ok, ko
    if c: ok += 1
    else: ko += 1; print('FAIL', n)
for p in sorted(glob.glob(f'{root}/content/m04/assessments/*.json')):
    d = json.load(open(p, encoding='utf-8')); ids = set()
    for q in d['questions']:
        chk(f'{q["id"]} unique', q['id'] not in ids); ids.add(q['id'])
        chk(f'{q["id"]} 4 options', len(q['options']) == 4)
        chk(f'{q["id"]} bonne réponse présente', q['correct'] in [o['id'] for o in q['options']])
        chk(f'{q["id"]} options distinctes', len({o['text'] for o in q['options']}) == 4)
        chk(f'{q["id"]} explication', len(q['explanation']) > 20)
    for k in d.get('calculations', []):
        chk(f'{k["id"]} numérique', isinstance(k['answer'], (int, float)) and k['tolerance'] > 0 and len(k['solution']) > 10)
d = json.load(open(f'{root}/content/m04/assessments/EX4.exam.json', encoding='utf-8')); K = {k['id']: k for k in d['calculations']}
def near(a, b, t): return abs(a - b) <= t
chk('K1', near(1.0850 * 1.04 / 1.02, K['EX4-K1']['answer'], .0002))
chk('K2', near((1.045 / 1.022 - 1) * 100, K['EX4-K2']['answer'], .01))
chk('K3', near((1.08 / 1.05 - 1) * 100, K['EX4-K3']['answer'], .01))
chk('K4', near(0.21007 * 1.5 + 0.14801 * 2.0 + 0.12769 * 0.5, K['EX4-K4']['answer'], .01))
chk('K5', near(0.20 ** 2 + 0.50 ** 2 + (0.30 - 1) ** 2, K['EX4-K5']['answer'], .01))
A = {a['id']: a for a in d['analyses']}; E1 = ' '.join(A['EX4-A1']['expectedElements']); E2 = ' '.join(A['EX4-A2']['expectedElements'])
chk('A1 surprise', near(0.40 * 25, 10, 1e-9) and '−10 pb' in E1)
chk('A1 réel', near(2.50 - 3.6, -1.10, 1e-9) and near(2.50 - 2.4, 0.10, 1e-9) and near(3.75 - 2.50, 1.25, 1e-9) and '−1,10' in E1 and '1,25 point' in E1)
chk('A1 change', near((1.0934 / 1.1000 - 1) * 100, -0.60, 0.005) and '−0,60 %' in E1)
chk('A2 prix', near(0.40 * 20, 8, 1e-9) and near((1.08 / 1.02 - 1) * 100, 5.88, 0.005) and '+5,88 %' in E2)
chk('A2 différentiel', near(4.50 - 3.875, 0.625, 1e-9) and near((1.03875 / 1.045 - 1) * 100, -0.60, 0.005) and '−0,60 %' in E2)
chk('A2 persistance', near((156 - 152) / (160 - 152) * 100, 50, 1e-9) and '50 %' in E2)
chk('total points', d['totalPoints'] == len(d['questions']) + 3 * len(d['calculations']) + sum(a['points'] for a in d['analyses']))
chk('25 QCM', len(d['questions']) == 25); chk('5 calculs', len(d['calculations']) == 5); chk('2 analyses', len(d['analyses']) == 2)
chk('seuil', abs(d['passThreshold'] * d['totalPoints'] - 42) < 1e-9)
# recalcul des QCM numériques de chapitre
chk('4.1 forward', near(1.1130 * 1.03875 / 1.025, 1.1279, 0.0001)); chk('4.1 inverse', near(1.1130 * 1.025 / 1.03875, 1.0983, 0.0001))
chk('4.1 fama', near(-1.019 * 1.40, -1.43, 0.01)); chk('4.1 esp', near(0.685 * 25, 17.1, 0.05)); chk('4.1 eurusd', near((1.1130 / 1.1400 - 1) * 100, -2.37, 0.01))
chk('4.2 pm', near(4.96 - 2.64, 2.32, 1e-9)); chk('4.2 tips', near(4.95 - 2.653, 2.30, 0.005)); chk('4.2 ce', 290 + 153 + 14 - 207 == 250)
chk('4.2 flux', near((798 + 1105) / 250, 7.6, 0.05)); chk('4.2 us', near(-250.9 + 92.1 - 15.8 - 38.0, -212.6, 1e-9))
chk('4.3 tot', near((1.10 / 1.04 - 1) * 100, 5.77, 0.01)); chk('4.3 bls', near((1.116 / 1.081 - 1) * 100, 3.24, 0.01)); chk('4.3 contrib', near(0.21007 * 2.37, 0.50, 0.01))
chk('4.4 reel', near(2.50 - 3.8, -1.30, 1e-9)); chk('4.4 boe', near(3 / 9 * 100, 33.3, 0.05)); chk('4.4 boc', near(3.875 - 2.50, 1.375, 1e-9)); chk('4.4 rba', near(4.60 - 4 * 0.25, 3.60, 1e-9))
chk('4.5 pm', near((1.0125 / 1.046 - 1) * 100, -3.20, 0.01)); chk('4.5 persist', near((159.09 - 155.20) / (164 - 155.20) * 100, 44.2, 0.05))
chk('4.5 brier', near((0.25 - 1) ** 2 + 0.5 ** 2 + 0.25 ** 2, 0.875, 1e-9)); chk('exam impact', near(0.20 * 30, 6, 1e-9)); chk('exam ratio', near(1903 / 250, 7.6, 0.05))
for ch in ['4.1', '4.2', '4.3', '4.4', '4.5']:
    c = json.load(open(f'{root}/content/m04/assessments/chap_{ch}.quiz.json', encoding='utf-8')); chk(f'chap {ch} 6 questions', len(c['questions']) == 6)
print(f'{ok} contrôles OK ; {ko} échec(s)')
