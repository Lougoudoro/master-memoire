---
name: memoire-relecture
description: Relecture critique du mémoire de Master (OntoPlantMedBF) avec la grille d'un jury de l'IBAM. Utilise ce skill dès que l'utilisateur demande de relire, vérifier, corriger, évaluer, critiquer ou « préparer pour le jury » une section, un chapitre ou tout le mémoire, de chercher les incohérences ou les fautes, de vérifier que les chiffres concordent, ou d'anticiper les questions de la soutenance — même formulé simplement (« tu peux regarder mon chapitre IV ? », « est-ce que c'est prêt ? »).
---

# Relecture critique du mémoire

Le but est de dire à l'auteur, avant le jury, **ce qu'un examinateur exigeant relèverait**, classé par gravité, avec une correction proposée pour chaque point. Tu relis ; tu ne modifies les fichiers que si l'auteur le demande.

Appuie-toi sur `memoire-conventions` (ce que chaque partie doit contenir) et `memoire-style` (comment elle doit être écrite).

## Préparer la relecture

1. Lis entièrement la partie demandée, puis ce qui l'encadre : `parts/resume.tex` et `parts/abstract.tex`, `chapters/introduction.tex` (questions, objectifs, hypothèses), `chapters/conclusion.tex`, et `chapters/chapter4.tex` dès qu'un chiffre de résultat est en jeu. Une partie se juge par rapport aux promesses de l'introduction.
2. Consulte `rapport-croise-redaction-graphrag.md` et `rapport-etat-des-lieux.md` : ils listent des écarts déjà connus entre le récit et l'implémentation. Vérifie s'ils sont résolus plutôt que de les redécouvrir.
3. Pour vérifier une affirmation sur le système, regarde les preuves disponibles (ontologie dans `ontology/`, registres `.xlsx`, application `../GraphRAG/` si accessible). Une affirmation sans preuve est un point à signaler, pas à « corriger » par un chiffre plausible.

## Grille de lecture

Passe dans cet ordre, du plus grave au plus superficiel.

**A. Vérité et preuves**
- Chaque résultat annoncé est-il mesuré et visible au chapitre IV ? Le texte présente-t-il comme fait ce qui reste à faire (extraction, peuplement, évaluation utilisateurs) ?
- Chaque fait du domaine est-il cité ? Les clés `\cite` existent-elles dans `sanou-master.bib` ?
- Les conclusions dépassent-elles ce que les mesures montrent (ex. justesse scientifique alors que seule la restitution du graphe est mesurée) ?

**B. Cohérence interne**
- Les mêmes chiffres partout : résumé, abstract, introduction, chapitres II–IV, conclusion, README. Dresse un petit tableau *chiffre → valeur dans chaque fichier* (nombre de documents du corpus, documents exploités, classes, individus, plantes, usages, questions de test, F1, réponses conformes). Écart connu à vérifier : corpus annoncé à 35 documents contre 31 PDF dans `corpus/`.
- Chaque question de recherche reçoit une réponse, chaque hypothèse un statut (validée / partiellement / non) au chapitre IV et en conclusion.
- Les noms restent stables (OntoPlantMedBF, ontoMEDTRAD, Llama 3 8B…).

**C. Démarche scientifique** (attentes du jury et du modèle de l'encadrant)
- Hypothèses réfutables, objectifs évaluables.
- Revue de littérature critique, avec tableau de synthèse et positionnement explicite.
- Protocole d'évaluation défini au chapitre II avant les résultats ; référence de comparaison (baseline).
- Limites énoncées, notamment l'absence de validation par un expert du domaine et d'évaluation auprès d'utilisateurs.

**D. Conventions et structure** — d'abord le **canevas officiel** (`../memoire-conventions/references/canevas-officiel.md`) : chaque rubrique exigée est-elle présente ? Les écarts déjà connus y sont listés dans un tableau, vérifie s'ils sont corrigés. Pour une relecture d'un chapitre entier ou du mémoire, **mesure l'équilibre des chapitres** avec `python .claude/skills/memoire-conventions/scripts/equilibre_chapitres.py main.toc` (compile d'abord si `main.toc` est ancien) et reporte les écarts aux repères, avec des pistes de rééquilibrage sans remplissage. Ensuite, selon `memoire-conventions` : introduction et conclusion de chapitre, transition vers le chapitre suivant, résumé de 150 à 250 mots (compte-le), pièces liminaires complètes, sigles tous déclarés, figures et tableaux appelés dans le texte et sourcés.

**E. Travail restant** — compte les `\TODOchapo` et `TODO` de la partie (`grep -c`), et liste ceux qui bloquent une affirmation du texte.

**F. Exigences absolues de l'auteur** — lance `python .claude/skills/memoire-style/scripts/verifier_style.py <fichiers>` et reporte ses alertes. Il repère les phrases trop longues, les deux-points dans la prose, l'excès de parenthèses et les formules typiques de l'IA. Ajoute ce que le script ne voit pas à la lecture :
- **trace d'IA** : texte générique, symétrique, sans fait précis ;
- **risque de plagiat** : passage trop proche d'une source ou d'un mémoire modèle, définition non citée, traduction littérale.

Ces points sont **bloquants** dans le rapport. Pour les paragraphes longs, regroupe les alertes par type plutôt que de les lister toutes.

**G. Langue et typographie** — selon `memoire-style` : fautes, phrases trop longues, temps incohérents, superlatifs, typographie LaTeX. Regroupe les fautes répétitives au lieu de les lister une à une.

## Format du rapport

Écris le rapport dans la conversation (ou dans un fichier `relecture-<partie>.md` à la racine si l'auteur le demande ou si la partie est longue) :

```
# Relecture — <partie> (<date>)

## Verdict
<2-3 phrases : état général, prêt / pas prêt pour le jury, les 3 priorités>

## Points bloquants
1. <fichier:ligne> — <problème> → <correction proposée>

## Points importants
...

## Améliorations
...

## Contrôle automatique du style
<résultat de verifier_style.py : nombre d'alertes par type, lignes concernées>

## Langue (regroupée)
- <type de faute> : <exemples avec lignes> → <règle>

## Questions probables du jury
- <question> — <éléments de réponse disponibles dans le mémoire, ou ce qui manque>

## Travail restant
<nombre de \TODOchapo, ceux qui bloquent>
```

- **Bloquant** : faux, non prouvé, incohérent entre parties, ou absent alors qu'exigé. **Important** : affaiblit la démarche ou la lisibilité. **Amélioration** : mieux, mais acceptable en l'état.
- Cite toujours `fichier:ligne` et l'extrait court en cause, pour que l'auteur retrouve le passage.
- Une correction proposée respecte le style de l'auteur ; si elle exige une information que tu n'as pas (un chiffre, une source), dis-le au lieu de l'inventer.
- Reste juste : signale aussi ce qui est solide en une ligne dans le verdict, pour que l'auteur sache quoi ne pas toucher.

## Questions de soutenance à anticiper

Le jury interroge presque toujours sur : le choix de l'ontologie de départ et des critères de comparaison ; la représentativité du corpus (10 documents exploités sur 35) ; la fiabilité de l'extraction par modèle de langue sans relecture experte ; le choix de Llama 3 8B face à Gemini ; les refus à tort ; la sécurité des requêtes Cypher générées ; l'usage réel par des tradipraticiens ou chercheurs ; les risques sanitaires (l'outil ne pose pas de diagnostic) ; la suite du travail. Pour chacune, indique où le mémoire répond déjà et ce qu'il faudrait ajouter.
