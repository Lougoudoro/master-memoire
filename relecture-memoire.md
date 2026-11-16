# Relecture — mémoire complet (16/11/2026)

Relecture menée avec les skills `memoire-relecture`, `memoire-conventions` et `memoire-style`, sur l'état du dépôt après le commit `6d8db52` « apres corretion ». Le mémoire compile sans erreur ni référence indéfinie (98 pages).

## Verdict

Le mémoire est **sur le fond honnête et cohérent**. Les chiffres concordent partout, il ne reste aucun `\TODOchapo`, et les limites sont dites avec une rigueur rare : ne touchez pas à cette prudence. Il **n'est pas encore prêt pour le jury**, pour trois raisons principales :
1. le résultat phare, un F1 de 0,995, a été obtenu sur les questions qui ont servi à corriger le système ;
2. le dispositif expérimental est incomplet ;
3. il reste environ 230 alertes de style au regard de vos propres règles.

---

## Points bloquants

1. **Le jeu de test a servi à corriger le système.** [chapter4.tex:175](chapters/chapter4.tex:175) Le F1 passe de 0,728 à 0,995 après des corrections faites « en lisant ses échecs sur ces 50 questions ». Le mémoire le reconnaît, aux lignes 175, 265 et 295, ainsi que dans le résumé et la conclusion. Mais ce score mesure alors la capacité à réussir ces 50 questions, pas la fiabilité du système. Un jury y verra le point faible n° 1, et le résumé met ce chiffre en avant.
   → **Correction recommandée, à faire pendant l'implémentation.** Constituez un **jeu de questions nouvelles**, d'environ 20 à 30 questions, écrites de préférence par une autre personne, par exemple un camarade ou l'encadrant. Mesurez-le **une seule fois** avec la version finale, sans aucune correction ensuite. Présentez-le comme le jeu de test. Les 50 questions actuelles deviennent alors le « jeu de mise au point ». C'est la pratique standard de séparation entre mise au point et test, et elle renforcerait nettement le chapitre IV.
   → À défaut, reformulez le résumé et la conclusion pour présenter 0,728 comme la mesure initiale et 0,995 comme le score après mise au point, sans en faire le résultat principal.

2. **Le dispositif expérimental est incomplet.** C'est une exigence du canevas et de `memoire-conventions`. Le chapitre II donne la figure du dispositif, le GPU T4, les modèles et les versions des bibliothèques. Il manque :
   - la **machine locale**, où tournent Neo4j et Streamlit : processeur, mémoire vive et système. La commande `systeminfo` les affiche sous Windows ;
   - les versions de **Python** (`python --version`), de **Neo4j** (le tableau indique seulement « Desktop (locale) »), d'**Ollama** (`ollama --version`), de **Protégé** et d'**HermiT** (menu « À propos ») ;
   - la **mémoire du GPU** et la **quantification** de `llama3:8b`, que donne `ollama show llama3:8b` ;
   - les **dates d'utilisation** des API (gpt-6-luna, Claude Opus 5.5, gemini-3.5-flash-lite), puisque leurs versions évoluent.
   → Ajoutez une sous-section « Dispositif expérimental » au chapitre II, avec un tableau « composant, version ou caractéristique, rôle ». Elle ajoutera aussi une page bienvenue.

3. **Une définition n'est pas citée.** [chapter1.tex:23](chapters/chapter1.tex:23) « L'Union Internationale pour la Conservation de la Nature (UICN) adopte une perspective plus large… » Cette définition est attribuée à l'UICN mais n'a aucune `\cite`. C'est un risque de plagiat au sens strict.
   → Ajoutez la référence de l'UICN au `.bib` et citez-la. Si vous n'avez pas la source, supprimez le paragraphe.

4. **Il reste des formules typiques de l'IA**, interdites par vos règles.
   - [chapter1.tex:686](chapters/chapter1.tex:686) « Il s'inscrit dans une dynamique plus large de valorisation… » → par exemple « Il prolonge les travaux de valorisation de la pharmacopée menés par… », en nommant l'acteur.
   - [chapter1.tex:846](chapters/chapter1.tex:846) « Elle s'inscrira dans une démarche de valorisation et de préservation des savoirs locaux… » → c'est une phrase générique de conclusion. Remplacez-la par ce que l'étude apporte concrètement, ou supprimez-la, car la phrase précédente suffit.

5. **Les règles de style sont enfreintes à grande échelle** (détail plus bas). Ce sont vos exigences absolues, donc un point bloquant. Le travail est mécanique mais long.

## Points importants

6. **Le chapitre des résultats est le plus court.** Le script d'équilibre donne : introduction 7 pages, I 23, II 17, III 21, **IV 9**, **conclusion 1**. Le chapitre IV est à 0,51 fois la moyenne, et la conclusion fait une page pour 2 à 4 attendues.
   → Ces ajouts répondent aussi à d'autres points du rapport : le jeu de test indépendant (point 1), une analyse des erreurs par famille de questions avec exemples, et la confrontation explicite à chaque hypothèse. Pour la conclusion, développez le bilan action par action (corpus, comparaison, adaptation, extraction, peuplement, système RAG, application) et des perspectives concrètes.
   → Pour le chapitre I, des sections longues comme les représentations des connaissances ou le traitement du langage naturel peuvent être résumées ou passer en annexe.

7. **Les plateformes existantes ne sont pas nommées.** [chapter1.tex:794](chapters/chapter1.tex:794) Le canevas demande des « plateformes/outils existants avec forces et faiblesses ». La section décrit des *familles* (systèmes experts, systèmes à base de cas, chatbots médicaux, plateformes d'ontologies). Seul MYCIN est nommé, et il est hors domaine.
   → Ajoutez 2 à 4 outils réels liés aux plantes médicinales, par exemple des bases ethnobotaniques en ligne ou des portails de pharmacopée africaine que vous avez consultés. Donnez pour chacun ses forces et ses faiblesses, et intégrez-les au tableau de synthèse. Je ne cite pas de noms précis : à vous de choisir ceux que vous pouvez sourcer.

8. **L'ordre des pièces liminaires diffère du canevas.** [main.tex:86-93](main.tex:86) La table des matières vient après les listes et les sigles.
   → Déplacez `\tableofcontents` avant `\listoffigures`.

9. **Le décompte des limites est confus**, en deux endroits.
   - [chapter4.tex:279](chapters/chapter4.tex:279) annonce « Six limites » et en énumère bien six. Mais la ligne 295 annonce ensuite « Quatre réserves » et en donne cinq : justesse des faits, jeu servi à corriger, exemples couvrant les types, score aveugle aux phrases ajoutées, et document en OCR.
   - [conclusion.tex:13](chapters/conclusion.tex:13) annonce « Six limites », mais la phrase sur les niveaux de preuve fusionne deux limites, ce qui en fait lire cinq.
   → Corrigez « Quatre réserves » en « Cinq réserves », ou fusionnez deux phrases. Dans la conclusion, séparez la phrase sur les niveaux de preuve en deux, ou écrivez « Plusieurs limites ».

10. **L'introduction est au futur.** [introduction.tex](chapters/introduction.tex) compte 14 tournures au futur (« nous mettrons », « sera »…), alors que le travail est fait. C'était un point ouvert de `memoire-style`.
    → Je recommande le présent pour décrire l'étude et ses objectifs, en gardant le futur seulement pour l'annonce du plan. C'est à vous de décider.

11. **L'hypothèse 3 n'est pas vraiment réfutable.** « Une solution numérique… devrait faciliter l'accès » ne peut se vérifier sans test auprès des utilisateurs, et ce test n'a pas eu lieu. La conclusion le reconnaît (« partiellement étayée »).
    → Gardez-la, mais préparez la question du jury. Une reformulation mesurable serait par exemple « … permet de retrouver les faits documentés avec un F1 d'au moins 0,8 sur des questions nouvelles ». Ce n'est possible que si le point 1 est traité.

12. **Une phrase est obscure.** [chapter4.tex:144](chapters/chapter4.tex:144) « Pour la question Q45, la rédaction d'une page suivante cite deux plantes… » On ne comprend pas sans connaître le découpage en pages de la réponse.
    → Proposition : « La réponse à Q45 est rédigée en plusieurs parties. L'une d'elles cite deux plantes que la base ne rapporte pas au Kourittenga. »

## Améliorations

13. [chapter4.tex:263](chapters/chapter4.tex:263) dit « vérifiées manuellement avant le peuplement », tandis que la limite 4 (ligne 288) dit « seul le contrôle sur échantillon… a été réalisé ». Précisez en une phrase ce que couvrait la vérification manuelle, pour éviter qu'un jury y voie une contradiction.
14. Le [README.md](README.md) n'est plus à jour (11 octobre : « 48 blocs `\TODOchapo` restants »). Il n'est pas lu par le jury, mais il vous induira en erreur.
15. **Annexes** : aucune. Les 50 questions avec leur famille, les consignes des modèles et un extrait de l'ontologie y trouveraient leur place, et le chapitre IV s'en trouverait allégé.
16. [chapter3.tex:573](chapters/chapter3.tex:573) contient un chemin local, `application\app.py`, dans une commande. Décrivez le lancement au lieu de le montrer, ou placez-le en annexe.

---

## Contrôle automatique du style

Résultat de `verifier_style.py` :

| Fichier | Alertes | Phrases de plus de 30 mots | « : » dans la prose | Paragraphes avec trop de parenthèses |
|---|---|---|---|---|
| chapitre I | 54 | 34 | 18 | 24 |
| chapitre II | 42 | 29 | 13 | 10 |
| chapitre III | 36 | 18 | 18 | 5 |
| chapitre IV | 21 | 16 | 5 | 2 |
| introduction | 13 | 10 | 3 | 0 |
| conclusion | 10 | 7 | 3 | 0 |
| résumé, abstract, dédicace | 0 | 0 | 0 | 0 |
| remerciements | 1 | – | – | – |

Il faut y ajouter **2 formules de type IA** (point 4) et **1 fichier local** (point 16). Le chapitre IV est le plus propre et le chapitre I le plus chargé. Les phrases les plus longues se trouvent au [chapitre IV, ligne 45](chapters/chapter4.tex:45) (53 et 58 mots, sur le contrôle de l'échantillon de 30 usages) et à la [ligne 177](chapters/chapter4.tex:177) (47 mots).

**Ordre de traitement conseillé :** introduction et conclusion d'abord, car le jury les lit en premier, puis chapitre IV, chapitre I, chapitre II et chapitre III.

## Langue (regroupée)

- **Phrases à rallonge** coordonnées par « et » ou par des participes. Coupez au deuxième verbe principal.
- **« : » d'annonce** dans la prose, du type « … trois critères : X, Y et Z ». Remplacez par « … trois critères, X, Y et Z » ou par une liste.
- **Parenthèses d'exemples** comme « (plantes, parties, familles…) » ([chapter4.tex:89](chapters/chapter4.tex:89)). Intégrez les exemples dans la phrase ou gardez-en un seul.
- Pas de faute d'orthographe notable relevée dans les passages lus.

## Questions probables du jury

- **« Votre F1 de 0,995 n'est-il pas obtenu sur les questions qui ont servi à corriger le système ? »** Le mémoire le reconnaît, mais sans mesure indépendante, vous n'aurez pas de réponse solide. C'est le point 1.
- **« Pourquoi le F1 est-il passé de 0,728 à 0,995 ? Qu'avez-vous changé ? »** Les changements sont décrits au chapitre III : liaison des libellés, contrôle des valeurs, provenance, complétude, exemples. Préparez une réponse orale d'une minute.
- **« Dix documents sur 35, est-ce représentatif ? Comment les avez-vous choisis ? »** Vérifiez que le chapitre II justifie le choix des dix.
- **« L'extraction par modèle de langue est-elle fiable sans expert ? »** Vous avez le contrôle des 1 497 usages sur 1 501 et l'échantillon de 30 usages. Préparez aussi le chiffre d'erreurs de cet échantillon.
- **« Pourquoi Llama 3 8B, plus lent, et qui recopie des phrases de sa consigne ? »** Vous avez l'argument du modèle ouvert sur une instance contrôlée. Ajoutez la confidentialité et le coût nul.
- **« Les requêtes Cypher générées sont-elles sûres ? »** Elles sont validées en lecture seule. Sachez expliquer comment, en une phrase.
- **« Le système peut-il conseiller un patient ? »** Non, c'est un outil de consultation, comme le disent le résumé et la limite 6.
- **« Que feriez-vous avec trois mois de plus ? »** Les pistes de travail sont prêtes (ligne 302 du chapitre IV et conclusion).

## Travail restant

- **0 `\TODOchapo`** dans le mémoire.
- Cohérence des chiffres vérifiée : 35 documents, dix exploités, 92 classes, 6 877 individus, 289 plantes, 1 676 usages, 50 questions, 913 faits sur 915, F1 de 0,995 et 0,728 initial. Ces valeurs sont identiques dans le résumé, l'abstract, les chapitres II à IV et la conclusion.
- Résumé : 245 mots, abstract : 236 mots, tous deux dans la consigne de 150 à 250.
