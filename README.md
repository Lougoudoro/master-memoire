# Mémoire de Master II

Mémoire de Master II en informatique, option Ingénierie des Systèmes
d'Information en Entreprise, Université Joseph Ki-Zerbo.

## Sujet

Adaptation et enrichissement d'une ontologie existante pour un accès
intelligent aux connaissances sur les plantes médicinales du Burkina Faso
par l'intelligence artificielle.

Auteur : Sanou Lougoudoro. Encadrant : Dr. Belko Abdoul Aziz DIALLO.

## Organisation du projet

- `main.tex` : fichier principal de compilation LaTeX. Il déclare les titres
  de chapitres et les `\input` correspondants.
- `parts/gard.tex` : page de garde.
- `parts/dedicace.tex` : dédicace.
- `parts/remerciements.tex` : remerciements.
- `parts/resume.tex` : résumé.
- `parts/abstract.tex` : abstract.
- `parts/sigle-abreviation.tex` : liste des sigles et abréviations.
- `chapters/introduction.tex` : introduction générale.
- `chapters/chapter1.tex` : chapitre I, cadre théorique et revue de littérature.
- `chapters/chapter2.tex` : chapitre II, matériel et méthodologie.
- `chapters/chapter3.tex` : chapitre III, conception et développement du système.
- `chapters/chapter4.tex` : chapitre IV, résultats et discussion.
- `chapters/conclusion.tex` : conclusion générale.
- `sanou-master.bib` : références bibliographiques.
- `images/` : logos et figures utilisés.

Note : les titres de chapitres et leurs `\label` sont déclarés dans
`main.tex`. Les fichiers `chapters/*.tex` ne doivent pas contenir de
`\chapter{...}`, sinon le titre apparaît deux fois et le label est défini
en double.

## État d'avancement

Dernière mise à jour : 11 octobre 2026.

- Introduction générale : rédigée ;
- Chapitre I, cadre théorique et revue de littérature : rédigé (2 figures à
  produire) ;
- Chapitre II, matériel et méthodologie : rédigé (2 figures à produire) ;
- Chapitre III, conception et développement du système : rédigé (prose et
  structure), 35 blocs `\TODOchapo` restants (chiffres Protégé et Neo4j,
  captures d'écran, extraits de code réels) ;
- Chapitre IV, résultats et discussion : rédigé (prose et discussion), 48 blocs
  `\TODOchapo` restants — les résultats chiffrés de l'évaluation (ontologie,
  système RAG, application web) restent à relever ;
- Conclusion générale : rédigée, à re-chiffrer une fois le chapitre IV complété ;
- Dédicace, remerciements, résumé, abstract : fichiers vides, à rédiger.

Restent à produire : les figures manquantes (schémas et captures) et le
nettoyage de la bibliographie (entrées non citées, doublons). Un état des lieux
détaillé est disponible dans `rapport-etat-des-lieux.md`.

## Compilation

Depuis le dossier racine du projet :

```text
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Ou en une seule commande, si `latexmk` est disponible :

```text
latexmk -pdf main.tex
```

La compilation nécessite une distribution LaTeX comprenant `pdflatex` et
`biber`, par exemple MiKTeX ou TeX Live. Le fichier généré est `main.pdf`.

Le document compile sans erreur (91 pages). Une alerte `Float too large for
page` subsiste : le tableau des fonctionnalités du chapitre III
(`tab:fonctionnalites`) déborde la page et doit être réduit ou scindé.

## Bibliographie

Les références sont gérées avec `biblatex` et le backend `biber`. Toute
nouvelle référence doit être ajoutée dans `sanou-master.bib`, puis citée dans
un fichier `.tex` avec `\cite{cle-de-la-reference}`. Les clés de référence
doivent être uniques dans le fichier `.bib`.

## Périmètre du système

Le système vise la consultation des connaissances scientifiques sur les
plantes médicinales du Burkina Faso. Il ne constitue ni un outil de
diagnostic, ni un système de prescription médicale.