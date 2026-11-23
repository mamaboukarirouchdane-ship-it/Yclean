#!/usr/bin/env python3
"""Contrôles automatiques des leçons de production (hors pilotes). Usage: python3 -I tools/verify_lessons.py [ID ...]
Contrôles structurels + calculs (tools/checks/<ID>.py, fonction run(chk))."""
import re, json, glob, os, sys, importlib.util
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids = sys.argv[1:] or sorted(os.path.basename(p)[:-4] for p in glob.glob(f'{root}/content/m*/L*.mdx') if os.path.basename(p)[:-4] not in ('L0.01', 'L0.02', 'L0.03'))
cur = json.load(open(f'{root}/registry/curriculum.json', encoding='utf-8'))
meta = {l['id']: l for l in cur['lessons']}
src_text = open(f'{root}/content/sources.md', encoding='utf-8').read()
known_src = set(re.findall(r'\| (S-[A-Z]+-\d+) \|', src_text))
fails = 0; total = 0
def chk(label, cond, detail=''):
    global fails, total
    total += 1
    if not cond: fails += 1; print('FAIL', label, detail)
def calc(label, got, exp, tol=0.005):
    chk(f'calcul {label}', abs(float(got) - float(exp)) <= tol, f'obtenu {got} attendu {exp}')
SECT = ['Objectifs d\'apprentissage', 'Prérequis', 'Explication intuitive', 'Développement technique', 'Définitions essentielles', 'Exemples chiffrés', 'Application au Forex et à l\'or', 'Erreurs courantes', 'Limites de l\'interprétation', 'Exercices pratiques', 'Quiz', 'Résumé', 'Critères de maîtrise', 'Sources et références']
for lid in ids:
    m = int(lid[1:].split('.')[0]); mp = glob.glob(f'{root}/content/m{m:02d}/{lid}.mdx')
    chk(f'{lid} fichier présent', bool(mp))
    if not mp: continue
    t = open(mp[0], encoding='utf-8').read()
    fm = re.match(r'---\n(.*?)\n---\n', t, re.S); chk(f'{lid} frontmatter', bool(fm))
    chk(f'{lid} id frontmatter', f'id: {lid}' in t[:400])
    for i, s in enumerate(SECT, 1):
        chk(f'{lid} section {i} {s}', re.search(rf'(?m)^## {i}\. {re.escape(s)}', t) is not None)
    ex = re.findall(r'(?m)^\*\*Exercice (\d+)', t); det = len(re.findall(r'<details>', t)); cl = len(re.findall(r'</details>', t))
    chk(f'{lid} ≥ 3 exercices', len(ex) >= 3, str(len(ex))); chk(f'{lid} exercices = corrections', len(ex) == det == cl, f'{len(ex)}/{det}/{cl}')
    chk(f'{lid} cas historique/documenté', bool(re.search(r'[Cc]as historique', t)) or lid in ())
    chk(f'{lid} mention d\'une SIMULATION ou aucun chiffre fictif', 'SIMULATION' in t or 'fictif' not in t)
    chk(f'{lid} limite : pas de garantie de gain', bool(re.search(r'ne garantit pas|garantit pas', t)))
    used = set(re.findall(r'S-[A-Z]+-\d+', t)); chk(f'{lid} sources toutes listées', used <= known_src, str(used - known_src))
    chk(f'{lid} pas de marqueur d\'inachevé', not re.search(r'TODO|XXX|à compléter|lorem', t, re.I))
    qp = glob.glob(f'{root}/content/m{m:02d}/quiz/{lid}.quiz.json'); chk(f'{lid} quiz présent', bool(qp))
    if qp:
        q = json.load(open(qp[0], encoding='utf-8'))
        chk(f'{lid} quiz lessonId', q['lessonId'] == lid); chk(f'{lid} quiz seuil 0,8', q['passThreshold'] == 0.8)
        seen = set()
        for x in q['questions']:
            oids = [o['id'] for o in x['options']]
            chk(f'{x["id"]} id unique', x['id'] not in seen); seen.add(x['id'])
            chk(f'{x["id"]} 4 options', len(oids) == 4); chk(f'{x["id"]} correct ∈ options', x['correct'] in oids)
            chk(f'{x["id"]} explication', len(x['explanation']) > 40)
            chk(f'{x["id"]} options distinctes', len({o['text'] for o in x['options']}) == len(oids))
        chk(f'{lid} répartition des bonnes réponses', len({x['correct'] for x in q['questions']}) >= 3)
    cp = f'{root}/tools/checks/{lid}.py'
    if os.path.exists(cp):
        spec = importlib.util.spec_from_file_location('c', cp); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c); c.run(calc)
    else: chk(f'{lid} contrôles de calcul présents', False, 'tools/checks manquant')
print(f'{total - fails}/{total} contrôles OK ; {fails} échec(s) sur {len(ids)} leçon(s)')
sys.exit(1 if fails else 0)
