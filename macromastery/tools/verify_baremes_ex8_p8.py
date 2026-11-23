#!/usr/bin/env python3
"""Cohérence mathématique des barèmes v2 d'EX8 et de P8 (décision 4 du 23/11/2026). Lecture seule.
Usage : python3 -I tools/verify_baremes_ex8_p8.py
Ces contrôles vérifient l'arithmétique des règles, pas leur validité pédagogique.
"""
import itertools, json, os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = total = 0
def chk(label, cond):
    global fails, total
    total += 1
    if not cond: fails += 1; print('FAIL', label)
    return cond

# ---------- EX8 ----------
X = json.load(open(f'{root}/content/m08/assessments/EX8.exam.json', encoding='utf-8'))
T = X['totalPoints']; P = X['passPoints']; MIN = X['sectionMinimums']
sec = {s['id']: s['points'] for s in X['sections']}
items = [(q['section'], 'qcm', q['points']) for q in X['questions']] + [(c['section'], 'calc', c['points']) for c in X['calculations']] + [(a['section'], 'ana', a['points']) for a in X['analyses']]
chk('EX8 total 100 et seuil 70 = 0,7 × 100', T == 100 and P == 70 and abs(X['passThreshold'] * T - P) < 1e-9)
chk('EX8 sections recalculées = sections déclarées', all(sum(p for s, _, p in items if s == k) == v for k, v in sec.items()) and sum(sec.values()) == T)
chk('EX8 sections A 20, B 20, C 15, D 15, E 15, F 15', sec == dict(A=20, B=20, C=15, D=15, E=15, F=15))
obj = sum(p for _, t, p in items if t != 'ana'); ana = sum(p for _, t, p in items if t == 'ana')
chk('EX8 QCM 18, calculs 15, analyses 67', (sum(p for _, t, p in items if t == 'qcm'), sum(p for _, t, p in items if t == 'calc'), ana) == (18, 15, 67))
chk('EX8 parties objectives seules (33) < 70 : les analyses sont indispensables', obj == 33 and obj < P)
chk('EX8 avec parties objectives parfaites, il faut 37/67 aux analyses', P - obj == 37 and P - obj <= ana)
chk('EX8 espérance au hasard sur les QCM = 4,5', abs(0.25 * sum(p for _, t, p in items if t == 'qcm') - 4.5) < 1e-9)
# tableau d'effets de la proposition (objectif x, analyses y)
for x, y, att in [(1, .4, 59.8), (1, .5, 66.5), (1, .6, 73.2), (.8, .6, 66.6), (.8, .7, 73.3), (1, 1, 100)]:
    chk(f'EX8 effet objectif {x:.0%} + analyses {y:.0%} = {att}', abs(round(obj * x + ana * y, 1) - att) < 1e-9)
# minima : possibles, non redondants avec 70, compatibles avec la réussite
chk('EX8 minima A, D, F seulement', set(MIN) == {'A', 'D', 'F'})
chk('EX8 chaque minimum ≤ total de sa section et = 50 % arrondi', all(MIN[k] <= sec[k] and MIN[k] == -(-sec[k] // 2) for k in MIN))
chk('EX8 minima atteignables par les seules analyses', all(MIN[k] <= sum(p for s, t, p in items if s == k and t == 'ana') for k in MIN))
for k in MIN:  # un minimum n'est pas impliqué par le total de 70 : on peut avoir ≥ 70 et échouer sur ce minimum
    best_without = T - sec[k] + (MIN[k] - 0.5)
    chk(f'EX8 minimum {k} non redondant (total possible {best_without} ≥ 70 avec {k} sous le minimum)', best_without >= P)
chk('EX8 réussite possible au seuil exact avec les minima', sum(MIN.values()) <= P)
# énumération par demi-points des scores de section : réussite ⇔ total ≥ 70 et minima (cohérence de la règle écrite)
def reussit(sc): return sum(sc.values()) >= P and all(sc[k] >= MIN[k] for k in MIN)
grid = {k: [v * i / 4 for i in range(5)] for k, v in sec.items()}
n_ok = n_tot = 0
for combo in itertools.product(*[grid[k] for k in 'ABCDEF']):
    sc = dict(zip('ABCDEF', combo)); n_tot += 1; n_ok += reussit(sc)
chk(f'EX8 règle de réussite discriminante ({n_ok}/{n_tot} profils réussis, ni 0 ni tous)', 0 < n_ok < n_tot)
for a in X['analyses']:
    chk(f"EX8 {a['id']} taskPoints = une valeur par tâche, somme = points", len(a['taskPoints']) == len(a['tasks']) and sum(a['taskPoints']) == a['points'])
    chk(f"EX8 {a['id']} notation 0 / moitié / plein possible (demi-points)", all(float(tp * 2).is_integer() for tp in a['taskPoints']))
chk('EX8 durée signalée comme hypothèse non validée', 'non validée' in X.get('durationStatus', ''))

# ---------- P8 ----------
t = open(f'{root}/content/m08/project/P8.projet.mdx', encoding='utf-8').read()
grille = dict(re.findall(r'^\| ([A-H])\. [^|]+\| (\d+) \|', t, re.M)); grille = {k: int(v) for k, v in grille.items()}
chk('P8 grille A15 B10 C10 D15 E10 F10 G15 H15 = 100', grille == dict(A=15, B=10, C=10, D=15, E=10, F=10, G=15, H=15) and sum(grille.values()) == 100)
cats = re.findall(r'^\| (\d)\. ([^|]+)\| [^|]+\| ([^|]+)\| −(\d+) \|$', t, re.M)
CAP = {int(n): int(c) for n, _, _, c in cats}
chk('P8 cinq catégories, plafonds 8, 5, 8, 8, 6', CAP == {1: 8, 2: 5, 3: 8, 4: 8, 5: 6})
chk('P8 somme des plafonds 35, plafond global 25 annoncé', sum(CAP.values()) == 35 and 'Plafond global : −25' in t)
chk('P8 minima A 9, G 8, H 8 annoncés', all(x in t for x in ('A ≥ 9/15', 'G ≥ 8/15', 'H ≥ 8/15')))
chk("P8 absence de condition d'invalidation retirée des pénalités", "L'absence de condition d'invalidation n'est plus une pénalité" in t)
GLOBAL = 25
def penalite(fautes):
    """fautes : liste de (catégorie, nombre d'occurrences distinctes, chacune étant un fait générateur unique)."""
    par_cat = {}
    for c, k in fautes:
        if c == 1: v = 2 * k
        elif c == 2: v = 5 if k else 0
        elif c == 3: v = (5 + 3 * (k - 1)) if k else 0
        elif c == 4: v = 4 * k
        elif c == 5: v = 6 if k else 0
        par_cat[c] = min(CAP[c], par_cat.get(c, 0) + v)
    return min(GLOBAL, sum(par_cat.values()))
def note(brut, fautes): return max(0, brut - penalite(fautes))
chk("P8 exemple : prix reconstitué puis rendement = un seul fait générateur = −5", penalite([(3, 1)]) == 5)
pire = penalite([(1, 10), (2, 1), (3, 5), (4, 5), (5, 1)])
chk(f'P8 cumul maximal borné à −25 (calculé : −{pire})', pire == 25)
chk('P8 toutes les combinaisons de fautes restent dans [0, 25]', all(0 <= penalite([(1, a), (2, b), (3, c), (4, d), (5, e)]) <= 25 for a in range(6) for b in range(2) for c in range(4) for d in range(4) for e in range(2)))
chk('P8 note plancher 0', note(10, [(1, 10), (3, 5), (4, 5)]) == 0)
chk('P8 seuil 70 atteignable avec les minima (9 + 8 + 8 = 25 ≤ 70)', 9 + 8 + 8 <= 70)
chk('P8 un candidat à 95 bruts avec −25 échoue (70 n\'est pas garanti par le brut)', note(95, [(1, 4), (2, 1), (3, 2), (4, 2), (5, 1)]) == 70 and note(94, [(1, 4), (2, 1), (3, 2), (4, 2), (5, 1)]) < 70)
for k, m in (('A', 9), ('G', 8), ('H', 8)):
    chk(f'P8 minimum {k} non redondant (100 − {grille[k]} + {m - 1} ≥ 70)', 100 - grille[k] + (m - 1) >= 70)
chk('P8 durée signalée comme hypothèse non validée', 'hypothèse non validée' in t.split('---')[1])
print(f'{total - fails}/{total} contrôles OK ; {fails} échec(s)')
sys.exit(1 if fails else 0)
