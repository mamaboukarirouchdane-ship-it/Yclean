# Module 8 — Rapport de préparation à l'intégration

Date : 31/10/2026. Phase de préparation uniquement : **aucun test d'intégration, déploiement, publication, installation, dépense ni modification du site**. Journal détaillé : `registry/M8_PREPARATION_JOURNAL.md`. Sauvegardes : `backups/_revisions_prep/`.

## 1. Corrections effectuées

| Demande | Résultat | Statut |
|---|---|---|
| 1. Biais de longueur des 64 quiz de leçon (A27) | Distracteurs réécrits pour 64 questions sur 64 ; énoncés, bonnes réponses et explications conservés ; positions équilibrées (2 par lettre). Rapport de longueur moyen ramené de 2,5–4,6 à 1,07–1,27 ; la bonne réponse reste la plus longue dans 4 à 7 questions sur 8 selon la leçon (44 sur 64 au total) | **Corrigé en grande partie, résiduel** ; relecture à l'aveugle requise |
| 2. A29, « signal central » | Définition ajoutée dans L8.05 (révision 2) : VIX et S&P 500, désignés avant l'observation ; or exclu pour éviter la circularité ; règle étendue au risk-on ; exemples vérifiés cohérents | **Corrigé** ; convention pédagogique non validée |
| 3. A30, seuil | Quiz de leçon : 0,875 = 7/8 ; quiz de chapitre : 5/6 ; `passRule` ajoutée ; contrôles alignés (le contrôle impose désormais seuil = k/n affiché pour le module 8) | **Corrigé pour le module 8** |
| 4. Sources à lire | `registry/M8_SOURCES_A_LIRE.md` : 25 lignes en 4 niveaux de priorité, URL exactes tirées de `content/sources.md`, informations à vérifier ; EO 14266 sans URL consignée | Livré |
| 5. Protocole de données | `registry/M8_PROTOCOLE_VERIFICATION_DONNEES.md` : principes, sources de référence proposées (or, pétrole, dollar, rendements, attentes), procédure en huit étapes, tolérances à valider | Livré, non exécuté |
| 6. Grille EX8/P8 | `registry/M8_GRILLE_AUDIT_EX8_P8.md` : constats arithmétiques, hypothèses de durée, 12 critères pour EX8, 10 pour P8 | Livré, non appliqué |

Constats utiles de la grille : le maximum des parties objectives d'EX8 est de 51/100, donc 19 points d'analyses suffisent pour atteindre 70 ; aucun seuil par section ; les pénalités de P8 peuvent atteindre −52 sans plafond global (score négatif possible). Les durées de 120 min et de 8 h ne sont pas mesurées.

## 2. Anomalies encore ouvertes (35 lignes dans ANOMALIES_M8.md)

- **A33 (critique)** : aucune source lue intégralement. **Reste ouverte.**
- **L4.11, L5.08, anomalie de périmètre CFTC** : critiques héritées, **restent ouvertes**, non utilisées dans le module 8.
- Anomalies de données **A1–A26 et A31–A32** : ouvertes, aucune valeur choisie arbitrairement, aucune fermée faute de preuve.
- **A27, A29, A30** : statut « corrigé » avec preuve ; validation pédagogique encore requise.
- **A28** (biais résiduel des quiz de chapitre) ; **A34** (17 quiz sur 86 des modules 0–7 avec seuil stocké ≠ k/n, non modifiés) ; **A35** (barèmes, seuils, durées d'EX8 et P8 non audités) : ouvertes.
- Points ouverts des leçons L8.01–L8.08 : 71 (70 + 1 ajouté à L8.05 sur la définition du signal central).

## 3. Sources à vérifier

Voir `registry/M8_SOURCES_A_LIRE.md`. En tête : directive 3 de l'OFAC (S-OFAC-02), communiqué du Trésor sur la directive 4 (S-UST-05), EO 14257, 14259, 14316 et **14266 (à identifier)**, communiqués de la Fed du 12/03/2023 et du 28/04/2023 et rapport complet sur SVB, conférence de presse de la BCE du 06/09/2012, **discours de Draghi (métadonnées seulement)**, chapitre 2 du GFSR (tronqué), Monetary Policy Report 2009 (tronqué), ERP 1991 (tronqué). Séries LBMA, EIA, Trésor et Fed à obtenir en version officielle pour remplacer les commentaires.

## 4. Contrôles réussis et échoués

Réussis à la date du rapport :
- Leçons L8.01–L8.08 : **699/699** ; ensemble du dépôt (91 leçons vérifiées) : **8 578/8 578**.
- Évaluations du module 8 : **115/115** (quiz 8.1–8.4, synthèses, examen EX8, seuils 5/6 et 7/8).
- Audit des quiz : positions équilibrées, explications ≥ 60 caractères, aucun doublon, 6 ou 8 questions, seuils conformes.
- `consolidate.py` : 487 points, 493 empreintes régénérées.

Échoués puis corrigés au cours de la session (conséquence de l'harmonisation des seuils) : contrôle « quiz seuil 0,8 » dans `verify_lessons.py` (8 leçons) et dans `verify_assessments_m08.py` (4 chapitres). Les deux contrôles ont été **modifiés pour exiger seuil = k/n affiché** ; ils n'ont pas été assouplis. Aucun échec ne subsiste.

Non réalisés (hors périmètre ou non autorisés) : lecture intégrale des sources, vérification contre les séries, essai chronométré d'EX8, essai de P8, relecture à l'aveugle des QCM, test sur téléphone, tout test d'intégration. **Les contrôles automatiques attestent la conformité technique, non la validité scientifique ni pédagogique.**

## 5. Décisions qui nécessitent ton autorisation

1. **Obtenir et lire les sources** : accord sur la liste de priorité 1 et 2, et sur la manière de lire intégralement (mes outils web ne renvoient que des résumés ; la lecture complète suppose des fichiers que tu me transmets ou une lecture de ta part).
2. **Télécharger des séries de prix** (LBMA, EIA, Trésor, Fed) : accord source par source, avec nom, origine et taille ; aucune souscription ni API payante sans accord.
3. **Accepter la définition du signal central** (VIX et S&P 500, or exclu) ou en choisir une autre ; elle est conventionnelle.
4. **Barèmes et seuils d'EX8 et P8** : ajouter ou non un minimum aux analyses et par section, un plafond de pénalités, et sur quelle base fixer la durée.
5. **Biais de longueur résiduel** : accepter, ou prévoir une relecture à l'aveugle et une nouvelle révision.
6. **Seuils des quiz des modules 0–7** (A34) : harmoniser ou laisser.
7. **Diagnostic initial du module 8** (non produit) : le produire ou non avant l'intégration.
8. **Lancement de l'intégration et des tests** : non engagé ; je n'ai besoin d'aucune décision pour rester en pause.

Le module 8 reste **rédigé, techniquement conforme, non validé scientifiquement**.
