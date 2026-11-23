#!/usr/bin/env python3
"""Transcrit l'inventaire initial (export Claude Docs, rev. 25) en registry/curriculum.json.
Usage: python3 -I tools/build_curriculum.py <inventaire.md> <racine_projet>
Aucune donnée n'est inventée : tout champ absent de l'inventaire vaut "à définir"."""
import re, json, sys, hashlib, datetime
src, root = sys.argv[1], sys.argv[2]
txt = open(src, encoding='utf-8').read()
TBD = "à définir"
def num(s): return float(s.strip().replace(',', '.'))
secs = re.split(r'(?m)^## ', txt)
mods = {}; m15rev = None
for s in secs:
    m = re.match(r'Module (\d+) — (.+?)\n', s)
    if m and 'révisé' not in s.split('\n')[0]:
        mods[int(m.group(1))] = s
    if s.startswith('Module 15 (révisé)'): m15rev = s
assert sorted(mods) == list(range(16)) and m15rev
def meta(s):
    d = {}
    p = re.search(r'\*\*Prérequis :\*\* (.+?)\. \*\*Niveau :\*\* (.+?)\. \*\*Durée des leçons :\*\* (.+)', s)
    d['prerequis_module_texte'], d['niveau'], d['duree_texte'] = p.group(1), p.group(2), p.group(3).strip()
    o = re.search(r'\*\*Objectif du module :\*\* (.+)', s); d['objectif_module'] = o.group(1).strip() if o else TBD
    c = re.search(r'\*\*Chapitres :\*\* (.+)', s); d['chapitres_texte'] = c.group(1).strip() if c else TBD
    e = re.search(r'\*\*Exercices et évaluations :\*\* (.+)', s); d['exercices_evaluations_initiaux'] = e.group(1).strip() if e else TBD
    r = re.search(r'\*\*Sources de référence[^*]*\*\* (.+)', s); d['familles_sources_initiales'] = r.group(1).strip() if r else TBD
    crit = re.search(r'\*\*Critères de validation propres au module :\*\*\n\n((?:- .+\n?)+)', s)
    d['criteres_validation_module'] = [x[2:].strip() for x in crit.group(1).strip().split('\n')] if crit else TBD
    return d
def chapters(txt_):
    out = []
    for part in txt_.split(' · '):
        m = re.match(r'(\d+\.\d+) (.+?) \((L\d+\.\d+)(?: à (L\d+\.\d+))?\)', part.strip())
        if m: out.append((m.group(1), m.group(2), m.group(3), m.group(4) or m.group(3)))
    return out
def mod_nums(t):
    ms = set(); 
    for a, b in re.findall(r'modules? (\d+)(?: à (\d+))?', t):
        if b: ms.update(range(int(a), int(b)+1))
        else: ms.add(int(a))
    for a in re.findall(r'(?:,| et) (\d+)', t): ms.add(int(a))
    return sorted(ms)
modules = []; lessons = []
order = {}
for n in range(16):
    s = mods[n]; d = meta(s)
    rows = re.findall(r'(?m)^\| (L\d+\.\d+) \| \*\*(.+?)\.\*\* (.+?) \| ([\d,]+) \| (\w+) \|$', s)
    if n == 15: continue
    chs = chapters(d['chapitres_texte'])
    for (lid, title, obj, h, st) in rows:
        ch = next(((c[0], c[1]) for c in chs if c[2] <= lid <= c[3]), (TBD, TBD))
        explicit = re.findall(r'préreq\. (L\d+\.\d+)', obj)
        lessons.append(dict(id=lid, module=n, chapter=ch[0], chapter_title=ch[1], title_initial=title,
            objective_initial=re.sub(r' \(préreq\. L\d+\.\d+\)', '', obj), duration_hours_initial=num(h),
            level=d['niveau'], mandatory=True, status_initial=st,
            prerequisites=dict(module_level=d['prerequis_module_texte'], lesson_level_initial=explicit,
                               lesson_level_proposed=TBD),
            objectives_detailed=TBD, key_concepts=TBD, historical_case=TBD, sources_planned=d['familles_sources_initiales'],
            archive=False))
    sumh = sum(num(r[3]) for r in rows)
    declared = num(re.search(r'([\d,]+) h', d['duree_texte']).group(1))
    modules.append(dict(module=n, title=re.match(r'Module \d+ — (.+?)\n', s).group(1), lessons=len(rows),
        hours_rows=sumh, hours_declared_initial=declared, **d,
        chapters=[dict(id=c[0], title=c[1], first=c[2], last=c[3]) for c in chs],
        modules_prerequis_parse=mod_nums(d['prerequis_module_texte'])))
# --- Module 15 révisé (remplace l'ancien) ---
d15 = meta(m15rev) if '**Durée des leçons' in m15rev else None
p = re.search(r'\*\*Prérequis :\*\* (.+?)\. \*\*Niveau :\*\* (.+)', m15rev)
rows = re.findall(r'(?m)^\| (L15\.\d+) \| (.+?) \| ([\d,]+) \| (.+?) \| (.+?) \|$', m15rev)
assert len(rows) == 12
for (lid, title, h, deps, adds) in rows:
    lessons.append(dict(id=lid, module=15, chapter=TBD, chapter_title=TBD, title_initial=title,
        objective_initial=adds, duration_hours_initial=num(h), level='C', mandatory=True, status_initial='Planifiée',
        prerequisites=dict(module_level=deps, lesson_level_initial=[], lesson_level_proposed=TBD,
                           note="liens « s'appuie sur » au niveau des modules ; numéros de leçons à ajouter quand ces modules seront rédigés"),
        objectives_detailed=TBD, key_concepts=TBD, historical_case=TBD, sources_planned="FMI ; BIS ; CFTC ; EIA ; World Gold Council ; banques centrales ; articles académiques sélectionnés et vérifiés (famille de l'ancienne version, à préciser)",
        archive=False))
obj15 = re.search(r'\*\*Objectif du module :\*\* (.+)', m15rev).group(1)
modules.append(dict(module=15, title="Spécialisation avancée — Macro avancée appliquée au Forex et à l'or (version révisée)", lessons=12,
    hours_rows=sum(num(r[2]) for r in rows), hours_declared_initial=46.0, prerequis_module_texte=p.group(1), niveau='C',
    objectif_module=obj15, chapitres_texte=TBD, chapters=[], exercices_evaluations_initiaux="examen 2 h ; projet final 12 h (note de recherche complète)",
    familles_sources_initiales=TBD, criteres_validation_module=["quiz à 80 %, examen à 75 %, aucun bloc sous 60 %, rappel à 70 %, projet final évalué sur grille, validation par l'utilisateur"],
    modules_prerequis_parse=[2,4,5,6,9,10,12], project_final_hours=12, exam_hours=2, reviews_hours=4.6))
# --- Archive de l'ancien module 15 ---
old = mods[15]
oldrows = re.findall(r'(?m)^\| (L15\.\d+) \| \*\*(.+?)\.\*\* (.+?) \| ([\d,]+) \| (\w+) \|$', old)
assert len(oldrows) == 14
archive = dict(note="Archive de l'ancienne version du module 15 (3 parcours, 14 leçons). Conservée sans suppression (décision utilisateur du 30/10/2026). Les 6 leçons obligatoires de cette version étaient L15.01, L15.02 et les 4 leçons du parcours choisi ; les 8 autres étaient facultatives. Hors parcours obligatoire actuel.",
    meta=meta(old), lessons=[dict(id_ancien=r[0], title=r[1], objective=r[2], duration_hours=num(r[3]), status=r[4],
        mandatory_in_old_version=(r[0] in ('L15.01','L15.02')) or None) for r in oldrows])
archive['hours_total_14'] = sum(l['duration_hours'] for l in archive['lessons'])
# --- totaux ---
tot_l = len(lessons); tot_h = sum(l['duration_hours_initial'] for l in lessons)
data = dict(version=1, built=str(datetime.date.today()), source=dict(document="MacroMastery Academy — Phase 2 : inventaire pédagogique (Claude Docs, révision 25)", sha256_export=hashlib.sha256(open(src,'rb').read()).hexdigest()),
    decisions=[
      dict(date="2026-10-30", id="D1", text="Module 15 révisé adopté : 12 leçons obligatoires + projet final de 12 h. 150 leçons obligatoires au total ; ~469 h de leçons ; ~562 h au total (provisoire, à recalculer)."),
      dict(date="2026-10-30", id="D2", text="Les 8 anciennes leçons facultatives du module 15 sont conservées dans l'archive pédagogique (registry/archive_m15_ancien.json), hors parcours obligatoire. Aucune trace de l'ancienne architecture n'est supprimée."),
      dict(date="2026-10-30", id="D3", text="Réorganisation L0.04 (prix, liquidité, sessions + taille de position/lots), L0.05 (taux croisés, conversions, cohérence des cotations, applications), L0.06 (or : once troy, contrats, ETF, marché physique), sous réserve de préserver les objectifs initiaux. Les notions des pilotes sont rappelées brièvement puis approfondies sous un angle différent."),
      dict(date="2026-10-30", id="D4", text="Durées détaillées par leçon retenues. Modules 1 et 2 : totaux 34 h et 35 h conservés ; les sommes annoncées dans l'inventaire (33,5 h et 35,5 h) sont consignées comme écarts historiques sans modification."),
      dict(date="2026-10-30", id="D5", text="Quiz de chapitre, examens de module, projets pratiques et grilles, corrections, critères de maîtrise, diagnostic initial + version alternative finale, projet de clôture : produits progressivement avec les modules, non reportés."),
      dict(date="2026-10-30", id="D6", text="Cas historiques et données choisis par l'auteur : sources primaires consultées avant usage, dates et références, distinction faits/interprétations/calculs/simulations, sources inaccessibles signalées, aucune référence inventée."),
      dict(date="2026-10-30", id="D7", text="Agents distincts autorisés pour les audits (vérification financière, contrôle des sources, qualité pédagogique, cohérence globale) ; ils ne remplacent pas l'audit final."),
      dict(date="2026-10-30", id="D8", text="Production module par module sans validation individuelle ; pilotes L0.01-L0.03 intacts ; contrôle intermédiaire fin M5 ; bilan concis à la fin de chaque module. Interdits : GitHub, site, publication, dépense, installation de dépendance."),
    ],
    totals=dict(lessons=tot_l, mandatory=tot_l, lesson_hours=tot_h, provisional_total_hours_user=562,
        note="Total de 562 h = leçons + 32 h examens + révisions + 2 h diagnostic + 12 h projet : provisoire, à recalculer."),
    discrepancies=[
      dict(id="E1", text="Module 1 : durée annoncée 33,5 h dans l'inventaire ; somme des 12 leçons = 34,0 h. Retenu : 34,0 h (décision D4).", declared=33.5, rows=34.0),
      dict(id="E2", text="Module 2 : durée annoncée 35,5 h ; somme des 12 leçons = 35,0 h. Retenu : 35,0 h (décision D4).", declared=35.5, rows=35.0),
      dict(id="E3", text="Totaux du résumé de l'inventaire (152 leçons, 144 obligatoires, 534 h) antérieurs à la révision du module 15 ; remplacés par 150 / 150 / ~469 h de leçons (décisions D1).", old=dict(lessons=152, mandatory=144, hours=534)),
      dict(id="E4", text="Pilotes : titres et durées réalisés différents de l'inventaire (voir pilot_deltas dans les entrées L0.01-L0.03)."),
    ],
    modules=modules, lessons=lessons)
# pilotes : fusion en lecture seule
reg = json.load(open(f'{root}/registry/lessons.json'))
for e in reg['lessons']:
    for l in lessons:
        if l['id'] == e['id']:
            l['pilot'] = True
            l['pilot_delta'] = dict(title_current=e['title'], duration_hours_current=e['duration_hours'])
# Réaffectations D3 (objectifs initiaux préservés, rattachements ajoutés)
for l in lessons:
    if l['id'] == 'L0.04': l['decision_notes'] = ["D3 : intègre la taille de position/de lot (objectif initial de L0.03 non couvert par le pilote) et les sessions de marché."]
    if l['id'] == 'L0.05': l['decision_notes'] = ["D3 : le pilote L0.03 traite déjà le calcul de base d'un taux croisé ; L0.05 le rappelle brièvement puis approfondit conversions de montants, cohérence des cotations, pouvoir d'achat et applications."]
    if l['id'] == 'L0.06': l['decision_notes'] = ["D3 : le pilote L0.03 introduit XAU/USD ; L0.06 rappelle brièvement puis approfondit once troy, spot, contrats, ETF, physique et leurs différences."]
for l in lessons:
    l.setdefault('pilot', False)
    if l['id'] == 'L1.01': pass
json.dump(data, open(f'{root}/registry/curriculum.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(archive, open(f'{root}/registry/archive_m15_ancien.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(tot_l, 'leçons', tot_h, 'h;', archive['hours_total_14'], 'h archive')
for m in modules: print(m['module'], m['lessons'], m['hours_rows'], m['hours_declared_initial'], m['modules_prerequis_parse'])
