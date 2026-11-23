# Rapport de contrôle qualité — leçons pilotes L0.01 à L0.03
Mis à jour le 29 octobre 2026 (révision 3 de L0.01). Auteur du contrôle : l'assistant (même instance que la rédaction ; pas de relecture indépendante).

## 1. Statut par leçon
| Leçon | Révision | Contrôles exécutés | Réserves |
|---|---|---|---|
| L0.01 | 3 (révisions du 29/10/2026) | voir section 2 | voir section 3 |
| L0.02 | 1 | calculs, quiz, structure, sources (script) ; relecture critique | non révisée depuis ; voir section 3 |
| L0.03 | 1 | idem | non révisée depuis ; voir section 3 |

## 2. Vérifications réellement exécutées (L0.01, révision 2)
| # | Vérification | Méthode | Résultat |
|---|---|---|---|
| 1 | Source BCE : passage « 49 % / environ 35 % », périmètre, dénominateurs, comparabilité | Deux lectures de la page S-ECB-01 par l'outil de lecture web (résumés automatiques), la seconde reproduisant le tableau des engagements ligne par ligne | 49 % = prêts / total des engagements financiers sélectionnés (48,9 %) confirmé par le tableau. Le « 35 % » n'est pas une ligne du tableau : 8 430 + 3 747 = 12 177 = 35,4 % du même total ; rapprochement cohérent mais non explicité par la page. Périmètre : administrations publiques, sociétés non financières, ménages. |
| 2 | Part « résiduelle » | Calcul sur le tableau | Le « 16 % » obtenu par 100 − 49 − 35 reposait sur des arrondis. Remplacé par la part des trois lignes dépôts + fonds de pension + autres = 5 406 / 34 395 = 15,7 %, documentée par le tableau. La somme des six lignes (34 396) dépasse le total publié de 1 Md€ (arrondis). |
| 3 | Calculs de la révision (Exemples A, B, D ; Exercices 1(e), 2, 3, 6 ; seuil) | `verify_m00.py` | Tous concordent (22 contrôles ajoutés pour la révision 2 ; script global : RÉSULTAT GLOBAL OK) |
| 4 | Quiz L0.01 : 8 questions, une seule bonne réponse chacune, explications, seuil | Lecture complète du JSON + script | Conforme ; `passThreshold` = 0,8 ; ⌈0,8 × 8⌉ = 7 bonnes réponses sur 8, cohérent avec la leçon. **Quiz non modifié.** |
| 5 | Structure de la leçon (rubriques, 3 à 6 exercices avec correction, sources citées définies) | Script | 6 exercices, 6 corrections, aucune rubrique manquante, aucune source non définie |
| 6 | Page SEC (citations) | Relecture de la page S-SEC-01 par l'outil de lecture web | Trois citations confirmées. Numéros de page : deux lectures donnent 13 puis 14 pour la même phrase → aucun numéro de page n'est cité. |
| 7 | Cohérence du registre et de la fiche des sources | Chargement JSON ; relecture | Mis à jour (durée 3 h, révision 2, S-BIS-01 ajoutée à L0.01) |

## 3. Points restant à vérifier
- Valeurs du tableau BCE : relevées par lecture automatisée (deux lectures concordantes), jamais vues directement ; à reconfirmer sur la page.
- Phrase complète de la BCE sur 49 % / 35 % : citée par fragments seulement (la lecture automatisée ne restitue pas les phrases longues).
- Définitions de cours non sourcées : marché primaire/secondaire, familles de marchés (capitaux, monétaire, dérivés), profondeur, slippage, commission, forward, future, swap de change.
- Tableau 4.4 (mode de négociation par instrument) : connaissance générale, non sourcée ; à sourcer ou à garder en interprétation.
- « Jusqu'à un an » pour le marché monétaire : convention, non sourcée.
- Terminologie « contrat à terme / contrat de change à terme / future / forward » : L0.01 distingue forward (gré à gré) et future (standardisé) ; L0.02 (glossaire) et L0.03 emploient « contrat à terme » pour le forward. **Non modifiées** ; à harmoniser sur ta décision.
- Durée estimée passée de 2,5 h à 3 h : estimation, non mesurée.
- Lecture par un débutant réel ; relecture indépendante ; test dans une interface (aucun site).
- Quiz : volontairement inchangé ; aucune question n'évalue encore la liquidité affichée/disponible, les coûts hors spread ni les émissions supplémentaires. Passer à plus de 8 questions modifierait la règle « 7 sur 8 » : décision à prendre.
- Points déjà signalés pour L0.02 et L0.03 (parts de la BRI totalisant 101 %, texte détaillé du FX Global Code, place de l'EUR/USD, etc.) : inchangés.

## 4. Sources effectivement consultées pour la révision 2 (29/10/2026)
- S-ECB-01 (BCE, « Financial structure ») : deux lectures.
- S-SEC-01 (SEC/DERA, 2017) : une lecture de contrôle des citations.
- S-BIS-01 (BRI, glossaire « Spot ») : lue lors de la rédaction initiale (même jour) ; non relue pour la révision.

## 5. Révision 3 de L0.01 (5 corrections finales)
| Vérification | Statut |
|---|---|
| Consultation visuelle du tableau BCE (total 34 395, six montants, périmètre, notes, écart d'1 Md€) | **NON EFFECTUÉE — en attente.** Tentatives : extension Chrome non connectée à la session ; curl vers ecb.europa.eu refusé (403). Les valeurs restent celles de deux lectures automatisées concordantes. |
| Écart d'1 Md€ (somme des lignes 34 396 vs total 34 395) | Constaté par calcul sur les valeurs lues ; origine (arrondis) non vérifiée sur le tableau original |
| Quiz L0.01 : fichier JSON lu en entier (huit questions, bonnes réponses, explications, seuil) | **Effectuée.** Une seule bonne réponse par question, explications cohérentes avec les réponses ; passThreshold 0,8 ; ⌈0,8 × 8⌉ = 7 ; la leçon dit « au moins 7 sur 8 ». Quiz inchangé. Remarque : l'explication de la Q6 cite trois dimensions de la liquidité (rapidité, taille, coût) alors que la leçon en décrit cinq ; non fausse, mais incomplète. |
| Calculs (Exemples A, B, D ; Exercices 1 à 6) | Script `verify_m00.py` relancé : voir sortie ci-dessous dans la réponse |
| Reformulation du marché primaire, de l'Exemple B/D (coût simulé vs coût réel), conclusion | Effectuées (relecture par l'auteur, pas d'avis indépendant) |

## 6. Mise à jour du statut de L0.01 après vérification indépendante du tableau BCE (29/10/2026)
| Point | Statut |
|---|---|
| Valeurs du tableau « Main financial liabilities of non-financial sectors in the euro area at end-2012 » (six montants et total 34 395 Md€) | **Vérifiées dans le contenu officiel accessible de la BCE.** Vérification indépendante rapportée par l'utilisateur ; je ne l'ai pas refaite moi-même (mes deux lectures automatisées concordaient déjà avec ces valeurs). |
| Consultation visuelle du tableau original | **NON réalisée** (ni par moi, ni indiquée comme faite dans la vérification rapportée). |
| Somme des six montants affichés | 34 396 Md€, contre un total publié de 34 395 Md€ (écart de 1 Md€). |
| Explication de l'écart par les arrondis | **Probable, mais non formellement confirmée.** |
| Contenu de la leçon, quiz, autres modules | **Non modifiés** à cette étape. |

**Statut recommandé de L0.01 : « Prête pour validation pédagogique ».** Elle reste non validée, non intégrée et non testée dans une interface ; relecture indépendante et lecture par un débutant restent à faire (voir section 3).

Note de cohérence : la table des sources de la leçon (`L0.01.mdx`) indique encore « vérification visuelle du tableau original en attente ». Cette formulation reste exacte pour la consultation visuelle mais ne mentionne pas la vérification indépendante ; elle n'a pas été modifiée, conformément à la consigne.

## 7. Révision 2 de L0.02 (29/10/2026) — corrections ciblées
| Point | Vérification / statut |
|---|---|
| BRI : page https://www.bis.org/statistics/rpfx25_fx.htm relue (outil de lecture web, résumé automatique) | Total 9,6 mille milliards (base « net-net »), 4,4 (46 %), 4,8 (50 %), clients non financiers 5 % sans montant publié. La page n'explique pas le 101 %. |
| Passage 4,4 + 4,8 vs 9,6 | **Corrigé** : comparaison partielle (deux catégories sur trois). L'écart 0,4 est une estimation calculée sur montants arrondis, du même ordre que 5 % × 9,6 ≈ 0,48 ; présenté comme approximation, non comme chiffre publié. Plage d'arrondi calculée : le résiduel se situe entre 0,25 et 0,55, la valeur 0,48 y est incluse. |
| 101 % | Explication par les arrondis conservée, prudente, sous réserve de la méthodologie officielle (non lue). |
| CFTC : communiqué 9316-26 (27/10/2026) et page de description | Lus le 29/10/2026. Plan de publication deux fois par semaine d'ici fin 2026 (lundi→mercredi, mercredi→vendredi, 15 h 30 ET), sans date de début ; la page de description décrit encore une publication hebdomadaire (mardi → vendredi). **Aucune preuve officielle que le nouveau calendrier soit en vigueur** ; page « Release Schedule » non lue. |
| Tenue de marché (400 $), Exemple A (hypothèses de couverture), transition vers l'or | Textes ajoutés ; **calculs inchangés** (400 ; 1 848 428,84 €), vérifiés par le script. |
| Quiz L0.02, L0.01, L0.03 | **Non modifiés.** Q6 (calendrier traditionnel) reste exacte mais ne couvre pas l'évolution annoncée. |
| Script `verify_m00.py` | Relancé : RÉSULTAT GLOBAL OK (trois contrôles ajoutés : écart 0,4, 5 % de 9,6, délai mardi → vendredi). |
| Relecture indépendante, lecture par un débutant | Non faites. |

## 8. Révision 2 du quiz L0.02 (30/10/2026) — 10 questions, seuil 8/10
Décision de l'utilisateur : version à 10 questions ; Q1 à Q3 conservées ; Q4 à Q8 retouchées ; Q9 et Q10 ajoutées.

| Contrôle | Résultat |
|---|---|
| Fichier `quiz/L0.02.quiz.json` : 10 questions, une seule bonne réponse chacune, identifiants uniques, explication présente | **Réussi** (script) |
| Seuil : 0,8 × 10 = 8 ; leçon §11 : « au moins 8 bonnes réponses sur 10 » | **Réussi** (script, cohérence quiz / leçon vérifiée aussi pour L0.01 et L0.03, inchangés) |
| Q1, Q2, Q3 : énoncé, options, bonne réponse, étiquettes identiques à la version précédente | **Réussi** (comparaison avec la sauvegarde de la version précédente). Explications enrichies (Q2 : revenu brut ; Q3 : origine des distracteurs). |
| Q4 : aucun chiffre dans les options (les parts sont dans l'énoncé) | **Réussi** (script) |
| Q6 : « calendrier traditionnel » dans l'énoncé ; champs `volatile` et `review_when` présents | **Réussi** (script) |
| Champs `skill`, `difficulty`, `sources`, `lessonRefs` présents ; sources toutes définies dans `sources.md` | **Réussi** (script) |
| Répartition des bonnes réponses : a 3, b 3, c 2, d 2 | Constatée (script) |
| Q4 à Q10 : bonne réponse strictement la plus longue | 0 question sur 7 (script, informatif) |
| Calcul Q3 (300 000 / 1,2 = 250 000 ; 300 000 / 1,08 = 277 777,78 ; 300 000 × 1,2 = 360 000) et Q9 (1 000 000 × 0,0004 = 400) | **Réussi** (script et calcul direct) |
| Calendrier CFTC (traditionnel / annoncé / date effective) | Revérifié le 30/10/2026 sur la page de description et le communiqué n° 9316-26 : traditionnel = publication hebdomadaire du vendredi ; annoncé = deux publications par semaine « d'ici la fin de 2026 » ; **date effective non confirmée**. Page « Release Schedule » non lue. |
| L0.01, L0.03 et leurs quiz | **Non modifiés** (octets identiques à l'archive précédente) |
| Relecture indépendante, test auprès d'un débutant, exécution dans une interface | **Non effectués** |

Points ouverts propres au quiz : Q6 à actualiser lorsque le nouveau calendrier de la CFTC sera officiellement appliqué ; la spéculation, l'allocation et le besoin de transaction ne sont pas évalués directement (Exercice 1) ; le caractère « difficile » de Q9 et Q10 est une estimation, non mesurée.

## 9. Validation de L0.02 par l'utilisateur (30/10/2026)
L'utilisateur a validé L0.02 (leçon révision 2, quiz révision 2 : 10 questions, seuil 8/10). État `validated` = true dans le registre. Inchangés : la leçon n'est ni intégrée ni testée dans une interface (aucun site), les points ouverts restent ouverts (Q6 à actualiser quand le nouveau calendrier de la CFTC sera officiellement appliqué ; aucune relecture indépendante ni test auprès d'un débutant). Cette validation ne concerne que L0.02 : L0.01 reste en attente de validation pédagogique, L0.03 n'a pas été examinée.

## 10. Validation globale du Module 0 pilote (30/10/2026)
À la demande de l'utilisateur (« valide tout »), L0.01 et L0.03 sont enregistrées comme validées par l'utilisateur, comme L0.02 (section 9). Précisions de fidélité :
- L0.01 : validée avec ses points ouverts — consultation visuelle du tableau BCE non réalisée (valeurs vérifiées dans le contenu officiel accessible, selon la vérification indépendante rapportée par l'utilisateur), définitions de cours non sourcées, terminologie « contrat à terme / forward / future » à harmoniser.
- L0.03 : validée **sans** avoir fait l'objet d'un audit détaillé comparable à celui de L0.01 et L0.02 ; ses points ouverts (parts de la BRI totalisant 101 %, place de l'EUR/USD non lue, etc.) restent ouverts.
- Aucune des trois leçons n'est intégrée ni testée dans une interface ; aucune n'a eu de relecture indépendante ni de test auprès d'un débutant.

## 11. Audit de L0.03 et actualisation des chiffres de la BRI (30/10/2026)
Autorisation de l'utilisateur : corrections 1 à 6 de l'audit ; chiffres de décembre 2025 retenus ; seuils et structure des quiz inchangés. Sauvegarde préalable : `backups/2026-10-30_avant-maj-BRI-decembre-2025/` (huit fichiers, copies identiques aux originaux au moment de la copie).

**Constat.** Les leçons L0.02 et L0.03 citaient les chiffres préliminaires de la BRI (page du 30/09/2025), qui annonçait elle-même des chiffres définitifs pour décembre 2025.

**Sources lues le 30/10/2026** (résumés automatiques, deux lectures concordantes pour chaque valeur reprise) : S-BIS-03 (*BIS Quarterly Review*, décembre 2025, tableau A.2, encadré C) et S-BIS-04 (tableaux détaillés : tableaux 1, 2 et 3, et la ligne par pays), plus S-BIS-02 relue. Les PDF n'ont pas été vus directement.

**Modifications.**
| Fichier | Modification |
|---|---|
| `L0.03.mdx` | Total 9 510 Md$ (+27 %) ; instruments 42 / 31 / 18 / 7 / 2 % avec montants publiés ; devises en montants publiés + pourcentages marqués « calcul de l'auteur » (dollar ≈ 89,1 %) ; règle des 200 % sourcée (note des tableaux) ; **classement des paires corrigé** (EUR/USD, USD/JPY, USD/CNY ; plus de « trois premières citées ») ; places financières : parts de septembre marquées préliminaires + contrôle de l'auteur sur les montants ; Exemple E, Exercice 5 et sa correction, résumé, limites et sources mis à jour |
| `quiz/L0.03.quiz.json` | Q5 : 18 % et 4 015 Md$ ; Q6 : explication sourcée ; Q7 : « environ 89 % » à la place de « 89,2 % », pourcentage marqué calcul de l'auteur. Seuil, nombre de questions (8) et réponses correctes inchangés |
| `L0.02.mdx` | §4.3 : 9 510 Md$, parts 47 / 49 / 5 % et montants 4 443 / 4 627 / 441 publiés ; **le 101 % est expliqué par un calcul de l'auteur** (parts exactes 46,7 / 48,7 / 4,6 %, toutes arrondies vers le haut) sans prétendre que la BRI l'ait expliqué ; l'écart « 0,4 » devient 440 ≈ 441 (clients non financiers) ; Exercice 3, erreurs courantes, résumé, sources |
| `quiz/L0.02.quiz.json` | Q4 uniquement (énoncé et explication) ; autres questions, seuil 8/10 et réponses inchangés |
| `content/sources.md` | S-BIS-03 et S-BIS-04 ajoutées ; S-BIS-02 marquée préliminaire ; calculs de l'auteur listés à part |
| `registry/lessons.json` | Sources, révisions, points ouverts, mention « nouvelle validation à confirmer » pour L0.02 et L0.03 |
| `verify_m00.py` | Contrôles BRI remplacés par les montants de décembre et les calculs de l'auteur ; contrôle des résidus préliminaires non étiquetés |

**Points d'honnêteté.**
- Le 101 % : explication par arrondi calculée par l'auteur à partir des montants ; la BRI indique seulement « Turnover and absolute change rounded » sous le tableau et ne commente pas ce total.
- Pourcentages par devise, par paire et par pays : calculs de l'auteur, présentés comme tels.
- Le rang de USD/CHF et de USD/HKD et la liste des autres paires n'ont pas été établis.
- « Définitif » : déduction ; la page de septembre annonçait les chiffres définitifs pour le numéro de décembre du Quarterly Review, mais le foreword ne le dit pas explicitement.
- La valeur 4 015 (swaps de change) est imprimée sans séparateur dans le tableau A.2 ; lue 4 015, seule valeur compatible avec le total ; confirmée par S-BIS-04 (4 015 293 M$).
- Aucune modification de L0.01, de ses fichiers, des seuils des quiz ni de la structure des quiz.

**Points ouverts.** Voir `registry/lessons.json` (entrées L0.02 et L0.03) : définitions de cours non sourcées de L0.03, parts géographiques publiées seulement en septembre, phrase sur les dix paires non revérifiée, aucune relecture indépendante, nouvelle validation de l'utilisateur à confirmer.

## 12. Phase 2 : audit de L0.01 et harmonisation forward / future (30/10/2026)
Autorisation de l'utilisateur : corrections A (L0.01) et B (L0.02, L0.03), plus harmonisation des formulations de L0.02 Q5 et L0.03 Q5. Sauvegarde préalable : `backups/2026-10-30_avant-phase2-forward-future/` (10 fichiers). Aucune sauvegarde supprimée.

**Constat.** L0.01 §7 distinguait correctement forward (gré à gré) et future (marché organisé), mais L0.02 employait « contrat à terme (*forward*) » (glossaire, Exemple A) et « contrats à terme » pour les *futures* de la CFTC, tandis que L0.03 employait « contrat à terme sec » sans lien explicite avec le forward de L0.01. Aucune erreur factuelle ; risque de confusion terminologique.

**Modifications.**
| Fichier | Modification |
|---|---|
| `L0.01.mdx` (révision 4) | Sources S-ECB-02, S-INV-01, S-CFTC-04, S-SEC-02, S-BIS-05 ajoutées avec leur portée (§4.2, 4.3, 4.5, 4.7, 7, 14) ; tableau comparatif forward / future ; explication du risque de contrepartie et de la compensation centralisée ; seuil BCE de « plus de deux jours ouvrés » présenté comme convention de définition ; simulation de défaillance (taux fictifs, 62 714,55 €, calcul de l'auteur) ; glossaire, limites, résumé et tableau de sources distinguent notions sourcées et définitions du cours ; réserve sur la vérification visuelle du tableau BCE **maintenue** |
| `L0.02.mdx` | Glossaire (« contrat de change à terme (*forward*) » + renvoi à L0.01 §7), Exemple A, §4.6, limites : *futures* nommés « contrats à terme standardisés » |
| `quiz/L0.02.quiz.json` (révision 4) | Q5 : énoncé précisé (« contrats à terme standardisés (*futures*) »). Réponse correcte (a), options, explications, seuil 8/10 inchangés |
| `L0.03.mdx` (révision 3) | §4.4 : le contrat à terme sec est identifié comme le forward de L0.01, distinct du *future* ; tableau des instruments et glossaire alignés ; sources S-ECB-02 et S-BIS-05 ; note sur les définitions du cours |
| `quiz/L0.03.quiz.json` (révision 3) | Q5 : option c libellée « Les contrats à terme secs (*outright forwards*, 18 %) ». Réponse correcte (a), seuil 7/8 inchangés |
| `content/sources.md` | Cinq sources ajoutées avec faits retenus et « ce que la source ne dit pas » |
| `registry/lessons.json` | Révisions mises à jour ; **L0.01, L0.02 et L0.03 à `validated` = false** avec `previous_validations` et `awaiting` |
| `verify_m00.py` | Contrôles ajoutés : plus aucune occurrence non qualifiée de « contrat à terme », éléments Phase 2 de L0.01 présents, simulation recalculée, Q5 inchangées, états du registre |

**Décision à signaler.** L0.01 avait été validée à la révision 3 ; comme la leçon a été modifiée (révision 4), le registre la remet en attente de validation, avec la trace de la validation antérieure. Vous n'aviez explicitement mentionné que L0.02 et L0.03.

**Points d'honnêteté.**
- Les cinq sources ont été lues par résumé automatique ; la page du glossaire d'Investor.gov n'a été lue que sur ses 100 000 premiers caractères (sur environ 119 000).
- Le seuil « plus de deux jours ouvrés » est la définition de la BCE ; je n'ai pas vérifié d'autres conventions.
- La définition CFTC du forward concerne les marchandises ; le bulletin de la SEC concerne le forex de détail. Leur application aux forwards de change d'entreprise est une extension du cours, signalée dans la leçon.
- Non sourcés (définitions du cours) : marché secondaire, marché de capitaux, spread, mid, profondeur, liquidité affichée / disponible, slippage, cinq dimensions de la liquidité, tableau §4.4.
- Vérification visuelle du tableau de la BCE : toujours **non réalisée**.
- Calendrier COT de la CFTC : inchangé ; l'application du nouveau calendrier reste non confirmée.
- Phases 3 et 4 non commencées. Archive `macromastery-m00-pilotes.zip` reconstruite après cette phase (29 fichiers dont les sauvegardes, test d'intégrité OK, contenu identique aux fichiers locaux).
