import json, glob, os, math, statistics as st, datetime as dt
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ok = 0; ko = 0
def chk(n, c):
    global ok, ko
    if c: ok += 1
    else: ko += 1; print('FAIL', n)
def near(a, b, t): return abs(a - b) <= t
K = 1e6 / 31.1034768
for p in sorted(glob.glob(f'{root}/content/m07/assessments/*.json')):
    d = json.load(open(p, encoding='utf-8')); ids = set()
    for q in d['questions']:
        chk(f'{q["id"]} unique', q['id'] not in ids); ids.add(q['id'])
        chk(f'{q["id"]} 4 options', len(q['options']) == 4)
        chk(f'{q["id"]} bonne réponse présente', q['correct'] in [o['id'] for o in q['options']])
        chk(f'{q["id"]} options distinctes', len({o['text'] for o in q['options']}) == 4)
        chk(f'{q["id"]} explication', len(q['explanation']) > 20)
    for k in d.get('calculations', []):
        chk(f'{k["id"]} numérique', isinstance(k['answer'], (int, float)) and k['tolerance'] > 0 and len(k['solution']) > 10)
d = json.load(open(f'{root}/content/m07/assessments/EX7.exam.json', encoding='utf-8')); C = {k['id']: k for k in d['calculations']}
chk('K1', near((142000 - 22000) / 600000 * 100, C['EX7-K1']['answer'], .05))
chk('K2', near(120000 * 100 / K, C['EX7-K2']['answer'], .05))
chk('K3', near((515 - 480) - 6, C['EX7-K3']['answer'], .5))
chk('K4', near((87000 - 70000) / 8500, C['EX7-K4']['answer'], .05))
chk('K5', near(250e9 / (1800 * 32150.7466), C['EX7-K5']['answer'], 1))
A = {a['id']: a for a in d['analyses']}; E1 = ' '.join(A['EX7-A1']['expectedElements']); E2 = ' '.join(A['EX7-A2']['expectedElements'])
chk('A1 net', 99000 - 135000 == -36000 and near((99000 / 135000 - 1) * 100, -26.7, .05) and '−36 000' in E1 and '−26,7' in E1)
chk('A1 part', near(135000 / 600000 * 100, 22.5, .05) and near(99000 / 560000 * 100, 17.7, .05) and '22,5' in E1 and '17,7' in E1)
chk('A1 résidu', (412 - 400) - 8 == 4 and '+4 Md$' in E1)
chk('A1 taux/prix', near((1.6 - 1.9) * 100, -30, 1e-9) and 3880 - 4000 == -120 and near((3880 / 4000 - 1) * 100, -3.0, 1e-9) and '−30 pb' in E1 and '−120 $' in E1)
chk('A2 âge', (dt.date(2026, 10, 31) - dt.date(2026, 10, 13)).days == 18 and '18 jours' in E2)
chk('A2 OI', 390000 - 520000 == -130000 and near((390000 / 520000 - 1) * 100, -25.0, 1e-9) and '−130 000' in E2 and '−25,0' in E2)
chk('A2 percentile', near(1 / 8 * 100, 12.5, 1e-9) and '12,5' in E2)
chk('total points', d['totalPoints'] == len(d['questions']) + 3 * len(d['calculations']) + sum(a['points'] for a in d['analyses']))
chk('25 QCM', len(d['questions']) == 25); chk('5 calculs', len(d['calculations']) == 5); chk('2 analyses', len(d['analyses']) == 2)
chk('seuil', abs(d['passThreshold'] * d['totalPoints'] - 42) < 1e-9 and d['totalPoints'] == 60)
# QCM numériques des chapitres et de l'examen
chk('7.1 âge', (dt.date(2026, 10, 31) - dt.date(2026, 10, 13)).days == 18)
chk('7.1 net', 142000 - 22000 == 120000); chk('7.1 t', near(111079 * 100 / K, 345.5, .05)); chk('7.1 part', near(111079 / 526276 * 100, 21.1, .05))
chk('7.2 résidu', (520 - 500) - 5 == 15); chk('7.2 oz', near(10 * 32150.7466, 321507, 1)); chk('7.2 glissante', 3 + 18 + 10 == 31)
chk('7.2 délai', (dt.date(2026, 9, 3) - dt.date(2026, 7, 31)).days == 34); chk('7.2 187', 244 - 57 == 187)
chk('7.3 dénom', near(80000 / 400000 * 100, 20.0, 1e-9) and near(76000 / 304000 * 100, 25.0, 1e-9)); chk('7.3 percentile', near(47 / 52 * 100, 90.4, .05))
chk('EX net', 150000 - 20000 == 130000); chk('EX part', near(130000 / 650000 * 100, 20.0, 1e-9)); chk('EX t', near(130000 * 100 / K, 404.3, .05))
chk('EX z', near((180 - 150) / 20, 1.5, 1e-9)); chk('EX âge', (dt.date(2026, 11, 9) - dt.date(2026, 11, 3)).days == 6)
chk('EX résidu', (560 - 600) - 10 == -50); chk('EX prix implicite', near(574e9 / (4256 * 32150.7466), 4195, 1))
chk('EX T2 délai', (dt.date(2026, 7, 30) - dt.date(2026, 6, 30)).days == 30); chk('EX bps', near((2.64 - 2.40) * 100, 24, 1e-9)); chk('EX brut', 150000 + 20000 == 170000)
chk('EX S1', near(56.5 + 288.9, 345.4, .05))
for ch in ['7.1', '7.2', '7.3']:
    c = json.load(open(f'{root}/content/m07/assessments/chap_{ch}.quiz.json', encoding='utf-8')); chk(f'chap {ch} 6 questions', len(c['questions']) == 6)
print(f'{ok} contrôles OK ; {ko} échec(s)')
