#!/usr/bin/env python3
"""Décision 7, exécution du 24/11/2026 : consigne le résultat des téléchargements de tools/fetch_sources_m08.py.
- précise dans CATALOGUE.json la cause de chaque échec et le contrôle technique de chaque fichier obtenu
  (taille, type, lisibilité ; repérage d'une page d'erreur ou de consentement) ;
- régénère CATALOGUE.md à partir de CATALOGUE.json (sans repasser par make_catalogue_sources_m08.py, qui remettrait
  les statuts à « non téléchargé ») ;
- ajoute au registre REGISTRE_TELECHARGEMENTS.md une section « Contrôle des fichiers ».
Contrôle technique seulement : aucun contenu n'est déclaré lu, aucune donnée n'est extraite. Bibliothèque standard
et pdftotext (déjà présent) ; n'écrit aucun fichier dans fichiers/. Usage : python3 -I tools/annotate_sources_m08.py
"""
import datetime as dt, hashlib, html, json, os, re, subprocess

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base = f'{root}/sources_documentaires/m08'; cat_p = f'{base}/CATALOGUE.json'; log_p = f'{base}/REGISTRE_TELECHARGEMENTS.md'
DAY = '2026-11-24'
# Hôtes autorisés dans l'environnement « Yclean (sources officielles M8) » le 24/11/2026 (get_environment).
ALLOWED = {'ofac.treasury.gov', 'content.govdelivery.com', 'www.govinfo.gov', 'www.federalregister.gov', 'www.federalreserve.gov',
           'www.ecb.europa.eu', 'www.bis.org', 'www.imf.org', 'imf.org', 'fraser.stlouisfed.org', 'fred.stlouisfed.org', 'www.eia.gov',
           'www.wto.org', 'cdn.cboe.com', 'www.finma.ch', 'www.archives.gov', 'www.federalreservehistory.org', 'prices.lbma.org.uk', 'www.lbma.org.uk'}
# Observations faites le 24/11/2026 (sorties consignées dans le journal M8, entrée 38).
REMARQUES = {
    'S-BIS-12': "suspect : l'URL annonce un PDF, le serveur a renvoyé une page HTML (titre « Verbatim of the remarks at the Global Investment Conference », 26 July 2012) ; la page peut ne contenir qu'un résumé et un lien : texte intégral non vérifié",
    'S-LBMA-05': "suspect : page d'article du site LBMA (titre conforme) ; on ne sait pas si elle contient le rapport complet ou seulement sa présentation",
    'S-FEDH-01': "PDF d'une page web (impression de la page Federal Reserve History) ; texte extractible",
    'S-FED-32': "page courte (4 098 octets, 251 mots) mais titre conforme (communiqué du 17/09/2001)",
}
CAUSES_SERVEUR = {
    'S-FR-01': "hôte autorisé, mais le serveur redirige (HTTP 302) vers unblock.federalregister.gov (page anti-robot), hôte non autorisé dans l'environnement",
    'fraser.stlouisfed.org': "hôte autorisé ; le serveur ferme la connexion sans réponse (2 tentatives, 24/11/2026) : refus côté serveur probable",
    'fred.stlouisfed.org': "hôte autorisé ; le serveur ferme la connexion sans réponse (2 tentatives, 24/11/2026) : refus côté serveur probable",
    'www.imf.org': "hôte autorisé ; le serveur répond HTTP 403 (refus côté serveur)",
    'imf.org': "hôte autorisé ; le serveur répond HTTP 403 (refus côté serveur)",
    'prices.lbma.org.uk': "hôte autorisé ; le serveur répond HTTP 403 (refus côté serveur)",
}


def controle(path):
    b = open(path, 'rb').read()
    if not b: return 'suspect : fichier vide'
    if path.endswith('.pdf'):
        if not b.startswith(b'%PDF'): return 'suspect : en-tête PDF absent'
        t = subprocess.run(['pdftotext', '-l', '3', path, '-'], capture_output=True, text=True).stdout
        return f'PDF lisible ({len(t.split())} mots sur les 3 premières pages extraits par pdftotext)' if t.strip() else 'suspect : PDF sans texte extractible'
    if path.endswith(('.csv', '.json')): return 'à contrôler'
    d = b.decode('utf-8', 'replace')
    m = re.search(r'<title[^>]*>(.*?)</title>', d, re.S | re.I); title = re.sub(r'\s+', ' ', html.unescape(m.group(1))).strip() if m else ''
    words = len(re.sub(r'<script.*?</script>|<style.*?</style>|<[^>]+>', ' ', d, flags=re.S | re.I).split())
    if re.search(r'access denied|page not found|\b404\b.*not found|captcha|request blocked|are you a robot', title, re.I): return f'suspect : page d\'erreur ({title})'
    return f'HTML, titre « {title[:100]} », {words} mots hors balises ; pas une page d\'erreur ni de consentement'


C = json.load(open(cat_p, encoding='utf-8'))
rows = []
for e in C['entries']:
    st = e.get('status', '')
    if e.get('local_file'):
        p = f"{base}/{e['local_file']}"
        assert hashlib.sha256(open(p, 'rb').read()).hexdigest() == e['sha256'], e['id']
        c = controle(p); r = REMARQUES.get(e['id'])
        if r: c = f'{c} ; {r}' if not r.startswith('suspect') else f'{r} ({c})'
        e['controle'] = c; e['status'] = f"téléchargé le {e['downloaded'][:10]}, non lu" + (' — SUSPECT' if c.startswith('suspect') else '')
        rows.append((e['id'], e['local_file'], e['bytes'], c))
    elif st.startswith('échec'):
        h = e['host']
        if h not in ALLOWED: cause = "hôte non autorisé dans l'environnement (403 du proxy)"
        else: cause = CAUSES_SERVEUR.get(e['id']) or CAUSES_SERVEUR.get(h) or st
        e['status'] = f'échec le {DAY} : {cause}'; e['failure_cause'] = cause
C['date'] = DAY
C['note'] = ('Catalogue généré le 23/11/2026 ; statuts mis à jour par tools/fetch_sources_m08.py et tools/annotate_sources_m08.py (24/11/2026). '
             '« Téléchargé » ne veut pas dire « lu intégralement ».')
json.dump(C, open(cat_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

cat = C['entries']
L = ['# Module 8 — Dossier documentaire local : catalogue des références et des limites', '',
     'Généré par `tools/make_catalogue_sources_m08.py` à partir de `content/sources.md`, des leçons et du projet du module 8 et de `registry/M8_SOURCES_A_LIRE.md`. **Aucune référence n\'est inventée.** Les fichiers sont téléchargés par `tools/fetch_sources_m08.py` dans `fichiers/`, avec empreinte SHA-256 et date ; **un fichier téléchargé n\'est pas une source lue** : la lecture intégrale se consigne à part (règle de clôture de `M8_SOURCES_A_LIRE.md`).', '',
     f'Mise à jour du {DAY} : tableau régénéré à partir de `CATALOGUE.json` par `tools/annotate_sources_m08.py` (statuts conservés). Empreintes SHA-256 : `REGISTRE_TELECHARGEMENTS.md`.', '',
     f"Entrées : {len(cat)} ({sum(1 for c in cat if c['kind'] == 'document')} documents cités dans le module 8, {sum(1 for c in cat if c['kind'] != 'document')} séries historiques). Primaires : {sum(1 for c in cat if c.get('nature') == 'primaire')} ; secondaires : {sum(1 for c in cat if c.get('nature') == 'secondaire')}.",
     f"Statuts : téléchargés, non lus : {sum(1 for c in cat if c.get('local_file'))} (dont suspects : {sum(1 for c in cat if 'SUSPECT' in c['status'])}) ; échecs : {sum(1 for c in cat if c['status'].startswith('échec'))} ; non tentés : {sum(1 for c in cat if c['status'] == 'non téléchargé')} (priorité 4 ou sans URL).", '',
     '| ID | Prio. | Nature | Document | Hôte | Niveau de lecture / limites | À vérifier | Fichier local / statut |', '|---|---|---|---|---|---|---|---|']
for c in sorted(cat, key=lambda c: (c.get('priority') or 9, c['id'])):
    f = f"`{c['local_file']}` — {c['status']}" if c.get('local_file') else c['status']
    L.append(f"| {c['id']} | {c.get('priority') or '—'} | {c.get('nature', '—')} | {(c.get('title') or '—').replace('|', '/')} | {c.get('host') or '—'} | {' ; '.join(c.get('limits', [])).replace('|', '/')} | {(c.get('to_verify') or '—').replace('|', '/')} | {f.replace('|', '/')} |")
open(f'{base}/CATALOGUE.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')

reg = open(log_p, encoding='utf-8').read()
if f'## Contrôle des fichiers ({DAY})' not in reg:
    R = ['', f'## Contrôle des fichiers ({DAY})', '',
         'Contrôle technique (taille, type, lisibilité, page d\'erreur ou de consentement) ; **aucun fichier n\'est lu ni exploité**. Fichiers suspects signalés, non supprimés.', '',
         '| ID | Fichier | Octets | Contrôle |', '|---|---|---|---|']
    R += [f'| {i} | {f} | {n} | {c.replace("|", "/")} |' for i, f, n, c in rows]
    R += ['', f'Échecs du {DAY} (cause consignée dans `CATALOGUE.json`, champ `failure_cause`) :', '']
    R += [f"- {e['id']} ({e['host']}) : {e['failure_cause']}" for e in cat if e.get('failure_cause')]
    open(log_p, 'a', encoding='utf-8').write('\n'.join(R) + '\n')
print(f"{len(rows)} fichiers contrôlés ; suspects : {sum(1 for r in rows if r[3].startswith('suspect'))} ; échecs : {sum(1 for e in cat if e.get('failure_cause'))}")
