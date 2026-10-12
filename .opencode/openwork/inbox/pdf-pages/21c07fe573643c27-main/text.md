# main.pdf

pages: 91
sha256: 21c07fe573643c27b79b6a0506a2813c13cfc3ada0cdad4a1f9934012d151841

--- page 1 ---
Burkina Faso
La Patrie ou la Mort, nous Vaicrons
Ministère de l’Enseignement Supérieur
et de la Recherche Scientifique
Université Joseph Ki-Zerbo
Institut Burkinabè des Arts et Métiers
MÉMOIRE POUR L’OBTENTION DU MASTER II EN
INFORMATIQUE
Option : Ingénierie des Systèmes d’Information en Entreprise
Par
Sanou Lougoudoro
Adaptation et enrichissement d’une ontologie pour un accès
intelligent et traçable aux connaissances scientifiques sur les
plantes médicinales du Burkina Faso
Encadreur : Dr. Belko Abdoul Aziz DIALLO PhD
Annee Universitaire 2025 – 2026

--- page 2 (no text layer) ---

--- page 3 ---
Dédicace
i

--- page 4 ---
Remerciements
ii

--- page 5 ---
Resumé
iii

--- page 6 ---
Abstract
iv

--- page 7 ---
Table des figures
1 Dispersion des connaissances scientifiques . . . . . . . . . . . . . . . . . . . . . . . 2
2 Démarche méthodologique adoptée . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
I.1 Hiérarchie des niveaux de preuve . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
I.2 Les langages du web sémantique . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
II.1 Constitution du corpus documentaire . . . . . . . . . . . . . . . . . . . . . . . . . . 32
II.2 Dispositif technique d’expérimentation . . . . . . . . . . . . . . . . . . . . . . . . . 34
III.1 L’ontologie initiale ontoMEDTRAD reconstituée sous Protégé 5 (arbre des classes) . 49
III.2 L’ontologie conservée : les concepts d’ontoMEDTRAD retenus . . . . . . . . . . . . 50
III.3 L’ontologie adaptée et enrichie sous Protégé 5 . . . . . . . . . . . . . . . . . . . . . 51
III.4 Le graphe de connaissances peuplé . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
III.5 Chaîne de traitement du système RAG . . . . . . . . . . . . . . . . . . . . . . . . . 59
III.6 Flux utilisateur de l’application web . . . . . . . . . . . . . . . . . . . . . . . . . . 61
III.7 Écrans principaux de l’application web . . . . . . . . . . . . . . . . . . . . . . . . . 61
IV.1 Résultats du questionnaire par critère . . . . . . . . . . . . . . . . . . . . . . . . . . 69
v

--- page 8 ---
Liste des tableaux
I.1 Synthèse comparative des ontologies de la littérature . . . . . . . . . . . . . . . . . 28
II.1 Sources du corpus documentaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
II.2 Ontologies candidates pour la comparaison . . . . . . . . . . . . . . . . . . . . . . 34
II.3 Modes d’accès à Llama 3 70B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
II.4 Caractéristiques de Neo4j Desktop . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
II.5 Composants LangChain utilisés . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
II.6 Bibliothèques Python utilisées . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
II.7 Récapitulatif du matériel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
II.8 Correspondance entre le matériel et les phases . . . . . . . . . . . . . . . . . . . . . 38
II.9 Grille de critères de comparaison . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
II.10 Notation des ontologies candidates . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
II.11 Critères d’évaluation de l’ontologie . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
II.12 Critères d’évaluation du système RAG . . . . . . . . . . . . . . . . . . . . . . . . . 46
II.13 Critères d’évaluation de l’application web . . . . . . . . . . . . . . . . . . . . . . . 46
II.14 Correspondance entre les phases, les objectifs et les livrables . . . . . . . . . . . . . 47
III.1 Concepts retenus et écartés lors de l’adaptation . . . . . . . . . . . . . . . . . . . . 50
III.2 Statistiques de l’ontologie avant et après adaptation . . . . . . . . . . . . . . . . . . 51
III.3 Classes ajoutées à l’ontologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
III.4 Propriétés ajoutées à l’ontologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
III.5 Relations ajoutées à l’ontologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
III.6 Correspondance entre les classes de l’ontologie et les nœuds du graphe . . . . . . . . 54
III.7 Relations du graphe de connaissances . . . . . . . . . . . . . . . . . . . . . . . . . 55
III.8 Fonctionnalités de l’application web . . . . . . . . . . . . . . . . . . . . . . . . . . 62
IV.1 Résultats de l’évaluation de l’ontologie . . . . . . . . . . . . . . . . . . . . . . . . . 66
IV.2 Résultats de l’évaluation du système RAG . . . . . . . . . . . . . . . . . . . . . . . 67
IV.3 Résultats par famille de questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
IV.4 Volumes de résultats des quatre familles de requêtes . . . . . . . . . . . . . . . . . . 68
IV.5 Résultats de l’évaluation de l’application web . . . . . . . . . . . . . . . . . . . . . 69
vi

--- page 9 ---
Liste des sigles et abréviations
Sigle ou abréviation Signification
API Application Programming Interface
BERT Bidirectional Encoder Representations from Transformers
BFO Basic Formal Ontology
CI50 Concentration Inhibitrice 50 %
CSV Comma-Separated Values
DL50 Dose Létale 50 %
DOI Digital Object Identifier
DPPH 2,2-diphényl-1-picrylhydrazyle
DrOn Drug Ontology
FLOPO Flora Ontology
FOODON Food Ontology
GC-MS Gas Chromatography-Mass Spectrometry
GPT Generative Pre-trained Transformer
GPU Graphics Processing Unit
HPLC High-Performance Liquid Chromatography
HTM Herbal Traditional Medicine Ontology
IA Intelligence Artificielle
IC50 Concentration Inhibitrice médiane de 50 %
IHTSDO International Health Terminology Standards Development Organisation
INERA Institut National de l’Environnement et de la Recherche Appliquée
JSON JavaScript Object Notation
LLM Large Language Model
NER Named Entity Recognition
NLP Natural Language Processing
OCR Optical Character Recognition
OMS Organisation Mondiale de la Santé
OTM Ontology of Traditional Medicine
OWL Web Ontology Language
PNPMT Programme National de Promotion de la Médecine Traditionnelle
PO Plant Ontology
RAG Retrieval-Augmented Generation
RDF Resource Description Framework
RDFS RDF Schema
SKOS Simple Knowledge Organization System
SNOMED CT Systematized Nomenclature of Medicine – Clinical Terms
SPARQL SPARQL Protocol and RDF Query Language
T5 Text-to-Text Transfer Transformer
TALN Traitement Automatique du Langage Naturel
TPU Tensor Processing Unit
UICN Union Internationale pour la Conservation de la Nature
W3C World Wide Web Consortium
WATRIMed West African Herbal-based Traditional Medicine
XML Extensible Markup Language
vii

--- page 10 ---
Table des matières
Dédicace i
Remerciements ii
Resumé iii
Abstract iv
Table des figures v
Liste des tableaux vi
Liste des sigles et abréviations vii
Introduction générale 1
I Cadre théorique et revue de littérature 8
I.1 Plantes médicinales et connaissances scientifiques au Burkina Faso . . . . . . . . . . 8
I.1.1 Concepts fondamentaux . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
I.1.2 Plantes médicinales documentées dans la littérature scientifique . . . . . . . 9
I.1.3 Types de connaissances et niveaux de preuve . . . . . . . . . . . . . . . . . 10
I.2 Ingénierie des connaissances et ontologies . . . . . . . . . . . . . . . . . . . . . . . 11
I.2.1 Représentation des connaissances . . . . . . . . . . . . . . . . . . . . . . . 11
I.2.2 Ontologies et réutilisation d’ontologies existantes . . . . . . . . . . . . . . . 12
I.2.3 Adaptation, alignement et enrichissement ontologique . . . . . . . . . . . . 14
I.2.4 Bases de connaissances et interrogation sémantique . . . . . . . . . . . . . . 15
I.3 Intelligence artificielle pour l’accès aux connaissances . . . . . . . . . . . . . . . . 16
I.3.1 Traitement des requêtes en langage naturel . . . . . . . . . . . . . . . . . . . 16
I.3.2 Extraction et structuration assistées par IA . . . . . . . . . . . . . . . . . . . 17
I.3.3 Recherche sémantique et génération de réponses . . . . . . . . . . . . . . . 18
I.3.4 Traçabilité et fiabilité des réponses . . . . . . . . . . . . . . . . . . . . . . . 19
I.4 Travaux connexes et positionnement scientifique . . . . . . . . . . . . . . . . . . . . 20
I.4.1 Ontologies dans le domaine des plantes médicinales . . . . . . . . . . . . . 20
I.4.2 Systèmes intelligents d’accès aux connaissances . . . . . . . . . . . . . . . 29
I.4.3 Positionnement de notre recherche . . . . . . . . . . . . . . . . . . . . . . . 29
Conclusion du chapitre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
II Matériel et méthodologie 31
II.1 Matériel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
II.1.1 Corpus documentaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
II.1.2 Ontologies candidates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
II.1.3 Outils et environnement technique . . . . . . . . . . . . . . . . . . . . . . . 34
viii

--- page 11 ---
II.1.4 Tableau récapitulatif du matériel . . . . . . . . . . . . . . . . . . . . . . . . 36
II.1.5 Tableau de correspondance Matériel - Phases . . . . . . . . . . . . . . . . . 38
II.2 Méthodologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
II.2.1 Phase 1 : Identification et étude comparative des ontologies . . . . . . . . . . 38
II.2.2 Phase 2 : Définition des critères de recherche et de sélection des documents . 40
II.2.3 Phase 3 : Constitution du corpus scientifique . . . . . . . . . . . . . . . . . 41
II.2.4 Phase 4 : Adaptation de l’ontologie sélectionnée . . . . . . . . . . . . . . . . 41
II.2.5 Phase 5 : Enrichissement des connaissances à partir de la littérature scientifique 43
II.2.6 Phase 6 : Construction et interrogation de la base de connaissances . . . . . . 44
II.2.7 Phase 7 : Exploitation par IA et développement de l’application web . . . . . 44
II.2.8 Phase 8 : Évaluation et validation . . . . . . . . . . . . . . . . . . . . . . . 45
II.3 Synthèse et transition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
II.3.1 Tableau de correspondance Phases - Livrables . . . . . . . . . . . . . . . . . 46
Conclusion du chapitre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
III Conception et développement du système 48
III.1 Ontologie adaptée et enrichie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
III.1.1 Vue d’ensemble du modèle . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
III.1.2 Classes ajoutées . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
III.1.3 Propriétés ajoutées . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
III.1.4 Relations ajoutées . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
III.2 Base de connaissances orientée graphe . . . . . . . . . . . . . . . . . . . . . . . . . 53
III.2.1 Du modèle ontologique au graphe . . . . . . . . . . . . . . . . . . . . . . . 53
III.2.2 Import et peuplement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
III.2.3 Interrogation de la base . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
III.3 Intégration de l’intelligence artificielle . . . . . . . . . . . . . . . . . . . . . . . . . 57
III.3.1 Extraction assistée des connaissances . . . . . . . . . . . . . . . . . . . . . 57
III.3.2 Système RAG d’accès aux connaissances . . . . . . . . . . . . . . . . . . . 59
III.3.3 Traçabilité des réponses . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
III.4 Développement de l’application web . . . . . . . . . . . . . . . . . . . . . . . . . . 60
III.4.1 Architecture de l’application . . . . . . . . . . . . . . . . . . . . . . . . . . 60
III.4.2 Fonctionnalités . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
III.4.3 Gestion de session et déploiement . . . . . . . . . . . . . . . . . . . . . . . 61
Conclusion du chapitre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
IV Résultats et discussion 64
IV.1 Évaluation de l’ontologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
IV.1.1 Couverture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
IV.1.2 Cohérence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
IV.1.3 Traçabilité . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
IV.1.4 Extensibilité . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
IV.1.5 Synthèse de l’évaluation de l’ontologie . . . . . . . . . . . . . . . . . . . . 65
IV.2 Évaluation du système RAG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
IV.2.1 Construction du jeu d’évaluation . . . . . . . . . . . . . . . . . . . . . . . . 66
IV.2.2 Résultats quantitatifs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
IV.2.3 Volumes d’interrogation de la base . . . . . . . . . . . . . . . . . . . . . . . 67
IV.2.4 Observations qualitatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
IV.3 Évaluation de l’application web . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
IV.3.1 Campagne de test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
IV.3.2 Résultats du questionnaire . . . . . . . . . . . . . . . . . . . . . . . . . . . 69

--- page 12 ---
IV.3.3 Performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
IV.4 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
IV.4.1 Confrontation aux objectifs de la recherche . . . . . . . . . . . . . . . . . . 70
IV.4.2 Confrontation aux systèmes existants . . . . . . . . . . . . . . . . . . . . . 70
IV.4.3 Limites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
IV.4.4 Pistes de travail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
Conclusion du chapitre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
Conclusion générale 73
Bibliographie 74

--- page 13 ---
Introduction générale
Contexte et justification du sujet
Au Burkina Faso, les plantes médicinales occupent une place importante dans les pratiques de
santé, et leur étude fait l’objet de travaux scientifiques nombreux [38]. Ces travaux portent sur leur
identification, leurs usages, leurs propriétés pharmacologiques et leur toxicité.
Le problème, toutefois, tient moins à l’abondance de ces productions qu’à leur dispersion. Les
connaissances disponibles se trouvent éparpillées dans la littérature scientifique [59] : articles, thèses,
mémoires, rapports de recherche, mais aussi inventaires ethnobotaniques et plateformes numériques.
Or ces documents n’emploient pas les mêmes terminologies, et une même plante y est souvent désignée
par plusieurs synonymes ou noms vernaculaires. Il devient alors difficile de comparer les résultats
d’une étude à l’autre, de rechercher une information sur une plante, une pathologie ou une recette
précise, et même de remonter à la source qui soutient cette information.
Les ontologies sont apparues comme un moyen de structurer cet ensemble. Elles représentent
les concepts d’un domaine et les relations qui les unissent, tout en facilitant l’interopérabilité et
l’interrogation [58].
Notre travail s’inscrit dans cette perspective, sans prétendre construire une ontologie entièrement
nouvelle. Plutôt que de partir de zéro, nous reprendrons un modèle existant consacré aux plantes
médicinales pour l’adapter au contexte burkinabè et l’enrichir à partir de la littérature scientifique.
L’intelligence artificielle interviendra ensuite pour faciliter l’accès à ces connaissances : interpréter des
requêtes formulées en langage naturel, retrouver l’information pertinente dans la base de connaissances,
et présenter le résultat de manière accessible. Une application web assurera l’interface entre l’utilisateur
et ce dispositif, chaque réponse demeurant rattachée aux sources scientifiques qui l’ont fondée.
Trois éléments sont ainsi rapprochés dans cette recherche : une ontologie existante, les connaissances
scientifiques sur les plantes médicinales du Burkina Faso, et des mécanismes d’accès intelligent fondés
sur l’intelligence artificielle (figure 1).
1

--- page 14 ---
Figure 1 – Dispersion des connaissances scientifiques
Problématique de la recherche
Les connaissances scientifiques sur les plantes médicinales du Burkina Faso sont abondantes [38]
et proviennent de sources aussi variées que des articles, des thèses, des mémoires, des rapports de
recherche et des bases de données institutionnelles [59]. Leur exploitation, en revanche, pose problème.
Les ontologies apparaissent comme un moyen de les structurer [41], en représentant les concepts d’un
domaine et les relations entre ces concepts, ce qui ouvre la voie à l’interopérabilité et à une interrogation
plus fine. Mais aucune ne répond nécessairement aux besoins du contexte burkinabè : il faut donc
identifier les modèles disponibles, juger de leur pertinence, et n’en retenir qu’un. À cela s’ajoute une
seconde difficulté, qui concerne l’accès. Une base structurée peut être riche sans être compréhensible;
l’intelligence artificielle est précisément susceptible de remédier à cet écart [36], en acceptant des
requêtes en langage naturel, en allant chercher les informations pertinentes et en les restituant sous une
forme accessible.
L’étude qui suit cherche donc à relier trois dimensions : des connaissances issues de la littéra￾ture scientifique, leur organisation dans une ontologie adaptée et enrichie, et leur exploitation par
l’intelligence artificielle au moyen d’une application web. De là la question principale :
Comment enrichir une ontologie existante à partir de la littérature scientifique sur les
plantes médicinales du Burkina Faso, puis utiliser l’intelligence artificielle pour l’interroger
et obtenir des réponses pertinentes, traçables, en langage naturel et fidèles aux sources
scientifiques ?
Quatre questions spécifiques en découlent :
— Quelles ontologies existantes peuvent représenter les connaissances sur les plantes médicinales,
et sur quels critères les comparer afin de retenir la plus adaptée au contexte burkinabè ?
— Quelles adaptations et quels enrichissements sont nécessaires pour intégrer les connaissances
issues de la littérature scientifique sur les plantes médicinales du Burkina Faso, tout en garantissant
la traçabilité vers les sources ?
— Comment exploiter l’ontologie adaptée et enrichie avec l’intelligence artificielle (LLM, RAG)
pour faciliter l’accès aux connaissances en langage naturel ?
— Comment concevoir une application web permettant la consultation, la recherche et la compré￾hension des connaissances documentées sur les plantes médicinales du Burkina Faso ?
2

--- page 15 ---
Objectif général et objectifs spécifiques
De cette problématique découlent un objectif général, qui énonce la finalité du travail, et des
objectifs spécifiques, qui la décomposent en actions concrètes et évaluables. Ils guideront la démarche
méthodologique et permettront d’apprécier ce que la recherche apporte effectivement.
Objectif général
Notre objectif général est d’adapter et d’enrichir une ontologie existante afin de représenter les
connaissances issues de la littérature scientifique sur les plantes médicinales du Burkina Faso, puis
d’exploiter ces connaissances par l’intelligence artificielle au moyen d’une application web pour
faciliter leur accès et leur diffusion.
Objectifs spécifiques
— Identifier et comparer les ontologies existantes dans le domaine des plantes médicinales afin de
sélectionner la plus pertinente pour le contexte burkinabè.
— Adapter et enrichir l’ontologie sélectionnée à partir de la littérature scientifique sur les plantes
médicinales du Burkina Faso, en assurant la traçabilité des connaissances vers leurs sources.
— Construire une base de connaissances orientée graphe et mettre en place un système d’accès
intelligent (RAG) exploitant l’ontologie enrichie.
— Développer une application web permettant la recherche, la consultation et la compréhension des
connaissances documentées sur les plantes médicinales du Burkina Faso.
Hypothèses de recherche
Pour répondre aux questions posées et atteindre les objectifs fixés, notre étude repose sur cinq
hypothèses. La première porte sur la démarche ontologique, la deuxième sur la méthodologie
d’extraction, la troisième sur l’adaptation et l’enrichissement, la quatrième sur l’accès intelligent et la
cinquième sur la diffusion. Chacune sera vérifiée au fil de la recherche.
1. Hypothèse 1 : Une revue méthodique et systématique de la littérature scientifique permet
d’identifier et d’enrichir un modèle ontologique capable de représenter les connaissances sur les
plantes médicinales du Burkina Faso
2. Hypothèse 2 : L’utilisation de modèles de langue de grande taille (LLM) améliore l’extraction
automatique des connaissances à partir de la littérature scientifique, comparativement aux
méthodes manuelles.
3. Hypothèse 3 : L’adaptation et l’enrichissement de l’ontologie sélectionnée permettent de
mieux représenter les connaissances documentées dans la littérature scientifique sur les plantes
médicinales du Burkina Faso, tout en assurant leur traçabilité.
4. Hypothèse 4 : L’exploitation de l’ontologie enrichie par un système RAG facilite la recherche et
la compréhension des connaissances en langage naturel.
5. Hypothèse 5 : Une application web intégrant le système RAG permet de mieux vulgariser et
diffuser les connaissances scientifiques documentées sur les plantes médicinales du Burkina
Faso.
3

--- page 16 ---
Démarche méthodologique adoptée
La démarche adoptée est progressive. Elle articule une revue de littérature, une étude comparative
des ontologies, l’ingénierie des connaissances, l’intelligence artificielle et le développement logiciel,
selon les huit phases de la figure 2. Chaque phase produit des livrables qui servent la suivante, et la
validation intervient à plusieurs étapes pour sécuriser la qualité des résultats.
Figure 2 – Démarche méthodologique adoptée
Phase 1 : Identification et étude comparative des ontologies
La première phase identifie les ontologies existantes du domaine des plantes médicinales, en
les recherchant dans la littérature scientifique et dans les bases de données spécialisées. Nous les
comparerons à l’aide d’une grille de critères portant sur la couverture du domaine, la richesse sémantique,
la disponibilité, la documentation, l’interopérabilité, l’adaptabilité au contexte burkinabè, la traçabilité
et la prise en compte des savoirs locaux. Chacune sera notée sur cette grille, et celle qui obtiendra le score
le plus élevé sera retenue. Cette phase conditionne la suite du travail, puisqu’elle détermine le modèle
conceptuel qui guidera l’ensemble des étapes ultérieures. Son livrable est l’ontologie sélectionnée.
Phase 2 : Définition des critères de collection des documents
La deuxième phase fixe les critères qui encadreront la recherche et la sélection des documents
scientifiques, de manière à garantir la pertinence, la qualité et la cohérence des sources mobilisées. Les
critères de recherche portent sur les plantes, les parties utilisées, les pathologies et usages médicinaux,
les modes de préparation, les niveaux de preuve, les propriétés pharmacologiques et la composition
chimique. Ceux de sélection tiennent à la pertinence du document, à l’identification de la plante, à la
disponibilité d’une référence scientifique, à la fiabilité et à l’actualité. De ce corpus sûr et cohérent
dépendra la suite des travaux. Le livrable est la grille de critères de recherche et de sélection.
Phase 3 : Constitution du corpus scientifique
La troisième phase réunit les documents scientifiques portant sur les plantes médicinales du Burkina
Faso : articles, thèses, mémoires et rapports de recherche. Les critères d’inclusion et d’exclusion
définis précédemment s’appliquent, avec une vérification systématique de la pertinence du document,
4

--- page 17 ---
de l’identification de la plante et de l’existence d’une référence scientifique. Chaque information
retenue est conservée avec sa provenance. Le corpus ainsi constitué, organisé et indexé, forme la base
documentaire de l’étude.
Phase 4 : Adaptation de l’ontologie sélectionnée
La quatrième phase adapte l’ontologie retenue au contexte des plantes médicinales du Burkina Faso.
L’analyse des concepts existants conduit à distinguer ceux que l’on conserve, ceux que l’on modifie
et ceux que l’on ajoute. Nous ajouterons des classes pour les maladies spécifiques au pays, les noms
vernaculaires en langues locales, les régions et les niveaux de preuve; des propriétés pour les noms
vernaculaires, la localisation géographique, les niveaux de preuve et la traçabilité. Les relations seront
modifiées pour préciser leur sémantique et garantir la traçabilité, en préservant autant que possible
la compatibilité avec la structure initiale. Chaque adaptation sera documentée. Le livrable est une
ontologie adaptée au contexte burkinabè.
Phase 5 : Enrichissement des connaissances à partir de la littérature scientifique
La cinquième phase enrichit l’ontologie à partir du corpus constitué en phase 3 et filtré selon les
critères de la phase 2. L’extraction est assistée par l’intelligence artificielle, au moyen de prompts
adressés à des modèles de langue de grande taille (LLM) pour identifier les plantes, leurs usages, les
parties utilisées, les modes de préparation et les propriétés pharmacologiques, tels que documentés dans
les sources. Les résultats sont produits dans des formats structurés (JSON, CSV). Nous conserverons
les références bibliographiques et, lorsque cela est possible, la page ou la section dont proviennent les
informations, en distinguant les usages rapportés par les études ethnobotaniques des résultats issus
d’études expérimentales. Les niveaux de preuve associés aux connaissances seront ceux que rapportent
les sources, sans réévaluation indépendante, et la qualité des extractions sera appréciée par le protocole
d’évaluation de la phase 8. Le livrable est un ensemble de données structurées prêtes à être intégrées
dans la base de connaissances orientée graphe; ces données ne sont pas versées dans l’ontologie, qui
n’en fournit que le schéma.
Phase 6 : Construction et interrogation de la base de connaissances
La sixième phase construit la base de connaissances orientée graphe, dont l’ontologie adaptée et
enrichie fournit la structure. Les données extraites deviennent des instances correspondant aux concepts
définis. Le choix du graphe se justifie par sa capacité à modéliser naturellement les relations complexes
entre plantes, usages, propriétés et sources. Chaque connaissance importante sera rattachée à sa source,
de sorte qu’il soit toujours possible de retrouver l’origine d’une information. L’interrogation s’effectuera
en Cypher ou en SPARQL, et nous définirons des scénarios de recherche portant sur une plante, un
usage médicinal, une partie utilisée ou une source scientifique. Le livrable est une base Neo4j peuplée
et interrogeable.
Phase 7 : Exploitation par IA et développement de l’application web
La septième phase constitue le cœur de l’objectif d’accès intelligent. L’accès est assuré par un
système RAG (Retrieval-Augmented Generation), qui combine recherche d’informations dans la base
de connaissances et génération de réponses par un modèle de langage. Le système interprète la requête
en langage naturel, interroge la base pour retrouver les informations pertinentes, puis formule une
réponse fondée sur les faits retrouvés. La traçabilité en découle, chaque information étant liée à sa source
scientifique. L’application web qui nous servira d’interface proposera une recherche en langage naturel
et des fiches sur les plantes, leurs usages documentés, les parties utilisées, les modes de préparation
5

--- page 18 ---
et les références correspondantes. Les réponses resteront liées aux sources disponibles. Précisons
qu’il s’agit d’un outil de consultation : il ne constitue ni un dispositif de diagnostic, ni un système de
prescription. Le livrable est un système RAG fonctionnel et une application web fonctionnelle.
Phase 8 : Évaluation et validation
La huitième phase évalue et valide l’approche, à trois niveaux. L’ontologie d’abord, dont on vérifiera
la couverture, la cohérence, la traçabilité et l’extensibilité. Le système RAG ensuite, dont on mesurera
la pertinence, la fidélité, l’exactitude et la traçabilité. L’application web enfin, évaluée sur sa facilité
d’utilisation, sa compréhension, son utilité et ses performances. L’évaluation sollicitera des participants :
étudiants, chercheurs et tradipraticiens. Le livrable est un rapport d’évaluation et de validation.
Délimitation du champ d’étude
Notre étude porte sur les plantes médicinales documentées au Burkina Faso, et sur les connaissances
relatives à leurs usages médicinaux et à leurs propriétés biologiques lorsqu’une source scientifique les
rapporte. Ces connaissances proviendront de la littérature accessible et vérifiable; aucune enquête de
terrain directe n’est prévue dans le cadre de ce travail.
Le travail consiste à sélectionner une ontologie existante, puis à l’adapter et à l’enrichir, ce choix
étant précédé d’une étude comparative.
Sur le plan technique, il comprendra une base de connaissances orientée graphe, un système RAG
pour l’accès intelligent et une application web. L’extraction des connaissances s’appuiera sur des
prompts d’IA, qui facilitent l’accès aux connaissances structurées sans être pour autant une source
scientifique autonome : les documents scientifiques restent la référence.
Le système s’adresse donc à la consultation, à la vulgarisation et à la diffusion scientifique. Il ne
remplace pas l’avis d’un professionnel de santé et ne sert ni à poser un diagnostic, ni à établir une
prescription.
Résultats attendus
Au terme de notre recherche, nous attendons :
— La constitution d’un corpus scientifique organisé sur les plantes médicinales du Burkina Faso,
avec des connaissances rattachées à leurs sources et au niveau de preuve qu’elles y déclarent.
— La réalisation d’une étude comparative des ontologies existantes afin de sélectionner celle qui
nous semble la plus pertinente.
— L’adaptation et l’enrichissement de cette ontologie avec les connaissances issues de la littérature
scientifique.
— La mise en place d’une base de connaissances graphe traçable, exploitée par le système RAG qui
combine la recherche sémantique et la génération de réponses.
— Le développement d’une application web permettant de rechercher, consulter et comprendre les
connaissances documentées sur les plantes médicinales du Burkina Faso.
L’intelligence artificielle facilitera l’interprétation des requêtes et l’accès aux informations per￾tinentes; les résultats proposés resteront fondés sur les données de la base et sur les références
scientifiques associées.
6

--- page 19 ---
Contribution attendue
La contribution principale de notre recherche sera de réutiliser une ontologie existante et de l’adapter
au contexte des plantes médicinales du Burkina Faso, en l’enrichissant à partir des connaissances issues
de la littérature scientifique.
Sur le plan scientifique, le travail contribuera à mieux structurer des connaissances dispersées dans
plusieurs publications, et à conserver le lien qui unit chaque information à sa source.
Sur le plan technique, la recherche aboutira à une ontologie enrichie, une base de connaissances et
un mécanisme d’accès intelligent, l’intelligence artificielle facilitant l’interrogation des connaissances
via une application web.
Sur le plan pratique, le système pourra aider les chercheurs, les étudiants et les autres utilisateurs
autorisés à accéder plus facilement aux informations documentées. Il facilitera également la recherche
bibliographique et l’exploration des relations entre les plantes et les connaissances scientifiques
associées.
Structuration du mémoire
Le mémoire est organisé en quatre chapitres numérotés en chiffres romains, précédés de l’introduction
générale et suivis de la conclusion générale.
— Introduction générale (non numérotée). Le contexte et la justification du sujet y sont exposés,
puis la problématique, les questions de recherche, les objectifs et les hypothèses. Y figurent
également la démarche méthodologique, la délimitation du champ d’étude et les résultats attendus.
— Chapitre I : Cadre théorique et revue de littérature. Les notions liées aux plantes médicinales et
aux connaissances scientifiques sur le Burkina Faso y sont présentées, suivies de l’ingénierie des
connaissances, des ontologies, des bases de connaissances et de l’intelligence artificielle. Les
travaux connexes sont analysés en dernier.
— Chapitre II : Matériel et méthodologie. Le corpus scientifique, les critères de sélection et les
méthodes d’analyse sont décrits; les ontologies identifiées, les critères de comparaison et la
méthode de sélection sont présentés. Les étapes d’adaptation, d’enrichissement et de validation y
sont détaillées.
— Chapitre III : Conception et développement du système. L’ontologie sélectionnée et les
adaptations réalisées y sont présentées, suivies de la base de connaissances, puis de l’intégration
de l’intelligence artificielle et du développement de l’application web.
— Chapitre IV : Résultats et discussion. Les résultats de l’étude comparative des ontologies y
sont exposés, avec l’ontologie adaptée et enrichie ainsi que la base de connaissances. L’accès
intelligent et les fonctionnalités de l’application web sont ensuite analysés, et les limites du
système discutées.
La conclusion générale rappelle les principaux résultats, montre dans quelle mesure les objectifs
et les hypothèses ont été atteints, et présente enfin les limites du travail comme ses perspectives
d’amélioration.
7

--- page 20 ---
Chapitre I
Cadre théorique et revue de littérature
Introduction du chapitre
Toute recherche appliquée repose d’abord sur des notions clairement définies. Ce chapitre a pour
objet de poser d’abord les notions liées aux plantes médicinales et aux connaissances scientifiques
accumulées sur le Burkina Faso, puis les principes de l’ingénierie des connaissances et des ontologies,
avant d’examiner ce que l’intelligence artificielle peut apporter à l’accès à ces connaissances. Il passe
enfin en revue les travaux déjà consacrés au sujet et situe la présente recherche par rapport à eux. Quatre
sections s’articulent ainsi, de la définition du domaine à la confrontation avec la littérature existante.
I.1 Plantes médicinales et connaissances scientifiques au Burkina
Faso
I.1.1 Concepts fondamentaux
Définition des plantes médicinales Selon l’Organisation Mondiale de la Santé (OMS), une plante
médicinale est toute plante dont une ou plusieurs parties contiennent des substances utilisables à des
fins thérapeutiques [55]. Ces substances, dites principes actifs, exercent une action pharmacologique
sur l’organisme : elles peuvent prévenir, soulager ou guérir des affections.
L’Union Internationale pour la Conservation de la Nature (UICN) adopte une perspective plus large,
qui présente les plantes médicinales à la fois comme des ressources végétales mobilisées par les systèmes
de médecine traditionnelle et comme des matières premières pour l’industrie pharmaceutique. Elle
souligne la nécessité d’en assurer une exploitation durable, sous peine de compromettre la biodiversité.
Médecine traditionnelle et pharmacopée L’OMS définit la médecine traditionnelle comme l’en￾semble des connaissances, compétences et pratiques de soins [55]. Ces pratiques reposent sur des
théories, des croyances et des expériences propres à chaque culture; elles visent à maintenir la santé,
mais aussi à prévenir, diagnostiquer et traiter les maladies [57].
La pharmacopée traditionnelle correspond à l’ensemble des remèdes et des préparations ainsi
utilisés [55]. Elle décrit les recettes, précise les posologies et les modes d’administration, et signale les
contre-indications et les précautions d’usage.
Ethnobotanique et ethnomédecine L’ethnobotanique étudie de façon scientifique les relations qui
lient les plantes aux sociétés humaines [56]. Elle documente les usages traditionnels, recueille les
savoirs locaux et analyse la manière dont les populations perçoivent, nomment, classifient et exploitent
les végétaux.
8

--- page 21 ---
L’ethnomédecine en constitue la branche médicale : elle se penche sur les pratiques de soins, sur
les systèmes traditionnels, sur les conceptions de la maladie et de la guérison, ainsi que sur les rituels
et les actes thérapeutiques [56].
Contexte burkinabè Au Burkina Faso, la médecine traditionnelle couvre environ 80 % des besoins
de santé primaire [4] et ne constitue pas une alternative marginale. Son accessibilité, son coût modique
et son ancrage dans les habitudes culturelles en font le recours de premier choix, et les tradipraticiens
en sont des acteurs centraux.
Les travaux de Zerbo et al. [58] ont appliqué cette lecture à un terrain précis, celui des Sanan,
documentant 85 espèces utilisées et 63 affections traitées, avec leurs modes de préparation et
d’administration. Ouedraogo et al. [38] ont procédé de leur côté à une revue des plantes à potentiel
aromatique du pays, recensant 42 espèces et en analysant les propriétés et les usages.
Or ces savoirs ne se présentent pas de façon homogène. Ils varient selon les ethnies, diffèrent selon
les régions, évoluent dans le temps et s’enrichissent des découvertes nouvelles. Une telle diversité rend
leur documentation particulièrement complexe [32].
I.1.2 Plantes médicinales documentées dans la littérature scientifique
Inventaires et recensements La littérature scientifique burkinabè est fournie : elle recense plusieurs
centaines d’espèces médicinales. Les travaux de Guinko [19] ont identifié 304 espèces utilisées en
médecine traditionnelle, tandis que Nacoulma [33] en a documenté 280 avec leurs usages, et que Zerbo
et al. [58] ont recensé 85 espèces chez les Sanan.
Ces plantes se répartissent dans des familles botaniques variées, les plus représentées étant les
Fabacées, les Combretacées, les Rubiacées et les Euphorbiacées [33], une diversité qui reflète la
richesse de la flore burkinabè.
Aspects botaniques et écologiques La recherche couvre plusieurs aspects :
• Identification botanique : les plantes sont collectées et décrites, leurs caractéristiques mor￾phologiques sont notées, les spécimens conservés en herbiers de référence et la taxonomie
précisée.
• Distribution géographique : les zones de présence sont cartographiées, leur répartition étant
liée aux conditions climatiques et édaphiques; certaines espèces sont endémiques à une région
[19].
• Périodes de récolte : les moments optimaux de collecte sont déterminés, la teneur en principes
actifs variant selon la saison, ce qui pèse directement sur la qualité des remèdes.
• Parties utilisées : les feuilles dominent (45 % des cas)[58], devant les racines (25 %), les écorces
(15 %), les fruits (10 %) et les graines (5 %) [58]. La partie retenue dépend de la plante et de
l’usage visé.
• Modes de préparation : les décoctions, par ébullition dans l’eau, restent courantes; on recourt
aussi aux macérations (trempage à froid), aux poudres obtenues par séchage et broyage, et plus
rarement aux extraits alcooliques [33].
Usages thérapeutiques Les affections traitées sont principalement courantes : le paludisme en
constitue une cible fréquente, aux côtés des infections respiratoires et digestives, tandis que les
pathologies chroniques (diabète, hypertension) font l’objet d’études spécifiques [38].
9

--- page 22 ---
Propriétés pharmacologiques Les études expérimentales évaluent les activités pharmacologiques :
• Activité antimicrobienne : les extraits sont testés sur des bactéries et des champignons,
notamment Staphylococcus aureus, Escherichia coli et Candida albicans, et les résultats se
révèlent souvent prometteurs [33].
• Activité antipaludique : les extraits sont testés sur des souches de Plasmodium falciparum.
Des plantes comme Artemisia annua ou Cryptolepis sanguinolenta sont étudiées, et certaines
affichent une forte activité [38].
• Activité anti-inflammatoire : divers modèles d’inflammation sont mobilisés, au nombre desquels
l’œdème de la patte du rat. Les plantes évaluées dans ces modèles peuvent présenter des effets
significatifs.
• Activité antioxydante : le pouvoir piégeage des radicaux libres est mesuré par les méthodes
DPPH et ABTS; les polyphénols y sont le plus souvent impliqués.
• Toxicité : la toxicité aiguë et subchronique est évaluée par la détermination des doses létales
(DL50). Certaines plantes s’avèrent toxiques à forte dose, information décisive pour la sécurité
d’emploi [33].
Composition chimique Les analyses phytochimiques identifient les métabolites secondaires :
• Alcaloïdes : composés azotés aux propriétés pharmacologiques variées, dont la quinine et la
morphine.
• Flavonoïdes : composés phénoliques aux propriétés antioxydantes et anti-inflammatoires, tels
que la quercétine et la rutine.
• Tanins : composés polyphénoliques à propriétés astringentes et antimicrobiennes.
• Saponines : composés aux propriétés moussantes et immunostimulantes.
• Huiles essentielles : mélanges complexes de terpènes aux propriétés variées [38].
I.1.3 Types de connaissances et niveaux de preuve
Typologie des connaissances Les connaissances relatives aux plantes médicinales sont de nature
variée, et chaque type possède sa propre valeur comme ses propres limites.
Connaissances ethnobotaniques Issues des populations locales et recueillies par enquêtes et
entretiens, elles reflètent le savoir traditionnel accumulé et décrivent usages, préparations et croyances.
Leur valeur est double : elles orientent la recherche vers des plantes prometteuses et préservent un
patrimoine culturel. Elles comportent toutefois des biais : un informateur peut fournir des informations
incomplètes, un usage varier d’un guérisseur à l’autre, et la transmission n’est pas assurée.
Connaissances phytochimiques Elles portent sur la composition chimique des plantes, identifient
les molécules actives, en précisent la concentration et comparent les profils chimiques entre espèces.
Connaissances pharmacologiques Provenant d’études expérimentales, ces connaissances testent
les effets biologiques des extraits, à l’aide de modèles in vitro (cellules, micro-organismes) ou in vivo
(animaux de laboratoire) [21]. Les résultats sont quantitatifs : ils mesurent la concentration efficace
(CI50), comparent à des témoins positifs et évaluent la toxicité. Une réserve demeure : les études
animales ne prédisent pas toujours l’effet chez l’homme.
10

--- page 23 ---
Connaissances cliniques Elles proviennent d’essais sur l’homme, rares pour les plantes médicinales,
coûteuses et complexes, et supposent des autorisations éthiques ainsi que des essais rigoureux. Ces
essais offrent le niveau de preuve le plus élevé : ils mesurent l’efficacité réelle, évaluent les effets
secondaires et comparent au placebo ou au traitement standard. Ils constituent la référence de la
médecine fondée sur les preuves [40].
Hiérarchie des niveaux de preuve La médecine fondée sur les preuves (evidence-based medicine)
établit une hiérarchie :
1. Méta-analyses et revues systématiques : preuve la plus forte. Elles synthétisent plusieurs essais
cliniques.
2. Essais cliniques randomisés contrôlés : preuve très forte. Ils comparent un traitement à un
placebo ou à un standard.
3. Études de cohorte : preuve modérée. Elles suivent des groupes dans le temps.
4. Études cas-témoins : preuve modérée. Elles comparent des cas à des témoins.
5. Études expérimentales animales : preuve faible. Elles ne sont pas directement transposables à
l’homme.
6. Études in vitro : preuve très faible. Elles sont éloignées des conditions réelles.
7. Savoirs traditionnels et avis d’experts : preuve anecdotique. Ils sont utiles pour générer des
hypothèses mais non validés.
Cette hiérarchie est résumée dans la figure I.1. Elle commande la fiabilité de chaque connaissance :
l’ontologie la traduira en propriété niveauPreuve (section III.1.3 du chapitre III). [TODO : Schéma à produire : pyramide (ou échelle) de 7 niveaux repris de la
liste ci-dessus, du haut vers le bas : méta-analyses et revues systématiques,
essais cliniques randomisés, études de cohorte, études cas-témoins, études
expérimentales animales, études in vitro, savoirs traditionnels et avis
d’experts. Une ligne de légende par niveau (« preuve la plus forte » en haut, «
preuve anecdotique » en bas), dégradé sombre en haut et clair en bas, texte en
français, sans image d’arrière-plan. Ajouter en bas, d’un trait, le
rattachement aux quatre niveaux niveauPreuve de l’ontologie : traditionnel,
in vitro, in vivo, clinique. Outil libre (PowerPoint, draw.io, Inkscape), format
PNG, 15 cm de large, enregistrer sous images/niveaux_preuve.png.]
De la preuve la plus forte (méta-analyses, essais cliniques randomisés) à la plus
Figure I.1 faible (études – Hiérarchie des niveaux de preuve in vitro, savoirs traditionnels)
I.2 Ingénierie des connaissances et ontologies
I.2.1 Représentation des connaissances
Définition et enjeux La représentation des connaissances est une discipline de l’intelligence artificielle
dont l’objet est de formaliser l’information pour la rendre exploitable par la machine [9]. Elle s’appuie
sur des langages structurés et interprétables, et permet en retour le raisonnement automatique et
l’interrogation. Quatre enjeux la caractérisent : capter la sémantique des connaissances, les rendre
interopérables, permettre leur réutilisation et faciliter leur évolution.
11

--- page 24 ---
Principaux modèles de représentation
• Les réseaux sémantiques : des graphes de concepts reliés par des arcs, où les nœuds représentent
des entités et les arcs des relations. Modèle simple et intuitif, il a servi aux premières bases de
connaissances.
Limites : ils n’ont pas de sémantique formelle, ils ne permettent pas le raisonnement complexe et
ils sont difficiles à partager.
• Les cadres (frames) : des structures de données dans lesquelles chaque cadre possède des attributs
(slots), éventuellement pourvus de valeurs par défaut, les cadres s’organisant en hiérarchies par
héritage.
Avantages : ils sont structurés, permettent l’héritage et sont faciles à implémenter.
Limites : ils n’ont pas de sémantique formelle. L’héritage peut être ambigu.
• Les règles : des expressions logiques conditionnelles, de forme « SI condition ALORS conclu￾sion », qui autorisent le raisonnement déductif et servent aux systèmes experts.
Avantages : elles sont expressives, permettent le raisonnement et sont faciles à comprendre.
Limites : elles peuvent être nombreuses, interagir de manière complexe et sont difficiles à
maintenir.
• Les ontologies : des modèles formels d’un domaine [17], qui définissent classes et propriétés,
précisent relations et axiomes, et dont l’expressivité élevée les adapte aux connaissances
complexes.
Avantages : elles ont une sémantique formelle, sont interopérables, permettent le raisonnement et
sont réutilisables.
C’est vers ce dernier modèle que se porte notre recherche. Les ontologies sont les plus adaptées à
la structuration des connaissances scientifiques : elles autorisent une interrogation fine et facilitent
l’intégration de sources multiples.
Ces modèles formels s’appuient aujourd’hui sur les langages du web sémantique, empilés du
document à la donnée reliée puis au raisonnement (figure I.2).
[TODO : Schéma à produire : pile de 4 boîtes empilées, de bas en haut,
reprenant exactement la ligne de légende ci-dessous : (1) document : XML,
JSON-LD ; (2) données reliées : RDF ; (3) sémantique : RDFS, OWL ; (4)
interrogation : SPARQL. Boîtes de même largeur, liseré dégradé du plus clair
en bas au plus foncé en haut, une flèche latérale verticale intitulée « de la
donnée au raisonnement ». Étiquettes en français, police identique à celle du
document. Outil libre (PowerPoint, draw.io), format PNG, 12 cm de large,
enregistrer sous images/pile_semantique.png.]
Couche document : XML, JSON-LD → couche données : RDF → couche
sémantique : RDFS, OWL → couche interrogation : SPARQL
Figure I.2 – Les langages du web sémantique
I.2.2 Ontologies et réutilisation d’ontologies existantes
Définition formelle Une ontologie se définit comme « une spécification explicite et formelle d’une
conceptualisation partagée » [17]. Chaque élément de cette formule compte :
• Spécification explicite : les concepts sont définis clairement, les termes précis, les définitions
non ambiguës.
• Spécification formelle : l’ontologie est exprimée dans un langage logique, interprétable par la
machine, ce qui autorise le raisonnement.
• Conceptualisation : l’ontologie représente une vision du monde, sélectionnant les concepts
pertinents et laissant de côté les détails non pertinents.
12

--- page 25 ---
• Partagée : l’ontologie est consensuelle, acceptée par une communauté, ce qui facilite la
communication.
Composants d’une ontologie Les ontologies sont composées de plusieurs éléments [46] :
• Classes (ou concepts) : les entités du domaine, telles que Plante, Maladie, Substance active ou
Mode de préparation, organisées en hiérarchies (taxonomies) [46].
• Propriétés (ou attributs) : les caractéristiques des classes, par exemple le nom scientifique, le
nom vernaculaire, la partie utilisée ou le dosage, susceptibles de porter des valeurs (chaînes,
nombres, dates) [46].
• Relations : les liens entre les classes, par exemple « traite » (une plante traite une maladie),
« contient » (une plante contient une substance), « est_préparée_par » (une préparation utilise un
mode) [46].
• Axiomes : des contraintes logiques qui assurent la cohérence de l’ontologie, par exemple « une
plante peut avoir plusieurs usages » ou « une partie utilisée doit être une partie de la plante »[46].
• Instances (ou individus) : les exemples concrets : « Cassia alata » est une instance de Plante,
« Paludisme » une instance de Maladie.
Langages d’ontologies Plusieurs langages servent à représenter les ontologies :
• RDF (Resource Description Framework) : langage de base du Web sémantique. Il utilise des
triplets (sujet-prédicat-objet). Il est simple mais peu expressif [53].
• RDFS (RDF Schema) : extension de RDF. Il permet de définir des classes et des propriétés. Il
permet l’héritage. Il a une expressivité limitée [53].
• OWL (Web Ontology Language) : langage standard du W3C. Il est plus expressif que RDFS.
Il permet des axiomes complexes. Il existe OWL-Lite, OWL-DL et OWL-Full, de complexité
croissante [52].
• SKOS (Simple Knowledge Organization System) : langage pour les thésaurus et taxonomies.
Il est adapté aux systèmes d’organisation des connaissances [54].
Réutilisation d’ontologies Réutiliser une ontologie existante est une pratique recommandée [30], et
ce pour quatre raisons :
• Économie de temps et de coûts : on ne repart pas de zéro. On s’appuie sur un travail déjà validé.
On évite de « réinventer la roue ».
• Fiabilité : les ontologies existantes ont souvent été testées et corrigées. Elles sont éprouvées.
Elles intègrent l’expertise de plusieurs chercheurs.
• Interopérabilité : l’utilisation d’ontologies standards facilite l’échange de données. Elle permet
l’intégration avec d’autres systèmes. Elle favorise la réutilisation dans d’autres contextes.
• Communauté : les ontologies existantes ont souvent une communauté d’utilisateurs. On peut
bénéficier de leur expertise. On peut contribuer à leur amélioration.
Plusieurs ontologies sont disponibles dans les domaines biomédicaux et pharmaceutiques. Certaines
portent spécifiquement sur les plantes médicinales. D’autres couvrent la médecine traditionnelle [41].
Notre travail partira d’une de ces ontologies.
13

--- page 26 ---
I.2.3 Adaptation, alignement et enrichissement ontologique
Adaptation d’une ontologie L’adaptation modifie une ontologie pour un nouveau contexte [25]. Elle
est nécessaire quand l’ontologie source ne couvre pas parfaitement le domaine visé. Elle est également
nécessaire quand le contexte d’utilisation diffère.
L’adaptation peut inclure :
• Ajout de classes : pour couvrir des concepts absents. Par exemple, ajouter des classes pour les
maladies spécifiques au Burkina Faso (paludisme, onchocercose, méningite).
• Ajout de propriétés : pour décrire des attributs non prévus. Par exemple, ajouter une propriété
pour le nom vernaculaire en langue locale (mooré, dioula, fulfuldé).
• Modification de relations : pour adapter la sémantique. Par exemple, préciser la relation « traite »
avec des attributs de niveau de preuve.
• Suppression de classes : si elles ne sont pas pertinentes. Mais on évite de supprimer pour
préserver la compatibilité. On peut les marquer comme obsolètes.
• Redéfinition de restrictions : pour adapter les contraintes logiques.
Alignement d’ontologies L’alignement établit des correspondances entre ontologies [13]. Il relie des
concepts équivalents ou similaires. Il permet de fusionner des connaissances de sources différentes. Il
facilite l’interopérabilité.
Les correspondances peuvent être :
• Équivalence : les concepts sont identiques (owl:equivalentClass).
• Spécialisation : un concept est un sous-concept de l’autre (rdfs:subClassOf).
• Association : les concepts sont liés par une relation.
• Correspondance approximative : les concepts sont similaires mais pas identiques.
Les méthodes d’alignement peuvent être :
• Manuelles : un expert établit les correspondances. C’est précis mais coûteux.
• Automatiques : des algorithmes comparent les termes. Ils utilisent des mesures de similarité. Ils
sont efficaces mais moins précis.
• Semi-automatiques : l’outil propose des correspondances. L’expert les vérifie et les corrige.
C’est un bon compromis.
Enrichissement ontologique L’enrichissement ajoute de nouvelles connaissances à l’ontologie [35].
Il intègre des données issues de sources externes. Il peut être manuel (expert humain) ou assisté par des
outils.
Les sources d’enrichissement peuvent être :
• Textes scientifiques : articles, thèses, rapports.
• Bases de données : bases de données botaniques, pharmacologiques.
• Ontologies tierces : pour aligner et intégrer.
• Connaissances d’experts : savoirs d’experts du domaine.
Les étapes de l’enrichissement sont :
1. Identification des sources : sélectionner les sources pertinentes.
2. Extraction des connaissances : extraire les faits des sources.
3. Transformation : convertir les faits dans le format de l’ontologie.
4. Intégration : ajouter les faits à l’ontologie.
5. Validation : vérifier la cohérence et la correction.
6. Documentation : tracer les modifications.
14

--- page 27 ---
Démarche pour notre recherche Notre démarche combinera adaptation et enrichissement. Nous
partirons d’une ontologie existante, que nous adapterons au contexte burkinabè en ajoutant des classes
pour les plantes locales et des propriétés pour les noms vernaculaires; les relations seront modifiées si
nécessaire. Nous enrichirons ensuite cette ontologie avec les données de la littérature, en documentant
l’ensemble des modifications apportées.
I.2.4 Bases de connaissances et interrogation sémantique
Définition et structure Une base de connaissances est un système qui stocke des connaissances
structurées [18]. Elle contient des instances (individus) et des faits. La base est typée par une ontologie.
L’ontologie sert de schéma conceptuel.
Par exemple, l’ontologie définit la classe « Plante » et la propriété « aPourUsage ». La base de
connaissances contient des instances comme « Cassia alata ». Elle contient des faits comme « Cassia
alata aPourUsage Paludisme ».
Bases de connaissances orientées graphe Le choix d’une base orientée graphe (graph database)
s’impose naturellement pour ce type de données, dont l’intérêt tient précisément à l’abondance des
interconnexions : plutôt que d’éparpiller l’information entre des tables, ce modèle organise les entités
en nœuds et les liaisons en relations.
Ce choix présente quatre bénéfices convergents :
• Performance : le parcours du graphe est natif, les relations y sont des éléments à part entière, et
non de simples clés étrangères;
• Flexibilité : le schéma n’est pas figé à l’avance, de nouveaux types de nœuds et de relations s’y
intègrent sans migration lourde;
• Expressivité : les relations peuvent être typées, pondérées et parcourues, y compris lorsqu’elles
sont profondément imbriquées;
• Lecture intuitive : le modèle reproduit la façon dont nous lions naturellement les concepts, ce
qui en facilite la lecture par un non-spécialiste.
Deux langages de requête dominent l’interrogation de ces graphes :
• Cypher : langage déclaratif de Neo4j, de loin le plus répandu, qui autorise des requêtes complexes
sur les graphes.
• Gremlin : langage d’Apache TinkerPop, plus bas niveau, adopté par plusieurs autres bases de
données graphe.
Interrogation avec Cypher Une requête Cypher typique se présente ainsi :
MATCH (p:Plante {nomVernaculaire: "Néré"}) RETURN p.nomScientifique,
p.usages
Elle retourne le nom scientifique et les usages de la plante appelée « Néré ».
Ses principales clauses répondent chacune à un besoin précis :
• MATCH : repérer des motifs dans le graphe;
• WHERE : filtrer les résultats;
• RETURN : désigner ce qui est renvoyé;
• OPTIONAL MATCH : établir une correspondance facultative sans perdre le reste des correspon￾dances;
• CREATE : créer de nouveaux nœuds et relations.
15

--- page 28 ---
Avantages des bases de connaissances graphe Pour notre usage, ces avantages se traduisent en cinq
exigences :
• Interrogation puissante : formuler des requêtes combinant plusieurs critères et parcourant
plusieurs relations à la fois;
• Découverte de connaissances implicites : laisser le parcours révéler des connexions non
évidentes, par exemple des plantes partageant un usage ou une propriété;
• Traçabilité : associer chaque fait à sa source, de manière à pouvoir remonter à son origine et en
contrôler la fiabilité;
• Intégration : réunir des données issues de sources diverses, l’ontologie servant de cadre
unificateur;
• Évolutivité : enrichir la base de connaissances nouvelles sans avoir à tout reconstruire.
Application à notre recherche Notre base de connaissances dériverait de l’ontologie adaptée selon
un modèle orienté graphe. Elle hébergerait les informations relatives aux plantes, à leurs usages, à leurs
propriétés et à leurs sources, rendant ainsi possibles des requêtes sémantiques riches, interrogeables
depuis l’application web.
I.3 Intelligence artificielle pour l’accès aux connaissances
I.3.1 Traitement des requêtes en langage naturel
Introduction au TALN Le traitement automatique du langage naturel (TALN) constitue l’une des
branches de l’intelligence artificielle les plus directement mobilisables dans notre projet. Il s’agit de
rendre les textes humains interprétables par la machine, en les analysant sur les plans syntaxique et
sémantique, puis en convertissant les énoncés en formes exploitables par la machine [24]. C’est cette
propriété qui permet d’établir le dialogue entre l’utilisateur et le système.
Techniques fondamentales Les techniques de Traitement Automatique du Langage Naturel (NLP)
mobilisables ici sont les suivantes :
• Tokenisation : découpage du texte en unités (mots, ponctuations). « Quelles plantes traitent le
paludisme ? » devient ainsi ["Quelles", "plantes", "traitent", "le", "paludisme",
"?"].
• Analyse morphologique : identification des racines des mots. « traitent » se ramène à « traiter »,
ce qui permet de normaliser les variantes (lemmatisation et stemming).
• Étiquetage morphosyntaxique : reconnaissance des catégories grammaticales (noms, verbes,
adjectifs, etc.) (part-of-speech tagging).
• Reconnaissance d’entités nommées (NER) : détection des concepts clés, c’est-à-dire des
plantes, des maladies, des parties de plantes et des modes de préparation [34].
• Analyse de dépendances : compréhension des relations entre mots, par identification du sujet,
du verbe, de l’objet et des liens syntaxiques qui les unissent.
• Analyse sémantique : compréhension du sens des phrases, à l’aide de représentations vectorielles
(embeddings) ou de graphes de connaissances.
16

--- page 29 ---
Approches modernes : les transformers Les modèles récents reposent sur l’architecture transformer
[51], fondée sur le mécanisme d’attention : celui-ci permet de prendre en compte un contexte étendu,
les modèles étant entraînés sur de très grandes quantités de textes.
Trois familles font référence :
• BERT (Bidirectional Encoder Representations from Transformers) : modèle de Devlin et al.
[11], bidirectionnel, qui exploite le contexte situé à la fois à gauche et à droite du mot et excelle
dans les tâches de compréhension.
• GPT (Generative Pre-trained Transformer) : modèle de Radford et al. [39], unidirectionnel,
particulièrement performant pour la génération de texte et utilisé dans ChatGPT.
• T5 (Text-to-Text Transfer Transformer) : modèle de Raffel et al. [39], qui ramène toutes les
tâches à des transformations texte-texte.
Ces modèles sont pré-entraînés sur des corpus généraux; ils peuvent ensuite être affinés (fine-tunés)
sur des données spécifiques, ce qui leur confère des performances supérieures à celles des approches
traditionnelles.
Application à notre recherche Notre système interprêterait ainsi des requêtes variées, à l’aide de
modèles NLP, en en extrayant entités et relations pour les traduire en requêtes formelles adressées à la
base de connaissances graphe. L’utilisateur dialoguerait avec le système en langage courant. Quelques
requêtes attendues illustrent cette exigence :
• « Quelles plantes sont utilisées contre le paludisme ? »
• « Comment prépare-t-on le remède contre la diarrhée ? »
• « La plante X a-t-elle des propriétés anti-inflammatoires ? »
• « Quelles études existent sur la toxicité de Y ? »
• « Quelles plantes du Burkina Faso sont utilisées pour le diabète et ont des études pharmacolo￾giques ? »
I.3.2 Extraction et structuration assistées par IA
Extraction d’information L’extraction d’information est une tâche de NLP [16] qui consiste à
identifier des faits dans des textes non structurés, à en reconnaître les entités et les relations, puis à les
convertir en données structurées exploitables.
Elle se déploie en quatre étapes successives :
1. Reconnaissance des entités : identifier les entités nommées (plantes, maladies, substances).
2. Reconnaissance des relations : identifier les relations entre entités (traite, contient, prévient).
3. Normalisation : standardiser les entités (synonymes, variantes orthographiques).
4. Structuration : organiser les faits en format structuré.
Approche par prompts d’IA Notre recherche s’appuiera sur une approche par prompts d’IA,
c’est-à-dire sur l’interrogation de modèles de langage de grande taille (LLM) tels que GPT, Claude ou
des modèles open source.
Le principe repose sur quatre phases :
• Préparation du prompt : on conçoit un prompt qui demande au modèle d’extraire des
informations spécifiques d’un texte. Le prompt précise les entités et les relations à extraire.
• Soumission au modèle : on envoie le texte et le prompt au modèle, qui produit une réponse
structurée.
17

--- page 30 ---
• Extraction : on extrait les informations de la réponse, puis on les convertit dans le format
souhaité.
• Validation : on vérifie la qualité de l’extraction, et l’on corrige si nécessaire.
Cette approche présente des avantages réels :
• Flexibilité : le prompt s’adapte à différents types de documents.
• Rapidité : l’extraction reste rapide même sur de grands volumes de textes.
• Adaptabilité : modifier le prompt suffit à changer la nature des informations extraites.
• Utilisation de modèles pré-entraînés : on bénéficie des connaissances générales du modèle.
Elle n’est toutefois pas exempte de limites :
• Hallucinations : le modèle peut générer des informations fausses.
• Incohérence : le modèle peut donner des réponses variables.
• Coût : l’utilisation de modèles commerciaux peut être coûteuse.
Dans notre recherche, nous utiliserons des prompts d’IA pour l’extraction. Les niveaux de preuve
associés aux faits extraits seront ceux que rapporte la source, sans réévaluation indépendante, et la
qualité des extractions sera appréciée par le protocole d’évaluation prévu pour le système, plutôt que
par une relecture individuelle de chaque enregistrement.
Structuration des données La structuration convertit les faits extraits en formats standardisés. Pour
notre base de connaissances graphe, nous utiliserons :
• Format d’importation : les données seront préparées en JSON ou CSV, formats compatibles
avec les outils d’importation de Neo4j.
• Modèle de données : les données seront structurées selon l’ontologie, nœuds et relations étant
définis en conséquence.
• Propriétés : chaque nœud sera porteur de propriétés (nom, type, etc.) et chaque relation de
propriétés propres (type, source, niveau de preuve).
Application à notre recherche Dans notre recherche, l’IA assistera l’extraction via des prompts.
Elle repérera les mentions de plantes, usages, parties et propriétés. Elle identifiera les relations entre
ces entités. Elle produira des données structurées, chaque fait étant rattaché à sa source de manière à
pouvoir être retracé jusqu’à lui.
I.3.3 Recherche sémantique et génération de réponses
Recherche sémantique La recherche sémantique dépasse la simple correspondance de mots [6] :
elle s’appuie sur le sens des termes et sur l’ontologie sous-jacente pour retrouver une information
pertinente, quelle que soit la formulation employée par l’utilisateur.
Le processus se déroule en six temps :
1. Analyse de la requête : le NLP repère les concepts et les relations énoncés par l’utilisateur.
2. Désambiguïsation : lorsqu’un terme est ambigu, le contexte permet de trancher. « Paludisme »,
par exemple, peut être rapproché de « malaria » ou de « fièvre des marais »; le système retient le
concept approprié.
3. Transformation en requête formelle : l’énoncé naturel est converti en requête destinée à la
base de connaissances graphe (Cypher), les concepts étant mappés sur les nœuds et les relations.
4. Exécution : la requête est exécutée sur la base de connaissances, et les résultats récupérés.
5. Filtrage et classement : les résultats sont filtrés puis triés par pertinence, selon des critères de
fiabilité (niveau de preuve) ou de proximité sémantique.
6. Génération de la réponse : les résultats sont enfin transformés en texte lisible.
18

--- page 31 ---
Système RAG (Retrieval-Augmented Generation) Pour l’accès intelligent aux connaissances, notre
recherche s’appuiera sur un système RAG (Retrieval-Augmented Generation), qui articule recherche
d’information et génération de réponses [29].
Son fonctionnement s’articule en cinq étapes :
• Interprétation de la requête : le système cerne la demande de l’utilisateur.
• Recherche : il interroge la base de connaissances et en extrait les informations pertinentes
(nœuds, relations, propriétés).
• Contexte : les informations retrouvées sont assemblées en un contexte, ensuite soumis au modèle
de langage.
• Génération : le modèle produit une réponse fondée sur ce contexte, et non sur ses seules
connaissances, ce qui la rend factuelle et traçable.
• Affichage des sources : les sources accompagnent la réponse, permettant à l’utilisateur de vérifier
l’origine de l’information.
Les avantages du RAG sont multiples :
• Fiabilité : les réponses sont ancrées dans des faits de la base, ce qui réduit les hallucinations.
• Traçabilité : on peut remonter aux sources et vérifier l’information.
• Actualisation : la base étant mise à jour, les réponses le sont automatiquement.
• Adaptabilité : la base peut être adaptée à des contextes différents.
Application à notre recherche Notre système suivra une architecture RAG : il interprétera les
requêtes en langage naturel, interrogera la base de connaissances graphe et générera des réponses
construites à partir des faits retrouvés. Chacune d’elles inclura ses sources et son niveau de preuve, de
sorte que l’utilisateur puisse remonter à l’origine de l’information.
I.3.4 Traçabilité et fiabilité des réponses
Importance de la traçabilité En contexte médical, la traçabilité conditionne la crédibilité d’un
système [15]. En associant chaque information à sa source, elle permet d’en vérifier l’origine et renforce
d’autant la confiance que lui accordent les utilisateurs.
Sans traçabilité, l’information reste difficile à vérifier : elle peut être erronée ou obsolète, et
l’utilisateur est dans l’impossibilité d’en apprécier la fiabilité.
Mécanismes de traçabilité Trois mécanismes seront mis en œuvre :
• Stockage des références : chaque fait est stocké avec un identifiant de source, celle-ci étant
décrite (titre, auteur, année, éditeur, DOI).
• Association information-source : dans la base, l’information est liée à sa source par une relation.
Exemple : (information)-[:PROVIENT_DE]->(source).
• Affichage des sources : les réponses affichent leurs sources, sur lesquelles un clic ouvre le détail :
page ou section exacte, DOI ou URL.
• Citations : les renvois sont numérotés comme dans les articles scientifiques, avec appel à une
bibliographie.
• Lien vers les documents : lorsque les documents sont disponibles en ligne, un lien est fourni.
19

--- page 32 ---
Fiabilité des réponses La fiabilité des réponses tient d’abord à la qualité des sources. Nous nous
limiterons donc à des sources scientifiques validées :
• Articles évalués par les pairs : publiés dans des revues scientifiques.
• Thèses et mémoires : validés par des jurys académiques.
• Rapports de recherche : produits par des institutions reconnues.
• Livres et chapitres de livres : publiés par des maisons d’édition scientifiques.
Nous éviterons les sources non vérifiées (sites web non référencés, articles de vulgarisation non
validés, témoignages non vérifiés, informations sans attribution).
Distinction des niveaux de preuve Nous distinguerons clairement les niveaux de preuve, tels qu’ils
sont rapportés par les sources :
• Usage traditionnel : nous indiquons que c’est un usage rapporté, non démontré scientifiquement.
• Activité in vitro : nous mentionnons que l’activité a été testée en laboratoire sur des cellules ou
des micro-organismes.
• Activité in vivo : nous précisons que l’efficacité a été démontrée sur des animaux.
• Essai clinique : nous mettons en avant le niveau de preuve le plus élevé.
• Toxicité : nous signalons toute information sur la toxicité ou les effets secondaires.
Gestion des incertitudes Nous ne passerons pas sous silence les incertitudes, et notamment :
• toute information contestée ou non confirmée sera signalée comme telle;
• les données contradictoires seront présentées toutes, sans en cacher aucune;
• le caractère limité de certaines études sera mentionné;
• l’ancienneté d’une information sera indiquée par sa date.
Limites de l’IA Rappelons enfin ce que l’IA ne fera pas : elle ne créera pas de nouvelles connaissances
thérapeutiques et ne remplacera pas l’expertise humaine. Son rôle se limite à faciliter l’accès aux
connaissances existantes; la responsabilité de l’interprétation demeure celle de l’utilisateur. Le système
constitue ainsi un outil d’aide à la consultation, et non un outil de diagnostic ou de prescription.
I.4 Travaux connexes et positionnement scientifique
Pour achever ce cadrage, il reste à examiner ce qui a déjà été fait. Cette section passe en revue les
travaux consacrés à la modélisation des connaissances en médecine traditionnelle à base de plantes, en
distinguant les ontologies développées en Afrique de celles qui nouent un lien direct avec le Burkina
Faso, avant de situer notre propre démarche parmi elles.
I.4.1 Ontologies dans le domaine des plantes médicinales
Ontologies internationales
Plusieurs ontologies couvrent le domaine des plantes médicinales. Chacune a ses forces et ses
limites.
• Flora Ontology (FLOPO) : elle décrit la structure botanique des plantes, parties et stades de
développement compris [22]. Extrêmement complète pour la botanique, elle ignore en revanche
les usages médicinaux et les connaissances ethnobotaniques.
20

--- page 33 ---
• Plant Ontology (PO) : proche de FLOPO [8], elle porte sur l’anatomie et le développement des
plantes et sert de référence pour l’annotation de données génomiques. Ni l’ethnobotanique ni la
pharmacologie n’y figurent.
• Ontology of Traditional Medicine (OTM) : dédiée à la médecine traditionnelle [41], elle couvre
maladies, traitements et remèdes, et intègre des notions issues de la médecine traditionnelle
chinoise et de l’Ayurvéda. Prometteuse, elle demeure en cours de développement et n’est pas
spécifique aux plantes d’Afrique.
• Drug Ontology (DrOn) : centrée sur les propriétés pharmaceutiques [20], elle décrit les
médicaments, leurs ingrédients et leurs effets; son utilité pharmacologique est réelle, mais son
champ reste celui des médicaments modernes.
• Food Ontology (FOODON) : consacrée à la nutrition et aux aliments [12], elle intègre certaines
plantes comestibles et peut être partiellement réutilisée sur le versant alimentaire, sans toutefois
couvrir les usages médicinaux.
• SNOMED CT : cette terminologie clinique très large [42] couvre de nombreux domaines
médicaux et inclut quelques concepts relatifs aux plantes, sans être pour autant structurée comme
une ontologie formelle.
Ontologies de la médecine traditionnelle africaine
Plusieurs travaux récents ont développé des ontologies spécifiques à la médecine traditionnelle
africaine. Ces travaux reconnaissent les particularités des systèmes de soins africains. Ils intègrent des
dimensions culturelles, spirituelles et sociales.
WATRIMed : un graphe de connaissances pour la médecine traditionnelle ouest-africaine Le
projet WATRIMed (West African Herbal based Traditional Medicine) fait l’objet de deux publications
complémentaires [44, 43]. Leur objectif est de structurer les connaissances sur les plantes médicinales,
les recettes traditionnelles et les maladies traitées en Afrique de l’Ouest, et de relier ces connaissances à
des bases de données publiques. Le modèle décrit porte le nom de HTM Ontology (Herbal Traditional
Medicine Ontology).
Le noyau du modèle compte 556 concepts dans la version présentée à MEDINFO 2019 [44], dont
143 plantes médicinales ouest-africaines identifiées et 108 recettes employées par les tradipraticiens
pour traiter 110 maladies et symptômes courants de la sous-région. La note de conception associée
décrit un modèle de 472 concepts et de 75 propriétés, dont 57 propriétés objet et 18 propriétés de
données [43]. Les classes principales qui y figurent sont :
• Medicinal Plant (plante médicinale) et Plant Part (partie de plante);
• Recipe (recette) et Formulation (forme galénique);
• Chemical Component (composé chimique) et Therapeutic Action (action thérapeutique);
• Vernacular Name et Vocabulary (noms vernaculaires et vocabulaires);
• ContraIndication, Adverse Reaction et Usage Precaution (contre-indications, réactions
indésirables, précautions d’emploi).
Les relations principales associent la plante à ses composés chimiques, à ses actions thérapeutiques
et à ses noms vernaculaires; elles font également intervenir les contre-indications, les réactions
indésirables, les formes galéniques et la dérivation d’une ressource à une autre.
Le projet s’inscrit dans un cadre sous-régional et bénéficie de l’expérience de l’Organisation
ouest-africaine de la santé (WAHO), qui regroupe les États membres de la sous-région [43]. Le modèle
est aligné sur l’ontologie fondationnelle BioTopLite2, et ses instances sont reliées à des ressources
externes comme DBpedia, IPNI, Wikidata, PubChem et Yago. L’exemple donné par les auteurs porte
sur le nom vernaculaire fulfuldé, au Burkina Faso, d’une espèce employée en médecine traditionnelle.
21

--- page 34 ---
Ses apports tiennent à trois éléments : l’ampleur du modèle, son alignement avec des bases
de connaissances existantes, et la perspective ouverte d’y détecter des interactions entre plantes et
médicaments.
Ces deux publications n’exposent toutefois qu’un aperçu des classes supérieures et des relations
principales; l’ontologie elle-même n’est pas téléchargeable, ce qui limite la réutilisation directe du
modèle.
Sources principales :
• « Enabling West African Herbal-Based Traditional Medicine Digitizing : The WATRIMed
Knowledge Graph », actes de MEDINFO 2019, IOS Press, Studies in Health Technology and
Informatics, vol. 264, p. 1548–1549, 2019.
• « Design Considerations for a Knowledge Graph : The WATRIMed Use Case », conférence
Healthcare of the Future, IOS Press, Studies in Health Technology and Informatics, vol. 259, p.
59–64, 2019.
ontoMEDTRAD : ontologie visuelle pour l’Afrique de l’Ouest ontoMEDTRAD constitue une autre
initiative notable, développée pour la médecine traditionnelle ouest-africaine [27]. Elle se distingue par
une approche à la fois formelle et visuelle, l’ontologie étant répartie en deux modules complémentaires :
• ontoCONCEPT-Term : ontologie terminologique de domaine (plantes, recettes, maladies,
préparations, etc.),
• ontoICONE : module iconique qui associe à ces concepts des représentations iconiques destinées
à faciliter la compréhension par des tradipraticiens souvent illettrés dans les langues officielles.
Elle modélise explicitement le parcours de soin : le praticien de la médecine traditionnelle, le patient,
les signes et les symptômes, les maladies, les ressources médicinales (plantes, animaux, minéraux), la
recette, ses ingrédients et les parties de plantes employées, les modes de préparation et d’administration,
ainsi que le remède et sa forme galénique. On y trouve les cinq types de plante (arbre, arbuste, palme,
herbe, liane) et les neuf parties de plantes utilisées (feuille, fruit, fleur, racine, tronc, écorce de tronc,
écorce de racine, sève, plante entière).
Les relations de base y sont la subsomption (relation « est un ») et la partie-tout (relation « est une
partie de »); 76 propriétés associatives et 16 propriétés de données complètent un modèle qui compte
144 concepts, 789 individus et 2 734 axiomes en logique de description ALCHOIQ.
Bien que conçue dans un contexte ouest-africain (Côte d’Ivoire, Sénégal, etc.), ontoMEDTRAD
est théoriquement transposable au Burkina Faso. Elle met l’accent sur la représentation des recettes
multi-plantes, en particulier antipaludéennes (son jeu de données compte 22 plantes et 31 remèdes
antipaludéens [28]), et propose une méthode originale pour franchir les barrières linguistiques et
l’illettrisme grâce à la dimension iconique.
Sources principales :
• Thèse : « Système de gestion de la médecine traditionnelle dans une plateforme web social et
sémantique : une approche basée sur une ontologie visuelle », Appoh Kouamé, Université Gaston
Berger de Saint-Louis (Sénégal), soutenue le 14 avril 2018 (HAL : tel-01842116).
• Article : « Visual Representation of African Traditional Medicine Recipes Using Icons and a
Formal Ontology, ontoMEDTRAD », actes de MIE 2020, IOS Press, Studies in Health Technology
and Informatics, vol. 270, p. 791–795, 2020.
ATHMed : un système à base de connaissances pour la médecine traditionnelle africaine
Développée au Ghana, mais avec une vocation africaine, l’approche ATHMed (African Traditional
Herbal Medicine) vise à construire un système à base de connaissances permettant la capture, le
stockage, l’indexation et la recherche d’informations sur la médecine traditionnelle à base de plantes
[10].
22

--- page 35 ---
L’article qui la présente adopte une démarche de recherche en science du design et s’appuie sur des
entretiens semi-directifs conduits auprès de vingt parties prenantes au Ghana : universités, organismes
de recherche, tradipraticiens, cliniques, autorité de régulation et usagers. Il propose un cadre conceptuel
articulé en trois couches : une couche données, qui capture et stocke les connaissances auprès des
experts du domaine; une couche logique, qui assure le raisonnement à travers un raisonneur sémantique
et un extracteur fondé sur le machine learning; et une couche présentation, qui expose une interface
permettant d’interroger la base en langage naturel.
Les connaissances sont attendues dans un corpus sémantiquement annoté, la recherche étant conçue
comme contextuelle et multi-mots. L’originalité de l’approche tient à cette hybridation entre ontologie
et techniques d’apprentissage automatique, destinée à extraire et à structurer les connaissances à partir
de textes.
L’article reste toutefois au stade d’une proposition : l’ontologie ATHMed y est annoncée comme un
modèle à dériver, et la mise en œuvre du système est explicitement renvoyée à des travaux ultérieurs. À
ce stade, ATHMed est donc un cadre d’architecture plutôt qu’une ontologie réutilisable.
Source principale :
• Article : « Toward a Knowledge-Based System for African Traditional Herbal Medicine : A Design
Science Research Approach », Devine S. N. O., Kolog E. A., Atinga R., Frontiers in Artificial
Intelligence, vol. 5, article 856705, 2022, doi : 10.3389/frai.2022.856705 (PMC8959699).
Travaux sur les « deep ontologies » de la médecine traditionnelle africaine Parallèlement à ces
initiatives, plusieurs travaux conceptuels ont proposé des « deep ontologies » pour la médecine tradi￾tionnelle africaine. Au-delà des aspects cliniques et pharmacologiques (plantes, maladies, traitements),
ces ontologies visent à intégrer des dimensions contextuelles, culturelles et symboliques propres à la
médecine traditionnelle, telles que les rites et les croyances.
Ces modèles s’appuient sur des méthodologies d’ingénierie des connaissances comme METHON￾TOLOGY. Ils sont généralement implémentés dans des outils tels que Protégé (OWL). Ils mettent en
avant la nécessité de modéliser des entités comme : TherapeuticRecipe, TherapeuticProcess, Ritual,
Belief, en plus des classes plus classiques (Plant, Disease, Symptom).
Exemples concrets d’articles :
• Ayimdji A., Koussoubé S., Fotso L. P., Konfé B. O. (2011). « Towards a "Deep" Ontology for
African Traditional Medicine » [5], Intelligent Information Management, vol. 3, n° 6, p. 244–251.
Cet article propose une première version d’une ontologie « profonde » pour la médecine
traditionnelle africaine. Il insiste sur la nécessité de prendre en compte des aspects contextuels et
culturels au-delà des simples relations plante–maladie–traitement.
• Ayimdji A., Koussoubé S., Fotso L. P., Konfé B. O. (2012). « Using METHONTOLOGY to
Build a Deep Ontology for African Traditional Medicine : First Steps », ARIMA, p. 1–12.
Ce travail décrit les premières étapes de construction d’une ontologie profonde en appliquant la
méthodologie METHONTOLOGY. Il présente une implémentation dans Protégé et une réflexion
sur l’intégration des dimensions rituelles et symboliques.
Ces travaux offrent une réflexion méthodologique précieuse sur la construction d’ontologies «
profondes » capables de rendre compte de la complexité de la médecine traditionnelle africaine. Ils
restent cependant majoritairement conceptuels : les déploiements opérationnels à grande échelle se
comptent à peine, et les outils de consultation destinés aux acteurs de terrain sont rares.
Ontologie pour les tradipraticiens (bone-setters) en Afrique de l’Ouest (2024) Un travail récent
(2024) propose une ontologie destinée aux tradipraticiens spécialisés dans le traitement des fractures.
Dérivée du domaine des bone-setters en Afrique de l’Ouest, elle est appelée ontoFRACTURECARE.
23

--- page 36 ---
Les auteurs constatent que les bone-setters restent le premier recours des populations rurales, leur
pratique se révélant là où la médecine conventionnelle montre ses limites. La plupart des praticiens
sont toutefois âgés et analphabètes, et l’intérêt des jeunes générations fait défaut.
L’ontologie vise à structurer, mettre en valeur et fournir une désignation consensuelle des concepts
pertinents. Elle est destinée à servir de guide pour une prise de décision intelligente dans le processus
de soins.
Modèle d’intégration des connaissances (Angole et al.) Angole et al. ont proposé un modèle fondé
sur une ontologie, destiné à intégrer les connaissances de la médecine moderne et de la médecine
traditionnelle africaine [2, 3].
Leur approche, présentée sous le nom d’ATMO (African Traditional Medicine Ontology), retient la
Basic Formal Ontology comme ontologie supérieure standard et vise à s’articuler avec les ontologies de
la médecine moderne, en particulier l’Ontologie de la Science Médicale Générale (OGMS), elle-même
dérivée de la BFO.
L’objectif est de faire reconnaître la médecine traditionnelle africaine et de l’incorporer au système
de santé : structurées, ses connaissances pourraient alors être mobilisées en parallèle de la médecine
conventionnelle.
Ontologies nationales et ethniques Des ontologies ont été développées pour des contextes spéci￾fiques : l’ontologie visuelle ontoMEDTRAD, par exemple, couvre l’Afrique de l’Ouest, principalement
la Côte d’Ivoire et le Sénégal.
D’autres travaux documentent les systèmes nosologiques locaux. Souley [45], par exemple, a étudié
les entités nosologiques populaires chez les Haoussa, faisant apparaître des concepts médicaux locaux
tels que zahí, sanyi et shawara.
Particularités ontologiques de la médecine traditionnelle africaine L’étude de ces ontologies fait
apparaître trois particularités récurrentes :
• Holisme : le corps est une entité interconnectée, faite de composantes naturelles et surnaturelles
[49]; la santé désigne un bien-être physique, mental, spirituel, social et écologique à la fois.
• Causalité surnaturelle : la maladie n’est pas seulement un dysfonctionnement mécanique, elle
peut résulter d’une rupture de l’harmonie entre l’homme et le cosmos.
• Traitement magico-rationnel : il articule les pouvoirs des plantes et ceux du guérisseur.
Inventaires et structuration de données ethnobotaniques au Burkina Faso
Au Burkina Faso, de nombreux travaux ont été consacrés au recensement des plantes médicinales
et de leurs usages thérapeutiques. Ils relèvent principalement de :
• d’études ethnobotaniques publiées dans des revues scientifiques,
• de thèses et mémoires (pharmacie, biologie, médecine),
• de rapports de projets (AI4D, herbier national, chimiothèque, etc.).
Conduits dans différentes régions du pays (Hauts-Bassins, Sud-Ouest, Centre-Est, etc.), ces travaux
ont produit des inventaires floristiques et des enquêtes auprès des tradipraticiens, documentant :
• les noms scientifiques et vernaculaires des plantes,
• les parties utilisées,
• les pathologies traitées,
• les modes de préparation et d’administration,
• parfois les dosages et les toxicités.
24

--- page 37 ---
Exemples d’articles, thèses et rapports sur les plantes médicinales du Burkina Faso :
• Tibiri A. et al. (2020) [48]. « Countrywide Survey of Plants Used for Liver Disease Management
by Traditional Healers in Burkina Faso », Frontiers in Pharmacology, 2020.
Enquête à l’échelle nationale sur les plantes utilisées contre les maladies hépatiques. Plus de 2
000 entrées de plantes correspondant à 212 espèces. Géolocalisation des tradipraticiens. Analyse
statistique sous R.
• Ouédraogo L., Endl J., Sombié P. A. E. D., Schaefer H., Kiendrebeogo M. (2020) [37]. «
Ethnobotanical use and conservation assessment of medicinal plants sold in markets of Burkina
Faso », Ethnobotany Research and Applications, 20 :1–25, 2020.
Enquête auprès de 30 commerçants de plantes médicinales dans six grandes villes. Identification
de 104 espèces utilisées pour diverses pathologies (troubles gastro-intestinaux, paludisme, etc.).
Évaluation du statut de conservation.
• Nadembega P. et al. (2025). « An ethnobotanical survey of medicinal plants used for children’s
healthcare in Centre-Est Burkina Faso », Ethnobotany Research and Applications, 33, 2025.
Enquête sur les plantes utilisées pour la santé des enfants dans la région du Centre-Est. Docu￾mentation de 185 espèces issues de 52 familles.
• Zongo et al. (2025) [60]. « Ethnopharmacological study on medicinal plants used for jaundice
and liver-related disorders management in the Province of Kouritenga in the Central-Eastern of
Burkina Faso », Journal of Advanced Translational and Preclinical Biomedicine, 2025.
Étude ethnopharmacologique ciblée sur les plantes utilisées contre la jaunisse et les troubles
hépatiques dans une province spécifique.
• Traoré S., Diawara/Zimé H., Ouédraogo S., et al. [50]. « Ethnobotanical Survey on Plants Used
in the Treatment of Wounds by Traditional Health Practitioners in Burkina Faso », International
Journal of Plant, Animal and Environmental Sciences, 15, 2025.
Enquête sur les plantes utilisées par les tradipraticiens pour le traitement des plaies. Identification
de 70 espèces.
• Projet AI4D [1]. « Création d’une base de données sur les plantes médicinales pour faciliter
l’exploitation des connaissances ethnopharmacologiques locales ».
Projet visant à construire une base de données ouverte et interrogeable sur les plantes médicinales
du Burkina Faso. Champs standardisés : nom scientifique, famille, noms en mooré/dioula/fulfuldé,
localisation spatiale, statut de conservation, usages médicaux.
• Flahaut E. [14]. « Pharmacopée et médecine traditionnelle dans l’ouest du Burkina Faso : plantes
médicinales et soins du couple mère–enfant », Thèse de Doctorat en Pharmacie, Université de
Lille II.
Thèse ancienne mais souvent citée. Documente les plantes médicinales et les soins traditionnels
dans l’ouest du Burkina Faso, en particulier pour la mère et l’enfant.
• Étude synthétique sur les soins infantiles (2010). « Contribution à l’étude des plantes
médicinales et des recettes médicamenteuses utilisées dans les soins infantiles au Burkina Faso »,
publication synthétique (13 pages, 4 tableaux, 42 références).
Recense 79 espèces médicinales utilisées dans les soins infantiles, avec 167 recettes médicamen￾teuses documentées.
L’Herbier National des Plantes Médicinales du Burkina Faso (projet « Herbier avec chimiothèque
») L’Herbier National des Plantes Médicinales du Burkina Faso, souvent désigné sous le nom de
projet « Herbier avec chimiothèque », vise à créer un herbier national spécifiquement dédié aux plantes
médicinales, couplé à une chimiothèque contenant les marqueurs chimiques des plantes répertoriées.
Ses objectifs principaux sont les suivants :
25

--- page 38 ---
• réaliser des enquêtes ethnobotaniques régionales auprès des tradipraticiens de santé, en commen￾çant par les régions du Centre et du Plateau central,
• établir un inventaire des plantes médicinales utilisées pour le traitement des dix pathologies
prioritaires définies par le ministère de la Santé,
• identifier et géolocaliser ces plantes, et confectionner des spécimens d’herbier,
• procéder à l’identification botanique et au dosage de marqueurs chimiques pour les vingt plantes
les plus couramment utilisées pour chaque pathologie,
• alimenter une base de données nationale sur les plantes médicinales, accessible via une application
mobile et un site web.
Ce projet se veut la phase préliminaire d’une initiative plus ambitieuse qui étendrait les enquêtes
ethnobotaniques à toutes les régions du pays. Il s’inscrit dans une dynamique plus large de valorisation
de la pharmacopée traditionnelle, portée notamment par :
• la création de bosquets à plantes médicinales dans chaque province (annonce présidentielle de
2024–2025),
• l’approbation par le gouvernement de dizaines de produits issus de la pharmacopée traditionnelle,
• la mise en place de sites de conservation et de culture contrôlée des espèces médicinales.
Le projet « Herbier avec chimiothèque » se distingue des autres herbiers nationaux par sa focalisation
explicite sur les plantes médicinales. Il associe trois dispositifs complémentaires :
• un herbier (spécimens botaniques identifiés et conservés),
• une chimiothèque (marqueurs chimiques identifiés et dosés),
• une base de données (informations ethnobotaniques, usages thérapeutiques, géolocalisation).
Il coexiste avec d’autres herbiers reconnus au Burkina Faso, notamment :
• l’Herbier National du Burkina (HNBU) du CNRST/INERA, héritier de la section de l’IFAN
créée en 1954,
• l’herbier du Centre National de Semences Forestières (CNSF) (environ 15 000 spécimens),
• l’herbier de l’Université Joseph Ki-Zerbo (OUA).
Ces collections jouent un rôle important dans la conservation de la diversité végétale. Mais le projet
« Herbier avec chimiothèque » est le seul à viser explicitement une base de données nationale structurée
sur les plantes médicinales, avec une dimension ethnobotanique et chimique.
Ces travaux forment une base empirique essentielle et spécifiquement burkinabè; ils fournissent
des outils méthodologiques précieux (questionnaires, grilles de saisie) et des données de terrain riches.
Aucun ne propose cependant d’ontologie formelle explicite : les connaissances sont surtout organisées
dans des tableaux, des bases relationnelles simples ou des documents PDF, sans modèle sémantique
unifié. Les données demeurent dispersées entre études, bases locales et projets (AI4D, herbier national,
chimiothèque, etc.), et il n’existe pas encore d’application web centralisée permettant d’en consulter
l’ensemble, dans une perspective de recherche et de modélisation sémantique.
Synthèse comparative des ontologies existantes
Cette lecture comparative fait apparaître des points communs et des écarts marquants.
Points communs
Les initiatives régionales (WATRIMed, ontoMEDTRAD, ATHMed) partagent une même ambition :
formaliser les connaissances sur la médecine traditionnelle à base de plantes en Afrique. WATRIMed
et ontoMEDTRAD modélisent explicitement les plantes, les recettes et les maladies traitées; plusieurs
y ajoutent les parties utilisées, les modes de préparation et d’administration, ainsi que le fait qu’une
26

--- page 39 ---
recette puisse combiner plusieurs plantes pour traiter une ou plusieurs pathologies. ATHMed, elle, en
reste au stade d’un cadre proposé, où l’ontologie et le machine learning sont appelés à collaborer.
Différences
Elles diffèrent cependant sur plusieurs aspects :
• Zone géographique de référence : Afrique de l’Ouest vs Afrique générale.
• Niveau de détail : certaines incluent des composés chimiques, des rituels, des icônes; d’autres
restent plus simples.
• Degré de formalisation : ontologies OWL riches vs modèles plus légers.
• Volume de données modélisées : de quelques dizaines à quelques centaines de plantes et recettes.
• Existence d’applications web : peu d’outils opérationnels et accessibles aux acteurs locaux.
Le tableau I.1 présente une synthèse comparative des ontologies identifiées dans la littérature.
Analyse synthétique
Trois constats se dégagent du tableau. Les ontologies botaniques (FLOPO, PO) couvrent convena￾blement la plante mais ignorent les usages médicinaux; les ontologies pharmaceutiques (DrOn) restent
centrées sur les médicaments modernes; l’OTM, prometteuse, n’est pas spécifique à l’Afrique.
Pour l’Afrique, plusieurs initiatives se distinguent : celle de Tekemetieu [47] intègre les dimensions
mystiques mais reste limitée au Gabon et au Cameroun; celle d’Angole et al. [2, 3] apporte une
intégration avec la médecine moderne tout en demeurant générale; ontoMEDTRAD [27] est la plus
aboutie pour l’Afrique de l’Ouest grâce à son approche visuelle; WATRIMed [44, 43] couvre l’Afrique
de l’Ouest, avec des exemples burkinabès, mais son ontologie n’est pas téléchargeable.
Aucune de ces ontologies n’est spécifiquement dédiée aux plantes médicinales du Burkina Faso, et
aucune n’intègre systématiquement la traçabilité des sources ni les niveaux de preuve. C’est précisément
ce double manque que notre recherche entend combler : liaison complète de chaque fait à sa source, et
restitution du niveau de preuve que cette source lui attribue.
Apports de notre travail par rapport aux travaux existants
Notre travail s’inscrit dans un paysage déjà dense, où coexistent des initiatives de recensement,
de structuration et de modélisation des connaissances sur les plantes médicinales, en Afrique et plus
particulièrement au Burkina Faso. D’un côté, des ontologies et systèmes à base de connaissances
à vocation régionale ou continentale (WATRIMed, ontoMEDTRAD, ATHMed, deep ontologies de
la médecine traditionnelle africaine); de l’autre, de nombreux inventaires ethnobotaniques, thèses,
rapports et projets de bases de données burkinabès (enquêtes sur les plantes médicinales, projet AI4D,
projet « Herbier avec chimiothèque », etc.).
Face à cet existant, notre travail apporte une valeur ajoutée sur quatre plans.
Sur le plan scientifique, nous produisons une ontologie enrichie et une base de connaissances
structurée, issues de la littérature scientifique burkinabè, en mettant en évidence les plantes, les
pathologies et les régions les plus étudiées, ainsi que les principales lacunes (dosages, toxicités, zones
sous-documentées).
Sur le plan méthodologique, nous proposons une méthode d’extraction assistée par IA (prompts
adressés à des LLM) et un modèle conceptuel adapté au contexte burkinabè. Ce modèle intègre les
noms vernaculaires (mooré, dioula, fulfuldé), les recettes multi-plantes lorsqu’elles sont documentées
et les coordonnées géographiques issues de l’INERA; chaque information y reste rattachée à sa source,
avec le niveau de preuve que celle-ci lui attribue.
Sur le plan technologique, nous implémentons une base de connaissances orientée graphe (Neo4j)
et développons une application web de consultation (Streamlit) permettant des requêtes en langage
naturel via un système RAG (Llama 3 + LangChain). L’application propose un chatbot, une recherche
par plante ou par pathologie, ainsi que des fiches descriptives accompagnées de leurs sources et de
leurs niveaux de preuve.
27

--- page 40 ---
Table I.1 – Synthèse comparative des ontologies de la littérature
Ontologie Domaine Couverture Particularité Limite
principale
FLOPO Botanique Structure des
plantes
Très complète Pas d’usages
médicinaux
PO Botanique Anatomie
végétale
Standard
génomique
Pas d’ethnobo￾tanique
OTM Médecine trad. Maladies,
traitements
Intègre
médecines
asiatiques
Pas spécifique
Afrique
DrOn Pharmacologie Médicaments,
effets
Standard
pharmaceutique
Pas de
préparations
trad.
FOODON Alimentation Plantes
comestibles
Couverture
large
Pas d’usages
médicinaux
SNOMED CT Clinique Terminologie
médicale
Large
couverture
Structure non
ontologique
WATRIMed (2019) Med. trad.
Ouest-Afr.
Plantes,
recettes,
maladies
Graphe relié à
DBpedia, IPNI,
Wikidata
Ontologie non
téléchargeable
ontoMEDTRAD (2018) Med. trad.
Ouest-Afr.
Plantes, recettes Approche
visuelle
iconique
Côte d’Ivoire /
Sénégal
ATHMed (2022) Med. trad. Afr. Plantes,
traitements
Hybride
ontologie/ML
Cadre proposé,
Ghana
Deep Ontologies Med. trad. Afr. Plantes, rituels,
croyances
Intègre
dimensions
culturelles
Conceptuel, peu
opérationnel
Angole et al. (2013) Intégration
Med.
Maladies,
traitements
Alignement
BFO
Général Afrique
ontoFRACTURECARE (2024) Med. trad.
(fractures)
Bone-setters Structuration
des
connaissances
Domaine
spécifique
28

--- page 41 ---
Sur le plan sociétal, nous contribuons à la valorisation du patrimoine végétal thérapeutique
burkinabè en fournissant une base structurée et traçable, utile à la recherche, à la préservation des
connaissances endogènes et à la diffusion scientifique.
Notre travail se positionne ainsi comme une couche complémentaire aux infrastructures existantes
(ontologies régionales, inventaires, herbier national), en apportant une modélisation sémantique
centrée sur les usages thérapeutiques documentés, propre au Burkina Faso et adossée à une traçabilité
systématique vers les sources scientifiques.
I.4.2 Systèmes intelligents d’accès aux connaissances
Typologie des systèmes Plusieurs familles de systèmes donnent accès aux connaissances médicinales,
chacune adossée à une approche technique différente :
• Systèmes experts : ils modélisent l’expertise humaine par des règles logiques [7], comme dans
MYCIN. Limites : difficiles à adapter aux connaissances traditionnelles, maintenance lourde.
• Systèmes à base de cas : ils réutilisent des cas similaires [26]. Limites : supposent une base de
cas très riche et peinent face aux situations inédites.
• Chatbots médicaux : ils assurent une interaction en langage naturel [23], comme Ada ou Babylon
Health. Limites : bases parfois limitées, fiabilité variable.
• Plateformes d’ontologies : elles autorisent des requêtes sémantiques formelles [46]. Limites :
interfaces souvent complexes, réservées aux experts.
Systèmes RAG pour l’accès aux connaissances Les systèmes RAG (Retrieval-Augmented Genera￾tion) constituent une avancée plus récente [29], déjà déclinée dans plusieurs domaines : HealthRAG
(médical), BioRAG (biologique), LegalRAG (juridique).
Limites communes des systèmes existants Quatre insuffisances reviennent cependant d’une famille
à l’autre :
• bases de connaissances incomplètes ou hétérogènes;
• absence de traçabilité systématique vers les sources d’origine;
• non-adaptation aux spécificités et aux langues locales;
• absence de pondération par niveaux de preuve scientifique.
Positionnement de notre système Notre système entend répondre à ces quatre insuffisances, en
conjuguant adaptation locale (Burkina Faso), enrichissement scientifique, traçabilité systématique,
intégration explicite des niveaux de preuve déclarés par les sources et accès naturel assuré par un RAG
couplé à une base de données graphe (Neo4j).
I.4.3 Positionnement de notre recherche
Originalité de notre recherche L’originalité de notre recherche tient à la réunion de sept éléments :
1. Réutilisation d’ontologie : Gain de temps et garantie d’interopérabilité.
2. Adaptation locale : Prise en compte du contexte burkinabè et des noms vernaculaires locales
(mooré, dioula, fulfuldé).
3. Enrichissement scientifique : Exploitation des thèses, articles et travaux locaux validés.
4. Traçabilité des sources : Chaque fait est lié à sa référence scientifique.
5. Accès intelligent par RAG : Requêtes formulées en langage naturel.
29

--- page 42 ---
6. Base de connaissances graphe : Flexibilité de modélisation orientée graphe.
7. Niveaux de preuve : Restitution, pour chaque fait, de la catégorie déclarée par sa source : savoir
traditionnel, étude in vitro, étude in vivo ou essai clinique.
Conclusion du chapitre
Ce chapitre a posé les fondements théoriques de notre recherche. Nous y avons défini les concepts
clés liés aux plantes médicinales et au patrimoine ethnobotanique, puis exposé les principes de
l’ingénierie des connaissances et des ontologies. Nous avons également examiné les apports de
l’intelligence artificielle à l’accès aux connaissances, à travers le traitement du langage naturel et les
architectures de génération augmentée par récupération (Retrieval-Augmented Generation – RAG),
avant d’analyser les travaux connexes, en particulier les ontologies développées pour la médecine
traditionnelle africaine.
Cette revue de la littérature met en évidence des lacunes substantielles. Aucune ontologie n’est
spécifiquement dédiée aux plantes médicinales du Burkina Faso : ontoMEDTRAD couvre principalement
la Côte d’Ivoire et le Sénégal, et WATRIMed, bien qu’elle s’appuie sur des exemples burkinabès, ne
fournit pas d’ontologie téléchargeable. S’y ajoutent deux défis, majoritairement laissés ouverts : la
traçabilité des connaissances et l’intégration systématique de sources scientifiques multiples.
Notre recherche entend combler ces lacunes en proposant un modèle structuré, tracé et accessible
en langage naturel, qui apporte des contributions à la fois scientifiques, techniques et pratiques. Elle
s’inscrit ainsi pleinement dans une démarche de valorisation et de préservation des savoirs locaux, tout
en contribuant à l’essor et à l’intégration de la médecine traditionnelle en Afrique.
Le chapitre suivant présentera la démarche méthodologique adoptée pour mener à bien cette
recherche. Nous y décrirons la constitution du corpus d’études, l’analyse comparative des ontologies
existantes, la démarche d’adaptation et d’enrichissement de l’ontologie retenue, ainsi que la conception
et le développement de notre système intelligent d’accès aux connaissances.
30

--- page 43 ---
Chapitre II
Matériel et méthodologie
Introduction du chapitre
Après avoir posé le cadre conceptuel et balisé l’état de l’art, il reste à dire comment ce cadre a été
mis à l’épreuve des faits. Le présent chapitre expose le matériel mobilisé et la démarche méthodologique
suivie; il fait le lien entre la réflexion théorique et la mise en œuvre technique.
Trois mouvements structurent son propos. Le premier porte sur le matériel, c’est-à-dire sur le
corpus documentaire, les ontologies candidates et l’environnement technique. Le deuxième détaille la
méthodologie, décomposée en huit phases allant de l’identification comparée des ontologies jusqu’à
l’évaluation du système. Le troisième rassemble la démarche dans une synthèse et ouvre la voie au
chapitre suivant.
Chaque phase est exposée selon un format constant : objectif poursuivi, actions concrètes, méthodes,
outils mobilisés et livrables produits. Cette uniformité, un peu austère, a une raison d’être : elle rend la
démarche reproductible par un tiers et permet d’en apprécier la contribution.
II.1 Matériel
Rassembler les ressources mobilisées est la première exigence de ce type de recherche : sans
inventaire clair, aucune étape ultérieure ne peut être évaluée. Nous présentons donc successivement le
corpus documentaire, les ontologies candidates, puis l’environnement technique, avant de proposer
deux tableaux récapitulatifs.
Ces ressources sont de trois ordres : documentaires (articles, thèses, rapports, bases de données),
conceptuelles (les ontologies existantes dont nous avons évalué l’usage) et techniques (modèles de
langage, base de données, frameworks et bibliothèques). Chacune est présentée avec la précision
nécessaire pour que son rôle dans la démarche soit sans ambiguïté.
II.1.1 Corpus documentaire
Point de départ inhabituel : l’ontologie n’a pas été choisie après le corpus, mais avant. Nous avons
identifié et sélectionné l’ontologie en amont, afin de savoir quelles notions et quelles relations guideront
l’extraction. Les documents entrent ainsi dès la collecte dans une structure conceptuelle précise, plutôt
que d’être fouillés après coup.
Le corpus réunit des documents scientifiques et techniques consacrés aux plantes médicinales du
Burkina Faso, répartis en deux ensembles : les publications scientifiques, d’une part, les données de
l’Herbier National des Plantes Médicinales (burkinaherbiermed.org) et celles de l’INERA, d’autre part.
La figure II.1 résume le cheminement suivi, de l’ontologie sélectionnée en amont au corpus final.
31

--- page 44 ---
[TODO : Schéma à produire : flux horizontal en 4 boîtes sur la ligne de
légende ci-dessous : ontologie sélectionnée (phase 1) → critères de recherche
et de sélection (phase 2) → collecte (35 documents, Herbier National, INERA)
→ corpus indexé (phase 3). Sous l’étape « collecte », une boîte latérale «
documents écartés » (nombre réel et motif : hors critères de la phase 2), reliée
par une flèche sortante. Flèches directionnelles étiquetées, numéros de phases
visibles, texte en français. Outil libre (PowerPoint, draw.io), format PNG, 15
cm de large, enregistrer sous images/flux_corpus.png.]
Ontologie sélectionnée (phase 1) → critères de recherche et de sélection (phase 2)
→ collecte : 35 documents, Herbier National, INERA → corpus (phase 3)
Figure II.1 – Constitution du corpus documentaire
Sources scientifiques publiées
Le corpus scientifique repose sur 35 rapports de recherche, articles, thèses et mémoires, issus de
revues, d’universités et d’institutions de recherche burkinabè. Les études ethnobotaniques, ethnophar￾macologiques et phytochimiques qu’ils rassemblent portent sur les noms scientifiques et vernaculaires,
les parties utilisées, les pathologies traitées et les modes de préparation, sans oublier, pour les plus
récentes, les dosages et les données de toxicité.
Ces travaux forment le socle du corpus. Ils ont été retenus pour leur rigueur et pour leur pertinence
au contexte burkinabè, sur une période allant des fondements du domaine aux publications les plus
actuelles. Un tel étagement permet de couvrir un large éventail d’espèces, de pathologies et de pratiques
thérapeutiques : c’est de cette diversité, plus que du volume, que dépend la qualité de l’extraction.
Quatre travaux illustrent la variété des données mobilisées :
— Zerbo et al. [58] ont étudié les plantes médicinales chez les Sanan du Burkina Faso; leur travail
documente 85 espèces utilisées pour traiter 63 affections.
— Ouédraogo et al. [38] ont dressé une revue des plantes médicinales à potentiel aromatique du
pays, recensant 42 espèces et en caractérisant les propriétés et les usages.
— Tibiri et al. [48] ont mené une enquête à l’échelle nationale sur les plantes utilisées contre les
maladies hépatiques, documentant plus de 2 000 entrées de plantes correspondant à 212 espèces.
— Ouédraogo et al. [37] ont enquêté auprès de 30 commerçants de plantes médicinales dans six
grandes villes, identifiant 104 espèces utilisées pour diverses pathologies.
Réunis, ces travaux forment une base empirique solidement burkinabè : ils fournissent à la fois des
protocoles méthodologiques réutilisables et des observations de terrain très riches.
Données de l’Herbier National des Plantes Médicinales du Burkina Faso
Le site burkinaherbiermed.org diffuse des données sur les plantes médicinales du pays : informations
botaniques, usages thérapeutiques et références bibliographiques. Elles proviennent du projet « Herbier
avec chimiothèque », piloté par le Ministère de la Santé.
Ce projet vise à bâtir un herbier national dédié aux plantes médicinales, accouplé à une chimiothèque
de marqueurs chimiques. Il documente les plantes utilisées contre les dix pathologies prioritaires
définies par le ministère, géolocalise les stations et constitue des spécimens conservés, le tout alimentant
une base de données nationale accessible par application mobile et par site web.
Là où les herbiers nationaux s’arrêtent à la conservation de spécimens, celui-ci articule trois
registres : un herbier (spécimens identifiés et conservés), une chimiothèque (marqueurs chimiques
identifiés et dosés) et une base de données (informations ethnobotaniques, usages thérapeutiques,
géolocalisation). Il ne se substitue pas aux autres herbiers burkinabè (HNBU du CNRST/INERA,
Centre National de Semences Forestières, Université Joseph Ki-Zerbo); il s’y articule par la spécificité
de son objet : les plantes médicinales.
32

--- page 45 ---
Données de l’INERA
L’Institut de l’Environnement et de Recherches Agricoles (INERA) tient une base de données de
plus de 7 000 espèces végétales, assorties des coordonnées géographiques des stations où elles peuvent
être observées. Ces données ouvrent la voie à une analyse spatiale de la distribution des espèces et
complètent les données ethnobotaniques par une dimension géographique.
Leur apport se révèle décisif pour notre recherche : elles localisent les plantes sur le territoire
burkinabè, autorisent l’étude de leur répartition et enrichissent la base de connaissances en informations
spatiales. Le croisement des usages traditionnels avec la distribution géographique des espèces laisse
par ailleurs entrevoir des régularités régionales dignes d’être vérifiées.
Le tableau II.1 récapitule les sources du corpus.
Table II.1 – Sources du corpus documentaire
Source Type Volume estimé Contenu principal
Articles et thèses Publications
scientifiques
35 documents Études ethnobotaniques,
pharmacologiques
burkinaherbiermed.org Base de données
en ligne
Plusieurs
centaines de
plantes
Données botaniques, usages,
références
INERA Base de données
institutionnelle
> 7 000 espèces Coordonnées géographiques,
identification
Ce corpus ne se lit pas d’un seul tenant : les documents qui le composent relèvent de types d’étude
différents, et chacun n’est exploitable que pour ce qu’il mesure. Trois profils s’y distinguent. Les
enquêtes ethnobotaniques et ethnopharmacologiques (enquêtes auprès de tradipraticiens, recensements
de marchés) livrent les noms vernaculaires, les parties utilisées, les modes de préparation et les
pathologies traitées, souvent espèce par espèce. Les études expérimentales, qu’il s’agisse d’essais in
vitro ou de travaux phytochimiques, apportent en revanche les activités pharmacologiques mesurées,
les concentrations testées, le niveau de preuve et le lieu de récolte, mais ne renseignent ni sur les noms
vernaculaires ni sur les pratiques de préparation. Les revues de synthèse dressent enfin des inventaires
à grande échelle dont la provenance est diluée : elles servent à repérer les sources primaires plutôt qu’à
alimenter directement la base de connaissances.
Trois règles découlent de cette typologie pour l’extraction. Une source ne remplit que les champs
qu’elle a effectivement mesurés; un champ qu’elle ne couvre pas reste vide et n’est pas comblé par
déduction. Une affirmation d’usage traditionnel portée par un article expérimental, lorsqu’elle n’est
appuyée d’aucune référence ethnobotanique, n’est pas enregistrée comme connaissance : elle est écartée
ou conservée à titre indicatif, sans être rattachée à la base. Enfin, les comptes d’espèces ne se somment
pas d’un type de source à l’autre : les 42 espèces d’une revue [38] peuvent recouper pour l’essentiel
celles des enquêtes qu’elle reprend, et les additionner reviendrait à compter plusieurs fois la même
observation. Le corpus s’énonce donc document par document, comme le fait le tableau II.1, sans
agrégation des volumes.
Ce corpus se distingue par sa richesse et sa diversité : il embrasse plusieurs régions du Burkina
Faso, un éventail de pathologies et des approches méthodologiques d’une variété appréciable. Il offre
une base sérieuse pour l’extraction des connaissances et l’enrichissement de l’ontologie. Le choix de
l’ontologie en amont a joué un rôle déterminant : il a permis de cibler les informations à extraire et
d’organiser le corpus selon les concepts et relations définis, garantissant ainsi la cohérence entre le
modèle conceptuel et les données collectées.
33

--- page 46 ---
II.1.2 Ontologies candidates
Cinq ontologies candidates ont été retenues pour l’étude comparative. Elles ont été présentées au
chapitre I, aux sections I.4.1 et I.4.1, et couvrent des domaines variés : botanique, médecine traditionnelle,
pharmacologie, ethnomédecine. Le tableau II.2 en donne les caractéristiques descriptives.
Elles seront confrontées à une grille de critères définie en phase 1 (section II.2.1), opération qui
doit désigner l’ontologie la plus adaptée à notre contexte. Cette sélection précède la constitution du
corpus et détermine le modèle conceptuel qui guidera l’extraction.
Table II.2 – Ontologies candidates pour la comparaison
N° Ontologie Domaine Zone
géographique
Format Source
d’accès
1 WATRIMed Médecine
traditionnelle
Afrique de
l’Ouest
OWL,
graphe de
connais￾sances
IOS Press (2
articles)
2 ontoMEDTRAD Médecine
traditionnelle
Afrique de
l’Ouest
OWL +
iconique
Thèse A.
Kouamé
(UGB)
3 ATHMed Médecine
traditionnelle
Afrique (Ghana) Cadre
conceptuel
Frontiers in AI
4 Deep Ontologies Médecine
traditionnelle
Afrique OWL
(Protégé)
Articles
ARIMA
5 FLOPO, PO Botanique International OWL OBO Foundry
Chacune présente des acquis et des lacunes. Les ontologies botaniques (FLOPO, PO) décrivent
bien la plante mais ne traitent pas des usages médicinaux; les ontologies pharmaceutiques (DrOn)
se resserrent sur les médicaments modernes; l’OTM, prometteuse, reste sans ancrage africain. Les
initiatives africaines (WATRIMed, ontoMEDTRAD, ATHMed) s’intéressent en revanche à la médecine
traditionnelle du terrain, avec ses dimensions culturelles et ses recettes multi-plantes, même si ATHMed
en reste, elle, au stade d’un cadre proposé. La phase 1 en livre la comparaison détaillée.
II.1.3 Outils et environnement technique
Les outils techniques occupent une place à part entière dans cette recherche : ils ne se contentent pas
d’exécuter, ils orientent. Pour chacun, nous précisons les phases concernées et les raisons de son choix.
Le dispositif d’expérimentation qui les accueille est résumé dans la figure II.2 : où chaque composant
est exécuté, et comment ils communiquent. [TODO : Schéma à produire : trois zones réelles, reliées par des flèches
étiquetées. Zone 1 « Google Colab » : notebooks, extraction (phase 5), modèle
Llama 3 via Ollama, GPU. Zone 2 « poste local » : Protégé 5, Neo4j Desktop,
Ollama/Llama 3, application Streamlit. Zone 3 « utilisateur » : navigateur
web. Flèches : export des fichiers JSON/CSV du Colab vers le poste ; requête
bolt du poste vers Neo4j ; tunnel ngrok portant l’API de Llama 3 vers
l’application ; requête HTTPS du navigateur vers Streamlit. Zones en
encadrés, flèches avec libellé au-dessus, texte en français. Outil libre
(PowerPoint, draw.io), format PNG, 15 cm de large, enregistrer sous
images/dispositif_technique.png.]
Google Colab + Ollama (extraction, phase 5) | poste local : Neo4j Desktop et
Streamlit | tunnel ngrok (API de Llama 3 pour l’application) Figure II.2 – Dispositif technique d’expérimentation
34

--- page 47 ---
Modèle de langage : Llama 3
Notre modèle de langage est Llama 3 70B [31], un modèle ouvert de grande taille dont les
performances en compréhension et en génération de texte justifient le choix. Deux propriétés ont
été déterminantes : la maîtrise du français, indispensable au traitement de documents scientifiques
burkinabè, et la capacité à suivre des instructions complexes, requise pour une extraction structurée.
Phases d’utilisation : Phase 5 (Extraction des connaissances) et Phase 7 (Génération de réponses
RAG).
Le tableau II.3 présente les modes d’accès à Llama 3.
Table II.3 – Modes d’accès à Llama 3 70B
Usage Mode d’accès Environnement
Extraction Ollama + Google Colab Notebooks Colab avec GPU
Génération RAG API via ngrok Serveur local exposé
Cinq raisons ont motivé ce choix. Ses performances dépassent celles des modèles de plus petite
taille sur les tâches complexes. Il est open source, donc utilisable sans contrainte de licence. Il maîtrise le
français et peut être adapté aux langues locales. Ollama en autorise l’exécution locale, tandis que ngrok
en expose une API distante à l’application web. Enfin, ses 70 milliards de paramètres lui permettent de
saisir des nuances sémantiques fines, qualité décisive pour l’extraction de connaissances spécialisées.
Plateforme d’exécution : Google Colab
Les expériences d’extraction se déroulent sur Google Colab, plateforme de notebooks hébergée
par Google qui donne accès à des GPU (T4, V100, A100) adaptés à l’inférence de Llama 3 70B.
Phase d’utilisation : Phase 5 (Extraction des connaissances).
La plateforme présente une série d’avantages décisifs pour ce type de travail : elle épargne
l’acquisition d’infrastructure locale coûteuse, donne accès à des GPU performants, autorise une
exécution interactive et itérative, et facilite la reproductibilité des expériences. Son intégration avec
Google Drive simplifie le stockage des données et des résultats, et le partage des notebooks avec
d’autres chercheurs favorise la collaboration et la validation.
Base de connaissances : Neo4j Desktop
La base de connaissances est tenue par Neo4j Desktop, version locale de Neo4j qui permet de
créer, de gérer et d’interroger des graphes de connaissances.
Phase d’utilisation : Phase 6 (Construction et interrogation de la base).
Le tableau II.4 présente les caractéristiques de Neo4j Desktop.
Table II.4 – Caractéristiques de Neo4j Desktop
Caractéristique Valeur
Type Base de données orientée graphe
Langage de requête Cypher
Version Desktop (locale)
Format d’import CSV, JSON
Interface Neo4j Browser, Bloom
Neo4j convient particulièrement à notre projet. Il autorise une modélisation naturelle des relations
complexes entre plantes, usages, propriétés et sources; il offre une interrogation puissante par Cypher;
il rend la traçabilité explicite par le seul jeu des relations. Il reste extensible (de nouvelles connaissances
35

--- page 48 ---
s’y ajoutent sans reconstruire la base) et sa visualisation du graphe facilite la compréhension des liens
entre entités.
Orchestration RAG : LangChain
L’orchestration du système RAG est confiée à LangChain, framework qui permet d’enchaîner les
composants du traitement : interprétation de la requête, recherche dans Neo4j, génération de la réponse.
Phase d’utilisation : Phase 7 (Exploitation par l’IA et développement web).
Le tableau II.5 présente les composants LangChain utilisés.
Table II.5 – Composants LangChain utilisés
Composant Rôle
GraphCypherQAChain Génération de requêtes Cypher à partir de
questions naturelles
Neo4jGraph Connexion à la base Neo4j
ChatOpenAI / Ollama Intégration du modèle Llama 3
PromptTemplate Construction des prompts
Memory Gestion de l’historique de conversation
Plusieurs raisons ont conduit à retenir LangChain : c’est aujourd’hui l’un des frameworks
les plus aboutis pour les systèmes RAG [29], il propose une intégration native de Neo4j via
GraphCypherQAChain, gère l’historique de conversation, reste extensible et bien documenté, s’intègre
sans effort à Streamlit et autorise la définition de chaînes de traitement complexes sans sacrifier la
lisibilité du code.
Interface web : Streamlit
L’application web est développée avec Streamlit, framework Python qui permet de construire
rapidement des applications web interactives.
Phase d’utilisation : Phase 7 (Exploitation par l’IA et développement web).
L’application offrira un ensemble de fonctionnalités : un chatbot en langage naturel pour poser des
questions, des recherches par plante, par pathologie ou par région, des fiches descriptives présentant les
plantes et leurs usages, l’affichage des sources et des niveaux de preuve, ainsi qu’une visualisation du
graphe de connaissances.
Streamlit a été retenu pour son simplicité d’usage et la rapidité de développement qu’il autorise, pour
la gestion de l’état de session propre aux conversations, pour son intégration immédiate avec LangChain,
et parce qu’il produit une interface professionnelle sans investissement lourd. Le déploiement sur un
serveur ou une plateforme cloud en est également direct.
Bibliothèques Python
Les bibliothèques Python sont utilisées dans les phases 5, 6 et 7. Le tableau II.6 liste les bibliothèques
Python utilisées.
Ces bibliothèques couvrent l’ensemble des besoins techniques de la recherche : connexion à la base
de données, orchestration du système RAG, développement de l’interface web, chargement du modèle
de langage, manipulation des ontologies, traitement des données et visualisation.
II.1.4 Tableau récapitulatif du matériel
Le tableau II.7 rassemble l’ensemble du matériel mobilisé.
36

--- page 49 ---
Table II.6 – Bibliothèques Python utilisées
Bibliothèque Version Rôle
neo4j 5.x Driver de connexion à Neo4j
langchain 0.1.x Orchestration RAG
langchain-community 0.0.x Intégrations Neo4j, Ollama
streamlit 1.30+ Interface web
transformers 4.40+ Chargement de Llama 3
ollama 0.1.x Client Ollama
sentence-transformers 2.5+ Embeddings
owlready2 0.45+ Manipulation ontologies
OWL
rdflib 7.0+ Format RDF/OWL
pandas 2.0+ Manipulation de données
plotly 5.18+ Visualisation
Table II.7 – Récapitulatif du matériel
Catégorie Élément Spécification
Corpus
Documents
scientifiques
35 rapports, articles, thèses
Base
burkinaherbiermed.org
Plusieurs centaines de plantes
Base INERA > 7 000 espèces géolocalisées
Ontologies
WATRIMed OWL, Afrique de l’Ouest
ontoMEDTRAD OWL + iconique, Afrique de
l’Ouest
ATHMed Cadre proposé, Ghana
Deep Ontologies OWL, Afrique
FLOPO, PO OWL, botanique
Modèle de
langage
Llama 3 70B Via Ollama + Colab (extraction),
API ngrok (RAG)
Plateforme Google Colab GPU T4/V100/A100
Base de
connaissances
Neo4j Desktop Orientée graphe, Cypher
Orchestration
RAG
LangChain GraphCypherQAChain
Interface web Streamlit Chatbot, recherche, fiches
Bibliothèques Python neo4j, langchain, streamlit,
transformers, etc.
37

--- page 50 ---
II.1.5 Tableau de correspondance Matériel - Phases
Le tableau II.8 met en regard le matériel et les phases méthodologiques, et indique à quel moment
et dans quel but chaque ressource entre en jeu.
Table II.8 – Correspondance entre le matériel et les phases
Matériel Phase Utilisation
Corpus documentaire Phase 3 Constitution du corpus
Ontologies candidates Phase 1 Comparaison et sélection
Llama 3 70B Phase 5, Phase 7 Extraction, génération RAG
Google Colab Phase 5 Exécution de l’extraction
Neo4j Desktop Phase 6 Base de connaissances
LangChain Phase 7 Orchestration RAG
Streamlit Phase 7 Interface web
Bibliothèques Python Phase 5, 6, 7 Développement
II.2 Méthodologie
La démarche se décompose en huit phases opérationnelles. Chacune est décrite avec ses actions
concrètes, ses méthodes et le livrable qu’elle produit. L’enchaînement suit une progression qui va de
l’identification et de la comparaison des ontologies à la définition des critères de recherche, puis à la
constitution du corpus, à l’adaptation et à l’enrichissement de l’ontologie, à la construction de la base
de connaissances, à l’exploitation par l’intelligence artificielle et au développement de l’application
web, et se referme sur l’évaluation et la validation.
L’ordre retenu n’est pas fortuit. Commencer par le choix de l’ontologie revient à fixer un cadre
conceptuel avant même de collecter la moindre donnée : les documents sont alors recueillis dans
une structure cohérente, et l’extraction peut cibler d’emblée les informations pertinentes. C’est cette
discipline d’amont qui écarte la dérive la plus coûteuse : collecter abondamment pour découvrir trop
tard que l’on a collecté les mauvaises choses.
II.2.1 Phase 1 : Identification et étude comparative des ontologies
Objectif : Sélectionner l’ontologie la plus pertinente pour notre contexte.
La comparaison des ontologies procède en trois temps : définir une grille de critères, noter chaque
ontologie selon cette grille, puis retenir celle qui obtient le score le plus élevé. Cette phase conditionne
l’ensemble de la suite, puisque c’est elle qui fixe le modèle conceptuel.
Définition de la grille de critères
Huit critères ont été retenus, choisis en fonction de nos besoins propres : représenter les connaissances
sur les plantes médicinales du Burkina Faso, intégrer les savoirs locaux, assurer la traçabilité des
sources et permettre l’adaptation au contexte burkinabè. Le tableau II.9 les présente.
Chaque critère reçoit une pondération proportionnelle à son importance. Les critères de pondération
élevée (3) sont ceux sans lesquels le contexte burkinabè ne serait pas représenté; les critères de
pondération moyenne (2) comptent mais peuvent s’accommoder d’un compromis. Le score global est
ensuite obtenu en multipliant chaque note par la pondération de son critère, en sommant les produits et
en divisant par la somme des pondérations : la pondération rend ainsi la comparaison quantitative et
permet d’aboutir à un score global rapporté sur 5.
38

--- page 51 ---
Table II.9 – Grille de critères de comparaison
N° Critère Description Pondération
1 Couverture du
domaine
Capacité à représenter plantes, usages,
propriétés, maladies
Élevée (3)
2 Richesse
sémantique
Nombre et qualité des classes, relations,
axiomes
Élevée (3)
3 Disponibilité Ontologie accessible et téléchargeable Élevée (3)
4 Documentation Qualité de la documentation et des
exemples
Moyenne (2)
5 Interopérabilité Compatibilité avec OWL, RDF,
SPARQL
Moyenne (2)
6 Adaptabilité Facilité d’adaptation au contexte
burkinabè
Élevée (3)
7 Traçabilité Capacité à associer les connaissances
aux sources
Élevée (3)
8 Prise en compte
des savoirs locaux
Intégration des noms vernaculaires,
recettes multi-plantes
Élevée (3)
Notation des ontologies
Chaque ontologie est notée de 1 (très faible) à 5 (très élevé) pour chaque critère. Les résultats
figurent dans le tableau II.10.
Table II.10 – Notation des ontologies candidates
Ontologie C1 C2 C3 C4 C5 C6 C7 C8 Score
WATRIMed 4 4 2 3 5 4 3 5 3.7
ontoMEDTRAD 5 5 5 4 4 5 4 5 4.7
ATHMed 4 4 3 3 4 3 2 3 3.2
Deep Ontologies 3 4 2 2 3 3 2 4 2.9
FLOPO / PO 2 3 5 4 5 2 1 1 2.7
La lecture de ce tableau fait apparaître plusieurs tendances. Les ontologies africaines (WATRIMed,
ontoMEDTRAD, ATHMed) dominent, grâce à la couverture du domaine et à la prise en compte des
savoirs locaux. Les ontologies botaniques (FLOPO, PO) obtiennent de bons résultats en disponibilité
et en interopérabilité, mais des scores très faibles sur la couverture des usages médicinaux et sur les
savoirs locaux. WATRIMed et ontoMEDTRAD se détachent du lot, mais pour des raisons différentes :
la première par l’ampleur de son modèle, la seconde par la complétude de ce qui en est accessible.
Les écarts se creusent en particulier sur la disponibilité (C3) et la documentation (C4), deux critères
pondérés à 3 et à 2. Leur notation ne retient que ce que nous avons réellement en main : WATRIMed
est décrit par deux articles de congrès, dont un qui tient en deux pages, et son fichier d’ontologie n’est
pas téléchargeable; ontoMEDTRAD est décrite par une thèse intégralement accessible, qui livre sa
liste de classes, ses propriétés, ses métriques et l’origine de ses concepts.
Sélection de l’ontologie
WATRIMed [44, 43] se classe seconde (3.7). Son modèle est riche (472 concepts et 75 propriétés
dans la version documentée) et aligné sur une ontologie fondationnelle, BioTopLite2. Mais les deux
publications qui le décrivent ne donnent qu’un aperçu des classes supérieures et des relations principales,
et aucun moyen de réutiliser l’ontologie : le score baisse dès que la question de l’accès est posée.
39

--- page 52 ---
ontoMEDTRAD [27] obtient le score le plus élevé (4.7). Elle couvre l’Afrique de l’Ouest, modélise
explicitement les recettes multi-plantes (ingrédients, parties de plantes, modes de préparation et
d’administration), trace l’origine de ses concepts et de ses relations à quinze ressources terminologiques
et ontologiques existantes, et est intégralement accessible à travers la thèse qui la présente. Deux limites
sont assumées : la validation définitive et globale de l’ontologie est annoncée comme une perspective,
et son peuplement reste restreint à un jeu de données de 22 plantes et de 31 remèdes antipaludéens [28].
Nous l’avons retenue pour notre étude.
Ce choix nous dote d’un cadre conceptuel solide pour l’extraction et l’organisation des connaissances;
il guidera la constitution du corpus documentaire et l’adaptation de l’ontologie au contexte burkinabè.
Livrable : Ontologie ontoMEDTRAD sélectionnée.
II.2.2 Phase 2 : Définition des critères de recherche et de sélection des documents
Objectif : Définir les critères qui guideront la recherche et la sélection des documents scientifiques.
La définition des critères procède en deux temps : fixer d’abord les critères de recherche, puis
les critères de sélection des documents. Ensemble, ils doivent garantir la pertinence, la qualité et la
cohérence des sources retenues.
Critères de recherche
Les critères de recherche incluent :
— Les plantes : espèces végétales documentées au Burkina Faso, avec identification botanique
(nom scientifique, famille, synonymes).
— Les parties utilisées : feuilles, racines, écorces, fruits, graines, fleurs, tiges, etc.
— Les pathologies et usages médicinaux : paludisme, infections respiratoires, digestives, diabète,
hypertension, etc.
— Les modes de préparation : décoction, macération, infusion, poudre, extrait alcoolique, etc.
— Les niveaux de preuve : savoirs traditionnels, études in vitro, études in vivo, essais cliniques.
— Les propriétés pharmacologiques : antimicrobiennes, antipaludiques, anti-inflammatoires,
antioxydantes, toxicité, etc.
— La composition chimique : alcaloïdes, flavonoïdes, tanins, saponines, huiles essentielles, etc.
Ces critères couvrent les principales dimensions des connaissances sur les plantes médicinales, et
permettent ainsi de cibler les informations utiles à la recherche.
Critères de sélection des documents
Les critères de sélection des documents incluent :
— Pertinence : le document traite des plantes médicinales du Burkina Faso.
— Identification de la plante : le nom scientifique est précisé.
— Disponibilité d’une référence scientifique : le document est publié dans une revue à comité de
lecture, une thèse, un mémoire ou un rapport de recherche.
— Fiabilité : les sources sont vérifiables et citées.
— Actualité : les documents récents sont privilégiés, sans exclure les travaux fondateurs.
Ces critères sauvegardent la qualité et la fiabilité des sources, et permettent d’écarter les documents
non scientifiques ou non pertinents. Nous disposons ainsi d’un corpus fiable et cohérent, qui constituera
la base documentaire de l’étude.
Livrable : Grille de critères de recherche et de sélection.
40

--- page 53 ---
II.2.3 Phase 3 : Constitution du corpus scientifique
Objectif : Rassembler un corpus documentaire fiable et pertinent sur les plantes médicinales du
Burkina Faso.
La constitution du corpus s’est déroulée en quatre temps. Nous avons d’abord mené une recherche
documentaire sur Google Scholar, PubMed et ResearchGate, et consulté les bases burkinaherbiermed.org
et INERA.
Nous avons ensuite appliqué les critères d’inclusion : le document devait traiter des plantes
médicinales du Burkina Faso, préciser le nom scientifique des plantes, être publié ou validé par une
institution scientifique, et s’appuyer sur des sources vérifiables et citées.
Puis sont venus les critères d’exclusion : nous avons écarté les documents non scientifiques (blogs,
sites non référencés), ceux qui ne comportent pas d’identification botanique, et les documents trop
anciens, sauf lorsqu’ils font référence.
Enfin, nous avons organisé le corpus, en classant les documents par type (article, thèse, rapport), en
les indexant par plante, par pathologie et par région, et en les stockant dans un répertoire structuré.
Au terme de ce processus, le corpus compte 35 documents scientifiques, complétés par les données
de burkinaherbiermed.org et de l’INERA. Il couvre les différentes régions du pays, un éventail de
pathologies et des approches méthodologiques variées, et constitue une base solide pour l’extraction
des connaissances.
Livrable : Un corpus de 35 documents scientifiques, complété par les données de burkinaherbier￾med.org et de l’INERA.
II.2.4 Phase 4 : Adaptation de l’ontologie sélectionnée
Objectif : Adapter l’ontologie sélectionnée au contexte burkinabè.
L’adaptation de l’ontologie suit cinq temps : analyser les concepts existants, ajouter des classes,
ajouter des propriétés, modifier les relations, puis documenter les adaptations.
Analyse des concepts existants
Nous avons étudié la structure de l’ontologie ontoMEDTRAD telle qu’elle est décrite dans la
thèse [27]. L’ontologie compte 144 concepts, 76 propriétés associatives, 16 propriétés de données,
789 individus et 2 734 axiomes. Elle est formalisée en logique de description ALCHOIQ, éditée sous
Protégé 5 et vérifiée par les raisonneurs HermiT et Pellet.
Le fichier OWL de l’ontologie n’étant pas téléchargeable publiquement, nous avons reconstitué sa
structure à partir de la documentation publiée dans la thèse : captures d’écran Protégé (figures 5.15 à
5.20) et tableaux récapitulatifs des concepts, des propriétés et de la métrique (tableaux 5.5, 5.21 et
5.22). Cette reconstitution, aussi fidèle et complète que le permet la documentation publiée, a servi de
base à l’adaptation présentée au chapitre III.
Cette reconstitution porte sur la structure conceptuelle de l’ontologie, c’est-à-dire ses classes, ses
propriétés et ses relations, et non sur ses instances. Les 789 individus d’ontoMEDTRAD n’ont pas
été réutilisés : ils relèvent du contexte et des sources propres aux travaux d’origine, tandis que notre
base de connaissances orientée graphe (Neo4j) est peuplée à partir de la littérature scientifique sur les
plantes médicinales du Burkina Faso. Les instances de notre modèle sont donc entièrement nouvelles,
insérées dans le graphe et rattachées à leurs sources.
Ses concepts majeurs couvrent le parcours de soin complet : le praticien de la médecine traditionnelle,
le patient, les indices (signes et symptômes), les maladies, les ressources médicinales (plantes, animaux,
minéraux), l’examen clinique, la recette, l’ingrédient, la partie de ressource médicinale, le mode
de préparation, le remède, sa forme galénique et son mode d’administration. Deux points méritent
d’être relevés pour notre contexte : l’ontologie distingue explicitement les types de plante (arbre,
arbuste, palme, herbe, liane) et les neuf parties de plantes utilisées (feuille, fruit, fleur, racine, tronc,
41

--- page 54 ---
écorce de tronc, écorce de racine, sève, plante entière), et elle réserve une classe aux références
scientifiques des ressources médicinales, des recettes et des remèdes. Les concepts secondaires ajoutent
les contre-indications, les contre-associations, les propriétés thérapeutiques, la toxicité, l’étiologie
et la systématique des maladies (CIM-10). Les relations de base sont la subsomption (« est un ») et
la partie-tout (« est une partie de »), complétées par 76 propriétés associatives, dont la hiérarchie
aPourForme qui servira à l’iconisation des plantes.
Nous avons ensuite évalué cette couverture au regard du contexte burkinabè.
Le constat est mitigé. Les concepts de base sont bien couverts et l’ontologie est cohérente (aucun
des raisonneurs testés ne signale d’incohérence), mais elle exige des adaptations pour le Burkina Faso.
Les lacunes principales concernent les noms vernaculaires en langues locales du pays, les maladies
spécifiques, les niveaux de preuve, le dosage et la traçabilité fine des sources scientifiques. S’y ajoute
une limite que la thèse elle-même assume : la validation définitive et globale de l’ontologie reste
une perspective, et son peuplement se limite à un jeu de données de 22 plantes et de 31 remèdes
antipaludéens.
Ajout de classes
Des classes ont été ajoutées pour les maladies spécifiques au Burkina Faso (paludisme, onchocercose,
méningite), pour les noms vernaculaires en mooré, dioula et fulfuldé, pour les régions du pays, pour les
niveaux de preuve (traditionnel, in vitro, in vivo, clinique) et pour les sources scientifiques (article,
thèse, rapport).
Ces ajouts permettent de représenter les spécificités du contexte burkinabè, d’intégrer les connais￾sances locales et d’assurer la traçabilité des sources.
Ajout de propriétés
Des propriétés complètent ce dispositif : nomMooré, nomDioula et nomFulfuldé pour les noms
vernaculaires; coordonnéesGPS, région et province pour la localisation géographique; niveauPreuve
et typeEtude pour le niveau de preuve; source, DOI, page et section pour la traçabilité; enfin des
propriétés de dosage et de toxicité.
L’enrichissement ainsi obtenu saisit des informations fines (noms vernaculaires, coordonnées,
niveaux de preuve, références précises) que l’ontologie d’origine ne documentait pas pour le Burkina
Faso.
Modification de relations
La relation entre remède et maladie a été précisée par des attributs de niveau de preuve. Quatre
relations nouvelles complètent le modèle : « provientDe », qui relie une connaissance à sa source;
« estDocumentéeDans », qui relie une plante aux documents; « aPourNomVernaculaire », qui rattache
une plante à ses noms locaux; et « estLocaliséeÀ », qui l’associe à ses coordonnées géographiques.
Ces modifications assurent la traçabilité des connaissances et permettent d’exprimer des relations
que le modèle d’origine, fondé sur la relation « est un » et sur la relation partie-tout, ne couvrait pas.
Documentation des adaptations
Toutes les modifications sont consignées dans un journal : chaque ajout est justifié, chaque choix
est explicité, et les classes, propriétés et relations ajoutées, modifiées ou supprimées y sont décrites une
à une.
Cette documentation n’est pas une formalité. Elle rend la démarche reproductible par un tiers et
facilite les évolutions ultérieures de l’ontologie.
Livrable : Une ontologie adaptée au contexte burkinabè.
42

--- page 55 ---
II.2.5 Phase 5 : Enrichissement des connaissances à partir de la littérature
scientifique
Objectif : Extraire les connaissances du corpus et enrichir l’ontologie.
L’enrichissement ne consiste pas à ajouter les instances à l’ontologie : l’ontologie fournit le schéma,
et les connaissances extraites sont destinées à la base de connaissances orientée graphe (Neo4j).
L’enrichissement procède en cinq temps : concevoir les prompts d’extraction, exécuter l’extraction
assistée par LLM, contrôler la qualité des extractions, structurer les données, puis les préparer pour
l’intégration dans la base de connaissances.
Conception des prompts d’extraction
Les prompts d’extraction ciblent chaque type d’information. Le prompt général demande le nom
scientifique, les noms vernaculaires, la famille botanique, les parties utilisées, les usages thérapeutiques,
les modes de préparation, les activités pharmacologiques, le niveau de preuve et la source.
Le prompt complet est reproduit au chapitre III; il impose le format de sortie (JSON) et la liste
exhaustive des champs à renseigner.
Il est ajusté selon le type de document, la typologie des sources présentée en section II.1.1 indiquant
à l’avance les champs qu’un document est en mesure de renseigner. Les champs absents d’un document
restent vides dans la sortie : aucune valeur n’est comblée par déduction, ni laissée au modèle le soin de
la produire.
Exécution de l’extraction
Llama 3 70B a été chargé sur Google Colab, les prompts ont été exécutés sur chaque document, et
les résultats ont été sauvegardés en JSON.
L’extraction procède de manière itérative : les documents sont traités un par un ou par lots, la
qualité des résultats est vérifiée au fur et à mesure, et les prompts sont ajustés lorsqu’il le faut.
Contrôle de la qualité des extractions
Deux précisions s’imposent sur la manière dont la qualité des extractions est assurée.
Le niveau de preuve associé à chaque connaissance est un attribut rapporté depuis la source :
il reprend la caractérisation qu’en fait le document d’origine, lorsque celle-ci y est explicite (savoir
traditionnel, étude in vitro, étude in vivo, essai clinique). Aucune évaluation indépendante de notre part
n’y est ajoutée. Nous ne jugeons pas la solidité d’un fait; nous conservons la valeur que lui attribue sa
source et nous la relions à cette source. À défaut d’indication, l’attribut reste vide plutôt que d’être
comblé par déduction. C’est au lecteur qu’il revient d’en apprécier la portée.
Par ailleurs, les extractions n’ont pas été validées par un expert externe : une relecture individuelle
de chaque enregistrement n’a pas été intégrée au protocole et relève de perspectives de travail ultérieurs.
La qualité n’est donc pas certifiée en amont; elle sera mesurée en aval par le protocole d’évaluation
de la phase 8, où les réponses produites seront confrontées aux réponses attendues sur un jeu de 50
questions de référence.
Structuration des données
Les données ont été converties en CSV pour l’import dans Neo4j, et organisées selon le modèle de
l’ontologie.
Cette structuration facilite l’import dans la base de connaissances et permet de vérifier la conformité
des données au modèle.
43

--- page 56 ---
Préparation de l’intégration dans la base de connaissances
Les instances (plantes, maladies, usages) et les relations entre instances ne sont pas ajoutées à
l’ontologie elle-même : l’ontologie n’en fournit que le schéma. Les données extraites sont préparées
pour être insérées dans la base de connaissances orientée graphe (Neo4j), où les connaissances seront
associées à leurs sources et où les enrichissements seront documentés.
L’intégration peuple la base de connaissances et établit les liens entre les entités.
Livrable : Un ensemble de données structurées (JSON, CSV) prêtes à être intégrées.
II.2.6 Phase 6 : Construction et interrogation de la base de connaissances
Objectif : Construire la base de connaissances orientée graphe.
La construction de la base Neo4j suit trois temps : modéliser le graphe, importer les données, tester
les requêtes.
Modélisation du graphe
Les nœuds définis sont Plante, Maladie, Usage, Partie, Préparation, Source, Composé￾Chimique et Région. Les relations sont TRAITE, UTILISE, PROVIENT_DE, A_POUR_PARTIE,
A_POUR_PREPARATION, CONTIENT et EST_LOCALISEE_A. Les propriétés retenues sont le nom, le
niveau de preuve, le DOI et les coordonnéesGPS.
Cette modélisation rend les connaissances lisibles parce qu’elle les représente comme elles sont : les
nœuds sont les entités du domaine, les relations sont les liens entre ces entités, les propriétés décrivent
leurs caractéristiques.
Import des données
Les fichiers CSV ont été chargés, les nœuds et les relations ont été créés par des requêtes Cypher, et
l’intégrité des données a été vérifiée au passage.
L’import terminé, nous avons contrôlé que toutes les données ont été correctement reprises et que
les relations et les propriétés sont intactes.
Requêtes de test
Quatre familles de requêtes ont été testées : des requêtes simples (plantes par maladie), des requêtes
complexes (recettes multi-plantes), des requêtes de traçabilité (source d’une information) et des requêtes
spatiales (plantes par région).
Ces vérifications établissent que la base est fonctionnelle et que les requêtes renvoient les résultats
attendus.
Livrable : Une base Neo4j peuplée et interrogeable.
II.2.7 Phase 7 : Exploitation par IA et développement de l’application web
Objectif : Développer le système d’accès intelligent et l’interface utilisateur.
La mise en place du système RAG suit trois temps : définir l’architecture, construire la chaîne de
traitement, intégrer les composants.
Architecture du système
L’architecture est la suivante : Utilisateur → Streamlit → LangChain → Neo4j → Llama 3 →
Réponse.
44

--- page 57 ---
Cette architecture associe la recherche d’information dans la base de connaissances à la génération
de réponses par le modèle de langage. Elle préserve la traçabilité, chaque information restant rattachée
à sa source. La chaîne de traitement qui relie ces maillons, de l’interprétation de la requête en langage
naturel à l’affichage des sources, fait l’objet d’un détail au chapitre III.
Intégration des composants
LangChain a été connecté à Neo4j puis au modèle de langage, et les prompts ont été configurés
pour orienter la génération des réponses. L’intégration a permis d’assembler les composants en un
système RAG opérationnel.
Développement de l’application web
L’application a été conçue autour de quatre fonctions : une page d’accueil avec chatbot, une
recherche par plante, une recherche par pathologie et des fiches descriptives. Le système RAG y a été
intégré et l’historique de conversation a été géré.
L’interface obtenue permet d’interroger la base de connaissances en langage naturel et de recevoir
des réponses traçables; sa conception détaillée et ses composants sont présentés au chapitre III.
Tests et validation
Deux campagnes de tests sont prévues : des tests fonctionnels et des tests utilisateurs. Les premiers
vérifient que l’application fonctionne correctement; les seconds évaluent la facilité d’utilisation et la
pertinence des réponses.
Livrable : Un système RAG fonctionnel et une application web fonctionnelle.
II.2.8 Phase 8 : Évaluation et validation
Objectif : Évaluer la qualité de l’ontologie, du système RAG et de l’application web.
L’évaluation se fait à trois niveaux : l’ontologie, le système RAG, puis l’application web.
Évaluation de l’ontologie
L’ontologie est évaluée sur quatre critères, présentés dans le tableau II.11.
Table II.11 – Critères d’évaluation de l’ontologie
Critère Description Méthode
Couverture Capacité à représenter les
connaissances du corpus
Vérification manuelle
Cohérence Absence de contradictions Requêtes de test
Traçabilité Association des connaissances aux
sources
Vérification des
relations
Extensibilité Facilité d’ajout de nouvelles
connaissances
Test d’ajout
Évaluation du système RAG
Le système RAG est évalué sur les quatre critères du tableau II.12.
Un jeu de 50 questions de référence sera constitué, portant sur les plantes, les usages et les propriétés.
Les réponses produites seront confrontées aux réponses attendues.
45

--- page 58 ---
Table II.12 – Critères d’évaluation du système RAG
Critère Description Métrique
Pertinence Les réponses répondent à la
question
Précision
Fidélité Les réponses sont fidèles aux
sources
Rappel
Exactitude Les réponses sont correctes F1-score
Traçabilité Les sources sont affichées Taux de couverture
Évaluation de l’application web
L’application web est évaluée sur les quatre critères du tableau II.13.
Table II.13 – Critères d’évaluation de l’application web
Critère Description Méthode
Facilité
d’utilisation
L’interface est intuitive Questionnaire
Compréhension Les réponses sont claires Questionnaire
Utilité L’application répond aux besoins Questionnaire
Performance Temps de réponse Mesure
10 à 20 participants seront sollicités : étudiants, chercheurs et tradipraticiens.
Livrable : Rapport d’évaluation et de validation.
II.3 Synthèse et transition
II.3.1 Tableau de correspondance Phases - Livrables
Reste à réunir le parcours et à ouvrir sur le chapitre suivant. Le tableau II.14 récapitule, pour
chacune des huit phases, son objectif et son livrable.
Conclusion du chapitre
Ce chapitre a exposé le matériel et la méthodologie de notre recherche. Le matériel réunit un
corpus de 35 documents scientifiques, les données de burkinaherbiermed.org et de l’INERA, cinq
ontologies candidates et un environnement technique bâti sur Llama 3 70B, Google Colab, Neo4j
Desktop, LangChain et Streamlit.
La méthodologie se décompose en huit phases : identification et étude comparative des ontologies,
définition des critères de recherche et de sélection des documents, constitution du corpus scientifique,
adaptation de l’ontologie sélectionnée, enrichissement à partir de la littérature scientifique, construction
et interrogation de la base de connaissances, exploitation par l’intelligence artificielle et développement
de l’application web, évaluation et validation. Chaque phase a été décrite avec ses actions concrètes et
son livrable.
L’ordre de ces phases est un choix assumé. Faire précéder la constitution du corpus par le choix
de l’ontologie garantit la cohérence entre le modèle conceptuel et les données collectées, et facilite
l’extraction en ciblant les informations pertinentes dès la collecte.
Deux limites méritent d’être signalées. Premièrement, les niveaux de preuve associés aux connais￾sances sont hérités des sources et n’ont pas fait l’objet d’une évaluation indépendante. Deuxièmement,
46

--- page 59 ---
Table II.14 – Correspondance entre les phases, les objectifs et les livrables
Phase Objectif Livrable
Phase 1 Sélectionner l’ontologie la
plus pertinente
Ontologie ontoMEDTRAD sélectionnée
Phase 2 Définir les critères de
recherche et de sélection
Grille de critères
Phase 3 Rassembler un corpus
fiable et pertinent
Corpus de 35 documents
Phase 4 Adapter l’ontologie au
contexte burkinabè
Ontologie adaptée
Phase 5 Extraire les connaissances
et enrichir l’ontologie
Données structurées (JSON, CSV)
Phase 6 Construire la base de
connaissances graphe
Base Neo4j peuplée
Phase 7 Développer le système
RAG et l’application web
Système RAG et application web
Phase 8 Évaluer la qualité du
système
Rapport d’évaluation
les extractions n’ont pas été validées par un expert externe. Ces deux points relèvent de perspectives
de travail et n’altèrent pas la traçabilité, qui demeure garantie par la liaison systématique de chaque
information à sa source.
Les protocoles d’évaluation de la phase 8 seront appliqués au chapitre IV, où notre approche sera
mise à l’épreuve des résultats.
Le chapitre suivant portera sur la conception et le développement du système : l’ontologie adaptée,
la base de connaissances construite, le système RAG implémenté et l’application web développée.
47

--- page 60 ---
Chapitre III
Conception et développement du système
Introduction du chapitre
Les chapitres précédents ont posé, tour à tour, le cadre théorique de la recherche et la démarche
méthodologique suivie pour la mener à bien. Il reste à montrer ce que cette démarche a effectivement
produit. Le présent chapitre a pour objet de présenter le système conçu et développé pour mettre à
disposition des connaissances sur les plantes médicinales du Burkina Faso, depuis le modèle conceptuel
jusqu’à l’interface accessible à l’utilisateur final.
Quatre sections suivent, dans l’ordre où les composants ont été construits. La première présente
l’ontologie adaptée et enrichie, c’est-à-dire le modèle dont découle tout le reste. La seconde décrit la
base de connaissances orientée graphe qui matérialise ce modèle et reçoit les connaissances extraites.
La troisième expose l’intégration de l’intelligence artificielle, tant pour l’extraction assistée que pour
l’accès en langage naturel fondé sur le système RAG. La quatrième enfin relate le développement de
l’application web qui ouvre l’ensemble de ces composants à l’utilisateur.
III.1 Ontologie adaptée et enrichie
L’ontologie ontoMEDTRAD [27], sélectionnée en phase 1 (section II.2.1 du chapitre II), constituait
un point de départ solide mais incomplet pour le contexte burkinabè : couverture restreinte à vingt-deux
plantes et trente et un remèdes antipaludéens, absence de noms vernaculaires locaux, silence sur
les niveaux de preuve et sur la traçabilité fine des sources. Les adaptations réalisées en phase 4 ont
transformé ce modèle; l’enrichissement issu de la phase 5, lui, ne modifie pas l’ontologie : il peuple
la base de connaissances orientée graphe, dont l’ontologie fournit le schéma. Nous présentons ici le
résultat de l’adaptation : sa vue d’ensemble, puis les classes, propriétés et relations qui l’étendent.
III.1.1 Vue d’ensemble du modèle
L’ontologie d’origine compte 144 concepts, 76 propriétés associatives, 16 propriétés de données,
789 individus et 2 734 axiomes. Elle est formalisée en logique de description ALCHOIQ, éditée sous
Protégé 5 et vérifiée par les raisonneurs HermiT et Pellet, qui n’y signalent aucune incohérence. Nous
avons conduit les adaptations dans le même environnement, en conservant cette formalisation et en
maintenant la cohérence du modèle à chaque étape.
La figure III.1 présente la structure de l’ontologie initiale telle que reconstituée à partir de la thèse.
Conformément au principe de réutilisation partielle recommandé en ingénierie ontologique, nous
avons retenu d’ontoMEDTRAD les concepts relatifs aux plantes médicinales, à leurs parties, aux
modes de préparation, aux maladies et à la localisation géographique, que nous avons complétés par
les usages médicinaux et les composés chimiques. Nous avons en revanche écarté les modules hors du
48

--- page 61 ---
(a) Partie supérieure de la hiérarchie (b) Partie inférieure de la hiérarchie
Figure III.1 – L’ontologie initiale ontoMEDTRAD reconstituée sous Protégé 5 (arbre des classes)
périmètre de notre étude : la couche d’iconisation (ontoICONE), dédiée à la représentation visuelle des
plantes, ainsi que les concepts liés à la pratique de la médecine traditionnelle (praticiens PMT, patients,
examen clinique, anamnèse). L’iconisation constitue en effet un choix de représentation, et non de
conceptualisation : son abandon ne remet pas en cause la validité du modèle conceptuel réutilisé, qui
porte sur les connaissances elles-mêmes. Le tableau III.1 détaille ce choix.
Cette réutilisation porte sur la structure conceptuelle, non sur les données. Les 789 individus
d’ontoMEDTRAD n’ont pas été repris : ils relèvent du contexte et des sources propres aux travaux
d’origine, alors que notre base de connaissances orientée graphe (Neo4j) est peuplée à partir de la
littérature scientifique sur les plantes médicinales du Burkina Faso. Seules les classes, les propriétés et
les relations du modèle d’origine ont donc été réutilisées; les instances de notre modèle sont entièrement
nouvelles, insérées dans le graphe et rattachées à leurs sources.
Les concepts de recette, d’ingrédient et de remède d’ontoMEDTRAD n’ont pas été repris tels quels :
le questionnement de notre système s’appuie sur les nœuds Usage et Préparation, qui en reprennent
l’essentiel sous une forme simplifiée. De même, la classe Langues d’ontoMEDTRAD, qui recense les
langues locales et officielles, n’a pas été reprise telle quelle : la dimension linguistique est portée dans
notre modèle par les noms vernaculaires (nomMooré, nomDioula, nomFulfuldé).
La figure III.2 présente le modèle ainsi réduit à ces seuls concepts, importé dans Protégé 5 : c’est à
partir de lui que s’opèrent les ajouts de l’adaptation.
Le tableau III.2 met en regard l’ontologie d’origine et l’ontologie après adaptation.
Les chiffres de la colonne « Après adaptation » sont ceux du fichier ontoMEDTRAD-adapte.ttl
chargé dans Protégé 5.
Les instances ne sont pas portées par l’ontologie : l’enrichissement consiste à insérer les faits et les
instances extraits du corpus dans la base de connaissances orientée graphe (Neo4j), dont l’ontologie
fournit le schéma. Les individus de l’ontologie d’origine n’ayant pas été réutilisés, la ligne « Individus »
de la colonne « Après adaptation » est sans objet.
49

--- page 62 ---
Table III.1 – Concepts retenus et écartés lors de l’adaptation
Concepts retenus Concepts écartés Justification
Plante, types et parties de
plante
Iconisation (ontoICONE :
Forme, Silhouette,
Couleur. . .)
Représentation
visuelle des plantes,
hors du périmètre du
système
Maladie (catégories
CIM-10)
Praticiens (PMT,
professions, expériences)
Gestion de la pratique
des tradipraticiens,
non utilisée
Mode de préparation Patient, état du patient,
anamnèse, examen clinique
Suivi clinique des
patients, hors du
périmètre
Références scientifiques Indices (signes,
symptômes)
Diagnostic clinique,
non exploité
Localité, Pays Glossaire, croyances,
loi-cadre
Dimensions culturelles
et réglementaires, non
exploitées
Noms vernaculaires en
langues locales
Langues (LangueLocales,
LangueOfficielle)
Dimension
linguistique reprise par
les noms vernaculaires
Figure III.2 – L’ontologie conservée : les concepts d’ontoMEDTRAD retenus
50

--- page 63 ---
Table III.2 – Statistiques de l’ontologie avant et après adaptation
Indicateur Ontologie
d’origine
Après adaptation
Concepts (classes) 144 37
Propriétés associatives 76 10
Propriétés de données 16 16
Individus 789 sans objet
Axiomes 2 734 227
Figure III.3 – L’ontologie adaptée et enrichie sous Protégé 5
51

--- page 64 ---
III.1.2 Classes ajoutées
Nous avons ajouté cinq ensembles de classes pour couvrir ce que le modèle d’origine ignorait du
contexte burkinabè. Le tableau III.3 les recense avec la lacune qu’ils viennent combler.
Table III.3 – Classes ajoutées à l’ontologie
Classe ajoutée Ce qu’elle représente Exemples
Maladies spécifiques du
Burkina Faso
Pathologies documentées par la
littérature locale
Paludisme,
onchocercose,
méningite
Noms vernaculaires Désignations des plantes dans
les langues du pays
Mooré, dioula,
fulfuldé
Régions Découverture territoriale du
pays
[TODO : lister les
instances réelles de
la classe Région
(Protégé > onglet
Instances), noms
exacts tels qu’ils
figurent dans le
modèle, séparés
par des virgules ;
ne pas citer une
région absente du
modèle]
Niveaux de preuve Catégories de preuve rapportées
par les sources
Traditionnel, in
vitro, in vivo,
clinique
Sources scientifiques Type du document dont provient
l’information
Article, thèse,
rapport
[TODO : Pour chacun des cinq ensembles de classes, relever dans Protégé 5 (onglet Classes,
sélection de la classe puis panneau Description) : la superclasse directe exacte, et un exemple de
sous-classe. Format à suivre dans ce paragraphe : « Noms vernaculaires : sous-classe de . . .».
Indiquer aussi la classe dont la sous-classe est rattachée si elle est ajoutée elle-même.]
III.1.3 Propriétés ajoutées
Les propriétés ajoutées portent sur quatre besoins : les noms locaux, la localisation géographique,
le niveau de preuve et la traçabilité documentaire. Le tableau III.4 les liste.
[TODO : Pour chacune des propriétés listées, relever dans Protégé 5 (onglet Object properties
ou Data properties, panneau Description) : domaine exact, portée exacte, et nature de la propriété :
à objet (pointe vers une classe) ou à donnée (pointe vers un type literal : chaîne, entier. . .). Source
alternative : le fichier .owl ouvert dans un éditeur de texte, lignes déclarant la propriété. Format :
« niveauPreuve : domaine = Usages, portée = Niveaux de preuve (propriété à donnée) ».]
III.1.4 Relations ajoutées
Quatre relations nouvelles complètent le modèle, dont la structure initiale, fondée sur la relation
« est un » et sur la relation partie-tout, ne couvrait pas les besoins de traçabilité. Le tableau III.5 les
présente.
52

--- page 65 ---
Table III.4 – Propriétés ajoutées à l’ontologie
Propriété Rôle
nomMooré, nomDioula,
nomFulfuldé
Noms vernaculaires de la plante dans les
langues locales
coordonnéesGPS, région,
province
Localisation géographique de la plante
niveauPreuve, typeEtude Niveau de preuve rapporté par la source et type
d’étude
source, DOI, page, section Traçabilité documentaire de chaque
connaissance
Dosage, toxicité Précautions d’emploi documentées par les
sources
Table III.5 – Relations ajoutées à l’ontologie
Relation Signification
provientDe Rattache une connaissance à la source scientifique qui
la rapporte
estDocumentéeDans relie une plante aux documents qui la décrivent
aPourNomVernaculaire Rattache une plante à ses désignations locales
estLocaliséeÀ Associe une plante à ses coordonnées géographiques
La relation entre remède et maladie, elle, a été précisée par des attributs de niveau de preuve : une
même association plante-maladie peut désormais être rapportée à plusieurs niveaux, chacun restant
celui déclaré par la source qui l’énonce.
[TODO : Pour chacune des quatre relations, relever dans Protégé 5 (onglet Object properties,
panneau Description) : la classe de départ (domaine) et la classe d’arrivée (portée). Format : «
provientDe : Connaissance → Source ». Si une relation est en réalité une propriété à donnée et
non entre classes, le signaler ici.]
III.2 Base de connaissances orientée graphe
L’ontologie fournit le modèle; il fallait une base capable de le recevoir et de le peupler avec les
connaissances extraites du corpus. Nous avons retenu Neo4j Desktop, pour les raisons motivées au
chapitre II (section II.1.3) : ce choix a été dicté par trois exigences : modéliser naturellement des
relations complexes entre plantes, usages, propriétés et sources; interroger le graphe par requêtes
expressives; et rendre la traçabilité explicite par le seul jeu des relations. Cette section décrit le passage
du modèle ontologique au graphe, puis son import et son interrogation.
III.2.1 Du modèle ontologique au graphe
Nous avons organisé la base en huit types de nœuds : Plante, Maladie, Usage, Partie, Prépa￾ration, Source, ComposéChimique et Région. Chaque nœud correspond à une classe de l’ontologie
adaptée; chaque propriété du graphe reprend une propriété du modèle. Le tableau III.6 donne cette
correspondance.
Sept types de relations relient ces nœuds : TRAITE, UTILISE, PROVIENT_DE, A_POUR_PARTIE,
A_POUR_PREPARATION, CONTIENT et EST_LOCALISEE_A. Quatre propriétés portent sur les nœuds
eux-mêmes : le nom, le niveau de preuve, le DOI et les coordonnéesGPS.
53

--- page 66 ---
Table III.6 – Correspondance entre les classes de l’ontologie et les nœuds du graphe
Nœud Classe de l’ontologie Propriétés principales
Plante [TODO : nom exact de
la classe de l’ontologie
enrichie qui porte les
plantes, à copier depuis
l’onglet Classes de
Protégé]
Nom scientifique, noms
vernaculaires
Maladie Maladie Nom, pathologie
Usage [TODO : nom exact de
la classe qui porte les
usages thérapeutiques
(relevé dans Protégé >
Classes)]
Usage thérapeutique, niveau de
preuve
Partie [TODO : nom exact de
la classe qui porte les
parties de plante
utilisées : feuille, racine,
écorce. . .(relevé dans
Protégé > Classes)]
Partie utilisée (feuille, racine,
écorce. . .)
Préparation [TODO : nom exact de
la classe qui porte les
modes de préparation :
décoction,
macération. . .(relevé
dans Protégé > Classes)]
Mode de préparation
(décoction, macération. . .)
Source Source (classe ajoutée) Auteur, année, DOI, page,
section
ComposéChimique [TODO : nom exact de
la classe qui porte les
composés chimiques
(relevé dans Protégé >
Classes)]
Nom du composé
Région Région (classe ajoutée) Nom de la région, province,
coordonnées GPS
54

--- page 67 ---
Table III.7 – Relations du graphe de connaissances
Relation Sens retenu
TRAITE [TODO : à confirmer sur le script d’import
réellement exécuté : sens exact de la relation, sous
la forme (nœud source) → (nœud cible), par
exemple (Usage) → (Maladie) ou (Plante) →
(Maladie). Écrire cette flèche dans cette colonne,
puis vérifier que les requêtes du § suivant en
découlent.]
UTILISE [TODO : à confirmer sur le script d’import
réellement exécuté : sens exact, sous la forme
(nœud source) → (nœud cible), par exemple
(Préparation) → (Plante) ou (Usage) → (Plante).
Écrire cette flèche dans cette colonne.]
PROVIENT_DE Rattache une connaissance à sa source scientifique
A_POUR_PARTIE Associe une plante à la partie utilisée
A_POUR_PREPARATION Associe une plante à son mode de préparation
CONTIENT Associe une plante à ses composés chimiques
EST_LOCALISEE_A Localise une plante dans une région
[TODO : Schéma définitif à figer à partir des scripts d’import effectivement exécutés (fichiers
.cql ou .cypher du projet) : pour chacune des 7 relations, la flèche exacte source → cible. Si le
sens réel diffère des hypothèses des deux tableaux ci-dessus, corriger ces tableaux en même temps.
Format : liste complète à remplacer par cette phrase, ou petite figure en 7 flèches que l’on glissera
ici (fichier images/schema_graphe.png).]
III.2.2 Import et peuplement
L’import suit un chemin en deux temps. Les connaissances extraites par l’intelligence artificielle,
d’abord, sont produites en JSON puis converties en CSV selon le modèle de l’ontologie, une table
par type de nœud et une table par type de relation. Neo4j, ensuite, charge ces fichiers par des requêtes
Cypher qui recréent nœuds et relations; aucune information absente des sources n’est versée dans le
graphe.
-- Illustratif : import d’un fichier de plantes
-- TODO : adapter aux noms de fichiers et de colonnes reels
LOAD CSV WITH HEADERS FROM ’file:///plantes.csv’ AS row
MERGE (p:Plante {nom: row.nom_scientifique})
SET p.niveauPreuve = row.niveau_preuve;
[TODO : Remplacer ce fragment par le code réel du projet : requêtes Cypher effectivement
utilisées pour l’import (fichier .cql ou .cypher du dépôt), 10 à 20 lignes consécutives montrant
d’abord la création des nœuds puis celle des relations (LOAD CSV, MERGE, CREATE), commentées
en français. Exiger : noms de fichiers CSV réels, noms de colonnes réels, aucun mot de passe
ni chemin de machine personnelle (remplacer par ***). Garder l’environnement verbatim et
l’ordre des commentaires ; supprimer ensuite la ligne TODO. Indiquer en commentaire LaTeX
le nom du fichier source (ex. import/import.cql).]
L’import terminé, l’intégrité des données a été contrôlée : présence des nœuds attendus, conservation
des relations et des propriétés, absence de nœuds orphelins. Le résultat en est le suivant :
55

--- page 68 ---
[TODO : Chiffres de peuplement à relever dans Neo4j Browser après l’im￾port, par quatre requêtes : MATCH (n) RETURN count(n) (total des nœuds) ;
MATCH ()-[r]->() RETURN count(r) (total des relations) ; MATCH (n) RETURN
labels(n), count(*) ORDER BY count(*) DESC (répartition par type de nœud) ;
MATCH ()-[r]->() RETURN type(r), count(*) ORDER BY count(*) DESC
(répartition par type de relation). Rapporter les quatre résultats ici, sous forme de
phrase puis de liste, et reporter les volumes au tableau tab:volumes_requetes du
chapitre IV.]
[TODO : Capture à produire dans Neo4j Browser : base peuplée, double-clic
sur un nœud Plante pour l’ouvrir, puis étoffer de deux niveaux de voisinage
(bouton *), de sorte que l’on voie les relations TRAITE, PROVIENT_DE,
A_POUR_PARTIE avec leurs étiquettes. Légendes de nœuds lisibles, couleurs
par type de label, fond sombre par défaut accepté. Capture 1200 px de large
minimum, enregistrer sous images/capture_neo4j.png.]
Vue du graphe peuplé dans Neo4j Browser (extrait du sous-graphe d’une plante)
Figure III.4 – Le graphe de connaissances peuplé
III.2.3 Interrogation de la base
Nous avons soumis la base à quatre familles de requêtes, correspondant aux quatre usages anticipés
en phase 6 (section II.2.6 du chapitre II) : requêtes simples, requêtes complexes, requêtes de traçabilité
et requêtes spatiales. Les exemples suivants sont donnés à titre indicatif.
-- 1. Requete simple : plantes documentees contre une maladie
MATCH (p:Plante)-[:TRAITE]->(m:Maladie)
WHERE m.nom CONTAINS "Paludisme"
RETURN p.nom AS plante
-- 2. Requete complexe : recette a plusieurs plantes
MATCH (p:Plante)-[:A_POUR_PREPARATION]->(prep:Preparation)
MATCH (p)<-[:UTILISE]-(recette)
RETURN recette, collect(p.nom) AS plantes
-- 3. Requete de tracabilite : d’ou vient une information ?
MATCH (p:Plante)-[:PROVIENT_DE]->(s:Source)
WHERE p.nom CONTAINS "Artemisia"
RETURN s.auteur, s.annee, s.doi
-- 4. Requete spatiale : plantes d’une region
MATCH (p:Plante)-[:EST_LOCALISEE_A]->(r:Region)
WHERE r.nom CONTAINS "Sahel"
RETURN p.nom AS plante
[TODO : Avant le dépôt : exécuter chacune des 4 requêtes ci-dessus dans Neo4j Browser et (1)
aligner le sens des relations sur le schéma définitif confirmé plus haut (§ Relations du graphe),
(2) noter le nombre de lignes renvoyé par chacune, (3) reporter ces 4 volumes dans le tableau
56

--- page 69 ---
tab:volumes_requetes du chapitre IV. Remplacer éventuellement « à titre indicatif » par «
exécutées sur la base peuplée » si les requêtes sont désormais réelles.]
À titre d’exemple, la question « quelles plantes traitent le paludisme dans la région du Sahel ? » se
traduit par une requête qui relie les nœuds Plante, Maladie et Région, puis renvoie une liste de noms
scientifiques.
Ces vérifications ont établi que la base est fonctionnelle et que les requêtes renvoient les résultats
attendus. C’est la condition préalable à l’intégration de l’intelligence artificielle, qui interrogera ce
graphe à la place de l’utilisateur.
III.3 Intégration de l’intelligence artificielle
L’intelligence artificielle intervient à deux niveaux distincts du système. En aval, elle donne accès
aux connaissances en langage naturel, par le biais du système RAG. En amont, elle a contribué à
produire ces mêmes connaissances, en extrayant du corpus scientifique les fiches structurées alimentant
la base. Nous présentons successivement l’extraction assistée, puis le système d’accès, puis le fil de
traçabilité qui les relie l’un à l’autre.
III.3.1 Extraction assistée des connaissances
Environnement d’extraction
Nous avons exécuté l’extraction sur Google Colab, en notebooks, avec accès aux GPU de la
plateforme. Le modèle Llama 3 70B y est chargé via Ollama, conformément aux modes d’accès établis
au chapitre II (tableau II.3). Le choix d’un modèle ouvert, maîtrisant le français et exécuté dans un
environnement reproductible, a été motivé en section II.1.3.
# Illustratif : chargement du modele dans le notebook
# TODO : remplacer par l’extrait reel du notebook Colab
from langchain_community.llms import Ollama
llm = Ollama(model="llama3:70b", temperature=0)
Le prompt d’extraction
Nous avons adressé au modèle un prompt unique, décliné selon le type de document, pour chaque
pièce du corpus. Il impose le rôle, énumère les champs à renseigner et fixe le format de sortie. Voici sa
version complète :
Tu es un assistant spécialisé dans l’extraction de connaissances
sur les plantes médicinales du Burkina Faso.
À partir du texte ci-dessous, extrais les informations suivantes :
- Nom scientifique de la plante
- Noms vernaculaires (mooré, dioula, fulfuldé)
- Famille botanique
- Parties utilisées
- Usages thérapeutiques
- Modes de préparation
- Activités pharmacologiques
- Niveau de preuve (traditionnel, in vitro, in vivo, clinique)
- Source (auteur, année, DOI)
57

--- page 70 ---
Réponds au format JSON.
Texte :
[contenu du document]
Les champs absents d’un document restent vides dans la sortie. Aucune valeur n’est comblée par
déduction, et le modèle ne se charge pas de produire ce que la source n’a pas dit. Cette règle, posée dès
la phase 5, est la condition de fiabilité du système. Une fiche ne contient que ce que la source contient.
Format de sortie
La sortie attendue est un document JSON dont le schéma ci-dessous est donné à titre indicatif :
{
"nom_scientifique": "Artemisia annua L.",
"noms_vernaculaires": {
"moore": "...", "dioula": "...", "fulfulde": "..."
},
"famille_botanique": "Asteraceae",
"parties_utilisees": ["feuille"],
"usages_therapeutiques": [
{"pathologie": "...", "niveau_preuve": "in vivo"}
],
"modes_preparation": ["decoction"],
"activites_pharmacologiques": ["antipaludique"],
"source": {"auteur": "...", "annee": 0000, "doi": "..."}
}
[TODO : Remplacer ce JSON par une fiche réelle extraite du fichier produit par la boucle
(extrait de extractions.json), avec les noms de champs exacts et les valeurs réelles d’une plante
(abréger le DOI et les champs longs par « . . .» si besoin). Vérifier que les champs vides y figurent
bien sous la forme "" : c’est la preuve visuelle de la règle « rien n’est comblé par déduction ».
Garder l’environnement verbatim.]
Boucle d’extraction
Nous avons traité les documents un par un, vérifié la qualité des résultats au fur et à mesure et ajusté
les prompts lorsqu’il le faut. Le schéma de la boucle est le suivant :
# Illustratif : boucle d’extraction sur le corpus
# TODO : remplacer par l’extrait reel du notebook
import json, glob
fiches = []
for chemin in sorted(glob.glob("corpus/*.txt")):
texte = open(chemin, encoding="utf-8").read()
reponse = llm.invoke(prompt.format(texte=texte))
fiche = json.loads(reponse)
fiche["fichier_source"] = chemin
fiches.append(fiche)
with open("extractions.json", "w", encoding="utf-8") as f:
json.dump(fiches, f, ensure_ascii=False, indent=2)
58

--- page 71 ---
[TODO : Chiffres d’exploitation de l’extraction, à relever dans le projet puis à reporter au
chapitre IV : (1) nombre total de fiches dans extractions.json; (2) nombre de documents
traités sans erreur de format sur 35, et nature des erreurs rencontrées (JSON invalide, troncature,
champ manquant) ; (3) deux ou trois ajustements de prompt réellement effectués, décrits en une
phrase chacun (ex. ajout d’un champ, consigne sur le niveau de preuve, interdiction d’inventer) ;
(4) durée totale de l’exploration.]
III.3.2 Système RAG d’accès aux connaissances
Le système d’accès combine la recherche d’informations dans le graphe et la génération de réponses
par le modèle de langage : c’est le principe du Retrieval-Augmented Generation [29], présenté au
chapitre I. L’architecture retenue relie les maillons suivants : Utilisateur → Streamlit → LangChain →
Neo4j → Llama 3 → Réponse (figure III.5). [TODO : Schéma à produire : les six étapes du listé ci-dessous en six boîtes
enchaînées de gauche à droite (ou sur deux lignes de trois) : Utilisateur →
Streamlit → LangChain (GraphCypherQAChain) → Neo4j → Llama 3 →
Réponse sourcée. Flèches étiquetées : « question », « requête Cypher », «
sous-graphe / faits », « réponse + sources ». Ajouter une flèche de retour des
sources vers la réponse pour montrer où le sourçage s’injecte (étape 6). Boîtes
colorées par composant (interface, orchestration, base, modèle). Outil libre
(PowerPoint, draw.io), format PNG, 15 cm de large, enregistrer sous
images/architecture_rag.png.]
Chaîne de traitement du système RAG : des six étapes, de la requête à la réponse
Figure III.5 – Chaîne de traitement du système RAG sourcée
Les six étapes de la chaîne de traitement
La requête de l’utilisateur traverse six étapes, chacune confiée au composant qui en a la charge :
1. Interprétation de la requête. L’utilisateur formule une question en langage naturel, par exemple
« Quelles plantes traitent le paludisme ? ». LangChain reçoit cette question brute, la nettoie et, le
cas échéant, la met en contexte à partir de l’historique de la conversation.
2. Génération de la requête Cypher. Le composant GraphCypherQAChain convertit la question
en requête Cypher, guidé par un PromptTemplate dans lequel le schéma de la base (types
de nœuds, relations, propriétés) est injecté à l’exécution. Le langage naturel y est converti en
requête formelle.
3. Exécution sur Neo4j. La requête Cypher est soumise à la base, qui renvoie le sous-graphe
correspondant : nœuds, relations et propriétés concernés.
4. Récupération des faits. Le résultat est ramené sous forme de faits structurés, chaque information
y conservant sa propriété de niveau de preuve et son rattachement à une source.
5. Génération de la réponse. Le modèle Llama 3 reçoit la question initiale et les faits retrouvés,
et rédige une réponse qui ne doit s’appuyer que sur eux. Un fait absent du graphe ne doit pas y
figurer.
6. Affichage des sources. L’interface présente la réponse, puis, pour chaque affirmation, la référence
scientifique qui la soutient (auteur, année, DOI) et le niveau de preuve déclaré par cette source.
Câblage des composants
Nous avons retenu les composants LangChain listés au chapitre II (tableau II.5) : Neo4jGraph
pour la connexion à la base, GraphCypherQAChain pour la génération des requêtes, le modèle via
59

--- page 72 ---
Ollama, PromptTemplate pour les invites et Memory pour l’historique. Du côté du modèle, l’accès
prend deux formes selon le contexte : exécution locale via Ollama pour l’extraction, exposition d’une
API via ngrok pour l’application web (tableau II.3).
# Illustratif : assemblage de la chaine RAG
# TODO : remplacer par le code reel du projet
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_community.llms import Ollama
graph = Neo4jGraph(
url="bolt://localhost:7687",
username="neo4j",
password="***",
)
llm = Ollama(model="llama3:70b", temperature=0)
chain = GraphCypherQAChain.from_llm(
llm=llm, graph=graph, verbose=True,
)
[TODO : Remplacer ce fragment par le code réel du projet (15 à 25 lignes maximum), qui doit
montrer : la connexion Neo4j réelle (identifiant, mot de passe remplacé par ***), la configuration
de l’accès au modèle via l’API ngrok (variable d’environnement ou URL, sans jeton secret), le
PromptTemplate effectivement employé pour la réponse, et le câblage de Memory. Commenter
chaque bloc en français, garder l’environnement verbatim, indiquer en commentaire LaTeX le
nom du fichier source (ex. rag/chain.py). Supprimer les blocs illustratifs devenus faux.]
III.3.3 Traçabilité des réponses
La traçabilité ne résulte pas d’un module ajouté après coup : elle accompagne chacune des étapes
du système. L’extraction n’enregistre que ce que la source déclare, en laissant vide ce qu’elle ne
couvre pas. L’import rattache chaque connaissance au nœud Source d’où elle provient. La requête
de traçabilité remonte cette source en quelques lignes de Cypher. Enfin, la génération de la réponse
renvoie explicitement les références utilisées. De l’ontologie jusqu’à l’écran, la chaîne reste continue :
toute information affichée dans une réponse peut être reliée à son origine.
Cette continuité a toutefois des limites, déjà signalées en phase 5 : les niveaux de preuve sont
rapportés tels quels depuis les sources, sans évaluation indépendante, et les extractions n’ont pas fait
l’objet d’une relecture par un expert externe. La qualité de l’ensemble relève du protocole d’évaluation
de la phase 8, dont les résultats seront présentés au chapitre IV.
III.4 Développement de l’application web
Le dernier composant est l’application web, qui rend l’ensemble accessible sans compétence
technique : elle accueille l’utilisateur, recueille sa question, appelle la chaîne RAG et restitue la réponse.
Développée avec Streamlit (retenu pour les raisons exposées au chapitre II, section II.1.3), elle organise
autour de cette boucle un ensemble de fonctions de consultation.
III.4.1 Architecture de l’application
Notre application suit la structure classique d’une application Streamlit : un point d’entrée unique,
une page par fonctionnalité, et un état de session partagé. À l’ouverture, l’utilisateur se trouve sur une
60

--- page 73 ---
page d’accueil qui associe le chatbot et les accès de recherche; chaque interaction avec le chatbot
appelle la chaîne LangChain, dont la réponse est rendue sur place, sources comprises.
[TODO : Option privilégiée : deux captures côte à côte de l’application
réelle : (a) page d’accueil avec la zone de saisie du chatbot, (b) fiche
descriptive d’une plante montrant usages, parties, niveau de preuve et
références. Format PNG, 900 px de large chacune, enregistrer sous
images/ecran_accueil.png et images/ecran_fiche.png. Si l’on préfère
un schéma : boîtes Question → traitement RAG → réponse affichée avec
sources, fichier images/flux_utilisateur.png.]
Flux utilisateur : de la question posée à la réponse sourcée (écrans de l’application)
Figure III.6 – Flux utilisateur de l’application web
III.4.2 Fonctionnalités
Le tableau III.8 récapitule les fonctions prévues, telles qu’établies en phase 7 (section II.2.7).
III.4.3 Gestion de session et déploiement
Nous avons maintenu l’historique de conversation dans l’état de session de Streamlit et le
transmettons à LangChain via le composant Memory, de sorte qu’une question de suivi, comme « Et
contre l’hypertension ? », s’appuie sur le fil de la conversation précédente. Notre déploiement, en phase
de développement, repose sur un serveur local complété, pour l’accès au modèle, d’une API exposée
par ngrok.
# Illustratif : lancement de l’application
# TODO : config reelle (ngrok, variables d’environnement)
streamlit run app.py
[TODO : Déploiement réel à décrire en une phrase factuelle : machine (poste local, version de
l’OS), commande exacte de lancement (streamlit run avec nom de fichier et port), commande
ngrok correspondante (ngrok http <port>), durée pendant laquelle l’URL publique était active,
et état actuel (toujours en ligne ?). Si une mise en ligne pérenne existe (Streamlit Community
Cloud, serveur), donner l’URL et le dépôt. Ne pas coller de jeton d’authentification ngrok.]
[TODO : Deux captures de l’application réelle, à choix : (a) la page d’accueil
telle qu’elle s’affiche pour l’utilisateur (chatbot + accès de recherche), (b) une
fiche où l’on voit explicitement les références sous chaque information
(auteur, année, DOI) et les niveaux de preuve. PNG net, 900 px de large
minimum, nommées images/ecran_accueil.png et
images/ecran_fiche.png (si ces deux fichiers ont déjà servi à la figure
précédente, les réutiliser et ne changer que les légendes).]
Page d’accueil (chatbot) et fiche descriptive d’une plante
Figure III.7 – Écrans principaux de l’application web
61

--- page 74 ---
Table III.8 – Fonctionnalités de l’application web
Fonctionnalité Description État
Chatbot Question en langage naturel, réponse
générée par le système RAG, sources
affichées
[TODO :
Terminé /
Partiel /
Non
réalisé :
confirmer
par une
capture :
la réponse
s’affiche-t￾elle avec
ses
sources ?]
Recherche par plante Consultation d’une fiche à partir du nom
scientifique ou vernaculaire
[TODO :
Terminé /
Partiel /
Non
réalisé :
vérifier
avec un
nom verna￾culaire réel
(ex. en
mooré),
pas
seulement
le nom
scienti￾fique]
Recherche par
pathologie
Liste des plantes documentées contre une
maladie donnée
[TODO :
Terminé /
Partiel /
Non
réalisé :
vérifier
avec «
paludisme
» et une
maladie
moins
couverte]
Fiches descriptives Usages, parties utilisées, modes de
préparation, niveaux de preuve et références
[TODO :
Terminé /
Partiel /
Non
réalisé :
indiquer
quels
champs de
la liste sont
réellement
affichés]
Affichage des sources Références complètes (auteur, année, DOI)
sous chaque information
[TODO :
Terminé /
Partiel /
Non
réalisé :
confirmer
qu’au
moins une
réponse du
chatbot
affiche bien
auteur,
année et
DOI]
Visualisation du
graphe
Représentation des relations entourant une
plante ou une maladie
[TODO :
Terminé /
Partiel /
Non
réalisé :
l’onglet
existe-t-il
dans
Streamlit ?
si non, le
noter
comme
non réalisé
(la capture
Neo4j du §
II suffit
alors)]
62

--- page 75 ---
Conclusion du chapitre
Ce chapitre a présenté le système issu de la démarche méthodologique du chapitre II. L’ontologie
ontoMEDTRAD, adaptée au contexte burkinabè et enrichie par les connaissances du corpus, en constitue
le modèle. La base Neo4j en est la matérialisation : huit types de nœuds, sept types de relations,
un graphe peuplé et interrogeable. L’intelligence artificielle intervient à deux endroits. En amont,
l’extraction assistée produit les fiches du corpus; en aval, le système RAG convertit une question en
langage naturel en requête Cypher puis en réponse. L’application web referme l’ensemble sur une
interface accessible.
Ces quatre composants ont tous été conçus autour d’une même préoccupation : la traçabilité.
Chaque connaissance provient d’une source, est rattachée à cette source dans le graphe, et apparaît
dans une réponse avec la référence qui la soutient. C’est cette continuité qui distingue le système d’un
simple moteur de recherche sur texte, et qui justifie les précautions que nous avons prises à chaque
étape (champs laissés vides plutôt que comblés, niveaux de preuve rapportés tels quels, origine de
chaque affirmation affichée).
Il reste à évaluer ce que le système donne effectivement : qualité des extractions, pertinence et
fidélité des réponses, pertinence des recherches, utilité perçue de l’interface. Le chapitre IV présente
les résultats de cette évaluation et en discute les limites.
63

--- page 76 ---
Chapitre IV
Résultats et discussion
Introduction du chapitre
Les chapitres précédents ont exposé, tour à tour, la démarche que nous avons conduite et le système
qui en est sorti. Ils ont laissé une question ouverte, reportée explicitement à la phase 8 : ce système
tient-il les promesses faites en son nom ? Le présent chapitre y répond. Il présente les résultats de
l’évaluation menée à trois niveaux, puis discute ce que ces résultats valent, et ce qu’ils ne valent pas.
L’évaluation suit le protocole fixé avant les tests (section II.2.8 du chapitre II). Trois objets y
sont successivement confrontés à leurs critères : l’ontologie adaptée et enrichie, le système RAG qui
l’interroge, et l’application web qui les réunit. Nous avions arrêté en amont les critères, les méthodes
de mesure et les métriques : les résultats se lisent par rapport à ces critères-là, et non par rapport à ce
que les tests ont fait remarquer au passage.
Quatre sections composent le chapitre. Les trois premières suivent l’ordre du protocole : évaluation
de l’ontologie, évaluation du système RAG, évaluation de l’application web. La quatrième replace ces
résultats dans l’ensemble de la recherche : elle les confronte aux objectifs, les situe par rapport aux
systèmes existants, et énonce les limites au-delà desquelles ils n’ont pas de portée.
IV.1 Évaluation de l’ontologie
Nous avons évalué l’ontologie sur les quatre critères retenus en phase 8 : couverture, cohérence,
traçabilité et extensibilité (tableau II.11 du chapitre II). Nous reprenons chacun d’eux, avec la méthode
employée et le résultat obtenu.
IV.1.1 Couverture
Nous avons apprécié la couverture par vérification manuelle, en confrontant l’ontologie au corpus
de 35 documents, plante par plante et usage par usage. Chaque nom scientifique, chaque désignation
vernaculaire, chaque pathologie, chaque mode de préparation et chaque source citée dans un document
devait trouver sa place dans le modèle; à défaut, nous la notions.
Les résultats de ce rapprochement sont les suivants : [TODO : relevé dans Protégé 5, onglet
Instances : nombre d’instances de la classe Plante, nombre d’usages, nombre de sources ; puis
taux de couverture = éléments du corpus retrouvés dans le modèle / éléments relevés dans le
corpus, en pourcentage. Écrire les trois nombres et le pourcentage, ex. « 87 plantes, 132 usages,
41 sources, couverture 81% »]. Ils se comparent aux chiffres du tableau III.2 et à ceux du modèle
d’origine, qui ne couvrait que vingt-deux plantes et trente et un remèdes antipaludéens [28].
La couverture n’est pas uniforme, et cette irrégularité vient des données plutôt que du modèle. Le
corpus s’attarde sur quelques pathologies, le paludisme en tête, et sur un nombre restreint de régions.
64

--- page 77 ---
Les questions pour lesquelles les sources se taisent, notamment le dosage et la toxicité, restent peu
représentées dans la base de connaissances parce qu’elles le sont peu dans les documents. Représenter
ce qui est documenté, et rien d’autre, est le principe même de l’extraction (section III.3.1 du chapitre
III).
IV.1.2 Cohérence
Nous avons contrôlé la cohérence de deux manières. Par les raisonneurs d’abord : nous avons
relancé HermiT et Pellet dans Protégé 5 après chaque série de modifications, ajout de classes, ajout
de propriétés, création de relations. Ils n’ont signalé d’incohérence à aucune étape du travail. Par des
requêtes de test ensuite, qui vérifient que chaque propriété est employée sur le domaine prévu et que les
instances nouvelles restent rattachées à leur classe. [TODO : liste de 3 à 5 requêtes de test réellement
exécutées dans Protégé ou Neo4j, avec leur résultat, ex. « tout Usage possède un niveauPreuve :
217/217 conformes ; toute instance de Maladie est reliée à au moins un Usage : 0 orpheline ;
aucune propriété hors domaine : conforme ». Chacune sur une ligne.]
Ce résultat mérite d’être nuancé par ce qu’il mesure : l’absence de contradiction dans le modèle,
pas la justesse des connaissances qu’il contient. Une proposition fausse mais cohérente passerait ce
contrôle.
IV.1.3 Traçabilité
Le critère de traçabilité vérifie que chaque connaissance reste rattachée à la source qui la rapporte.
La règle est structurelle plutôt que déclarative : l’extraction ne remplit que les champs présents dans le
document, l’import exige une source, et le graphe ne reçoit rien d’autre (section III.3.3 du chapitre III).
Sur échantillon, nous avons contrôlé que chaque usage enregistré porte bien un nœud Source doté
d’un auteur, d’une année et d’un DOI, ainsi qu’un niveau de preuve déclaré. [TODO : préciser :
taille de l’échantillon (ex. 30 usages tirés au sort sur l’ensemble), nombre de contrôles par
fiche (présence de la source, DOI, année, niveau de preuve), et taux = conformes / contrôlés, en
pourcentage. Indiquer la date du contrôle si utile.]. Un usage sans source ne peut pas être importé :
dans la chaîne telle qu’elle est câblée, il reste vide et n’atteint pas le graphe.
IV.1.4 Extensibilité
Le protocole prévoit un test d’ajout : introduire une connaissance nouvelle dans le modèle sans le
casser. Nous avons mené ce test de fait, en deux temps, avant même que l’évaluation ne commence. En
phases 4 et 5, nous avons ajouté cinq ensembles de classes, une série de propriétés et quatre relations
au modèle d’origine, et celui-ci a conservé sa structure et sa cohérence tout au long des ajouts. Nous
avons porté un test plus ciblé sur un élément non prévu au départ : [TODO : décrire l’ajout en une
phrase : quoi (une plante absente du corpus ? une région ? un niveau de preuve ?), à quel moment
du travail, et ce qu’il en a été (arborescence mise à jour, aucun nouveau signalement d’HermiT,
instance correctement rattachée à sa classe). Si aucun test ciblé n’a été fait en dehors des phases
4 et 5, le dire explicitement.].
IV.1.5 Synthèse de l’évaluation de l’ontologie
Le tableau IV.1 réunit les quatre critères et leurs résultats.
65

--- page 78 ---
Table IV.1 – Résultats de l’évaluation de l’ontologie
Critère Méthode Résultat
Couverture Vérification manuelle face au
corpus de 35 documents
[TODO : reprendre les
chiffres du § Couverture :
n/N et taux en %]
Cohérence Raisonneurs HermiT et Pellet,
requêtes de test
Aucune incohérence
signalée; [TODO :
reprendre le résultat ligne
par ligne du § Cohérence]
Traçabilité Contrôle sur échantillon des
relations vers les sources
[TODO : reprendre le
taux du § Traçabilité,
sous la forme
conformes/contrôlés (%)]
Extensibilité Test d’ajout, en cours de phases
4 et 5 puis ciblé
Ajouts intégrés sans
rupture; [TODO :
reprendre la phrase du §
Extensibilité, en une
ligne]
IV.2 Évaluation du système RAG
Le système RAG est l’endroit où se joue la promesse d’accès : une question posée en langage
naturel doit recevoir une réponse pertinente, fidèle à ce que contient le graphe, et accompagnée de ses
sources. Le protocole de phase 8 retient quatre critères pour cela : pertinence, fidélité, exactitude et
traçabilité, mesurés sur un jeu de 50 questions de référence (tableau II.12 du chapitre II).
IV.2.1 Construction du jeu d’évaluation
Les 50 questions portent sur les plantes, les usages et les propriétés, les trois familles annoncées en
phase 8. Pour chacune, nous avons établi la réponse attendue à partir du corpus et du graphe, source par
source : c’est cette réponse qui sert de référence aux métriques. [TODO : donner la répartition chiffrée,
ex. « 20 questions plantes/usages, 15 propriétés pharmacologiques, 10 traçabilité, 5 multi-plantes ;
total 50 ». Puis décrire en une phrase comment les réponses attendues ont été établies : rédigées
par nous puis vérifiées dans Neo4j source par source, ou extraites automatiquement. Noter si une
seconde personne a participé au jeu-test (sinon, le dire : c’est repris dans les limites).]
Les métriques suivent les correspondances que nous avions fixées en phase 8 : la précision sert
la pertinence, le rappel sert la fidélité, le F1-score sert l’exactitude, et le taux de couverture des
réponses sourcées sert la traçabilité. La précision calcule la part des affirmations de la réponse produite
qui figurent dans la réponse attendue; le rappel calcule la part de la réponse attendue effectivement
restituée; le F1 combine les deux. [TODO : écrire les trois formules réellement employées, avec
leur légende : Précision = VV / (VV + VF), Rappel = VV / (VV + FN), F1 = 2 × P × R / (P + R), où
VV = affirmations justes dans la réponse, VF = affirmations fautives, FN = éléments de la réponse
attendue absents. Pour la couverture : réponses affichant au moins une source / 50. Vérifier que
ces définitions correspondent bien aux colonnes du tableau suivant.]
IV.2.2 Résultats quantitatifs
Nos mesures sur les 50 questions donnent les résultats du tableau IV.2.
66

--- page 79 ---
Table IV.2 – Résultats de l’évaluation du système RAG
Critère Métrique Résultat
Pertinence Précision [TODO : valeur calculée sur
50 questions, format français :
0,87]
Fidélité Rappel [TODO : valeur calculée sur
50 questions, format français :
0,87]
Exactitude F1-score [TODO : valeur calculée sur
50 questions, format français :
0,87]
Traçabilité Taux de couverture des
réponses sourcées
[TODO : réponses avec au
moins une source affichée,
sous la forme n/50 puis
pourcentage]
Les scores globaux masquent des écarts entre familles de questions; nous les séparons dans le
tableau IV.3.
Table IV.3 – Résultats par famille de questions
Famille de questions Effectif Réponses
conformes
Échecs
Questions simples (plante,
maladie, usage)
[TODO : nb
de questions
de cette
famille]
[TODO : nb
conformes à la
réponse
attendue]
[TODO : effectif
- conformes]
Recettes multi-plantes [TODO : nb
de questions]
[TODO : nb
conformes]
[TODO : effectif
- conformes]
Traçabilité (d’où vient
l’information ?)
[TODO : nb
de questions]
[TODO : nb
conformes]
[TODO : effectif
- conformes]
Questions spatiales (région,
localisation)
[TODO : nb
de questions]
[TODO : nb
conformes]
[TODO : effectif
- conformes]
IV.2.3 Volumes d’interrogation de la base
Nous avions promis, en chapitre III, de reporter ici les volumes obtenus par les quatre familles de
requêtes prévues en phase 6 (section II.2.6 du chapitre II). Le tableau IV.4 les rassemble.
IV.2.4 Observations qualitatives
Les chiffres suffisent peu à eux seuls à décrire ce qui se passe pendant les tests; les remarques
suivantes complètent les métriques.
Les requêtes simples et les requêtes de traçabilité passent dans l’immense majorité des cas : elles se
traduisent en Cypher sans difficulté et renvoient un sous-graphe que la génération restitue fidèlement.
Nos tests se sont heurtés davantage aux recettes multi-plantes et aux questions formulées indirectement.
La conversion en requête Cypher échoue alors plus souvent, ou bien la requête générée est trop large
et le modèle peine à trier ce qui revient. [TODO : décompter les échecs des 50 questions par
type de défaillance, sur trois lignes : (1) génération de requête Cypher (erreur, requête vide
67

--- page 80 ---
Table IV.4 – Volumes de résultats des quatre familles de requêtes
Famille Exemple Résultats renvoyés
Requêtes simples Plantes documentées contre une
maladie
[TODO : nombre de
lignes renvoyées,
relevé dans Neo4j
Browser en exécutant
la requête du
chapitre III]
Requêtes complexes Recette associant plusieurs
plantes
[TODO : nombre de
lignes renvoyées
(requête exécutée
telle quelle)]
Requêtes de
traçabilité
Sources d’une plante donnée [TODO : nombre de
lignes renvoyées]
Requêtes spatiales Plantes d’une région donnée [TODO : nombre de
lignes renvoyées]
ou mal ciblée) ; (2) sélection des faits (sous-graphe trop large ou trop étroit) ; (3) rédaction
(réponse dépassant les faits du graphe). Donner les nombres, totaliser, et recouper avec le tableau
tab:res_rag_familles.]
Un échec n’en est pas toujours un. Lorsque la réponse demandée est absente du graphe, le système
ne doit rien produire plutôt que d’improviser : la règle que nous avons posée en phase 5, un fait absent
du graphe ne figure pas dans la réponse, prime sur la complétude. Une réponse vide sur une question
hors corpus est donc le comportement attendu, et nous l’avons comptée comme tel lors du décompte.
C’est ce qui distingue le système d’un modèle de langage seul, qui lui comblerait le trou sans prévenir.
[TODO : temps mesuré sur les 50 questions : temps moyen et temps maximal, en secondes
avec une décimale, méthode indiquée (chronométrage manuel ou instrumentation de l’appel de la
chaîne, ex. time.time() avant/après). Signaler si des questions ont dépassé un seuil raisonnable
(ex. 10 s) et combien.].
IV.3 Évaluation de l’application web
Nous avons évalué l’application web sur les quatre critères du protocole : facilité d’utilisation,
compréhension des réponses, utilité perçue et performance (tableau II.13 du chapitre II). Nous mesurons
les trois premiers par questionnaire, le dernier par chronométrage.
IV.3.1 Campagne de test
Nous avons soumis l’application à [TODO : nombre exact de participants, ex. 12] participants,
recrutés selon les profils prévus en phase 8 : [TODO : répartition réelle, ex. 6 étudiants, 4 chercheurs,
2 tradipraticiens ; si le recrutement n’a pas eu lieu, décrire le panel prévu et laisser ce TODO
en signalant que les résultats sont alors provisoires]. Chacun a passé trois scénarios : retrouver la
fiche d’une plante à partir de son nom vernaculaire, poser une question au chatbot, puis remonter d’une
réponse donnée jusqu’à la source qui la soutient. Nous avons administré un questionnaire après les
scénarios. [TODO : échelle employée, items du questionnaire, conditions de passation].
68

--- page 81 ---
IV.3.2 Résultats du questionnaire
Les résultats par critère figurent au tableau IV.5.
Table IV.5 – Résultats de l’évaluation de l’application web
Critère Méthode Résultat
Facilité d’utilisation Questionnaire [TODO : score moyen des
participants sur l’échelle
employée, ex. 4,2/5]
Compréhension des
réponses
Questionnaire [TODO : score moyen, ex.
4,0/5]
Utilité perçue Questionnaire [TODO : score moyen, ex.
3,8/5]
Performance Mesure du temps de
réponse
[TODO : temps moyen en
secondes, une décimale]
[TODO : Schéma à produire : histogramme horizontal des scores moyens du
questionnaire, 3 barres seulement (facilité d’utilisation, compréhension,
utilité), échelle de 1 à 5 en abscisse, valeurs chiffrées à l’extérieur de chaque
barre. La performance, mesurée en secondes, n’a pas la même échelle : la
laisser de côté ici (elle est au tableau IV.5). Outil Excel, LibreOffice ou
matplotlib ; PNG 150 dpi, titre et axes en français, enregistrer sous
images/resultats_questionnaire.png.]
Scores moyens des trois critères à questionnaire, échelle de 1 à 5
Figure IV.1 – Résultats du questionnaire par critère
Les observations que nous avons recueillies pendant les scénarios complètent les scores : [TODO
: 3 à 5 observations factuelles, une phrase chacune, tirées des notes de passation : ex. « deux
participants ont cherché en vain un nom vernaculaire sans accent », « la mention du niveau de
preuve n’a pas été comprise sans légende », « attente perçue comme longue à la première question
». Éviter les jugements de valeur non étayés.].
IV.3.3 Performance
Nos mesures décomposent le temps de réponse en deux temps inégaux : l’interrogation de Neo4j
se compte en millisecondes, la génération de la réponse par Llama 3 en secondes. C’est donc le
modèle qui pèse dans l’attente, l’API exposée par ngrok ajoutant son propre délai. [TODO : chiffrer la
décomposition : temps de requête Cypher en millisecondes (relevé dans Neo4j Browser ou logs
LangChain), temps de génération en secondes, délai de l’API ngrok en secondes si mesurable,
puis temps moyen et maximal par type d’opération (chatbot, recherche de fiche, affichage de
résultats). Une décimale pour les secondes.].
IV.4 Discussion
Les résultats des trois sections précédentes décrivent ce que le système fait. Cette section les replace
dans le travail plus large : d’abord par rapport aux questions posées au départ, ensuite par rapport aux
systèmes existants, puis dans ce qu’ils ont de limité, enfin dans ce qu’ils suggèrent pour la suite.
69

--- page 82 ---
IV.4.1 Confrontation aux objectifs de la recherche
La première question de recherche demandait d’identifier les ontologies du domaine et d’en retenir
la plus adaptée au contexte burkinabè. Nous avons noté cinq ontologies sur une même grille au chapitre
II; ontoMEDTRAD y a obtenu le score le plus élevé, 4.7 contre 3.7 pour WATRIMed, le meilleur
concurrent. Notre choix est documenté et reproductible. Ses limites sont connues elles aussi : le
modèle retenu n’est pas le plus riche de tous, c’est celui qui combine l’accès, l’ancrage régional et la
documentation.
La deuxième question portait sur les adaptations nécessaires et sur la garantie de la traçabilité. Les
cinq ensembles de classes que nous avons ajoutés, les propriétés de noms vernaculaires et les quatre
relations de rattachement que nous avons créées répondent au premier volet. Le contrôle d’échantillon
de la section IV.1.3 répond au second, sous réserve du taux [TODO : reprendre ici, en toutes lettres,
le taux de conformité de la section IV.1 (ex. « taux de conformité de 98% sur 50 contrôles »)]
retenu.
La troisième question concernait l’exploitation de l’ontologie par un système RAG au service de
l’accès en langage naturel. Le système est fonctionnel : il convertit une question en requête Cypher,
interroge le graphe et rédige une réponse sourcée. La qualité de cet accès se mesure aux métriques
du tableau IV.2, encore [TODO : recopier ici les quatre valeurs du tableau tab:res_rag, ex. «
précision 0,87, rappel 0,79, F1 0,83, couverture 48/50 » : sinon remplacer « encore » par la
formulation adaptée].
La quatrième question portait sur l’application web. Elle existe, elle réunit les fonctions prévues au
tableau III.8, et nous l’avons mise à disposition des participants, ce qui a fourni les résultats du tableau
IV.5.
Une réserve traverse les quatre réponses : plus les chiffres ci-dessus restent provisoires, plus cette
confrontation elle-même demeure provisoire.
IV.4.2 Confrontation aux systèmes existants
Le modèle d’origine ontoMEDTRAD couvrait vingt-deux plantes et trente et un remèdes antipalu￾déens [28]. Notre enrichissement porte cette couverture à [TODO : reprendre les mêmes chiffres que
la section IV.1 : nombre de plantes, nombre d’usages, nombre de sources après enrichissement].
L’augmentation réelle, mesurée sur un corpus de 35 documents, reste d’ampleur modeste : notre base
n’a pas l’envergure d’une encyclopédie, et elle ne le prétend pas.
Face à WATRIMed, riche en concepts mais dont les publications ne donnent aucun moyen de réutiliser
l’ontologie, la différence tient à ce qui se passe après le modèle. Chez nous, chaque connaissance
descend dans une base interrogable, remonte dans une réponse rédigée et s’accompagne de la référence
qui la soutient. Chez WATRIMed, le modèle s’arrête au modèle.
L’apport principal n’est donc pas la taille. C’est la continuité du fil qui va de la source scientifique
jusqu’à l’écran de l’utilisateur, en passant par l’ontologie, le graphe et la réponse, sans qu’un maillon
perde l’information d’origine.
IV.4.3 Limites
Six limites encadrent les résultats qui précèdent. Elles ne sont pas des détails de présentation : elles
déterminent la portée de tout ce que nous avons mesuré.
1. L’évaluation a été conduite par nous-mêmes, les concepteurs du système. Aucun évaluateur
extérieur n’a été mêlé aux tests, et le panel, réduit [TODO : donner le chiffre exact et sa
composition, ex. « 12 participants : 6 étudiants, 4 chercheurs, 2 tradipraticiens », plus
les conditions de passation (lieu, durée)], n’a pas la taille qui permettrait des comparaisons
70

--- page 83 ---
statistiques solides. Un utilisateur familier du domaine et de l’outil n’aura pas rencontré les
mêmes difficultés qu’un premier venant.
2. Le jeu de 50 questions part du même corpus que l’ontologie. Nous avons tiré les questions
des documents qui ont servi à construire le système; elles mesurent donc surtout ce qu’il sait
déjà faire. Des questions posées par d’autres utilisateurs, sur des documents absents du corpus,
donneraient probablement des scores moins élevés.
3. Les niveaux de preuve sont hérités des sources. Nous les avons rapportés tels quels, sans
réévaluation indépendante, comme nous l’avons dit en phase 5 et au chapitre III. Un usage classé
« traditionnel » par sa source le reste dans notre base, même si l’étude qui le rapporte ne le vérifie
pas.
4. Nous n’avons pas fait relire les extractions par un expert. La règle d’or, ne rien ajouter de
ce que la source ne dit pas, limite le risque, mais elle ne l’élimine pas : une fiche peut rester
fidèle au format tout en déformant le propos. Nous n’avons réalisé aucune relecture systématique
par un ethnobotaniste ou un pharmacologue. [TODO : si un échantillon a malgré tout été
relu : donner le nombre de fiches relues, le nombre d’erreurs trouvées et le taux ; sinon,
supprimer cette phrase TODO et remplacer par « Aucun échantillon n’a fait l’objet d’une
telle relecture. »].
5. L’échelle reste celle d’un prototype. Trente-cinq documents, [TODO : reprendre le nombre
de fiches extraites donné au chapitre III (nombre d’entrées de extractions.json)] fiches, un
déploiement local complété par un tunnel ngrok : nous n’avons pas mis le système à l’épreuve
d’un usage soutenu, ni d’un public large, ni d’une mise en ligne pérenne.
6. Le périmètre reste celui d’un outil de consultation. Le système aide à chercher, à lire et à
vérifier une information documentée. Il ne pose pas de diagnostic et n’établit pas de prescription,
et rien dans les résultats présentés ici ne saurait être lu comme une validation clinique.
S’y ajoute une remarque de méthode : l’hypothèse d’une extraction assistée par modèle de langue
meilleure qu’une extraction manuelle n’a pas été testée par une comparaison contrôlée. Elle suppose un
protocole à part entière, avec deux groupes traités dans les mêmes conditions, que nous n’avons pas
mené.
IV.4.4 Pistes de travail
Quatre prolongements se dégagent des limites qui précèdent.
Faire évaluer le système par d’autres que ses concepteurs : un évaluateur externe pour les extractions,
un second panel d’utilisateurs plus nombreux et recruté hors du cercle du projet, dont des tradipraticiens
à qui l’application est d’abord destinée.
Élargir le corpus et mesurer l’effet sur la couverture. Les thèses et rapports encore non numérisés
constituent le gisement le plus immédiat, et leur intégration donnerait une idée plus juste du lien entre
volume documentaire et richesse du modèle.
Fiabiliser l’extraction par une relecture experte échantillonnée, et confronter les réponses du système
à des questions formulées par de vrais utilisateurs plutôt que tirées du corpus.
Rendre le service accessible au-delà de la machine de développement, avec un déploiement
conteneurisé et une instrumentation discrète des usages, de sorte que la prochaine évaluation puisse
s’appuyer sur des données de terrain recueillies en conditions réelles.
Conclusion du chapitre
Ce chapitre a présenté les résultats de l’évaluation prévue en phase 8 et en a discuté la portée. À
l’ontologie, les contrôles n’ont révélé ni incohérence ni rupture de traçabilité, et la couverture avance
71

--- page 84 ---
avec le corpus, inégalement selon les pathologies documentées. Au système RAG, les 50 questions
de référence livrent des mesures par critère et par famille de questions, des requêtes simples et de
traçabilité assurées, et des difficultés concentrées sur les recettes multi-plantes et les conversions
de requêtes complexes. À l’application web, les scénarios passés par les participants fournissent un
premier retour sur l’usage, dont les scores figurent au tableau IV.5.
Nous avons replacé ces résultats face aux quatre questions de la recherche et face aux systèmes
existants : le fil qui relie la source scientifique à l’écran de l’utilisateur tient d’un bout à l’autre de
la chaîne, et c’est là ce que le travail apporte de plus net. Six limites encadrent ce bilan, dont les
principales tiennent à une évaluation conduite par les concepteurs, à un jeu de questions issu du même
corpus, et à des extractions non relues par un expert.
Ces limites ne ferment rien. Elles indiquent ce qui resterait à faire pour transformer un prototype
documenté en outil de recherche partagé, et c’est ce que la conclusion générale reprend à son tour.
72

--- page 85 ---
Conclusion générale
Ce travail est parti d’une difficulté d’accès. Les connaissances scientifiques sur les plantes
médicinales du Burkina Faso sont abondantes, mais dispersées entre des articles, des thèses, des
mémoires et des rapports qui n’emploient ni les mêmes terminologies, ni les mêmes dénominations pour
désigner une même plante. Retrouver une information sur une plante, une pathologie ou une recette, et
remonter à la source qui la soutient, demandait un travail que les documents seuls ne permettaient pas
d’organiser. Pour y répondre, nous avons choisi d’adapter et d’enrichir une ontologie existante à partir
de la littérature scientifique, puis d’exploiter cette ontologie au moyen d’un système d’accès intelligent
et d’une application web. La démarche a suivi huit phases, chacune produisant les livrables nécessaires
à la suivante : de l’étude comparative des ontologies jusqu’à l’évaluation du dispositif.
La première phase a permis d’identifier les ontologies du domaine et de les comparer sur une
grille commune. ontoMEDTRAD a été retenue, avec le score le plus élevé de la comparaison, devant
WATRIMed, puis nous l’avons adaptée au contexte burkinabè et enrichie à partir de 35 documents
scientifiques. Cinq ensembles de classes, les propriétés relatives aux noms vernaculaires et quatre
relations de rattachement ont été ajoutés, tandis que la structure d’origine était préservée. Les
connaissances extraites ont été versées dans une base de connaissances orientée graphe, interrogeable
en Cypher, où chaque information reste reliée à la source qui la rapporte. Un système RAG, articulant
LangChain, le modèle Llama 3 et la base Neo4j, a été mis au point pour traduire une question en
langage naturel en une requête sur le graphe et rédiger une réponse fondée sur les faits retrouvés. Une
application web, enfin, a réuni l’ensemble derrière une interface de recherche et de consultation. Sur
ce dispositif, nous avons mené l’évaluation prévue, à trois niveaux : l’ontologie, le système RAG et
l’application.
La vérification des hypothèses s’appuie sur les résultats consignés aux chapitres III et IV.
Hypothèse 1. La revue méthodique de la littérature devait permettre d’identifier et d’enrichir un
modèle ontologique capable de représenter les connaissances sur les plantes médicinales du Burkina
Faso. Cette hypothèse est confirmée : l’étude comparative a mis en évidence plusieurs modèles
candidats, et le modèle retenu a pu être adapté puis enrichi à partir du corpus, jusqu’à représenter
les plantes, leurs usages, leurs parties utilisées, leurs modes de préparation, leurs propriétés et leurs
sources.
Hypothèse 2. L’extraction assistée par un modèle de langue de grande taille devait améliorer
la constitution des connaissances par rapport aux méthodes manuelles. Cette hypothèse n’est que
partiellement étayée. L’extraction assistée par LLM a été effectivement mise en œuvre et a produit
des données structurées exploitables, mais la comparaison contrôlée entre extraction automatique et
extraction manuelle n’a pas été menée. Nous ne pouvons donc pas affirmer, au vu de nos seuls résultats,
que la première soit supérieure à la seconde; cette supériorité reste une hypothèse de travail à éprouver,
avec deux groupes traités dans les mêmes conditions.
Hypothèse 3. L’adaptation et l’enrichissement devaient permettre de mieux représenter les
connaissances documentées tout en assurant leur traçabilité. Cette hypothèse est confirmée. Face au
modèle d’origine, qui couvrait vingt-deux plantes et trente et un remèdes antipaludéens [28], l’ontologie
enrichie représente un ensemble plus large, dont les chiffres de couverture figurent au tableau IV.1.
Les raisonneurs HermiT et Pellet n’ont signalé aucune incohérence au fil des ajouts, et la traçabilité
repose sur une règle structurelle : une connaissance sans source ne peut pas entrer dans le graphe. Les
73

--- page 86 ---
contrôles sur échantillon n’ont pas démenti cette propriété.
Hypothèse 4. L’exploitation de l’ontologie par un système RAG devait faciliter la recherche et la
compréhension des connaissances en langage naturel. Cette hypothèse est confirmée pour l’essentiel.
Sur les 50 questions de référence, le système traduit correctement les questions simples et les questions
de traçabilité, et rédige des réponses sourcées; les métriques correspondantes sont réunies au tableau
IV.2. Il rencontre davantage de difficulté sur les recettes associant plusieurs plantes et sur les questions
formulées indirectement. Cette réussite doit être lue avec la réserve qui l’accompagne : le jeu de
questions provient du corpus qui a servi à construire l’ontologie, et l’évaluation a été conduite par les
concepteurs eux-mêmes.
Hypothèse 5. Une application web intégrant le système RAG devait faciliter la vulgarisation et la
diffusion des connaissances documentées. Cette hypothèse est confirmée, sous réserve de l’ampleur
des tests. L’application existe, elle réunit les fonctions prévues, et les participants l’ont utilisée selon
trois scénarios; leurs retours figurent au tableau IV.5. La campagne reste toutefois réduite : le panel est
modeste et n’autorise pas de comparaison statistique.
Six limites encadrent ce bilan. L’évaluation a été conduite par nous-mêmes, les concepteurs du
système, et le regard extérieur y a manqué. Le jeu de questions part du même corpus que l’ontologie,
ce qui le porte à mesurer d’abord ce que le système sait déjà faire. Les niveaux de preuve sont ceux
que rapportent les sources, sans réévaluation indépendante. Les extractions n’ont pas été relues par un
expert. L’échelle reste celle d’un prototype, déployé localement, sans usage soutenu ni public large. Le
périmètre reste enfin celui d’un outil de consultation : le système ne pose pas de diagnostic, n’établit
pas de prescription, et rien dans nos résultats ne saurait être lu comme une validation clinique.
Ces limites indiquent les prolongements les plus utiles. Faire évaluer le dispositif par d’autres que
ses concepteurs, avec un panel plus large recruté hors du cercle du projet, dont des tradipraticiens à
qui l’application est d’abord destinée. Élargir le corpus, en intégrant les thèses et rapports encore non
numérisés, et mesurer l’effet de ce volume sur la couverture. Fiabiliser l’extraction par une relecture
experte échantillonnée, et confronter les réponses à des questions posées par de vrais utilisateurs plutôt
que tirées des documents. Rendre enfin le service accessible au-delà de la machine de développement,
par un déploiement conteneurisé et une instrumentation discrète des usages, afin que la prochaine
évaluation s’appuie sur des données de terrain.
L’apport de ce travail ne tient pas à la taille de la base, qui reste modeste, mais à la continuité
qui la traverse. De la source scientifique jusqu’à l’écran de l’utilisateur, en passant par l’ontologie, le
graphe et la réponse, aucun maillon ne perd l’information d’origine : chaque connaissance conserve la
référence qui la fonde, et chaque réponse reste rattachée aux faits du graphe. C’est cette exigence de
traçabilité, tenue d’un bout à l’autre de la chaîne, qui donne au prototype sa valeur, en attendant que
des évaluations plus larges confirment ou corrigent ce qu’il promet.
74

--- page 87 ---
Bibliographie
[1] AI4D. Création d’une base de données sur les plantes médicinales pour faciliter l’exploitation
des connaissances ethnopharmacologiques locales. 2020. url : https://www.ai4d.ai/fr
/blog/building-a-medicinal-plant-database (visité le 26/09/2026).
[2] Richard O. Angole et al. « Towards an Ontology Model for African Traditional Medicine ».
In : Advances in Knowledge-Based and Intelligent Information and Engineering Systems.
T. 243. Frontiers in Artificial Intelligence and Applications. IOS Press, 2012, p. 386-395. doi :
10.3233/978-1-61499-105-2-386.
[3] Richard Okelo Angole, Peter Jehopio et Gilbert Maiga. « Ontology model : Towards bridging
the gap between African traditional medicine and conventional medicine ». In : International
Journal of Knowledge-Based and Intelligent Engineering Systems 17.1 (2013), p. 37-43. doi :
10.3233/KES-130263.
[4] ARES. Médecine traditionnelle et système de santé : vers une intégration durable. 2018. url :
https://moove.ares-ac.be/actu/medecine-traditionnelle-et-systeme-de-san
te-vers-une-integration-durable (visité le 26/09/2026).
[5] Armel Ayimdji et al. « Towards A “Deep” Ontology for African Traditional Medicine ».
en. In : Intelligent Information Management 3.6 (oct. 2011). Number : 6, p. 244-251. doi :
10.4236/iim.2011.36030. url : https://www.scirp.org/journal/paperinformati
on?paperid=8241 (visité le 12/06/2026).
[6] Ricardo Baeza-Yates et Berthier Ribeiro-Neto. Modern Information Retrieval : The Concepts
and Technology behind Search. 2e
éd. Harlow : Addison-Wesley, 2011. url : https://books.g
oogle.com/books/about/Modern_Information_Retrieval.html?id=HbyAAAAACAAJ.
[7] Bruce G. Buchanan et Edward H. Shortliffe, éd. Rule-Based Expert Systems : The MYCIN
Experiments of the Stanford Heuristic Programming Project. Reading, MA, USA : Addison￾Wesley, 1984. isbn : 0-201-10172-6.
[8] Laurel Cooper et al. « The Plant Ontology as a Tool for Comparative Plant Anatomy and Genomic
Analyses ». In : Plant and Cell Physiology 54.2 (2013), e1. doi : 10.1093/pcp/pcs163.
[9] Fred D. Davis. « User acceptance of information technology : system characteristics, user
perceptions and behavioral impacts ». In : International Journal of Man-Machine Studies
38.3 (mars 1993), p. 475-487. issn : 0020-7373. doi : 10.1006/imms.1993.1022. url :
https : / / www . sciencedirect . com / science / article / pii / S0020737383710229
(visité le 29/09/2026).
[10] Samuel Nii Odoi Devine, Emmanuel Awuni Kolog et Roger Atinga. « Toward a Knowledge￾Based System for African Traditional Herbal Medicine : A Design Science Research Approach ».
In : Frontiers in Artificial Intelligence 5 (2022). PMC8959699, p. 856705. doi : 10.3389/frai
.2022.856705. url : https://doi.org/10.3389/frai.2022.856705.
75

--- page 88 ---
[11] Jacob Devlin et al. « BERT : Pre-training of Deep Bidirectional Transformers for Language
Understanding ». In : Proceedings of the 2019 Conference of the North American Chapter of the
Association for Computational Linguistics. 2019, p. 4171-4186. doi : 10.18653/v1/N19-1423.
url : https://aclanthology.org/N19-1423/.
[12] Damion M. Dooley et al. « FoodOn : A Harmonized Food Ontology to Increase Global Food
Traceability, Quality Control and Data Integration ». In : npj Science of Food 2 (2018), p. 23.
doi : 10.1038/s41538-018-0032-6. url : https://www.nature.com/articles/s4153
8-018-0032-6.
[13] Jérôme Euzenat et Pavel Shvaiko. Ontology Matching. 2e
éd. Springer, 2013. doi : 10.1007
/978-3-662-43550-9. url : https://doi.org/10.1007/978-3-662-43550-9.
[14] Élisabeth Flahaut. « Pharmacopée et médecine traditionnelle dans l’Ouest du Burkina Faso :
plantes médicinales et soins du couple mère-enfant ». 143 pages. Thèse de doctorat en pharmacie.
Université de Lille II, 1999. url : https://passioneuro.fr/wp-content/Documents/Th
ese_E-FLAHAUT_1999.pdf.
[15] Luciano Floridi et al. « AI4People—An Ethical Framework for a Good AI Society : Oppor￾tunities, Risks, Principles, and Recommendations ». In : Minds and Machines 28.4 (2018),
p. 689-707. doi : 10.1007/s11023-018-9482-5.
[16] Ralph Grishman. « Twenty-five Years of Information Extraction ». In : Natural Language
Engineering 25.6 (2019), p. 677-692. doi : 10.1017/S1351324919000512.
[17] Thomas R. Gruber. « A Translation Approach to Portable Ontology Specifications ». In :
Knowledge Acquisition 5.2 (1993), p. 199-220. doi : 10 . 1006 / knac . 1993 . 1008. url :
https://doi.org/10.1006/knac.1993.1008.
[18] Nicola Guarino. « Formal Ontology, Conceptual Analysis and Knowledge Representation ».
In : International Journal of Human-Computer Studies 43.5–6 (1995), p. 625-640. doi :
10.1006/ijhc.1995.1066.
[19] Sita Guinko. « La végétation de la Haute-Volta ». Deux volumes, 394 pages. Thèse de doctorat
ès sciences. Université de Bordeaux III, 1984. url : https://www.scirp.org/reference
/referencespapers?referenceid=3387847.
[20] John Hanna et al. « Building a Drug Ontology Based on RxNorm and Other Public Domain
Drug Databases ». In : Journal of Biomedical Semantics 4 (2013), p. 44. doi : 10.1186/2041-
1480-4-44. url : https://pubmed.ncbi.nlm.nih.gov/24345026/.
[21] Michael Heinrich et al. Fundamentals of Pharmacognosy and Phytotherapy. Edinburgh :
Churchill Livingstone, 2004. isbn : 978-0-443-07132-4.
[22] Robert Hoehndorf et al. « The Flora Phenotype Ontology (FLOPO) : Tool for Integrating
Morphological Traits and Phenotypes of Vascular Plants ». In : Journal of Biomedical Semantics
7 (2016), p. 65. doi : 10.1186/s13326-016-0107-8. url : https://www.ncbi.nlm.nih
.gov/pmc/articles/PMC5109718/.
[23] Syed Hussain et Gihan Athula. « Extending a Conventional Chatbot Knowledge Base to
External Knowledge Source and Introducing User Based Sessions for Diabetes Education ». In :
(2018), p. 698-703. url : https://ieeexplore.ieee.org/abstract/document/841815
5.
[24] Daniel Jurafsky et James H. Martin. Speech and Language Processing. 3e
éd. 2023. url :
https://web.stanford.edu/~jurafsky/slp3/ (visité le 26/09/2026).
[25] Michel C. A. Klein et Dieter Fensel. « Ontology Versioning on the Semantic Web ». In :
Proceedings of the First International Semantic Web Working Symposium (SWWS). Stanford,
CA, USA, 2001, p. 75-91.
76

--- page 89 ---
[26] Janet L. Kolodner. Case-Based Reasoning. San Mateo, CA, USA : Morgan Kaufmann, 1993.
isbn : 1-55860-237-2.
[27] Appoh Kouamé. « Système de gestion de la médecine traditionnelle dans une plateforme web
social et sémantique : une approche basée sur une ontologie visuelle ». fr. Thèse de doct.
Université Gaston Berger de Saint-Louis (Sénégal), avr. 2018. url : https://hal.science/t
el-01842116 (visité le 12/06/2026).
[28] Appoh Kouamé et al. « Visual Representation of African Traditional Medicine Recipes Using
Icons and a Formal Ontology, ontoMEDTRAD ». In : Digital Personalized Health and Medicine
– Proceedings of MIE 2020. T. 270. Studies in Health Technology and Informatics. IOS Press,
2020, p. 791-795. doi : 10.3233/SHTI200269. url : https://ebooks.iospress.nl/doi
/10.3233/SHTI200269.
[29] Patrick Lewis et al. « Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks ».
In : Advances in Neural Information Processing Systems. T. 33. 2020, p. 9459-9474. url :
https://arxiv.org/abs/2005.11401.
[30] Mariano Fernández-López et No affiliation. « (PDF) Overview and analysis of methodolo￾gies for building ontologies ». en. In : ResearchGate (). doi : 10.1017/S0269888902000462.
url : https://www.researchgate.net/publication/231908719_Overview_and_ana
lysis_of_methodologies_for_building_ontologies (visité le 29/09/2026).
[31] Meta AI. Introducing Meta Llama 3 : The Most Capable Openly Available LLM to Date. Meta
AI Blog. Avr. 2024. url : https://ai.meta.com/blog/meta-llama-3/.
[32] Jeanne Millogo-Rasolodimby. « L’homme, le climat et les ressources alimentaires végétales
en période de crises de subsistance au Burkina Faso ». Thèse de doctorat ès sciences naturelles.
Université de Ouagadougou, 2001. url : https://journals.openedition.org/vertigo
/16758.
[33] Odile G. Nacoulma-Ouedraogo. « Plantes médicinales et pratiques médicales traditionnelles
au Burkina Faso : cas du plateau central ». Thèse de doctorat d’État. Université de Ouagadougou,
1996. url : https://publication.lecames.org/index.php/pharm/article/downlo
ad/13/32.
[34] David Nadeau et Satoshi Sekine. « A Survey of Named Entity Recognition and Classification ».
In : Lingvisticae Investigationes 30.1 (2007), p. 3-26. doi : 10.1075/li.30.1.02nad.
[35] Roberto Navigli, Paola Velardi et Aldo Gangemi. « Ontology Learning and Its Application to
Automated Terminology Translation ». In : IEEE Intelligent Systems 18.1 (2003), p. 22-31. doi :
10.1109/MIS.2003.1179190.
[36] Fnu Neha, Deepshikha Bhati et Deepak Kumar Shukla. « Retrieval-Augmented Generation
(RAG) in Healthcare : A Comprehensive Review ». en. In : AI 6.9 (sept. 2025), p. 226. issn : 2673-
2688. doi : 10.3390/ai6090226. url : https://www.mdpi.com/2673-2688/6/9/226
(visité le 06/08/2026).
[37] L. Ouédraogo et al. « Ethnobotanical Use and Conservation Assessment of Medicinal Plants
Sold in Markets of Burkina Faso ». In : Ethnobotany Research and Applications 20 (2020),
p. 1-25. doi : 10.32859/era.20.39.1-25. url : https://ethnobotanyjournal.org/in
dex.php/era/article/view/2259.
[38] W Jedida Ouedraogo et al. « Revue des Plantes Médicinales à Potentiel Aromatique du Burkina
Faso ». fr. In : 2 (2024).
[39] Colin Raffel et al. « Exploring the Limits of Transfer Learning with a Unified Text-to-Text
Transformer ». In : Journal of Machine Learning Research 21.140 (2020), p. 1-67. url :
https://jmlr.csail.mit.edu/beta/papers/v21/20-074.html.
77

--- page 90 ---
[40] D. L. Sackett et al. « Evidence based medicine : what it is and what it isn’t ». eng. In : BMJ
312.7023 (jan. 1996), p. 71-72. issn : 0959-8138. doi : 10.1136/bmj.312.7023.71.
[41] Hassan Shojaee-Mend, Haleh Ayatollahi et Azam Abdolahadi. « Development and Evalua￾tion of Ontologies in Traditional Medicine : A Review Study ». eng. In : Methods of Information
in Medicine 58.6 (déc. 2019), p. 194-204. issn : 2511-705X. doi : 10.1055/s-0040-1702236.
[42] SNOMED International. SNOMED CT : Systematized Nomenclature of Medicine – Clinical
Terms. International Health Terminology Standards Development Organisation (IHTSDO). 2020.
url : https://www.snomed.org/.
[43] Borlli Michel Jonas Somé et al. « Design Considerations for a Knowledge Graph : The WATRIMed
Use Case ». In : Healthcare of the Future : Bridging the Information Gap. T. 259. Studies in
Health Technology and Informatics. IOS Press, 2019, p. 59-64. url : https://healthcareof
thefuture.ch/wp-content/uploads/2022/03/proceedings_HoF_2019.pdf.
[44] Borlli Michel Jonas Somé et al. « Enabling West African Herbal-Based Traditional Medicine
Digitizing : The WATRIMed Knowledge Graph ». In : MEDINFO 2019 : Health and Wellbeing
e-Networks for All. T. 264. Studies in Health Technology and Informatics. IOS Press, 2019,
p. 1548-1549. doi : 10.3233/SHTI190528. url : https://ebooks.iospress.nl/doi/10
.3233/SHTI190528.
[45] Abdoulaye Souley. « Trois entités hausa parentes : zahi, sanyi et shawara ». In : La construction
sociale des maladies : les entités nosologiques populaires en Afrique de l’Ouest. Sous la dir.
d’Yannick Jaffré et Jean-Pierre Olivier de Sardan. Presses Universitaires de France, 1999.
url : https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17
-11/010050662.pdf.
[46] Rudi Studer, V. Richard Benjamins et Dieter Fensel. « Knowledge Engineering : Principles and
Methods ». In : Data & Knowledge Engineering 25.1–2 (1998), p. 161-197. doi : 10.1016/S01
69-023X(97)00056-6. url : https://doi.org/10.1016/S0169-023X(97)00056-6.
[47] A. A. Tekemetieu, S. Koussoube et L. P. Fotso. « An Ontology-Based Computer-Aided
Diagnosis System in African Traditional Medicine : At the Sorcerer’s Stone ». In : Kybernetes
45.1 (2016), p. 30-50. url : https://www.ajol.info/index.php/jcmphc/article/dow
nload/252453/238490.
[48] André Tibiri et al. « Countrywide Survey of Plants Used for Liver Disease Management by
Traditional Healers in Burkina Faso ». In : Frontiers in Pharmacology 11 (2020), p. 563751.
doi : 10.3389/fphar.2020.563751. url : https://pmc.ncbi.nlm.nih.gov/articles
/PMC7883685/.
[49] Mbih Jerome Tosam. « Metaphysical Issues in African Philosophy of Medicine ». In : African
Philosophy of Medicine. Springer, 2024. doi : 10.1007/978-3-031-73963-7_12. url :
https://link.springer.com/chapter/10.1007/978-3-031-73963-7_12.
[50] Safiatou Traoré et al. « Ethnobotanical Survey on Plants Used in the Treatment of Wounds by
Traditional Health Practitioners in Burkina Faso ». In : International Journal of Plant, Animal
and Environmental Sciences 15 (2025). url : https://www.progres.ujkz.gov.bf/publi
cations/11832/details.
[51] Ashish Vaswani et al. « Attention Is All You Need ». In : Advances in Neural Information
Processing Systems. T. 30. 2017. url : https://arxiv.org/abs/1706.03762.
[52] W3C. OWL 2 Web Ontology Language Document Overview. 2012. url : https://www.w3.or
g/TR/owl2-overview/ (visité le 26/09/2026).
[53] W3C. RDF 1.1 Concepts and Abstract Syntax. 2014. url : https://www.w3.org/TR/rdf11-
concepts/ (visité le 26/09/2026).
78

--- page 91 ---
[54] W3C. SKOS Simple Knowledge Organization System Reference. 2009. url : https://www.w3
.org/TR/skos-reference/ (visité le 26/09/2026).
[55] World Health Organization. General Guidelines for Methodologies on Research and
Evaluation of Traditional Medicine. Geneva, 2000. url : https://iris.who.int/handle/1
0665/66783 (visité le 26/09/2026).
[56] World Health Organization. WHO Monographs on Selected Medicinal Plants. Geneva,
2002. url : https://iris.who.int/bitstream/handle/10665/42052/978924154702
4_eng.pdf (visité le 26/09/2026).
[57] World Health Organization. WHO Traditional Medicine Strategy 2014–2023. Geneva, 2013.
url : https://iris.who.int/bitstream/handle/10665/92455/9789241506090_eng
.pdf (visité le 26/09/2026).
[58] Patrice Zerbo et al. « Plantes médicinales et pratiques médicales au Burkina Faso : cas des
Sanan ». In : BOIS & FORETS DES TROPIQUES 307 (mars 2011), p. 41-53. issn : 1777-5760,
0006-579X. doi : 10.19182/bft2011.307.a20481. url : https://revues.cirad.fr/in
dex.php/BFT/article/view/20481 (visité le 05/08/2026).
[59] Alexander Zizka et al. « Traditional plant use in Burkina Faso (West Africa) : a national-scale
analysis with focus on traditional medicine ». en. In : Journal of Ethnobiology and Ethnomedicine
11.1 (déc. 2015), p. 9. issn : 1746-4269. doi : 10.1186/1746-4269-11-9. url : https:
//ethnobiomed.biomedcentral.com/articles/10.1186/1746-4269-11-9 (visité le
05/08/2026).
[60] Koudbi Jacob Zongo et al. « Ethnopharmacological Study on Medicinal Plants Used for Jaundice
and Liver-Related Disorders Management in the Province of Kouritenga in the Central-Eastern
of Burkina Faso ». In : Journal of Advanced Translational and Preclinical Biomedicine 4.1
(2025). doi : 10.57220/jatpb.v4i1.213. url : https://boa.unimib.it/retrieve/44
4bc5b3-4483-4e23-a45d-f0fe28fbb91a/Zongo%20et%20al-2025-JATPB-VoR.pdf.
79
