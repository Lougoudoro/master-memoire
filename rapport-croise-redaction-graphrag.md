# Rapport croisé — rédaction du mémoire et implémentation GraphRAG

**Date de vérification :** 13 octobre 2026  
**Périmètre :** mémoire LaTeX dans `redaction/`, application et documentation dans `GraphRAG/`, corpus documentaire PDF dans `corpus/`.  
**Objet :** établir l’état réel de l’implémentation par rapport à ce qui est rédigé, identifier les écarts à corriger et proposer un ordre de finalisation. Ce rapport ne remplace pas l’évaluation scientifique du contenu des articles.

---

## 1. Synthèse exécutive

Le mémoire et l’application GraphRAG relèvent bien du **même projet de recherche** : structurer des connaissances publiées sur les plantes médicinales du Burkina Faso dans un graphe traçable, puis les rendre consultables en langage naturel par une application web.

Le workspace contient effectivement un corpus de **31 fichiers PDF** dans `corpus/`, une ontologie adaptée en Turtle dans `redaction/ontology/` et une application Streamlit modulaire dans `GraphRAG/application/`. Il serait donc inexact de conclure que le projet ne possède aucun corpus documentaire.

Une distinction essentielle demeure toutefois : **le code de l’application charge actuellement un jeu de démonstration synthétique**, et non les PDF de `corpus/`. Les trois CSV de démonstration contiennent quatre sources, douze plantes et quarante-cinq usages, tous identifiés comme données de démonstration (`est_demo=1`). Les PDF sont des documents sources disponibles pour le travail d’extraction, mais leur présence ne prouve ni qu’ils ont tous été sélectionnés selon les critères, ni que leurs connaissances ont été extraites, validées et chargées dans Neo4j.

Le mémoire présente en plusieurs endroits l’extraction réelle, le peuplement Neo4j et l’évaluation comme des travaux réalisés et comporte des résultats annoncés, alors que les scripts applicatifs et les CSV examinés montrent surtout un prototype de démonstration. Le chapitre IV conserve des marqueurs `\TODOchapo` pour les mesures qui permettraient de soutenir ces affirmations. **La priorité est donc d’aligner le récit sur les preuves disponibles, pas de remplacer les valeurs manquantes par des chiffres hypothétiques.**

### Repères vérifiés

| Élément | Constat établi dans les fichiers examinés |
|---|---|
| Corpus du workspace | 31 PDF dans `corpus/` (le mémoire annonce 35 documents scientifiques; écart à réconcilier) |
| Données chargées par l’application | `sources_demo.csv` : 4 lignes ; `plantes_demo.csv` : 12 ; `usages_demo.csv` : 45 |
| Provenance des CSV | Les 4 sources, 12 plantes et 45 usages portent `est_demo=1`; le README les qualifie de synthétiques |
| Extraction PDF → JSON/CSV | Aucun pipeline d’extraction des PDF vers les CSV de production n’a été identifié dans `GraphRAG/application/` |
| Ontologie | Fichier `redaction/ontology/ontoMEDTRAD-adapte.ttl` présent; le commentaire précise que les instances ne sont pas dans l’ontologie |
| Application | Huit écrans déclarés dans `application/app.py`; récupération déterministe principale et génération Cypher de repli |
| Tests automatisés | 124 réussis, 37 ignorés, 0 échec lors de l’exécution locale de la suite (2 avertissements de dépréciation Neo4j) |
| Chapitres III–IV | Les marqueurs de travail sont toujours présents, notamment pour les chiffres, extraits de code réels et résultats d’évaluation |

---

## 2. Périmètre et méthode de vérification

Les constats s’appuient sur la lecture des fichiers suivants :

- `redaction/README.md`, `redaction/rapport-etat-des-lieux.md`, `redaction/main.tex` ;
- `redaction/chapters/introduction.tex`, `chapter2.tex`, `chapter3.tex`, `chapter4.tex` et `conclusion.tex` ;
- `redaction/ontology/ontoMEDTRAD-adapte.ttl` ;
- `GraphRAG/README.md`, `GraphRAG/docs/01-diagnostic.md` et `GraphRAG/application/data/README.md` ;
- les modules `GraphRAG/application/rag/`, `database/`, `models/`, `app.py` et `tools_chargement.py` ;
- les CSV de démonstration et la suite de tests.

> **Limite de l’examen :** la vérification porte sur les fichiers présents dans le workspace. Elle n’a pas interrogé une instance Neo4j en direct, ni ouvert les 31 PDF un à un, ni validé leur admissibilité scientifique, leurs métadonnées ou leur contenu. Aucun résultat de base en production n’est affirmé ici.

---

## 3. État des ressources documentaires et des données

### 3.1 Le dossier `corpus/`

Le dossier contient **31 PDF**, d’après le comptage des fichiers `.pdf`. Le mémoire annonce un corpus de **35 rapports, articles, thèses et mémoires** (chapitre II, § II.1.1 et phase 3). L’écart constaté est donc de quatre documents, mais il ne permet pas à lui seul de conclure à une lacune : les quatre documents peuvent se trouver ailleurs, ou le nombre du mémoire peut être à actualiser. Il faut établir une liste de référence, avec un identifiant stable, un titre, des auteurs, l’année, le type, le chemin du PDF et le statut d’inclusion.

Le chapitre II mentionne aussi des données de l’Herbier National et de l’INERA. Aucun export de ces deux sources n’a été identifié dans les fichiers applicatifs examinés. Leur disponibilité, leur format et leur utilisation effective doivent être précisés avant de les présenter comme données intégrées.

### 3.2 Données intégrées à l’application

Les chemins de données déclarés dans le README et l’outil `application/tools_chargement.py` pointent vers les CSV `application/data/*_demo.csv`. Leur documentation précise explicitement que les usages, dosages, compositions et niveaux de preuve associés sont inventés pour la maquette et ne doivent pas servir à un usage scientifique ou médical. Les CSV confirment le marquage `est_demo=1` pour les quatre sources, les douze plantes et les quarante-cinq usages.

En conséquence, le prototype démontre le fonctionnement technique du schéma, des requêtes, de la visualisation, de l’interface et de la chaîne de génération. **Il ne constitue pas encore, dans l’état livré, la preuve d’un enrichissement du graphe avec les 31 PDF du corpus.** Les deux catégories de données doivent rester distinctes dans le mémoire et dans toute démonstration :

1. corpus documentaire réel : PDF scientifiques à sélectionner et analyser ;
2. jeu synthétique : données de démonstration explicitement marquées, utilisées pour tester le prototype.

---

## 4. Correspondance entre le mémoire et l’implémentation

| Sujet | Ce qu’annonce ou décrit le mémoire | Ce que montrent les fichiers GraphRAG | État / action éditoriale |
|---|---|---|---|
| Ontologie | ontoMEDTRAD est retenue, adaptée et enrichie ; les instances sont versées dans Neo4j, non dans l’OWL | Ontologie adaptée présente en Turtle; schéma applicatif Neo4j distinct, proposé à partir des chapitres du mémoire | Cohérence de principe, mais démontrer le mapping entre classes/propriétés Turtle et nœuds/relations réellement chargés |
| Extraction | Phase 5 décrit des prompts Llama 3 70B, Colab, sortie JSON puis CSV; chapitre III prévoit des extraits réels | Aucun extracteur PDF, notebook d’extraction ou export JSON/CSV réel n’a été trouvé dans `application/`; seuls les CSV de démo y alimentent le chargeur | Présenter l’extraction comme non intégrée/non démontrée tant que les artefacts réels ne sont pas fournis |
| Modèle de langage | Llama 3 70B via Ollama/Colab et ngrok pour le RAG (chap. II–III) | `application/models/llm.py` configure Google Gemini via `langchain-google-genai`, avec un modèle distinct possible pour les réponses et le Cypher | Écart majeur : mettre à jour le mémoire pour décrire le modèle réellement utilisé, ou documenter une version séparée fondée sur Llama si elle existe réellement |
| Récupération RAG | `GraphCypherQAChain` décrit comme chaîne centrale : question → Cypher → graphe → réponse | Chemin principal déterministe : détection d’entités et requêtes fixes; génération Cypher en solution de repli, validée en lecture seule | Décrire l’architecture actuelle, en différenciant chemin principal et repli; ne pas présenter `GraphCypherQAChain` comme composant applicatif s’il n’est pas utilisé |
| Graphe | Huit types de nœuds et sept relations annoncés au chapitre III | Le schéma applicatif déclare dix labels et dix types de relations, avec Usage et NiveauPreuve séparés | Réconcilier le tableau de correspondance et le schéma final; mentionner les extensions si elles sont intentionnelles |
| Traçabilité | Chaque connaissance devrait être liée à sa source et le niveau de preuve rapporté | Les prompts RAG citent des identifiants de sources et le modèle vérifie les IDs retournés; le jeu démo contient des sources fictives et badges de démo | Le mécanisme technique est présent dans le code, mais la qualité scientifique n’est pas validée par les données synthétiques |
| Interface | Le mémoire annonce une application Streamlit avec recherche, fiches, chatbot, sources et graphe | Huit vues déclarées : accueil, assistant, recherche, plantes, pathologies, graphe, sources, à propos | Fonctionnalités disponibles dans le code; les captures et essais avec données réelles restent à documenter |
| Sécurité | Le mémoire exige une réponse fidèle aux faits du graphe | La validation Cypher en lecture seule, l’absence de réponse générée sans résultat et le garde-fou contre sources inventées sont décrits dans le code | Point fort technique à documenter avec tests, sans le confondre avec une validation de l’exactitude des connaissances |
| Évaluation | Le chapitre IV décrit une évaluation d’ontologie, de 50 questions et d’utilisateurs et présente certaines phrases au passé | Le projet contient une suite de tests logiciels; aucun jeu d’évaluation des réponses ou questionnaire utilisateur n’a été identifié dans les fichiers examinés | Tests logiciels ≠ évaluation scientifique ou utilisateur; vérifier les traces et reformuler toute mesure non documentée |

### 4.1 Ontologie Turtle et schéma Neo4j

L’ontologie adaptée contient notamment les classes `UsageTherapeutique`, `SourceScientifique`, `NiveauDePreuve`, `RegionBF` et des propriétés de provenance. Le schéma de l’application emploie cependant des catégories différentes ou supplémentaires, notamment `Usage`, `NiveauPreuve`, `PartiePlante`, `ModePreparation`, `Substance` et `Propriete`, ainsi que les relations `UTILISEE_POUR`, `POUR_TRAITER`, `NIVEAU_PREUVE`, `PROVIENT_DE` et `CITEE_DANS`.

Cette différence peut correspondre à une **projection applicative** de l’ontologie dans Neo4j, plutôt qu’à une contradiction. Mais elle doit être explicitée et vérifiée formellement. Le mémoire ne doit pas dire que chaque nœud « correspond » directement à une classe si le mapping est en réalité plusieurs-à-un, simplifié ou augmenté.

### 4.2 Implémentation GraphRAG et choix du terme

Dans la version actuelle, le nom du dossier est GraphRAG et les données sont interrogées dans Neo4j. Le chemin principal du code est toutefois une récupération déterministe par détection d’entités et requêtes Cypher fixes; un modèle peut générer une requête seulement en repli. Le modèle Gemini rédige la réponse à partir du contexte récupéré. Il est donc plus rigoureux de décrire l’application comme un **RAG fondé sur un graphe de connaissances**, avec un chemin de récupération déterministe et un repli de génération Cypher, sauf si une définition plus spécifique de GraphRAG est justifiée dans le cadre théorique.

---

## 5. État de la rédaction et éléments manquants

Le rapport d’état des lieux antérieur indique que le mémoire compile en 91 pages et estime la rédaction à environ 80 %, tout en recensant 87 marqueurs `\TODOchapo` dans les chapitres. Le contrôle de contenu confirme que les marqueurs structurants restent présents dans les chapitres III et IV. Les pages liminaires `resume.tex` et `abstract.tex` sont vides au moment de la vérification.

### Priorités documentaires et scientifiques

1. **Inventaire des sources** : réconcilier les 31 PDF du dossier avec les 35 documents annoncés; identifier les doublons, PDF illisibles ou hors critères; distinguer corpus inclus, exclus et en attente.
2. **Extraction reproductible** : fournir le script/notebook utilisé, sa configuration non secrète, le prompt/version, le schéma JSON, les sorties réelles et une table de provenance PDF/page/section → assertion extraite.
3. **Validation des extractions** : définir le contrôle humain (idéalement un échantillon relu), les règles de déduplication et la gestion des champs absents, erreurs de format et assertions contradictoires.
4. **Chargement des données réelles** : créer un jeu de données distinct des CSV synthétiques, avec références bibliographiques vérifiées et liens source–usage; documenter la base de test utilisée et les comptages après import.
5. **Réconciliation technique** : choisir les faits exacts sur modèle (Gemini ou Llama), architecture RAG, mapping ontologie–Neo4j, versions et déploiement, puis mettre à jour les chapitres II–III en conséquence.
6. **Évaluation** : construire et archiver le jeu de questions/réponses de référence, définir le calcul des métriques, mesurer couverture et traçabilité, enregistrer les temps et décrire les essais utilisateurs réellement menés.
7. **Complétude éditoriale** : produire les figures et captures réelles, compléter les pages liminaires, revoir la conclusion selon les résultats, puis nettoyer bibliographie et marqueurs TODO.

### Affirmations à reformuler tant qu’elles ne sont pas prouvées

Dans les chapitres II–IV, les formulations au passé telles que « nous avons exécuté l’extraction sur chaque document », « nous avons chargé les fichiers CSV » et « nos mesures sur les 50 questions donnent… » doivent être conservées seulement si des traces reproductibles existent. Sinon, les remplacer temporairement par une formulation de prototype, de procédure prévue ou de résultat restant à obtenir. Les exemples chiffrés placés dans les instructions de TODO sont des exemples et ne sont pas des résultats.

---

## 6. Vérification logicielle effectuée

La suite `GraphRAG/venv/Scripts/python.exe -m pytest GraphRAG/application/tests -q` a été exécutée dans le workspace le 13 octobre 2026 :

- **124 tests réussis** ;
- **37 tests ignorés** (notamment tests dépendant d’une base ou de conditions externes) ;
- **0 échec** ;
- deux avertissements de dépréciation liés à la fermeture des pilotes Neo4j.

Ce résultat démontre que les tests logiciels automatisés présents réussissent dans cet environnement. Il ne démontre pas que la base réelle est peuplée avec le corpus PDF, que les réponses sont scientifiquement exactes, ni que l’évaluation utilisateur du chapitre IV a été conduite.

---

## 7. Plan de travail recommandé

### Étape 1 — Geler une source de vérité

Établir un inventaire des documents et une décision écrite sur le corpus retenu. Le chiffre 35 du mémoire ne doit pas être remplacé automatiquement par 31 : expliquer les quatre documents non présents ou corriger le périmètre en s’appuyant sur l’inventaire final.

### Étape 2 — Séparer démo et données de recherche

Conserver `*_demo.csv` étiquetés comme synthétiques pour les tests et la démonstration. Ajouter un jeu réel versionné séparément, ou un chemin de chargement distinct, après extraction et validation. Éviter de charger les CSV démo dans une base présentée comme résultats scientifiques.

### Étape 3 — Réconcilier l’architecture écrite

Mettre à jour le mémoire pour refléter le code actuellement livré : Gemini, Streamlit multipage/routage interne, récupération déterministe en première intention, génération Cypher en repli, validation lecture seule et citations d’identifiants de source. Si Llama 3, Colab, Ollama ou ngrok ont été réellement employés dans une autre expérimentation, distinguer précisément cette version de la version intégrée finale et fournir ses artefacts.

### Étape 4 — Vérifier le mapping ontologique

Documenter une table OWL/Turtle → labels/propriétés Neo4j, les simplifications, les propriétés transformées en nœuds, et le sens de chaque relation. Mettre à jour les tableaux du chapitre III à partir de ce schéma unique.

### Étape 5 — Produire les preuves d’extraction et d’évaluation

Archiver les extractions avec provenance, les résultats du chargement, les requêtes et leurs sorties, le protocole et les données de mesure. Ne calculer les métriques que sur une base et un jeu de référence décrits; si l’évaluation n’est pas terminée, présenter le chapitre IV comme protocole et état d’avancement, sans résultats fictifs.

### Étape 6 — Finaliser la rédaction

Rédiger résumé et abstract après stabilisation des résultats, réaliser les captures correspondantes à la version testée, supprimer les marqueurs TODO uniquement après résolution ou remplacement explicite par une limite, puis compiler et vérifier les renvois et références.

---

## 8. Conclusion

Le dossier `corpus/` confirme qu’un **fonds documentaire réel est disponible dans le workspace**. En parallèle, l’application GraphRAG fournie s’appuie explicitement sur un **jeu de données synthétique** pour sa démonstration, et aucun pipeline de transformation des PDF du corpus en données réelles Neo4j n’a été identifié dans l’application examinée. La formulation correcte n’est donc ni « le corpus n’existe pas », ni « le graphe est déjà enrichi par les PDF », mais : **les sources PDF sont présentes; l’extraction et l’intégration scientifiques restent à démontrer dans les artefacts de l’implémentation actuelle**.

Le prototype technique est structuré, doté de garde-fous et testé. Le principal travail restant est de relier, de manière vérifiable, les documents du corpus à des assertions extraites, à leur provenance dans le graphe et aux résultats d’évaluation, puis de faire correspondre exactement cette chaîne au récit des chapitres II à IV.

---

## Références de fichiers du workspace

- `redaction/README.md`
- `redaction/rapport-etat-des-lieux.md`
- `redaction/chapters/chapter2.tex` — corpus et méthode, phase 5 à 8
- `redaction/chapters/chapter3.tex` — ontologie, graphe, extraction, RAG et interface
- `redaction/chapters/chapter4.tex` — protocole et résultats attendus/à compléter
- `redaction/ontology/ontoMEDTRAD-adapte.ttl`
- `GraphRAG/README.md`
- `GraphRAG/docs/01-diagnostic.md`
- `GraphRAG/application/data/README.md`
- `GraphRAG/application/rag/retrieval.py`, `chain.py`, `prompts.py`
- `GraphRAG/application/database/schema.py`, `tools_chargement.py`
- `GraphRAG/application/models/llm.py`
- `corpus/` — documents PDF inventoriés
