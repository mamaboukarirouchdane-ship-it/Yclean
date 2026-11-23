import json, glob, math, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ok = 0; ko = 0
def chk(n, c):
    global ok, ko
    if c: ok += 1
    else: ko += 1; print('FAIL', n)
for p in sorted(glob.glob(f'{root}/content/m01/assessments/*.json')):
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
d = json.load(open(f'{root}/content/m01/assessments/EX1.exam.json', encoding='utf-8')); K = {k['id']: k for k in d['calculations']}
def near(a, b, t): return abs(a - b) <= t
chk('K1', near((19011 - 19154) / 19154 * 100, K['EX1-K1']['answer'], .01))
chk('K2', near((1.05 / 1.02 - 1) * 100, K['EX1-K2']['answer'], .01))
i_ = 0.0617 / 12; chk('K3', near(200000 * i_ / (1 - (1 + i_) ** -360), K['EX1-K3']['answer'], .02))
chk('K4', near(80 * 1.035 / 1.025 + 2, K['EX1-K4']['answer'], .01))
chk('K5', near((1.03 / 1.037 - 1) * 100, K['EX1-K5']['answer'], .01))
chk('total points', d['totalPoints'] == len(d['questions']) + 3 * len(d['calculations']))
print(f'{ok} contrôles OK ; {ko} échec(s)')
