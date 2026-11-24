# Index des sauvegardes

Chaque sauvegarde est une copie complète de `content`, `registry` et `tools` à un instant donné ; elle contient donc **tous les modules existants à ce moment**, pas seulement celui indiqué. Les noms ne sont pas renommés (préservation de l'existant).

| Dossier | Contenu vérifié le 30/10/2026 | Rôle |
|---|---|---|
| 2026-10-30_avant-corrections-P1-P7 | fichiers à plat : leçons pilotes L0.01 à L0.03 (.mdx et quiz), lessons.json, rapport qualité, vérificateur | avant corrections P1–P7 (ancienne architecture, à plat) |
| 2026-10-30_avant-etape1-registre-150 | m00 (3 leçons pilotes) | avant le registre de 150 leçons |
| 2026-10-30_avant-maj-BRI-decembre-2025 | m00 (2 leçons) | avant la mise à jour BRI |
| 2026-10-30_avant-phase2-forward-future | fichiers à plat : leçons pilotes L0.01 à L0.03, lessons.json, sources.md, rapport qualité, vérificateur | avant la phase 2 (ancienne architecture, à plat) |
| 20261030_1042_fin_module0 | m00 : 10 leçons ; 1 examen | fin du module 0 |
| 20261030_1112_fin_module1 | m00–m01 : 22 leçons ; 2 examens | fin du module 1 |
| 20261030_1145_fin_module2 | m00–m02 : 34 leçons ; 3 examens | fin du module 2 |
| 20261030_1618_fin_module3 | m00–m03 : 46 leçons ; 4 examens | fin du module 3 |
| 20261030_1706_fin_module4 | m00–m04 : 58 leçons ; 5 examens ; banque de diagnostic amorcée | fin du module 4 |

Convention pour les prochaines sauvegardes : `AAAAMMJJ_HHMM_fin_moduleN`. Les modules 0 à 3 sont identiques dans les sauvegardes `fin_module3` et `fin_module4` (comparaison de fichiers faite le 30/10/2026) ; les leçons pilotes L0.01 à L0.03 sont identiques.
| 20261030_2329_fin_module5 | m00–m05 : 70 leçons ; 6 examens ; banque de diagnostic (m04, m05) | fin du module 5 |

Les modules 0 à 4 et les pilotes L0.01 à L0.03 sont identiques dans les sauvegardes `fin_module4` et `fin_module5` et dans l'état courant (comparaison de fichiers faite le 30/10/2026). L5.04 a été révisée (révision 2, correction des pondérations de l'indice large) : l'état antérieur n'est pas dans une sauvegarde de module, il est conservé dans backups/20261030_2329_fin_module5/_revisions/L5.04.rev1.mdx et la correction est consignée dans PRODUCTION_LOG.md.
| 20261031_0740_fin_module6 | m00–m06 : 78 leçons ; 7 examens ; banque de diagnostic (m04, m05, m06) | fin du module 6 |

Les modules 0 à 5 et les pilotes L0.01 à L0.03 sont identiques dans les sauvegardes `fin_module5` et `fin_module6` et dans l'état courant (comparaison de fichiers faite le 31/10/2026). Module 6 : L6.01 à L6.08, 4 quiz de chapitre, examen EX6, projet P6.
| 20261031_1043_fin_module7 | m00–m07 : 86 leçons ; 8 examens ; banque de diagnostic (m04–m07) | fin du module 7 |

Les modules 0 à 6 et les pilotes L0.01 à L0.03 sont identiques dans les sauvegardes `fin_module6` et `fin_module7` et dans l'état courant (comparaison de fichiers faite le 31/10/2026). Module 7 : L7.01 à L7.08 (L7.04, L7.05, L7.06 en révision 2 ; L7.08 en révision 2 avec correction des périmètres Futures Only / Combined ; versions antérieures dans `backups/_revisions_m7/`), 3 quiz de chapitre, examen EX7, projet P7, registre `registry/M7_DONNEES_INDISPONIBLES.md`.

| _revisions_decisions_1_3 | 84 fichiers avant modification (L8.05, 73 quiz des modules 0 à 7, verify_lessons.py, registres) ; MANIFEST_AVANT.sha256, MANIFEST_APRES.sha256, LISTE_73_QUIZ.txt | application des décisions 1 (= A) et 3 (= R1) du 31/10/2026 |
| _revisions_decisions_2_8 | 414 fichiers avant modification (content/m08, content/diagnostic, tools, registry, quiz et évaluations des modules 0 à 8, verify_m00.py) ; MANIFEST_AVANT.sha256, MANIFEST_APRES.sha256, LISTE_63_QUIZ_R1.txt | application des décisions 2, 4, 5, 6, 7, 8, extension de R1 et alignement des générateurs (23/11/2026) |
| _revisions_docs_relecture_essais | journal, journal de production, empreintes, points à vérifier, index (avant ajout des documents d'appui) ; MANIFEST_AVANT.sha256 | documents de relecture et d'essais (24/11/2026) |
| _revisions_sources_m08 | 9 fichiers avant modification (catalogue JSON et MD, registre des téléchargements, journal, anomalies, journal de production, empreintes, points à vérifier, index) ; MANIFEST_AVANT.sha256 | exécution de la décision 7 : téléchargement des sources du module 8 (24/11/2026) |
