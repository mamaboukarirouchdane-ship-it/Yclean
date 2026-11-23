# MacroMastery Academy — contenus pilotes du module 0

Contenu de l'archive (aucun site, aucune dépendance, aucune clé API, aucun dépôt GitHub concerné) :

| Fichier | Rôle |
|---|---|
| `content/m00/L0.01.mdx`, `L0.02.mdx`, `L0.03.mdx` | Les trois leçons (texte Markdown/MDX, lisible dans n'importe quel éditeur de texte) |
| `content/m00/quiz/L0.0X.quiz.json` | Un quiz par leçon : 8 questions, bonne réponse (`correct`) et correction détaillée (`explanation`) |
| `content/sources.md` | Fiche des sources : URL, date de consultation, faits retenus, ce que chaque source ne dit pas |
| `registry/lessons.json` | Registre : états de chaque leçon (planifiée, rédigée, sourcée, évaluée, intégrée, testée, validée) et points ouverts |
| `verify_m00.py` | Script de vérification (calculs, quiz, structure, sources) |
| `RAPPORT_QUALITE.md` | Rapport de contrôle qualité : vérifications exécutées et vérifications restantes |

## Comment lire les documents
1. Décompresser l'archive.
2. Ouvrir `content/m00/L0.01.mdx` (puis L0.02, L0.03) avec un éditeur de texte. Les blocs `<details>` contiennent les corrections des exercices : le texte est lisible tel quel.
3. Ouvrir le quiz JSON correspondant : pour chaque question, `options`, `correct` (lettre de la bonne réponse) et `explanation`.
4. Consulter `content/sources.md` pour les sources, puis `RAPPORT_QUALITE.md`.

## Comment relancer les vérifications
Prérequis : Python 3 (aucun paquet à installer). Depuis le dossier `macromastery/` :

    python3 -I verify_m00.py

La dernière ligne doit afficher `RÉSULTAT GLOBAL: OK`. Le script ne lit que des fichiers locaux, n'écrit rien et n'utilise pas le réseau.

## Limites
Le script vérifie les calculs, la structure et la cohérence interne. Il ne vérifie pas la justesse des sources, la qualité pédagogique ni l'accessibilité des URL : voir `RAPPORT_QUALITE.md`.
