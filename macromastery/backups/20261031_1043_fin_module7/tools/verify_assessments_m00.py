import json, glob, math, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ok = 0; ko = 0
def chk(n, c):
    global ok, ko
    if c: ok += 1
    else: ko += 1; print('FAIL', n)
for p in sorted(glob.glob(f'{root}/content/m00/assessments/*.json')):
    d = json.load(open(p, encoding='utf-8')); ids = set()
    for q in d['questions']:
        chk(f'{q["id"]} unique', q['id'] not in ids); ids.add(q['id'])
        chk(f'{q["id"]} 4 options', len(q['options']) == 4)
        chk(f'{q["id"]} bonne réponse présente', q['correct'] in [o['id'] for o in q['options']])
        chk(f'{q["id"]} options distinctes', len({o['text'] for o in q['options']}) == 4)
        chk(f'{q["id"]} explication', len(q['explanation']) > 20)
    for k in d.get('calculations', []):
        chk(f'{k["id"]} numérique', isinstance(k['answer'], (int, float)) and k['tolerance'] > 0 and len(k['solution']) > 10)
# Recalcul indépendant des 5 calculs
d = json.load(open(f'{root}/content/m00/assessments/EX0.exam.json', encoding='utf-8')); K = {k['id']: k for k in d['calculations']}
def near(a, b, t): return abs(a - b) <= t
chk('K1', near(150 / (30 * 10), K['EX0-K1']['answer'], .005))
chk('K2', near(1.09 * 148, K['EX0-K2']['answer'], .01))
chk('K3', near(2000 / 31.1034768, K['EX0-K3']['answer'], .01))
chk('K4', near(sum(50 / 1.04 ** k for k in (1, 2)) + 1050 / 1.04 ** 3, K['EX0-K4']['answer'], .01))
pk = 0; m = 0
for x in (100, 108, 102, 112, 104, 109): pk = max(pk, x); m = min(m, x / pk - 1)
chk('K5', near(-m * 100, K['EX0-K5']['answer'], .01))
chk('total points', d['totalPoints'] == len(d['questions']) + 3 * len(d['calculations']))
print(f'{ok} contrôles OK ; {ko} échec(s)')
