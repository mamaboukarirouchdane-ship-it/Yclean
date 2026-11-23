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
