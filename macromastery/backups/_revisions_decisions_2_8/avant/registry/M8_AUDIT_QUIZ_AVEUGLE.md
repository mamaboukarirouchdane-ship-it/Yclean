# Audit « à l'aveugle » des quiz du module 8 — rapport des anomalies et corrections proposées

Date : 31/10/2026. **Aucune modification supplémentaire n'a été faite** (ta consigne : rapport d'abord). Périmètre : 64 questions de quiz de leçon révisées, 24 questions de quiz de chapitre, et, à titre de contrôle, les 18 QCM d'EX8.

## 1. Méthode et limite

Une relecture réellement « à l'aveugle » exige une personne qui n'a pas écrit les questions et qui répond sans voir la clé : **je n'en suis pas une**, et je ne prétends pas l'avoir faite. J'ai donc fait deux choses : (1) un **test automatique de devinette** (`tools/blind_audit_quizzes_m08.py`) : six heuristiques qui tentent de trouver la bonne réponse sans connaître le sujet (réponse la plus longue, la plus chiffrée, la plus proche de l'énoncé, la plus « centrale » parmi les options, celle qui contient le moins de mots absolus, la plus ponctuée) ; (2) une **relecture critique** de plausibilité, d'unicité et de grammaire sur les questions signalées. Une relecture humaine à l'aveugle reste nécessaire avant toute validation.

## 2. Résultats du test de devinette (hasard = 25 %)

```
Taux de réussite de chaque heuristique de devinette (hasard = 25 %) :

quiz de leçon (64): 64 questions
  plus longue                                    65.8 %
  plus de chiffres                               31.6 %
  recouvrement avec l'énoncé                     17.6 %
  plus proche des autres options                 27.0 %
  moins d'absolus                                32.3 %
  plus de virgules/point-virgule (précision)     56.0 %
  marqueurs absolus : 7 dans les bonnes réponses ; 56 dans les distracteurs (0.29 par distracteur)

quiz de chapitre (24): 24 questions
  plus longue                                    58.3 %
  plus de chiffres                               45.1 %
  recouvrement avec l'énoncé                     12.2 %
  plus proche des autres options                 25.0 %
  moins d'absolus                                29.2 %
  plus de virgules/point-virgule (précision)     62.8 %
  marqueurs absolus : 5 dans les bonnes réponses ; 24 dans les distracteurs (0.33 par distracteur)

QCM EX8 (18): 18 questions
  plus longue                                    55.6 %
  plus de chiffres                               16.7 %
  recouvrement avec l'énoncé                     33.8 %
  plus proche des autres options                 18.1 %
  moins d'absolus                                39.8 %
  plus de virgules/point-virgule (précision)     59.7 %
  marqueurs absolus : 3 dans les bonnes réponses ; 27 dans les distracteurs (0.50 par distracteur)

Questions signalées (rapport de longueur ≥ 1,35, ou absolus dans les trois distracteurs et aucun dans la bonne réponse) : 20
  ('L8.02.quiz.json', 'L8.02-Q4', 1.4, 0, [1, 0, 0])
  ('L8.02.quiz.json', 'L8.02-Q5', 1.48, 0, [0, 0, 0])
  ('L8.02.quiz.json', 'L8.02-Q8', 1.43, 0, [0, 1, 1])
  ('L8.03.quiz.json', 'L8.03-Q7', 1.15, 0, [1, 1, 1])
  ('L8.04.quiz.json', 'L8.04-Q3', 1.37, 0, [0, 0, 0])
  ('L8.04.quiz.json', 'L8.04-Q6', 1.43, 0, [1, 1, 0])
  ('L8.04.quiz.json', 'L8.04-Q8', 1.41, 0, [1, 1, 1])
  ('chap_8.1.quiz.json', 'C8.1-Q2', 1.39, 0, [0, 0, 1])
  ('chap_8.2.quiz.json', 'C8.2-Q5', 1.43, 1, [0, 0, 0])
  ('chap_8.2.quiz.json', 'C8.2-Q6', 1.44, 1, [0, 1, 0])
  ('chap_8.4.quiz.json', 'C8.4-Q3', 1.15, 0, [1, 1, 1])
  ('chap_8.4.quiz.json', 'C8.4-Q4', 1.78, 2, [0, 0, 0])
  ('EX8.exam.json', 'EX8-Q2', 1.49, 1, [0, 0, 1])
  ('EX8.exam.json', 'EX8-Q3', 1.44, 0, [0, 0, 0])
  ('EX8.exam.json', 'EX8-Q5', 1.55, 0, [1, 1, 2])
  ('EX8.exam.json', 'EX8-Q7', 1.49, 0, [1, 0, 1])
  ('EX8.exam.json', 'EX8-Q8', 1.41, 0, [0, 0, 0])
  ('EX8.exam.json', 'EX8-Q13', 1.75, 0, [0, 0, 0])
  ('EX8.exam.json', 'EX8-Q15', 1.24, 0, [1, 1, 2])
  ('EX8.exam.json', 'EX8-Q16', 0.79, 0, [1, 1, 1])
```

**Lecture.** (a) La révision a ramené le rapport de longueur moyen vers 1,1–1,3, mais le **classement** compte plus que le rapport : la bonne réponse est encore la plus longue dans environ deux cas sur trois (66 % pour les quiz de leçon, 58 % pour les chapitres, 56 % pour EX8), soit un indice exploitable (le hasard donne 25 %). (b) L'heuristique de **ponctuation/précision** (virgules, deux-points, points-virgules) réussit à 56–63 % : les bonnes réponses contiennent plus de qualifications. (c) Les **mots absolus** (toujours, jamais, aucun, seulement…) sont rares dans les bonnes réponses (7 sur 64 questions de leçon) et fréquents dans les distracteurs (56) : un apprenant averti élimine les options absolues. (d) Le recouvrement lexical avec l'énoncé n'aide pas (12–34 %) et la « centralité » est neutre (18–27 %).

## 3. Anomalies constatées

| # | Constat | Où | Gravité | Correction proposée |
|---|---|---|---|---|
| Q1 | Indice de longueur : la bonne réponse est la plus longue dans 69 % des questions de leçon | 64 questions | importante | Rééquilibrer par le **contenu**, non par le raccourcissement des bonnes réponses : donner aux distracteurs la même densité d'information (chiffres, condition, périmètre) ; faire en sorte que la bonne réponse soit la plus longue dans au plus 30–35 % des questions ; **ne pas raccourcir artificiellement** une bonne réponse dont la précision est le point évalué |
| Q2 | Indice de précision : seules les bonnes réponses portent des réserves (« non vérifié », « hypothèse », « conditionnel ») | tous quiz | importante | Introduire des distracteurs qualifiés mais faux (réserve placée au mauvais endroit, hypothèse présentée avec des chiffres exacts) et des bonnes réponses courtes et affirmatives lorsque le sujet s'y prête |
| Q3 | Indice de mots absolus : distracteurs « toujours/jamais/aucun » | 56 contre 7 | importante | Remplacer une partie des distracteurs absolus par des distracteurs nuancés mais faux ; ne pas mettre d'absolu dans plus d'un distracteur par question |
| Q4 | Étiquettes dupliquées entre bonne réponse et distracteur : « De perception » figure dans les options a et d | L8.05-Q2 | mineure | Réécrire d (« De comportement : … » est déjà pris deux fois) ; viser deux étiquettes différentes avec des justifications différentes pour éviter la lecture par étiquette seule |
| Q5 | Règle « couvert / partiel / non couvert » : « proche de l'horizon » n'est pas défini ; une option parle de « quinze jours » | L8.06-Q2 ; EX8 (D, K4) | importante | **Défaut de la leçon**, non du quiz : définir une tolérance (par exemple jours ouvrés avant ou après l'horizon) dans L8.06 par une révision documentée ; en attendant, ne pas évaluer les cas limites |
| Q6 | Redondance : la variation COMEX 278,60 → 275,30 est posée dans L8.05 et L8.06 ; le taux effectif 25 % × 40 % dans L8.04, C8.2 et EX8 (K1 avec d'autres valeurs) | plusieurs | mineure | Acceptable pour une révision de chapitre ; remplacer l'un des deux doublons du même niveau par une variante numérique |
| Q7 | Réponse d'un quiz comportant un fait non vérifié : borne d'un an des OMT (non retrouvée dans le résumé), « 30/12/2022 » (inférence) | L8.07 (OMT), énoncés citant la clôture de fin 2022 | importante | Réécrire la question pour porter sur le fait vérifié (voir M8_VERIFICATION_SOURCES.md) ou conserver la mention « d'après les sources lues » dans l'énoncé |
| Q8 | Questions où la bonne réponse énumère plusieurs éléments (L8.08-Q1 dix étapes) alors que les distracteurs sont des permutations : plausibles mais l'évaluation porte sur la mémorisation d'un ordre | L8.08-Q1 | mineure | Garder si l'ordre est un objectif d'apprentissage déclaré ; sinon évaluer la compréhension d'une étape |
| Q9 | Unicité : aucune question n'a plus d'une bonne réponse au regard des textes des leçons, à l'exception de Q4 et Q5 ci-dessus | 88 questions | — | Confirmer par relecture humaine |

## 4. Questions signalées par l'audit automatique

(Rapport de longueur ≥ 1,35, ou absolus dans les trois distracteurs et aucun dans la bonne réponse.) Pour chacune, la correction proposée est de type Q1/Q2/Q3.

    Questions signalées (rapport de longueur ≥ 1,35, ou absolus dans les trois distracteurs et aucun dans la bonne réponse) : 20
      ('L8.02.quiz.json', 'L8.02-Q4', 1.4, 0, [1, 0, 0])
      ('L8.02.quiz.json', 'L8.02-Q5', 1.48, 0, [0, 0, 0])
      ('L8.02.quiz.json', 'L8.02-Q8', 1.43, 0, [0, 1, 1])
      ('L8.03.quiz.json', 'L8.03-Q7', 1.15, 0, [1, 1, 1])
      ('L8.04.quiz.json', 'L8.04-Q3', 1.37, 0, [0, 0, 0])
      ('L8.04.quiz.json', 'L8.04-Q6', 1.43, 0, [1, 1, 0])
      ('L8.04.quiz.json', 'L8.04-Q8', 1.41, 0, [1, 1, 1])
      ('chap_8.1.quiz.json', 'C8.1-Q2', 1.39, 0, [0, 0, 1])
      ('chap_8.2.quiz.json', 'C8.2-Q5', 1.43, 1, [0, 0, 0])
      ('chap_8.2.quiz.json', 'C8.2-Q6', 1.44, 1, [0, 1, 0])
      ('chap_8.4.quiz.json', 'C8.4-Q3', 1.15, 0, [1, 1, 1])
      ('chap_8.4.quiz.json', 'C8.4-Q4', 1.78, 2, [0, 0, 0])
      ('EX8.exam.json', 'EX8-Q2', 1.49, 1, [0, 0, 1])
      ('EX8.exam.json', 'EX8-Q3', 1.44, 0, [0, 0, 0])
      ('EX8.exam.json', 'EX8-Q5', 1.55, 0, [1, 1, 2])
      ('EX8.exam.json', 'EX8-Q7', 1.49, 0, [1, 0, 1])
      ('EX8.exam.json', 'EX8-Q8', 1.41, 0, [0, 0, 0])
      ('EX8.exam.json', 'EX8-Q13', 1.75, 0, [0, 0, 0])
      ('EX8.exam.json', 'EX8-Q15', 1.24, 0, [1, 1, 2])
      ('EX8.exam.json', 'EX8-Q16', 0.79, 0, [1, 1, 1])

## 5. Critère d'acceptation proposé pour une révision 3

- Test de devinette : chaque heuristique ≤ 35 % sur chaque groupe (leçon, chapitre, examen).
- La bonne réponse est la plus longue dans au plus 35 % des questions de chaque quiz de leçon.
- Un seul mot absolu au maximum par question parmi les distracteurs, et au moins un distracteur qualifié par question.
- Relecture à l'aveugle par une personne extérieure : taux de réussite sans formation sur le module ≤ 40 % (indicatif).
- Aucune bonne réponse n'est raccourcie sans justification pédagogique ; aucune clé n'est modifiée.

## 6. Décision attendue

Autoriser (ou non) la révision 3 des quiz selon le critère ci-dessus, avec sauvegardes dans `backups/_revisions_audit/` et journalisation. Les quiz restent en révision 2 en attendant.
