#!/usr/bin/env python3
"""Extension de R1 (décision du 23/11/2026) à tous les quiz qui n'ont pas encore de requiredCorrect :
51 quiz des modules 0 à 4 et 7 restés à 0,8 (leçons des modules 0 à 3, L4.01 à L4.04, quiz de 10 questions) et 12 quiz du module 8.

Clés de seuil remplacées par tools/r1.py (passThreshold, requiredCorrect, passRule), insérées à la place de passThreshold ;
pour le module 8, l'ancienne passRule est remplacée par le libellé R1 commun (même nombre exigé, vérifié).
Le script refuse d'écrire si le nombre exigé change pour un quiz ou si la note affichée (« k sur n » ou « k/n ») le contredit.
Questions, options, bonnes réponses, explications, note, titre et révision ne sont pas touchés.
Usage : python3 -I tools/apply_r1_extension.py [--dry-run]
"""
import glob, importlib.util, json, math, os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('r1', f'{root}/tools/r1.py'); r1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r1)
dry = '--dry-run' in sys.argv
files = sorted(glob.glob(f'{root}/content/m*/quiz/L*.quiz.json')) + sorted(glob.glob(f'{root}/content/m*/assessments/chap_*.quiz.json'))
done = []
for p in files:
    s = open(p, encoding='utf-8').read(); d = json.loads(s)
    if 'requiredCorrect' in d:
        continue
    rel = os.path.relpath(p, root); n = len(d['questions']); new_keys = r1.seuil(n); rc = new_keys['requiredCorrect']
    assert math.ceil(d['passThreshold'] * n - 1e-9) == rc, f'{rel} : le nombre exigé changerait'
    for m in re.finditer(r'(\d+) (?:bonnes réponses )?sur (\d+)|seuil (\d+)/(\d+)', d.get('note', '')):
        k, nn = (int(m.group(1)), int(m.group(2))) if m.group(1) else (int(m.group(3)), int(m.group(4)))
        assert (k, nn) == (rc, n), f'{rel} : la note affiche {k}/{nn}, R1 donne {rc}/{n}'
    if 'passRule' in d:
        assert d['passRule'].startswith(f'{rc} bonnes réponses sur {n}'), f'{rel} : passRule incompatible'
    out = {}
    for k, v in d.items():
        if k == 'passThreshold':
            out.update(new_keys)
        elif k in ('passRule', 'requiredCorrect'):
            continue
        else:
            out[k] = v
    txt = json.dumps(out, indent=2, ensure_ascii=False) + ('\n' if s.endswith('\n') else '')
    if not dry:
        open(p, 'w', encoding='utf-8').write(txt)
    done.append(rel)
if not dry:
    open(f'{root}/backups/_revisions_decisions_2_8/LISTE_63_QUIZ_R1.txt', 'w', encoding='utf-8').write('\n'.join(done) + '\n')
print(f'{len(done)} quiz {"vérifiés (simulation, rien écrit)" if dry else "mis à jour"} selon R1')
