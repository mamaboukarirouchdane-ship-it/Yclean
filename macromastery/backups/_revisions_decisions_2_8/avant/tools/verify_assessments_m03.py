import json, glob, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ok = 0; ko = 0
def chk(n, c):
    global ok, ko
    if c: ok += 1
    else: ko += 1; print('FAIL', n)
for p in sorted(glob.glob(f'{root}/content/m03/assessments/*.json')):
    d = json.load(open(p, encoding='utf-8')); ids = set()
    for q in d['questions']:
        chk(f'{q["id"]} unique', q['id'] not in ids); ids.add(q['id'])
        chk(f'{q["id"]} 4 options', len(q['options']) == 4)
        chk(f'{q["id"]} bonne réponse présente', q['correct'] in [o['id'] for o in q['options']])
        chk(f'{q["id"]} options distinctes', len({o['text'] for o in q['options']}) == 4)
        chk(f'{q["id"]} explication', len(q['explanation']) > 20)
    for k in d.get('calculations', []):
        chk(f'{k["id"]} numérique', isinstance(k['answer'], (int, float)) and k['tolerance'] > 0 and len(k['solution']) > 10)
d = json.load(open(f'{root}/content/m03/assessments/EX3.exam.json', encoding='utf-8')); K = {k['id']: k for k in d['calculations']}
def near(a, b, t): return abs(a - b) <= t
chk('K1', near((29000 - 90000) / 35600, K['EX3-K1']['answer'], .01))
chk('K2', near((1.005 ** 12 - 1) * 100, K['EX3-K2']['answer'], .01))
chk('K3', near((1.063 / 1.037 - 1) * 100, K['EX3-K3']['answer'], .01))
chk('K4', near((55.3 + 56.7 + 52.7 + 59.0 + 48.6) / 5, K['EX3-K4']['answer'], .01))
chk('K5', near((1.056 / 1.034 - 1) * 100, K['EX3-K5']['answer'], .01))
A = {a['id']: a for a in d['analyses']}
chk('A1 z', near((70000 - 110000) / 40000, -1.0, 1e-9) and 'z = −1,00' in ' '.join(A['EX3-A1']['expectedElements']))
chk('A1 intervalle', near(70000 - 120000, -50000, 0) and near(70000 + 120000, 190000, 0) and '−50 000 à +190 000' in ' '.join(A['EX3-A1']['expectedElements']))
chk('A1 total', 62000 + 8000 == 70000)
chk('A1 salaire réel', near((1.036 / 1.032 - 1) * 100, 0.39, 0.005))
chk('A2 annualisation', near((1.002 ** 12 - 1) * 100, 2.43, 0.005) and near((1.004 ** 12 - 1) * 100, 4.91, 0.005))
chk('A2 contributions', near(0.08 * 3.0 + 0.13 * 0.1 + 0.79 * 0.2, 0.411, 1e-9) and abs(8 + 13 + 79 - 100) == 0)
chk('A2 énergie', near(0.08 * 3.0, 0.24, 1e-9)); chk('A2 coeur', near(0.79 * 0.2, 0.158, 1e-9))
chk('total points', d['totalPoints'] == len(d['questions']) + 3 * len(d['calculations']) + sum(a['points'] for a in d['analyses']))
chk('25 QCM', len(d['questions']) == 25); chk('5 calculs', len(d['calculations']) == 5); chk('2 analyses', len(d['analyses']) == 2)
chk('seuil', abs(d['passThreshold'] * d['totalPoints'] - 42) < 1e-9)
for ch in ['3.1', '3.2', '3.3', '3.4', '3.5', '3.6']:
    c = json.load(open(f'{root}/content/m03/assessments/chap_{ch}.quiz.json', encoding='utf-8')); chk(f'chap {ch} 6 questions', len(c['questions']) == 6)
print(f'{ok} contrôles OK ; {ko} échec(s)')
