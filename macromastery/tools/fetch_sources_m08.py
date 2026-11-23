#!/usr/bin/env python3
"""Décision 7 : télécharge les sources officielles et séries gratuites du catalogue (sources_documentaires/m08/CATALOGUE.json)
dans sources_documentaires/m08/fichiers/, avec SHA-256, taille, type, statut HTTP et date. Bibliothèque standard seulement
(aucune installation) ; respecte le proxy de l'environnement (HTTPS_PROXY). N'écrase jamais un fichier : une nouvelle version
reçoit un suffixe daté. N'écrit jamais « lu » : télécharger n'est pas lire.
Usage : python3 -I tools/fetch_sources_m08.py [--priorite 3] [--ids S-IMF-04,SER-FRED-VIXCLS] [--timeout 30]
Par défaut : priorités 1 à 3 (documents officiels et séries) ; la priorité 4 (presse, sites de données) n'est pas téléchargée.
"""
import argparse, datetime as dt, hashlib, json, mimetypes, os, re, sys, urllib.error, urllib.parse, urllib.request

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base = f'{root}/sources_documentaires/m08'; cat_p = f'{base}/CATALOGUE.json'; log_p = f'{base}/REGISTRE_TELECHARGEMENTS.md'
ap = argparse.ArgumentParser(); ap.add_argument('--priorite', type=int, default=3); ap.add_argument('--ids', default=''); ap.add_argument('--timeout', type=int, default=30)
a = ap.parse_args()
C = json.load(open(cat_p, encoding='utf-8')); now = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
want = set(filter(None, a.ids.split(',')))
log = [] if os.path.exists(log_p) else ['# Registre des téléchargements — module 8', '', 'Une ligne par tentative. « Téléchargé » ne veut pas dire « lu intégralement ».', '', '| Date (UTC) | ID | URL | Résultat | Fichier | Octets | SHA-256 |', '|---|---|---|---|---|---|---|']
ok = ko = 0
for e in C['entries']:
    if not e.get('url'): continue
    if want and e['id'] not in want: continue
    if not want and (e.get('priority') or 9) > a.priorite: continue
    url = urllib.parse.quote(e['url'], safe=":/?&=#%~+,;@!$'()*[]")  # encode les espaces présents dans certaines URL de sources.md
    req = urllib.request.Request(url, headers={'User-Agent': 'MacroMastery-documentation/1.0 (usage pedagogique)'})
    try:
        with urllib.request.urlopen(req, timeout=a.timeout) as r:
            body = r.read(); ctype = r.headers.get('Content-Type', '').split(';')[0].strip(); code = r.status
        ext = {'application/pdf': '.pdf', 'text/html': '.html', 'text/csv': '.csv', 'application/json': '.json', 'text/plain': '.txt'}.get(ctype) or mimetypes.guess_extension(ctype or '') or '.bin'
        name = f"{e['id']}{ext}"; path = f'{base}/fichiers/{name}'
        if os.path.exists(path):
            if hashlib.sha256(open(path, 'rb').read()).hexdigest() == hashlib.sha256(body).hexdigest():
                res = 'déjà présent, identique'
            else:
                name = f"{e['id']}_{now[:10]}{ext}"; path = f'{base}/fichiers/{name}'; open(path, 'xb').write(body); res = f'nouvelle version (HTTP {code})'
        else:
            open(path, 'xb').write(body); res = f'téléchargé (HTTP {code}, {ctype or "type inconnu"})'
        h = hashlib.sha256(body).hexdigest()
        e.update(local_file=f'fichiers/{name}', sha256=h, bytes=len(body), content_type=ctype, downloaded=now, status='téléchargé, non lu')
        log.append(f"| {now} | {e['id']} | {e['url']} | {res} | {name} | {len(body)} | {h} |"); ok += 1
    except urllib.error.HTTPError as x:
        e.update(status=f'échec HTTP {x.code} le {now[:10]}'); log.append(f"| {now} | {e['id']} | {e['url']} | échec HTTP {x.code} | — | — | — |"); ko += 1
    except Exception as x:
        msg = re.sub(r'\s+', ' ', str(x))[:120]
        e.update(status=f'échec le {now[:10]} : {msg}'); log.append(f"| {now} | {e['id']} | {e['url']} | échec : {msg.replace('|', '/')} | — | — | — |"); ko += 1
json.dump(C, open(cat_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open(log_p, 'a', encoding='utf-8').write('\n'.join(log) + '\n')
print(f'{ok} téléchargé(s), {ko} échec(s) ; registre : {os.path.relpath(log_p, root)}')
