---
name: memoire-conventions
description: Structure et conventions d'un mémoire de Master II à l'UJKZ / IBAM (option ISIE), tirées de mémoires soutenus et du modèle de l'encadrant. Utilise ce skill dès qu'il faut rédiger, compléter ou restructurer une partie du mémoire — page de garde, dédicace, remerciements, résumé, abstract, sigles, introduction générale, introduction ou conclusion de chapitre, revue de littérature, positionnement, conclusion générale, perspectives — ou vérifier qu'une partie contient ce qu'un jury attend, même si l'utilisateur ne parle pas de « conventions » (ex. « écris mes remerciements », « mon résumé est-il complet ? », « ajoute une transition à la fin du chapitre II »).
---

# Conventions du mémoire de Master (UJKZ / IBAM)

Ce skill dit **ce que chaque partie du mémoire doit contenir et dans quel ordre**. Pour la manière d'écrire (voix, temps, typographie), utilise le skill `memoire-style` ; pour juger une partie déjà écrite, `memoire-relecture`.

## D'où viennent ces règles, et quel poids leur donner

Par ordre d'autorité :

1. **Le canevas officiel** « Canevas de structure d'un mémoire », V1.0 du 26/09/2024 (résumé complet dans `references/canevas-officiel.md`). C'est la règle. En cas de conflit avec un mémoire modèle, le canevas l'emporte, sauf si l'encadrant a donné une autre consigne.
2. **Trois mémoires soutenus** (détail et exemples dans `references/modeles-analyses.md`) : — Sawadogo (UJKZ/IBAM, ISIE, 2023), Zongo (UJKZ/IBAM, SI, 2023), Nabi (UNB/ESI, 2022). Un jury les a acceptés : ce qu'ils ont **en commun** est une convention sûre.
3. **Un brouillon non soutenu** — Yaro (UJKZ/IBAM, ISIE, 2025), **même encadrant que l'auteur** (Dr Belko Abdoul Aziz DIALLO) et même modèle de document. Il révèle les attentes de l'encadrant (démarche QR/OS/H, revue critique). Ses apports sont des **recommandations fortes**, pas des règles validées en soutenance.

Quand tu proposes quelque chose qui vient seulement de Yaro, dis-le (« recommandé par le modèle de l'encadrant »). Ne reproduis jamais les défauts des modèles, même soutenus (voir la fin de ce fichier).

## Le projet LaTeX

- `main.tex` déclare les titres de chapitres, leurs `\label` et les `\input`. **Les fichiers `chapters/*.tex` ne contiennent jamais de `\chapter{...}`** (sinon titre en double et label dupliqué).
- Pièces liminaires dans `parts/` : `gard.tex`, `dedicace.tex`, `remerciements.tex`, `resume.tex`, `abstract.tex`, `sigle-abreviation.tex`.
- Chapitres : `introduction.tex`, `chapter1.tex` (cadre théorique et revue de littérature), `chapter2.tex` (matériel et méthodologie), `chapter3.tex` (conception et développement), `chapter4.tex` (résultats et discussion), `conclusion.tex`.
- Bibliographie : biblatex + biber, fichier `sanou-master.bib`.
- Travail restant signalé par `\TODOchapo{...}` (rouge) : ne jamais le remplacer par un chiffre inventé.
- Introduction et conclusion de chapitre : `\phantomsection`, `\section*{Introduction du chapitre}` / `\section*{Conclusion du chapitre}` et `\addcontentsline{toc}{section}{...}`.

Avant de rédiger, lis le fichier concerné et ceux qu'il résume (un résumé se rédige à partir des chapitres, pas de mémoire).

## Ordre des pièces

Ordre du canevas officiel : Page de garde → Dédicace → Remerciements → Résumé français → Résumé anglais (abstract) → **Table des matières → Liste des figures → Liste des tableaux → Liste des abréviations** → Introduction générale → chapitres → Conclusion → Bibliographie → **Annexes** (A1, A2…). Pagination romaine pour les pièces liminaires, arabe à partir de l'introduction.

Le canevas numérote l'introduction générale comme « Chapitre 1 » (revue = 2, méthodologie = 3, implémentation/évaluation = 4). Les mémoires soutenus et le brouillon de Yaro, postérieur au canevas, la laissent non numérotée. **Décision de l'auteur (2026-11-15) : l'introduction générale reste non numérotée** et les chapitres vont de I à IV, comme dans les mémoires soutenus. Ne signale plus cet écart et ne propose pas de renumérotation.

Le canevas autorise à **diviser la méthodologie en plusieurs chapitres** (c'est le cas ici : chapitre II « Matériel et méthodologie » et chapitre III « Conception et développement »), à condition de **garder un équilibre de pages entre chapitres** et d'adapter la numérotation.

## Taille et équilibre des chapitres

Le canevas demande un **équilibre de pages entre chapitres**. Un jury remarque vite un état de l'art de 23 pages suivi de résultats en 9 pages : le mémoire semble alors plus descriptif que productif. Les mémoires soutenus montrent que ce n'est pas un motif de refus (Nabi a 22, 9 et 9 pages), mais c'est une faiblesse visible qu'il vaut mieux corriger.

**Repères** (pages du PDF compilé, hors pièces liminaires et bibliographie) :
- aucun chapitre au-dessus de **1,5 fois** la moyenne des chapitres, aucun sous **la moitié** de cette moyenne ;
- le chapitre des **résultats ne doit pas être le plus court** des chapitres numérotés, car il porte la contribution ;
- **introduction générale** de 5 à 8 pages ;
- **conclusion générale** de 2 à 4 pages ;
- corps du mémoire (introduction à conclusion) d'environ **60 à 90 pages**, ordre de grandeur des modèles (Sawadogo 40, Zongo 75, Yaro environ 45 pour un brouillon).

**Mesure.** Après compilation, lance :

```bash
python .claude/skills/memoire-conventions/scripts/equilibre_chapitres.py main.toc
```

Le script lit la table des matières, donne les pages de chaque partie et signale les écarts aux repères. Mesure à nouveau après chaque ajout important, surtout pendant la phase d'implémentation, où le chapitre des résultats grossit.

**Rééquilibrer sans remplissage.** Ajouter du texte creux pour gagner des pages est pire que le déséquilibre, et contraire aux règles de `memoire-style`. Les bonnes façons de rééquilibrer sont :
- pour un chapitre trop long, déplacer en annexe ce qui est consultable mais pas nécessaire au raisonnement (définitions détaillées, inventaires, extraits de code ou d'ontologie, tableaux complets) et fusionner les définitions qui se recoupent ;
- pour un chapitre de résultats trop court, ajouter ce que le canevas exige et qui manque souvent : le dispositif expérimental, la description des données de test, l'analyse des erreurs par catégorie avec exemples, la confrontation explicite à chaque hypothèse, la comparaison aux travaux du chapitre I ;
- pour une conclusion trop courte, développer le bilan action par action et des perspectives concrètes, sans y mettre de résultat nouveau.

Propose toujours le rééquilibrage à l'auteur avant de déplacer du texte.

## Pièces liminaires

**Page de garde** — Université Joseph Ki-Zerbo, Institut Burkinabè des Arts et Métiers ; « Mémoire pour l'obtention du Master II en informatique » ; option ; thème ; « Présenté par » ; encadrant(s) **avec leur grade** (ex. « Maître de conférences ») ; période de stage si pertinente ; année académique.

**Dédicace** — très courte (2 à 4 lignes), alignée à droite ou centrée, adressée à des proches. Pas de phrase d'introduction du type « Je dédie ce travail à : ».

**Remerciements** — au « nous » académique, une phrase d'ouverture puis une liste dans **l'ordre hiérarchique** observé dans tous les modèles :
1. le directeur / l'encadrant de mémoire (nommé, avec ce qu'il a apporté) ;
2. la direction de l'institut, le corps professoral et administratif ;
3. le jury (« pour avoir accepté d'évaluer ce travail ») — présent chez Nabi et Yaro, à ne pas oublier ;
4. les structures ou personnes qui ont fourni données ou terrain ;
5. camarades, famille, amis, « tous ceux qui de près ou de loin ».
Chaque remerciement dit *pour quoi* on remercie, en évitant les formules creuses répétées.

**Résumé** — **150 à 250 mots** (consigne du modèle de l'encadrant), un seul bloc, dans cet ordre : contexte → problématique → méthodologie → principaux résultats **chiffrés** → limites/perspectives. Suivi de **4 à 8 mots-clés**. Il doit être compréhensible sans lire le mémoire et ne contient ni citation ni sigle non développé.

**Abstract** — traduction fidèle du résumé (mêmes chiffres, même ordre, mêmes limites), mots-clés traduits. Toute modification du résumé se répercute dans l'abstract, et inversement.

**Sigles et abréviations** — ordre alphabétique, deux colonnes (sigle / signification), développés en français avec l'original entre parenthèses si anglais. Vérifie que chaque sigle utilisé dans le texte y figure et qu'il n'y a pas de doublon.

## Introduction générale

Le canevas impose quatre rubriques : **Contexte et motivation** ; **Problématique et hypothèses** (ou questions de recherche), formulées clairement ; **Objectifs** (général, puis spécifiques détaillés et exhaustifs) ; **Organisation du mémoire** (contenu synthétique de chaque chapitre). Les mémoires modèles permettent d'aller plus loin :

1. **Contexte** (justification et motivation) — du général au Burkina Faso, chiffres sourcés.
2. **Problématique** — le manque précis, aboutissant à une **question de recherche** formulée comme une question.
3. **Questions de recherche spécifiques** (QR1, QR2…) — recommandé par le modèle de l'encadrant.
4. **Objectif général** puis **objectifs spécifiques** (OS1, OS2…), chacun évaluable et rattaché à une question.
5. **Hypothèses** (H1, H2…) — une par question, **réfutables** : elles disent ce qui sera observé et comment on le saura (pas « l'approche X est efficace » sans critère).
6. **Méthodologie / démarche** en étapes numérotées (résumée ; le détail va au chapitre II).
7. **Organisation du document** — un paragraphe ou une puce par chapitre.

Si le mémoire pose une définition de travail de l'objet étudié, elle peut apparaître dès l'introduction et renvoyer au chapitre I.

## Chapitres

Chaque chapitre :
- **s'ouvre** sur une introduction de 3 à 6 phrases qui annonce ce que le chapitre fait et dans quel ordre ;
- **se ferme** sur une conclusion qui (a) fait le bilan de ce qui a été établi, (b) en tire la conséquence pour la suite, (c) **annonce le chapitre suivant** en une ou deux phrases. Cette transition est présente dans tous les modèles ; c'est l'élément le plus souvent oublié.
- relie les sections par des phrases de transition (« Après avoir défini…, il convient d'examiner… »).

### Revue de littérature (chapitre I)

Le canevas demande deux volets distincts, puis une synthèse :
1. **Concepts et théories** nécessaires pour comprendre le travail ;
2. **Plateformes et outils existants** en lien avec le sujet (des systèmes concrets, nommés, et pas seulement des familles de systèmes), avec **leurs forces et leurs faiblesses** ;
3. **Travaux de recherche** (articles scientifiques) liés à la problématique, avec une **analyse de leurs résultats qui fait ressortir leurs limites** par rapport au travail ;
4. **Synthèse** de l'état de l'art : discussion, forces, faiblesses.

Ne pas enchaîner des « Dans [7], les auteurs… » sans analyse (défaut de Sawadogo et Zongo). Un exemple rédigé de cette construction se trouve dans `memoire-style`, section « Paragraphe de revue critique ». Pour chaque travail : auteurs et année → données et contexte → méthode → résultat chiffré → **limite au regard du contexte de l'étude** (« Cependant… »). Puis :
- un **tableau de synthèse comparative** (travail, année, contexte, données, méthode, résultat) ;
- une sous-section **limites des travaux existants** ;
- un **positionnement** explicite, placé **après** le tableau : ce que l'étude reprend, ce qu'elle fait autrement, et pourquoi. C'est le seul endroit de la revue où l'on annonce une décision ; la présentation de chaque travail reste factuelle (le passage « Suivant l'approche de [7]… Contrairement à… » de Sawadogo est le bon modèle).

### Matériel et méthodologie (chapitre II)

Le canevas en fait **la partie la plus importante du mémoire** : la démarche doit être **schématisée** (algorigramme, diagramme, architecture) et **la contribution présentée clairement**, chaque étape décrite de façon à montrer la pertinence des choix.

Corpus ou données (origine, période, critères de sélection, volume), outils et **justification des choix** (tableau comparatif quand il y a des alternatives), démarche en phases, protocole d'évaluation (métriques, jeu de test) **défini avant** les résultats.

### Conception et développement (chapitre III)

Architecture (figure), modèles (ontologie, données), implémentation, outils, captures d'écran légendées. Les figures produites par l'auteur portent « Source : nous-mêmes » ou équivalent ; les autres citent leur source.

### Résultats et discussion (chapitre IV)

Le canevas (« Implémentation / Expérimentation / Évaluation ») exige ici : le processus d'implémentation et la **justification des choix**, **l'environnement matériel et logiciel** (le dispositif expérimental : machine, GPU ou Colab, versions des logiciels et des modèles), **les données utilisées** pour l'expérimentation, puis la présentation, l'analyse et **l'interprétation** des résultats. Comme l'implémentation est décrite au chapitre III, le dispositif expérimental peut y figurer, mais il doit exister quelque part sous ce nom.

#### Dispositif expérimental : environnement matériel et logiciel

Exigence explicite du canevas et de l'auteur. Un jury doit pouvoir **reproduire** l'expérience et juger si les temps de réponse sont comparables. Une mention vague (« un GPU », « Neo4j », « Python ») ne suffit pas : chaque élément est nommé **avec sa version ou sa caractéristique précise**. Présente-le dans une sous-section dédiée, intitulée par exemple « Dispositif expérimental », avec un ou deux tableaux.

À couvrir, pour chaque machine réellement utilisée :
- **Matériel** : type de machine (ordinateur personnel, Colab, serveur), processeur, mémoire vive, **GPU avec son modèle et sa mémoire** (ex. NVIDIA T4, 16 Go), système d'exploitation et version.
- **Logiciels** : version de Python, de Neo4j, d'Ollama, de Protégé et du raisonneur, de Streamlit, de LangChain et des bibliothèques clés. Le numéro exact est relevé avec `pip show`, `ollama --version` ou le menu « À propos ».
- **Modèles de langue** : identifiant exact (ex. `llama3:8b`), taille, **quantification**, fenêtre de contexte, température et paramètres de génération, fournisseur et **période d'utilisation** pour les modèles accessibles par API (leurs versions évoluent).
- **Répartition** : quelle étape tourne sur quelle machine (extraction, peuplement, génération, interface, évaluation).
- **Conditions de mesure** : réseau ou tunnel utilisé, nombre d'exécutions, ce qui peut influer sur les temps (session Colab partagée, démarrage à froid).

Toute valeur inconnue s'écrit `\TODOchapo{version de … à relever}`. Une version ne s'invente jamais, et une version « probable » ne remplace pas la valeur relevée.

Résultats chiffrés par question de recherche, puis discussion : confrontation aux hypothèses (validée, partiellement, non), comparaison avec les travaux du chapitre I, **limites** de l'étude. Les conclusions ne dépassent pas ce que les mesures montrent.

## Conclusion générale

Le canevas demande deux choses : **le bilan des principales actions réalisées** et **les perspectives**. Rappel du problème et de l'objectif → démarche suivie → principaux résultats chiffrés → réponse à chaque question / statut de chaque hypothèse → limites → **perspectives** concrètes. Pas de résultat nouveau qui n'apparaîtrait pas au chapitre IV.

## Défauts des modèles à ne pas reproduire

- Bibliographie faite d'URL « [En ligne] » sans auteur ni date (Sawadogo, Zongo) : utiliser de vraies références biblatex.
- Superlatifs non démontrés (« performance exceptionnelle », « révolutionner »).
- Revue de littérature purement descriptive, sans critique ni positionnement.
- Hypothèses non réfutables, objectifs non évaluables.
- Éléments de brouillon laissés : « Rédigez ici… », « Prénom NOM », « figure ?? », sigle cassé.
- Fautes d'accord et de frappe ; numérotation des tableaux qui saute (Tableau 6 → 8 chez Sawadogo).
