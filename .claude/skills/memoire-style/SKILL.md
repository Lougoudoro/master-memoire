---
name: memoire-style
description: Voix académique et règles d'écriture du mémoire de Master de Sanou Lougoudoro (OntoPlantMedBF, LaTeX, français). Utilise ce skill chaque fois qu'il faut écrire, réécrire, reformuler, raccourcir, harmoniser, corriger le français ou « rendre plus académique » un passage du mémoire, traduire le résumé en abstract, ou rédiger un nouveau paragraphe dans chapters/ ou parts/ — même pour une seule phrase, et même si l'utilisateur dit simplement « améliore ce paragraphe » ou « c'est mal dit ».
---

# Style du mémoire

Ce skill fixe **comment écrire**. Ce que chaque partie doit contenir relève de `memoire-conventions` ; l'évaluation critique d'un passage, de `memoire-relecture`.

L'objectif est que tout texte produit soit indiscernable de ce que l'auteur écrit déjà de mieux : son texte actuel est la référence, pas un style générique d'IA ni celui des mémoires modèles (qui ont des défauts relevés plus bas).

## La voix de l'auteur

Observée dans `chapters/chapter1.tex`, `chapters/chapter4.tex` et `parts/resume.tex` :

- **« Nous » académique**, accords au pluriel de modestie (« nous avons retenu », jamais « j'ai »). Seule la dédicace peut être à la première personne du singulier.
- **Phrases courtes à moyennes**, une idée par phrase. Si une phrase dépasse ~35 mots ou enchaîne trois subordonnées, coupe-la.
- **Ton vivant mais sobre** : des verbes d'action précis (« recense », « documente », « restitue ») plutôt que « permet de » répété.
- **Chaque chiffre est sourcé ou mesuré** : « environ 80 % des besoins de santé primaire \cite{ares2018medecine} », « un F1-score de 0,728 ».
- **Prudence explicite** : l'auteur dit ce qui n'a pas été fait (« elle n'a pas été évaluée auprès d'utilisateurs », « les extractions n'ont pas été relues par un expert »). Conserve et imite cette honnêteté ; c'est le point fort du mémoire face aux modèles.
- **Pas de superlatif non démontré** : bannis « exceptionnel », « révolutionnaire », « parfaitement », « crucial » répété, « de nombreux » sans nombre.

Exemple de la voix à imiter :
> Or ces savoirs ne se présentent pas de façon homogène. Ils varient selon les ethnies, diffèrent selon les régions, et s'enrichissent des découvertes nouvelles.

## Exigences absolues de l'auteur

Ces cinq règles passent avant toutes les autres. L'auteur les a posées explicitement : un texte qui les enfreint n'est pas livrable, même s'il est juste sur le fond. Après chaque rédaction ou réécriture, lance le contrôle automatique (voir plus bas) et corrige ce qu'il signale avant de livrer.

### 1. Aucune trace d'IA

Un jury repère vite un texte généré : il est lisse, symétrique, plein de formules toutes faites et ne dit rien de précis. Pour l'éviter :
- **Bannis les tournures stéréotypées** : « il est important de noter », « il convient de souligner », « joue un rôle crucial / essentiel / clé », « dans un monde en constante évolution », « à l'ère du numérique », « véritable », « enjeu majeur », « pierre angulaire », « levier », « en somme », « en définitive », « force est de constater », « non seulement… mais aussi », « s'inscrit dans une démarche de », « offre une solution innovante », « permet de » répété dans un paragraphe. La liste complète est dans `scripts/verifier_style.py`.
- **Pas de triplets réflexes** (« clair, précis et efficace ») ni d'énumérations de trois éléments à chaque phrase.
- **Varie la longueur des phrases** : une suite de phrases toutes de même longueur et de même structure trahit la génération.
- **Pas de connecteur en tête de chaque phrase.** « Ainsi », « En effet », « De plus » au début de deux phrases consécutives sont à supprimer.
- **Pas de tiret cadratin (—)** pour insérer une idée, pas de gras décoratif dans la prose.
- **Du concret plutôt que du général.** Chaque phrase doit porter un fait, un chiffre, un nom ou un choix de l'auteur. Une phrase qui pourrait figurer dans n'importe quel mémoire est à supprimer ou à préciser.
- **Pas de paraphrase de conclusion** à la fin de chaque paragraphe (« Cela montre l'importance de… »).

### 2. Aucun plagiat

- Toute idée, définition ou donnée reprise d'une source est **reformulée réellement** (structure et vocabulaire différents, pas une permutation de mots) **et citée** avec `\cite{}`.
- Une formulation reprise mot pour mot est une citation : entre `\enquote{…}`, courte (une phrase au plus), avec la page `\cite[p.~12]{clé}`. Pas plus d'une citation littérale par section.
- **Ne réutilise jamais une phrase des mémoires modèles** (Sawadogo, Nabi, Zongo, Yaro) : ils servent à comprendre la structure, pas à fournir du texte. Les exemples de `memoire-conventions` sont des descriptions, pas des phrases à recopier.
- Ne traduis pas un passage anglais phrase à phrase : lis, comprends, puis écris à partir de ce que tu as compris.
- Ce que tu écris doit venir des données de l'auteur (chapitres, fichiers du dépôt), pas de connaissances générales présentées comme les siennes.

### 3. Pas de phrases trop longues

- **25 mots au maximum par phrase** en règle générale, **30 au grand maximum** et seulement si la phrase reste limpide. La moyenne d'un paragraphe doit rester autour de 15 à 20 mots.
- Une phrase ne porte qu'une idée. Coupe au niveau des « et », « qui », « dont », « afin de » qui enchaînent une deuxième idée.

### 4. Pas de deux-points dans la prose

- **N'emploie pas « : » dans les phrases rédigées.** Remplace-le par un point, par « car », « donc », « ainsi », ou par une construction directe (« Llama 3 8B traduit la question en requête Cypher. Cette requête est validée… »).
- Tolérance : avant une liste `itemize` qui l'introduit, et dans les étiquettes de puces existantes (`\textbf{… :}`). N'en crée pas de nouvelles si une phrase complète peut faire le même travail.
- Pas de « : » en milieu de titre de section non plus.

### 5. Peu de parenthèses

- **Une parenthèse par paragraphe au maximum**, réservée au développement d'un sigle à sa première occurrence ou à une précision indispensable (unité, nom latin).
- Une information qui mérite d'être dite s'intègre dans la phrase ; sinon elle est supprimée. Pas de parenthèses imbriquées, pas de liste d'exemples entre parenthèses.

## Temps verbaux

- **Ce que le mémoire fait ou montre** : présent (« Ce chapitre présente… », « L'ontologie compte 92 classes »).
- **Ce qui a été réalisé** (corpus, extraction, évaluation) : passé composé (« Nous avons comparé cinq ontologies »).
- **Annonce de plan** : futur ou présent acceptés (« Le chapitre suivant présentera… »).
- **À trancher avec l'auteur** : l'introduction générale décrit aujourd'hui le travail au futur (« nous mettrons en place », « Notre objectif général sera »). Pour un mémoire terminé, le présent est plus juste. Signale-le, ne réécris pas toute l'introduction sans accord.
- Une fois un temps choisi pour une section, garde-le dans toute la section.

## Preuves et affirmations

- Une affirmation factuelle sur le domaine porte une citation `\cite{clé}` existant dans `sanou-master.bib`. Vérifie la clé avec une recherche dans le .bib ; si aucune ne convient, écris `\TODOchapo{citation à trouver : …}` au lieu d'inventer une référence.
- Une affirmation sur les résultats renvoie à un chiffre du chapitre IV. **N'invente jamais de chiffre** ; s'il manque, laisse ou ajoute un `\TODOchapo{…}`.
- Pour une définition ou un chiffre repris d'un ouvrage, donne la page si elle est connue : `\cite[p.~12]{clé}` (pratique recommandée par le modèle de l'encadrant).
- Ne présente pas comme réalisé ce que le dépôt ne prouve pas (voir `rapport-croise-redaction-graphrag.md`).

## Pas de fichiers locaux dans le texte

Le lecteur et le jury n'ont que le PDF. Ils ne voient ni le dépôt, ni les dossiers, ni les scripts. Un nom de fichier local ne leur apprend donc rien et donne au texte l'air d'un rapport technique interne.

- **Ne cite pas les fichiers et chemins locaux** dans le texte visible : `ontoMEDTRAD-faits.xlsx`, `registre-validation-corpus.xlsx`, `ttl_import.py`, `app.py`, `main.tex`, `corpus/`, `GraphRAG/application/…`, noms de CSV ou de notebooks.
- **Décris plutôt ce que contient ou fait le fichier.** Par exemple, « le registre de validation du corpus » au lieu de `registre-validation-corpus.xlsx`, ou « le programme d'import » au lieu de `ttl_import.py`.
- **Exception : l'ontologie OntoPlantMedBF**, livrable du mémoire. On peut la nommer, et mentionner son format Turtle. Son nom est préférable à son nom de fichier quand les deux conviennent.
- Les commentaires LaTeX (`% Source : …`) peuvent garder les chemins, car ils n'apparaissent pas dans le PDF.
- Dans un extrait de code ou une commande, évite aussi les chemins propres à ta machine. Si un dépôt public existe, cite-le par son adresse dans la bibliographie ou en annexe.

## Paragraphe de revue critique

Une revue de littérature ne résume pas les travaux un par un. Pour chaque travail, elle dit **ce qu'il fait**, puis **ce qu'il ne permet pas dans le contexte de l'étude**, et enfin **ce qu'il apporte malgré tout**. C'est la construction du brouillon de Yaro, qui en est le meilleur apport, mais sans ses défauts d'écriture (phrases de plus de 30 mots, « : » à répétition, sigles anglais entre parenthèses).

Trois temps, en deux paragraphes courts :
1. **Le travail** : auteurs et citation, objectif, données ou terrain, méthode, chiffres clés.
2. **La limite pour l'étude** : ce qui manque au regard du Burkina Faso, du corpus ou de la traçabilité. Cette limite doit être vérifiable, et non une opinion.
3. **L'apport** : ce que le travail couvre des besoins de l'étude, constaté de façon factuelle.

**Pas de décision dans la présentation d'un travail.** À ce stade, le lecteur n'a pas encore vu le tableau comparatif. Annoncer « nous avons retenu… » anticiperait une conclusion que la revue doit d'abord établir. La décision se place donc après le tableau de synthèse, dans la section « Positionnement ». Le choix méthodique de l'ontologie, avec sa grille de critères et sa notation, relève du chapitre II.

Exemple construit avec les faits du chapitre I (`chapters/chapter1.tex`, §ontoMEDTRAD). Il montre la construction et ne doit pas être recopié ailleurs. Il passe le contrôle de style sans alerte :

> Kouamé et ses collègues ont conçu \textit{ontoMEDTRAD} pour la médecine traditionnelle ouest-africaine \cite{kouame_systeme_2018}. L'ontologie associe un module terminologique à un module d'icônes destiné aux tradipraticiens peu alphabétisés. Elle décrit le parcours de soin, du praticien au remède, avec 144 concepts, 789 individus et 2~734 axiomes. Son jeu de données réunit 22 plantes et 31 remèdes antipaludéens, recueillis en Côte d'Ivoire et au Sénégal \cite{kouame_visual_2020}.
>
> Ce modèle reste toutefois difficile à employer tel quel au Burkina Faso. Il ne prévoit ni les noms en mooré, en dioula ou en fulfuldé, ni le niveau de preuve d'un usage. Il ne rattache pas non plus chaque fait à la publication qui le rapporte. C'est pourtant ce qu'exige un accès traçable à la littérature scientifique. Sa description du parcours de soin correspond en revanche aux usages, recettes et préparations rapportés dans notre corpus.

À noter dans cet exemple :
- chaque phrase porte un fait, et aucune n'est générique ;
- la limite découle des besoins de l'étude, et non d'un jugement de valeur ;
- la dernière phrase constate un apport sans annoncer de choix, qui viendra au positionnement puis au chapitre II ;
- les phrases font 12 à 24 mots, sans « : » ni parenthèse.

## Transitions

- Entre sections : une phrase qui ferme et ouvre (« Après avoir défini les plantes médicinales, il convient d'examiner la manière dont ces savoirs sont structurés. »).
- Connecteurs variés et logiques : *or, en effet, toutefois, ainsi, de ce fait, en revanche, par ailleurs*. Évite d'ouvrir trois paragraphes de suite avec le même.

## Typographie et LaTeX

- Pourcentages : `80\,\%` ; grands nombres : `6~936` ; décimales à virgule en français (0,728), à point en anglais (0.728).
- Espace insécable avant référence ou unité : `Figure~\ref{…}`, `50~questions` si la coupure gêne.
- Guillemets français : `\enquote{…}` (csquotes) ou « … ».
- Noms d'ontologies, de logiciels étrangers et termes latins en `\textit{}` (\textit{ontoMEDTRAD}, \textit{in vitro}) ; noms d'espèces en italique.
- Sigles : développés à la première occurrence (« génération augmentée par récupération (RAG) »), puis employés seuls ; chacun présent dans `parts/sigle-abreviation.tex`.
- Listes `itemize` avec `[label={$\bullet$}, leftmargin=1cm]` comme dans le reste du texte ; une puce = une phrase complète terminée par « ; », la dernière par « . ».
- Ne touche pas aux `\label`, `\ref` et clés `\cite` existants sauf demande.

## Français : fautes fréquentes à corriger

Relevées dans les mémoires modèles et typiques du registre :
- accords (« les données collectées », « les résultats obtenus ») ; « peu concluant » et non « peut concluant » ;
- « à l'endroit de » (formule locale acceptée dans les remerciements, à éviter ailleurs) ;
- anglicismes : « data scientists » → « spécialistes des données », « performer » → « être performant », « implémentation » acceptable en informatique ;
- « malgré que » → « bien que » ; « au niveau de » vague → préposition précise ;
- « cinq (5) » : la forme chiffre entre parenthèses est un usage administratif ; garder le nombre en lettres ou en chiffres, pas les deux.

## Résumé ↔ abstract

L'abstract traduit fidèlement le résumé : mêmes chiffres (séparateurs anglais : 6,936 ; 0.728), même ordre, mêmes limites, « Keywords: ». Après toute modification de l'un, mets l'autre à jour et dis-le.

## Contrôle automatique

Après chaque rédaction ou réécriture, lance :

```bash
python .claude/skills/memoire-style/scripts/verifier_style.py <fichier.tex> [autres fichiers…]
```

Le script signale, avec leur ligne, les phrases de plus de 25 mots (alerte au-delà de 30), les deux-points dans la prose, les paragraphes avec plus d'une parenthèse, les formules typiques de l'IA, les connecteurs répétés en tête de phrase, les tirets cadratins et les noms de fichiers locaux visibles dans le PDF (OntoPlantMedBF excepté). Il ne remplace pas la lecture, mais rien ne doit être livré tant qu'il signale une alerte que tu n'as pas justifiée. Pour vérifier un texte qui n'est pas encore dans un fichier, écris-le d'abord dans le dossier temporaire (scratchpad), puis lance le script dessus.

## Manière de livrer

- Pour une réécriture, montre l'**avant / après** (ou applique l'édition dans le fichier si l'utilisateur l'a demandé) et explique en une ligne chaque changement non évident.
- Conserve le sens et les sources ; si un changement modifie le fond, signale-le séparément au lieu de l'inclure discrètement.
- Écris en français, sauf l'abstract.
