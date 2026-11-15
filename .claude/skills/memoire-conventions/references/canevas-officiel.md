# Canevas officiel de structure d'un mémoire — V1.0 du 26/09/2024

Document de référence fourni par l'auteur (`CanevasType_MémoireMaster (1).docx`, dans `C:\Users\sloug\Downloads\Telegram Desktop\`, non versionné). C'est **la règle la plus forte** pour la structure. Restitution fidèle de son contenu, reformulée.

## Pièces liminaires (dans cet ordre)
En-tête ; page de garde ; dédicace ; remerciements ; résumé français ; résumé anglais ; table des matières ; liste des figures ; liste des tableaux ; liste des abréviations.

## Chapitre 1 : Introduction générale
1. **Contexte et motivation** : contexte, justification et motivation du thème.
2. **Problématique et/ou hypothèses** : problématique décrite clairement ; hypothèses ou questions de recherche expliquées et formulées clairement.
3. **Objectifs** : objectif général ; objectifs spécifiques détaillés et exhaustifs, qui feront l'objet du travail.
4. **Organisation ou plan du mémoire** : contenu synthétique de chaque chapitre.

## Chapitre 2 : Revue de littérature / État de l'art
1. **Concepts et théories** importants, dont la clarification est nécessaire pour comprendre le travail.
2. **Présentation des travaux existants** :
   - plateformes et outils existants liés au travail ;
   - leurs forces et leurs faiblesses ;
   - travaux de recherche (articles scientifiques) liés à la problématique ;
   - analyse ou discussion de leurs résultats, qui met en évidence leurs insuffisances et limites par rapport au travail ;
   - synthèse de l'état de l'art (discussion, forces, faiblesses).

## Chapitre 3 : Méthodologie
- Peut être divisé en plusieurs chapitres ; dans ce cas, **veiller à l'équilibre du nombre de pages** entre chapitres et adapter la numérotation.
- Décrire la démarche suivie pour résoudre le problème, **schématisée** si possible (algorigramme, diagramme, algorithme, architecture).
- Présenter clairement la solution et les contributions.
- C'est **la partie importante du travail** : décrire clairement chaque étape pour faire ressortir la pertinence des propositions.

## Chapitre 4 : Implémentation / Expérimentation / Évaluation de la solution
- Processus d'implémentation.
- Choix d'implémentation, décrits et justifiés.
- Environnement matériel et logiciel (dispositif expérimental).
- Données utilisées pour l'expérimentation.
- Présentation, analyse et interprétation des principaux résultats.

## Conclusion
- Bilan des principales actions réalisées.
- Perspectives.

## Bibliographie
Références bibliographiques utilisées dans le mémoire.

## Annexes
Annexe A1, A2, A3…

## Correspondance avec le mémoire OntoPlantMedBF (état au 2026-11-15)

| Canevas | Mémoire | Écart |
|---|---|---|
| Intro = Chapitre 1 numéroté | Introduction générale non numérotée, chapitres I à IV | Écart accepté : l'auteur garde l'introduction non numérotée (décision du 2026-11-15), à ne plus signaler |
| TdM → figures → tableaux → abréviations | figures → tableaux → sigles → TdM (`main.tex`) | Ordre à aligner sur le canevas |
| Plateformes/outils existants + forces/faiblesses | §1.4.2 « Systèmes intelligents d'accès aux connaissances » décrit des familles de systèmes | Vérifier qu'il nomme des plateformes concrètes |
| Méthodologie divisible | Chap. II + Chap. III | Conforme ; déséquilibre mesuré le 2026-11-15 : I = 23 p., II = 17, III = 21, IV = 9, conclusion = 1 p. (voir `scripts/equilibre_chapitres.py`) |
| Environnement matériel et logiciel | Chap. II, tableaux « Modèles de langage et modes d'accès », « Bibliothèques Python utilisées » et « Récapitulatif du matériel » (GPU T4 sur Colab) | Partiel : manquent la machine locale (processeur, mémoire, système), les versions de Python, Neo4j, Ollama, Protégé, la quantification et les paramètres de Llama 3 8B, la période d'usage des API |
| Annexes | Aucune | À envisager : questions d'évaluation, extraits d'ontologie, prompts |
