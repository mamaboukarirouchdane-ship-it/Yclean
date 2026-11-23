# Module 8 — Géopolitique et risques mondiaux : rapport consolidé de clôture de rédaction

> Mise à jour postérieure : voir `registry/M8_RAPPORT_PREPARATION_INTEGRATION.md` (31/10/2026) pour les corrections de la phase de préparation (quiz de leçon, L8.05 rév. 2, seuils) ; les chiffres de ce rapport restent ceux de la clôture de rédaction.

Date : 31/10/2026. **La clôture de rédaction du module 8 ne signifie pas que celui-ci est scientifiquement validé.** Aucune intégration au site, aucun test utilisateur, aucune publication et aucune dépense n'ont eu lieu. Une bonne analyse fondamentale ne garantit pas une transaction gagnante.

## 1. Leçons rédigées

| Leçon | Durée prévue | Révision | Exercices corrigés | Quiz (révision) | Contrôles techniques | Points ouverts |
|---|---|---|---|---|---|---|
| L8.01 Cadre d'analyse du risque géopolitique | 2,5 h | 1 | 8 | 8 q. (1) | 83/83 | 8 |
| L8.02 Sanctions | 3 h | 2 | 8 | 8 q. (1) | 97/97 | 11 |
| L8.03 Élections | 3 h | 2 | 8 | 8 q. (2) | 87/87 | 12 |
| L8.04 Commerce et droits de douane | 3 h | 2 | 8 | 8 q. (2) | 92/92 | 10 |
| L8.05 Risk-on et risk-off | 3 h | 1 | 8 | 8 q. (1) | 79/79 | 8 |
| L8.06 Durée des effets d'un choc | 3 h | 1 | 8 | 8 q. (1) | 99/99 | 7 |
| L8.07 Crises bancaires et souveraines | 3 h | 2 | 8 | 8 q. (2) | 85/85 | 9 |
| L8.08 Décider sans surréagir | 3 h | 1 | 8 | 8 q. (1) | 77/77 | 5 |

Total : 8 leçons sur 8, 23,5 h prévues (durées indicatives), environ 45 000 mots, 64 exercices corrigés. Évaluations de module : 4 quiz de chapitre (6 questions, seuil 5/6) ; 3 synthèses de chapitre (8.2 à 8.4, 3 exercices corrigés chacune) ; frise comparative 8.3 ; examen EX8 (120 min, 100 points : A 20, B 20, C 15, D 15, E 15, F 15 ; seuil provisoire 70/100) ; projet P8 (8 parties, 100 points, seuil provisoire 70/100). Diagnostic initial du module : **non produit**.
États du registre pour les 8 leçons : planifiée, rédigée, sourcée, évaluée = oui ; **intégrée, testée, validée = non**.

## 2. Contrôles techniques réussis

- Leçons : 699 contrôles sur 8 leçons, 0 échec (structure en 14 sections, exercices et corrections en nombre égal, marqueurs d'inachevé, mentions obligatoires, identifiants de sources définis, calculs des fichiers tools/checks).
- Évaluations : 113 contrôles, 0 échec (quiz 8.1–8.4, synthèses, calculs de l'examen EX8, dates, espérances, barèmes 20/20/15/15/15/15 et 100 points, grille P8 de 100 points).
- Audit des quiz : tools/audit_quizzes_m08.py (6 questions, position des bonnes réponses équilibrée, explications ≥ 60 caractères, absence de doublons, biais de longueur).
- Ces contrôles confirment une **conformité technique**, non la validité scientifique, l'exactitude des sources ni la valeur pédagogique.

## 3. Sources consultées intégralement

**Aucune.** Toutes les lectures web ont été des résumés automatiques ; aucune source n'a été lue en entier par le rédacteur.

## 4. Sources consultées uniquement par résumé

- Les 89 identifiants cités par les leçons L8.01–L8.08 (registry/lessons.json, content/sources.md) relèvent de ce niveau : organismes officiels (Federal Reserve, OFAC, Federal Register, GovInfo, EIA, FMI, BRI, BCE, WGC, LBMA, CBOE, etc.), données de sites commerciaux et commentaires de gestionnaires.
- Lectures tronquées : Economic Report of the President 1991 et Fed Monetary Policy Report de février 2009 (100 000 premiers caractères), chapitre du FMI d'avril 2025 (100 000 sur 115 658 caractères), Northern Miner (premier paragraphe).
- Métadonnées seulement : S-BIS-12 (page du discours de Draghi), S-NM-01.
- Chiffres de presse ou de commentaires de gestionnaires (par exemple S-WT-01, S-MC-01/02/03) : identifiés comme tels dans les leçons, non vérifiés.

## 5. Données indisponibles

Séries journalières de l'or, du pétrole, du dollar, des rendements et des taux réels autour de chaque épisode ; textes intégraux des directives et décrets (annexe I de l'EO 14259, EO 14266) ; discours de Draghi de juillet 2012 ; rapport complet de la Fed sur SVB, dates de fermeture de SVB et taux du BTFP ; attentes préalables documentées de la plupart des événements ; valeurs récentes de l'indice GPR ; chiffres du FMI et de la Banque mondiale propres à l'or. Aucun prix manquant n'a été reconstitué ; les horizons non couverts restent non couverts. Détail : registry/ANOMALIES_M8.md, section « Données indisponibles ».

## 6. Anomalies non résolues

33 lignes dans registry/ANOMALIES_M8.md, toutes **ouvertes** : 1 critique, 16 importantes, 16 mineures. Sont conservées sans arbitrage : plus haut LBMA 2025 (4 481,85 / 4 338,25 $), pic du pétrole d'octobre 1990 (≈ 40 / 46 $), or du 14/09/2001 (300 / 295 $), baisse de l'or en 2008 (−8,2 % et ≈ −20 %, non comparables), date du discours de Draghi (non établie), taux initial de la Chine dans la guerre tarifaire (34 / 84 %), avoirs d'ETF de fin mars 2022 (3 836 / 3 835 / 3 838,3 t). Nouvelles anomalies de clôture : biais de longueur des quiz de leçon (non corrigé, A27), « signal central » non défini dans la règle de L8.05 (A29), seuil stocké 0,8 contre 7/8 des quiz de leçon (A30), absence de toute lecture intégrale (A33, critique).
Points ouverts des leçons : 70 (44 importants, 19 mineurs, 7 critiques hérités). **L4.11, L5.08 et l'anomalie de périmètre CFTC restent ouverts** et ne sont utilisés dans aucune leçon du module 8.

## 7. Éléments nécessitant une validation scientifique ou pédagogique

- Lecture des sources primaires en intégralité (directives, décrets, discours, rapports de la Fed, textes FMI et BCE) puis relecture des énoncés factuels des 8 leçons.
- Séries de prix harmonisées (même instrument, même horaire) pour les trois épisodes de L8.06, 2008 et 2010-2012 avant toute conclusion sur l'or, le dollar ou les taux.
- Règles et seuils pédagogiques (matrice risk-on/off, seuils de couverture, protocole de décision, probabilités et espérances fictives) : conventions de cours, non résultats scientifiques.
- Barèmes et seuils de réussite (quiz 5/6, quiz de leçon 7/8, examen 70/100, projet 70/100) et durée de 2 h de l'examen : provisoires, à calibrer avec des essais réels.
- Corrections du biais de longueur des 64 questions de quiz de leçon ; relecture de la qualité des distracteurs.
- Durée du projet P8 (8 h) : provisoire, comme P7.
- Diagnostic initial du module 8 : à produire.
- Réserves du verdict 8.4 : appliquées à L8.07 révision 2 (2008 non comparable, aucun effet établi pour 2010-2012, SVB/BTFP/Fed à vérifier, aucune citation ni date attribuée à Draghi).

## 8. Décision attendue

Le module 8 est **rédigé, techniquement conforme, non validé**. Le passage à l'intégration et aux tests n'est pas engagé : il dépend de ta décision. Aucun changement de site, GitHub, publication, dépense ou installation n'a été effectué.
