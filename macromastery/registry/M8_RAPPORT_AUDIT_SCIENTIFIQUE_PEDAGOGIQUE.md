# Module 8 — Rapport d'audit scientifique et pédagogique (31/10/2026)

Suite à ta décision : intégration, tests d'intégration, déploiement, publication, installation et dépenses restent **interdits** et **n'ont pas eu lieu**. Aucun quiz, aucune épreuve, aucun seuil et aucune leçon n'a été modifié, sauf une correction de référence (URL) documentée. **Les contrôles automatisés sont distincts de la validation scientifique et pédagogique.**

## 1. Sources et données effectivement vérifiées

Détail : `registry/M8_VERIFICATION_SOURCES.md`. **Niveau de lecture : résumé automatique pour les 14 sources consultées ; aucune lecture intégrale** (A33 reste ouverte).

- **Cohérent avec le résumé consulté** : directive 3 de l'OFAC (24/02/2022 ; 26/03/2022 ; 14 jours ; 13 entités nommées) ; EO 14257 (signé le 02/04/2025 ; base de 10 % le 05/04 ; taux par pays le 09/04) ; EO 14259 (Chine de 34 à 84 %, effet le 09/04) ; EO 14316 (signé le 07/07/2025, suspension prolongée jusqu'au 01/08/2025) ; Fed 12/03/2023 (BTFP jusqu'à un an, collatéral au pair) ; Fed 28/04/2023 (quatre causes, 31 avertissements) ; Fed 17/09/2001 (−50 pb à 3 %) ; EIA (Brent 2022 : 100 $ en moyenne, 75 $ le 08/12, 85 $ en fin d'année ; prévision de 116 $ du 03/03/2022) ; FMI (environ 1 % sur un trimestre pour les chocs globaux ; queues de risque environ six mois ; définition de l'événement majeur) ; Cboe (VIX du 13/03/2023 : 26,52, plus haut intrajournalier 30,81, VIX9D 30,93).
- **Écarts découverts** : (i) **URL de S-EIA-01 erronée**, corrigée (preuve : la bonne page donne les chiffres) — A39 ; (ii) la formulation de L8.01 sur le FMI (« 1 point par mois », « 2,5 points sur les émergents ») n'est pas retrouvée à l'identique (A36) ; (iii) la borne d'un an des OMT n'apparaît pas dans le résumé (A37) ; (iv) l'exclusion de l'or du 2-3 avril n'est pas confirmée par l'EO 14257 vu, annexe II absente (A38) ; (v) « 30/12/2022 » est une inférence ; (vi) « proche de l'horizon » n'est pas défini dans L8.06 (A40).
- **Non vérifiable avec mes outils** : séries LBMA (or), séries EIA journalières, rendements du Trésor autour du 13/03/2023, dollar, attentes préalables. Aucune valeur inventée ; les anomalies de données A1–A6, A8–A14, A17–A19, A21–A26 restent ouvertes.
- **Preuves partielles, sans fermeture** : A7, A15, A31, A32 ; A16 et A20 inchangées.
- **Signal central de L8.05** : définition conservée comme convention ; analyse de huit cas (quatre non évaluables), limites et risques de biais de sélection dans `registry/M8_SIGNAL_CENTRAL_ANALYSE.md` ; options A, B, C de révision proposées, aucune appliquée.

## 2. Résultats de l'audit des quiz

Détail : `registry/M8_AUDIT_QUIZ_AVEUGLE.md`. **Limite : je ne peux pas faire une vraie relecture à l'aveugle** (j'ai rédigé les questions) ; j'ai fait un test automatique de devinette et une relecture critique.
- **Indice de longueur encore exploitable** : deviner la réponse la plus longue réussit à **66 %** (quiz de leçon), **58 %** (chapitre), **56 %** (QCM d'EX8), contre 25 % au hasard. Le rapport de longueur est faible (1,1–1,3), le classement reste prédictif.
- **Indice de précision** (ponctuation) : 56–63 % ; **indice des mots absolus** : 7 dans les bonnes réponses contre 56 dans les distracteurs des quiz de leçon.
- Heuristiques sans effet : recouvrement avec l'énoncé (12–34 %), centralité (18–27 %).
- Autres anomalies : étiquettes dupliquées (L8.05-Q2), règle de couverture ambiguë (L8.06, A40), redondances entre quiz, faits non vérifiés dans des énoncés. Aucune question n'a plus d'une bonne réponse selon les textes des leçons (à confirmer par un humain).
- **Corrections proposées, non appliquées** : rééquilibrage par le contenu (densité d'information comparable), distracteurs qualifiés mais faux, au plus un absolu par question, critère d'acceptation chiffré, aucune bonne réponse raccourcie artificiellement, aucune clé modifiée.

## 3. Tableau des seuils et propositions d'harmonisation

Détail et tableau complet de 73 lignes : `registry/M8_SEUILS_QUIZ.md` (script `tools/audit_thresholds.py`).
- 136 quiz audités ; **0 cas où le nombre de réponses exigé diffère de celui affiché**.
- **73 écarts numériques** (35 quiz de leçon des modules 4 à 7 : 0,8 stocké pour « 7 sur 8 » ; 38 quiz de chapitre des modules 0 à 7 : 0,8 stocké pour « 5 sur 6 »), **sans effet pratique sur la réussite**. **Correction** : le chiffre de 17 communiqué précédemment était un sous-comptage.
- **Proposition R1 (recommandée)** : exigé = ⌈0,8 × n⌉, stocké comme entier `requiredCorrect` ; 8 questions → 7, 6 → 5, 10 → 8. Alternatives R2 (formats uniformes) et R3 (75 %).
- Le module 8 est déjà harmonisé. **Aucune modification globale automatique** n'a été faite.

## 4. Propositions de barèmes EX8 et P8

Détail et calculs : `registry/M8_PROPOSITION_BAREMES_EX8_P8.md`.
- **EX8 v2** : QCM 18 × 1 = 18 ; calculs 15 ; analyses 67 (au lieu de 49). Avec parties objectives parfaites, 70 impose 37/67 (55 %) aux analyses au lieu de 19/49 (39 %). Totaux de sections inchangés (20/20/15/15/15/15) ; pondération par tâche pour A1–A6.
- **Minima proposés** : A 10/20, D 8/15, F 8/15 (compétences non compensables : qualification, non-conclusion sur absence de données, décision) ; aucun minimum pour B, C, E.
- **P8** : consolidation des dix pénalités en cinq catégories avec plafonds, **plafond global −25** (au lieu de −52 sans plafond), un fait générateur = une seule pénalité, minima A ≥ 9, G ≥ 8, H ≥ 8 sur 15. Exemple : une faute unique passe de −11 à −5.
- **Durées** (120 min, 8 h) : hypothèses, **non validées**, essai chronométré proposé. Rien n'est appliqué.

## 5. Diagnostic initial M8 proposé

Fichier : `content/diagnostic/banque_m08.json` (statut : **PROPOSITION — non validée, non intégrée**).
- Même architecture que `banque_m04` à `banque_m07` : 4 paires de QCM parallèles A/B (forme A = diagnostic initial, forme B = version finale alternative), accessible avant le cours, non noté.
- **Prérequis testés uniquement** : variation en %, délai en jours, écart à l'attendu, variation en points de base. **Aucune notion enseignée par le module** (statuts, canaux, régimes, horizons, protocole) n'est testée ; ces **sept compétences à acquérir** sont listées à part, non évaluées.
- Deux questions ouvertes non notées (observé / prévu ; facteurs simultanés de l'or).
- Cohérence : même schéma d'items ; ajouts de champs (`status`, `revision`, `prerequisites_tested`, `competences_to_acquire_not_tested`, `open_questions`, `prerequisite`) absents des banques existantes — à harmoniser lors de l'élaboration du diagnostic général ; les modules 0 à 3 restent à alimenter dans la banque générale. Les valeurs ont été recalculées par script ; relecture humaine requise.

## 6. Anomalies restantes, fichiers modifiés, sauvegardes et contrôles

**Anomalies (40 lignes, `registry/ANOMALIES_M8.md`)** : **A33 (critique), L4.11, L5.08 et l'anomalie de périmètre CFTC restent ouvertes.** Fermée avec preuve : A39 (URL). Ouvertes avec preuve partielle : A7, A15, A31, A32. Ouvertes : A1–A6, A8–A14, A16–A26, A28, A34 (73 quiz), A35, A36–A38, A40. Corrigées en phase précédente, à valider : A27, A29, A30.

**Fichiers modifiés** : content/sources.md, content/m08/L8.01.mdx, content/m08/L8.02.mdx (URL de référence uniquement), registry/ANOMALIES_M8.md, registry/assessments.json, registry/PRODUCTION_LOG.md, registry/M8_PREPARATION_JOURNAL.md, registry/M8_RAPPORT_PREPARATION_INTEGRATION.md (correction du chiffre 17 → 73), POINTS_A_VERIFIER.md et EMPREINTES.sha256 (régénérés).
**Fichiers créés** : registry/M8_VERIFICATION_SOURCES.md, M8_SIGNAL_CENTRAL_ANALYSE.md, M8_AUDIT_QUIZ_AVEUGLE.md, M8_SEUILS_QUIZ.md, M8_PROPOSITION_BAREMES_EX8_P8.md, ce rapport ; content/diagnostic/banque_m08.json ; tools/blind_audit_quizzes_m08.py, tools/audit_thresholds.py, tools/make_diagnostic_m08.py.
**Sauvegardes** : `backups/_revisions_audit/` (sources.md, L8.01, L8.02, ANOMALIES_M8 avant modification) avec `MANIFEST_AVANT.sha256` ; empreintes SHA-256 après modification dans le journal.

**Contrôles** : réussis — leçons L8.01–L8.08 699/699 ; ensemble du dépôt 8 578/8 578 (91 leçons) ; évaluations du module 8 115/115 ; audit des seuils : 0 incohérence d'effet ; `consolidate.py` : 503 empreintes. Échoués — aucun. **Non réalisés** : lecture intégrale des sources, vérification contre les séries, relecture humaine à l'aveugle, essais chronométrés d'EX8 et P8, test sur téléphone, tout test d'intégration.

## Décisions qui attendent ton accord

1. Signal central : A (conserver et documenter les limites), B, C ou statu quo.
2. Révision 3 des quiz selon le critère d'acceptation, et relecture humaine à l'aveugle (qui ?).
3. Règle commune de seuils R1/R2/R3 et application aux 73 quiz des modules 0 à 7.
4. Barème EX8 v2, minima A/D/F, pénalités P8 plafonnées, minima A/G/H.
5. Essais chronométrés d'EX8 et P8.
6. Révisions de leçons proposées (L8.01 FMI, L8.07 OMT, L8.04 or, L8.06 tolérance) après lecture des sources.
7. Obtention de fichiers pour la lecture intégrale des sources de priorité 1 et 2, et des séries de prix (téléchargements gratuits, source par source).
8. Harmonisation du schéma du diagnostic avec les banques existantes.
