#!/usr/bin/env python3
"""Décision 7 (23/11/2026) : dossier documentaire local du module 8 — catalogue des références et de leurs limites.
Lit content/sources.md (tableaux des sources), les leçons et le projet du module 8 (identifiants cités) et
registry/M8_SOURCES_A_LIRE.md (priorités et points à vérifier). Écrit :
- sources_documentaires/m08/CATALOGUE.json (machine, utilisé par tools/fetch_sources_m08.py) ;
- sources_documentaires/m08/CATALOGUE.md (lecture humaine).
N'invente aucune référence : toute ligne vient de content/sources.md ou de la liste des séries ci-dessous (URL publiques gratuites,
à confirmer au téléchargement). Usage : python3 -I tools/make_catalogue_sources_m08.py
"""
import glob, json, os, re
from urllib.parse import urlparse

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = f'{root}/sources_documentaires/m08'; os.makedirs(f'{out}/fichiers', exist_ok=True)
src = open(f'{root}/content/sources.md', encoding='utf-8').read()
rows = {}
for line in src.splitlines():
    m = re.match(r'^\| (S-[A-Z]+(?:-[A-Z]+)?-\d+) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|', line)
    if m: rows[m.group(1)] = dict(id=m.group(1), nature=m.group(2).strip(), document=m.group(3).strip(), url=m.group(4).strip(), consulte=m.group(5).strip())
texts = [open(p, encoding='utf-8').read() for p in sorted(glob.glob(f'{root}/content/m08/*.mdx')) + [f'{root}/content/m08/project/P8.projet.mdx']]
cited = sorted({i for t in texts for i in re.findall(r'S-[A-Z]+(?:-[A-Z]+)?-\d+', t)})
lire = open(f'{root}/registry/M8_SOURCES_A_LIRE.md', encoding='utf-8').read()
prio, verif = {}, {}
for block, n in ((r'## Priorité 1(.*?)## Priorité 2', 1), (r'## Priorité 2(.*?)## Priorité 3', 2), (r'## Priorité 3(.*?)## Priorité 4', 3), (r'## Priorité 4(.*?)## Suivi', 4)):
    b = re.search(block, lire, re.S).group(1)
    for line in b.splitlines():
        ids = re.findall(r'S-[A-Z]+(?:-[A-Z]+)?-\d+', line)
        cells = [c.strip() for c in line.split('|')]
        for i in ids:
            prio.setdefault(i, n)
            if n <= 3 and len(cells) > 6: verif.setdefault(i, cells[-2])
def nature(r):
    t = r['nature'].lower()
    return 'primaire' if 'primaire' in t or 'officiel' in t else 'secondaire'
def niveau(r):
    t = r['nature'].lower()
    if 'métadonnées' in t: return 'métadonnées seulement'
    if 'premiers caractères' in t or 'tronqu' in t or 'premier paragraphe' in t: return 'résumé automatique tronqué'
    if 'résumé' in t: return 'résumé automatique'
    return 'non précisé dans sources.md'
cat = []
for i in cited:
    r = rows.get(i)
    if not r: cat.append(dict(id=i, kind='document', priority=prio.get(i), status='référence absente des tableaux de content/sources.md', url=None)); continue
    u = r['url'] if r['url'].startswith('http') else None
    lim = []
    if nature(r) == 'secondaire': lim.append('source secondaire : à remplacer par une source primaire ou à garder étiquetée')
    lim.append(f"niveau de lecture actuel : {niveau(r)} (aucune lecture intégrale, anomalie A33)")
    if not u: lim.append('URL absente ou non exploitable dans sources.md')
    cat.append(dict(id=i, kind='document', priority=prio.get(i, 4), nature=nature(r), source_type=r['nature'], title=r['document'], url=u,
                    host=urlparse(u).hostname if u else None, consulted=r['consulte'], to_verify=verif.get(i), limits=lim,
                    local_file=None, sha256=None, status='non téléchargé'))
# Séries historiques gratuites (priorité 3). URL publiques sans clé ; disponibilité, couverture et conditions d'usage à confirmer au téléchargement.
SERIES = [
 ('SER-FRED-DCOILBRENTEU', 'Brent, prix au comptant quotidien (EIA via FRED)', 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILBRENTEU', 'L8.01, L8.02, L8.06 (1990-91 non couvert : série Brent FRED débutant en 1987, à vérifier)'),
 ('SER-FRED-DCOILWTICO', 'WTI, prix au comptant quotidien (EIA via FRED)', 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILWTICO', 'L8.06 (1990-91, A10-A11)'),
 ('SER-FRED-DGS10', 'Rendement du Trésor américain à 10 ans, quotidien (Fed H.15 via FRED)', 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10', 'L8.05, L8.07 (mars 2023), L8.03'),
 ('SER-FRED-DFII10', 'Rendement réel du TIPS à 10 ans, quotidien (via FRED)', 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10', 'canal des taux réels (depuis 2003 : 1990, 2001 non couverts)'),
 ('SER-FRED-DTWEXBGS', 'Indice large du dollar, quotidien (Fed H.10 via FRED)', 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS', 'canal du dollar (depuis 2006 ; épisodes antérieurs non couverts)'),
 ('SER-FRED-VIXCLS', 'VIX, clôture quotidienne (Cboe via FRED)', 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS', 'L8.05, signal central (depuis 1990)'),
 ('SER-FRED-SP500', 'S&P 500, clôture quotidienne (via FRED ; historique limité par licence)', 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500', 'L8.05, signal central (FRED ne diffuse qu\'environ dix ans : épisodes anciens non couverts)'),
 ('SER-LBMA-GOLD-PM', 'LBMA Gold Price PM, quotidien', 'https://prices.lbma.org.uk/json/gold_pm.json', 'A3, A4, A5, A9, A21 (fixings de l\'après-midi ; conditions d\'utilisation LBMA à vérifier)'),
 ('SER-LBMA-GOLD-AM', 'LBMA Gold Price AM, quotidien', 'https://prices.lbma.org.uk/json/gold_am.json', 'A5 (fixings du matin ; ne pas mélanger avec le PM)'),
]
for sid, title, u, use in SERIES:
    cat.append(dict(id=sid, kind='série', priority=3, nature='primaire ou diffuseur officiel (à confirmer)', title=title, url=u, host=urlparse(u).hostname,
                    to_verify=use, limits=['série non téléchargée à ce jour ; couverture, unité, horaire et révisions à consigner au téléchargement', 'aucune valeur de cette série n\'est utilisée dans les leçons tant qu\'elle n\'a pas été lue et consignée'],
                    local_file=None, sha256=None, status='non téléchargé'))
json.dump(dict(date='2026-11-23', note='Catalogue généré ; statut mis à jour par tools/fetch_sources_m08.py. « Téléchargé » ne veut pas dire « lu intégralement ».', entries=cat),
          open(f'{out}/CATALOGUE.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
L = ['# Module 8 — Dossier documentaire local : catalogue des références et des limites', '',
     'Généré par `tools/make_catalogue_sources_m08.py` à partir de `content/sources.md`, des leçons et du projet du module 8 et de `registry/M8_SOURCES_A_LIRE.md`. **Aucune référence n\'est inventée.** Les fichiers sont téléchargés par `tools/fetch_sources_m08.py` dans `fichiers/`, avec empreinte SHA-256 et date ; **un fichier téléchargé n\'est pas une source lue** : la lecture intégrale se consigne à part (règle de clôture de `M8_SOURCES_A_LIRE.md`).', '',
     f"Entrées : {len(cat)} ({sum(1 for c in cat if c['kind'] == 'document')} documents cités dans le module 8, {len(SERIES)} séries historiques). Primaires : {sum(1 for c in cat if c.get('nature') == 'primaire')} ; secondaires : {sum(1 for c in cat if c.get('nature') == 'secondaire')}.", '',
     '| ID | Prio. | Nature | Document | Hôte | Niveau de lecture / limites | À vérifier | Fichier local |', '|---|---|---|---|---|---|---|---|']
for c in sorted(cat, key=lambda c: (c.get('priority') or 9, c['id'])):
    L.append(f"| {c['id']} | {c.get('priority') or '—'} | {c.get('nature', '—')} | {(c.get('title') or '—').replace('|', '/')} | {c.get('host') or '—'} | {' ; '.join(c.get('limits', [])).replace('|', '/')} | {(c.get('to_verify') or '—').replace('|', '/')} | {c['status']} |")
open(f'{out}/CATALOGUE.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(len(cat), 'entrées ;', sum(1 for c in cat if c.get('url')), 'avec URL ;', len({c['host'] for c in cat if c.get('host')}), 'hôtes')
