# Propositions de barèmes, seuils et pénalités — EX8 et P8 (non appliquées)

Date : 31/10/2026. **Ces propositions ne modifient ni `EX8.exam.json` ni `P8.projet.mdx`.** Elles attendent ta décision. Les durées de 120 minutes (EX8) et de 8 heures (P8) restent **provisoires** jusqu'à un essai chronométré. Calculs refaits par script dans la session ; barèmes et seuils sont des choix pédagogiques à valider, non des résultats scientifiques.

> **Mise à jour du 23/11/2026 — décision 4 = B : propositions appliquées.** EX8 révision 3 (barème v2, pondération par tâche, minima A 10/20, D 8/15, F 8/15, règles de correction) et P8 (cinq catégories plafonnées, plafond global −25, note plancher 0, minima A 9, G 8, H 8 sur 15). Cohérence arithmétique contrôlée par `tools/verify_baremes_ex8_p8.py`. Les durées restent des hypothèses (décision 5 : `registry/M8_PROTOCOLE_ESSAIS_CHRONOMETRES.md`). Le texte ci-dessous est la proposition d'origine, conservée telle quelle.

## 1. EX8 — constat et objectif

Barème actuel : 18 QCM × 2 = 36 ; 5 calculs × 3 = 15 ; 6 analyses = 49. Parties objectives : 51/100, analyses : 49 %. Pour atteindre 70 avec des parties objectives parfaites, il suffit de **19/49 (39 %)** aux analyses ; un candidat au hasard aux QCM obtient en moyenne 9 points. Les compétences d'analyse (qualification, canaux, régimes, horizons, crises, décision) sont le cœur du module et pèsent trop peu.

## 2. EX8 — barème proposé (v2)

Totaux par section inchangés (A 20, B 20, C 15, D 15, E 15, F 15 = 100).

| Section | QCM (1 point) | Calculs (3 points) | Analyse | Total |
|---|---|---|---|---|
| A. Identification et qualification d'un choc | 4 | 0 | A1 : 16 | 20 |
| B. Canaux de transmission | 3 | K1, K2 : 6 | A2 : 11 | 20 |
| C. Régimes risk-on / risk-off | 3 | K3 : 3 | A3 : 9 | 15 |
| D. Durée et persistance | 3 | K4 : 3 | A4 : 9 | 15 |
| E. Crises bancaires et souveraines | 3 | K5 : 3 | A5 : 9 | 15 |
| F. Décision argumentée sur l'or | 2 | 0 | A6 : 13 | 15 |
| **Total** | **18** | **15** | **67** | **100** |

Le QCM passe de 2 à 1 point (il est devinable ; voir l'audit à l'aveugle) ; les analyses passent de 49 à 67 points (67 %). Parties objectives : 33/100.

**Effets (calculés).**

| Situation | Barème actuel | Barème proposé |
|---|---|---|
| Parties objectives parfaites ; analyses nécessaires pour 70 | 19/49 (38,8 %) | 37/67 (55,2 %) |
| Espérance au hasard sur les QCM | 9,0 points | 4,5 points |
| Objectif parfait + analyses à 40 % | 70,6 (réussite) | 59,8 (échec) |
| Objectif parfait + analyses à 50 % | 75,5 | 66,5 (échec) |
| Objectif parfait + analyses à 60 % | 80,4 | 73,2 (réussite) |
| Objectif à 80 % + analyses à 60 % | 70,2 | 66,6 (échec) |
| Objectif à 80 % + analyses à 70 % | 75,1 | 73,3 (réussite) |
| Objectif à 100 % + analyses à 100 % | 100 | 100 |

Sous le barème proposé, **70 impose toujours au moins 37/67 aux analyses** : un minimum global séparé sur les analyses serait redondant.

### Pondération par tâche des analyses (v2)

| Analyse | Tâches (points) | Total |
|---|---|---|
| A1 (A) | T1 classement des cinq énoncés : 4 ; T2 rubriques 1 à 3 de G8 : 4 ; T3 annonce / signature / application et fenêtres : 3 ; T4 non-attribution du mouvement de l'or : 3 ; T5 conclusions impossibles : 2 | 16 |
| A2 (B) | T1 association observable-canal : 3 ; T2 trois canaux, deux directions : 3 ; T3 pas de signe unique : 2 ; T4 conclusion permise : 3 | 11 |
| A3 (C) | T1 classement et score : 3 ; T2 verdict par la règle : 2 ; T3 deux hypothèses : 2 ; T4 limites et statut des seuils : 2 | 9 |
| A4 (D) | T1 dates et rangs : 3 ; T2 grille : 3 ; T3 commentaire de décembre : 1 ; T4 conclusion permise : 2 | 9 |
| A5 (E) | T1 solvable mais illiquide : 1 ; T2 calcul à 15 % : 2 ; T3 comparaison à 40 % : 2 ; T4 liquidité contre solvabilité : 2 ; T5 or vendu d'abord (hypothèse) : 2 | 9 |
| A6 (F) | T1 six critères : 3 ; T2 espérance et sensibilité : 2 ; T3 décision et déclencheur : 3 ; T4 invalidations : 2 ; T5 abstention et biais rétrospectif : 2 ; T6 journal : 1 | 13 |

**Règles de correction proposées** : échelle par tâche 0 / moitié / plein, avec descripteurs écrits ; une erreur de calcul reportée dans une étape suivante correcte n'est pas sanctionnée deux fois ; toute réponse qui présente une prévision de prix ou une certitude de gain perd les points de la tâche de conclusion concernée ; l'usage de données postérieures à la date du cas est interdit.

### Seuils minimaux par section (proposition)

Je propose des minimaux **uniquement** pour trois compétences jugées indispensables, à 50 % de la section :

| Section | Minimum | Justification pédagogique |
|---|---|---|
| A (qualification d'un choc) | 10/20 | Sans distinction fait / déclaration / hypothèse et annonce / application, toutes les analyses suivantes reposent sur un statut faux |
| D (durée et persistance) | 8/15 | Le cours interdit de conclure d'une absence de données ; c'est une règle de rigueur non compensable par d'autres sections |
| F (décision argumentée) | 8/15 | C'est la synthèse du module : protocole, robustesse, invalidations, refus de l'abstention et de la réaction systématiques |

Les sections B, C, E ne reçoivent pas de minimum : leurs compétences sont importantes mais compensables (lecture des canaux, des régimes et des crises relève d'un jugement qui s'affine avec la pratique), et multiplier les minima augmenterait le risque d'échec pour une erreur isolée. **Réussite proposée : total ≥ 70 et minima A, D, F.** Le seuil de 70 reste provisoire.

## 3. EX8 — durée

120 minutes = hypothèse. Répartition de départ à tester : QCM 18 × 1,5 min = 27 ; calculs 5 × 4 = 20 ; analyses 73 (A1 et A6 plus longues). **Essai chronométré proposé** : au moins 3 candidats de niveau cible, temps relevé par bloc ; décision de durée prise sur la médiane et la fraction qui termine les analyses ; toute durée de la grille d'audit reste « non validée » avant cet essai.

## 4. P8 — pénalités : constat

Pénalités actuelles : sources (−2, plafond −8), donnée postérieure à T0 (−5), rendement entre instruments ou horaires différents (−4), prix reconstitué ou case non couverte remplie (−5), contradiction tranchée sans le dire (−4), hypothèse présentée comme un fait (−3), absence de condition d'invalidation (−6), thèse présentée comme prévision ou signal (−6), scénarios modifiés après observation (−6), résumé présenté comme lecture intégrale (−5). Cumul théorique : **−52**. **Aucun plafond global** : un score négatif est possible. **Cumul injustifié** : un seul défaut peut déclencher plusieurs pénalités et aussi faire perdre des points de grille. Exemple (une seule faute : un prix reconstitué par interpolation, puis utilisé pour un rendement) : prix reconstitué −5, donnée sans source −2, rendement entre horaires différents −4 = **−11**, en plus de la perte de points aux critères C et E. De même, « absence de condition d'invalidation » (−6) répète la perte déjà prévue au critère G (15 points).

## 5. P8 — règles proposées

1. **Pénalités réservées aux manquements d'intégrité**, pas aux insuffisances de qualité (déjà notées dans les critères).
2. **Un fait générateur = une seule pénalité**, la plus spécifique ; les conséquences en cascade ne sont pas sanctionnées à nouveau.
3. **Catégories et plafonds** :

| Catégorie | Pénalité | Plafond de catégorie |
|---|---|---|
| Sources manquantes | −2 par donnée | −8 |
| Gel de l'information (donnée postérieure à T0 en B ou G) | −5 une fois | −5 |
| Intégrité des données (rendement entre instruments ou horaires différents ; prix reconstitué ou case non couverte remplie) | −5 pour la première faute, −3 pour chaque autre | −8 |
| Étiquetage épistémique (hypothèse comme fait ; thèse comme prévision ou signal ; contradiction tranchée sans le dire ; résumé présenté comme lecture intégrale) | −4 par faute | −8 |
| Intégrité du processus (scénarios modifiés après observation) | −6 une fois | −6 |

   Somme des plafonds : 35 ; **plafond global proposé : −25** ; note plancher 0.
4. « Absence de condition d'invalidation » ne donne plus de pénalité : elle est sanctionnée par le critère G et par un **minimum de 8/15** en G.
5. **Minima proposés** : A ≥ 9/15 (existant), G ≥ 8/15 (invalidations et scénarios), H ≥ 8/15 (séparation faits, interprétations, hypothèses et conclusions impossibles). Réussite : total après pénalités ≥ 70 et minima A, G, H.
6. La grille de 100 points reste inchangée (A 15, B 10, C 10, D 15, E 10, F 10, G 15, H 15) ; les poids d'analyse macroéconomique (D, E, F, G, H) totalisent 65 points.
7. Rédiger des **descripteurs à quatre niveaux** (0, 1/3, 2/3, plein) par critère avant usage.

**Effet sur l'exemple** : la faute unique ci-dessus coûte −5 (intégrité des données) au lieu de −11, et le total cumulé de toutes les pénalités ne peut pas dépasser −25.

## 6. Durée de P8

8 heures = hypothèse (comme pour P7). Essai proposé : une fiche complète faite par une personne extérieure à la rédaction sur un événement choisi par elle, temps relevé par partie ; décision après essai.

## 7. Ce que ces propositions ne changent pas

Aucun fichier d'épreuve. Les contrôles automatiques actuels (113 sur EX8) vérifient le barème en vigueur ; ils devront être adaptés si la v2 est adoptée. Les barèmes ne valent pas validation scientifique.

## 8. Décisions attendues

(1) Adopter ou non le barème EX8 v2 et la pondération par tâche. (2) Valider ou modifier les minima A, D, F d'EX8 et A, G, H de P8. (3) Adopter ou non le plafond de −25 et les cinq catégories de pénalités de P8. (4) Autoriser les essais chronométrés (qui, quand). Rien n'est appliqué en attendant.
