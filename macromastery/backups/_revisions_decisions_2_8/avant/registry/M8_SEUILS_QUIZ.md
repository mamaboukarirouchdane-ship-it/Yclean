# Seuils des quiz des modules 0 à 8 — audit et règle commune proposée

Date : 31/10/2026. Script : `tools/audit_thresholds.py` (lecture seule). **Aucune modification n'a été appliquée** aux modules 0 à 7 ; les quiz du module 8 avaient déjà été harmonisés (7/8 = 0,875 ; 5/6).

> **Mise à jour du 31/10/2026 — décision 3 = R1 appliquée.** Les 73 quiz du tableau ci-dessous portent désormais `requiredCorrect` (entier, ⌈0,8 × n⌉), `passThreshold = requiredCorrect / n` et `passRule`. Questions, bonnes réponses et explications inchangées. Les constats et le tableau ci-dessous décrivent l'état **avant** application et sont conservés tels quels. Contrôles : `tools/verify_thresholds_r1.py`, `tools/audit_thresholds.py` (0 écart), `tools/verify_lessons.py` (contrôle des modules 0 à 7 aligné). Non traités (hors du périmètre autorisé) : les 51 quiz restés à 0,8 sans écart (leçons des modules 0 à 3 et 2 quiz de 10 questions) et les 12 quiz du module 8, qui n'ont pas de champ `requiredCorrect` ; les générateurs `tools/make_quiz.py` et `tools/make_assessment_m00.py` à `m07.py` produisent toujours 0,8. Voir `registry/M8_PREPARATION_JOURNAL.md`, entrées 13 à 20.

## 1. Constat

- 136 quiz audités : 92 de 8 questions, 42 de 6 questions, 2 de 10 questions.
- Seuils stockés : 0,8 (124 quiz), 0,875 (8 quiz de leçon du module 8), 5/6 ≈ 0,833 (4 quiz de chapitre du module 8).
- **Aucun quiz n'a de nombre de bonnes réponses exigé incohérent** avec sa note : pour 0,8 × 8 = 6,4, il faut 7 bonnes réponses (⌈6,4⌉) ; pour 0,8 × 6 = 4,8, il en faut 5 ; pour 0,8 × 10 = 8, il en faut 8.
- **Écart numérique seul (73 quiz : 35 quiz de leçon des modules 4 à 7 et 38 quiz de chapitre des modules 0 à 7)** : seuil stocké 0,8 alors que la note affiche « 7 sur 8 » (= 0,875) ou « 5 bonnes réponses sur 6 » (= 0,833). **Correction d'un chiffre antérieur** : le nombre de 17 communiqué dans le rapport précédent provenait d'un contrôle qui ne lisait que la formulation « k sur n » ; le chiffre complet est 73. L'**effet pratique est identique** si l'application calcule ⌈seuil × nombre de questions⌉ ou compare la fraction obtenue au seuil (7/8 = 0,875 ≥ 0,8 ; 6/8 = 0,75 < 0,8). L'écart devient un risque seulement si l'application affiche le pourcentage stocké (80 %) à côté de « 7 sur 8 » ou compare des arrondis. C'est donc une **incohérence documentaire**, non une erreur de notation.

| Quiz | Module | Questions | Seuil stocké | Exigé (selon seuil stocké) | Affiché dans la note | Règle commune (⌈0,8 × n⌉) | Écart et correction proposée |
|---|---|---|---|---|---|---|---|
| L4.05 | m04 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L4.06 | m04 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L4.07 | m04 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L4.08 | m04 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L4.09 | m04 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L4.10 | m04 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L4.11 | m04 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L4.12 | m04 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.01 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.02 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.03 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.04 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.05 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.06 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.07 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.08 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.09 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.10 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.11 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L5.12 | m05 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L6.01 | m06 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L6.02 | m06 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L6.03 | m06 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L6.04 | m06 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L6.05 | m06 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L6.06 | m06 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L6.07 | m06 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L6.08 | m06 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L7.01 | m07 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L7.02 | m07 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L7.03 | m07 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L7.04 | m07 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L7.05 | m07 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L7.06 | m07 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| L7.07 | m07 | 8 | 0.8 | 7 sur 8 | 7 sur 8 | 7 sur 8 | même effet pratique; proposé : stocker 7/8 = 0.875 |
| chap_0.1 | m00 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_0.2 | m00 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_0.3 | m00 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_0.4 | m00 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_0.5 | m00 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_1.1 | m01 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_1.2 | m01 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_1.3 | m01 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_1.4 | m01 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_1.5 | m01 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_2.1 | m02 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_2.2 | m02 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_2.3 | m02 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_2.4 | m02 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_2.5 | m02 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_3.1 | m03 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_3.2 | m03 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_3.3 | m03 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_3.4 | m03 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_3.5 | m03 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_3.6 | m03 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_4.1 | m04 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_4.2 | m04 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_4.3 | m04 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_4.4 | m04 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_4.5 | m04 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_5.1 | m05 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_5.2 | m05 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_5.3 | m05 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_5.4 | m05 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_5.5 | m05 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_6.1 | m06 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_6.2 | m06 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_6.3 | m06 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_6.4 | m06 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_7.1 | m07 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_7.2 | m07 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |
| chap_7.3 | m07 | 6 | 0.8 | 5 sur 6 | 5 sur 6 | 5 sur 6 | même effet pratique; proposé : stocker 5/6 = 0.8333 |

Répartition des 73 écarts par module : m00 5, m01 5, m02 5, m03 6, m04 13, m05 17, m06 12, m07 10. **Effet pratique différent : 0 cas.** Les quiz du module 8 sont conformes (harmonisés le 31/10/2026).

## 2. Règle commune proposée

**Règle R1 (recommandée).** Nombre de bonnes réponses exigé = ⌈0,8 × n⌉. Il est **stocké comme un entier** (`requiredCorrect`) et le pourcentage affiché est calculé à partir de lui ; `passThreshold` = `requiredCorrect / n`. Résultat : 8 questions → 7 (87,5 %), 6 questions → 5 (83,3 %), 10 questions → 8 (80 %).
Avantages : conforme au seuil pédagogique de 80 % comme plancher ; identique à la pratique actuelle ; aucune ambiguïté d'arrondi ; aucun changement de réussite pour les apprenants.
Limite : la sévérité varie de 80 % à 87,5 % selon n.

**Règle R2 (alternative).** Nombre de questions uniforme (8 par quiz de leçon, 6 par chapitre) et exigence fixe (7/8 et 5/6). Plus simple à communiquer, mais impose de modifier les 2 quiz de 10 questions.

**Règle R3 (alternative moins stricte).** ⌈0,75 × n⌉ : 6/8, 5/6 (4,5 → 5), 8/10. Elle diminue l'exigence et modifierait la réussite de certains apprenants ; non recommandée sans essai.

## 3. Procédure d'application (après décision)

1. Sauvegarder chaque fichier avec empreinte SHA-256 dans `backups/_revisions_audit/`.
2. Ajouter `requiredCorrect` et `passRule`, mettre `passThreshold = requiredCorrect / n`.
3. Ne pas modifier les questions ni les clés.
4. Contrôler : script `audit_thresholds.py` (0 écart), puis `verify_lessons.py` (le contrôle des modules 0–7 devra être aligné ; il impose aujourd'hui 0,8 pour les modules antérieurs).
5. Journaliser, sans changement de statut « validé ».

## 4. Décision attendue

Choisir R1, R2 ou R3, et autoriser (ou non) l'application aux 17 quiz concernés (et au contrôle `verify_lessons.py` pour les modules 0–7). Rien n'est modifié en attendant.
