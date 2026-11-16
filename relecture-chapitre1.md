# Relecture du chapitre I : allègement (16/11/2026)

Objectif : réduire le chapitre I, le plus long du mémoire (23 pages, environ 10 600 mots), en retirant ou en condensant ce qui ne sert pas directement la recherche, pour mettre en avant les points qui fondent les choix des chapitres II à IV.

**Critère de tri.** Une partie mérite sa place si elle sert au moins l'un des trois usages suivants :
1. définir une notion **réellement employée** dans la suite du mémoire ;
2. analyser un **travail ou un outil concurrent** ;
3. justifier un **choix** fait aux chapitres II et III.

Une partie qui décrit une technique que le système **n'utilise pas**, ou qui répète un autre passage, est à retirer ou à condenser. Une partie qui décrit la conception du système relève du chapitre III.

Repère : environ 460 mots par page dans le chapitre I.

---

## 1. Ce qu'il faut garder tel quel (le cœur du chapitre)

| Partie | Mots | Pourquoi |
|---|---|---|
| 1.1.1 Concepts fondamentaux (plantes médicinales, médecine traditionnelle, ethnobotanique, contexte burkinabè) | 434 | Définit le domaine et le contexte |
| 1.1.3 Types de connaissances et niveaux de preuve | 412 | Les niveaux de preuve sont au cœur de l'ontologie et du chapitre IV |
| 1.2.2 Définition formelle et composants d'une ontologie | 257 | Notions employées partout ensuite |
| 1.2.3 Adaptation et enrichissement | 273 | C'est exactement ce que fait le mémoire |
| 1.2.4 Bases orientées graphe et Cypher | 400 | Neo4j et Cypher sont utilisés |
| 1.3.3 Génération augmentée par récupération | 202 | C'est le système construit |
| 1.4.1 Ontologies internationales et africaines (WATRIMed, ontoMEDTRAD, ATHMed, etc.) | 1 977 | Revue critique déjà mise à niveau |
| 1.4.1 Synthèse comparative et tableau | 602 | Exigé par le canevas |
| 1.4.2 Plateformes de données existantes | 612 | Exigé par le canevas, revue critique |

---

## 2. Ce qu'il faut retirer ou condenser

| # | Partie | Mots | Problème | Proposition | Gain estimé |
|---|---|---|---|---|---|
| 1 | 1.2.1 Principaux modèles de représentation (réseaux sémantiques, cadres, règles, ontologies, avec avantages et limites) | 287 | Manuel général. Seules les ontologies sont utilisées | Une phrase qui situe les ontologies parmi ces modèles et dit pourquoi on les retient | −220 |
| 2 | 1.2.2 Langages d'ontologies (RDF, RDFS, OWL, SKOS) | 120 | SKOS n'est pas utilisé. Le détail OWL-Lite, DL et Full ne sert pas | Deux phrases sur RDF, OWL et le format Turtle employé | −80 |
| 3 | 1.2.3 Alignement d'ontologies | 140 | Le mémoire n'aligne pas d'ontologies, il en adapte une | Supprimer, ou une phrase de définition | −120 |
| 4 | 1.3.1 Techniques fondamentales du TALN (tokenisation, lemmatisation, étiquetage, entités nommées, dépendances) | 172 | Aucune de ces techniques n'est employée : le système passe par un modèle de langue en Text2Cypher. Ces termes n'apparaissent dans aucun autre chapitre | Supprimer | −170 |
| 5 | 1.3.1 Les transformers (BERT, GPT, T5) | 161 | Seule la famille générative, dont Llama 3, est utilisée | Deux ou trois phrases : l'architecture transformer et les modèles génératifs, avec Llama 3 | −110 |
| 6 | 1.3.2 Extraction d'information : étapes, avantages et limites en listes | 341 | Listes génériques. La démarche réelle est décrite aux chapitres II et III | Un paragraphe qui garde la définition, les limites des modèles de langue (erreurs, variabilité) et le renvoi au chapitre III | −200 |
| 7 | 1.3.3 Recherche sémantique, chaîne en six étapes | 172 | Elle décrit un fonctionnement qui n'est pas celui du système (désambiguïsation « paludisme » vers « malaria », classement par proximité sémantique) | Deux phrases de définition. La chaîne réelle est au chapitre III | −130 |
| 8 | 1.3.4 Mécanismes de traçabilité, gestion des incertitudes, limites du système | 204 | C'est la conception du système, au futur, déjà traitée au chapitre III et dans les limites du chapitre IV. Risque de promettre ce qui n'est pas fait (lien vers les documents, citations numérotées) | Garder l'importance de la traçabilité et la distinction des niveaux de preuve. Retirer le reste | −180 |
| 9 | Les paragraphes « Application à notre recherche » de 1.2 et 1.3 | ≈ 300 | Ils annoncent au futur ce que le chapitre II décrit déjà | Les supprimer, ou une phrase de lien par section | −200 |
| 10 | 1.4.1 Inventaires burkinabè : liste détaillée des études, avec les titres complets en anglais | ≈ 600 | Long à lire. Seules les données clés servent : auteur, année, région, nombre d'espèces | Un tableau récapitulatif, suivi de la limite commune et de l'apport déjà rédigés | −350 |
| 11 | 1.4.1 Projet « Herbier avec chimiothèque » (objectifs, bosquets, autres herbiers HNBU, CNSF, OUA) | 495 | Il fait doublon avec le nouveau paragraphe sur la base de l'Herbier national (1.4.2). Les bosquets et les autres herbiers sont hors sujet | Fusionner avec 1.4.2 : garder les objectifs utiles (dix pathologies, vingt plantes, base nationale) | −350 |
| 12 | 1.4.1 Ontologies nationales et ethniques | 62 | Elle répète la couverture d'ontoMEDTRAD | La fusionner avec les particularités de la médecine traditionnelle africaine | −40 |
| 13 | Trois positionnements : « Apports attendus » (323), « Positionnement attendu de notre système » (48) et « Positionnement de notre recherche » (140) | 511 | Trois passages disent la même chose | Une seule section de positionnement, placée après le tableau de synthèse et les plateformes | −250 |
| 14 | 1.1.2 Aspects botaniques et écologiques, propriétés pharmacologiques, composition chimique | 421 | Utile en partie seulement : les familles, les parties utilisées et les préparations servent à l'ontologie. Le reste est général | Condenser en un paragraphe centré sur ce que l'ontologie représente | −200 |

**Gain total estimé : environ 2 600 mots, soit 5 à 6 pages.** Le chapitre I passerait d'environ 23 pages à environ 17 ou 18, c'est-à-dire la moyenne des chapitres. Il se concentrerait sur le domaine, les ontologies, la revue critique et le positionnement.

---

## 3. Points d'attention

- **Ne rien perdre de ce que le jury attend.** La revue critique, le tableau de synthèse, les plateformes et le positionnement restent intacts. Ce sont eux qui portent le chapitre.
- **Les promesses non tenues.** Les parties 7 et 8 décrivent au futur des fonctions que le système n'a pas, ou pas sous cette forme. Les retirer réduit aussi le risque de questions gênantes.
- **Les références.** Après suppression, certaines entrées du `.bib` ne seront plus citées, par exemple Devlin (BERT), Raffel (T5) ou Nadeau (NER). biblatex ne les affiche que si elles sont citées, donc il n'y a rien à faire, sauf pour garder le `.bib` propre.
- **Les annexes.** Le tableau des inventaires burkinabè, ou la liste complète des études avec leurs titres, peut aller en annexe si vous voulez garder le détail. C'est aussi un début d'annexe, que le canevas prévoit.
