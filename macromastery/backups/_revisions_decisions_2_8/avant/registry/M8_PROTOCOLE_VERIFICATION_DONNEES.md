# Protocole de vérification des données historiques — module 8

Date : 31/10/2026. Statut : **proposition, non exécutée** (aucune donnée n'a été téléchargée ni vérifiée par ce protocole). Il s'applique à l'or, au pétrole, au dollar, aux rendements et aux attentes préalables citées dans L8.01–L8.08, EX8 et P8. Les automatismes ne valident pas scientifiquement ; chaque étape produit une trace.

## 1. Principes

1. **Source de référence par type de donnée**, choisie avant la collecte et consignée ; en cas de plusieurs séries, aucune n'est choisie après avoir vu les écarts.
2. **Une valeur = un instrument, un horaire, une unité, une date de référence, une date de publication, une version** (millésime ou révision). Aucune comparaison entre fixings du matin et de l'après-midi, ni entre comptant et contrat à terme.
3. **Valeurs contradictoires conservées** (registre des anomalies) tant qu'une source supérieure n'a pas tranché ; la source qui tranche est citée.
4. **Aucune reconstitution** de prix manquant (interpolation, moyenne, valeur d'un instrument corrélé).
5. **Gel de l'information** : les attentes préalables ne comptent que si leur date de publication précède l'événement.
6. **Données non obtenues** : « non disponible » dans la leçon et dans le registre ; jamais d'estimation.
7. **Licence et conditions d'utilisation** vérifiées avant toute copie locale ; toute souscription payante est soumise à ton autorisation.

## 2. Données à vérifier et sources de référence proposées

| Donnée | Valeurs du module à vérifier | Source de référence proposée (à confirmer) | Alternatives / contrôle croisé | Anomalies liées |
|---|---|---|---|---|
| Or (XAU/USD) | Fixings LBMA AM/PM : 28/02/2022 (1 910 $ PM), 08/03/2022 (2 069 $), 31/03 (1 942 $), 30/09/2022 (1 672 $) ; 08/04 et 22/04/2025 AM (3 002,70 / 3 454,70 $) ; 30/10/2024 AM (2 783,95 $) ; 13 et 16/11/2001 (contrat de décembre COMEX, 278,60 / 275,30 $) ; moyennes mensuelles de 2008 (827 / 759 $) ; plus haut 2025 | Série LBMA Gold Price (AM/PM) officielle ; pour 2001 et 1990-91, série de bourse (CME/COMEX) ou archive officielle datée | WGC Goldhub (base de données), Fed de Saint-Louis (FRED) pour les séries LBMA si les droits le permettent | A3, A4, A5, A9, A13, A17-A19, A21-A22 |
| Pétrole | Brent 2022 (moyenne 100 $, 75 $ le 08/12, 85 $ le 30/12) ; plus haut en termes réels depuis 2014 le 08/03/2022 ; pétrole 1990 (≈ 22 / 21 $ avant l'invasion, pic ≈ 40 / 46 $, 26,70 $ le 23/10) | EIA (séries spot Brent et WTI, dites « Spot Prices ») ; pour 1990, EIA ou archive Fed (FRASER) | Banque mondiale (Pink Sheet), AIE | A10-A12 |
| Dollar | Indice du dollar (panier) pour les séances citées ; paires EUR/USD, USD/CHF mentionnées dans L8.05 ; part du dollar dans les réserves (COFER) | Fed (indice du dollar pondéré par le commerce, H.10) ; BCE pour les taux de change de référence ; FMI pour COFER | Cotations de banques centrales nationales | — |
| Rendements | 10 ans américain (−12 pb et −3 pb sont fictifs ; −40 pb au T1 2023 rapporté par le WGC), 2 ans, taux réels (TIPS), fourchettes cibles de la Fed | Trésor américain (taux de rendement quotidiens, Daily Treasury Par Yield Curve et Real Yield Curve) ; Fed (fourchette cible) | FRED pour accès commode | A14 (mars 2020), A31 |
| Attentes préalables | Consensus de la veille pour les décisions et publications, probabilités de marché (futures sur taux, sondages) citées ou absentes ; probabilités d'élection | Publications datées avant l'événement : calendrier officiel, sondages publiés, contrats à terme sur fonds fédéraux (CME) ; à défaut « non documentée » | Presse financière datée (étiquetée comme telle) | A4 (réaction à l'élection), L8.03 modèle jouet |

## 3. Procédure en huit étapes

1. **Inventaire** : extraire de chaque leçon la liste des valeurs numériques sourcées, avec l'ID de source et le paragraphe (script de recensement à écrire ; sortie : tableau CSV).
2. **Fiche de donnée** : pour chaque valeur, compléter instrument, horaire, unité, date de référence, date de publication, version.
3. **Obtention** de la série de référence : téléchargement après ton autorisation (voir section 6), stockage dans un dossier daté, empreinte SHA-256 du fichier.
4. **Rapprochement** : comparer la valeur de la leçon à la série ; classer **concordant** (écart < tolérance de l'unité), **écart explicable** (arrondi, horaire, version), **discordant**.
5. **Recalcul** des rendements et délais de la leçon à partir de la série (même instrument, même horaire) ; les calculs de l'auteur sont refaits indépendamment.
6. **Traitement des écarts** : conserver les deux valeurs, ouvrir ou mettre à jour l'anomalie ; ne corriger la leçon que par une révision documentée (version antérieure conservée).
7. **Attentes** : pour chaque événement, chercher la publication antérieure datée ; sinon inscrire « surprise non mesurable ».
8. **Clôture** : une anomalie ne se ferme que si la source supérieure est citée, lue en entier, rapprochée et consignée avec date de lecture.

## 4. Tolérances proposées (à valider)

Prix : égalité exacte à l'unité de cotation publiée (0,01 $ pour l'or LBMA) ; rendements calculés : 0,05 point de pourcentage ; délais : exacts ; valeurs rapportées arrondies : fourchette déduite de l'arrondi (comme dans L8.01).

## 5. Tests de cohérence automatiques (n'ont qu'une valeur de détection)

Dates valides et ouvrées de la place concernée ; horaires cohérents entre paires ; absence de rendement calculé entre instruments différents ; variation recalculée égale à celle affichée ; somme de composantes égale au total (cf. A6) ; unités (t, Md$, pb) ; séries sans trou sur les horizons annoncés « couverts ».

## 6. Décisions à soumettre avant toute exécution

Choix des sources de référence (section 2) ; autorisation de télécharger chaque fichier (nom, source, taille indiqués à l'avance) ; absence de coût (API payante interdite sans accord) ; stockage local des séries et respect des licences ; calendrier de la vérification (volume à établir par le recensement de l'étape 1 ; aucune estimation n'est avancée ici).

## 7. Limites

La vérification confirme l'accord avec une série de référence, pas la causalité ni la pertinence pédagogique. Les séries de 1990-91 et de 2001 peuvent n'exister que dans des archives ou des bases payantes ; dans ce cas, les horizons concernés restent « non couverts ».
