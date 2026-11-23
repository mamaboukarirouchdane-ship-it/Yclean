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
