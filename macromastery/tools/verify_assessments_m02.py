import json, glob, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ok = 0; ko = 0
def chk(n, c):
    global ok, ko
    if c: ok += 1
    else: ko += 1; print('FAIL', n)
for p in sorted(glob.glob(f'{root}/content/m02/assessments/*.json')):
    d = json.load(open(p, encoding='utf-8')); ids = set()
    for q in d['questions']:
        chk(f'{q["id"]} unique', q['id'] not in ids); ids.add(q['id'])
        chk(f'{q["id"]} 4 options', len(q['options']) == 4)
        chk(f'{q["id"]} bonne réponse présente', q['correct'] in [o['id'] for o in q['options']])
        chk(f'{q["id"]} options distinctes', len({o['text'] for o in q['options']}) == 4)
        chk(f'{q["id"]} explication', len(q['explanation']) > 20)
    for k in d.get('calculations', []):
        chk(f'{k["id"]} numérique', isinstance(k['answer'], (int, float)) and k['tolerance'] > 0 and len(k['solution']) > 10)
d = json.load(open(f'{root}/content/m02/assessments/EX2.exam.json', encoding='utf-8')); K = {k['id']: k for k in d['calculations']}
def near(a, b, t): return abs(a - b) <= t
chk('K1', near(2 + 3.5 + 0.5 * (3.5 - 2) + 0.5 * (-2), K['EX2-K1']['answer'], .01))
chk('K2', near(3.875 + 0.5 * (4.6 - 3.875), K['EX2-K2']['answer'], .01))
chk('K3', near(0 - 0.70 * 25, K['EX2-K3']['answer'], .1))
chk('K4', near(4500 * 0.038, K['EX2-K4']['answer'], .1))
chk('K5', near(11 / 16 * 100, K['EX2-K5']['answer'], .01))
chk('total points', d['totalPoints'] == len(d['questions']) + 3 * len(d['calculations']))
chk('25 QCM', len(d['questions']) == 25); chk('5 calculs', len(d['calculations']) == 5)
for ch in ['2.1', '2.2', '2.3', '2.4', '2.5']:
    c = json.load(open(f'{root}/content/m02/assessments/chap_{ch}.quiz.json', encoding='utf-8')); chk(f'chap {ch} 6 questions', len(c['questions']) == 6)
print(f'{ok} contrôles OK ; {ko} échec(s)')
