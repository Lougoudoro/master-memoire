# Analyse des quatre mémoires modèles

À lire quand il faut justifier une convention, montrer un exemple ou trancher entre deux usages. Les fichiers PDF d'origine sont dans `C:\Users\sloug\Downloads\` (non versionnés).

## Sommaire
1. Sawadogo — soutenu, UJKZ/IBAM, option ISIE
2. Zongo — soutenu, UJKZ/IBAM, option SI
3. Nabi — soutenu, UNB/ESI
4. Yaro — brouillon v4.1, UJKZ/IBAM, option ISIE, même encadrant
5. Tableau croisé

---

## 1. Sawadogo Sidbewende Omar — « Chat bot pour le diagnostic médical à partir des symptômes des patients » (2022-2023, 53 p., soutenu)

Encadrant : Dr TRAORE Yaya. **Même option que l'auteur (ISIE)**.

- **Ordre** : Résumé, Abstract, Dédicace, Remerciements, Sommaire, Sigles, Figures, Tableaux, Introduction générale, 3 chapitres (État de l'art ; Architecture ; Implémentation), Conclusion, Bibliographie, Table des matières.
- **Introduction** : ouverture par une phrase forte, contexte sanitaire chiffré (un médecin pour 10 000 habitants), question principale posée explicitement (« comment utiliser… ? »), objectif général + 2 objectifs spécifiques, annonce des trois chapitres.
- **Chapitres** : chaque chapitre s'ouvre par « Ce chapitre vise à présenter… en abordant… ». Pas de conclusion de chapitre systématique.
- **Revue** : sept travaux décrits un à un (« Dans [11], les auteurs… »), tableau récapitulatif (auteur, algorithme, résultat), puis **un vrai paragraphe de positionnement** : il reprend l'approche de [7], s'en distingue par les données (registres de CSPS burkinabè) et ajoute un algorithme. C'est la meilleure partie du mémoire.
- **Résultats** : tableaux comparatifs par métrique (exactitude, précision, rappel, F1), puis synthèse.
- **Figures** : « Source : Nous-mêmes » sous les figures produites.
- **Faiblesses** : bibliographie majoritairement en URL « [En ligne] » ; superlatifs (« performance exceptionnelle ») ; tableau des sigles décalé ; numérotation des tableaux qui saute ; conclusion sans limites réelles.

## 2. Zongo Wendlassida Aimée Gwladys — « Approche d'analyse des vulnérabilités et des menaces dans les systèmes de télémédecine » (2022-2023, 85 p., soutenu)

Directeur : Dr J. S. D. OUATTARA ; superviseur : Dr S. G. BARRO (grades indiqués sur la page de garde).

- **Ordre** : Remerciements (incluant une dédicace fusionnée), Sigles, Figures, Tableaux, Table des matières, Résumé, Abstract, Introduction générale, 5 chapitres (Contexte de l'étude ; État de l'art ; … ; Résultats et discussion), Conclusion générale, Bibliographie.
- **Particularité** : un chapitre 1 « Contexte de l'étude » avec Contexte, Problématique, Objectifs, **Résultats attendus**, Méthodologie (recherche documentaire sur 2022-2024 dans ResearchGate, IEEE Xplore, Google Scholar).
- **Revue** : liste à puces « Traiter… », « Intégrer… » avec référence en fin de puce ; peu de critique.
- **Faiblesses** : bibliographie entièrement en URL ; chapitre « Résultats et discussion » qui est en réalité une liste de recommandations sans mesure ; conclusion générale courte, sans perspectives chiffrées.

## 3. Nabi Rasidatou — « Méthode de préparation de données pour les algorithmes d'apprentissage automatique » (2020-2021, 56 p., soutenu, UNB/ESI)

Directeur : Dr Yaya TRAORE.

- **Ordre** : Avant-propos (présentation de l'université et du lieu de stage), Dédicace, Remerciements, Table des matières, Figures, Tableaux, Sigles, Résumé, Abstract, Introduction générale (Contexte et justification ; Objectif général ; Organisation du travail), 3 chapitres, Conclusion générale, Références.
- **Chapitres** : **introduction et conclusion à chaque chapitre**, la conclusion annonçant le chapitre suivant (« Le chapitre suivant sera consacré à… »).
- **Revue** : après chaque famille de techniques, un encadré « **Positionnement sur les approches** » qui dit lesquelles seront retenues — bonne pratique, simple à imiter.
- **Remerciements** : président de l'université, directeur de l'école, directeur de mémoire, **membres du jury**, corps professoral, promotion, « MERCI » final.
- **Conclusion générale** : bilan en trois temps (« Nous avons d'abord… Par la suite… Enfin… ») puis perspectives en deux points.
- **Faiblesses** : critère de qualité arbitraire (précision ≥ 80 % = données de qualité) ; fautes (« les stockées », « data scientistes ») ; incohérence « cinq (04) étapes ».

## 4. Yaro Békassoé Emmanuel — « Cartographie des zones d'habitations non planifiées à Ouagadougou par apprentissage automatique » (2024-2025, brouillon v4.1, 45 p., NON soutenu)

Encadrant professionnel : **Dr Belko Abdoul Aziz DIALLO** (le même que l'auteur). Rédigé avec le même type de modèle LaTeX (classe book, « CHAPITRE 1 »).

- **Consignes laissées dans le modèle** : résumé et abstract de **150 à 250 mots**, présentant contexte, problématique, méthodologie, principaux résultats et perspectives ; mots-clés.
- **Introduction générale** la plus complète des quatre : Contexte ; Problématique (conséquences par plan : environnemental, sécuritaire, sanitaire, statistique) ; **définition de travail** de l'objet ; question principale + **QR1 à QR4** ; but + **OS1 à OS4** ; **H1 à H4** ; Méthodologie en **10 étapes numérotées** ; Organisation du document.
- **Chapitre I** : Définitions (avec transitions entre sous-sections et « NB : » pour préciser le choix de définition) ; Revue de la littérature où chaque travail est suivi d'un « Cependant… » qui mesure sa limite **pour le contexte burkinabè** ; **tableau 1.1 de synthèse comparative** (article, année, localité, source, résolution, méthode, précision) ; « Limites des méthodes étudiées » ; Conclusion annonçant le chapitre suivant.
- **Citations avec page** : `[1, p. 1]`, `[23, p. 3]`.
- **Validation** : annotation contrôlée par un expert, accord mesuré par le Kappa.
- **Faiblesses (brouillon)** : placeholders (« Rédigez ici », « Prénom NOM »), « figure ?? », sigle cassé, nombreuses fautes, introduction au futur, H1/H3 peu réfutables (« sont efficaces »).

## 5. Tableau croisé

| Élément | Sawadogo | Zongo | Nabi | Yaro |
|---|---|---|---|---|
| Soutenu | oui | oui | oui | non |
| Résumé + mots-clés + abstract | oui | oui | oui | consigne 150-250 mots |
| Dédicace séparée | oui | fusionnée | oui | oui |
| Jury remercié | non | non | oui | oui |
| Question de recherche explicite | oui | implicite | non | oui + QR1-4 |
| Objectifs spécifiques | oui | non | oui | OS1-4 |
| Hypothèses | non | non | non | H1-4 |
| Intro + conclusion par chapitre | intro seule | non | oui | oui |
| Transition vers chapitre suivant | non | non | oui | oui |
| Revue critique | partielle | non | positionnement | oui |
| Tableau de synthèse de la revue | oui | non | non | oui |
| Positionnement explicite | oui | non | oui | oui |
| Bibliographie académique | non (URL) | non (URL) | mixte | oui |
| Limites dans la conclusion | faibles | non | non | à venir |
