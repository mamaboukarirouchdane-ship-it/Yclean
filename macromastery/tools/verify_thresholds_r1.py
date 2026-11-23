#!/usr/bin/env python3
"""Contrôle de non-régression de la règle R1 (décision 3 du 31/10/2026, étendue à tous les quiz le 23/11/2026). Lecture seule.
Usage : python3 -I tools/verify_thresholds_r1.py

1. Les 136 quiz (leçons et chapitres, modules 0 à 8) : requiredCorrect entier = ⌈0,8 × n⌉, passThreshold = requiredCorrect / n,
   passRule cohérente, note affichée (« k sur n », « k/n », « p % ») cohérente ; pour chaque score 0..n, réussite identique par
   fraction, par nombre exigé et selon l'ancienne règle (score/n ≥ 0,8).
2. Contenu hors seuil inchangé par l'application de R1 : les 73 quiz du 31/10 (sauvegarde _revisions_decisions_1_3) et les
   51 quiz des modules 0 à 7 de l'extension du 23/11 (sauvegarde _revisions_decisions_2_8). Les 12 quiz du module 8 sont révisés
   par la décision 2 : leur contenu est contrôlé par tools/verify_quiz_rev3_m08.py.
3. Anti-retour : les générateurs de quiz utilisent tools/r1.py ; aucun seuil de quiz écrit en dur dans tools/ (0,8, 5/6, 7/8, 0,875).
"""
import glob, importlib.util, json, math, os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('r1', f'{root}/tools/r1.py'); r1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r1)
fails = total = 0
def chk(label, cond):
    global fails, total
    total += 1
    if not cond: fails += 1; print('FAIL', label)

def liste(path):
    p = os.path.join(root, path)
    return set(open(p, encoding='utf-8').read().split()) if os.path.exists(p) else None
lot1 = liste('backups/_revisions_decisions_1_3/LISTE_73_QUIZ.txt'); lot2 = liste('backups/_revisions_decisions_2_8/LISTE_63_QUIZ_R1.txt')
chk('liste des 73 quiz présente', lot1 is not None and len(lot1) == 73)
chk('liste des 63 quiz présente', lot2 is not None and len(lot2) == 63)
lot1 = lot1 or set(); lot2 = lot2 or set()
SEUIL_KEYS = {'passThreshold', 'requiredCorrect', 'passRule'}

# 0. le module de règle lui-même
chk('r1 : plancher 0,8', r1.PLANCHER == 0.8)
chk('r1 : 8 → 7, 6 → 5, 10 → 8', [r1.required_correct(n) for n in (8, 6, 10)] == [7, 5, 8])

files = sorted(glob.glob(f'{root}/content/m*/quiz/L*.quiz.json')) + sorted(glob.glob(f'{root}/content/m*/assessments/chap_*.quiz.json'))
chk('136 quiz', len(files) == 136)
for f in files:
    rel = os.path.relpath(f, root); d = json.load(open(f, encoding='utf-8')); n = len(d['questions']); thr = d['passThreshold']
    rc = d.get('requiredCorrect')
    chk(f'{rel} requiredCorrect présent et entier', type(rc) is int)
    if type(rc) is not int: continue
    chk(f'{rel} requiredCorrect = ⌈0,8 × n⌉', rc == r1.required_correct(n))
    chk(f'{rel} passThreshold = requiredCorrect / n', abs(thr - rc / n) < 1e-12)
    chk(f'{rel} passRule = « {rc} bonnes réponses sur {n} … »', d.get('passRule', '').startswith(f'{rc} bonnes réponses sur {n} '))
    chk(f'{rel} ordre des clés de seuil', [k for k in d if k in SEUIL_KEYS] == ['passThreshold', 'requiredCorrect', 'passRule'])
    note = d.get('note', '')
    for m in re.finditer(r'(\d+) (?:bonnes réponses )?sur (\d+)|seuil (\d+)/(\d+)', note):
        k, nn = (int(m.group(1)), int(m.group(2))) if m.group(1) else (int(m.group(3)), int(m.group(4)))
        chk(f'{rel} note {k}/{nn} = requiredCorrect/n', (k, nn) == (rc, n))
    pct = re.search(r'[Ss]euil\D{0,12}(\d+) %', note)
    if pct: chk(f'{rel} pourcentage affiché ({pct.group(1)} %) : ⌈p × n⌉ = requiredCorrect', math.ceil(int(pct.group(1)) / 100 * n - 1e-9) == rc)
    for sc in range(n + 1):
        chk(f'{rel} score {sc}/{n} : fraction = nombre exigé = ancienne règle', (sc / n >= thr - 1e-12) == (sc >= rc) == (sc / n >= 0.8 - 1e-12))
    # 2. contenu hors seuil inchangé
    for lot, bk in ((lot1, '_revisions_decisions_1_3'), (lot2, '_revisions_decisions_2_8')):
        if rel in lot and '/m08/' not in rel:
            old = json.load(open(os.path.join(root, 'backups', bk, 'avant', rel), encoding='utf-8'))
            chk(f'{rel} contenu hors seuil identique à la sauvegarde {bk}', {k: v for k, v in d.items() if k not in SEUIL_KEYS} == {k: v for k, v in old.items() if k not in SEUIL_KEYS})
chk('les deux lots couvrent les 136 quiz', lot1 | lot2 == {os.path.relpath(f, root) for f in files})

# 3. anti-retour dans les générateurs
gens = [f'{root}/tools/make_quiz.py'] + sorted(glob.glob(f'{root}/tools/make_assessment_m0*.py'))
chk('10 générateurs de quiz', len(gens) == 10)
for g in gens:
    s = open(g, encoding='utf-8').read(); name = os.path.basename(g)
    chk(f'{name} charge tools/r1.py et appelle r1.seuil', "tools/r1.py" in s and 'r1.seuil(' in s)
    for m in re.finditer(r'passThreshold\s*=\s*([^,)\n]+)', s):
        chk(f'{name} : seul le seuil en points d\'un examen est écrit en dur ({m.group(1).strip()})', m.group(1).strip() == '0.7' and 'examId=' in s[s.rfind('\n', 0, m.start()):m.start()])
HARD = re.compile(r"""passThreshold['"]?\s*[=:]\s*(0\.8\b|0\.875|5\s*/\s*6|7\s*/\s*8)""")
for p in sorted(glob.glob(f'{root}/tools/**/*.py', recursive=True)):
    b = os.path.basename(p)
    if b.startswith(('verify_', 'audit_', 'apply_')) or b == 'r1.py': continue
    for i, line in enumerate(open(p, encoding='utf-8'), 1):
        chk(f'{os.path.relpath(p, root)}:{i} seuil de quiz écrit en dur', not HARD.search(line))
print(f'{total - fails}/{total} contrôles OK ; {fails} échec(s)')
sys.exit(1 if fails else 0)
