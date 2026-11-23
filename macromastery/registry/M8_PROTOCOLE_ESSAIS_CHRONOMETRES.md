# Module 8 — Protocole des essais chronométrés d'EX8 et de P8 (décision 5 = B, 23/11/2026)

**Statut : protocole rédigé ; aucun essai réalisé.** Les durées de **120 minutes (EX8)** et de **8 heures (P8)** restent des **hypothèses non validées** (champ `durationStatus` d'EX8, en-tête de P8). Elles ne seront validées qu'après les essais ci-dessous, sur décision de l'utilisateur. Je ne peux pas faire ces essais moi-même : je ne suis pas un candidat de niveau cible, et j'ai rédigé les épreuves.

## 1. Participants

| Épreuve | Nombre minimal | Profil | Exclusions |
|---|---|---|---|
| EX8 | 3 candidats (5 conseillés) | Ont suivi les leçons L8.01 à L8.08 et réussi leurs quiz ; niveau cible du cours | Rédacteurs des épreuves ; personnes ayant vu la correction ; relecteurs à l'aveugle des QCM (pour garder la relecture indépendante) |
| P8 | 2 candidats (3 conseillés) | Mêmes conditions ; choisissent eux-mêmes leur événement (section 1 de P8) | Idem |

## 2. Conditions (identiques pour tous)

- Version des épreuves figée et notée : EX8 révision 3 (barème v2), P8 barème v2 ; empreintes SHA-256 relevées dans `backups/_revisions_decisions_2_8/MANIFEST_APRES.sha256` au moment de l'essai.
- EX8 : sans limite de temps imposée (pour mesurer la durée réelle), documents autorisés comme prévu par la consigne, calculatrice autorisée. P8 : en plusieurs séances possibles, temps effectif noté.
- Aucune aide de l'auteur pendant l'essai ; questions de compréhension notées sur la fiche (elles signalent une consigne ambiguë).

## 3. Relevés

**EX8** — par candidat : heure de début et de fin de chaque bloc : QCM (18), calculs (K1 à K5), analyses (A1 à A6 séparément) ; analyses non terminées ; note obtenue avec le barème v2 (par section et par tâche).
**P8** — par candidat et par partie (A à H) : temps effectif ; temps de recherche des sources séparé du temps de rédaction ; parties non terminées ; note avant et après pénalités.

Feuille de relevé : une ligne par candidat et par bloc, avec `durée (min)`, `terminé (oui/non)`, `difficulté perçue (1-3)`, `remarque`.

## 4. Règle de décision (fixée avant les essais)

| Indicateur | Seuil de validation de la durée prévue |
|---|---|
| Fraction des candidats qui terminent toutes les analyses d'EX8 dans 120 min | ≥ 80 % (avec 3 candidats : tous) |
| Médiane de la durée totale d'EX8 | ≤ 110 min (marge de 10 min) |
| Fraction des candidats qui terminent P8 en 8 h de temps effectif | ≥ 2 sur 3 (ou 2 sur 2) |
| Médiane du temps effectif de P8 | ≤ 7 h 30 |

- Si un seuil n'est pas atteint : allonger la durée (EX8 : par paliers de 15 min ; P8 : par paliers d'une heure) **ou** réduire la charge (une analyse d'EX8 ou une partie de P8), puis refaire un essai. Choix soumis à l'utilisateur.
- Si tout est atteint avec une large marge (médiane EX8 ≤ 80 min) : signaler la possibilité de raccourcir ; décision de l'utilisateur.
- Les essais servent aussi de **contrôle du barème** : un candidat qui réussit les parties objectives mais échoue aux minima, ou l'inverse, est examiné ; aucune note n'est modifiée après coup.

## 5. Ce que les essais ne valident pas

Ni la validité scientifique des contenus, ni le seuil de 70 comme mesure de maîtrise (il faudrait davantage de candidats et une comparaison avec un jugement d'expert). Avec 3 à 5 candidats, les résultats sont **indicatifs**.

## 6. Traçabilité

Résultats à consigner dans `registry/M8_ESSAIS_CHRONOMETRES_RESULTATS.md` (à créer lors du premier essai), avec date, version des épreuves, participants anonymisés, relevés bruts et décision. Les durées ne changent de statut (`durationStatus`) qu'après cette consignation.
