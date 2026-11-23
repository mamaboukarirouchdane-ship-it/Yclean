#!/usr/bin/env python3
"""Contrôle de non-régression de la décision 3 (règle R1). Lecture seule. Usage : python3 -I tools/verify_thresholds_r1.py

Pour les 136 quiz (leçons et chapitres, modules 0 à 8) :
- quiz avec requiredCorrect : entier, = ⌈0,8 × n⌉, passThreshold = requiredCorrect / n, note (k sur n) et passRule cohérentes ;
- tous les quiz : pour chaque score 0..n, la réussite calculée par fraction (score/n ≥ passThreshold), par nombre exigé
  (score ≥ ⌈passThreshold × n⌉) et selon l'ancienne règle (score/n ≥ 0,8) est identique ;
- les 73 quiz modifiés : contenu identique à la sauvegarde (toutes les clés hors passThreshold, requiredCorrect, passRule),
  y compris questions, options, bonnes réponses et explications ; seuil antérieur = 0,8 ;
- les quiz non listés : octet pour octet identiques à leur état antérieur quand une sauvegarde existe, sinon absence de requiredCorrect.
"""
import json, glob, math, os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bk = os.path.join(root, 'backups', '_revisions_decisions_1_3')
listed = set(open(os.path.join(bk, 'LISTE_73_QUIZ.txt'), encoding='utf-8').read().split())
fails = total = 0
def chk(label, cond):
    global fails, total
    total += 1
    if not cond: fails += 1; print('FAIL', label)
files = sorted(glob.glob(f'{root}/content/m*/quiz/L*.quiz.json')) + sorted(glob.glob(f'{root}/content/m*/assessments/chap_*.quiz.json'))
chk('136 quiz', len(files) == 136)
SEUIL_KEYS = {'passThreshold', 'requiredCorrect', 'passRule'}
nr = 0
for f in files:
    rel = os.path.relpath(f, root); d = json.load(open(f, encoding='utf-8')); n = len(d['questions']); thr = d['passThreshold']
    need = math.ceil(thr * n - 1e-9)
    for sc in range(n + 1):
        a = sc / n >= thr - 1e-12; b = sc >= need; c = sc / n >= 0.8 - 1e-12
        chk(f'{rel} score {sc}/{n} : fraction = nombre exigé = ancienne règle', a == b == c)
    m = re.search(r'(\d+) (?:bonnes réponses )?sur (\d+)', d.get('note', ''))
    if m: chk(f'{rel} note k/n = nombre exigé', int(m.group(1)) == need and int(m.group(2)) == n)
    pct = re.search(r'[Ss]euil\D{0,12}(\d+) %', d.get('note', ''))  # seulement un pourcentage présenté comme seuil
    if pct: chk(f'{rel} pourcentage affiché ({pct.group(1)} %) cohérent : ⌈p × n⌉ = nombre exigé', math.ceil(int(pct.group(1)) / 100 * n - 1e-9) == need)
    if 'requiredCorrect' in d:
        nr += 1; rc = d['requiredCorrect']
        chk(f'{rel} requiredCorrect entier', type(rc) is int)
        chk(f'{rel} requiredCorrect = ⌈0,8 × n⌉', rc == math.ceil(0.8 * n - 1e-9))
        chk(f'{rel} passThreshold = requiredCorrect / n', abs(thr - rc / n) < 1e-12)
        chk(f'{rel} passRule = « {rc} bonnes réponses sur {n} »', d.get('passRule', '').startswith(f'{rc} bonnes réponses sur {n} '))
    if rel in listed:
        chk(f'{rel} requiredCorrect présent', 'requiredCorrect' in d)
        old = json.load(open(os.path.join(bk, 'avant', rel), encoding='utf-8'))
        chk(f'{rel} seuil antérieur 0,8', old['passThreshold'] == 0.8)
        chk(f'{rel} contenu hors seuil inchangé', {k: v for k, v in d.items() if k not in SEUIL_KEYS} == {k: v for k, v in old.items() if k not in SEUIL_KEYS})
        chk(f'{rel} questions inchangées (énoncés, options, clés, explications)', d['questions'] == old['questions'])
        chk(f'{rel} ordre des clés conservé', [k for k in d if k not in SEUIL_KEYS] == [k for k in old if k not in SEUIL_KEYS])
    else:
        chk(f'{rel} hors périmètre : pas de requiredCorrect', 'requiredCorrect' not in d)
chk('73 quiz avec requiredCorrect', nr == 73)
print(f'{total - fails}/{total} contrôles OK ; {fails} échec(s) ; {nr} quiz avec requiredCorrect sur {len(files)}')
sys.exit(1 if fails else 0)
