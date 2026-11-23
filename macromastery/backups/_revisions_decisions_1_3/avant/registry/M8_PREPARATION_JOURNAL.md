# Module 8 — Journal des modifications de la phase de préparation à l'intégration (31/10/2026)

Aucune leçon n'a été réécrite hors la modification documentée de L8.05 (révision 2). Aucun contenu n'a été supprimé. Toutes les versions antérieures sont dans `backups/_revisions_prep/` (et `backups/_revisions_m8/` pour les phases précédentes).

| # | Objet | Fichiers modifiés | Version antérieure conservée | Raison | Contrôle |
|---|---|---|---|---|---|
| 1 | Biais de longueur des 64 questions de quiz de leçon (A27) | tools/quizsrc/L8.01–L8.08.py (options réécrites ; énoncés, bonnes réponses et explications conservés), tools/quizsrc_rev2_m08.py (nouvelle source des options), content/m08/quiz/L8.0x.quiz.json (régénérés, révision +1) | backups/_revisions_prep/L8.0x.quizsrc.rev_before_prep.py et L8.0x.quiz.rev_before_prep.json | Audit du 31/10 : bonne réponse la plus longue dans 6 à 8 questions sur 8 ; rapport moyen 2,5–4,6 | tools/audit_quizzes_m08.py : rapport 1,07–1,27 ; résiduel 4 à 7 questions sur 8 encore les plus longues |
| 2 | Seuil des quiz de leçon (A30) | content/m08/quiz/L8.0x.quiz.json (passThreshold 0,875, passRule), tools/verify_lessons.py (contrôle du seuil = k/n affiché pour le module 8 ; modules 0–7 inchangés) | backups/_revisions_prep/verify_lessons.before_prep.py | Seuil stocké 0,8 ≠ 7/8 affiché | verify_lessons : 699/699 |
| 3 | Seuil des quiz de chapitre (même défaut que A30) | tools/make_assessment_m08.py (passThreshold 5/6, passRule), content/m08/assessments/chap_8.x.quiz.json, tools/verify_assessments_m08.py | backups/_revisions_prep/make_assessment_m08.before_prep.py | 5/6 ≈ 0,833 affiché avec 0,8 stocké | verify_assessments_m08 : 115/115 |
| 4 | Définition du « signal central » (A29) | content/m08/L8.05.mdx (révision 2 : définition ajoutée à la règle de verdict ; une phrase de l'exemple 6.1 précisée) | backups/_revisions_prep/L8.05.rev1_before_A29.mdx | Terme non défini dans la règle | verify_lessons L8.05 : 79/79 ; registry/lessons.json (révision 2, nouveau point ouvert) |
| 5 | Registre des anomalies | registry/ANOMALIES_M8.md (A27, A29, A30 : statut « corrigé » avec preuve ; A28 résiduel ; A34, A35 ajoutées) | backups/_revisions_prep/ANOMALIES_M8.before_prep.md | Documenter chaque correction sans fermer d'anomalie de données | — |
| 6 | Registres | registry/lessons.json (quiz_revision, quiz_pass_rule pour L8.01–L8.08 ; L8.05 révision 2), registry/PRODUCTION_LOG.md, POINTS_A_VERIFIER.md et EMPREINTES.sha256 (régénérés par consolidate.py) | — | Traçabilité | tools/consolidate.py exécuté |
| 7 | Nouveaux documents | registry/M8_SOURCES_A_LIRE.md ; registry/M8_PROTOCOLE_VERIFICATION_DONNEES.md ; registry/M8_GRILLE_AUDIT_EX8_P8.md ; registry/M8_RAPPORT_PREPARATION_INTEGRATION.md | (créations) | Points 4, 5, 6 et rapport demandés | Relecture |

Anomalies **non** modifiées : A1–A26, A31–A33 (données), A34, A35 ; L4.11, L5.08 et l'anomalie de périmètre CFTC restent ouvertes.

## Phase d'audit scientifique et pédagogique (31/10/2026, après décision de l'utilisateur)

| # | Objet | Fichiers | Sauvegarde / preuve | Remarque |
|---|---|---|---|---|
| 8 | Correction de l'URL de S-EIA-01 (id=51498 → 55079), références seulement | content/sources.md ; content/m08/L8.01.mdx ; content/m08/L8.02.mdx | backups/_revisions_audit/ (sources.before_audit.md, L8.01.before_url_fix.mdx, L8.02.before_url_fix.mdx ; MANIFEST_AVANT.sha256) ; SHA-256 après : sources.md 64ba5e7b…, L8.01 2b6426b5…, L8.02 a99bc72c… | Aucune révision de contenu ; verify_lessons 83/83 et 97/97 |
| 9 | Registre des anomalies mis à jour (A7, A15, A16, A20, A31–A33 : preuves partielles ; A34 corrigé en 73 quiz ; A36–A40 ajoutées ; A39 corrigée avec preuve) | registry/ANOMALIES_M8.md | backups/_revisions_audit/ANOMALIES_M8.before_audit.md ; SHA-256 après : 1676c828… | Aucune anomalie de données fermée sans lecture intégrale |
| 10 | Diagnostic initial M8 enregistré comme proposition | content/diagnostic/banque_m08.json ; tools/make_diagnostic_m08.py ; registry/assessments.json | SHA-256 banque : 0392cb77… ; assessments.json 6cff2430… | Statut « PROPOSITION — non validée, non intégrée » |
| 11 | Nouveaux scripts de lecture seule | tools/blind_audit_quizzes_m08.py ; tools/audit_thresholds.py | — | N'écrivent rien dans le contenu |
| 12 | Nouveaux documents | registry/M8_VERIFICATION_SOURCES.md ; M8_SIGNAL_CENTRAL_ANALYSE.md ; M8_AUDIT_QUIZ_AVEUGLE.md ; M8_SEUILS_QUIZ.md ; M8_PROPOSITION_BAREMES_EX8_P8.md ; M8_RAPPORT_AUDIT_SCIENTIFIQUE_PEDAGOGIQUE.md | — | Propositions en attente de décision |

Non modifiés dans cette phase : quiz (révision 2 conservée), EX8, P8, L8.05, seuils des modules 0 à 7, toutes les autres leçons.
