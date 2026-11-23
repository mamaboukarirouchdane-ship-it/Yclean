# Journal de production — MacroMastery Academy

Chaque entrée : date, action, fichiers, sauvegarde, contrôles. Le journal est additif (jamais réécrit).

## 2026-10-30 — Étape 1 : registre des 150 leçons
- Autorisation : message « VALIDATION DE L'ARCHITECTURE ET AUTORISATION DE PRODUCTION » (30/10/2026).
- Sauvegarde : `backups/2026-10-30_avant-etape1-registre-150/` (MANIFEST.sha256).
- Créés (aucun fichier existant modifié) : `registry/curriculum.json` (150 leçons, 16 modules, décisions D1–D8, écarts E1–E4), `registry/archive_m15_ancien.json` (14 leçons de l'ancien module 15, conservées), `tools/build_curriculum.py`, `tools/status.py`, ce journal.
- Source de la transcription : export de l'inventaire (Claude Docs, révision 25) ; empreinte SHA-256 dans `curriculum.json`.
- Champs absents de l'inventaire : « à définir » (objectifs détaillés, concepts clés, cas historiques, prérequis de leçon proposés).

## 2026-10-30 — L0.04 rédigée
- Fichiers créés : `content/m00/L0.04.mdx`, `content/m00/quiz/L0.04.quiz.json`, `tools/checks/L0.04.py`, `tools/quizsrc/L0.04.py`, `tools/verify_lessons.py`, `tools/make_quiz.py`, `tools/register.py`.
- Fichiers modifiés (ajouts seulement) : `content/sources.md` (nouvelle section « Module 0, suite »), `registry/lessons.json` (nouvelle entrée L0.04 ; entrées pilotes inchangées, vérifié par comparaison avec la sauvegarde).
- Contrôles : `verify_lessons.py L0.04` 125/125 ; `verify_m00.py` inchangé (OK) ; fichiers pilotes `.mdx` / `.quiz.json` : empreintes SHA-256 identiques à la sauvegarde.
- Sources lues par résumé automatique (voir `sources.md` et `open_points`).

## 2026-10-30 — L0.05 rédigée
- Créés : `content/m00/L0.05.mdx`, `content/m00/quiz/L0.05.quiz.json`, `tools/checks/L0.05.py`, `tools/quizsrc/L0.05.py`. Modifiés (ajouts) : `content/sources.md`, `registry/lessons.json` (entrée L0.05).
- Contrôles : `verify_lessons.py L0.04 L0.05` 244/244. Corrections faites avant livraison : arrondis (GBP/USD implicite 1,3288 ; XOF/USD réel 589,20) et deux placeholders de correction remplacés par des valeurs calculées.
- Particularité : cas réel BCE (28/10/2026) et parité XOF/EUR (BCEAO, Trésor) ; dates de taux non alignées signalées dans la leçon (yen au 26/10).

## 2026-10-30 — L0.06 rédigée
- Créés : `content/m00/L0.06.mdx`, quiz, `tools/checks/L0.06.py`, `tools/quizsrc/L0.06.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py L0.04–L0.06` OK. Corrections avant livraison : coquilles (« tu parie », « le taille »), deux placeholders numériques remplacés, ETF 3 ans (0,09880 et non 0,09881), XOF/g (97 637), en-tête « cas historique ».

## 2026-10-30 — L0.07 rédigée
- Créés : `L0.07.mdx`, quiz, `tools/checks/L0.07.py`, `tools/quizsrc/L0.07.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 130/130 sur L0.07. Corrections avant livraison : VA arrondies (889,00 ; 1 017,01), taux EE 3,526 %.
- Sources tentées et non lues consignées (Investor.gov, TreasuryDirect, taux directeurs BCE).

## 2026-10-30 — L0.08 rédigée
- Créés : `L0.08.mdx`, quiz, `tools/checks/L0.08.py`, `tools/quizsrc/L0.08.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 122/122 sur L0.08. Cas réel : courbe du Trésor américain du 30/06/2026 (table tronquée, dates postérieures non lues) ; exemples chiffrés de la SEC retrouvés par calcul. Correction avant livraison : VA de l'année 5 = 814,87.

## 2026-10-30 — L0.09 rédigée
- Créés : `L0.09.mdx`, quiz, `tools/checks/L0.09.py`, `tools/quizsrc/L0.09.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 99/99 sur L0.09. Aucune source officielle pour les conventions de graphique : annoncé comme définitions de cours. Cas réel : taux de référence BCE 27-29/10/2026 (rendements simple/log recalculés).

## 2026-10-30 — L0.10 rédigée
- Créés : `L0.10.mdx`, quiz, `tools/checks/L0.10.py`, `tools/quizsrc/L0.10.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 102/102 sur L0.10. Cas historique : abandon du plancher EUR/CHF (BNS, 15/01/2015) sans prix, faute de source lue.

## 2026-10-30 — Compléments du module 0
- Créés : 5 quiz de chapitre (6 QCM chacun, seuil 5/6), examen EX0 (25 QCM + 5 calculs, 40 points, seuil 28), mini-projet P0 avec grille de 40 points, `registry/assessments.json`, `tools/assessments/m00.py`, `tools/make_assessment_m00.py`, `tools/verify_assessments_m00.py`.
- Contrôles : 286 contrôles de structure et recalcul des 5 calculs de l'examen.
- Non fait : diagnostic initial (62 QCM + 2 questions ouvertes) et version finale alternative, prévus de façon progressive.
- Sauvegarde : `backups/*_fin_module0` avec MANIFEST.sha256. Pilotes L0.01 à L0.03 inchangés (voir vérification SHA-256).
- Constat : `verify_m00.py` (script des pilotes, non modifié) exige les champs `previous_validations` et `awaiting` pour toutes les entrées du registre ; il signale donc à tort L0.04–L0.10 (nouvelles leçons, sans validation antérieure). Exécuté avec une portée limitée à L0.01–L0.03 (copie hors projet), le script donne RÉSULTAT GLOBAL : OK. Les leçons L0.04–L0.10 sont contrôlées par `verify_lessons.py` (810/810) et leurs `checks/`.
- Correction de terminologie (L0.06) : les mentions non qualifiées de « contrat à terme » ont été remplacées par « future » (ou « contrat à terme standardisé » déjà présent), conformément au vocabulaire forward/future validé en phase 2. Fichiers : `L0.06.mdx`, quiz L0.06 (titre et une option), `tools/quizsrc/L0.06.py`. Ancienne version conservée dans la sauvegarde `backups/20261030_1042_fin_module0`.

## 2026-10-30 — L1.01 rédigée (module 1)
- Créés : `content/m01/L1.01.mdx`, quiz, `tools/checks/L1.01.py`, `tools/quizsrc/L1.01.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 97/97. Données réelles : communiqué BEA du 30/09/2026 (T2 2026 : 1,5 % → 2,2 %), lu par résumé automatique ; lacunes signalées dans la leçon.

## 2026-10-30 — L1.02 rédigée
- Créés : `L1.02.mdx`, quiz, `checks/L1.02.py`, `quizsrc/L1.02.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 84/84. Découverte : l'exemple chiffré du billet de la Fed de Saint-Louis (écart −0,07 %) est incohérent avec ses propres données (−0,747 %) ; signalé dans la leçon et dans les points ouverts.

## 2026-10-30 — L1.03 rédigée
- Créés : `L1.03.mdx`, quiz, `checks/L1.03.py`, `quizsrc/L1.03.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 95/95. Données réelles : BLS Productivity and Costs T2 2026 révisé (cohérence interne recalculée) ; tableau historique de la CBO (sommes recalculées).

## 2026-10-30 — L1.04 rédigée
- Créés : `L1.04.mdx`, quiz, `checks/L1.04.py`, `quizsrc/L1.04.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 96/96. Données réelles : CPI sept. 2026, PCE août 2026 ; écart PCE/CPI sous-jacent signalé sans explication.

## 2026-10-30 — L1.05 rédigée
- Créés : `L1.05.mdx`, quiz, `checks/L1.05.py`, `quizsrc/L1.05.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 95/95. Données réelles : enquête NY Fed sept. 2026 ; décomposition SF Fed 2022 (parts recalculées).

## 2026-10-30 — L1.06 rédigée
- Créés : `L1.06.mdx`, quiz, `checks/L1.06.py`, `quizsrc/L1.06.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 99/99. Cas : Japon 1998–2013 (BoJ 2014) et Grande Inflation 1965–1982 (Federal Reserve History).

## 2026-10-30 — L1.07 rédigée
- Créés : `L1.07.mdx`, quiz, `checks/L1.07.py`, `quizsrc/L1.07.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 100/100. Données réelles : emploi de sept. 2026 (identité emploi/population vérifiée) ; emploi d'équilibre (page de données FEDS, texte non lu).

## 2026-10-30 — L1.08 rédigée
- Créés : `L1.08.mdx`, quiz, `checks/L1.08.py`, `quizsrc/L1.08.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 90/90. Source : Lettre FRBSF 2019-05 ; diagnostic 2026 signalé comme hypothèse.

## 2026-10-30 — L1.09 rédigée
- Créés : `L1.09.mdx`, quiz, `checks/L1.09.py`, `quizsrc/L1.09.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 102/102. Sources : Census (sept. 2026), Freddie Mac (29/10/2026), lues par résumé ; lien taux/chantiers signalé comme compatibilité, non causalité.

## 2026-10-30 — L1.10 rédigée
- Créés : `L1.10.mdx`, quiz, `checks/L1.10.py`, `quizsrc/L1.10.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 98/98. Sources : BEA commerce août 2026, BEA balance des paiements T2 2026, NBER 21813 (Plaza), lues par résumé ; écart compte financier/balance courante signalé comme non interprété.

## 2026-10-30 — L1.11 rédigée
- Créés : `L1.11.mdx`, quiz, `checks/L1.11.py`, `quizsrc/L1.11.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 93/93. Sources : CBO MBR exercice 2026 (primaire), CRFB (secondaire), CNBC 2022 (presse) ; limites signalées (cas UK sur presse seule).

## 2026-10-30 — L1.12 rédigée
- Créés : `L1.12.mdx`, quiz, `checks/L1.12.py`, `quizsrc/L1.12.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 80/80. Leçon de synthèse sans donnée nouvelle ; bloc politique monétaire explicitement absent.

## 2026-10-30 — Module 1 : compléments d'évaluation
- Créés : `tools/assessments/m01.py`, `make_assessment_m01.py`, `verify_assessments_m01.py` ; `content/m01/assessments/` (5 quiz de chapitre de 6 QCM, examen EX1 : 25 QCM + 5 calculs, 40 points, seuil 28) ; `content/m01/project/P1.projet.mdx` (grille 40 points) ; `registry/assessments.json` (entrée m01).
- Contrôles : `verify_assessments_m01.py` 286/286. Aucun fichier existant modifié.

## 2026-10-30 — L2.01 rédigée (module 2 commencé)
- Créés : `content/m02/L2.01.mdx`, quiz, `checks/L2.01.py`, `quizsrc/L2.01.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 81/81. Sources : Fed (section 2A, déclaration d'objectifs, FOMC), Parlement européen, BCE, BCEAO (page + statuts 2010), Federal Reserve History (accord de 1951) ; points non vérifiés signalés. Données du rapport de la Fed de juillet 2026 (fourchette 3½–3¾ %) consignées dans sources.md pour L2.03.

## 2026-10-30 — L2.02 rédigée
- Créés : `L2.02.mdx`, quiz, `checks/L2.02.py`, `quizsrc/L2.02.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 85/85. Sources : Banque d'Angleterre 2014 (texte complet par résumé), Fed (réserves obligatoires, H.6 juin 2026). Exemples de bilans fictifs (SIMULATION).

## 2026-10-30 — L2.03 rédigée
- Créés : `L2.03.mdx`, quiz, `checks/L2.03.py`, `quizsrc/L2.03.py` ; ajouts : `content/sources.md` (section de notes de collecte remplacée par la section L2.03), `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 91/91. Sources : Fed (16/09 et 28/10/2026, note d'application), BCE (taux, transmission, mise en œuvre), Federal Reserve History (Volcker). Décision BCE d'octobre signalée comme non vérifiée.

## 2026-10-30 — L2.04 rédigée
- Créés : `L2.04.mdx`, quiz, `checks/L2.04.py`, `quizsrc/L2.04.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 87/87. Sources : H.4.1 du 22/10/2026, rapport de bilan de mai 2026, Fed de New York (LSAP). Point de vigilance corrigé : le poste de pensions inversées du H.4.1 n'est pas assimilé à la facilité ON RRP.

## 2026-10-30 — L2.05 rédigée ; L2.04 révisée (révision 2)
- Créés : `L2.05.mdx`, quiz, `checks/L2.05.py`, `quizsrc/L2.05.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 81/81 (L2.05) ; L2.04 revérifiée.
- **Correction de L2.04** : les minutes de septembre 2026 indiquent que les achats de gestion des réserves sont suspendus (réinvestissement du principal des titres d'agences en bons du Trésor) ; la leçon, son résumé, ses limites et sa liste de sources ont été mis à jour. Le contenu précédent a été conservé.

## 2026-10-30 — L2.06 rédigée
- Créés : `L2.06.mdx`, quiz, `checks/L2.06.py`, `quizsrc/L2.06.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 100/100. Sources : Fed (rapport de juillet 2026, encadré 4), Fed de New York (r-star), Bernanke 2010. Prescriptions de règles présentées comme **illustratives** (entrées de l'auteur), avec tableau de sensibilité.

## 2026-10-30 — L2.07 rédigée
- Créés : `L2.07.mdx`, quiz, `checks/L2.07.py`, `quizsrc/L2.07.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 83/83. Source nouvelle : discours de Powell à Jackson Hole (26/08/2022) via la BRI. Fourchette d'avant juin 2022 déduite (calcul de l'auteur). Seuils de décision non publiés : signalés comme tels.

## 2026-10-30 — L2.08 rédigée
- Créés : `L2.08.mdx`, quiz, `checks/L2.08.py`, `quizsrc/L2.08.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 84/84. Sources : pages Fed (FOMC, structure, section 10, Conseil), Federal Reserve History, Fed de Saint-Louis ; chiffres 2026 de l'actif différé tirés d'une **source secondaire** (First Trust), signalés comme à recouper.

## 2026-10-30 — L2.09 rédigée
- Créés : `L2.09.mdx`, quiz, `checks/L2.09.py`, `quizsrc/L2.09.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 86/86. Sources : pages BCE (Conseil, rotation, stratégie) ; décision de juin 2026 via la Banque d'Espagne. Le nombre de pays en 2015 n'est pas affirmé (non lu).

## 2026-10-30 — L2.10 rédigée
- Créés : `L2.10.mdx`, quiz, `checks/L2.10.py`, `quizsrc/L2.10.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 88/88. Sources primaires : BoJ (cadre, communiqué du 31/07/2026), BNS (résumé de discussion). **Sources secondaires signalées** : BoE de septembre (MTS, ForexCracked) et BoJ de septembre (Securities.io, fiabilité limitée) — à recouper. Autres banques centrales non traitées (signalé).

## 2026-10-30 — L2.11 rédigée
- Créés : `L2.11.mdx`, quiz, `checks/L2.11.py`, `quizsrc/L2.11.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 76/76. Communiqués Fed de septembre et octobre 2026 relus (résumés) ; conférence de presse via deux sources secondaires (signalées). Affirmation ambiguë sur le calendrier des réunions non retenue.

## 2026-10-30 — L2.12 rédigée (fin des leçons du module 2)
- Créés : `L2.12.mdx`, quiz, `checks/L2.12.py`, `quizsrc/L2.12.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 91/91 (un prix implicite recalculé 1 235,6 au lieu de 1 235,5). Sources majoritairement secondaires (WGC relayé, opinion, CNBC 2013) ; rendements du Trésor en cache jusqu'au 30/06/2026 : signalé.

## 2026-10-30 — Compléments du module 2
- Créés : `tools/assessments/m02.py`, `tools/make_assessment_m02.py`, `tools/verify_assessments_m02.py`, `content/m02/assessments/` (5 quiz de chapitre de 6 questions, EX2 : 25 QCM + 5 calculs, 40 points, seuil 28), `content/m02/project/P2.projet.mdx` (grille 40 points) ; entrée `m02` dans `registry/assessments.json`.
- Contrôles : `verify_assessments_m02.py` 293/293 (une explication trop courte corrigée). Recalcul indépendant des 5 calculs.
- Statuts : non intégré, non testé, non validé ; diagnostics initial et final alternatif non écrits.

## 2026-10-30 — L3.01 rédigée (module 3)
- Créés : `L3.01.mdx`, quiz, `checks/L3.01.py`, `quizsrc/L3.01.py` ; ajouts : `content/sources.md`, `registry/lessons.json`.
- Contrôles : `verify_lessons.py` 86/86. Sources : calendriers BLS (oct.–déc.), BEA, directive n° 3, calendrier IPCH de la BCE, pages BLS sur l'arrêt de financement de 2025. Limites signalées (date de modification BEA incohérente, réunion de décembre de la Fed en source secondaire, arrêt de 2026 non étudié).

## 2026-10-30 — Reprise (consigne du 15:55)
- État confirmé : 35 leçons rédigées (3 pilotes + 32 vérifiées, 3 058 contrôles OK), évaluations m00–m02, sauvegardes présentes. Ajout de `tools/consolidate.py` : registre des points à vérifier et empreintes SHA-256.

## 2026-10-30 — L3.02 rédigée
- Créés : `L3.02.mdx`, quiz, `checks/L3.02.py`, `quizsrc/L3.02.py` ; ajouts : sources.md, lessons.json. Contrôles 81/81. Consensus FactSet (secondaire), BLS lu par résumé.

## 2026-10-30 — L3.03 rédigée
- Créés : `L3.03.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 91/91. Séries fictives signalées ; papier NBER lu par résumé.

## 2026-10-30 — L3.04 rédigée
- Créés : `L3.04.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 85/85 (unité de calcul corrigée : 0,05 $). Sources BLS primaires (résumés) + First Trust secondaire.

## 2026-10-30 — L3.05 rédigée
- Créés : `L3.05.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 84/84. Anomalie du résumé (assureurs −90 000) écartée et signalée.

## 2026-10-30 — L3.06 rédigée
- Créés : `L3.06.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 90/90. CPI sept. 2026 (BLS, résumé) ; consensus et marché en sources secondaires ; décomposition en SIMULATION.

## 2026-10-30 — L3.07 rédigée
- Créés : `L3.07.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 84/84. PCE sept. 2026 (BEA, primaire, résumé) ; PPI en sources secondaires ; écart cœur PCE/CPI signalé comme cause non vérifiée.

## 2026-10-30 — L3.08 rédigée
- Créés : `L3.08.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 84/84. ISM services (PDF officiel) ; ISM manufacturier via copie du communiqué ; contradiction PNC écartée ; PMI zone euro en source secondaire.

## 2026-10-30 — L3.09 rédigée
- Créés : `L3.09.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 83/83. Sources primaires (BEA T3 avancé et T2 troisième, Census, Fed G.17) lues par résumé ; révision T2 1,5 → 2,2 %.

## 2026-10-30 — L3.10 rédigée
- Créés : `L3.10.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 86/86. Eurostat (IPCH via copie, chômage, PIB T2 flash) ; PIB T2 révisé en secondaire ; T3 non disponible.

## 2026-10-30 — L3.11 rédigée
- Créés : `L3.11.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 89/89. Cas du 02/10/2026 reconstitué avec sources secondaires/tertiaires ; incohérences d'horaires et d'instruments signalées, aucune conclusion causale.

## 2026-10-30 — L3.12 rédigée (module 3 : 12/12 leçons)
- Créés : `L3.12.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 82/82 (marqueur « à compléter » reformulé). Grille de douze rubriques, trois cas remplis.

## 2026-10-30 — Module 3 terminé (évaluations)
- Créés : `tools/assessments/m03.py`, `make_assessment_m03.py`, `verify_assessments_m03.py` ; 6 quiz de chapitre (3.1–3.6), examen EX3 (25 QCM + 5 calculs + 2 publications fictives, 60 points, seuil 42), projet P3 (grille 40 points) ; entrée `m03` dans `registry/assessments.json`.
- Contrôles : 334 contrôles d'évaluation OK ; leçons vérifiées par script. Sauvegarde `backups/20261030_1618_fin_module3`. `consolidate.py` relancé.

## 2026-10-30 — L4.01 rédigée (module 4)
- Créés : `L4.01.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 88/88. BRI 2016 (basis) et Chinn et autres 2022 (Fama) lus par résumé ; cours à terme calculé avec taux directeurs comme substituts (signalé). Anomalie signalée : identifiant S-BIS-01 en double dans sources.md (non corrigée, pour ne rien réécrire).

## 2026-10-30 — L4.02 rédigée
- Créés : `L4.02.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 89/89. Anticipations en sources secondaires ; cas 25/09–29/10/2026 présenté sans causalité.

## 2026-10-30 — L4.03 rédigée
- Créés : `L4.03.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 91/91. TIPS et points morts en sources secondaires ; incohérence de 30 pb sur le rendement nominal à 10 ans entre sources signalée, non réconciliée.

## 2026-10-30 — L4.04 rédigée
- Créés : `L4.04.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 90/90. FMI (BPM6), BCE (balance des paiements d'août 2026), BEA (T2) ; écart statistique américain signalé.

## 2026-10-30 — L4.05 rédigée
- Créés : `L4.05.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 85/85. BLS (prix à l'importation et à l'exportation, septembre 2026) lu par résumé ; Australie et Brent en sources secondaires ; aucun lien causal avec le change affirmé ; poids implicites des carburants signalés comme approximatifs.

## 2026-10-30 — L4.06 rédigée
- Créés : `L4.06.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 84/84. BRI (communiqué, résumé) et Réserve fédérale (pondérations H.10, résumé) ; niveaux de change en sources secondaires réutilisées de L4.02. Nouvelle règle appliquée : points ouverts classés [critique]/[importante]/[mineure] (aucun critique pour cette leçon). Pilotes L0.01–L0.03 non touchés.

## 2026-10-30 — L4.07 rédigée
- Créés : `L4.07.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 87/87. Décision BCE du 29/10/2026 lue par la presse uniquement (communiqué primaire inaccessible), signalée dans la leçon, le registre et les sources ; anticipation du 24/09 non assimilée à une surprise. Points ouverts classés : 3 importants, 3 mineurs, 0 critique.

## 2026-10-30 — L4.08 rédigée
- Créés : `L4.08.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 90/90. Banque du Japon (septembre), BoE et BNS lues par sources secondaires (primaires BoJ de juillet et BNS du 22/10 réutilisés) ; quatre points « importante », deux « mineure », aucun critique.

## 2026-10-30 — L4.09 rédigée
- Créés : `L4.09.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 86/86. Banque du Canada (texte reproduit) et RBA (secondaire) ; partie émergente volontairement conceptuelle faute de données lisibles, signalée dans la leçon et le registre (importante). Aucun point critique.

## 2026-10-30 — L4.10 rédigée
- Créés : `L4.10.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 84/84. BRI (Quarterly Review sept. 2024, primaire par résumé) ; septembre 2026 par un article Bloomberg reproduit (secondaire), avec intervention de change non vérifiée et incohérence avec L4.08 signalée. Trois points « importante », deux « mineure », aucun critique.

## 2026-10-30 — L4.11 rédigée
- Créés : `L4.11.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 84/84. Intervention du 31/07/2026 lue par une synthèse tertiaire (Wikipédia) et un article secondaire (total du ministère du 28/08) ; premier point **critique** consigné (cas central non confirmé à la source primaire) ; trois « importante », deux « mineure ». Plancher suisse de 2015 : source primaire (BNS via BRI).

## 2026-10-30 — L4.12 rédigée
- Créés : `L4.12.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Contrôles 82/82. Leçon de synthèse du module 4 : thèse guidée EUR/USD datée (25/09 → 29/10/2026), scénarios rédigés après coup signalés comme SIMULATION, score de Brier. Aucune nouvelle source ; points importants hérités consignés.

## 2026-10-30 — Fin du module 4 (12 leçons) : évaluations, projet, sauvegarde
- Évaluations : 5 quiz de chapitre (4.1 à 4.5, 6 QCM chacun), examen EX4 (25 QCM + 5 calculs + 2 cas fictifs ; 60 points, seuil 42), projet P4 (thèse EUR/USD datée comparée au résultat réel ; grille de 40 points, seuil 28). Contrôles techniques : verify_assessments_m04.py (323 OK) ; verify_lessons.py sur l'ensemble des leçons.
- Diagnostic : banque progressive amorcée (content/diagnostic/banque_m04.json, 4 paires A/B) ; modules 0–3 à alimenter.
- Sauvegarde : backups/20261030_1706_fin_module4 (contenu des modules 0 à 4). Index des sauvegardes : backups/INDEX.md.
- Points à vérifier : 1 critique (L4.11), importants et mineurs consignés par leçon dans registry/lessons.json ; consolidation relancée.

## 2026-10-30 — L5.01 rédigée
- Créés : `L5.01.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Chronologie 1900-1973 depuis cinq essais de la Réserve fédérale (primaires institutionnelles, lues par résumé) ; prix de l'or 2024-2026 par sources secondaires (deux records contradictoires signalés, deux « importante », deux « mineure », aucun critique). Aucune causalité de prix affirmée.

## 2026-10-30 — L5.02 rédigée
- Créés : `L5.02.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Bilan offre/demande 2025 du WGC (pages d'offre et de demande, résumés automatiques, 29/01/2026) et T2 2026 (total WGC, composantes par article secondaire). Contrôles 98/98. Identité offre = demande vérifiée (5 002,3 t) ; nature résiduelle du poste OTC signalée comme définition de cours non vérifiée. Trois « importante », deux « mineure », aucun critique. Aucune causalité de prix affirmée.

## 2026-10-30 — L5.03 rédigée
- Créés : `L5.03.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Plan en 8 blocs de l'utilisateur intégré en sections 4.1–4.8 (format à 14 sections conservé). Série FRED FII10 mensuelle (mai–septembre 2026) lue par résumé ; série quotidienne tronquée, non vérifiée ; page TreasuryDirect bloquée (TIPS par source secondaire). Contrôles 98/98 après correction de tolérance. Erreur de rédaction corrigée avant intégration (Fisher : 2,238 % exact, la soustraction surestime). Corrélations 4.8 = SIMULATION. Trois « importante », deux « mineure », aucun critique. Aucune causalité affirmée.

## 2026-10-30 — L5.04 rédigée
- Créés : `L5.04.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Indice large du dollar (FRED DTWEXBGS, H.10) lu par résumé sur cinq jours d'octobre 2026 (table tronquée) ; mécanisme et épisodes 2020/2022/2025 par un seul article de courtier (secondaire). Contrôles 86/86. Or en euros et scénarios = SIMULATION. Deux « importante », deux « mineure », aucun critique. Aucune causalité affirmée.

## 2026-10-30 — L5.05 rédigée
- Créés : `L5.05.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Point mort FRED T10YIEM (mai–septembre 2026) combiné au rendement réel (L5.03) pour décomposer le nominal ; CPI de septembre 2026 déjà lu ; étude WGC 2006 par notice et article secondaire (industrie, non évaluée). Contrôles 95/95 après correction d'une tolérance. Simulations (corrélation annuelle vs cumul, scénarios de CPI) signalées. Trois « importante », deux « mineure », aucun critique. Aucune causalité affirmée ; années 1970 : prix de l'or non lus, signalé.

## 2026-10-30 — L5.06 rédigée
- Créés : `L5.06.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Pages du WGC (T2 2026, Gold Focus de septembre, accès partiel) et trois articles Kitco (enquête, août, Chine en septembre), tous par résumé automatique. Trois incohérences entre sources signalées sans être réconciliées (avoirs de la Chine ; mensuel/trimestriel ; 188,9 t non itemisées). Contrôles 91/91 après correction de tolérance. Part d'or cible = SIMULATION. Trois « importante », deux « mineure », aucun critique. Aucune causalité affirmée.

## 2026-10-30 — L5.07 rédigée
- Créés : `L5.07.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Pages du WGC sur les flux d'ETF de juin et septembre 2026 (résumés automatiques) et flux 2025 par Mining Weekly (secondaire). Contrôles de cohérence : régions, avoirs, prix implicites (écarts de 2 à 4 t). Anomalie de date de la page de juin et écart valeur/tonnes signalés sans réconciliation. Contrôles 98/98 après correction de tolérances d'arrondi. Scénario = SIMULATION. Trois « importante », deux « mineure », aucun critique. Aucune causalité affirmée.

## 2026-10-30 — L5.08 rédigée
- Créés : `L5.08.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Quatre épisodes (2008 par une rétrospective du WGC sans chiffres, mars 2020 par un article secondaire non daté, février 2022 par la note mensuelle du WGC, février-mars 2026 par deux comptes rendus de séance et un article d'opinion). Contrôles 86/86. Second point **critique** consigné (récit 2026 fondé en partie sur une opinion à borne erronée) ; contradiction 5 589 / 5 595 signalée. Scénario décomposé = SIMULATION. Aucune causalité unique affirmée.

## 2026-10-30 — L5.09 rédigée
- Créés : `L5.09.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Règlement du COMEX (chapitre 113, primaire) et exemple de portage du 29-30 juillet 2026 d'un vendeur de métaux (secondaire), formule recalculée (4 095,58 $ retrouvé). **Collision d'identifiants détectée avant enregistrement :** S-CME-01 existait déjà (Euro FX, L0.04) et S-CME-02 (fiche or) aussi ; la nouvelle source a été renumérotée S-CME-04 et S-CME-02 réutilisée, sans toucher aux sections antérieures. Contrôle des doublons d'identifiants relancé (seul le doublon connu S-BIS-01 subsiste le cas échéant). Contrôles 92/92. Deux « importante », deux « mineure », aucun critique.
- Audit des identifiants (L5.09) : trois doublons **antérieurs au module 5** dans `content/sources.md`, non corrigés pour préserver le contenu validé : S-BIS-01 (déjà connu), S-CLE-01 (lignes 20 et 255 : Cleveland Fed, Exchange Stabilization Fund 2008 / PCE vs CPI 2014) et S-STL-01 (lignes 232 et 473 : St. Louis Fed, écart de production 2021 / remises de la Fed 2023). À renuméroter lors de l'audit général, sans réécrire les leçons. Les identifiants créés dans le module 5 (L5.01 à L5.09) ne produisent aucun doublon.

## 2026-10-30 — L5.10 rédigée
- Créés : `L5.10.mdx`, quiz, checks, quizsrc ; sources.md, lessons.json. Étude du WGC (juillet 2025, cinq marchés baissiers à prix de fin de mois), récapitulatif Reuters (2013) et article d'un vendeur de métaux (non daté), par résumé automatique. Différence de mesure séance / fin de mois traitée explicitement (850 $ contre 667 $). Identifiants vérifiés avant écriture (aucune collision). Contrôles 101/101. Trois « importante », deux « mineure », aucun critique. Aucune règle de durée ni prévision par cycle affirmée.

## 2026-10-30 — L5.04 : révision 2 (correction d'une affirmation inexacte)
- Constat : L5.04 (rédigée le même jour) indiquait que les pondérations de l'indice large du dollar étaient « non lues », alors que S-FED-25 (page de la Réserve fédérale du 2 février 2026) les avait déjà fournies en L4.06 (zone euro 21,007 %, Mexique 14,801 %, Canada 12,769 %, Chine 10,891 %). Corrigé : sections 4.2 et 9, liste des sources, check (somme des quatre premiers poids = 59,468 %), points ouverts mis à jour. Copie de l'état antérieur conservée hors du dépôt (/tmp/L5.04.rev1.mdx). Aucune autre leçon modifiée. Contrôles L5.04 : 87/87. Leçon de méthode : toujours rechercher dans sources.md avant d'écrire « non lu ».

## 2026-10-30 — L5.11 rédigée
- Créés : `L5.11.mdx`, quiz, checks, quizsrc ; sources.md (S-FED-26, S-KIT-04, S-BNC-01), lessons.json. Tableau de bord daté du 30/10/2026 (communiqué FOMC du 28/10, dépêche du 21/10, article d'opinion du 29/10, séries FRED et WGC de septembre), âge de chaque donnée, cases « non lu » explicites, sensibilité de la note aux pondérations (−1 / 0 / +2). Identifiants vérifiés avant écriture. Trois « importante », deux « mineure », aucun critique.

## 2026-10-30 — L5.12 rédigée
- Créés : `L5.12.mdx`, quiz, checks, quizsrc ; sources.md (réutilisations uniquement), lessons.json. Thèse en six pièces, cas rétrospectif 2012-2013 (SIMULATION explicitement rétrospective, biais signalé), valeur attendue et score de Brier (0,98 contre 0,667), squelette 2026 sans recommandation. Deux « importante », deux « mineure », aucun critique. Contrôles 82/82.

## 2026-10-30 — Module 5 : évaluations
- Créés : tools/assessments/m05.py, make_assessment_m05.py, verify_assessments_m05.py ; 5 quiz de chapitre (6 QCM), examen EX5 (25 QCM + 5 calculs + 2 cas fictifs, 60 points, seuil 42), projet P5 (40 points, seuil 28), entrée registry/assessments.json, banque de diagnostic content/diagnostic/banque_m05.json (4 paires A/B). Contrôles techniques : 332/332 (évaluations), 6146/6146 (leçons). Contrôles automatiques ≠ validation scientifique.

## 2026-10-30 — Point d'étape après le module 5 (non bloquant)
- Constats : 70 leçons rédigées, 0 intégrée/testée/validée ; contrôles techniques verts (leçons et évaluations m00–m05) ; sauvegarde fin_module5 identique pour m00–m04 et les pilotes. Doublons d'identifiants de sources antérieurs au module 5 (S-BIS-01, S-CLE-01, S-STL-01) toujours à renuméroter ; points ouverts hérités non classés des modules 0–3 toujours à classer ; point critique L4.11 et L5.08 à résoudre avant toute validation scientifique finale. Aucune action sur GitHub, développement du site, publication, dépense ou installation de dépendance. Le travail se poursuit au module 6.

## 2026-10-31 — L6.01 rédigée
- Créés : `L6.01.mdx`, quiz, checks, quizsrc ; sources.md (S-ECL-01, S-KIT-05, S-MIN-02), lessons.json. Orientation reçue de l'utilisateur appliquée : attendu contre publié, surprise, rumeur/nouvelle sans règle, deux hypothèses de signe pour l'or, fiche d'événement avec fenêtres 5 min / 30 min / 4 h fixées d'avance. Cas : réunions de la Fed des 29/07 et 28/10/2026 (articles = variations de séance, non réactions) et 29/02/2012. Les points critiques L4.11 et L5.08 restent au registre, non résolus. Trois « importante », deux « mineure », aucun critique.

## 2026-10-31 — L6.02 rédigée
- Créés : `L6.02.mdx`, quiz, checks, quizsrc ; sources.md (S-CME-05, S-CME-06, S-ADM-04 — S-ADM-02 déjà pris, collision évitée), lessons.json. Plan de l'utilisateur appliqué : taux actuel / anticipation / décision, méthode du CME recalculée (2,3350 % ; 0,725 point ; 2,9 pas ; 10 %/90 %), exemple fictif 60/30/10 → −12,5 pb, probabilités réelles du 28/10 (90,6 % ; 84 %) avec fiche de données, avertissement sur les probabilités consultées après coup. Complète L6.01 (surprise d'octobre ≈ −2,35 pb sous hypothèse), sans modifier L6.01. Points critiques L4.11 et L5.08 inchangés. Trois « importante », deux « mineure », aucun critique.

## 2026-10-31 — L6.03 rédigée
- Créés : `L6.03.mdx`, quiz, checks, quizsrc ; sources.md (S-KIT-06/07/08, S-MPL-01), lessons.json. Plan de l'utilisateur appliqué : quatre asymétries, rendement de fenêtre, trois niveaux de conclusion, cinq contrôles. Étude empirique dégradée et déclarée comme telle : cinq décisions du FOMC de 2026 (variations de séance), exclusions documentées (28/01, 18/03), protocole partiellement fixé d'avance (juillet et octobre déjà lus), permutation exacte (valeur-p minimale 0,20), comparaison par unité de choc (SIMULATION). Points critiques L4.11 et L5.08 inchangés. Trois « importante », deux « mineure », aucun critique.

## 2026-10-31 — L6.04 rédigée
- Créés : `L6.04.mdx`, quiz, checks, quizsrc ; sources.md (S-FRD-04, S-FRD-05), lessons.json. Plan de l'utilisateur appliqué : quatre dimensions, classification reproductible sans information future, état indéterminé, sept vérifications, diagnostic réel du 31/10/2026 avec incertitudes. Étude historique **sur données fictives** (aucune série quotidienne de l'or accessible) et circularité explicitée ; STLFSI4 non accessible. Points critiques L4.11 et L5.08 inchangés. Trois « importante », deux « mineure », aucun critique.

## 2026-10-31 — L6.05 rédigée
- Créés : `L6.05.mdx`, quiz, checks, quizsrc ; sources.md (S-WIK-01), lessons.json. Consignes appliquées : lien avec L6.04 (états inconnus traités par loi des probabilités totales et bornes), quatre sens de « probabilité » distingués, continuité avec L5.12 sans répétition (exemples différents), valeur attendue recalculée indépendamment (script de contrôle), analyse de sensibilité, probabilité d'équilibre, protocole d'enregistrement avec empreinte, évaluation par Brier et table de calibration, rappel qu'une espérance positive n'est pas une preuve de rentabilité. Points critiques L4.11 et L5.08 inchangés. Deux « importante », deux « mineure », aucun critique.

## 2026-10-31 — L6.06 rédigée
- Créés : `L6.06.mdx`, quiz, checks, quizsrc ; sources.md (S-GVZ-01, S-GVZ-02), lessons.json. Consignes appliquées : trois volatilités distinguées, mesure (rendement, écart-type, annualisation, fenêtres), amplitude/direction/tendance séparées, préparation (consensus, scénarios, mouvement implicite) et mesure sur fenêtres fixes, spreads/slippage/gaps chiffrés en simulation, canaux vers XAU/USD non systématiques. Absence de données intrajournalières signalée explicitement. Aucune valeur historique inventée. L4.11 et L5.08 inchangés. Deux « importante », trois « mineure », aucun critique.

## 2026-10-31 — L6.07 rédigée
- Créés : `L6.07.mdx`, quiz, checks, quizsrc ; sources.md (S-FED-27, S-FED-28, S-KIT-09, S-ATF-01, S-CRX-02, S-CME-07, S-UCA-01, S-CBK-01, S-FIN-01), lessons.json. Consignes appliquées : quatre cas (3 Fed + BCE), un cas qui contredit l'hypothèse naïve (16/09), chronologie stricte (probabilités datées, anciennes étiquetées), surprise monétaire recalculée, réactions séparées par niveau, limites explicites (pas d'intrajournalier, pas de réaction BCE). Aucune généralisation. L4.11 et L5.08 inchangés. Trois « importante », trois « mineure », aucun critique.

## 2026-10-31 — L6.08 rédigée
- Créés : `L6.08.mdx`, quiz, checks, quizsrc ; sources.md (aucune nouvelle source), lessons.json. Consignes appliquées : deux lectures opposées (consensus de hausse en décembre, alternatif de maintien), matrice de scénarios à quatre issues, calculs vérifiables (somme 100 %, espérance, valeur nette, sensibilité, probabilité d'équilibre, comparaison central/alternatif), grille de qualité de raisonnement sur 100 qui ne note pas la direction de l'or, note d'analyse modèle datée, scénario alternatif jamais présenté comme signal. Données fictives identifiées. L4.11 et L5.08 inchangés. Deux « importante », deux « mineure », aucun critique.

## 2026-10-31 — L7.01 rédigée
- Créés : `L7.01.mdx`, quiz, checks, quizsrc ; sources.md (S-CFTC-06, S-CFTC-07, S-CFTC-08, S-SAX-01), lessons.json (+ champs `title_working`, `architecture_note`), `registry/ARCHITECTURE_M7_PROPOSITION.md`. Titre de travail de l'utilisateur appliqué sans modifier le curriculum initial ; durée 3,0 h conservée. Données COT officielles du 13/10/2026 (CFTC) recalculées : nets, parts, non rapportables, somme nulle, tonnes, variation hebdomadaire (recoupée avec Saxo). Fiche de positionnement (qui / proportion / évolution / conclusions) avec registre des données indisponibles et conclusions impossibles ; six pièges traités. Aucune relation position-prix affirmée (prix non lus). L4.11 et L5.08 inchangés. Deux « importante », trois « mineure », aucun critique.

## 2026-10-31 — L7.01 révisée (révision 2)
- Motif : la « vérification » de la somme nulle des positions nettes (non rapportables compris) est une identité par construction, car les non rapportables sont déduits de l'intérêt ouvert ; la formulation pouvait laisser croire à un test indépendant. Précision ajoutée au § 4.4 et à l'exercice 3 ; tests indépendants rappelés (pourcentages publiés ; variations publiées). Ancienne version : `backups/20261031_0740_fin_module6/_revisions/L7.01.rev1.mdx`. Autres contenus inchangés.

## 2026-10-31 — Arbitrage du curriculum du module 7 (décision de l'utilisateur)
- Le curriculum initial est la **référence officielle** ; les titres proposés auparavant étaient des propositions pédagogiques. L7.04 reste « Flux d'ETF et d'investisseurs » (créations/rachats, avoirs, flux nets, limites) et L7.05 « Liquidité et calendriers de flux » (fin de mois et de trimestre, rééquilibrages, couvertures, flux institutionnels) ; ils approfondissent L5.06 et L5.07 sans répétition. Titres initiaux, durées et objectifs conservés ; toute modification sera documentée avant mise en œuvre. L7.02 suit donc le titre initial « Positionnement extrême », avec les exigences COT détaillées de l'utilisateur.

## 2026-10-31 — L7.02 rédigée
- Créés : `L7.02.mdx`, quiz, checks, quizsrc ; sources.md (S-CFTC-09 à S-CFTC-13, S-SAN-01, S-WNG-01), lessons.json. Titre du curriculum (« Positionnement extrême ») conservé ; exigences de l'utilisateur intégrées (catégories, net, variation, part de l'intérêt ouvert, limites, comparaison de six dates, aucun signal automatique, tableau COT à calculer). Six rapports officiels (8/9 à 13/10) tabulés ; cohérence positions/variations contrôlée (13 sur 15 exactes, 2 écarts de 1 contrat) ; extrême défini par fenêtre (percentile, z-score, min-max) ; deux études académiques lues ; rapprochement avec un prix présenté puis refusé. Rapports 20/10 et 27/10 inscrits au registre des données indisponibles. L4.11 et L5.08 inchangés. Trois « importante », trois « mineure », aucun critique.

## 2026-10-31 — L7.03 rédigée
- Créés : `L7.03.mdx`, quiz, checks, quizsrc ; sources.md (S-CFTC-14 à S-CFTC-18), lessons.json. Titre du curriculum (« COT sur l'or et le dollar ») conservé. Consignes appliquées : instruments exacts nommés (or COMEX GC 088691 ; « dollar » = Euro FX CME 099741, l'indice du dollar ICE 098662 n'ayant pas pu être localisé et étant inscrit au registre des données indisponibles) ; catégories Managed Money / Leveraged Funds / Asset Manager non présumées équivalentes ; aucun contrat brut comparé entre marchés ; net, variation, part de l'intérêt ouvert et écart standardisé sur fenêtre commune de cinq dates lues ; tableau à quatre situations non mécanique (la case dépend de la catégorie) ; changements de composition des 15 et 22/9 signalés (cause en hypothèse) ; corrélation déclarée non calculable (3 paires lues pour un seuil fixé à 8) ; corrélation de niveaux 0,97 présentée comme piège ; conclusion « indéterminée » admise. Valeurs du 6/10 reconstituées par différence et signalées. Contrôles : 35 comparaisons sur 42 exactes, 7 écarts de 1 contrat. L4.11 et L5.08 inchangés. Quatre « importante », deux « mineure », aucun critique.

## 2026-10-31 — L7.04 rédigée
- Créés : `L7.04.mdx`, quiz, checks, quizsrc ; sources.md (S-WGC-16 à S-WGC-20, S-IAU-01, S-GLD-01, S-INV-02), lessons.json. Titre du curriculum (« Flux d'ETF et d'investisseurs ») conservé ; approfondit L5.06/L5.07 sans reprise. Consignes appliquées : mécanique opérationnelle (créations/rachats contre marché secondaire), fiches IAU et GLD, portée des produits (physique, ETN, contrats à terme, barres et pièces) et des statistiques du WGC, conversions tonnes/onces/valeur, décomposition flux / valorisation sur sept fins de mois (mars–septembre 2026), exemple fictif d'encours en hausse malgré des retraits, piège du ratio flux ÷ tonnes, fréquences et régions, flux observé contre intention, atelier en cinq étapes (sept. 2026 = divergence documentée). Aucun cours de marché lu : prix implicites dérivés, signalés. Contrôles : concordances régionales (écart de 0,8 Md$ en mars), avoirs (écart de 2 t en juillet). L4.11 et L5.08 inchangés. Trois « importante », deux « mineure », aucun critique.

## 2026-10-31 — L7.04 révisée (révision 2)
- Motif (précaution de l'utilisateur) : le « −51 Md$ » de septembre est présenté comme **résidu de valorisation estimé** (différence de valeurs arrondies, dates de valorisation et avoirs non démontrés comparables), non comme mesure du prix de l'or ; les prix implicites ne remplacent pas les cours de marché. Écarts du WGC (régions de mars, avoirs et texte de juillet) maintenus ouverts, sans correction. Trois points ajoutés au registre. Ancienne version : `backups/_revisions_m7/L7.04.rev1.mdx`. Les 153 contrôles restent techniques, sans valeur de validation scientifique.

## 2026-10-31 — L7.05 rédigée
- Créés : `L7.05.mdx`, quiz, checks, quizsrc ; sources.md (S-CME-08, S-GSC-01, S-NBR-01, S-CXO-01, S-GUL-01, S-LBMA-04 ; S-CME-02 relue), lessons.json. Titre du curriculum (« Liquidité et calendriers de flux ») conservé. Consignes appliquées : relecture de L5.06/L5.07/L7.01/L7.04 sans reprise ; mécanismes traités séparément (rééquilibrage, clôtures mensuelle/trimestrielle, expiration, roulement, couverture, fixing) ; calendrier 2026 calculé (le dernier jour de négociation GC tombe 2 jours ouvrés avant la fin du mois) ; signe et ordre de grandeur d'un rééquilibrage (SIMULATION) ; protocole fixé d'avance avec règle de conclusion à trois issues ; exemple fictif calculé (moyenne, médiane, dispersion, sélection de dates) ; seul constat réel : intérêt ouvert COMEX (−5,13 % la semaine du 29/9, cause indéterminée) ; atelier « hausse de 2,3 % le dernier jour du trimestre » (SIMULATION). **Aucune série quotidienne lue : analyse empirique réelle impossible, conclusion « données insuffisantes ».** Aucun point critique de contenu ajouté ; L4.11 et L5.08 inchangés. Quatre « importante » (dont l'absence de série quotidienne), deux « mineure », aucun critique.

## 2026-10-31 — L7.05 révisée (révision 2)
- Motif (contrôle de l'utilisateur) : (1) la règle des deux jours ouvrés n'est plus généralisée (valable pour les mois du tableau selon la règle lue, à confirmer) ; (2) « le rééquilibrage vend ce qui a surperformé » est contextualisé (fonds à poids cibles fixes ; dépend de la stratégie, des bandes de tolérance et de la performance relative) ; (3) la baisse de 5,13 % de l'intérêt ouvert ne prouve ni liquidation de longs, ni rééquilibrage, ni baisse de la demande. Ancienne version : `backups/_revisions_m7/L7.05.rev1.mdx`. Quatre points ajoutés au registre. Les 131 contrôles restent techniques. L4.11 et L5.08 inchangés.

## 2026-10-31 — L7.06 rédigée
- Créés : `L7.06.mdx`, quiz, checks, quizsrc ; sources.md (S-WGC-21), lessons.json. Titre officiel du curriculum (« Horizons de flux », 2,5 h) conservé. Consignes appliquées : horizon / fréquence / délai distingués ; quatre horizons présentés comme convention pédagogique ; fiche de provenance par famille (ETF, COT, banques centrales, couverture, demande physique) avec mesure, fréquence, délai calculé, révisions, limites, horizon utile ; stocks, positions, achats et flux non traités comme équivalents ; conversion en tonnes sans addition ; critères de persistance écrits d'avance ; quatre scénarios A à D ; atelier fictif en six étapes (SIMULATION) ; étude de cas réelle en réemploi (T2 2026, septembre) ; question de synthèse ; critère « montré / suggéré / non permis ». Une seule nouvelle lecture (communiqué du T2 2026) ; autres données signalées comme réemplois. Révision documentée : T1 2026 des banques centrales 244 → 57 t. L4.11 et L5.08 inchangés. Trois « importante », trois « mineure », aucun critique.

## 2026-10-31 — L7.06 révisée (révision 2)
- Motif (contrôle méthodologique de l'utilisateur) : (1) fiche de la révision T1 2026 des banques centrales (244 → 57 t) : publication initiale non lue, publication révisée du 30/07/2026, période, motif non détaillé, 187 t non présentées comme des achats disparus ; (2) délais présentés comme observations sur les publications étudiées ; (3) sommes glissantes : fenêtre et méthode définies, aucun mélange avec les encours ; (4) T2 2026 : tableau des unités et bases de comparaison. Ancienne version : `backups/_revisions_m7/L7.06.rev1.mdx`. Quatre points ajoutés au registre. Contrôles automatiques techniques, non scientifiques. L4.11 et L5.08 inchangés.

## L7.07 — Combiner positionnement et fondamentaux (31/10/2026)
Rédigée, sourcée, évaluée (révision 1) : quatre piliers, trois niveaux A/B/C, matrice à six situations, atelier en huit étapes sur données réelles d'sept.–oct. 2026 (COT 13/10 de 18 jours classé en situation 6), fiche de thèse horodatée, exercices 1–8, quiz 8 questions. Nouvelles sources : S-BIS-10 (relais de presse). 83/83 contrôles automatiques (≠ validation scientifique). Points critiques L4.11 et L5.08 inchangés (ouverts).

## L7.08 — Atelier : un indicateur COT (31/10/2026)
Rédigée, sourcée, évaluée (révision 1). Nouvelle lecture : rapport désagrégé du 27/10/2026 (page courante CFTC, mise à jour 30/10, S-CFTC-19) ; série réelle de 8 semaines (20/10 reconstitué). Anomalie ouverte : chute de l'OI COMEX or (526 276 → 396 810) sans cause lue. Fenêtre insuffisante : percentile/z réels non exploités ; percentile et z enseignés sur série SIMULATION de 52 semaines. Quiz 10 questions, 6 exercices dont 3 de calcul, 1 cas réel, 1 interprétation complète. 138/138 contrôles automatiques (≠ validation scientifique). L4.11 et L5.08 inchangés (ouverts critiques). Fin du chapitre 7.3 : restent les évaluations du module 7.

## L7.08 révisée (révision 2) — périmètres Futures Only / Combined (31/10/2026)
Suite à la vigilance sur l'OI (−24,6 %) : vérification des périmètres. Page d'index CFTC (S-CFTC-21) : `/dea/futures/` = Futures Only, `/dea/options/` = Combined. Archives 08/09–13/10 (`other_sof`) = Combined ; rapport du 27/10 (`other_sf`) très probablement Futures Only (page CMX Futures Only S-CFTC-20 : OI 396 810, 287 opérateurs identiques). Correction : série Combined limitée à 6 semaines (−28 469 contrats, −20,4 %, 88,5 t) ; 27/10 présenté à part (tableau B), reconstitution du 20/10 sur son périmètre ; effet de dénominateur illustré par une SIMULATION ; calcul de variation d'OI entre périmètres supprimé ; quiz et contrôles mis à jour (140/140). Version 1 : backups/_revisions_m7/L7.08.rev1.mdx. Anomalie maintenue ouverte (périmètre non confirmé par l'en-tête ; rapports Combined du 27/10 et Futures Only du 13/10 non lus).

## Module 7 — évaluations et clôture (31/10/2026)
Quiz de chapitres 7.1, 7.2, 7.3 (6 questions chacun, seuil 5/6) ; examen EX7 (25 QCM + 5 calculs + 2 cas fictifs, 60 points, seuil 42/60) ; projet P7 (40 points, seuil 28, mini-projet « indicateur COT pour l'or et un dollar-pair » intégré en Partie C) ; banque de diagnostic m07 (4 paires A/B) ; registre consolidé des données indisponibles et conclusions impossibles ; vérificateur tools/verify_assessments_m07.py (262 contrôles, techniques). Sauvegarde backups/20261031_1043_fin_module7 ; modules 0–6 et pilotes identiques à fin_module6. L4.11 et L5.08 inchangés (ouverts critiques). Aucune intégration, aucun test utilisateur, aucune validation scientifique.

## L8.01 — Cadre d'analyse du risque géopolitique (31/10/2026)
Rédigée, sourcée, évaluée (révision 1). Grille G8 réutilisable (huit rubriques), trois statuts (possible, probable, confirmé), sept canaux de transmission avec signe possible pour l'or dans les deux directions, durées, règle d'attribution. Deux événements documentés : invasion de l'Ukraine (février 2022, exemple corrigé) et événements du 7 octobre 2023 (exercice autonome) ; exemple SIMULATION ambigu. Sources : GPR (Caldara et Iacoviello), IFDP Fed, Fed de Boston, FMI (blog et GFSR avril 2025 ch. 2), BRI (Bulletin 54), EIA (2), OFAC, Banque mondiale (28/10/2026), Fed (FSR mai 2026), WGC (3). 83/83 contrôles automatiques (≠ validation scientifique). Durée de l'effet sur l'or non évaluée ; prix issus du WGC non vérifiés LBMA. L4.11 et L5.08 inchangés (ouverts critiques) ; L5.08 non utilisée.

## L8.02 — Guerres, sanctions et énergie (31/10/2026)
Rédigée, sourcée, évaluée (révision 1). Trois couches de sanctions (annoncée, appliquée, effet observé) ; chaîne énergie → inflation → politique monétaire → taux réels et dollar → or en sept maillons étiquetés ; cas 2022 (directive 3 : signature 24/02, effet 26/03 ; communiqué du 28/02 ; Brent ; exportations russes de brut ; or rapporté 1 910/2 069/1 942/1 672 $) ; contre-exemple = même choc sur un horizon plus long, sans second épisode indépendant ; réserves officielles (COFER), achats d'or (WGC) et ETF distingués, motifs déclarés et interprétés, pas de dédollarisation automatique ; deux scénarios SIMULATION avec invalidations ; tableau faits / mécanismes / hypothèses / indisponibles ; 8 exercices dont refus d'une conclusion catégorique ; quiz 8 questions (7/8). Sources : OFAC (directive 3), Trésor (28/02/2022), EIA (3), BRI, FMI (2), WGC (6). 29/29 calculs, 97/97 contrôles de leçon (techniques ≠ validation). Textes de la directive 4 et de l'UE non lus ; prix WGC non vérifiés LBMA ; ID S-UST-05 pour éviter un doublon. L4.11, L5.08 et périmètre CFTC inchangés (ouverts).

## L8.02 — révision 2 (31/10/2026)
Trois corrections demandées au verdict : (1) contenu de la directive 4 présenté comme rapporté par le communiqué du Trésor, non vérifié dans le texte primaire ; (2) contre-exemple renommé « évolution ultérieure du même épisode », non indépendant, ne démontrant pas la cause de la baisse ; (3) prix de l'or du WGC explicitement non vérifiés ni confirmés comme clôtures. Version 1 conservée : backups/_revisions_m8/L8.02.rev1.mdx et .rev1.quiz.json. Écarts de stocks d'ETF conservés au registre des anomalies. Quiz inchangé (8 questions).

## L8.03 — Élections et changements de politique (31/10/2026)
Rédigée, sourcée, évaluée (révision 1). Résultat / attente / surprise (modèle jouet SIMULATION à deux issues) ; promesse, décision officielle, adoption juridique, application effective ; canaux budget, commerce, inflation, politique monétaire, taux réels, dollar, or ; deux cas documentés avec frise et statuts : novembre 2024 (312-226 ; or comptant −2,8 % le 06/11, Fed −25 pb le 07/11 ; EO 14257 du 02/04/2025 ; LBMA : T4 2024 −1,43 %, 2025 +62,9 %) et novembre 2016 (304-227 ; or > −8 % en novembre, Fed le 14/12 à 36 jours, loi fiscale 409 jours après) ; tableau faits / attentes / surprises / interprétations / hypothèses ; trois scénarios SIMULATION avec invalidations ; 8 exercices dont refus de « toujours » ; quiz 8 questions (7/8). 26/26 calculs. Prix de bases hétérogènes ; rendements et dollar en série non lus ; textes de l'EO, de la loi de 2017 et du communiqué 2016 non lus. L4.11, L5.08, périmètre CFTC inchangés. L8.02 corrigée en révision 2 en amont (backups/_revisions_m8).

## L8.03 — révision 2 (31/10/2026)
Trois corrections du verdict : (1) la variation de l'or du 06/11/2024 n'est plus présentée comme effet démontré de l'élection (bases hétérogènes, facteurs concurrents non mesurés) ; (2) surprise électorale explicitement non mesurée pour 2016 (attentes préalables non documentées), la baisse de novembre et le mouvement ultérieur n'isolant pas l'effet du scrutin ; (3) contradictions conservées sans choix (LBMA 2025 : 4 481,85 $ / 4 338,25 $ ; baisse de novembre 2024 : −2,8 % Reuters / −3,3 % OANDA) et suppression de tous les rendements mêlant instruments ou horaires (seule paire conservée : fixing du matin 06/01/2025 → fixing du matin 2025, avec les deux valeurs). Exercice 2 réécrit (calculs permis et interdits) ; question 4 du quiz remplacée (contradiction LBMA). Version 1 conservée dans backups/_revisions_m8/L8.03.rev1.*.

## L8.04 — Commerce, droits de douane et fragmentation (31/10/2026)
Rédigée, sourcée, évaluée (révision 1). Six statuts d'une mesure (annonce, adoption, entrée en vigueur, application effective, suspension/modification, invalidation), taux annoncé et effectif, canaux (prix des importations, coûts, inflation, croissance, marges, chaînes, incertitude), effets de change imposant/partenaires, fragmentation, matrice mesure → canal → observable → effet possible sur l'or ; deux chronologies documentées (2025 : 20/01-01/04, EO 14257 du 02/04, modifications des 08-09/04, Genève le 12/05, prévisions FMI/OMC, arrêt du 20/02/2026 via résumé ; 2018-2019 : listes 1 à 4, Phase 1, Fed du 31/07/2019, FMI 2019) ; comparaison des contextes monétaires sans conclure à des effets identiques ; prévisions publiées à l'époque séparées des résultats ; exercice multi-canaux SIMULATION ; trois scénarios SIMULATION avec invalidations ; 8 exercices dont refus de conclusion catégorique ; quiz 8 questions (7/8). 20/20 calculs. Textes officiels américains et chinois non lus ; aucun rendement mêlant bases ; anomalies LBMA/OMC/WGC consignées. L8.02 rév. 2 et L8.03 rév. 2 en amont. L4.11, L5.08, périmètre CFTC inchangés.

## L8.04 — révision 2 (31/10/2026, méthode par chapitre)
Textes officiels consultés **par résumé automatique** (non lecture intégrale) : EO 14257 (05/04 taux de base, 09/04 taux par pays, exemptions, annexes non vues), EO 14259 (34→84 % Chine, 09/04), EO 14316 (suspension prolongée au 01/08/2025). EO 14266 (125 %) et EO 14298 non lus. Ajout S-GOVINFO-02/03/04, S-FR-01 ; S-EIA-03 ajouté au frontmatter. Sauvegarde rev 1 : backups/_revisions_m8/L8.04.rev1.*. Vérification 92/92.

## Chapitre 8.2 — consolidation (31/10/2026)
Méthode par chapitre adoptée (registry/METHODE_CHAPITRE.md). Quiz de chapitre 8.2 (6 q., 5/6), synthèse et 3 exercices, tools/assessments/m08.py, tools/make_assessment_m08.py, tools/verify_assessments_m08.py (30/30), registry/assessments.json (m08), rapport registry/CH8.2_RAPPORT.md.

## L8.05 — Risk-on et risk-off (31/10/2026, chapitre 8.3)
Rédigée, sourcée, évaluée (révision 1). Régimes = co-mouvements ; indicateurs (VIX/VIXMO, actions, rendements, dollar, CHF/JPY, or) ; perception contre comportement ; pourquoi l'or ne monte pas systématiquement ; matrice de confirmation/contradiction à règle fixée d'avance ; trois épisodes (2001, mars 2020 selon un gestionnaire, 2022) ; 8 exercices, quiz 8 q. Vérification 79/79.

## L8.06 — Durée des effets d'un choc (31/10/2026, chapitre 8.3)
Rédigée, sourcée, évaluée (révision 1). Grille T0 / 7 / 30 / 90 jours / structurel ; tableau de couverture (couvert/partiel/non couvert) ; trois épisodes (1990-1991, 2001, 2022) sans reconstitution de prix ; 8 exercices, quiz 8 q. Vérification 99/99.

## Chapitre 8.3 — livrables consolidés (31/10/2026)
Frise comparative (content/m08/chap_8.3.frise.mdx), quiz de chapitre 8.3 (6 q., 5/6), synthèse + 3 exercices, rapport registry/CH8.3_RAPPORT.md, registre registry/ANOMALIES_M8.md (A1-A15). Vérifications : leçons 178/178, évaluations 56/56.

## L8.07 — Crises bancaires et de dette souveraine (31/10/2026, chapitre 8.4)
Rédigée, sourcée, évaluée (révision 1). Liquidité/solvabilité ; canaux de contagion ; typologie des interventions ; banque contre État ; trois épisodes (2008, 2010-2012, mars 2023) ; pourquoi l'or peut d'abord être vendu (hypothèse) ; 8 exercices, quiz 8 q. Vérification 86/86.

## L8.08 — Décider sans surréagir (31/10/2026, chapitre 8.4)
Rédigée, sourcée, évaluée (révision 1). Protocole en dix étapes ; ensemble d'informations daté ; critères agir/attendre/ne pas intervenir ; journal ; étude de cas de mars 2023 à trois dates ; SIMULATIONS (opportunité documentée, sensibilité). 8 exercices, quiz 8 q. Vérification 77/77.

## Chapitre 8.4 — livrables consolidés (31/10/2026)
Quiz de chapitre 8.4 (6 q., 5/6), synthèse + 3 exercices, rapport registry/CH8.4_RAPPORT.md, registre registry/ANOMALIES_M8.md (A1-A20). Vérifications : leçons 163/163 pour L8.07-L8.08, évaluations 77/77.

## L8.07 — révision 2 (31/10/2026, clôture du module 8)
Réserves du verdict du chapitre 8.4 : (1) deux estimations de la baisse de l'or en 2008 (−8,2 % et ≈ −20 %) conservées comme non comparables ; (2) aucun effet sur l'or, le dollar ou les taux présenté comme établi pour 2010-2012 ; (3) mars 2023 : fermeture de SVB, taux du BTFP et rapport complet de la Fed restent à vérifier ; (4) discours de Draghi : plus aucune citation ni date précise attribuée. Sauvegarde rev 1 : backups/_revisions_m8/L8.07.rev1.*. Quiz rév. 2 ; vérification 85/85.

## Module 8 — clôture pédagogique (31/10/2026)
Quiz de chapitre 8.1 (6 q., 5/6) ; audit des quiz (tools/audit_quizzes_m08.py) : biais de longueur des bonnes réponses constaté, distracteurs des quiz 8.1–8.4 réécrits (révision 2 pour 8.2–8.4, sauvegarde backups/_revisions_m8/m08.assessments.before_distractors.py) ; quiz de leçon non corrigés (anomalie A27). Examen final EX8 (120 min, 100 points, sections 20/20/15/15/15/15, seuil provisoire 70) ; projet P8 (100 points, seuil provisoire 70) ; registre des anomalies complet (33 lignes, backup avant clôture) ; rapport consolidé registry/M8_RAPPORT_CONSOLIDE.md. Vérifications : leçons 699/699 (L8.01–L8.08), évaluations 113/113. Aucune intégration, aucun test, aucune validation scientifique.

## Module 8 — préparation à l'intégration (31/10/2026)
Quiz de leçon L8.01–L8.08 : distracteurs réécrits (révision +1, sauvegardes dans backups/_revisions_prep/). Seuils harmonisés (7/8 = 0,875 ; 5/6). L8.05 révision 2 : définition du signal central (VIX et S&P 500 ; l'or exclu), convention non validée. Création de M8_SOURCES_A_LIRE, M8_PROTOCOLE_VERIFICATION_DONNEES, M8_GRILLE_AUDIT_EX8_P8, M8_PREPARATION_JOURNAL et du rapport de préparation. A33, L4.11, L5.08 et l'anomalie de périmètre CFTC restent ouvertes. Aucun test d'intégration, déploiement, publication, installation ni dépense.

## Module 8 — audit scientifique et pédagogique (31/10/2026)
Consultation de 14 sources par résumé automatique (aucune lecture intégrale) ; URL de S-EIA-01 corrigée (références seulement, sauvegardes et SHA-256 dans le journal) ; registre des anomalies mis à jour (A36–A40) ; audit automatisé à l'aveugle des quiz (indice de longueur encore exploitable : 66 % de réussite de la devinette sur les quiz de leçon) ; audit des seuils (73 écarts numériques sans effet pratique) ; propositions de barèmes EX8/P8, de signal central et diagnostic M8 enregistrées comme propositions. Aucune modification de quiz, d'épreuve, de seuil ou de L8.05. Aucun test d'intégration, déploiement, publication, installation ni dépense.

- 31/10/2026 : rapport final registry/M8_RAPPORT_AUDIT_SCIENTIFIQUE_PEDAGOGIQUE.md créé (aucune modification de contenu).
