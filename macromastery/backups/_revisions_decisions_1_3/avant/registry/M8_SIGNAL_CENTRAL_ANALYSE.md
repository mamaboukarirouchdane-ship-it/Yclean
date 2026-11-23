# L8.05 — Le « signal central » : cas historiques, limites et révision proposée (non appliquée)

Date : 31/10/2026. Conformément à ta décision : la définition actuelle de L8.05 révision 2 est **conservée provisoirement comme convention pédagogique**, non comme règle scientifique. Ce document n'a modifié ni L8.05 ni aucune autre leçon.

## 1. Convention actuelle (rappel)

Matrice de six indicateurs fixés avant l'observation (VIX, S&P 500, rendement du 10 ans, dollar, franc suisse contre euro, or). Risk-off si score ≥ +4 et aucun signal central contredit ; risk-on si score ≤ −4 et aucun signal central contredit ; sinon « régime non tranché ». **Signaux centraux : VIX et S&P 500** ; un signal neutre ne contredit pas ; l'or n'est jamais central.

## 2. Cas historiques : la convention est-elle utile, ambiguë ou trompeuse ?

Seuls les faits consultés sont donnés comme tels ; le reste est marqué comme hypothèse ou « non évaluable ». Les chiffres de marché proviennent de résumés automatiques de pages web.

| Cas | Ce que montrent les données consultées | Verdict de la convention | Jugement | Statut des données |
|---|---|---|---|---|
| **13/03/2023, faillite de SVB** | VIX clôture 26,52 (plus haut intrajournalier 30,81) ; VIX9D 30,93, au-dessus du VIX (Cboe). Variation du S&P 500 non restituée ; rendement du 10 ans −40 pb au T1 2023 et or +8,5 % en mars (WGC, rapportés) | Le VIX est un signal confirmant (hausse de la volatilité) ; le S&P 500 n'est pas documenté ici | **Ambigu** : le stress est bancaire et de taux ; un indicateur d'actions peut ne pas le refléter. La convention ne dirait rien sur la composante bancaire | VIX vérifié par résumé ; S&P 500 non lu |
| **05/08/2024, pic du VIX** | Selon la BRI (bulletin 95), le VIX approche 66 en pré-marché (+180 %), un pic attribué à la cotation des dealers et à l'élargissement des écarts acheteur-vendeur sur options de vente, les ETF de volatilité n'étant pas le moteur principal | Le VIX contribuerait à un risk-off marqué | **Potentiellement trompeur** : l'indicateur de perception peut exagérer le stress réel quand l'écart de cotation s'élargit ; le S&P 500 est le garde-fou (clôture et variation non lues) | Pré-marché lu par résumé ; clôtures non restituées |
| **Mars 2020 (commentaire de gestionnaire)** | S&P 500 −13 %, or −10 % la semaine du 9 au 16 mars ; chiffres non sourcés, instrument de l'or non précisé (A14) | Si les chiffres étaient exacts, VIX et S&P 500 confirmeraient ; l'or contredit | **Utile** pour justifier l'exclusion de l'or du noyau : un régime risk-off peut coexister avec un or en baisse (liquidité) | Non vérifié ; ne prouve rien seul |
| **11-17/09/2001** | Fed −50 pb le 17/09 ; Dow −6 % intrajournalier (presse) ; VIX non lu | Non évaluable | **Non évaluable** | VIX et S&P 500 non lus |
| **Guerre du Golfe 1990-91** | Séries d'actions et de volatilité non lues | Non évaluable | **Non évaluable** ; la disponibilité d'un VIX comparable avant 1993 n'est pas documentée dans le module (à vérifier) | — |
| **Février 2022 (Ukraine)** | Or +6 % en février (WGC, rapporté) ; VIX et S&P 500 non lus | Non évaluable | **Non évaluable** | — |
| **Avril 2025 (droits de douane)** | Fixings LBMA du matin +15,1 % entre le 8 et le 22/04 ; VIX et S&P 500 non lus dans le module | Non évaluable | **Non évaluable** | — |
| **SIMULATION, exercice 3 de L8.05** | VIX +8,3 % (< seuil de +10 %) donc neutre ; cinq autres signaux confirment ; score +5 | Risk-off (aucun central contredit) | **Illustre la sensibilité aux seuils** : avec un seuil de +8 %, le VIX deviendrait confirmant et le score passerait de +5 à +6 ; à +9 % ou +10 % il resterait à +5 ; le verdict ne change pas ici, mais le décompte dépend du seuil | Fictif |

**Lecture.** Sur les cas dont les données sont consultables, la convention est utile pour exclure l'or du noyau et pour exiger la cohérence entre un indicateur de perception (VIX) et un indicateur de comportement (S&P 500) ; elle est ambiguë quand le stress n'est pas d'actions (bancaire, taux, liquidité) ; elle peut être trompeuse quand la volatilité implicite s'écarte du comportement des prix. **Quatre cas sur huit ne peuvent pas être évalués** faute de données lues : aucune conclusion de validité ne peut en être tirée.

## 3. Limites de la convention

1. **Biais d'actions et d'Amérique du Nord** : VIX et S&P 500 mesurent le marché américain des actions ; les stress de taux, de change, de crédit, de liquidité ou régionaux peuvent y être faiblement visibles.
2. **Redondance** : les deux signaux centraux sont corrélés par construction (le VIX est calculé sur des options sur le S&P 500) ; ils ne comptent pas comme deux informations indépendantes. Le noyau est plus étroit qu'il n'y paraît.
3. **Seuils arbitraires** (+10 %, −1 %, −5 pb, 0,3 %, 0,5 %) : aucun n'est calibré sur des données ; le décompte est sensible aux valeurs proches des seuils (voir la simulation).
4. **Horizon** : une séance, une semaine ou un mois n'ont pas la même lecture ; la convention ne fixe pas d'horizon universel.
5. **Neutre ne contredit pas** : cette règle autorise un verdict risk-off avec un signal central neutre, ce qui peut paraître trop tolérant.
6. **L'or exclu** : exclure l'or évite la circularité mais peut masquer des régimes où l'or est précisément l'enjeu.
7. **Aucune validation empirique** : aucun test sur un échantillon, aucun taux de faux positifs.

## 4. Risques de biais de sélection

- **Choix des indicateurs après observation** (data snooping) : choisir VIX et S&P 500 parce qu'ils « marchent » sur les épisodes connus ferait de la convention un habillage rétrospectif. Le désignation avant observation est la seule protection ; elle doit être **horodatée** par l'apprenant.
- **Choix des épisodes** : les cas du cours sont des épisodes marquants, donc non représentatifs (biais de survivance de l'attention).
- **Biais de confirmation** : tendance à retenir les cas où la convention « fonctionne ».
- **Biais rétrospectif** : connaissant l'issue, on classe plus facilement un signal comme utile.
- **Taille d'échantillon** : huit cas dont quatre non évaluables n'autorisent aucune généralisation.

## 5. Révision proposée (à valider avant toute modification)

**Option A — conserver** la convention telle quelle, en ajoutant à L8.05 une section « Limites de la convention » reprenant les points 1 à 7 et la mention « convention pédagogique, non validée » (révision 3, rédaction seule).
**Option B — élargir le noyau** à trois signaux de natures différentes (volatilité, actions, taux) en exigeant qu'au plus un contredise ; plus robuste aux stress de taux, mais change la règle.
**Option C — supprimer la notion de signal central** et ne garder que le score, avec une règle « au plus un signal contredisant ».
**Dans tous les cas** : ajouter un test de sensibilité des seuils (±20 %) ; exiger l'horodatage de la liste des signaux ; compléter les cas historiques par des séries lues (VIX, S&P 500) avant de les citer comme exemples d'application. Recommandation : **A à court terme**, puis réexamen après lecture des séries (voir le protocole de données).

## 6. Décision attendue

Choisir A, B ou C (ou conserver sans changement). Aucune modification de L8.05 n'a été faite dans cette phase.
