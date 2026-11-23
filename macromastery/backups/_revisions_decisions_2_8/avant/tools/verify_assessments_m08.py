#!/usr/bin/env python3
"""Vérifie les évaluations de chapitre du module 8. Usage: python3 -I tools/verify_assessments_m08.py"""
import json, os, datetime as dt
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ok = bad = 0
def chk(n, c):
    global ok, bad
    if c: ok += 1
    else: bad += 1; print('FAIL', n)
for ch in ('8.1', '8.2', '8.3', '8.4'):
    d = json.load(open(f'{root}/content/m08/assessments/chap_{ch}.quiz.json', encoding='utf-8'))
    qs = d['questions']
    chk(ch + ' 6 questions', len(qs) == 6); chk(ch + ' seuil 5/6', abs(d['passThreshold'] - 5 / 6) < 1e-9)
    for q in qs:
        chk(q['id'] + ' 4 options', len(q['options']) == 4); chk(q['id'] + ' une bonne', sum(o['id'] == q['correct'] for o in q['options']) == 1)
        chk(q['id'] + ' explication', len(q['explanation']) > 60)
import math
chk('8.3 synthèse ex1', abs(22/16-1-0.375)<1e-12 and (dt.date(2025,5,5)+dt.timedelta(90))==dt.date(2025,8,3) and abs(103/100-1-0.03)<1e-12 and abs(98/100-1+0.02)<1e-12)
chk('8.1 calc', abs(1910/1.06-1802)<1 and abs(0.05*40-2.0)<1e-12 and abs(0.4*5-2.0)<1e-12)
chk('8.4 calc', abs(759/827-1+0.0822)<1e-4 and abs(0.5*2+0.3*-1+0.2*-3-0.1)<1e-9 and abs(0.4*2+0.3*-1+0.3*-3+0.4)<1e-9 and (40-30)==10)
chk('8.3 score', 4 - 1 == 3)
chk('8.3 T0+90', (dt.date(2001, 9, 11) + dt.timedelta(90)) == dt.date(2001, 12, 10)); chk('8.3 jour 66', (dt.date(2001, 11, 16) - dt.date(2001, 9, 11)).days == 66)
chk('8.3 or', abs(2069 / 1910 - 1 - 0.0832) < 1e-4); chk('8.3 jour 12', (dt.date(2022, 3, 8) - dt.date(2022, 2, 24)).days == 12)
chk('calc jours', (dt.date(2022, 3, 26) - dt.date(2022, 2, 24)).days == 30)
chk('calc espérance', abs(0.4 * 1950 + 0.6 * 2050 - 2010) < 1e-9)
chk('calc surprise', abs((1950 / 2010 - 1) + 0.0299) < 1e-4)
chk('calc taux effectif', abs(0.25 * 0.4 - 0.10) < 1e-12)
chk('calc AM-AM', abs((3454.70 / 3002.70 - 1) - 0.1505) < 1e-4)
chk('synthèse ex1', abs(0.30 * 0.50 - 0.15) < 1e-12 and abs(2040 / 2000 - 1 - 0.02) < 1e-12)
chk('synthèse ex2', abs(3100 / 2500 - 1 - 0.24) < 1e-12 and abs(3010 / 2500 - 1 - 0.204) < 1e-12)
t = open(f'{root}/content/m08/chap_8.2.synthese.mdx', encoding='utf-8').read() + open(f'{root}/content/m08/chap_8.3.synthese.mdx', encoding='utf-8').read() + open(f'{root}/content/m08/chap_8.4.synthese.mdx', encoding='utf-8').read()
chk('ne garantit pas', 'ne garantit pas' in t); chk('SIMULATION', 'SIMULATION' in t)
chk('exercices = details', t.count('**Exercice') == t.count('<details>') == t.count('</details>'))

# --- Examen final EX8 ---
import math
X = json.load(open(f'{root}/content/m08/assessments/EX8.exam.json', encoding='utf-8'))
chk('EX8 total 100', X['totalPoints'] == 100 and X['passPoints'] == 70)
chk('EX8 sections', {k['id']: k['points'] for k in X['sections']} == dict(A=20, B=20, C=15, D=15, E=15, F=15))
chk('EX8 effectifs', len(X['questions']) == 18 and len(X['calculations']) == 5 and len(X['analyses']) == 6)
KK = {k['id']: k for k in X['calculations']}
chk('EX8 K1', abs(0.30 * 0.35 * 100 - KK['EX8-K1']['answer']) < 0.05)
chk('EX8 K2', abs(2100 / 0.96 - KK['EX8-K2']['answer']) < 0.5)
chk('EX8 K3', abs(30 * math.sqrt(30 / 365) - KK['EX8-K3']['answer']) < 0.05)
t0 = dt.date(2027, 3, 14); fin = t0 + dt.timedelta(days=90)
chk('EX8 K4', (fin - dt.date(2027, 5, 19)).days == KK['EX8-K4']['answer'] == 24 and fin == dt.date(2027, 6, 12))
chk('EX8 K5', abs((10 / 0.6 - 10) - KK['EX8-K5']['answer']) < 0.05)
chk('EX8 A3 score', abs(22.4 / 20 - 1 - 0.12) < 1e-9 and (1 + 1 + 0 + 1 + 1 - 1) == 3)
chk('EX8 A4 dates', [(t0 + dt.timedelta(days=n)).strftime('%d/%m') for n in (7, 30, 90)] == ['21/03', '13/04', '12/06'] and [(dt.date(2027, *md) - t0).days for md in ((3, 15), (3, 26), (4, 18), (5, 19))] == [1, 12, 35, 66])
chk('EX8 A5 banque', abs(10 / 0.85 - 11.76) < .01 and abs(10 / 0.85 - 10 - 1.76) < .01 and abs(10 - (10 / 0.85 - 10) - 8.24) < .01 and abs(10 - (10 / 0.6 - 10) - 3.33) < .01)
chk('EX8 A6 espérance', abs(0.4 * 3 - 0.4 * 1 - 0.2 * 4) < 1e-12 and abs(0.3 * 3 - 0.4 * 1 - 0.3 * 4 + 0.7) < 1e-12)
chk('EX8 SIMULATION', all('SIMULATION' in a['title'] for a in X['analyses'])) and 'ne garantit pas' in X['note']
chk('EX8 analyses points', sum(a['points'] for a in X['analyses']) == 49)
chk('EX8 réponses uniques', all(sum(1 for o in q['options'] if o['id'] == q['correct']) == 1 for q in X['questions']))
chk('seuils de chapitre = 5/6', all(abs(json.load(open(f'{root}/content/m08/assessments/chap_{c}.quiz.json', encoding='utf-8'))['passThreshold'] - 5 / 6) < 1e-9 for c in ('8.1', '8.2', '8.3', '8.4')))
chk('seuils de leçon = 7/8', all(abs(json.load(open(f'{root}/content/m08/quiz/L8.0{i}.quiz.json', encoding='utf-8'))['passThreshold'] - 7 / 8) < 1e-9 for i in range(1, 9)))
print(f'{ok}/{ok+bad} contrôles OK ; {bad} échec(s)')
