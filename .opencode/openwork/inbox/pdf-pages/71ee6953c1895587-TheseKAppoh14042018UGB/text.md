# TheseKAppoh14042018UGB.pdf

pages: 216
sha256: 71ee6953c189558763b18006be8a36bd7b0d0f83295349254c7ea06401e0c00f

--- page 1 ---
LANI LARIMA
UNIVERSITÉ GASTON BERGER DE SAINT-LOUIS (UGB)
ÉCOLE DOCTORALE
SCIENCES ET TECHNOLOGIES
Laboratoire d’Analyse Numérique et Informatique - LANI
T H È S E
pour obtenir le titre de
Docteur en Informatique
Présentée par
Appoh KOUAME
SYSTÈME DE GESTION DE LA MÉDECINE TRADITIONNELLE DANS UNE
PLATEFORME WEB SOCIAL ET SÉMANTIQUE : UNE APPROCHE BASÉE
SUR UNE ONTOLOGIE VISUELLE
Soutenue publiquement le 14 avril 2018
Sous la direction de M. Moussa LO et le co-encadrement de M. Jean Baptiste LAMY
JURY :
Président de jury : Cheikh Talibouya DIOP, Professeur titulaire, Université Gaston Berger de
Saint-Louis, Sénégal
Directeur de thèse : Moussa LO, Professeur titulaire, Université Gaston Berger de Saint-Louis, Sénégal
Co-encadrant : Jean Baptiste LAMY, Maître de conférences, HDR, Université Paris 13, Bobigny,
France
Rapporteur : Engelbert MEPHU NGUIFO, Professeur titulaire, Université Clermont-Ferrand
Auvergne, France
Rapporteur : Mouhamadou THIAM, Maître de conférences, Université de Thiès, Sénégal
Rapporteur : Lina Fatima SOUALMIA, Maître de conférences, HDR, Université de Rouen, France
Examinateur : Michel BABRI, Professeur titulaire, Institut National Polytechnique F. Houphouet
Boigny de Yamoussoukro, Côte d’Ivoire
Examinateur : Konan Marcellin BROU, Maître de conférences, Institut National Polytechnique F.
Houphouet Boigny de Yamoussoukro, Côte d’Ivoire.

--- page 2 ---
Dédicaces
A mes feus Parents DATTE K. et DAKROME A. A ;
A mes Aïeux ;
A toute la famille ;
A l’ÊTRE de qui tout est, à l’origine de tout, de la pensée.

--- page 3 ---
Épigraphies
– Above all, humanity (mankind) is the very first need of the world.
– La centralité sur l’espèce humaine, sa persistance, sa préservation et sa pérennisation, tel est le but
de la somme des intelligences émanant des hommes, de toute action anthropique (adresse, technicité
et science).
– Lorsqu’il s’agit d’un art sauveur (salvateur) de la vie, négliger d’apprendre est un crime surtout pour
un faiseur ou pratiquant de santé. Samuel Hahnemann (1755-1843).
– Inférence :
Dans le monde, on n’a pas que des faits objets. On a encore un autre type de "faits" en termes
d’implications ou de glissements (entailments en anglais). Le pourquoi des choses et ce qu’elles
engendrent : moteur de l’évolution (et de développement). Un lien inné inébranlable existe toujours
entre trois choses : abduction, déduction et induction. "Déduction valide" est une règle d’inférence
au sens d’Aristote pour contrer les sophistes devenus moins sages (sophiste détourné de son sens
originel).
– Aucune communication n’est possible sans une iconicité minimale préférable à image. Peirce C S.

--- page 4 ---
Remerciements
Je tiens à remercier en premier lieu, Prof. Moussa LO, recteur de l’Université Virtuelle de Sénégal
(UVS), pour la confiance qu’il a placée en moi et de l’opportunité qu’il m’a offerte de faire cette thèse.
Pendant l’encadrement, ses sages conseils m’ont beaucoup appris. Je lui suis amplement reconnaissant et
ce de façon distinguée.
Je remercie Prof. Jean Baptiste LAMY pour m’avoir encadré. Il a fait montre de sa disponibilité
que ce soit durant mes deux séjours au Limics (Laboratoire d’Informatique Médicale et d’Ingénierie des
Connaissances en e-Santé) à l’Université Paris 13 de Bobigny (France), lors de son premier séjour au
Sénégal ou à distance de Yamoussoukro, d’Abidjan et de Saint-Louis avec Paris. Il a été à l’écoute de
mes questionnements nombreux. Il s’est très vite intéressé à l’avancement de mes travaux. Sa compétence,
sa rigueur scientifique, sa clairvoyance, son esprit éclairé, ses conseils et encouragements, et surtout ses
appoints m’ont suffisamment appris. Il est pour beaucoup dans le résultat final de cette thèse. Il m’a formé
dans ce travail de chercheur où il m’a donné de l’assurance et la confiance en soi, une autonomie certaine.
Je lui témoigne ma gratitude.
Je remercie Dr. Gaoussou CAMARA (Université de Bambey, Sénégal) pour ses conseils, son esprit
de secoureur, sa rigueur scientifique et son soutien indéfectible dont il a fait preuve dans les moments
difficiles. Merci Gaoussou.
Je tiens à remercier le jury scientifique, qui me fait l’honneur d’avoir examiné et rapporté ces travaux
de recherche consignés dans ce manuscrit. Je remercie également tous les membres du jury d’avoir accepté
d’assister à la présentation de ce travail.
Je remercie les responsables de l’Agence Universitaire de la Francophonie (AUF) à Dakar pour la prise
en charge en partie de mes deux premiers déplacements au Sénégal de quatre (4) mois pour séjours de
mobilité de recherche. En particulier, je remercie Mme Fabar SANE de l’AUF pour son soutien tout au
long de ces séjours à l’UGB de Saint-Louis.
Je remercie le Ministère de l’enseignement supérieur et de la recherche scientifique de Côte d’Ivoire et
l’Ambassade de France en Côte d’Ivoire, à travers l’Appui à la modernisation et à la réforme des Universités
et Grandes écoles de Côte d’Ivoire (AMRUGE-CI) / C2D 2015, au compte duquel j’ai été admis à une
bourse pour un séjour de recherche de deux mois à Paris.
Je remercie la Direction Générale de l’Institut National Polytechnique Félix Houphouet-Boigny (INP￾HB) de Yamoussoukro, Côte d’Ivoire.
Je dis merci aux responsables du Centre d’Excellence Africain en Mathématiques, Informatique et
Technologie de l’Information et de la Communication (CEAMITIC) de l’UGB pour l’appui financier obtenu
en six mois de mobilité de recherche en vue de finaliser ma thèse de doctorat. Aussi dois-je noter que le
déplacement et le séjour des jurés ont été également pris en charge par ce centre.
Je remercie tous les enseignants chercheurs de Limics de l’Université Paris 13 et particulièrement Prof.
Sylvie DESPRES pour son soutien. Je peux compter sur sa rigueur dans l’analyse des problèmes et ses
très nombreuses connaissances. Je lui témoigne ma gratitude.

--- page 5 ---
Je remercie les Professeurs Cheikh Talibouya DIOP, Michel BABRI, Souleymane OUMTANAGA,
Konan Marcellin BROU pour leurs conseils et soutiens.
Je remercie les enseignants-chercheurs de l’Unité de formation et de recherche Sciences Appliquées et de
Technologie (UFR-SAT) de l’UGB de Saint-Louis et particulièrement Prof. Mamadou SY, Prof. Ousmane
THIARE et Prof. Aliou DIOP, Prof. M MBAYE, Dr. Fatou S KAMARA, Dr. F NDIAYE et les autres.
Je dis merci à Ibrahima NDIAYE des services financiers et à Baboucar NDOYE des services adminis￾tratifs de l’UFR-SAT, puis à Tayib FALL du CEAMITIC, tous de l’UGB, pour leur sympathie et bonne
cohabitation.
Merci à Dr. Sadouanouan MALO de l’Université Nazi Boni (UNB) de Bobo-dioulasso, Burkina Faso,
qui m’a apporté son soutien lors de son séjour à l’UGB par ses encouragements.
Je remercie Prof. O HILI et Prof. B YAO de l’INP-HB pour leurs conseils pleins de sagesse et d’en￾couragements.
Merci à l’endroit de mes deux collègues du programme projet "Plateforme web pour le partage des
connaissances communautaires ouest-africaines" porté par Prof. M LO, notamment, feu P Fary DIALLO
(Que son âme repose en paix), Dr. Yaya TRAORE (Université Ouagadougou 1 Prof. Joseph KI-Zerbo,
Burkina Faso) avec qui nous avons partagé des moments intéressants mais aussi les moins bons.
Mes remerciements s’adressent aux autres collègues D MBOUP, C BERE, Aly N NGOM, BABACAR,
OUSMANE pour leurs soutiens et leur enthousiasme à partager leur culture scientifique. Il en va de même
pour Dr. Guidedi KALADZAVI (from Maroua’s University in Cameroon).
Je remercie les acteurs du Programme National de Promotion de la Médecine Traditionnelle (PNPMT)
au Plateau (Abidjan) dont principalement le Directeur coordonnateur, Dr. Ehoulé KROA, médecin attaché
de recherche, pour leur facilitation.
Au Sénégal, je remercie les tradipraticiens, praticiens de la MT (PMT) de la région de Saint-Louis
et de Podor en passant par Richard Toll et Dagana pour leur collaboration et adhésion au projet. Parmi
eux, je salue notamment Alassane Oumar BA à Figo, Président des PMT du département de Podor et
Alassane SY à Saint-Louis. Merci.
Je remercie les PMT de Côte d’Ivoire à travers MM Assamoi KOUADIO à Abobo (commune d’Abidjan)
et Brahima KONE, Président de la FTSN-CI, pour leur collaboration.
Je remercie Dr. E V A GBODOSSOU de la Prometra à Dakar, Dr. D SEYE à l’hôpital régional de
la ville de Saint-Louis et Dr. A Dorothée ABOU à la Formation sanitaire urbaine du Plateau (Abidjan),
tous médecins, pour leurs conseils.
Je dis merci à Beugré M AMESSAN (Abidjan, Côte d’Ivoire) et à Mamadou P SAMBA (Saint-Louis,
Sénégal) dans leur rôle bien tenu de traducteur et d’aiguilleur lors des visites de terrain chez les PMT.
Mes remerciements s’adressent aux collègues enseignants du Département de formation et de recherche
Math-informatique (DFR-MI) de l’INP-HB, notamment K A TOURE, I LOKPO, B GOORE, N BLE,
T L TANOH, J LUE, R GNENESSIO, A L ASSALE, A BONZOU, M TAHA, K KOUAME, KIMOU,
KADJO, ...
Je remercie toute la famille à Abidjan, à Yamoussoukro, à Bondoukou, à Tanda, à Tiédio et partout
ailleurs (Canada, USA, ...).
Je remercie mes frères et sœurs, oncles et tantes, cousins et cousines, nièces et neveux.
A l’endroit de Adama APPOH, M ABO, M SOW, N NIASSA, M V THIAW, Rachel GORE, YTO,
Mémé API, A DIA, J AHOU et J AKA, je leur dis merci pour leurs soutiens.
Cette liste pourrait s’allonger et être décrite aussi canoniquement et de manière équivalente. Ainsi, à
tous ceux que je n’ai pas nommés, ce travail vient en témoignage de ma reconnaissance pour leurs peines
partagées et soutiens multiples.

--- page 6 ---
Avant-Propos
Une ontologie est une expression d’une "vision du monde" sous forme d’un réseau de concepts pour
les besoins d’un traitement automatique. Dans cette optique, Tom Gruber affirme : "une ontologie est une
spécification formelle explicite d’une conceptualisation". Cette définition a donné suite à une succession
d’autres par différents auteurs dans le monde informatique. Cette pensée s’inscrit dans une autre plus large
de l’ontologie considérée comme la partie de la philosophie qui a pour objet l’étude de l’être en tant que
être, celle qui étudie les propriétés générales de l’être au sens d’Aristote. Pour en arriver à un traitement
automatique, il est donc mis en évidence l’objet d’étude consistant en une description approfondie d’une
situation, de sorte à permettre à la machine d’atteindre une sémantique plus aboutie, nous éloignant du
bruit et du silence : la précision maximale sur fond d’intelligibilité sémantique par la machine à même de
nous éloigner des ambiguïtés du langage naturel et des erreurs à une échelle communautaire minimale. On
arrive depuis presque deux à trois décennies, à mettre ainsi en lumière le sens des objets décrits, intelligibles
à la machine. Du coup l’intercompréhension entre communautés d’agents humains et machines est devenue
une réalité.
A l’échelle du web, sous le vocable de web de données, le réseau des hyperliens entre pages web est
étendu par un réseau de liens entre données structurées via lequel des agents automatisés accèdent plus
intelligemment au sens, à la signification de ces données prises comme ressources. Ceci a valu le terme de
web sémantique par Tim BERNERS-LEE, co-inventeur du Web et Directeur du W3C.
En général, l’on décrit une réalité sémantiquement valide dans un domaine de discours. Alors, il en
résulte deux entités que sont le décrivant d’une part et d’autre part le décrit ou "individu ou instance".
Via une ontologie formelle intégrant un système de représentation de connaissances, ces deux entités sont
transposées en machine avec un niveau sémantique largement supérieur à celui qu’offre habituellement une
base de données relationnelle (ontologie légère). Ce sont donc les réseaux sémantiques et les frames qui
seront révolutionnés par les langages piliers de la compréhension de l’information par la machine. Parmi
ces langages fondamentaux comptent RDF/XML et OWL (une des logiques de description-LDs ou DLs).
Ce présent travail embrasse une innovation de taille portée sur la sémantique iconique ajoutée à la
précédente qui est terminologique. Ceci débouche bien entendu à un amorçage de langage iconique de
plantes médicinales, avec une esquisse de remède iconique pour la médecine traditionnelle (MT) africaine
de l’Afrique de l’ouest. Ce langage s’appuie sur une approche d’ontologie visuelle, une composante de
l’ontologie de domaine de la MT, ontoMEDTRAD. Avec pour support les TIC, cette contribution est le
socle du cadre collaboratif véritable pour les experts praticiens de la MT (PMT) en majorité ne sachant
ni lire ni écrire, tel que le propose SysMEDTRAD utilisant ontoMEDTRAD dans une contexture de
plateforme web social et sémantique. Dotés de cet outil, ces PMT sont affranchis des barrières linguistiques
(langues locales et officielles) dans la pratique de l’art médical traditionnel. De manière graduelle, au
terme d’une série de validations d’ontoMEDTRAD, il sera disponible une mémoire organisationnelle et
structurante des connaissances et expériences de la MT. Ainsi, la forte perte due au caractère fortement oral
de la transmission de ces connaissances devra connaître un frein certain. L’utilisation de sysMEDTRAD

--- page 7 ---
induit inévitablement une augmentation des offres de soins de santé primaires par la MT, en plus de
celles émanant de la médecine moderne (MM). Ce travail vient en renforcement de tout ce qui est fait en
matière de modernisation de la MT de l’Afrique de l’ouest particulièrement. Il s’agit en conséquence d’une
valorisation plus explicite de cette MT.
Dans ce domaine, les difficultés rencontrées et non les moindres, sont multiples (MT taboue et forte￾ment tacite, réticence des PMT). Cependant, elles ont pu être levées grandement. Des facilitations, grâce
aux programmes nationaux de promotion de la MT (e.g : PNPMT de Côte d’Ivoire), d’ONG de la MT
(e.g : Prometra au Sénégal), d’associations et fédérations de PMT ivoiriennes et sénégalaises, n’ont pas
fait défaut. En partie, des appuis académiques et/ou financiers relèvent de l’École doctorale "Sciences et
technologies" de l’UGB à Saint-Louis (Sénégal), des laboratoires de recherche LANI de l’UGB, du pro￾gramme AMRUGE-CI 2015 (C2D) et de LIMICS de l’Université Paris 13 (France), du CEAMITIC de
l’UGB et de l’AUF-Dakar. Bien évidemment, notre démarche a aussi compté.

--- page 8 ---
Résumé
La médecine traditionnelle (MT) africaine est vue comme un système complémentaire de santé à la médecine
moderne (MM). Elle a l’avantage d’être plus facile d’accès, moins coûteuse et plus adaptée aux spécificités locales. On
note dans la MT, l’absence de partage et de conservation des connaissances médicales : la majorité des praticiens
de la MT (PMT) parlent des langues locales non codifiées et beaucoup d’entre eux gardent leur savoir secret.
Pour faciliter la préservation de ces connaissances et la communication entre PMT, nous cherchons à concevoir
SysMEDTRAD, un système basé sur une ontologie de domaine de la MT et une ontologie d’approche visuelle
intégrant un langage iconique. Ce travail de recherche est porteur d’une solution innovante pour les PMT, non
seulement leur permettant de manière continue de contribuer à la modernisation et à la valorisation explicite
de cette médecine, mais également les dotant d’un outil pour pratiquer leur art de guérisseur. Plus précisément,
ce travail a porté sur la construction d’une ontologie de domaine dénommée ontoCONCEPT-Term entièrement
terminologique. Il inclut aussi un langage iconique amorcé permettant d’identifier les plantes médicinales. Les
recettes et les remèdes traditionnels ont une représentation diagrammatique. Ce langage devra s’étendre tout en
suivant le cadre d’une approche d’ontologie visuelle, ontoICONE. Cette ontologie visuelle permettra de transcender
les barrières liées à l’illettrisme, à l’oralité et aux multiples langues locales au nombre de 1127 d’Afrique de l’ouest,
où a lieu ce projet de partage de connaissances web communautaire. ontoICONE est en partie terminologique
et iconique. La partie terminologique est commune avec ontoCONCEPT-Term. ontoICONE et ontoCONCEPT￾Term forment ontoMEDTRAD. Pour construire notre ontologie, nous nous sommes inspirés des méthodologies de
construction d’ontologies notamment Diligent, NeOn et ontoInfoforScience. Nous avons combiné de multiples sources
d’informations et de connaissances, à savoir des rencontres répétées avec les PMT de différentes régions, des travaux
publiés en biosciences (MT, Ethnobotanique) couvrant la sous région ouest Africaine, des sites web, des ouvrages
livresques, l’observation (jardins botaniques visités), des structures nationales (PNPMT), des ONG (Prometra), des
associations et fédérations de PMT (Côte d’Ivoire, Sénégal). Nous avons identifié trois cas d’utilisation principaux :
identifier la maladie à partir des symptômes et signes du patient ; prescrire le remède (recettes abstraite et physique :
ingrédients et mode de préparation) ; préparer le remède et l’administrer au patient.
La richesse de la MT, son caractère tacite et tabou, et la complexité de la représentation visuelle, nous ont
conduit à adopter une approche de construction progressive s’appuyant sur les règles sémiologiques notamment la
similarité visuelle, l’association sémantique et la convention. Dans les ressources médicinales, les plantes représentent
plus de 60 % des traitements traditionnels de santé. Nous avons donc choisi d’amorcer l’iconisation par le concept de
Plante en concevant un langage iconique partant des propriétés morphologiques de la plante en s’appuyant sur des
sources botaniques. Nous avons rassemblé un jeu de données comprenant 22 plantes et 31 remèdes antipaludéens,
et nous avons vérifié que notre langage iconique permettait bien d’identifier ces 22 plantes, à l’aide d’un outil
logiciel d’apprentissage et de classification (Weka). Ce langage a été présenté aux PMT lors de la première étape de
validation. La prochaine se focalisera sur la validation définitive et globale de ontoMEDTRAD et surtout l’adoption
d’une véritable ontologie visuelle. Elle intègre aussi le déploiement de ontoMEDTRAD (ontoICONE) dans une
plateforme Wiki sémantique (via Virtuoso), afin de rendre opérationnel sysMEDTRAD. En perspectives, les T-Box
et A-box d’une ontologie formelle seront complétées par G-Box, une partie graphique comprenant icônes et leur
structure (ontoMEDTRAD). Aligner l’ontologie visuelle à d’autres existantes (MT et MM) et donner une stature
de référence régionale voire mondiale à cette ontologie de domaine de la MT africaine ne seront pas en reste.
Mots clés : médecine traditionnelle, Afrique de l’ouest, plantes médicinales, langage iconique, approche d’on￾tologie visuelle, icône, iconème, graphisme, santé, patient, praticien de la médecine traditionnelle, connaissance,
représentation des connaissances, ontologie, sémantique iconique, ontoMEDTRAD, sysMEDTRAD.
I

--- page 9 ---
Abstract
Traditional medicine (TM) is seen as a complementary health system to modern medicine (MM). This TM
has the advantage of being easier to access, cheaper and more adapted to local specificities. However, African TM
suffers from the lack of sharing and preservation of medical knowledge : the majority of practitioners speak local
languages. They use non-codified languages, and many of them keep their secret knowledge. To facilitate knowledge
preservation and communication between practitioners of TM (TMP) we aim at designing SysMEDTRAD, a system
based on a domain ontology of TM and a visual ontology integrating an iconic language. This research work
brings an innovative solution for practitioners of TM, not only to allow them to contribute continuously to the
modernization and the explicit improvement of this medicine, but also to equip them with a tool to practice
their healing art. More precisely, this work has focused on the construction of a domain ontology referred to as
ontoONCONCEPT-Term entirely terminological. It also includes an iconic language started on identifying medicinal
plants. Traditional recipes and remedies have a diagrammatic representation. This language will have to be extended
while following the princple drawn by a visual ontology approach, ontoICONE. Via this visual ontology, we can
trenscand the barriers related to illiteracy, orality and the many local languages to the number of 1127 in West
Africa, where this community web knowledge sharing project takes place. ontoICONE is partly terminological
and iconic. This terminological part is common with onCONCEPT-Term. Those two entities ontoICONE and
ontoCONCEPT-Term form ontoMEDTRAD. To build our ontology, we took inspiration from ontology construction
methodologies, especially Diligent, NeOn and ontoInfoforScience. We have combined multiple sources of information
and knowledge on TM, including repeated meetings with TMP in different regions, published works in biosciences
(TM, ethnobotanics) covering the West African sub-region, websites, books, observation in botanic gardens, national
structures of TM (PNPMT), NGOs (Prometra), associations and federations of TMP (Côte d’Ivoire, Sénégal). We
identified three main use cases : identifying the disease from the patient’s symptoms and signs ; prescribing the
remedy (determining the abstract and material recipes : its ingredients and how to prepare it) ; preparing the
remedy and administering it to the patient.
The richness of TM, its tacit and taboo nature, and the complexity of the visual representation, have led us to
adopt a progressive construction approach based on semiotic rules namely visual similarity, semantic association and
convention. In medicinal resources, plants represent more than 60% of TM’s treatments. We have therefore chosen
to initiate iconization with the Plant concept by designing an iconic language from the morphological properties
of the plant based on botanical sources. We have collected a dataset of 22 plants and 31 antimalarial remedies,
and we have verified that our iconic language allows us to identify these 22 plants, using an automatic learning
and classification tool (Weka). This iconic language was presented to TMP during a first validation step. The next
step will focus on the definitive and global validation of ontoMEDTRAD, and mostly the adoption of a real visual
ontology (ontoICONE). It also integrates the deployment of ontoMEDTRAD (ontoICONE) into a semantic wiki
platform, such as Virtuoso, in order to have sysMEDTRAD being operational. In perspectives, the T-Box and A￾box of a formal ontology will be completed by G-box, a graphic part including the icons and their structure
(ontoMEDTRAD). Align the visual ontology with existing ones (TM and MM) and give a regional and
worldwide reference stature to this domain ontology of African TM will not be left out.
Keywords : traditional medicine, West Africa, medicinal plants, iconic language, visual ontology ap￾proach, icon, iconem, graphic design, health, patient, traditional medicine practitioner, knowledge, know￾ledge representation, ontology, iconic semantic, ontoMEDTRAD, sysMEDTRAD.
II

--- page 10 ---
Liste des symboles
AEN African Ethnobotany Network
AMRUGE-CI Appui à la Modernisation et à la Réforme des Universités et Grandes Ecoles de
Côte d’Ivoire
BFO Basic formal ontology
CEAMITIC Centre d’excellence en Mathématiques, Informatique et TIC
CEDEAO Communauté Economique des Etats de l’Afrique de l’Ouest (ECOWAS en anglais)
CIM10 Classification internationale des maladies (ICD10 en anglais)
CNRTL Centre National de Ressources Textuelles et Lexicales de Nancy
France (http ://www.cnrtl.fr/definition (consulté en 2014))
CODESRIA Council for the Development of Social Science Research in Africa (Conseil pour le dévelop￾pement de la recherche en sciences sociales en Afrique)
DAML DARPA Agent Markup Language
DOLCE Descriptive Ontology for Linguistic and Cognitive Engineering
ECOWAS Economic Community of West African States
FMA Foundational Model of Anatomy
FOAF Friend of a friend
FTSN-CI Fédération des tradipraticiens de santé et naturothérapeutes de Côte d’Ivoire
GO Gene Ontology
GPRS General Packet Radio Service
ICD10 International classification diseases
IRD Institut de recherche pour le développement, ex ORSTOM
ISO International Standards Organization, International Organization for Standardization (en
français : Organisation internationale de normalisation)
LDs Logiques de description (en anglais, Description logics DLs)
MeSH Medical Subject Headings
MM Médecine Moderne, Médecine Concentionnelle
MOT Modélisation par Objet Typé
III

--- page 11 ---
MT Médedecine Traditionnelle (en anglais TM)
NCIT National Cancer Institute Thesaurus
OBO Open Biomedical Ontologies Foundary
OIL Ontology Interchange Language
OMS Organisation Mondiale de la Santé (en anglias WHO)
ORSTOM Office de la recherche scientifique et technique outre-mer,
OWL Web Ontology Language
PMT Praticien de la MT (en anglais TMP)
PNPMT Programme National de Promotion de la MT
PO Plant Ontology
PROMETRA Organisation non gourvernementale de promotion de la MT
PSO Plant Structure Ontology
RAE Réseau Africain d’Ethnobotanique (en anglais AEN)
RAMEAU Répertoire d’Autorité-Matière Encyclopédique et Alphabétique Unifié
RDF Resource Description Framework
RDFS RDF Schema
RTO Ressources Terminolgiques et ontologiques
SNOMED-CT Systematized Nomenclature of Medicine – Clinical Terms
SPARQL SPARQL Protocol and RDF Query Language
SUMO Suggested Upper Merged Ontology
SWRL Semantic Web Rule Language
TIC Technologies de l’Information et de la Communication
TM Traditional Medicine
TMP Traditional medicine practitioner
TO Trait Ontology
UML Unified Modeling Language
UNESCO United Nations Educational, Scientific and Cultural Organization (Organisation des Na￾tions Unies pour l’Education, la Science et la Culture ; Organe (démembrement) de l’Or￾ganisation des Nations Unies (ONU))
W3C World Wide Web Consortium
WHO World Health Organization
YAMATO Yet Another More Advanced Top-level Ontology
IV

--- page 12 ---
Liste des figures
1.1 Composantes basiques "ou fondationnelles" d’ontoMEDTRAD . . . . . . . . . . . . . . . 6
1.2 Correspondance sémantique entre termes/concepts et icônes/concepts . . . . . . . . . . . . 7
1.3 Architecture simplifiée de la plateforme web social et sémantique : cadre basique d’échange
et de partage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1 Processus de clarification de signes et de symptômes d’une maladie . . . . . . . . . . . . . 19
2.2 Déterminants ou facteurs de l’état de santé humain des plus englobants aux plus spécifiques 21
2.3 Grands courants de l’évolution de la médecine de l’humanité . . . . . . . . . . . . . . . . . 21
2.4 Quatre grandes époques marquantes de la médecine de l’humanité . . . . . . . . . . . . . 22
3.1 Sémantique et implication inférentielle sur énoncés en représentation des connaissances . . 40
3.2 Aperçu chronologique sur les outils et langages pivots conjointement utilisés pour la repré￾sentation des connaissances et ontologies . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.3 Niveaux de formalisation des langages et formes de représentation des connaissances : De
l’informel au formel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.4 Bloc fragmentaire constitué des Logiques de description de la logique des prédicats (LPO) 48
3.5 Racines RDF(S) des constructeurs de base pour OWL . . . . . . . . . . . . . . . . . . . . 55
3.6 Illustration des cinq (5) phases de la méthodologie Diligent [77] . . . . . . . . . . . . . . . 60
3.7 Illustration des étapes en 9 scénarios de NEON [53] . . . . . . . . . . . . . . . . . . . . . . 62
3.8 Reparcours des étapes pour l’atteinte d’un niveau de stabilité suffisant pour nos modèles 62
3.9 Illustration des 9 étapes de ontoForInfoScience [160] . . . . . . . . . . . . . . . . . . . . . 64
3.10 Icônes de VétoMed . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
3.11 Syntaxe de l’alphabet de base du langage iconique VCM . . . . . . . . . . . . . . . . . . . 73
4.1 Caractère persistant et inchangé de l’icône . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.2 Extraction d’un langage iconique pour les personnes handicapées aphasiques . . . . . . . . 81
4.3 Triangle sémiotique de base selon Peirce . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
4.4 Triangle sémiotique signifié-signifiant-référent de Peirce inspiré de [118] . . . . . . . . . . . 85
4.5 Isotype de Neurath (1882-1945), un exemple de symboles et de combinaison symbolique . 88
4.6 Structure générale de l’ontologie iconique de VCM . . . . . . . . . . . . . . . . . . . . . . 89
5.1 Vue synoptique et architecturale de sysMEDTRAD . . . . . . . . . . . . . . . . . . . . . . 94
5.2 Fond organisationnel des connaissances et des expériences continu de la MT pour les PMT 95
5.3 Cycle de vie de construction d’ontologies (prototype général) . . . . . . . . . . . . . . . . 97
5.4 Cycle de vie de construction d’ontologies (inspiré de Methontology) en phase avec Neon,
Diligent et OntoforInfoScience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
5.5 Schéma récapitulatif des étapes de construction pragmatique d’une ontologie . . . . . . . . 99
V

--- page 13 ---
5.6 Vues synoptiques succinctes de la spécification des besoins à l’implémentation de la solution
en machine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
5.7 Description algorithmique de l’UC1. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
5.8 Description algorithmique de la première partie de l’UC2 . . . . . . . . . . . . . . . . . . 110
5.9 Description algorithmique de la deuxième partie de l’UC2 . . . . . . . . . . . . . . . . . . 112
5.10 Description algorithmique de première partie de UC3 . . . . . . . . . . . . . . . . . . . . . 113
5.11 Description algorithmique de la deuxième partie de UC3 . . . . . . . . . . . . . . . . . . . 114
5.12 Concepts de la MT qui découlent de l’UC1 . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
5.13 Diagramme des classes (partie une) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
5.14 Principales classes et relations d’ontoMEDTRAD . . . . . . . . . . . . . . . . . . . . . . . 128
5.15 Liste des classes sous Protégé de ontoMEDTRAD . . . . . . . . . . . . . . . . . . . . . . . 130
5.16 Liste des classes avec le nombre d’individus ou d’instances par classe de ontoMEDTRAD . 131
5.17 Liste des propriétés de ontoMEDTRAD . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
5.18 Classes pour iconisation ontoMEDTRAD . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
5.19 Mise en relief des propriétés d’iconisation (Plante) . . . . . . . . . . . . . . . . . . . . . . 133
5.20 Copie écran montrant l’exécution d’Hermit et l’expressivité de ontoMEDTRAD . . . . . . 134
6.1 Impact du moment d’unité dans la reconnaissance d’une image iconique . . . . . . . . . . 144
6.2 13 critères attributs de description des 22 plantes . . . . . . . . . . . . . . . . . . . . . . . 146
6.3 Poids des attributs des plantes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
6.4 6 Critères candidats à l’élagage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
6.5 Paramétrage de JRIP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
6.6 Illustration de la classification à 100% des 22 espèces de plantes . . . . . . . . . . . . . . . 149
6.7 Mise en relief de la relation entre plante et les sept critères . . . . . . . . . . . . . . . . . 150
6.8 Relation de la Plante avec chacun des (7) sept critères . . . . . . . . . . . . . . . . . . . . 150
6.9 Les cinq iconèmes pour le critère silhouette . . . . . . . . . . . . . . . . . . . . . . . . . . 150
6.10 Exemple d’assemblage d’iconèmes pour l’icône d’une plante . . . . . . . . . . . . . . . . . 153
6.11 Icône de la plante Azadirachta indica A. Juss . . . . . . . . . . . . . . . . . . . . . . . . . 153
6.12 Extraction de ontoMedtrad montrant la classe Plante et les classes dérivées des critères pour
la représentation iconique des espèces de plantes médicinales . . . . . . . . . . . . . . . . . 155
6.13 Relations sémantiques entre Plante et les classes pour la représentation iconique . . . . . . 155
6.14 Code source en python pour la création des icônes des 22 espèces de plantes médicinales
antipaludiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
6.15 Relation ternaire entre Recette, Plante et Partie de plante . . . . . . . . . . . . . . . . . . 161
6.16 Modèle de recette exhaustif . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
6.17 Représentation diagrammatique de la recette . . . . . . . . . . . . . . . . . . . . . . . . . 161
6.18 Représentation formelle de la recette en vue de son iconisation . . . . . . . . . . . . . . . . 162
6.19 Esquisse d’icône de mTRecipe01 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
6.20 Représentation diagrammatique du remède succincte . . . . . . . . . . . . . . . . . . . . . 164
6.21 Représentation formelle du remède en vue de son iconisation . . . . . . . . . . . . . . . . . 164
6.22 Esquisse d’icône du remède rmd01 basé sur la recette mTRecipe01 . . . . . . . . . . . . . 166
6.23 Diagramme pour le langage iconique des remèdes et recettes . . . . . . . . . . . . . . . . . 166
6.24 Diagramme pour le langage iconique intégrant les maladies à partir des remèdes et recettes 168
6.25 Forme canonique répondant aux trois cas d’utilisation pour l’iconisation des recettes et
remèdes partant des Plantes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
VI

--- page 14 ---
6.26 Forme canonique répondant aux trois cas d’utilisation pour l’iconisation des recettes et
remèdes partant des Ressources Médicinales . . . . . . . . . . . . . . . . . . . . . . . . . . 171
VII

--- page 15 ---
Liste des tableaux
2.1 Exemple de nom botanique ou scientifique d’une plante selon Linné . . . . . . . . . . . . . 17
2.2 Comparaison des connaissances modernes et traditionnelles . . . . . . . . . . . . . . . . . 24
3.1 Quelques définitions des concepts donnée, information et connaissance par neuf (9) auteurs . . . . . . . 36
3.2 Typologie des connaissances . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.3 Exemple de syntaxe, sémantique et de raisonnement en LPO partant du pseudo langage
naturel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.4 Description de chacune des 5 étapes de Diligent . . . . . . . . . . . . . . . . . . . . . . . . 59
3.5 Description de chacune des 9 scénarii de Néon . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.6 Illustration des étapes en 9 scénarios de ontoForInfoScience . . . . . . . . . . . . . . . . . 63
3.7 SNAP et SPAN de BFO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
3.8 Propriétés d’une partie d’un objet suite à sa subdivision . . . . . . . . . . . . . . . . . . . 68
3.9 Traduction d’une phrase du langage naturel au langage iconique . . . . . . . . . . . . . . . 71
4.1 Exemples, d’images, de pictogrammes et d’icônes . . . . . . . . . . . . . . . . . . . . . . . 79
4.2 Exemples, d’images, de pictogrammes et d’icônes (suite et fin) . . . . . . . . . . . . . . . . 80
4.4 Types peircéens de signe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
4.5 Cinq (5) lois émanant de la Gestalt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
5.1 Cartographie des acteurs et utilisateurs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
5.2 Point d’ancrage pour de la construction de ontoMEDTRAD . . . . . . . . . . . . . . . . . . . . 100
5.3 Principe de contextualisation et de décontextualisation pour l’émergence des concepts/classes future 101
5.4 Principe de contextualisation et de décontextualisation pour l’émergence des concepts/classes future
(suite et fin du Tableau 5.3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
5.5 Concepts majeurs et concepts secondaires . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
5.6 Indication de sources (RTO et ontologies) de concepts utilisés dans ontoMEDTRAD . . . 121
5.7 Indication des sources (RTO et ontologies) pour les rôles et subsomptions utilisés dans ontoMEDTRAD122
5.8 Étude comparative de quelques outils éditeurs d’ontologies formelles . . . . . . . . . . . . 123
5.9 Quatre approches d’évaluation d’une ontologie (de domaine) . . . . . . . . . . . . . . . . . 124
5.10 Catalogue des 9 groupes d’erreurs courantes dans les ontologies . . . . . . . . . . . . . . . 125
5.11 Groupe 1 des erreurs relatives aux concepts . . . . . . . . . . . . . . . . . . . . . . . . . . 125
5.12 Groupe 2 des erreurs relatives aux concepts, relations et propriétés . . . . . . . . . . . . . 125
5.13 Groupe 3 des erreurs relatives aux relations . . . . . . . . . . . . . . . . . . . . . . . . . . 126
5.14 Groupe 4 des erreurs relatives aux propriétés . . . . . . . . . . . . . . . . . . . . . . . . . 126
5.15 Groupe 5 des erreurs d’ordre général . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
5.16 Groupe 6 des erreurs relatives aux concepts, relation, instances individuelles et valeurs . . 127
5.17 Groupe 7 des erreurs relatives aux instances individuelles et valeurs . . . . . . . . . . . . 127
VIII

--- page 16 ---
5.18 Groupe 8 des erreurs relatives aux axiomes . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
5.19 Groupe 9 des erreurs relatives à la définition de concepts équivalents . . . . . . . . . . . . 127
5.20 Classification des erreurs par cause . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
5.21 Liste des figures des copies d’écran sous Protégé du contenu en partie de ontoMEDTRAD . . . . 129
5.22 Métrique de ontoMEDTRAD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
6.1 Liste des 22 plantes anti-malaria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
6.2 Liste de trente un (31) remèdes traditionnels . . . . . . . . . . . . . . . . . . . . . . . . . . 141
6.3 Liste des critères . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
6.4 Liste des critères (suite) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
6.5 Différentes classifications des types de plantes selon deux botanistes . . . . . . . . . . . . . 145
6.6 Exemples d’iconèmes relatifs aux formes de feuille, de fruit et à la pennation . . . . . . . . 151
6.7 Cadre graphique rectangulaire subdivisé en régions spatiales pour la position des iconèmes
de Plante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
6.8 Correspondance des critères et des régions spatiales du cadre graphique et nombres d’ico￾nèmes par critère . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
6.9 Définition de six classes pour les sept critères . . . . . . . . . . . . . . . . . . . . . . . . . 154
6.10 État du caractère fonctionnel des object properties ou propriétés objet entre plante (do￾maine) et classe de critère (range) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
6.11 Quelques data properties relatives aux Plantes et à leur iconisation . . . . . . . . . . . . . 156
6.12 Les 22 icônes des 22 espèces de plantes antipaludiques . . . . . . . . . . . . . . . . . . . . 159
6.13 les 9 iconèmes des parties de plantes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
6.14 Relations sémantiques de la recette . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
6.15 Cadre graphique pour l’iconisation de la recette . . . . . . . . . . . . . . . . . . . . . . . . 162
6.16 Projection du cadre graphique pour l’iconisation d’une recette (R) à base de deux espèces
de plantes P1 et P2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
6.17 mTRecipe01 extrait de ontoMEDTRAD (ontoCONCEPT-Term) . . . . . . . . . . . . . . 163
6.18 Relations sémantiques du Remède et des classes associées. . . . . . . . . . . . . . . . . . . 165
6.19 Cadre graphique du remède . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
6.20 Récapitulatif des iconèmes appartenant à l’alphabet du langage iconique . . . . . . . . . . 172
IX

--- page 17 ---
Table des matières
1 Introduction générale 1
1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Contexte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Problématique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Objectifs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.5 Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.5.1 Idée maitresse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.5.1.1 Fondement de notre travail de recherche : ontoCONCEPT-Term et ontoI￾CONE de ontoMEDTRAD . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.5.1.2 Structure fondationnelle d’une ontologie d’approche visuelle . . . . . . . . 7
1.5.1.3 Plateforme web sémantique et social . . . . . . . . . . . . . . . . . . . . 7
1.5.2 Publications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.6 Plan de la thèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2 Médecine traditionnelle de l’Afrique de l’ouest et son état pour capitalisation (des
connaissances) 9
2.1 Analyse de la MT : Nécessité de capitaliser et de pérenniser les savoirs . . . . . . . . . . . 10
2.2 Définitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2.1 Médecine traditionnelle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2.2 Tradipraticien ou thérapeute traditionnel . . . . . . . . . . . . . . . . . . . . . . . 12
2.2.3 Ethnopharmacologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.2.4 Pharmacopée traditionnelle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.2.5 Ethnobotanique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.2.6 Phytothérapie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.2.6.1 Phytothérapie traditionnelle . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.2.6.2 Phytothérapie moderne (phytothérapie clinique) . . . . . . . . . . . . . . 15
2.2.7 Mise sur le marché des produits de la MT . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.8 Plante médicinale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.9 Partie utile de plante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.2.10 Recette . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.2.11 Remède . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.2.12 Signes et symptômes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.3 Fondement historique, origine et évolution de la MT . . . . . . . . . . . . . . . . . . . . . 20
2.3.1 Fondement de l’art médical traditionnel . . . . . . . . . . . . . . . . . . . . . . . . 20
2.3.2 Évolution de la médecine de l’humanité et courants de médecine en usage . . . . . 20
2.4 Traits caractéristiques de la MT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
X

--- page 18 ---
2.4.1 Comparaison des connaissances natives et occidentales . . . . . . . . . . . . . . . . 23
2.4.2 Caractéristiques propres à la MT . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.5 Organisations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.5.1 Acquisition et transmission des connaissances et savoirs de la MT . . . . . . . . . . 26
2.5.2 Ressources médicinales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.5.3 Récolte des ressources médicinales . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.5.4 Forces et faiblesses de la MT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.5.4.1 Forces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.5.4.2 Faiblesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.6 Prédisdisposition organisationnelle et solutionnelle de capitalisation des connaissances . . 31
2.7 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3 Représentation de connaissances et ontologies 34
3.1 De "donnée" à "connaissance" . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.1.1 Donnée . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.1.2 Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.1.3 Connaissance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.2 Représentation des connaissances . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.2.1 Vocabulaire contrôlé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.2.2 Taxonomies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.2.3 Thésaurus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.2.4 Logique propositionnelle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
3.2.5 Logique du premier ordre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
3.2.6 Graphes conceptuels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.2.7 Réseaux sémantiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.2.8 Modélisation par objet typé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
3.2.9 Logiques de description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
3.2.9.1 Syntaxe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
3.2.9.2 Interprétation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
3.2.9.3 Signature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
3.2.9.4 Fonction d’interprétation . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
3.2.10 RDF et Web sémantique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
3.2.11 Ontologies formelles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
3.2.11.1 Définition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
3.2.11.2 Types d’ontologies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.2.11.3 Langage OWL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.3 Construction d’une ontologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.3.1 Méthodologies de construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.3.1.1 Norme I3E 1074-1995 de développement d’application logicielle, appliquée
à la construction d’une ontologie . . . . . . . . . . . . . . . . . . . . . . . 56
3.3.1.2 Méthodologie Diligent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.3.1.3 Méthodologie NeOn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
3.3.1.4 Méthodologie ontoForInfoScience . . . . . . . . . . . . . . . . . . . . . . 60
3.3.2 Principes généraux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.3.2.1 Rejet de l’hypothèse du nom unique (UNA) . . . . . . . . . . . . . . . . . 63
XI

--- page 19 ---
3.3.2.2 Hypothèse du monde ouvert (OWA) . . . . . . . . . . . . . . . . . . . . . 65
3.3.2.3 Continuants et occurrents . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.3.2.4 Processus et évènements . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
3.3.2.5 Objets fluents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
3.3.2.6 Homéomères (noms non comptables) et anhoméomères (noms comptables) 67
3.3.3 Conclusion sur les méthodologies existantes . . . . . . . . . . . . . . . . . . . . . . 68
3.4 Représentation des connaissances et ontologies existantes dans des domaines connexes . . 69
3.4.1 Travaux relevant de la MT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
3.4.2 Travaux relevant de la MM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
3.5 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
4 Icône et Langage iconique 74
4.1 Importance de l’icône . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
4.2 Définition et constance de l’icône . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
4.2.1 Définition de l’icône . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.2.2 Définition d’un langage iconique . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.2.3 Constance de l’icône . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.2.4 Exemple d’icônes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.3 Icône et communauté . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.4 Étude et décomposition des icônes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.4.1 Sémiologie des icônes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.4.2 Triangle sémiotique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
4.4.3 Théorie de la Gestalt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
4.4.4 Propriétés des icônes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
4.5 Exemples de langages iconiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
4.6 Langages iconiques formalisés . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
4.7 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
5 OntoMEDTRAD : vers une ontologie de la médecine traditionnelle africaine 90
5.1 Présentation et architecture globale du système envisagé : sysMEDTRAD . . . . . . . . . 91
5.1.1 Cartographie globale des acteurs et des utilisateurs . . . . . . . . . . . . . . . . . 92
5.1.2 Quatre composants essentiels de SysMEDTRAD . . . . . . . . . . . . . . . . . . . 92
5.2 Notre méthodologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
5.3 Étapes de construction de notre ontologie . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
5.4 Spécifications des besoins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
5.4.1 MT : Besoins tactiques et stratégiques . . . . . . . . . . . . . . . . . . . . . . . . . 106
5.4.2 Besoins pragmatiques pour la construction de ontoMEDTRAD : Trois cas d’utilisa￾tion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
5.4.3 Description détaillée des cas d’utilisations . . . . . . . . . . . . . . . . . . . . . . . 108
5.4.3.1 Description de l’UC1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
5.4.3.2 Description de l’UC2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
5.4.3.3 Description de l’UC3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
5.5 Conceptualisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
5.5.1 Cinq règles d’or pour initier la conceptualisation de manière compatible avec Dili￾gent, NeOn et ontoForInfoScience . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
5.5.2 Acquisition de connaissances . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
XII

--- page 20 ---
5.5.3 Modélisation conceptuelle (UML) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
5.5.4 Diagramme UML des classes relativement à ontoCONCEPT-Term . . . . . . . . . 119
5.6 Concepts présents dans des ontologies ou ressources déjà existantes . . . . . . . . . . . . . 119
5.7 Formalisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
5.7.1 Choix de l’outil de modélisation ontologique . . . . . . . . . . . . . . . . . . . . . . 122
5.7.2 Typologies des erreurs dans les ontologies de fondement existantes . . . . . . . . . 122
5.7.2.1 Catalogue de 33 écueils communément rencontrés dans la construction des
ontologies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
5.7.2.2 Classification des erreurs par cause . . . . . . . . . . . . . . . . . . . . . . 128
5.7.3 Résultat : ontoCONCEPT-Term . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
5.8 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
6 Vers une ontologie visuelle : construction d’un langage iconique pour les plantes mé￾dicinales, les recettes et les remèdes 136
6.1 Position de ontoICONE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
6.2 Périmètre de notre travail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
6.3 Construction d’un langage iconique pour les plantes . . . . . . . . . . . . . . . . . . . . . . 138
6.3.1 Extraction d’un jeu de données (31 remèdes et 22 plantes) . . . . . . . . . . . . . . 138
6.3.2 Définition des critères . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
6.3.3 Définition des valeurs des critères . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
6.3.4 Sélection des critères . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
6.3.5 Dessin des iconèmes et choix des couleurs . . . . . . . . . . . . . . . . . . . . . . . 149
6.3.6 Assemblage des iconèmes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
6.4 Génération automatique des icônes de plantes à partir de l’ontologie ontoMEDTRAD (ontoCONCEPT￾Term) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
6.4.1 Lien ontologique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
6.4.2 Programme en python (attachement procédural) pour la génération des icônes de
plantes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
6.5 Remarque importante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
6.6 Iconisation de la recette et du remède . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
6.6.1 Parties utilisées de la plante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
6.6.2 Recette et Ingrédient . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
6.6.3 Remède . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
6.6.4 Langage diagrammatique pour les recettes et les remèdes . . . . . . . . . . . . . . . 165
6.7 Généralisation de l’iconisation des remèdes et recettes pour l’ensemble des maladies . . . . 167
6.8 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
6.9 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
7 Discussion, conclusion et perspective 173
7.1 Discussions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
7.1.1 Comparaison aux travaux de Kuicheu . . . . . . . . . . . . . . . . . . . . . . . . . 175
7.1.2 Comparaison aux travaux de Lamy . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
7.1.3 Icônes et photos réalistes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
7.2 Vers des ontologies iconiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
Bibliographie 178
XIII

--- page 21 ---
Chapitre 1
Introduction générale
Sommaire
1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Contexte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Problématique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Objectifs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.5 Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.6 Plan de la thèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1

--- page 22 ---
1.1 Introduction
Les connaissances actuelles peuvent se décomposer en connaissances traditionnelles locales d’une part
et en connaissances universellement et scientifiquement prouvées d’autres part. Les dernières, sont souvent
originaires du monde occidental ou orientées par celui-ci, et sur lesquelles actuellement, les recherches se
focalisent. Cependant, de plus en plus, des connaissances natives, endogènes et locales voire aborigènes
ou encore naturelles attirent l’attention des scientifiques [49] [139] [150] [244] [245]. En occurrence, la
biomimétique s’inspirant du mimétisme du vivant, est en éclosion. Elle vise à répondre à de nouvelles
perspectives et à de nouveaux besoins humains. En réalité, le capital naturel a toujours servi de levier
d’amorçage à la science 1
. En clair, ce capital n’a jamais fait défaut, mais dans un rôle apparaissant souvent
très passif : apport de "matières à moudre" à la science.
Dès l’aube de l’humanité, l’homme a appris à connaître les ressources naturelles, et notamment les
plantes, pour se nourrir, puis à en cerner les vertus thérapeutiques [10]. Ce volet thérapie concerne la
médecine. De la médecine hippocratique (d’Hippocrate à -5e
siècle) en passant par celle de Paracelse (+15e
siècle) [73], plusieurs médecines ont contribué à l’établissement de la médecine dite traditionnelle (MT).
Cette dernière, jusqu’à nos jours, continue de constituer un vivier important non négligeable [49] [51] [126]
[196], pour la médecine conventionnelle dont la médecine moderne (MM). Très présente de par ses progrès
scientifiques remarquables et ses retombées en terme d’offre de soins de santé, cette MM est actuellement
lancée dans une course vers les technologies de pointe. Relevons également qu’au fil du temps et selon les
espaces, la MT revêt une apparence de persistance et de transcendance. Loin de remplacer la MM, ou
d’être oblitérée par elle, elle ne donne aucune impression de disparaître. Le Président de l’ONG Prometra
(Dakar) dit au sujet de la MT : "Qu’elle ait existé jusqu’à maintenant, justifie son efficacité et tout l’intérêt
qu’il convient de lui porter" [133]. A l’initiative de l’OMS, avec l’avènement des soins de santé primaires
en 1978 [210] [240], lors de la Conférence internationale d’Alma-Ata (actuel Almaty au Kazakhstan), il
a été motivé l’intérêt d’intégrer la MT dans les systèmes de santé nationaux des pays du tiers monde,
suite au constat de la non couverture médicale de l’ensemble des couches des populations par l’offre de
la médecine conventionnelle. La MT constitue un patrimoine culturel pour les populations autochtones
qui la pratiquent depuis des lustres (des temps les plus reculés). L’ambition pour la MT est d’en faire un
système complémentaire de santé plutôt qu’un substitut des offres de soins issues de la MM. Elle n’a pas
non plus pour objectif de copier la MM.
Dans ce travail, notre contribution vise à favoriser l’augmentation du potentiel des soins de santé pri￾maires par la MT, pour les populations africaines et plus particulièrement celles de quinze (15) pays de
l’Afrique de l’ouest. De nombreuses cultures y foisonnent, incluant différentes aires linguistiques, diverses
sources ou ressources naturelles d’ordres végétal, minéral et animal. Il y a aussi une grande variabilité mor￾phologique pour une même espèce vivante (animale ou végétale) selon la région, l’habitat et/ou le climat.
Pour les acteurs de premier rang de la MT, il n’existe quasiment pas de cadre collaboratif (flexible). La
1.
http ://www.cnrtl.fr/definition/science (consulté en 2014) ; Selon CNRTL (Centre national de ressources textuelles et lexicales de
Nancy/France), par science, il faut entendre la somme de connaissances qu’un individu possède ou peut acquérir par l’étude, la réflexion
ou l’expérience ; Plus spécifiquement, c’est la connaissance approfondie des choses dans ce qu’elles sont ou encore celle des règles et des
techniques propres à une activité. En outre, de la même source, la science est l’ensemble structuré de connaissances qui se rapportent
à des faits obéissant à des lois objectives (ou considérés comme tels) et dont la mise au point exige systématisation et méthode. On a
les sciences dures formelles, axiomatiques, abstraites (mathématiques, informatique, statistiques, actuariat, ...), les sciences abstraites
et concrètes (biologie, physiques, ...) et les sciences dites non exactes notamment les humanités (anthropologie, sociologie, ...). D’autres
classifications existent.
2

--- page 23 ---
conception d’un tel cadre collaboratif passe nécessairement par la création d’un environnement approprié
et propice pour ces acteurs que sont précisément les praticiens de la MT (PMT).
Un tel environnement devrait s’appuyer sur les Technologies de l’Information et de la Communica￾tion (TIC), qui sont les outils de référence pour la valorisation de l’information. En clair, au sens de R.
Dieng [80], il s’agit de constituer un fond organisationnel de connaissances et d’expériences accumulées
durant plusieurs décennies voire des siècles, dans le domaine de la MT africaine. L’organisation de ces
connaissances nécessite une approche classificatoire ontologique afin de mieux les représenter dans une
compréhension commune à la communauté des PMT. Le monde bien qu’étant unique est décrit et très
souvent compris de façon multiple. Décrire ce monde de manière formelle peut être un préalable à la
compréhension consensuelle par les humains. Dans cette optique, en s’appuyant sur les technologies du
web sémantique [100] [151], l’intelligibilité sémantique de ce monde par la machine est rendue possible. Ce
cadre d’échanges sous forme de plateforme web vient alors faciliter la collaboration entre les PMT.
Comment allons-nous nous y prendre afin de permettre à ces guérisseurs de partager, de co-construire
et de co-enrichir cette plateforme quand plus de la moitié (65 %) [135] d’entre eux ne savent ni lire, ni
écrire dans les quatre (4) langues officielles (le français, l’anglais, l’espagnol et le portugais) ? En plus, cette
même majorité des PMT s’exprime dans des langues locales différentes et appartiennent à des cultures
aux us et coutumes variés.
Pour répondre à cette question, notre travail de recherche vise la Gestion de la MT dans une
plateforme web social et sémantique selon une approche basée sur une ontologie visuelle
(iconique). Cette approche associe des icônes aux principaux concepts de l’ontologie terminologique au
plan des utilisations.
En effet, il est indispensable de réfléchir à un langage non-textuel, et constant d’un pays à un autre, à
même de transcender le multilinguisme accentué et très caractéristique de cet espace régional. Ce multilin￾guisme est une barrière dans la communication entre personnes. Cette difficulté est d’importance variable
pour chacun des pays de cette sous région africaine. Par exemple, en Côte d’Ivoire, il n’y a pas de langue
qui s’impose parmi la soixantaine existante. Après le français, nous avons trois langues locales (Baoulé,
Bété et Dioula ) qui sont les plus utilisées. Au contraire, au Sénégal, le Wolof est une langue locale qui
tend à s’imposer (parlé), venant après le français (écrit). Selon le pays, les langues locales ont un nombre
variable se situant entre 2 et 80 en général, et jusqu’à 527 au Nigeria [148]. Leur nombre total est estimé
à 1127 pour l’ensemble de l’Afrique de l’ouest.
Nous projetons alors, à partir d’une ontologie de domaine de la MT de l’Afrique de l’ouest, baptisé
ontoMEDTRAD, de construire un langage iconique selon une approche d’ontologie visuelle. Ce langage
prend appui sur une partie d’ontoMEDTRAD qui est ontoICONE. Ce projet est ambitieux et sera réalisé
méthodiquement et en plusieurs étapes, le présent travail constituant la première étape.
1.2 Contexte
Nos travaux de thèse entrent dans le cadre du projet [232] "Mise en place d’une plateforme web social et
sémantique pour le partage des connaissances des communautés ouest-africaines" piloté par Prof. Moussa
LO 2
. Il s’agit d’amener ces communautés caractérisées par des activités socioculturelles et professionnelles,
à partager leurs connaissances au moyen d’outils parmi lesquels les technologies du web social et sémantique
sont présentes. Cette plateforme Web sémantique centrée sur une base de connaissances ontologique devra
s’étendre à ces différentes communautés des localités urbaines et rurales de la sous région ouest-africaine.
2. http ://www.unesco.org/new/fileadmin/MULTIMEDIA/HQ/ED/pdf/SenegalGastonBergerFR.pdf consulté en 2013
3

--- page 24 ---
Les moyens d’accès envisagés sont multiples, notamment via l’Internet par la téléphonie mobile.
Plus spécifiquement, comme déjà mentionnée, la communauté concernée dans le présent travail de
recherche est celle de la MT, où notre solution comprend une approche d’ontologie permettant l’utilisation
d’icônes. Ainsi, au moyen d’un langage iconique, l’ensemble des concepts terminologiques afférents à la MT
devront être iconisés sinon, l’être en grande partie. L’aspect visuel permettra au tradipraticien (ou PMT)
de s’affranchir des barrières linguistiques, dans l’exercice de son art de guérisseur. Les PMT, experts du
domaine de la MT et composant notre endogroupe, constituent un centre d’intérêt important à prendre
en compte à toutes les grandes étapes charnières du projet vu le caractère consensuel souhaité.
L’importance et l’urgence de ce travail ne sont plus à démontrer : depuis plusieurs années, l’hégémonie
de la MM laisse peu de place à l’expression des MT et à l’utilisation naturelle des plantes médicinales.
Ces pratiques ancestrales sont désormais menacées de disparition. Cet état de fait est aggravé par la
mondialisation (économie mondiale) qui déstructure de plus en plus les populations des pays en voie de
développement (PED) et conduit à un bouleversement global des valeurs et des ressources. Les jeunes
générations se tournent alors désormais de plus en plus vers les valeurs occidentales, délaissent celles de
leurs aînés et notamment celles portées par la MT.
À l’époque de l’informatique des gros systèmes centralisés, des mainframes puis de l’informatique
ubiquitaire actuelle, les progrès réalisés dans le domaine des TIC sont évidents. En ce début de troisième
millénaire, les applications web et le web lui-même ne cessent d’augmenter en capacité. Ceci constitue
une motivation supplémentaire pour intégrer les TIC dans l’organisation de la MT de l’Afrique de l’ouest.
L’ensemble formé par les ontologies, le web sémantique et les langages de programmation objet, offre un
cadre technologique adéquat pour :
– pérenniser et sauvegarder les connaissances de la MT en termes de mémoire organisationnelle ;
– tirer le meilleur parti de la MT pour l’ensemble des acteurs : PMT, Patient, Entourage Patient, In￾formaticiens (ingénierie ontologique, wiki sémantique, infographie), Médecin de la MM, Faunisticien,
Botaniste, Enseignants-chercheurs, Chercheurs, Apprenants et Population grand public.
1.3 Problématique
L’Afrique de l’ouest est l’une des parties du monde où le taux de natalité est le plus élevé [56]. On y
note un état de pauvreté aggravant pour les couches sociales en surpeuplement. S’agissant de la MM, la
répartition des infrastructures sanitaires et surtout de soins de santé, est notoirement inégale au regard des
ratios des populations avec les espaces géographiques ou tout simplement de la densité (nombre d’habitants
par km2
) ou encore de la concentration des masses. La médecine à domicile est quasiment absente. On
constate également un manque de médecine de proximité et une insuffisance du personnel soignant dont
principalement les médecins [135]. Ce personnel est beaucoup plus concentré au niveau des métropoles
[165], un peu moins dans les autres zones urbaines et beaucoup moins dans les zones rurales.
De plus, les coûts élevés, parfois prohibitifs et dispendieux, des offres de soins de santé même primaires
rendent l’accès à la MM, difficile et inéquitable. Du coup, parallèlement à l’utilisation de la MM par ces
populations, ces dernières font appel à la MT pour répondre à leurs besoins en soins de santé. Selon l’OMS
[175] et à travers d’autres sources notamment [51], [201] et [210], la proportion de cette population ayant
recours à la MT est estimée à 80%.
Cependant, le patrimoine culturel constitué par la MT se perd du fait du caractère oral de la transmission
des connaissances d’une part, et d’autre part du vieillissement des PMT alors que l’espérance de vie actuelle
4

--- page 25 ---
est autour de 60 ans [56]. Nous relevons comme principaux moyens de transmission des connaissances, la
descendance, la lignée et l’innéisme [136].
Dans les pays d’Afrique de l’ouest, les PMT travaillent sans une véritable communication entre eux.
Aussi relevons-nous une absence totale de mécanismes et d’outils de préservation des savoirs, des connais￾sances, des pratiques et des expériences dans ce domaine. A leur mort, les PMT disparaissent avec les
savoirs et les savoir-faire tacites et professionnels accumulés durant des décennies.
A ce titre, leur créer un cadre d’échange, d’acceptation mutuelle, de collaboration constitue un chalenge
majeur. Ce cadre se veut un incubateur de capitalisation et de mutualisation durable du patrimoine formé
par les connaissances et expériences de la MT. C’est une mémoire organisationnelle [100], qui une fois
réalisée, sera utilisée et enrichie par les principaux acteurs, les PMT. Quant aux usages offerts aux autres,
notamment patients, chercheurs, médecins de la MM, enseignants en TIC et en Biosciences, et apprenants,
différents paliers de restrictions sur leurs possibilités d’intervention pourraient être définis. Cependant, la
pérennisation de ces savoirs nécessite aussi de faire face à la dégradation de l’environnement naturel, car
les sources médicinales sont à plus de 50 % végétales [10] [136]. Les connaissances ainsi mémorisées auront
non seulement un sens pour l’historique, mais également pour la pratique des soins de santé, si le couvert
floristique et faunique, c’est à dire le réel perçu et vivant d’où est assorti le matériel brut de travail du
PMT, continue d’exister. En conséquence, ce couvert se doit d’être préservé et régénéré au moyen de
mécanismes et techniques dont pourra tenir compte notre mémoire en terme d’extension.
Sans aucun doute, à terme, notre travail est à même d’apporter une contribution forte à la modernisation
et à la revalorisation de la MT africaine.
1.4 Objectifs
L’objectif principal de cette thèse est de construire une ontologie de domaine de la médecine tradition￾nelle (MT) comprenant une base de connaissances et un module de concepts iconisés (concepts représentés
par des icônes) selon un langage iconique s’appuyant sur une ontologie d’approche visuelle. Cela consiste
à élaborer des concepts terminologiques ou des termes conceptuels de l’ontologie suivie de leur représenta￾tion visuelle en s’appuyant sur un langage iconique de nature compositionnelle. Dans ce langage, les icônes
seront construites en assemblant plusieurs éléments (couleurs, pictogrammes, partie d’icône ou iconèmes,
etc). Ce langage facilitera l’exploitation de la plateforme par les PMT, qui sont en grande partie illettrés.
Les icônes conçues devront donc être propres à la MT et reconnues comme telles. Cette ontologie de la
MT, avec sa couche iconique, est ensuite destinée à être utilisée dans des outils de gestion de la MT.
Ce travail s’inscrit dans un projet de plus grande ampleur, en trois étapes :
– Étape 1 : construire une ontologie du domaine de la MT ;
– Étape 2 : créer une couche iconique de l’ontologie propre à la MT ;
– Étape 3 : utiliser les outils du web social et sémantique (par exemple un Wiki et plus spécifiquement
Virtuoso) comme technologie support, devant permettre aux PMT d’être assistés dans leurs tâches
de guérisseur.
Ce travail de thèse se concentre sur les étapes 1 et 2, l’étape 3 constituant une perspective future
proche.
Au regard de ce qui précède, un certain nombre de méta-préoccupations auxquelles une ontologie de
5

--- page 26 ---
domaine de la MT comme celle qui fait l’objet de notre travail de recherche est en mesure de répondre,
sont manifestes. Ce sont :
– revaloriser la MT au moyen d’outils technologiques de référence notamment les TIC ;
– renforcer la médecine associée, collaborative et intégrative en gestation [215] ;
– affranchir les PMT des barrières linguistiques ;
– faciliter la collaboration entre PMT dans l’exercice de l’art médical traditionnel.
1.5 Contributions
1.5.1 Idée maitresse
Rendre intelligibles à l’ordinateur les connaissances présentes dans une base de connaissances nécessite
l’utilisation d’une terminologie codée.
Construire une ontologie d’approche visuelle, notre préoccupation essentielle, est donc un défi au regard
de la complexité visuelle et de ce qui précède. Pour venir à bout de ce problème, nous allons construire une
ontologie formelle terminologique au sens habituel, sur laquelle devra s’adosser l’ontologie d’approche vi￾suelle. La première ontologie, ontoCONCEPT-Term, et la seconde, ontoICONE, forment ontoMEDTRAD,
une ontologie de domaine de la MT. ontoMEDTRAD elle-même est la principale composante du système
intégral envisagé : sysMEDTRAD. Ce dernier devra intégrer une plateforme web social et sémantique.
Le langage iconique principalement de nature compositionnelle se base sur ontoICONE, et fera corres￾pondre à un concept donné de ontoCONCEPT-Term une icône.
1.5.1.1 Fondement de notre travail de recherche : ontoCONCEPT-Term et ontoICONE de
ontoMEDTRAD
Figure 1.1 – Composantes basiques "ou fondationnelles" d’ontoMEDTRAD
La structure de ontoMEDTRAD est illustrée par la figure 1.1. La couche A représente l’ontologie
de la MT via les termes (concepts terminologiques). La description des concepts et des relations séman￾tiques entre ces concepts est d’ordre hiérarchique (taxinomique), associatif (horizontal) et composition￾nel. La couche B comprend les icônes en correspondance associative à un sous-ensemble des concepts de
ontoCONCEPT-Term (tous les concepts n’ont donc pas une icône). Ici, on privilégie la fonction iconique
d’ontoICONE (car elle détient une partie terminologique en partage avec ontoCPNCEPT-Term).
6

--- page 27 ---
Figure 1.2 – Correspondance sémantique entre termes/concepts et icônes/concepts
Figure 1.3 – Architecture simplifiée de la plateforme web social et sémantique : cadre basique d’échange
et de partage
1.5.1.2 Structure fondationnelle d’une ontologie d’approche visuelle
L’approche visuelle consiste à construire d’abord une ontologie de domaine avec des concepts et re￾lations entre eux, et ensuite à représenter par une icône chacun des concepts et relations à travers un
langage iconique. La figure 1.2 donne une démonstration d’une situation idéale structurant une ontologie
d’approche visuelle.
1.5.1.3 Plateforme web sémantique et social
Dans sysMEDTRAD, la plateforme dans sa quintessence est formée d’une base de connaissances issue
de l’ontologie. On a accès aux données primitives, axiomatisées, définies, instancielles et inférentielles. Cet
accès est opéré via des interfaces dont seules celles des acteurs principaux PMT et patient, cités ici dans
l’ordre de leur importance contextuelle, sont mises en relief à travers la figure 1.3.
En somme, ontoCONCEPT-Term dénote les concepts terminologiques de la MT. ontoICONE dénote
l’ensemble des icônes (et pictogrammes) représentant visuellement ces concepts. L’accès à sysMEDTRAD
par les différents acteurs se fera à travers d’un média Wiki sémantique (support de la plateforme web
social et sémantique).
Vu la complexité de la visualisation et celle de la construction d’une icône d’un concept donné, la
couverture des termes des concepts par les icônes sont réalisées de manière progressive et incrémentale.
Dans le cadre de cette thèse, nous présenterons un langage iconique pour identifier les plantes médicinales,
7

--- page 28 ---
ainsi qu’un langage diagrammatique pour présenter des recettes de remèdes à base de plantes et des
remèdes. De plus, le langage iconique a été relié à l’ontologie, de sorte à pouvoir générer automatiquement
les icônes à partir de la description formelle des plantes dans l’ontologie.
1.5.2 Publications
Nous avons réalisé quatre publications :
1. "Architecture d’un système de gestion des connaissances de la médecine traditionnelle : SysMED￾TRAD" [19] : dans cet article, après y avoir donné les raisons pour créer un fond organisationnel des
connaissances de la MT, nous définissons l’objectif général, les objectifs spécifiques, et nous proposons
une architecture pour un système de gestion des connaissances de la médecine traditionnelle ;
2. "Modélisation conceptuelle d’une ontologie de la médecine traditionnelle (ontoMEDTRAD)" [18] :
dans cet article, nous décrivons la conceptualisation et la formalisation d’une ontologie terminologique
de la médecine traditionnelle ; cette ontologie de domaine à proprement dit est ontoCONCEPT￾Term, l’un des deux modules de ontoMEDTRAD ;
3. "Vers un système iconique d’aide à la décision pour les praticiens de la médecine traditionnelle" [16] :
cet article montre l’intérêt d’un langage iconique pour la MT. Il se focalise sur la partie iconique
de l’ontologie de la MT que nous proposons. Il décrit l’amorçage de l’iconisation sur les concepts de
plantes ;
4. "Modelization of recipe in african traditional medicine with visual ontology approach, iconic sketch"
[17] : cet article porte sur l’iconisation du concept de Plante. Il modélise également l’aspect iconique
de la recette et du remède traditionnels pour la communauté des PMT de l’Afrique de l’ouest.
ontoICONE amorcé justifié à partir du concept de plante, est l’un des deux principaux modules
de ontoMEDTRAD.
1.6 Plan de la thèse
Notre manuscrit regroupe tous les travaux de cette thèse. Il est structuré en sept (7) chapitres.
Suite au chapitre 1 introductif (contexte, problématique, objectifs et contributions), les trois suivants
tracent globalement l’état de l’art. Plus précisément, le chapitre 2 présente un état de l’art sur la médecine
traditionnelle (MT) de l’Afrique de l’Ouest avec une empreinte de capitalisation.
Le chapitre 3 porte sur l’état de l’art de la représentation des connaissances en général, et particuliè￾rement sur les ontologies formelles.
Le chapitre 4 présente un état de l’art sur les icônes et les langages iconiques.
Nos contributions sont les chapitres 5 et 6.
Le chapitre 5 décrit la construction d’ontoMEDTRAD, une ontologie de domaine de la MT africaine.
Le chapitre 6 présente ontoICONE, une ontologie visuelle via la description d’un langage iconique
portant sur des concepts de ontoCONCEPT-Term : Plante, Recette et Remède.
Le chapitre 7 est un récapitulatif des discussions, conclusions et perspectives.
8

--- page 29 ---
Chapitre 2
Médecine traditionnelle de l’Afrique de
l’ouest et son état pour capitalisation (des
connaissances)
Sommaire
2.1 Analyse de la MT : Nécessité de capitaliser et de pérenniser les savoirs . . . 10
2.2 Définitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.3 Fondement historique, origine et évolution de la MT . . . . . . . . . . . . . . . 20
2.4 Traits caractéristiques de la MT . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.5 Organisations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.6 Prédisdisposition organisationnelle et solutionnelle de capitalisation des connais￾sances . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
2.7 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
9

--- page 30 ---
Dans ce chapitre, nous allons présenter la médecine traditionnelle (MT) de l’Afrique de l’ouest à
travers ses caractéristiques et son organisation. Pour cela, nous nous sommes fondés sur des recherches
bibliographiques, la documentation obtenue de structures agrées de santé publique et d’organisations non
gouvernementales, les rencontres de terrains avec une cinquantaine (50) de PMT en Côte d’Ivoire et une
soixantaine (60) au Sénégal. L’observation et les ressources en ligne complètent cette liste de sources
documentaires non exhaustive pour asseoir notre analyse.
Nous nous focaliserons sur les préoccupations pouvant mener à des possibilités de solutions informatiques
en vue d’améliorer l’organisation de la MT et son intégration dans les systèmes nationaux de santé et
d’augmenter le volume des offres de soins de santé primaires en complément à celles de la MM, dans les
pays d’Afrique de l’ouest.
2.1 Analyse de la MT : Nécessité de capitaliser et de pérenniser les
savoirs
Depuis l’antiquité et même avant, la santé humaine a toujours été une préoccupation majeure de la
société pour prévenir et éradiquer la maladie ou vivre avec elle. Les courants de pensées, la transmission
du savoir via les écoles antiques jusqu’aux universités, puis à celles de standing actuel, les agissements
culturels et anthropiques, les échanges économiques partant du troc au capitalisme, et beaucoup d’autres
transformations ont eu lieu et continuent de s’opérer au fil des décennies et des siècles. A des degrés
divers, naturellement, ou au gré des progrès et découvertes scientifiques, nos modes de vie et de pratique
de nos activités socio-culturelles sont en perpétuelle mutation. Presque toutes les activités humaines y
compris les pratiques médicales et singulièrement la MT, telles qu’elles se menaient il y a un siècle,
une cinquantaine d’années ou par le passé, sont différentes de celles de nos jours. Nous pouvons noter
la disparition de certaines activités et l’émergence d’autres, somme toutes observant cette dynamique.
Inhérent à ces activités humaines, ce phénomène réflexif et récursif, continu et perceptible de génération
en génération, est irréversible. Relativement aux médecines du monde et singulièrement à celle d’Afrique,
les perturbations ou bouleversements intra et interculturels, sans occulter la traite négrière, l’esclavage,
la colonisation, les indépendances, les immigrations et les migrations, ont influencé tantôt positivement,
tantôt négativement à des moments donnés, leur élan savant [49] [103] [126] [139].
Avant l’avènement de la médecine actuelle à travers le monde entier, les hommes ont eu à développer
plusieurs pratiques médicales peu ou prou appropriées pour faire face aux nombreuses maladies mortelles.
Il s’agit notamment des produits relevant de la nature et essentiellement d’origine végétale, animale,
minérale et même métaphysique (divine ou surnaturelle). Ce type de pratiques médicinales, s’améliorant
sans cesse, fait apparaître deux domaines clés (ou majeurs) de médecine.
D’une part, nous avons la médecine moderne (MM), beaucoup plus structurée et connaissant un essor
remarquable grâce à la recherche scientifique. Elle est dite médecine conventionnelle. Au fil du temps,
cette médecine a connu différentes déclinaisons notamment médecine occidentale, médecine biologique, bio￾médecine, médecine scientifique, médecine de haute technologie, ... Aujourd’hui, on note dans ce domaine
l’utilisation des technologies de pointe. Dans les pays en voie de développement, cette médecine n’est pas
accessible à toutes les couches de la population pour qui les coûts de soins sont prohibitifs. Ce système de
santé s’appuie sur une recherche scientifique de haut niveau et caractérisé par des tests cliniques de très
grande rigueur [150]. Actuellement, elle est dite médecine de haute technologie et de précision. Il est fait
usage de toutes les sources médicinales hormis celles d’ordre métaphysique. Cependant, nous ne pouvons
que constater l’existence de maladies persistantes et inguérissables (folies et certaines maladies mentales),
10

--- page 31 ---
la résurgence d’anciennes maladies (e.g. : Ebola en Guinée Conakry en 2013) et l’apparition de nouvelles.
Nous pouvons préciser que la médecine conventionnelle est d’abord faite par et pour les pays occidentaux
et les patients ayant un mode de vie sédentaire et urbain : cela correspond au profil des patients recrutés
dans les essais cliniques, et aux patients « ciblés » par les laboratoires pharmaceutiques.
D’autre part, nous avons la médecine non conventionnelle dont les soins relèvent des produits naturels
ayant subi moins de transformations (notamment chimiques). Ce domaine progresse (plus lentement que
celui de la MM) avec des pratiques beaucoup moins structurées voire informelles ou semi-formelles. Toutes
les sources médicinales sont utilisées notamment végétales, minérales et animales et surnaturelles. Pour
faire face aux soins de santé, nombreuses sont les populations à travers tous les continents, et singulièrement
dans les pays en développement ou en voie de développement, qui continuent de se référer à ce type de
médecine.
A ce dernier niveau, deux sous-types de médecine sont à distinguer, l’un plus usité dans les pays déve￾loppés, qui est la médecine complémentaire ou parallèle, ou encore alternative ou douce (complementary
and alternative medicine), et l’autre dit médecine traditionnelle (MT) beaucoup plus pratiqué dans les
pays en développement (Afrique, Asie et Amérique du sud). En Asie, et principalement en Chine, la MT
représente 40% des soins de santé primaires (au regard de la pyramide sanitaire) administrés [173]. En
Afrique de l’ouest, pour cette même catégorie de soins, 80% de la population a recours à cette MT regrou￾pant des techniques et connaissances appelées pharmacopée traditionnelle [175]. Ce type de soins concerne
un sous domaine de la santé et cible plus spécifiquement l’être humain. Il donne lieu à un ensemble étendu
de connaissances et de pratiques. Il est simplement dénoté par la MT avec des déclinaisons africaine,
chinoise, indienne. . .
En Afrique de l’ouest, en matière de MT, le principal vecteur de transmission des connaissances, lors￾qu’elles ne sont pas tenues secrètes, est l’oralité, marquée d’une importance indubitable dans les us et
coutumes. Manifestement, lorsqu’un PMT décède, c’est toute la somme de ses expériences acquises qui
disparaissent. Une politique nouvelle doit permettre de disposer dans ce domaine, d’une base de connais￾sances (BC) et d’expériences évolutive pour atténuer cette perte. C’est ce à quoi s’attelle notre travail par
la création d’une mémoire collective de la MT, comme socle d’un héritage pour les générations nouvelles.
Cette mémoire est une capitalisation progressive des connaissances de la MT de l’Afrique occidentale. Du
secret à l’ouverture, du tacite à l’explicite, de la perte des connaissances à leur persistance du fait en
partie du renouvèlement et de l’enrichissement du fond organisationnel constitué, du caractère fortement
propriétaire des informations et concepts à leur désincarnation [100], donnent de la voie à une souplesse
infinie pour les habilités des acteurs en matière de réutilisation et de contribution.
2.2 Définitions
2.2.1 Médecine traditionnelle
Selon la définition officielle de l’OMS [173] [175], "la médecine traditionnelle (MT ou TM en anglais
traditional medicine) se rapporte aux pratiques, méthodes, savoirs et croyances en matière de santé qui
impliquent l’usage à des fins médicales de plantes, de parties d’animaux et de minéraux, de thérapies
spirituelles, de techniques et d’exercices manuels, séparément ou en association pour soigner, diagnostiquer
et prévenir les maladies ou préserver la santé". Plusieurs autres définitions se rapprochant de la précédente,
existent. Parmi elles nous en donnons trois autres :
– Pour l’UNESCO [231], la MT est un concept qui déborde largement le champ de la santé pour se
11

--- page 32 ---
placer au niveau socioculturel, religieux, politique et économique. Elle peut être considérée comme
"un système de prise en charge du malheur (biologique ou non), qui s’appuie sur des théories du
corps, de la santé, de la maladie et de la guérison ancrées dans l’histoire des cultures et des religions
qui ont construit et construisent un pays". On peut dire qu’il existe presque autant de médecines
traditionnelles que de cultures.
– "La MT est un ensemble des connaissances et des pratiques permettant de diagnostiquer et de
dispenser des soins de santé, au moyen de méthodes se référant au fondement socio-culturel propre
aux sociétés dites traditionnelles" selon Kroa [136].
– A travers [14], Gbodoussou, président de l’ONG Prometra dit : "La MT, qu’elle soit africaine, asia￾tique ou aztèque, se définit comme un système de connaissances, une sagesse ancienne, un ensemble
spécifique de pratiques assurant l’équilibre de l’être humain et l’harmonie avec son environnement".
2.2.2 Tradipraticien ou thérapeute traditionnel
Le tradipraticien ou thérapeute traditionnel est "une personne reconnue par la collectivité où elle vit,
comme compétente pour dispenser les soins de santé, grâce à l’emploi, de substances végétales, animales
ou minérales, et d’autres méthodes basées sur un fondement socioculturel et religieux, aussi bien que sur
les connaissances, compétences, croyances liées au bien être physique, mental et social ainsi qu’à l’étiologie
des maladies et invalidités prévalant dans la collectivité" [136].
Selon [21], le tradipraticien est également un homme ou une femme très connu et respecté, grand psy￾chologue, botaniste, pharmacologue et médecin, et qui connaît les noms des plantes, des animaux et des
roches pour soigner les malades.
Selon [129], à la fois prêtre, féticheur et médecin, le tradipraticien fait le lien entre les hommes et les
forces surnaturelles. Il est appelé aussi tradimédecin. On l’appelle également praticiens de la Médecine
Traditionnelle (PMT). C’est bien cette appellation que nous avons retenue et qui est la plus employée
dans ce manuscrit.
Typologies ou spécialités du PMT
Les catégories du PMT auxquelles les différents auteurs s’accordent sont [9] [14] [21] [72] [85] [133] [136] [150]
[172] [178] [192] : Accoucheuse traditionnelle, Diététicien traditionnel, Herboriste , Naturothérapeute , Phy￾tothérapeute, Psychothérapeute, Rebouteur traditionnel, Ophtalmologue traditionnel, Médico-droguiste
traditionnel, Kinésithérapeute traditionnel, Acuponcteur, Phlébotomiste.
Le phlébotomiste est un tradipraticien qui pratique principalement les techniques de saignée corporelle
du malade (patient) en vue de le soigner.
Nous pouvons remarquer que certaines fonctions qui existent en MM existent aussi en MT (e.g :
ophtalmologue). Bien entendu, les modes opératoires de prise en charge du patient sont très différents.
En plus de ce qui précède, par opposition aux fonctions cosmologiques, il existe les spiritualistes (ou noo￾logiques) qui soignent les patients principalement par les rites (religieux ou non) ou à partir de rites. Dans
cette classe sont logées plusieurs fonctions de guérisseurs PMT, notamment : Devin, Exorciste, Féticheur,
Occultiste, Prophète, Ritualiste, Voyant, Prêtre (musulman ou non), Sorcier.
12

--- page 33 ---
Nous relevons que le cas de sorcier est typique, car il peut également rendre malade, jeter ou lancer
des sorts, faire usage des sciences occultes.
Un PMT peut avoir ou exercer dans plus d’une spécialité ou catégorie. Également, il peut avoir plusieurs
titres spiritualistes. Il peut à la fois assurer des fonctions cosmologiques et spiritualistes.
Le Komian est un féticheur, dans l’ethnie Agni en Côte d’Ivoire, pouvant prédire les évènements
importants (malheur ou bonheur). Il est consulté pour trouver la cause d’une maladie, pour protéger
contre certains malheurs [136].
2.2.3 Ethnopharmacologie
L’ethnopharmacologie se définit comme "l’étude scientifique interdisciplinaire portée sur l’ensemble
formé de matières d’origine végétale, animale ou minérale et des savoirs ou des pratiques s’y rattachant, que
les cultures vernaculaires natives mettent en œuvre pour modifier les états des organismes vivants à des fins
thérapeutiques, curatives, préventives ou diagnostiques" [81]. C’est donc une approche transdisciplinaire
qui s’intéresse aux connaissances des populations concernant la recherche, la préparation et l’utilisation
de remèdes médicinaux traditionnels.
Elle est formalisée en trois étapes que sont :
– (a) terrain ;
– (b) laboratoire ;
– (c) retour sur terrain.
L’étape (a) est concentrée sur le recensement des savoirs thérapeutiques.
L’étape (b) porte sur les activités en laboratoire visant à évaluer l’efficacité thérapeutique des remèdes
traditionnels.
Et enfin, l’étape (c) est axée sur les programmes de développement de médicaments traditionnels
préparés avec des plantes cultivées ou récoltées localement.
Ainsi, l’ethnopharmacologie apparaît comme un programme logique et rigoureux pour proposer un
accès aux soins avec des médicaments à base de plantes, produits du terroir et issus des savoirs locaux.
En outre, l’ethnopharmacologie peut être vue comme un regard croisé ou une synthèse plus intéressante
entre la vision d’une représentation du monde et d’une culture donnée (ethnologie), et l’étude objective
des propriétés thérapeutiques de substances (pharmacologie) naturelles au laboratoire [49]. Guidée par les
usages empiriques des plantes, l’étude éthnopharmacologique a apporté à l’humanité plus de 60 % de ses
médicaments quotidiens (en pharmacie d’origine végétale). Fondamentalement, à la croisée des sciences de
l’homme et de la nature, elle développe des méthodologies originales, alliant tradition et modernité [92].
A cet effet, cette technique permet la codification des savoirs dont la transmission est fortement orale, et
dans un domaine où la reconnaissance du métier de guérisseur traditionnel par la MM, est difficile et non
systématique.
L’ethnopharmacologie est est un terme employé par écrit pour la première fois en 1967 par Efron
[35]. Elle porte de manière spécifique sur l’observation, l’identification, la description et l’investigation
expérimentale des ingrédients et leurs effets. Il n’en demeure pas moins des médicaments traditionnels
obtenus à partir des combinaisons de ces ingrédients [2].
Les fonctions et services de l’ethnopharmacologie occupent une place prépondérante dans l’industrie du
médicament et de l’innovation thérapeutique [35].
La démarche ethnopharmacologique consiste à s’intéresser aux relations existant entre les médicaments
et les manières de se soigner qui sont propres à chaque ethnie. Il s’agit précisément de mieux connaître les
remèdes traditionnels pour améliorer la santé. Pluridisciplinaire donc, l’ethnopharmacologie s’inscrit dans
13

--- page 34 ---
le champ de la recherche pharmaceutique et participe à l’innovation thérapeutique en soins de santé à
l’échelle de tous les besoins. Connexe à l’ethnopharmacologique et vu son caractère transversal également,
la psychopharmacologie (étudiant les psychotropes, sortes de produits ou de substances chimiques ayant un
effet sur le psychisme en matière de médicament) comprend en partie la pharmacopée traditionnelle d’une
part et d’autre part l’ethnobotanique dont nous donnons une description succincte dans les paragraphes
qui suivent.
2.2.4 Pharmacopée traditionnelle
La pharmacopée traditionnelle ou vernaculaire recouvre l’ensemble de remèdes fondés exclusivement
sur le long usage ancestral et autochtone, et sur l’observation transmise de génération en génération,
oralement ou par écrit. C’est aussi l’art de préparer des substances thérapeutiques par une approche
presque empirique, c’est-à-dire sans démarche expérimentale où l’oralité a pris une place plus importante
que l’écrit [248].
Kerharo [129] définit la pharmacopée traditionnelle comme un recueil de recettes ou de formules des￾tinées à préparer les médicaments dans lesquels entrent toutes les parties de plantes auxquelles s’ajoutent
parfois divers produits d’origine animale ou minérale. Elle est donc l’ensemble des substances naturelles
ainsi que leurs techniques de préparation en vue d’obtenir une thérapeutique destinée à supprimer les
altérations physiques ou psychiques constitutives de la maladie.
Cette pharmacopée englobe l’ensemble des remèdes et des pratiques thérapeutiques d’une ethnie don￾née. Elle est en conséquence liée à une région géographique particulière et appartient au système de santé
de l’ethnie en question. Elle est principalement alimentée par une faune et une flore caractéristiques et
variées en faveur du climat tropical de l’Afrique de l’ouest. L’on estime à plus de 500 espèces de plantes
médicinales [8] malgré la coupe franche menaçante à un rythme effréné donnant place à la déforestation
tangible surtout des zones sud de l’Afrique de l’ouest. Ces zones étaient auparavant plus couvertes.
2.2.5 Ethnobotanique
Contraction de l’ethnologie et de la botanique, l’ethnobotanique est l’étude des relations entre l’homme
et les plantes. Son domaine d’étude implique une large gamme de disciplines depuis les recherches archéo￾logiques sur les civilisations anciennes jusqu’à la bio-ingénierie contemporaine. L’étude ethnobotanique
laisse entrevoir le rôle de certaines plantes dans la construction de l’être humain au fur et à mesure de son
évolution vers l’âge adulte [234]. Elle participe à la création de l’identité humaine.
Le terme ethnobotanique est pour la première fois introduit par le botaniste américain John Harsh￾berger autour de 1895-1896 [60]. C’est une discipline qui interfère sur plusieurs autres, mettant en liaison
l’humain et la plante [1]. Bien que les plantes médicinales aient toujours constitué l’intérêt principal de
l’ethnobotanique, cette dernière s’intéresse également à d’autres produits dérivés de la nature comme
les aliments, l’utilisation des plantes dans des cérémonies rituelles, la coloration d’objet de tout genre,
les fibres de plantes, les poisons, les engrais, la construction de matériels de maisons, les ménages, les
bateaux, etc. Nous pouvons citer entre autres les disciplines en partie incluses dans l’ethnobotanique no￾tamment la botanique, la biochimie, la pharmacognosie (étude des médicaments provenant de substances
animales ou végétales), la toxicologie, la médecine, la nutrition, l’agriculture, l’écologie, l’évolution, la
religion comparative, la sociologie, l’anthropologie, la linguistique, la cognition, l’histoire et l’archéologie
[2].
14

--- page 35 ---
La Paléobotanique est une discipline interprétative et associative qui recherche, utilise, lie et interprète
les faits d’interrelations entre les sociétés humaines et les plantes en vue de comprendre et d’expliquer la
naissance et le progrès des civilisations, depuis leurs débuts végétariens jusqu’à l’utilisation et la trans￾formation des végétaux eux-mêmes dans les sociétés primitives ou évoluées. Elle n’étudie, en eux-mêmes,
ni les plantes, ni les sociétés humaines, ni les Hommes. Elle est une des deux branches de l’ethnobiolo￾gie, l’autre étant l’ethnozoologie. L’ethnobotanique est à l’intersection des domaines de l’ethnologie, de la
botanique, de l’agronomie et de la génétique [209].
2.2.6 Phytothérapie
Le mot phytothérapie provient de deux mots grecs "phuton" et "therapeia" qui signifient respective￾ment "plante" et "traitement" [57]. Plus explicitement, le préfixe Phyto d’origine grecque indique une
relation avec les plantes. Thérapie signifie un traitement médical ou thérapeutique. Ceci implique simple￾ment et nettement le terme "soigner avec les plantes". La phytothérapie est donc l’utilisation thérapeutique
des plantes. Elle repose sur une pratique millénaire basée sur un savoir empirique qui s’est transmis et
enrichi au fil d’innombrables générations. La phytothérapie est également une méthode thérapeutique qui
utilise l’action des plantes médicinales. Une spécificité de cette thérapie est la mycothérapie [113] [177]
qui consiste à un traitement médical par les champignons ou par les substances sécrétées par les champi￾gnons ( végétaux non ligneux). Dans ce travail nous ne ciblons pas les champignons (la mycothérapie).
On distingue deux types de pratique de la phytothérapie [211], l’un traditionnel et l’autre moderne,
respectivement encore qualifiés de phytothérapie traditionnelle et phytothérapie moderne.
2.2.6.1 Phytothérapie traditionnelle
Très ancienne, cette pratique est basée sur l’utilisation de plantes selon les vertus découvertes empirique￾ment. Cette phytothérapie traditionnelle est considérée comme une MT et encore massivement employée
dans les pays en voie de développement (en développement), selon l’OMS [211]. C’est une médecine non
conventionnelle du fait de l’absence d’étude clinique et scientifique.
2.2.6.2 Phytothérapie moderne (phytothérapie clinique)
Elle s’appuie sur les avancées scientifiques qui recherche des extraits actifs des plantes (ou drogues)
[57] [211]. Les extraits actifs identifiés sont standardisés. Cette pratique conduit aux phytomédicaments
et à des médicaments pharmaceutiques selon la règlementation en vigueur dans le pays.
Autres types de thérapies :
La thalassothérapie, la balnéothérapie (hydrothérapie) [149], et l’argilo-thérapie [133] viennent renforcer
la liste des thérapies traditionnelles (ou partiellement moderne) qui ne saurait être exhaustive.
– La thalassothérapie contractée thalasso, est une médecine douce reconnue depuis l’Antiquité. Elle
renferme un usage thérapeutique par bains de mer, en environnement et climat marins (eau de mer,
de boue ou d’algue, de sable et d’autres substances extraites de la mer).
15

--- page 36 ---
– La balnéothérapie comprend la thalassothérapie. Elle est plus générale et désigne l’ensemble des soins
effectués par des bains généraux ou locaux (d’eau douce, de boue ou d’algue, de sable et d’autres
substances extraites de la mer). Par extension, la balnéothérapie peut s’appliquer aux bains solaires
et aux rayons ultraviolets ou infrarouges. En somme la balnéothérapie comprend l’ensemble des
soins, traitements et cures où des bains sont utilisés.
– L’argilo-thérapie africaine (dans certaines régions de la côte d’ivoire) qui offre des soins curatifs et
préventifs à base d’argile (massage, pose d’argile sur entorse ..).
Traitement curatifs et préventifs :
Pour le traitement d’un patient, l’entendement du PMT des soins de santé curatifs et préventifs (voir
Typologie de prévention par l’OMS 1
) est conforme à celui de la MM dans la majorité des cas. Relativement
aux cas restants, le PMT de la MT ne peut jamais ignorer la maladie qui tenaille un patient dont aucun
signe n’est détectable par le médecin de la biomédecine (en dépit d’examens cliniques multiples). En outre,
si en MM, la maladie peut être ignorée, quand bien même le patient concerné se sent bien, elle est toujours
révélée en MT. En MT, des prédictions de mal effectif à moyen et long terme faite à l’endroit d’un patient
se portant bien actuellement permet de prendre des mesures prophylaxiques préventives traditionnels en
son endroit accompagnés de conseils avisés.
En somme, la volonté de guérison du patient par la racine en lieu et place par des calmants est très
manifeste chez la plupart des PMT surtout chez les plus renommés.
2.2.7 Mise sur le marché des produits de la MT
Pour la mise sur le marché (en vente) des médicaments et produits pharmaceutiques de la MM, si
une organisation soutenue est observée à travers des agences et autorités de régulation [174], au niveau
de la MT [214], une telle organisation est véritablement absente. Les structures de contrôle de la MM des
pays de cette région ouest-africaine ont alors amorcé des règlementations propres à la MT. En exemple
de ces structures, on a généralement, les laboratoires nationaux de santé publique et les démembrements
ministériels, en charge du contrôle de la pharmacie du médicament et des laboratoires. Ils sont chargés
de tester les principes actifs des plantes ou autres sources médicamenteuses de la MT. Les produits de la
MT ayant subi avec succès ce type de test sont qualifiés de médicaments traditionnels améliorés (MTA).
On a également des usages de masse. Dans ce cas on parle de médecine populaire. Tous ces médicaments
traditionnels sont en voie d’être classifiés en quatre (4) catégories (I, II, II,IV) tenant compte de leur
mode de préparation et le degré d’ingéniosité ou d’ingénierie, débuté depuis mai 2001 par un comité
régional d’experts de l’OMS Afrique sur la MT [13]. Ces quatre catégories sont décrites et n’ont pour
seules désignations actuelles : I, II, II, IV.
2.2.8 Plante médicinale
En MT, les ressources sont d’ordre végétal, animal, minéral et autres. La proportion de ces ressources
la plus présente, imposante et importante d’une part, et d’autre part la plus utilisée et accessible par le
PMT, porte sur une ressource végétale. Plus spécifiquement c’est la plante. Dès lors, la plante médicinale
est l’une des premières cibles dans notre approche de solution. La plante constituera alors un des concepts
ontologiques de base. Entendons par plante médicinale, une plante dont au moins une de ses parties
1. http ://www.herboristerie-de-lyon.com/82-les-differents-niveaux-de-prevention-selon-loms/ consulté en 2015
16

--- page 37 ---
Plante : neemier ou le margousier ou encore, arbre à pharmacie d’Afrique de l’ouest
famille genre espèce descripteur
(nom du botaniste auteur de la description de
la plante)
Meliaceae Azadirachta indica A. Juss
TABLEAU 2.1 – Exemple de nom botanique ou scientifique d’une plante selon Linné
(ou composantes) possède des propriétés thérapeutiques ou médicamenteuses [214]. En MT, les propriétés
thérapeutiques d’une partie de la plante (ressource médicinale en général) sont systématiquement conférées
à la plante. Autrement dit, les vertus thérapeutiques des parties d’une plante sont celles de la plante elle￾même. L’affirmation inverse, c’est à-dire, la vertu thérapeutique de la plante est celle de ses parties n’est
pas recevable sauf les cas d’utilisation de la plante entière (couramment les herbes).
En outre, pendant de nombreux siècles et de toute saison, la plante médicinale a constitué la principale
source thérapeutique disponible. Bien plus que cela, et du point de vue des anciens d’Afrique et d’ailleurs, la
plante médicinale est un microcosme vivant. Ainsi conceptualisé, cet individu est objet de deux approches
selon cette vision holistique : l’une est physiologique et l’autre thérapeutique. Cette vision renvoie la
plante comme une "globalité vivante". "Le tout est plus grand que la somme des parties" est une règle
fondamentale dictée par Ibn Sîna, plus connu sous le nom d’Avicenne (980-1037) [61]. Ainsi, l’homme
est un tout, doté d’un "tempérament" unique et particulier, qui n’est pas la résultante de la somme ses
composantes. Le constat est pareil pour la plante médicinale : l’action thérapeutique de la plante entière
diffère de celle de ses principes actifs isolés. On serait tenter de dire qu’elle est plus grande que celle de ses
parties prises individuellement. Ce tempérament est basé sur le principe présocratique hérité qui est "Tout
corps est constitué d’un mélange des quatre(4) éléments (feu, air, terre, eau) en proportion déterminée
[145].
La plante médicinale peut également avoir des usages alimentaires, condimentaires ou hygiéniques [57].
La plante de type arbre est aux mêmes fins (meubles, immeubles, habillement, papeterie, construction de
véhicules, ...) que les arbres.
La plante, espèce végétale est connue universellement par son nom scientifique ou botanique au sens
général de la systématique ou classification de Carl Von Linné (1707-1778). Cette classification connue
sous plusieurs autres appellations dont classification phylogénétique, systématique phylogénétique, repose
sur la phylogenèse ou phylogénie (un des systèmes de classification des êtres vivants). Ici, dans notre
notation de la plante, souvent on associe l’espèce et son genre, et parfois on rajoute la famille mis entre
parenthèse. On y rajoute souvent le nom du descripteur (auteur de la description) juste avant la famille.
Par exemple pour le neemier, le nom scientifique est Azadirachta indica A. Juss.(Meliaceae). L’espèce,
le genre, le descripteur et la famille sont respectivement Azadirachta, indica, A. Juss. et Meliaceae (voir
tableau 2.1).
Ce qui vaut effectivement "Azadirachta indica A. Juss" ou encore "Azadirachta indica A. Juss. (Me￾liaceae)", comme nom botanique ou nom scientifique attribué à la plante neemier.
2.2.9 Partie utile de plante
Une partie utile de la plante est une partie de cette plante (e.g : feuille, racine, fleur, tige, tronc, fruit,
écorce, sève, plante entière), pouvant entrer dans la composition d’une recette thérapeutique. Il faut noter
17

--- page 38 ---
que c’est à l’état de maturité, après croissance et avant le déclin, que la plante dispose au mieux à travers
ses parties, des principes actifs. Cette partie utile servira d’ingrédient pour les recettes médicamenteuses.
Notons que la plante est dans les ressources médicinales traditionnelles la plus prescrite par les PMT à
auteur de plus de 60%. Cette plante est donc la première cible de nos investigations conceptuelles et de
constructions iconiques en vue. Aussi notons-nous que parmi les parties de plantes, les feuilles sont au
taux d’environs 62 % [38] [82] [132] [170] [171]. Selon ces mêmes sources les écorces (des racines et des
troncs et tiges) sont à taux variable selon les maladies.
2.2.10 Recette
Le terme recette (recipe en anglais) est utilisé dans plusieurs domaines notamment en gastronomie
culinaire (cuisine), en musicologie (partitions musicales), en commerce et trésorerie financière (recettes
et dépenses), en linguistique (genre de texte discursif, récit, ordre, formulaire figé, plan, loi, conseils et
horoscopes) [4], en médecine [150], en gestion de projet (recette comme étant le test de conformité de
l’ouvrage à la demande formulée dans le dossier validé de conception générale relatif à la spécification des
besoins ou cahier de charges) [131], etc.
Ici, le terme recette est essentiellement propre à la MT (médecine traditionnelle). Intrinsèquement, la
recette est l’ensemble formé de parties utiles de ressources médicinales (e.g : végétal (ou plante), animal,
minéral) [134] en vue de soigner un patient, de lui apporter des soins de santé. La recette est souvent
rendue plus exhaustive en lui rajoutant le mode de préparation.
La recette est dite mono-spécifique [171] lorsqu’elle découle d’une seule plante. C’est à dire, les parties
utiles composant la recette, sont toutes d’une seule plante. La recette est dite multi-spécifique lorsqu’elle
émane de plusieurs plantes.
2.2.11 Remède
Par remède (remedy en anglais) [150], l’on entend, toute substance utilisée pour guérir une maladie,
un mal dont souffre un patient. Ce qui guérit un mal moral. Tout ce qui sert à prévenir un malheur,
une difficulté, à les faire cesser. "Un médicament est toute substance ou composition présentée comme
possédant des propriétés curatives ou préventives à l’égard des maladies humaines ou animales, ainsi que
tout produit pouvant être administré à l’homme ou à l’animal, en vue d’établir un diagnostic médical ou
de restaurer, corriger ou modifier leurs fonctions organiques" selon [57]. Le médicament est un remède mais
tout remède n’est pas un médicament surtout quand remède s’accorde comme un moyen, une solution face
à une difficulté ou à un problème donné. Zerbo et al [247] parlent de recette médicamenteuse en adressant
le remède ou le médicament traditionnel.
Dans le cadre de nos travaux une attention particulière raisonnée porte sur la représentation des re￾mèdes traditionnels de la MT à base de plantes médicinales. Ainsi, le remède est à base d’une recette. Il
comprend par essence une recette avec une forme de fin de préparation, un ou plusieurs modes d’adminis￾tration (et l’indication de traitement constituée par la maladie). Les formes de remèdes sont multiples. On
a les liquides (lotion, décoction, sirops, potion), les solides et galéniques, la poudre, les formes de vapeur
et gazeuses, la patte ou pommade, ... On a aussi comme remède, le MTA.
18

--- page 39 ---
Figure 2.1 – Processus de clarification de signes et de symptômes d’une maladie
2.2.12 Signes et symptômes
Dans l’art médical, signes et symptômes sont respectivement relatifs à la maladie et au patient [12].
Relevons que les symptômes ont une certaine subjectivité. Un symptôme est quelque chose que le pa￾tient ressent ou dont il se plaint. Les signes sont plus objectifs pour la détermination d’une maladie. Les
symptômes sont à vérifier afin de les admettre signes ou non, souvent à travers un test ou examen clinique.
Les symptômes objectifs sont admis comme signes. Les symptômes subjectifs peuvent devenir objectifs
dès leur confirmation par un examen clinique, sinon ils demeurent tels et au niveau du seul patient. La
véracité de ces symptômes tient aux seuls dires du patient qui est le seul à les ressentir.
Les symptômes sont décrits par le patient, alors que les signes sont recherchés et mis en évidence par le
médecin lors d’un examen clinique. Le diagramme de la figure 2.1 permet de mettre en lumière les nuances
entre signe et symptôme et d’en faire la distinction.
En MT, une ressource médicinale en général et en particulier une plante peut être utilisée pour traiter
une ou plusieurs maladies, et un ou plusieurs symptômes (ou signes). Dans un cadre plus général, le signe
est l’objet central d’étude scientifique pour la sémiologie ou la sémiotique. Cette science a un apport
indispensable dans le langage iconique à construire.
Un syndrome est l’ensemble des symptômes et des signes d’une maladie qui peuvent être manifestés
par un patient. Signe et symptôme constituent également des indices de la Maladie.
19

--- page 40 ---
2.3 Fondement historique, origine et évolution de la MT
2.3.1 Fondement de l’art médical traditionnel
Ce n’est pas une exagération de dire que l’art médical a la plus longue histoire de toute l’humanité.
La pensée de Kerharo vient une fois de plus en faire la démonstration à travers ses propres termes [129] :
" . . . S’il est un domaine dans lequel les hommes de tous les temps et de toutes les races ont, dans tous les
pays à l’origine de leur histoire, fait intervenir le sacré, le mystique et le religieux, c’est bien celui de l’art
médical, né de l’inquiétude humaine en présence de la maladie et de la mort". D’où parfois, la médecine
au regard d’une part du sacré et d’autre part du mysticisme, constitue une pratique où sont noués des
rapports véritablement complexes. Il s’en suit une vraie énigme ayant pour objet, la nature et le statut
épistémologique de la relation entre la santé et la médecine.
La question de la santé humaine revêt toujours des caractéristiques ou aspects touchant la multisec￾torialité et l’interdisciplinarité. En outre, les connaissances et les croyances relatives à la vie, à la mort,
aux maladies, aux empoisonnements, aux envoûtements, aux exorcismes et autres, sont connexes et même
inféodées à l’art médical. La pratique de l’art médical traditionnel jusqu’à nos jours, est du ressort des
différentes catégories d’individus ou de personnes qui en font profession, soit régulièrement, soit occa￾sionnellement. Entre autres nous pouvons citer : les guérisseurs, les féticheurs, les devins, les marabouts,
les charlatans [128]. La problématique du maintien de la santé des hommes est donc une préoccupation
centrale au cœur d’un environnement qui se veut sain et propice aux activités sociétales. En somme, la
médecine dans toute son entièreté et sur toutes ses formes, va de paire avec la présence humaine.
Au regard de ce qui précède, nous donnons quelques déterminants ou facteurs corrélés dont est assujetti
l’état de santé humain. A travers [44] et [123], notons que l’état de santé humain est influencé par quatre
facteurs catégoriels (ou strates inclusifs) en partant des plus englobantes au plus spécifiques. Ce sont un
environnement global suivi successivement de trois environnements spécifiques (voir figure 2.2).
Toutes sortes d’indicateurs peuvent être assorties de ces facteurs touchant l’état sanitaire d’une per￾sonne prise individuellement, d’une population.
2.3.2 Évolution de la médecine de l’humanité et courants de médecine en usage
Il est impossible de remonter jusqu’à l’origine de la science. Notre hypothèse se fonde sur ce que nous
laisse la littérature en matière de médecine dès la fin de l’antiquité. L’Europe médiévale est celle du moyen
âge. Le moyen âge occidental est l’époque de l’histoire située entre la fin de l’antiquité et le début de
l’Époque moderne, soit grossièrement entre 500 et 1400 ans après Jésus-Christ. Cette époque s’étend sur
une période d’environ mille ans. De cette période à maintenant, nous allons passer en revue les types de
médecine. Il a existé une médecine antique [162] [208] ou empirique devenue par la suite traditionnelle. De
cette dernière, notamment la MT [150], sont dérivés tous les autres types de médecines grâce à la recherche
fondamentale, expérimentale, et scientifique comme le montre la figure 2.3.
Nous avons ainsi l’évolution chronologique des grands courants de la médecine de l’humanité à travers
la figure 2.3, où le sens de la flèche indique deux éléments à savoir :
– l’évolution des courants de médecine dans le temps ;
20

--- page 41 ---
Figure 2.2 – Déterminants ou facteurs de l’état de santé humain des plus englobants aux plus spécifiques
Figure 2.3 – Grands courants de l’évolution de la médecine de l’humanité
21

--- page 42 ---
Figure 2.4 – Quatre grandes époques marquantes de la médecine de l’humanité
– un courant de médecine donné s’inspire d’un autre courant juste le précédant.
Néanmoins quelques relents ou traces d’inspirations existent en gros entre tous ces courants.
Il convient de noter le caractère persistant et transcendantal dans le temps et l’espace, de la MT, depuis
l’antiquité jusqu’à nos jours. Nous mentionnons cela, car les actes administratifs plus tard après les indé￾pendances africaines pour la reconnaissance de la MT, existent. L’amorce d’intégration de cette médecine
dans les systèmes de santé nationaux sont récents (environ 20 ans après 1978, l’année de proclamation de
la conférence internationale d’Alma-Ata).
La figure 2.4 donne une illustration de l’évolution temporelle des civilisations marquée par les quatre
dernières grandes époques : Antiquité, Moyen âge, Époque moderne et Époque contemporaine. Cette
illustration est en rapport avec les courants de médecines du passé et de maintenant (voir figure 2.3).
Comme le montre la figure 2.3, des mutations de courants thérapeutiques vont s’observer beaucoup
plus rapidement dès la fin du moyen âge et donc à l’entame de l’époque moderne. Ce constat est justifié par
le développement de nouvelles ramifications de courants dénotées par les médecines moderne, scientifique,
complémentaire et de haute technologie.
Exceptées la médecine antique et celle du moyen âge, tous les autres types de médecine sont actuelle￾ment en usage. Cela correspond à la partie marquée par l’entour plus épais en couleur noire (voir figure
2.3). Dans cet enclos et au même titre que la MT, les autres courants de médecine peuvent être dupliqués.
La duplication faite de la MT se justifie par l’objet que cette médecine constitue pour notre travail de
recherche. Néanmoins, il est utile de préciser que cette duplication n’est pas une copie "égalitaire" dans le
temps.
A ce titre, la notation "MT =⇒ MT" traduit implicitement deux états de la MT. Elle est explicitée
à travers :
E1(t1, MT) =⇒ E2(t2 , MT) où E1 et E2 sont deux états de la MT respectivement aux dates (périodes
ou époques) : t1 et t2 .
Ainsi, s’ajoute aux significations du sens de la flèche sus-citées, celle traduisant le temps qui court.
L’implication récursive d’un courant de médecine à lui-même n’est qu’apparente. A deux dates très dis￾tantes, éloignées ou séparées (e.g : d’au moins une trentaine d’années), un courant ne peut observer ou
conserver le même état. D’une date à une autre, l’état d’un même courant de médecine a forcément changé
par le fait de facteurs liés à la nature, à l’action anthropique, à l’intelligence et à l’innovation, à l’ingéniosité
et à l’ingénierie des acteurs (humains).
Cette succession chronologiquement des quatre dernières périodes de l’histoire est partagée par la
22

--- page 43 ---
plupart des historiens français 2
.
Nous notons que la MT chinoise (MTC) n’est pas occidentale. Elle fait donc partie de la MT telle que
décrite dans ce paragraphe.
Relativement à ce chapitre, dans ce qui suit, la MT que nous décrivons le plus est celle de l’Afrique et
singulièrement celle de l’Afrique de l’Ouest.
2.4 Traits caractéristiques de la MT
2.4.1 Comparaison des connaissances natives et occidentales
Plusieurs auteurs [51] [178] [244] ont montré l’intérêt de la collaboration entre la science occidentale
(modern and western knowledge) et les connaissances natives locales ou indigènes (traditional knowledge).
Ces connaissances locales sont plus marquées dans les pays en développement des sphères africaine, asia￾tique ou aztèque (voir tableau 2.2). La MT correspond à des connaissances natives locales et la MM à la
science occidentale moderne.
Les sciences modernes (orientées occidentales) et les savoirs autochtones (locaux) représentent des
systèmes de connaissances différents, en raison de leurs antécédents et fondements, de leurs valeurs, de
leurs principes d’organisation, des habitudes d’esprit des détenteurs de ces connaissances. A cela, on
pourrait ajouter les compétences et procédures des acteurs (communautés d’acteurs), des environnements
contextuels respectifs. En plus, il bon de savoir comment de chaque côté, c’est dire d’une communauté à
l’autre, la connaissance est utilisée.
L’ultime défi est de trouver la reconnaissance mutuelle et le respect de travailler ensemble de manière
complémentaire pour améliorer le bien-être de notre humanité et le développement durable de la planète
entière. L’entrée de l’ensemble des pays dans les sociétés du savoir ne doit pas être une recommandation
vaine. De cette façon, assurément, les approches scientifiques contemporaines s’augmenteraient avec une
vision plus globale incluant à la fois les dimensions spécifiques d’ordre psychologique, sociale et culturelle,
auparavant considérées comme extérieures à la logique scientifique [244].
2.4.2 Caractéristiques propres à la MT
Dans notre approche de recueil de données et des informations, nous avons constaté que certains
tradipraticiens de grande renommée voilent à peine leur détermination à mourir avec leur secret [10].
D’autres PMT veulent une transmission des savoirs par lignée. Le manque de confiance et d’acceptation
mutuelle entre PMT est également avéré.
Vu le caractère fortement tacite, natif [114], implicite et caché de la MT, nous avons réalisé des activités de
sensibilisation d’au moins cinquante (50) PMT en terre ivoirienne pour plus d’ouverture et leur adhésion
au projet. Le responsable du PNPMT 3 a eu un rôle de facilitation à Abidjan (capitale économique de la
Côte d’Ivoire).
Dans ses principes de soins en santé humaine, la MT aborde les dimensions morale, culturelle, sociale
et environnementale du patient. On parle alors de bien-être intégral [22].
2. http ://fr.wikipedia.org/wiki/Antiquité, 2013
3. Programme National de Promotion de la MT
23

--- page 44 ---
Connaissances natives locales
(indigenous knowledge)
Connaissances de la science moderne
axée occidentale (modern and western
science knowledge)
Frontière
géographique et
culturelle
Connaissances locales : Elles sont enracinées
dans une communauté particulière ; C’est un
ensemble d’expériences générées par des
personnes vivant dans les communautés.
Connaissances universelles et globales :
Produites dans les institutions scientifiques
modernes et certaines entreprises
industrielles, elles transcendent les limites
géographiques terrestres. Ce type de
connaissances a la même "vérité universelle"
peu importe où il se trouve.
Degré de
désincarnation
Connaissances tacites : connaissances
indigènes sont intégrées et incarnées dans les
personnes qui les génèrent et les utilisent ; Il
est donc difficile de saisir et de codifier ce
type de connaissances non formelles.
Connaissances explicites : Les connaissances
résultent de procédures rigoureuses de
création par l’observation, l’expérimentation
et la validation ;
Ces procédures pourraient être spécifiées et
mises facilement en instructions stratégiques
ou opérationnelles
Moyen de
transmission
Transmission orale des connaissances : les
connaissances sont rarement enregistrées sous
forme écrite. Elles sont transférées par
imitation ou démonstration.
Transmission orale, écrite, scolaire et
académique : Comme la connaissance est
produite et soigneusement documentée, elle
peut être enseignée par le système éducatif
formel.
Niveau théorique
et expérimental
Par expérience : les connaissances sont
dérivées de l’expérience et de l’essai et de
l’erreur. Il est testé au fil du temps dans le
"laboratoire social de survie" des
communautés locales.
Méthode scientifique, théorique,
expérimentale, formelle et mathématique : La
connaissance est dérivée d’hypothèses et de
méthodes scientifiques. Des études ont été
faites dans des laboratoires ou avec des
modèles scientifiques ou mathématiques.
Marque
spirituelles
et sociales
Connaissances empreintes de valeurs sociales
et spirituelles : La spiritualité est d’une
dimension importante et inséparable des
connaissances. La subjectivité joue un rôle.
La nature est vénérée comme la mère et la
fournisseuse de toute chose et de tout être.
Absence de valeurs spirituelles : Les
attitudes, les croyances et les dimensions
culturelles sont séparées du processus de
création des connaissances. L’objectivité est
l’approche essentielle. La nature doit être
conquise et/ou maitrisée.
Niveau d’approche
systémique
Approche holistique et globalisante :
L’humanité est considérée comme faisant
partie de la nature.
La tendance naturelle pour l’équilibre est le
thème central de la connaissance.
Approche systémique et comparative : Ce
système de connaissance décompose la
matière pour étude en plus petites
composantes afin d’atteindre la profondeur et
la partie cachée des faits du sujet étudié.
Niveau de partage
communicationnel
Très faible partage des connaissances :
connaissances éparpillées mais individualisées
et sectaires par communautés clés ou par
familles ou par personne, et ce des années
durant.
Grande ouverture et partage à l’échelle :
communication grandement ouverte
(révolutions et progrès industriels, TIC-web,
universités), partage des connaissances,
davantage de volonté d’ouverture et de
partage.
TABLEAU 2.2 – Comparaison des connaissances modernes et traditionnelles
24

--- page 45 ---
La MT est souvent à l’origine de découvertes en MM (médecine conventionnelle) [49]. Cela passe par
l’analyse des principes actifs présents dans les plantes utilisées pour les remèdes (pharmacognosie) [196]
[214].
En MM, la majorité des médicaments sont des produits de synthèse obtenus souvent suite à une longue
chaîne de production jonchée d’activités scientifiques (biologie et principes actifs des plantes médicinales,
adjonction d’excipients). Les fonctions de médecin et de pharmaciens sont distinctes, exercées par des
corps de métiers afférents différents même s’ils doivent travailler de manière concertée. La biomédecine
s’est émancipée depuis longtemps de la religion.
En MT, le mode opératoire de la prise en charge d’un patient est différent de celui de la MM ; le PMT
exerce à la fois les fonctions de "médecin" et de "pharmacien" [136]. Il détecte la maladie sur le patient
et le traite en lui administrant les soins sous forme de recettes ou de remèdes appropriés, et ce, quelques
fois extemporanément surtout pour la première des quatre catégories (I, II, III et IV) de médicaments
traditionnels (à base de plante) [13] toujours au stade de recommandation OMS. Il lui revient donc de
confronter les symptômes (relevés) du patient et de les comparer aux signes de la maladie explorée. A ce
type de diagnostic, il rajoute un autre d’ordre métaphysique (ou invisible) en plus de certains déterminants
socio-culturels et environnementaux [22]. La prescription du PMT est à l’état de recette (d’ingrédients,
...) en général, même pour les remèdes dits MTA.
L’échange entre patient et PMT est bidirectionnel, se démarquant nettement de la position dominante
ou de tout puissant du rôle de médecin moderne [133]. En somme, la MT vise un traitement holiste et
exhaustif du patient (corps physique, âme ou l’esprit, environnement social et culturel). Une des carac￾téristique de la MT est ainsi sa connexité intrinsèque et extrinsèque avec le social et le culturel. La MT
reste encore inféodée aux croyances religieuses (Dieu des païens, Christianisme et Islam, ...) [83].
La MT se voit comme dernier recours pour la grande majorité des cas où les symptômes du patient
persévèrent après l’intervention achevée de la MM [83].
Le concept de maladie en Afrique est approché de manière globale. Ce n’est pas l’approche plus
spécifique de l’occident. Cette approche globale se base essentiellement sur la sensibilité et la pensée
consciente des adultes plus imprégnés d’animisme [201]. La maladie reconnue comme un dérèglement
d’une ou de plusieurs parties du corps humain, est selon les sociétés africaines, un désordre, un déséquilibre
qualitatif et quantitatif entre toutes les composantes de l’Homme [133].
Les concepts surtout relatifs aux ressources médicinales, matériels de travail du PMT, sont primitifs.
Ces ressources sont utilisées dans leur naturalité sans subir de transformations véritables comme le fait
par le moyen de plusieurs procédés successifs en MM.
Parmi les PMT, l’on constate plus de personnes âgées et une dominance du genre masculin sur le
féminin au regard des listes que nous avons établies des PMT (au Sénégal et en côte d’ivoire) lors des
visites de terrains. Au Burkina, c’était purement par observation lors d’un bref séjour.
Une femme PMT en général travaille avec son mari.
Au regard de ce qui précède, entre MM et MT, les modes opératoires sont différents. Ceci rend difficile
la réutilisation diligente et automatique des ontologies ou des ressources terminologiques et ontologiques
(RTO) existantes en MM pour notre conception en MT. En conséquence les ontologies de fondement
pourraient servir de modèles de données dans nos constructions futures. En outre, selon Kepler J (1543,
gravitation autour du soleil) et Newton I (1687, mouvement de corps), le modèle a été vu comme lois et
comme principes respectivement. En tant qu’abstraction de la réalité, il est plus vu de nos jours comme
un moyen de production et d’exposition de connaissances [146].
25

--- page 46 ---
2.5 Organisations
2.5.1 Acquisition et transmission des connaissances et savoirs de la MT
La MT est un ensemble de savoirs et de savoir-faire, acquis par l’observation et l’expérience pratique,
transmis de génération en génération par voie orale, rarement par écrit. De façon fonctionnelle, il faut
considérer l’art traditionnel de soins, comme un ensemble de connaissances empiriques, acquises par l’une
des voies suivantes :
– par la famille (lignée ou descendance) [133] [136] : père à fils (fille), ou de mère à fille (fils), par les
relations d’alliance : belle-mère, beau-père, beau-frère, belle-sœur, mari, co-épouse, marâtre, etc ;
– par apprentissage de plusieurs années auprès de guérisseurs compétents, en dehors du cercle familial
[136] ;
– par l’achat d’une recette jugée efficace après le traitement d’une affection donnée [136] ;
– par la promotion des personnes prédisposées dans des écoles (rares) des traditpraticiens de santé ;
– par le fait d’avoir été ancien malade guéri par un remède traditionnel ou dont le mal a été atténué
(apaisé) par un remède traditionnel ;
– par innéisme (dans ce cas, on parle de transmission par les esprits bienveillants) [72].
– par observation de comportements d’animaux domestiques ou non, et dans un champ plus large par
observation de phénomènes biologiques de la nature (plante, rapport entre animaux souffrants et
plantes). Par exemple, dans son cheptel, l’observation régulière des bovins faite par le peule (peul,
peuhl ou peuhle ) [15] [123] lorsque leur santé n’est pas au beau fixe ou dans leur état maladif ;
– etc.
Certains citadins ou personnes d’une certaine aisance, ancrés totalement dans la modernité occidentale,
ayant bien évidemment abandonné les coutumes africaines éprouvent des difficultés liées à la honte à aller
se faire traiter à la MT au grand jour, surtout lorsqu’ils n’ont pas eu de satisfaction avec la MM. Ainsi,
ils font recours à la MT "à la sauvette", par la contrainte du mal dont ils souffrent.
2.5.2 Ressources médicinales
Il existe quatre sources principales de produits médicinaux traditionnels : végétales, animales, minérales et
magico-religieuses (métaphysiques). Plusieurs sources écrites et nos visites chez les PMT confirment cela
et nous permettent de mettre sous écrit ce qui suit.
– Les produits minéraux [133] d’usage courant en MT sont le sable, l’eau, la limaille de fer, le kaolin,
la terre des termitières et des guêpières.
– Quelques animaux les plus couramment utilisés en MT sont :
-les reptiles (crocodile, tortue gecko ou lézard, varan, caméléon, margouillat, ver de terre, vipère,
boa, python 4
),
-les volailles (pintade, poulet, canard, pigeon, ...) [133],
4. Le terme python est également utilisé comme un langage de programmation en informatique
26

--- page 47 ---
-les mammifères [150] (singe, chèvre, mouton, antilope, lion, panthère, buffle, gazelle, éléphant, pan￾golin, rhinocéros, lion, tigre, panthère, écureuil volant, cerf).
-les oiseaux (pigeon, tourterelle, tisserin, calao, touraco, coucal du Sénégal, francolin, aigle, figrette
garzette, héron garde bœuf, milan noir, ombrette africaine, cisticole, hirondelle, martinet, engoulevent
à longue queue, hirondelle, caille, effraie des clochers, petit-duc à face blanche, faucon lainier, baza
coucou, épervier de hartlaub, autour unibande, élanion blanc, ...), selon Koué et al [134].
- les autres : araignée et certains insectes, mollusques et crustacés (escargot ..), certains poissons
(huile), mille patte, ...
Il faut noter qu’il existe des animaux à la fois reptiles et mammifères.
Selon KOUE et al [134], quarante quatre (44) espèces aviaires issues de seize (16) familles d’oiseaux
de huit (8) ordres sont souvent utilisées dans la MT, par le peuple Gouro en Côte d’Ivoire.
Comme le nom scientifique ou botanique des plantes, celui des animaux existe et suit une classifica￾tion similaire relevant du règne animal.
Nous avons également l’usage courant de parties d’animaux (notamment les dents, la carapace,
le coquillage, les griffes, les cornes, la queue séchée, les plumes, les écailles, les sabots, la peau
sèche, le pelage, le sang) ou de ressources d’origine animale (miel, graisse, lait, œuf, toile d’araignée,
excrément, huile animale).
– Les ressources végétales notamment les plantes constituent de loin le lot le plus important et imposant
de l’ensemble des recettes thérapeutiques traditionnelles. Nous faisons ici l’économie de détailler les
espèces végétales utilisées, étant donné qu’elles sont les plus diversifiées et les plus utilisées en MT.
Nous sélectionnerons au chapitre 6 un échantillon de 22 plantes médicinales anti-paludéennes pour
l’amorçage de notre langage iconique.
Presque toutes les parties de la plante médicinale sont utilisées : feuilles, racines, écorces, tiges et
tronc, bourgeons, sève, épines, fleurs, fruits, tubercules, graines et pépins. Ces parties sont préparées
à l’état frais ou à l’état sec.
Exploitées habituellement à partir des peuplements sauvages, les plantes médicinales ne sont cultivées
par les guérisseurs que lorsqu’elles deviennent rares ou pour répondre aux cas d’urgence [136].
– Les ressources surnaturelles, magico-religieuses ou métaphysiques ne sont abordées.
2.5.3 Récolte des ressources médicinales
La récolte des organes des végétaux, des animaux ou des minéraux peut se dérouler au sein, à proximité
ou loin du village (valable pour un site urbain). Elle peut avoir lieu en pleine brousse (savane, forêt, cours
d’eau). La plupart des récoltes de plantes par les PMT sont réalisées au fur et à mesure de la demande
ou des besoins. Il en est de même des autres ressources médicinales. Certains PMT récoltent une grande
quantité de ressource (par exemple les plantes) qu’ils utilisent jusqu’à épuisement [136] du stock. On peut
noter que les dispositions particulières (normales) de conditionnement et de conservation sont rarement
prises.
Les récoltes peuvent se faire à des heures particulières (à l’aube crépusculaire, midi, minuit, à la rosée
matinale, ...) de cueillette. Elles peuvent se faire de jour comme de nuit. Il peut arriver que pour certaines
récoltes et surtout pour les plantes que des dispositions particulières soient observées : attitude de celui qui
fait la récolte depuis la veille, pendant la récolte savoir se tenir en terme d’orientation (points cardinaux,
soleil ou lune).
27

--- page 48 ---
2.5.4 Forces et faiblesses de la MT
Ces forces et faiblesses sont relevées des descriptions analytiques de la documentation mais également
des observations sur le domaine de discours.
2.5.4.1 Forces
À partir de la bibliographie [14] [22] [49] [133] [136] [178] [238] et des observations menées, nous
dégageons un certain nombre de forces de la MT :
– proximité géographique : Il n’y a pas de localité rurale sans MT. Il existe toujours un PMT au sein
d’un village ou juste à sa proximité. Au niveau urbain, on trouve quelques PMT plus concentrés aux
abords des marchés. La MM demeure essentiellement urbaine ;
– proximité et accessibilité culturelles : La MT fait partie intégrante de la culture africaine. Elle est
étroitement liée au contexte socioculturel et aux convictions métaphysiques d’une population locale.
Le guérisseur et son patient partagent les mêmes modes de vie, le même contexte social, le même
langage et les mêmes conceptions étiologiques. Le guérisseur est parfaitement intégré dans le milieu
social où il exerce. De plus, le PMT est très souvent agriculteur. Il vit au rythme des travaux agricoles
et partage les préoccupations de ses malades. Le guérisseur prend parfois les malades en charge à son
domicile ou à proximité de son domicile (hospitalité remarquable au niveau rural). Par conséquent
le patient est plus réceptif aux consignes du PMT ;
– caractère naturel des substances : Les PMT puisent directement dans la nature les médicaments
auxquels ils ont recours. Les excipients sont très négligeables ou eux-mêmes naturels également.
Ce qualificatif pourrait s’étendre aux liants, apaisants, adjuvants, conservateurs, colorants, arômes,
épices, ... ;
– moins d’effets secondaires : La MT produit moins d’effets secondaires que la MM. Les médicaments
sont naturels. Il y a même des usages extemporanés de remèdes traditionnels ;
– niveau populaire de prise en charge : Chaque habitant rural connaît les vertus thérapeutiques d’une
plante. La connaissance des plantes médicinales fait partie de la culture populaire. Des plantes pour
soigner certains maux légers sont connues de manière populaire. On parle de médecine populaire
traditionnelle ;
– coûts des soins de santé accessibles (abordables) : Le coût des traitements est modeste, abordable et
à la portée de tous. La souplesse des modalités de paiement est un paramètre crucial. Souvent la MT
ne nécessite pas d’achat d’ordonnances ; Dans certaines localités, le patient doit faire un don ou un
rituel suite à sa guérison ; Ceci n’est pas le cas en MM plus couteuse, même avec des consultations
payantes depuis 1994 pour la plupart des pays d’Afrique noire. La MM est moins accessible par
l’ensemble des couche sociales ;
– médecine holiste : La culture africaine considère l’homme comme un tout indivisible intégrant le
cosmos, la matière et l’esprit. L’équilibre humain est la résultante de facteurs d’influences réciproques
entre le corps physique, l’esprit , les croyances et l’environnement familial (et communautaire) ;
– MT plus efficace sur certaines maladies : Certaines maladies sont rapidement traitées notamment le
paludisme, les plaies de ventre, les hémorroïdes, la stérilité, l’impuissance sexuelle, la maladie de la
fontanelle (bébé) . . . ;
– traitement des maladies mystiques : La MT traite des cas des maladies mystiques non accessibles à
la MM (jet de mauvais sort, sorcellerie, crétinisme cérébral, débilité mentale, certaines folies) ;
28

--- page 49 ---
– encadrement psychologique : La MT pallie aux insuffisances de la MM sur le plan de l’encadrement
psychologique. Le patient est également entouré par le soutien familial ;
– Médecine préventive ;
– recrudescence de publications scientifiques [132] (Biosciences et ethnobotanique) ces deux derrières
décennies, sur l’utilisation en soins de santé primaires de la MT en Afrique en particulier et dans le
tiers monde en général.
2.5.4.2 Faiblesses
Plusieurs insuffisances de la MT sont notoires dans la bibliographie [14] [51] [133] [136] et également,
de nos observations durant les visites effectuées auprès des PMT dans leur art de traitement des patients.
Au nombre de ces faiblesses, nous avons constaté celles-ci :
– Mesures de dosage et posologie approximatives : il y a une insuffisance de mesure d’appréciation des
quantités tant au niveau des préparations des recettes qu’à celui de l’administration des remèdes ;
– Non respect scrupuleux des règles d’hygiène lors du conditionnement et de la conservation des
produits de la MT ;
– Faible contrôle des effectifs des PMT : Il y a un nombre élevé de faux PMT, de charlatans, de faux
médicaments. Le nombre incontrôlé de PMT résulte d’un faible niveau organisationnel de la MT en
général ;
– Existence d’effets secondaires des thérapies traditionnelles : il arrive que les effets secondaires ne
soient pas connus. Certains effets peuvent faire émerger des cas de complication graves ;
– Diagnostic approximatif car souvent non clinique : la rigueur de mesure de la MM est ici absente ;
– Danger relatif au jet de mauvais sort par la pratique du fétichisme : Dans certains cas, à travers le
caractère mystique de la MT, des PMT ont la capacité de faire le mal en jetant des mauvais sorts.
– Amertume et/ou senteur nauséabonde de certains remèdes : L’amertume et le relent de certains
remèdes proviennent des plantes ayant servi à les obtenir. Cet état de fait rend difficile la prise de
certains médicaments traditionnels ;
– Préparation des médicaments parfois contraignante : La préparation de certaines recettes peut s’avé￾rer complexe et pénible (écraser les plantes, les faire bouillir pour l’obtention des décoctions) ;
– Absence de règlementation et de contrôle de la MT pour régir les actes médicaux traditionnels :
bien qu’il existe une amorce de règles d’éthiques normatives (milieu urbain et rural) et de sanctions
(Côte d’Ivoire, Sénégal, Burkina Faso, Mali, Ghana, Togo, Bénin, ...) ;
– Manque de maitrise de la toxicité de certaines plantes : Certaine parties potentiellement toxiques de
plantes médicinales ne sont pas totalement supprimées ;
– Inefficacité de certains traitements : Quand la maladie n’est pas bien identifiée à travers ses signes et
les symptômes du patient, on arrive souvent à des traitements inefficaces. Il y a également le manque
de spécialité fortement reconnue ou de discipline où excelle le PMT ;
– Absence de plateau technique : il est difficile de définir un plateau technique à l’instar de celui de la
MM ;
– Pratique de l’avortement avec risque de complication : Pour avorter, des plantes sont utilisées avec
l’imprécision de dosage. Ce qui relève le niveau de risque ;
29

--- page 50 ---
– Absence ou rareté de chirurgie en MT : Les maladies, notamment celles nécessitant une chirurgie,
ne sont pas traitées couramment par la MT ;
– Insuffisance de formation des PMT : les instituts ou écoles de formation des PMT sont rares jusque￾là ;
– Iatrogénie : Il existe des erreurs de diagnostique et de traitement thérapeutiques au niveau du PMT.
Des erreurs médicales commises par le patient existent aussi ;
– Absence de précautions ou manque de rigueur dans l’observation des précautions propres à la consom￾mation de remèdes de MT issus de la phytothérapie [14]. Ce constat ressort d’une majorité écrasante
de personnes interrogées (159/200) par Konan [133] ;
– Existence de pratiques médicales secrètes de la MT : Elles engendrent souvent des erreurs médicales
(iatrogénie) ou non : Il peut arriver des cas où les interrogations ou/et dialogues bidirectionnels ne
soient pas tenus ;
– Manque de communication, de partage des connaissances et expériences entre PMT : l’absence de
partage des connaissances médicales traditionnelles est notoire. La transmission est amplement orale
sans possibilité de capitaliser ces savoirs traditionnels. Le mode de transmission très oral de l’art de
la MT ne constitue pas un gage de garantie pour son exercice par les générations futures ;
– Acquisition (ou apprentissage) de la MT non ouverte à tous : Elle est faite par lignée, par innéisme.
Les écoles en la matière, sont en nombre très insignifiant ( une (1) à l’est de la Côte d’ivoire, une
(1) au Sénégal ) ;
– Perte et disparition du patrimoine socio-culturel fondé sur les savoirs et connaissances en MT : A
la mort d’un PMT, c’est tout un ensemble de connaissances, de pratiques et d’expériences profes￾sionnellement accumulées durant son vécu, qui disparait. La relève de ce patrimoine culturel est
faible ;
– Absence de date de péremption des produits remèdes traditionnels et celle de la distinction de sexe
accompagnée de la non précision de l’âge ou de la tranche d’âge.
– impact des génériques non reluisant : Depuis l’avènement du générique, on note des saisies multiples
et fréquentes de faux médicaments, nuisant également la réputation des médicaments traditionnels
reconnus ;
– Manque ou insuffisance de référence (ou référencement) à une autre entité soignante (PMT ou
praticien de la MM) : Les PMT n’ont pas la culture de réorienter le malade vers des compétences
plus adéquates ;
– Réticence d’une frange du personnel de la MM à une reconnaissance soutenue de la MT ;
– Taux d’analphabétisme des acteurs PMT élevé (variant entre 65% à 80% selon le pays) 5
.
Partant de la collaboration entre les entités MT et MM distinctes, en essais pilotes dans certains
pays (Côte, Sénégal, ...) et dans l’optique de sa généralisation projetée [59] [215], il appert de nombreuses
difficultés afférentes à adresser en vue de parvenir à des solutions idoines. Au sens de [213], quelques unes
de ces difficultés sont :
– les messages contradictoires entre les différents acteurs (préjugés, dénigrement) ;
– le refus mutuel, l’intolérance, le manque de confiance réciproque et la non acceptation de l’autre ;
– le sentiment de concurrence déloyale d’un système à un autre ;
– les fortes dépendances des acteurs PMT aux croyances religieuses et culturelles ;
5. http ://uis.unesco.org/fr/news/journee-internationale-de-lalphabetisation consulté en 2017
30

--- page 51 ---
– les fondements idéologiques (avec adversité par moment) chez les médecins traditionnels et chez les
modernes de la MM ;
– l’absence de communication bilatérale entre MM et MT. Cette communication s’avère très insigni￾fiante quand elles existe ;
– l’esprit mercantile de certains PMT quand bien même les coûts sont faibles par rapports à ceux
pratiqués en MM ;
– l’absence d’un cadre définitionnel flexible et rigoureux des tâches de la MT vis à vis de la MM et
réciproquement.
Quelques unes de ces difficultés relatives à la communication bidirectionnelle et à la méfiance manifeste
au sein et à l’endroit de la MT, sont en rapport avec celles déjà précédemment relevées.
2.6 Prédisdisposition organisationnelle et solutionnelle de capitalisation
des connaissances
Au regard du tableau analytique qui vient d’être dressé, il y a lieu de renforcer certaines forces en
termes d’acquis. Les autres acquis sont à préserver. Cependant, il y a urgence à remédier aux faiblesses
de la MT en proposant des solutions idoines. Ce travail de recherche, sans prétendre apporter toutes les
solutions, espère à travers son centre d’intérêt scientifique, contribuer à l’augmentation des offres de soins
de santé primaires pour la population. Il s’agit principalement de disposer d’un fond organisationnel des
connaissances de la MT. Ce dispositif est soutenu par l’élaboration d’une ontologie formelle à intégrer
dans une plateforme web sémantique d’échange entre acteurs surtout principaux pour le partage de leurs
connaissances et expériences de l’art de guérir par la MT. Il faut ajouter à l’ontologie formelle termino￾logique, une autre d’approche visuelle à partir de laquelle nous construisons un langage iconique dont se
servira la communauté entière des PMT de l’Afrique de l’ouest. Un tel langage transcende le multilin￾guisme accentué de cette partie d’Afrique et le caractère très dominant de l’inaptitude à lire et à écrire des
PMT. A terme, ce fond organisationnel plus qu’une mémoire pourra constituer un outil de pérennisation
de l’exercice de l’art médical de la MT.
De la traduction en lettre de nos réflexions, devra résulter un outil relevant des TIC à même de contri￾buer à l’amélioration organisationnelle de la MT en matière de gestion, de sauvegarde et de capitalisation
des connaissances. Ceci débouche sur deux visions parallèles et salvatrices.
D’une part, il faut sauvegarder les connaissances, les savoirs et les expériences de la MT en mettant en
place un fond organisationnel de la mémoire supporté par les technologies du web sémantique. Ce cadre
d’échange et de partage des connaissances pour les PMT doit prendre en compte leur statut majoritaire￾ment illettré. Globalement, cette solution permettra aux générations futures de PMT de disposer de ces
connaissances et également de les enrichir.
D’autre part, vu que la matière première du PMT est constituée de ressources végétales, minérales et
animales, ce fond organisationnel pour la pratique de l’art de guérisseur traditionnel prend tout son sens
si ces mêmes ressources ne disparaissent pas de l’environnement naturel. Ce qui signifie que ces ressources
sont préservées, pérennisées et disponibles pour être utilisées dans l’exercice du PMT. Plus simplement,
considérées comme matériel de base du travail du PMT, ces ressources doivent continuer d’exister. In
fine, les connaissances sauvegardées en mémoire machine ou au niveau humain par différentes techniques
d’acquisition ou d’apprentissage n’auront de sens véritable que si on peut les appliquer effectivement et
ce de façon durable. Cette application effective nécessite donc que le matériel vivant de la nature soit
31

--- page 52 ---
préservé.
Ce sont là deux visions qui permettent de véritablement pérenniser de génération en génération l’art du
guérisseur. Cependant, la sauvegarde en terme de préservation des espèces de la faune et de la flore centrée
sur ces ressources médicinales n’est pas l’objectif poursuivi dans cette thèse. Ce travail se concentre sur la
première vision se rapportant au cadre d’échange entre PMT via les TIC et principalement les ontologies.
Il s’agit globalement du fond organisationnel de mémoire des connaissances et pratiques de la MT en vue
de les pérenniser et les utiliser.
2.7 Synthèse
Au fil des années, la MT africaine connaît une évolution certaine mais jusque-là considérée comme
faiblement positive au regard du progrès net de la MM (opération laser, chirurgie à distance via les TIC,
..). L’état de l’art de la MT, axé sur les faiblesses de celle-ci, n’est pas en marge de cette assertion.
En matière de santé, le regain d’intérêt suscité en MT, est le fait en partie des coûts de consultations
en soins de santé de la MM, même primaires, instaurés depuis les années 1994 en Afrique de l’ouest.
Aussi, les coûts des produits pharmaceutiques et de consultations en MM n’ont cessé d’augmenter jusqu’à
ce jour. La cherté de cette MM d’une part et d’autre part la répartition inégale par nombre d’habitants
des infrastructures de soins dans les espaces habités (métropoles, capitales, villes, communes, villages),
constituent les motifs principaux de l’inéquité d’accès à la MM par l’ensemble des couches sociales. En
plus de la croissance galopante de la population dans cette sous région ouest-africaine, la pauvreté est
manifestement accentuée. Conséquemment, une frange importante estimée à 80% des populations des
pays en développement et surtout d’Afrique [175] [210] a recours à la MT parallèlement à la MM.
Relativement à la MT africaine, de nombreux problèmes sont préoccupants, et ce, dans un environ￾nement sous régional à la fois multi-cuturel et multilinguiste. L’absence de mémoire de sauvegarde et de
partage des connaissances et expériences de la MT est l’un des non moindres problèmes. Venir à bout de
cette problématique nécessite de poser effectivement les piliers de la capitalisation et de la pérennisa￾tion du patrimoine formé par ces connaissances et expériences.
Après analyse de cette problématique, plusieurs facteurs sont à l’origine de ce manque de capitalisation.
Parmi ces derniers, les plus importants sont le caractère fortement oral de la transmission des savoirs de
cette MT et le manque de communication et d’échange entre les PMT. Au fond, la racine du problème
réside à la fois dans l’illettrisme de la majorité de ces acteurs (centraux) et le fait qu’ils s’expriment dans
des langues (locales) différentes. En revanche, en Chine, ce problème est surmonté par l’utilisation d’une
langue unique avec le même langage et la même écriture (le Kanji). Ainsi la codification des connaissances
de la MT chinoise (MTC) en savoirs, en est facilitée. De plus, de nombreux acteurs, dont les États, sont
impliqués et participe fortement à la MTC. En 1956, quatre (4) premières universités de la MTC furent
ouvertes dont une à Pékin, une à Chengdu, une à Shanghai et la dernière à Canton. Actuellement, il existe
plusieurs universités et collèges dévolus à l’enseignement des savoirs de la MTC, avec 4% des hôpitaux
dévolus à la pratique de l’art médical traditionnel [44].
Au regard des problèmes relevées, l’exercice contrôlé de la MT africaine pourrait être très bénéfique
pour les populations qui en font usage.
La construction d’un langage iconique que nous proposons, devra s’intégrer une plateforme web. Un tel
langage s’adosse sur une ontologie d’approche visuelle, ontoICONE, dans laquelle des représentations sous
formes d’icônes ou de pictogrammes, seront en correspondance avec des concepts terminologiques contenus
32

--- page 53 ---
dans une ontologie ontoCONCEPT-Term. Notre ontologie de domaine de la MT africaine, ontoMED￾TRAD renferme les deux composantes ontologiques ontoCONCEPT-Term et ontoICONE.
Dans notre travail, l’utilisation d’icônes vise à résoudre les problèmes posés par l’illettrisme et les
barrières de langues. L’utilisation d’une ontologie a pour objectif une description et une spécification plus
fine et approfondie de la MT avec la possibilité d’une sémantique formelle et d’un enrichissement continu
par les experts PMT. Avant notre apport de réponses idoines à ces préoccupations, dans les chapitres
suivants, nous allons dresser un état de l’art sur les représentations de connaissances, les ontologies et les
méthodologies de leur construction, les ontologies du domaine médical et de la MT (chapitre 3), puis sur
les représentations iconiques (chapitre 4).
33

--- page 54 ---
Chapitre 3
Représentation de connaissances et
ontologies
Sommaire
3.1 De "donnée" à "connaissance" . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.2 Représentation des connaissances . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.3 Construction d’une ontologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.4 Représentation des connaissances et ontologies existantes dans des domaines
connexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
3.5 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
34

--- page 55 ---
La représentation 1
[62] est le fait de rendre sensible en terme d’appréhension, de saisie, d’intelligence,
un objet ou un concept, même absent, au moyen d’une image, d’une figure, d’un signe, ou d’un autre objet
[101]. Il s’agit d’un processus par lequel l’on renvoie à une réalité extérieure, secondaire. La représentation
constitue un système d’interprétation des réalités du domaine du discours. Dans le monde courant et
presque dans toutes les sciences, nous avons des formes communes et d’autres très diversifiées, de la
représentation.
La représ0entation des connaissances (parfois appelée ingénierie des connaissances (IC) [58]) est une
branche de l’informatique et de l’intelligence artificielle qui vise à représenter, structurer, organiser et
formaliser les connaissances, de sorte à en faciliter l’usage par un humain mais aussi à en rendre l’utilisation
possible par une machine. Plusieurs moyens sont utilisés pour la représentation des connaissances dans le
contexte du web de données ou web sémantique. Nous pouvons citer (par ordre croissant de formalisation)
les taxonomies, les thésaurus et les ontologies. A ce titre, les ontologies constituent un support indispensable
du web sémantique. A leur tour, elles sont supportées par des logiques de descriptions.
Pour le partage communautaire, la sauvegarde et la représentation organisationnelle des informations
et des connaissances, les ontologies sont parmi les outils les plus utilisés actuellement. L’enrichissement
sémantique continu et sa formalisation dans les ontologies au moyen de langages formels de plus en plus
expressifs et décidables, permettent en particulier d’assurer des recherches d’informations ou de connais￾sances plus précises de sens et d’en diminuer le silence et le bruit. Tant qu’il est vrai que le bon compromis
entre expressivité et performance est à rechercher.
3.1 De "donnée" à "connaissance"
Données, information et connaissances sont des notions très importantes pour le fonctionnement normal
d’une organisation. Il importe alors de s’accorder sur leurs définitions. Dans la perspective des TIC, ces trois
termes sont très utilisés. Moult auteurs ont définis ces concepts : donnée, information et connaissance.
Le tableau 3.1 synthétise les contributions définitionnelles de neuf (9) auteurs au regard de [79] et [108].
3.1.1 Donnée
Souvent dans le langage courant, et même dans la littérature scientifique, "donnée" et "information"
sont utilisés comme des synonymes [93], alors que ces termes sont sémantiquement différents. Ils ne sont
pas synonymes [230]. Une donnée est un élément d’information. Atomique, elle constitue la représentation
de l’information sous forme conventionnelle en vue de son traitement par l’homme (ou par la machine).
Elle est non interprétée et non mise en contexte. "102" en est un exemple. Il a une absence de signification
particulière.
D’un point de vue sémiotique ou sémiologique, une donnée peut être considérée comme la réduction
syntaxique d’un signe [94].
3.1.2 Information
Une information est une donnée interprétée, à laquelle un sens est associé. Elle est une donnée avec une
sémantique (sens, significations) correspondante. Autrement dit la données peut être considérée, comme
la réduction syntaxique d’un signe, l’information comme sa réduction sémantique.
1. http ://daimon.free.fr/mediactrices/representations.html consulté en 2013
35

--- page 56 ---
Auteurs Donnée (data) Information Connaissance (knowledge)
Choo, Detlor, et
Turnbull, 2000
Faits et messages Données ayant une
signification.
Croyances vraies et justifiées.
Davenport, 1997 Simples
observations.
Données avec pertinence et
but.
Informations valables de l’esprit
humain
Davenport et
Prusak, 1998
Ensemble de faits
distincts.
Message destiné à changer
la perception du récepteur.
Expérience, valeurs, connaissances
et informations contextuelles
Fatimah Sidi, 2009 Texte qui ne répond
pas à la question
dans l’espace du
problème
Texte qui répond quand /
où / qui / quoi dans
l’espace du problème
Texte qui répond comment /
pourquoi dans l’espace du
problème
Nonaka et Takeuchi,
1995
Flux de messages
significatifs.
Engagements et croyances créés à
partir de ces messages.
Quigley et Debons,
1999
Texte ne répondant
pas aux questions
d’un problème
particulier.
Texte qui répond aux
questions qui, quand, quoi
ou où.
Texte qui répond aux questions
pourquoi ou comment.
Shannon (1916-2001) Message auquel est rajouté
le contexte, transmis avec
certaine une incidence
entropique (*).
Spek et Spijkervet,
1997
Symboles non encore
interprétés.
Données avec sens. Capacité d’attribuer un sens.
Wiig, 1993 Faits organisés pour décrire
une situation ou une
condition.
Vérités, croyances, perspectives,
jugements, savoir-faire et
méthodologies.
(*) : L’entropie est la mesure de l’incertitude quant à la nature d’un message (en communication). Elle
mesure le degré de désordre d’un système par rapport à son état initial probable. En thermodynamique,
grandeur qui mesure la dégradation de l’énergie d’un système au sens de CNRTL.
TABLEAU 3.1 – Quelques définitions des concepts donnée, information et connaissance par neuf (9) auteurs
36

--- page 57 ---
L’information peut être considérée comme la sémantique d’une donnée, et donc, de la réduction syn￾taxique d’un signe. "22552997923" est une donnée alors que "tél :+225 52997923" est un numéro de
téléphone à l’international.
3.1.3 Connaissance
On définit la connaissance comme ce qu’on a appris par l’étude ou par la pratique [230]. La connaissance
constitue une notion au sens unique et aux définitions multiples, à la fois utilisée dans le langage courant
et objet d’étude poussée. La connaissance est le résultat d’une réflexion sur les informations analysées en
se basant sur trois points : (1) ses propres idées, expériences et valeurs, puis sa propre expertise ; (2) le
point de vue ou avis d’autres personnes consultées pour l’occasion (contexte) et (3) l’expertise de ses pairs.
La connaissance est une information comprise et maitrisée. Elle s’intéresse à l’aspect pragmatique
d’utilité et d’utilisation de l’information donnée. Elle peut être tacite ou explicite. Sémiotiquement, elle
est assujettie à la pratique effective accordée à un signe (signifié). Elle traduit une interprétation d’éléments
factuels du monde ( discours du domaine ou domaine du discours).
Un savoir constitue un ensemble organisé de ces connaissances. Entre savoirs, nous pouvons distinguer
des savoirs théoriques fondamentaux, des savoir-faire et compétences en vue d’apporter une solution tant
au plan conceptuel qu’opérationnel (concret ou pratique).
Certaines connaissances sont subjectives et d’autres objectives [194]. Par exemple, un pianiste de re￾nommée internationale dans un opéra à Paris d’une part et d’autre part devant des indiens autochtones en
forêt amazonienne, nous laissent entrevoir, totalement opposés deux niveaux d’appréciation des connais￾sances détenues par ce pianiste. Il n’en demeure pas moins des données, informations et connaissances
afférentes à l’art de ce pianiste [79]. Nous en tirons deux conclusions : l’audience de l’opéra de Paris saura
apprécier à sa valeur le talent et les connaissances du pianiste. Ce sont des connaissances objectives. Toute
autre audience telle que celle de la forêt amazonienne ne pourra pas apprécier le talent du pianiste à sa
valeur. On parle de connaissances subjectives ou absentes.
La connaissance peut donc être couplée soit au contexte, soit aux individus concernés, ou à la fois aux
deux. Au contraire, les tautologies en logique propositionnelle sont des éléments de connaissance qui sont
toujours vrais ou toujours faux. A étant une proposition, [ (¬A → A) → A ] est toujours vraie.
Nous donnons une typologie des connaissances dans le tableau 3.2, inspiré de la littérature [199].
A ces types de connaissances, orthogonalement, nous pouvons ajouter quatre autres catégories et qui
peuvent donc être utilisées en combinaison [199] :
– Connaissance factuelle : elle est purement relative au fait du monde. Il est vérifiable par des expé￾riences et des méthodes formelles ;
– Connaissance tacite : C’est une connaissance implicite, "inconsciente", qui peut être difficile à ex￾primer sous forme de mots ou d’autres représentations ; Par exemple, le PMT (en terroir Bron ou
Abron de Bondoukou en Côte d’Ivoire) qui casse la patte d’un poulet et y pose un garrot traditionnel
avant de commencer le traitement de la fracture du pied d’un patient. La guérison du poulet sera
celle du patient ;
– Connaissance préalable (antérieure) : Elle est indépendante de l’expérience ou des preuves empiriques
évidentes. Par exemple on a : "tous ceux qui son nés en 2000 ont aujourd’hui plus de 16 ans" ;
37

--- page 58 ---
Types de connaissances Fondamentaux Description
Connaissance déclarative Concepts, objets, faits. C’est le « quoi » au sujet d’un problème donné.
Cette description inclut des déclarations
simplifiées qu’on peut affirmer comme étant
vraies ou fausses. Il en résulte une liste d’états
décrivant exhaustivement chaque objet ou
concept sous forme de triplet (objet, attribut,
valeur).
Connaissance procédurale Politique, règles, stratégies,
agendas, procédures.
C’est le comment au sujet d’un problème donné.
Ce type de connaissances fournit des orientations
sur la façon de faire quelque chose.
Connaissance heuristique Règles, astuces, métiers. Ici, la description est plus superficielle, empirique
au regard de la finalité computationnelle. Elle
provient directement de l’expert du domaine du
problème posé. Le capital descriptif tiré relève de
l’expérience de l’expert.
Méta-Connaissance Vision, connaissance sur les
autres types de
connaissances et comment
les exploiter.
Il s’agit de décrire la connaissance du savoir en
remplacement d’un champ plus étendu
notamment la connaissance de la connaissance.
Ce type de connaissance est utilisé pour choisir
d’autres connaissances qui sont les mieux
adaptées pour résoudre un problème. Les experts
l’utilisent en vue d’améliorer l’efficacité de la
résolution de problèmes, et orientant leur
raisonnement dans le domaine le plus
prometteur.
TABLEAU 3.2 – Typologie des connaissances
38

--- page 59 ---
– Connaissance postérieure : Elle est dépendante de l’expérience ou de la preuve empirique, comme
"X est né en 1990".
Le besoin humain et le but institutionnel façonnent et forment le tissu de l’organisation. Ce tissu est
incarné par donnée, information et connaissance, trilogie sur laquelle il repose également.
Remarque : Sagesse
La sagesse est un état englobant donnée, information et connaissance en un ensemble emprunt de
discernement et de jugement de bon sens. On atteint ici manifestement l’émergence des consciences. Dans
notre champ de recherche, nous nous arrêterons au niveau des connaissances, sans envisager la sagesse,
qui paraît difficile à formaliser.
De la donnée à la connaissance en passant par l’information, la sémantique des représentations est
augmentée en fonction de l’expressivité (axiomatisation et flexibilité) des langages formels utilisés avec la
possibilité d’ancrage inférentiel.
3.2 Représentation des connaissances
La représentation se veut une structure de symboles pour décrire un modèle d’une partie du monde
ou le monde lui-même dans le contexte d’une tâche spécifique. C’est une approximation ou une abstrac￾tion de la réalité. Elle ne retient que les traits essentiels de cette réalité en rapport avec l’objectivation
poursuivie et la contextualisation. Par [62], Clenet J. propose une définition générale du concept de re￾présentation : "Les représentations sont des créations d’un système individuel ou collectif de pensée. Elles
ont une fonction médiatrice entre le percept et le concept". La réflexion cognitive humaine est parsemée
d’états de représentations objectifs ou subjectifs en continu [63].
Vue à la fois comme un produit (état des idées) et comme un processus (construction des idées),
la représentation émane de l’esprit humain dans lequel elle recrée une "image complexe ou simple" de
l’environnement de l’homme. Cette représentation permet à l’homme de mieux penser et d’agir sur cet
environnement. Elle a un rôle d’une interface symbolique entre l’individu et son environnement perçu. Ces
représentations sont des modèles pouvant également être projetés dans des machines pour application.
Par représentation des connaissances (RC), on entend un ensemble de procédés, de techniques et
d’outils destinés à acquérir et à organiser le savoir humain ou naturel, pour ensuite l’utiliser et le partager.
Cela inclut également le transfert des connaissances d’un expert d’un domaine donné vers un ensemble de
machines pour les mêmes buts d’utilisation et de partage. L’un des formats importants de la RC est le
texte intégral relevant des indexations manuelles et cognitives à celles automatiques.
Toute représentation lorsqu’elle implique des connaissances, elle aide à tirer des inférences, des conclu￾sions, des déductions et est soumise à un raisonnement intelligent. Un tel système de RC implique une
combinaison de structures de données et de procédures d’interprétation qui, si elles sont correctement
utilisées dans un programme, permettront de prédire, d’inférer, de déduire et de conclure.
En somme, nos modèles de représentation doivent avoir un niveau de stabilité suffisant pour être
efficace. Pour cela, il faut éviter la variabilité notoire et les ambiguïtés d’interprétations. Il nous faut alors
lier la syntaxe formelle à la sémantique formelle via l’interprétation (dénotations, monde des possibles,
manifestations, étants).
39

--- page 60 ---
Figure 3.1 – Sémantique et implication inférentielle sur énoncés en représentation des connaissances
L’organisation des objets du monde en catégories constitue une part indispensable de la RC. En grande
partie, les raisonnements se fondent sur les catégories à travers les informations qui leur sont spécifiques,
bien que toutes les interactions portent sur des objets individuels. Cette organisation catégorielle du
domaine de discours passe par la réification du monde. Cette réification consiste à tout considérer comme
« chose ». Par exemple la couleur verte d’un objet, sa peau lisse, sa forme ronde, son diamètre approchant
les 30 cm, sa chair rouge, ses pépins noirs et sa présence au rayon des fruits permettent d’inférer qu’il
s’agit d’une pastèque, et qu’elle pourrait être utile pour réaliser une salade de fruits [225].
Idéalement, une bonne représentation doit apporter une réponse ou une résolution presque immédiate,
valide et cohérente du problème pour lequel elle est conçue. Elle doit donc être transparente, concise,
complète et doit permettre un accès rapide à l’information, selon une démarche procédurale.
Une représentation doit être fondée sur quatre aspects :
– lexical (syntaxe) : quels sont les symboles autorisés pour représenter objets et relations ?
– structurel : quelles sont les contraintes d’arrangement de ces symboles ?
– procédural : comment créer et modifier l’information ?
– sémantique : comment associer un sens aux descriptions formelles ?
En conséquence, un langage de RC pour répondre véritablement aux préoccupations de formalisation,
de manipulation, d’inférence et de prédiction doit comprendre ces quatre éléments. Le langage est composé
de symboles permettant de traduire les faits et les opérations sur les faits pour engendrer d’autres faits.
Relativement au formalisme, la sémantique repose sur un système déductif ou calculatoire. En plus, elle
joue un rôle double. Précisément, elle incarne une relation bidirectionnelle de sens ou de signification, no￾tamment du décrit (interprétés, objets, référents, individus, monde, domaine du discours) vers le décrivant
(syntaxe, représentant, formalisme) et réciproquement. Nous donnons une illustration de la sémantique et
de l’implication inférentielle en RC à travers la figure 3.1.
Après la RC, une seconde étape consiste à utiliser les connaissances formalisées dans un système
opérationnel. Pour y parvenir, Bachimont [27] prône certains engagements (explicités en section 3.2.11.1)
qui sont plus que nécessaires.
40

--- page 61 ---
FOL : First order logic
RDF(S) : Resources description framework (schema)
KL ONE (Well known knowledge representation system) dans la tradition des Réseaux sémantiques et Frames.
Figure 3.2 – Aperçu chronologique sur les outils et langages pivots conjointement utilisés pour la repré￾sentation des connaissances et ontologies
Divers moyens s’appuyant sur des méthodes, des technologies et des techniques, existent pour re￾présenter les connaissances. Il faut entendre par là, toutes sortes de schémas d’organisation partant des
simples listes alphabétiques ou faiblement structurées (listes d’autorité, glossaires, dictionnaires, nomen￾clatures, RAMEAU 2
, etc.) [195] [237] à des schémas classificatoires hiérarchiques (plans de classement,
classifications générales ou spécialisées, taxinomies, etc.) [11] [116] [152] [153] [189] [237] ou encore à des or￾ganisations incluant des relations non-hiérarchiques (thésaurus, réseaux sémantiques, ontologies, etc.)[30]
[36] [63] [64] [69] [76] [182] [224] et frames [26] [63] [182] [224], portant sur toutes sortes d’objets allant
des documents au sens classique du terme (textes, images fixes et animées, enregistrements sonores, etc.)
jusqu’à l’ensemble des phénomènes concrets ou abstraits (objets, évènements, processus, etc) et avec des
buts et des objectifs diversifiés notamment : retrouver, enseigner, produire de nouvelles connaissances,
communiquer, découvrir des connaissances cachées ou implicites, appliquer des traitements spécifiques et
appropriés, ou ad hoc etc [195].
C’est dans les années 1970 [26] qu’ont été développées les premières approches de RC, selon deux
branches distinctes notamment les représentation à base logique et celles à base non logique.
Les premières sont fondées sur une formalisation à base logique pour capturer et désambiguïser les
faits du monde. Les logiques de descriptions (LDs ou DLs) constituent une variante, un sous ensemble ou
encore un fragment décidable [121] [122] de la logique de premier ordre (logique des prédicats ou calcul
des prédicats). En particulier, les DLs se limitent à des relations unaires ou binaires alors qu’en logique de
premier ordre l’on a des relations (prédicats) ayant n-arité (avec n≥1). Pour cette catégorie de RC dénotée
par la famille des DLs, les réseaux sémantiques suivis des KL-ONE [45]ont été des précurseurs.
Les langages de représentation des connaissances à fondement logique ont évolué au fil du temps, et
ont aboutit au langage OWL2 (Ontology Web Language). Un aperçu chronologique est donné à la figure
3.2.
2. http ://rameau.bnf.fr/formation/pdf/guide_rameau_2017.pdf consulté en 2017
41

--- page 62 ---
Figure 3.3 – Niveaux de formalisation des langages et formes de représentation des connaissances : De
l’informel au formel
Les secondes concernent les représentations à base non logique. Ces dernières ont été souvent déve￾loppées en s’appuyant sur des notions plus cognitives dérivées d’expériences sur le rappel de la mémoire
humaine et sur l’exécution humaine des tâches (par exemple, les structures de réseau et des représen￾tations). Elles sont applicables dans différents domaines et sur différents types de problèmes. Leur base
inférentielle est nettement plus faible que celle des représentations à approche logique (classique).
De tout ce qui précède, nous relevons effectivement deux mondes en matière de formalisme qui se côtoient
sans s’opposer vertement, dans un but unique d’améliorer sans cesse la sémantique formelle. Ces deux
mondes s’enrichissent l’un de l’autre également.
La figure 3.3 donne un aperçu plus détaillé selon le degré de formalisme (ou de formalisation) de
certains langages et formes de RC toutes approches confondues.
Pour la RC, les langages naturels sont à tout point de vue un départ indispensable de tout outil
(formalismes et langages non naturels). A ce titre, le double sens de la flèche bleue exprime l’ultime but
de convergence sémantique recherchée de l’ensemble intégral des outils, formalismes et langages à des fins
d’utilisations (et d’usages) par les agents humains et pour les machines "intelligentes".
Dans les sous-sections suivantes, nous verrons les principales approches, des plus simples aux plus
complexes.
3.2.1 Vocabulaire contrôlé
Un vocabulaire contrôlé 3
est une liste de termes qui ont été énumérés explicitement propre à un
domaine [90] [115] [116] [117] [189]. Cette liste est contrôlée par une autorité compétente auprès de qui
elle peut être disponible . Tous ces termes de ce vocabulaire doivent avoir une définition non ambiguë et
non redondante. Cet objectif de conception peut ne pas être vrai dans la pratique. La rigueur de l’autorité
d’enregistrement de vocabulaire contrôlé [237] en dépend.
3. www.getty.edu/research/publications/electronic_publications/intro_controlled_vocab/what.pdf consulté en 2015
42

--- page 63 ---
Un terme est une représentation de concept (sous forme de mot ou groupes de mots). Quand un concept
est représenté par plus d’un terme, on parle de cas de termes synonymes ou alias [186]. En contrôlant un
vocabulaire, on limite la disparité d’indexation entre auteurs (table alphabétique de mots, de thèmes d’un
livre).
3.2.2 Taxonomies
"Taxinomie" ou "taxonomie" signifie science de la classification, et plus particulièrement, de celle
des formes vivantes selon [117]. Une taxonomie 4
est une collection de termes de vocabulaire contrôlés
organisés en structure hiérarchique [11]. Chaque terme dans une taxonomie est dans une ou plusieurs
relations parent-enfant à d’autres termes dans la taxonomie. Il peut y avoir différents types de relations
parents-enfants dans une taxonomie (e.g : partie à tout, genre-espèce, type-instance) , mais la bonne
pratique limite toutes les relations parent-enfant à un seul parent à être du même type [186] . Certaines
taxonomies permettent la poly-hiérarchie, ce qui signifie qu’un terme peut avoir plusieurs parents. Cela
signifie que si un terme apparaît en plusieurs endroits dans une taxonomie, alors c’est le même terme. Plus
précisément, si un terme a des enfants à un endroit dans une taxonomie, alors il a les mêmes enfants dans
tous les autres endroits où il apparaît.
Une taxonomie a une signification supplémentaire par rapport au vocabulaire contrôlé, par l’intermé￾diaire de la signification du lien hiérarchique. Dans une "taxonomie" traditionnelle, le sens est la généra￾lisation / spécialisation ou "est une sorte de". De nos jours, le mot "taxonomie" est utilisé pour désigner
d’autres types de hiérarchies ayant des significations différentes pour les liens (par exemple, une partie
de, un sujet plus large que, une instance de). Les taxinomies négligées n’identifieront pas explicitement la
signification du lien, et peuvent mélanger différentes significations. La plus grande des taxonomies orga￾nise environ dix millions d’espèces vivantes ou éteintes, dont beaucoup sont des coléoptères, en une seule
hiérarchie. Les bibliothécaires ont développé une taxonomie de tous les champs de connaissances, encodée
dans le système Dewey (Classification décimale de Dewey) [225].
3.2.3 Thésaurus
Les thésaurus 5 datent des années 1990. Un thésaurus est une collection de termes organisés hiérarchi￾quement. Il forme un ensemble de ressources lexicales. Contrairement aux taxonomies, les thésaurus (ou
thésauri) [11], ne sont pas seulement hiérarchiques. Ils constituent un élargissement des taxonomies en
intégrant, au-delà des relations hiérarchiques, d’autres propriétés [189]. Un thésaurus a d’autres types de
liens : terme plus large (boarder)/plus étroit (narrow) / relatif à (relative) / top (resp. BT/NT/RT/TT)
[36], qui ressemblent beaucoup aux liens de généralisation / spécialisation. En fait, ces liens ne sont pas
vraiment différents de ceux d’une taxonomie. Un autre UF (Used for) est une relation synonymique liant
un terme et ses synonymes [116]. Les relations entre les descripteurs peuvent être de plusieurs types :
équivalent, hiérarchique, associatif. Elles peuvent s’avérer des plus floues mais pas les moins intéressantes
pour le système d’indexation [152] [153]. Un thésaurus intègre un répertoire de vedettes-matière comme
par exemple le répertoire d’autorité-matière encyclopédique et alphabétique unifié (RAMEAU) [200]. Pour
exemple de thésaurus, on a MeSH (Medical Subject Headings) 6 de référence dans le domaine biomédical
construit par le NLM (U.S. National Library of Medicine).
4. www.getty.edu/research/publications/electronic_publications/intro_controlled_vocab/what.pdf consulté en 2014
5. www.getty.edu/research/publications/electronic_publications/intro_controlled_vocab/what.pdf consulté en 2014
6. http ://mesh.inserm.fr/mesh/ consulté en 2014
43

--- page 64 ---
Une recommandation ISO pour les thésaurus existe : ISO 25964 7
. Elle est en deux parties : la première
partie porte sur "Information and documentation", publiée en 2011 et la seconde sur "Interopérabilité
avec d’autres vocabulaires", publiée en 2013.
Un thésaurus peut être transformé en ontologie légère.
3.2.4 Logique propositionnelle
Un raisonnement est un discours qui permet d’établir la vérité d’un fait. C’est à cela que s’adonne la
logique. La syntaxe de la logique propositionnelle (LP) définit les énoncés valides. Les énoncés atomiques
consistent en un seul symbole propositionnel. Chacun de ces symboles représente une proposition qui peut
être vraie ou fausse. On y emploie des lettres ou des indices, par exemple P, Q, P1. Ces noms sont arbitraires
mais souvent choisis pour leurs propriétés mnémotechniques. Par exemple : P12. Notons que si P12 est
atomique alors P , 1 et 2 ne sont pas des parties significatives du symbole. Les énoncés complexes sont
construits à partir d’énoncés atomiques plus simples au moyen de parenthèses ( ) et de cinq connecteurs
logiques que sont : ¬ , ∧ , ∨ , → , ↔ . Seuls les connecteurs ¬ , ∧ , ∨ sont plus importants, les deux autres
pouvant s’en déduire.
La sémantique des énoncés définie par la logique, fournit les règles pour déterminer la vérité de ces
énoncés sur la base d’un modèle particulier. Elle repose sur la relation de vérité entre énoncés et des
mondes possibles. Deux symboles propositionnels possèdent une signification fixe : VRAI et FAUX.
Exemples de propositions : "le nombre 5 est plus petit que le nombre 104" est une proposition vraie ;
"il pleut" est vraie s’il pleut et fausse sinon ; "la variable numérique x est plus grande que 10" est vraie
pour les nombres supérieurs à 10 et est fausse dans tous les autres cas.
La LP est un langage trop faible pour représenter précisément les connaissances relatives à des environ￾nements complexes. Ainsi, mieux formaliser le raisonnement trouve sa réponse dans la logique du premier
ordre.
3.2.5 Logique du premier ordre
La logique du premier ordre (LPO) a d’autres appellations que sont logique des prédicats du premier
ordre, logique des prédicats, calcul des relations, calcul des prédicats (ou FOL : First Order Logic en
anglais). Elle est une extension de la LP par ajout de nouveaux connecteurs appelés quantificateurs (∀,∃).
Un prédicat est une fonction d’un nombre fini de variables ou de constantes. Elle permet de d’adresser des
structures comportant :
– un seul domaine non vide ; (domaine pouvant avoir plus de deux valeurs contrairement à la LP) ;
– des fonctions et relations sur ce domaine.
Le langage de cette logique comporte plusieurs catégories : les termes qui représentent les éléments du
domaine ou des fonctions sur ces éléments, des relations qui relient des termes entre eux et les formules qui
décrivent les interactions entre les relations grâce aux connecteurs (quantificateurs y compris). "II y a un
seul langage pertinent pour représenter l’information, qu’il soit déclaratif ou procédural, c’est la logique
des prédicats du premier ordre", selon Glannesini et al. [102].
La syntaxe de la LPO est une indication relativement claire de la sémantique sous-jacente au monde
7. http ://www.niso.org/schemas/iso25964 consulté en 2014
44

--- page 65 ---
(théorie des modèles ou théorie de la sémantique formelle qui relie les expressions aux interprétations 8
).
Le parti pris sémantique de toute représentation logique est celui d’une vue relationnelle du monde. Les
prédicats sont sémantiquement interprétés comme dénotant des relations entre des individus ou objets ici
appelés constantes. La quantification, la prédication et la référence constituent les ingrédients essentiels
de toute sémantique logique. Ils permettent de puissantes variations : interprétations extensionnelles vs.
interprétations intensionnelles. Même s’il existe différentes notations syntaxiques pour la LPO, chacune
d’elles est rigoureusement définie et il est facile de passer de l’une à l’autre. Tout élément notationnel
dépourvu d’une sémantique est exclu. Toute formule d’elles est sémantiquement pertinente. Cette vision
est partagée par [112]. Les principaux symboles en LPO sont :
– les variables : x, y, z, ... ;
– les constantes : A, a, b, c, ... ;
– les fonctions : f, g, h, ... ;
– les termes : variable, constante ou fonction n-aire appliquée à n arguments ;
– les prédicats : p, q, r, ... ;
– les atomes : ⊥, ⊤, or prédicat n-aire appliqué à n termes ;
– les littéraux : un atome p(...) ou sa négation ¬p(...) ;
– les connecteurs : ¬, ∧, ∨, →, ↔;
– les quantificateurs : ∀, ∃.
Un modèle est pris pour spécifier un état possible du monde, et l’analyse sémantique se réduit à
déterminer si oui ou non un énoncé « arbitraire » décrit correctement le monde ; Ou, en théorie des
modèles, si la phrase (statement) est vraie (ou non) dans le modèle en question.
La logique des prédicats offre deux possibilités pour représenter les catégories : prédicat et objet
– on peut utiliser le prédicat BallonDeBasket (b) pour dire que b est un BallonDeBasket,
– ou bien réifier la catégorie sous la forme de l’objet BallonDeBasket. On peut alors écrire membreDe(b,
BallonDeBasket), ou en abrégé b ∈ BallonDeBasket, pour dire cette fois-ci que b est un membre de
la catégorie des BallonDeBasket.
La LPO est indécidable bien qu’elle permet de représenter des connaissances, y compris celles com￾plexes. Une logique est décidable s’il existe un algorithme qui permet de savoir pour chaque formule si elle
est une tautologie (c’est-à-dire si elle est toujours vraie), dans une durée finie. Par conséquent, la LPO ne
permet pas d’automatiser des raisonnements sur les connaissances de manière satisfaisante.
Le tableau 3.3 donne un exemple de LPO.
3.2.6 Graphes conceptuels
Introduit par John F. Sowa en 1984 [218], un graphe conceptuel (GC) est un formalisme de RC et de
raisonnements à base de la LPO. Ce modèle est basé sur les graphes existentiels de C. S. Peirce (1909)
et les réseaux sémantiques [220] [221]. Il représente les connaissances à partir d’un graphe défini sur
un vocabulaire. De son évolution, émergent trois directions principales : interface graphique de la LPO,
système diagrammatique pour la LPO, formalisme de RC et de raisonnement basé sur les graphes.
8. http ://www.yoyodesign.org/doc/w3c/rdf-mt/#glossWorld consulté en 2014
45

--- page 66 ---
Langage naturel LPO
La variable x est un homme, la variable y est une
plante. La constante Socrate est un Homme
Homme(x), Plante(y),
Homme(Socrate)
Tout homme est mortel,
Socrate est un homme. Donc Socrate est mortel.
∀x, Homme(x) ⇒ Mortel(x),
Homme(Socrate) ⇒ Mortel(Socrate)
"Il existe un x gentil tel que pour tout y, x est
ami avec y" (énoncé complexe ou composé).
∃x Gentil(x) ∧∀y Amis(x, y)
TABLEAU 3.3 – Exemple de syntaxe, sémantique et de raisonnement en LPO partant du pseudo langage
naturel
Un GC est un graphe fini, connecté, bipartite. Deux types de nœuds sont utilisés dans ce réseau
sémantique : Concept et Relation conceptuelle (attribut relationnel) aux formalismes respectifs rectangle
et ellipse. Les seuls liens acceptables sont celui d’un concept vers une relation conceptuelle ou celui de la
relation conceptuelle vers un concept. De plus, un GC peut inclure un concept qui est un autre GC.
Contrairement à la plupart des notations pour la logique, les GC peuvent être utilisés avec une gamme
de précision continue : à des fins formelles. Ils sont sous tendus fortement par la logique classique dite
formelle. Cependant les GC peuvent également être utilisés de manière moins flexible et moins disciplinée
en voulant tenir compte de l’imprécision et de l’ambiguïté des langues naturelles [219] [220].
Les relations dans les GC sont seulement binaires [217]. Ce formalisme partage certaines imperfections
avec les réseaux sémantiques. Individu et concept (catégorie) sont syntaxiquement et sémantiquement
assignés aux mêmes symbologies graphiques dans le formalisme des GC.
3.2.7 Réseaux sémantiques
Le réseau sémantique à travers [26] [30], [63], [64], [69], [76], [182] et [224], est un schéma de RC qui
capture la connaissance sous forme de graphique (graphe). Les nœuds du graphe désignent des objets ou
concepts, ou des données. Les arcs indiquent des relations entre les nœuds. Un réseau sémantique est un
graphe marqué (orienté) destiné à la représentation des connaissances. Plus précisément, il représente des
relations sémantiques entre concepts. Les nœuds du graphe désignent les concepts et objets d’une part, et
d’autre part les propriétés et les valeurs correspondantes. Les arcs indiquent des relations entre les nœuds.
Nœuds et arcs sont généralement étiquetés. Un réseau sémantique emploie deux types de nœuds :
– les nœuds étiquetés par des constantes de concepts (représentant des catégories taxonomiques ) ;
– les nœuds étiquetés par des constantes d’objets (représentant des instanciations des concepts ou des
propriétés des concepts).
Un réseau sémantique est taxinomique et compositionnel. Il utilise quatre types d’arcs connectant les
nœuds :
– les arcs d’héritage aussi appelés liens "est un" (is a ou is-a) ;
– les arcs de composition et d’attributs appelés liens "a" (has a) ;
– les arcs d’instanciation également appelés liens "sorteDe" (is a kind of ou ako) ou " membre de" ;
– les arcs transversaux (non hiérarchiques, horizontaux) : les autres relations..
La logique est la base naturelle pour spécifier un sens pour ces structures de réseaux sémantiques.
46

--- page 67 ---
Cependant, ces deux structures ne comprennent que quelques fragments de cette LPO et non l’entièreté
de celle-ci [45]. Elles contiennent des ambiguïtés sur les constances de concepts et d’objets. Cela limite les
inférences.
Introduit par M.Minsky [167], les frames (cadres), sont issus des réseaux sémantiques, mais plus
structurés. De la structuration basée en partie sur l’approche orientée-objet, ces frames sont des granules
de connaissances plus importantes que les nœuds d’un réseau sémantique. Ils représentent une collection de
slots (listes à attributs) qui sont autant de propriétés pour décrire et caractériser. Ils peuvent être assignés
par des valeurs ou par des liens vers d’autres cadres [26], [63], [64], [182]. A ces slots sont associés les fillers
(valeurs ou contenus de champs) de type déclaratif. Ce type peut être procédural ou méta-donnée. Un
frame a qualité d’enregistrement (méta-données et données).
3.2.8 Modélisation par objet typé
La modélisation par objet typé (MOT) conçue par G. Paquette [32] [33] [179] [180] en collaboration avec
les chercheurs du centre de recherche LICEF 9
, est un langage de représentation graphique et semi-formel
de la connaissance. L’originalité de ce système de représentation réside dans le traitement intégré de quatre
types de connaissances : faits, concepts, procédures et principes. La MOT a six types de liens soumis à
certaines contraintes d’intégrité. Cette originalité tient également à sa capacité à représenter des catégories
de modèles complexes tels que les systèmes conceptuels, les théories, les processus et les méthodes. Ces liens
sont symbolisés par S, I, R, A, P et C signifiant respectivement spécialisation, instanciation, régulation,
application, précédence et composition.
3.2.9 Logiques de description
Précédemment appelées langage de représentation terminologique de connaissances, les logiques de
description (DLs ou LDs) sont une famille de langages formels de représentation des connaissances qui
sont largement utilisées dans la modélisation ontologique [158]. Les LDS correspondent à des fragments
de la LPO [106] obtenues en restreignant la syntaxe aux formules contenant deux variables. La figure 3.4
(inspirée de [106]) montre la multiplicité des notations à travers les différentes logiques apparentées à la
LPO. Ainsi, nous avons un bloc en rouge pour toute la famille des LDs, formé du fragment de chaque LD.
Les LDs sont plus expressives que la LP, mais moins que la LPO. Les LDs exploitent, en général, des
sous-ensembles décidables [121] [122] de la LPO. Ces logiques ont été créées dans le but de surmonter les
ambiguïtés des anciens systèmes, par exemple ceux à base de réseaux sémantiques. Les LDs sont donc
un compromis entre expressivité et décidabilité. Elles apparaissent comme le formalisme adéquat pour
représenter les connaissances aujourd’hui [167].
Les LDs incluant des constructions très expressives nécessitent des techniques de raisonnement avan￾cées. En particulier, le raisonnement dans les LDs doit prendre en compte les axiomes d’inclusion générale,
les rôles inverses, les restrictions de nombre, la fermeture réflexive-transitive des rôles, et les constructions
fixes pour les définitions récursives. Les LDs ont été introduites dans le but de fournir une reconstruction
plus formelle de systèmes de frames et de réseaux sémantiques. Au départ, la recherche s’est concentrée
sur la subsomption (taxonomie hiérarchique) d’expressions conceptuelles.
9. LICEF : Laboratoire en informatique cognitive et environnements de formation ; http ://www.licef.teluq.ca/ consulté
en 2014
47

--- page 68 ---
Figure 3.4 – Bloc fragmentaire constitué des Logiques de description de la logique des prédicats (LPO)
Après que soit soigneusement analysé le compromis entre l’expressivité et la souplesse du raisonnement
et que bien expérimentée la portée de l’applicabilité des techniques d’inférence correspondantes, alors il s’en
est suivi un changement d’orientation dans la recherche théorique sur le raisonnement en LDs. L’intérêt
s’est porté sur les LDs relatives aux langages de modélisation utilisés dans la gestion de base de données.
En outre, la découverte de relations strictes avec des logiques modales expressives a stimulé l’étude des
LDs dites très expressives [26].
Une caractéristique distincte des LDs est l’accent mis sur un service central à savoir le raisonnement :
permettant de déduire des connaissances implicitement représentées à partir de celles qui sont explicitement
contenues dans la base de connaissances. Les LDs prennent en charge les modèles d’inférence qui se
produisent dans de nombreuses applications de systèmes intelligents de traitement de l’information, et
qui sont également utilisés par les humains pour structurer et comprendre le monde : la classification
des concepts et des individus. Les langages de ces LDs peuvent être alors considérés comme le noyau des
récents systèmes de représentation des connaissances, prenant en compte à la fois la structure de la base
de connaissances et les services de raisonnement associés.
La recherche dans le domaine de la représentation des connaissances et du raisonnement est générale￾ment axée sur des méthodes en vue de fournir des descriptions de haut niveau d’abstraction du monde.
Ces descriptions sont utilisés efficacement pour construire des applications intelligentes. Dans ce contexte,
"intelligent" se réfère à la capacité d’un système applicatif, de trouver à partir de ses connaissances expli￾citement représentées, des conséquences implicites [167].
3.2.9.1 Syntaxe
Les LDs sont des notations construites pour faciliter la description des catégories à travers leurs défi￾nitions et propriétés. Leur évolution part des réseaux sémantiques en réponse à l’exigence de formaliser ce
que signifient les réseaux tout en conservant la structure taxonomique comme principe organisateur. Dans
les LDs, le principal système d’inférence repose sur la subsomption et la classification. Il y a également la
consistance et la cohérence déterminant si critères et axiomes d’appartenance sont logiquement satisfiables
(ou satisfaisable).
Les éléments de base de la représentation sont caractérisés comme des prédicats unaires, dénotant des
ensembles d’individus, et des prédicats binaires, dénotant des relations entre individus. En exemples, on
48

--- page 69 ---
a : Adulte(s) et marié(x,y).
Les LDs reposent sur trois notions de base : les concepts représentant des classes (ensemble d’objets),
les rôles (relations liant deux objets) et les individus (objets incarnés par les classes qu’ils instancient).
Pour décrire ces éléments, deux structures sont utilisées : T-Box et A-Box comme le stipulent [25], [26],
[120] et [169].
– La T-Box (boîte terminologique) comprend la description des concepts et des rôles. Cette description
est structurée à l’aide du lien hiérarchique sorteDe (parfois appelé est-un). Deux concepts particuliers
figurent d’office dans la T-BOX : le concept le plus générique (anything, noté ⊤) et le concept le
plus spécifique (nothing, noté ⊥).
– La A-Box (boîte assertionnelle) est constituée des individus, de leur description et des règles qui leur
sont attachées (axiomatisation).
Les inférences reposent sur la reconnaissance d’instances de concepts à partir de leur définition, la
détection des concepts plus généraux ou plus spécifiques, et la classification ordonnant les concepts dans
la hiérarchie.
Un axiome est une proposition qui est vrai mais non démontré, et dont on tire des conséquences
logiques, par opposition à un théorème qui est une proposition mathématique démontrée. Nous parlons
d’axiome pour indiquer qu’un énoncé est donné, et non dérivé d’autres énoncés.
Dans l’approche courante de la définition des concepts, on part des deux concepts fondamentaux
l’universel et l’absurde respectivement Thing (⊤) et Nothing (⊥). Après ces deux concepts clés, vient la
création des concepts et des rôles dits primitifs ou atomiques. A ce stade, aucun constructeur n’est utilisé.
Les constructeurs entrent en jeu chaque fois qu’il s’agira de créer des concepts et des rôles non atomiques.
Ils s’appliquent ainsi aux concepts atomiques et rôles atomiques pour engendrer d’autres concepts et rôles
plus complexes. Cette application est faite par conjonction, par disjonction, par négation, par combinaison
de quantification et de restriction numérique et par la composition de rôles. La liste des constructeurs est :
{⊓, ¬, ⊔ , ∃ ,∀, o}. Pour compléter la syntaxe, on rajoute d’autres symboles se rapportant aux éléments
suivants :
– les deux concepts fondamentaux ;
– l’équivalence de deux concepts ;
– la subsomption, qui est une relation hiérarchique entre concepts et entre rôles ;
– l’égalité définitoire d’un concept et d’un rôle complexes. Pour le concept, l’on parle de concept défini ;
– le point d’application de rôle à un concept ;
– les symboles d’égalité et d’inégalité mathématiques ;
– la composition de rôles de symbole.
La liste de ces symboles de l’alphabet est donc {⊓ , ⊔ , ∃, ∀, ¬ , ⊤ , ⊥ , ≡ ,
.= , . , = , ≤ , ≥ , ⊑ , o }
⊤ : concept le plus général, concept universel (Thing) ;
⊥ : concept impossible, absurde (Nothing) ;
⊑ : subsomption
⊓ : intersection ou conjonction de concepts ;
⊔ : union ou disjonction de concepts ;
≡ : équivalence de deux concepts ;
49

--- page 70 ---
.= : égalité définitoire d’un concept complexe, dit défini également ;
¬ : négation ou complément d’un concept ;
o : composition de rôle ;
= , < , > : symboles d’égalité et d’inégalité mathématiques, (NB : ≥ est déduit de : > et = ) ;
. : application d’un rôle sur un concept, avec C un concept et r un rôle, l’application de r à C s’écrit : r.C ;
∃ : quantificateur existentiel, ∃ r.C est la classe des x tel qu’il existe une relation de type r entre x et un individu
de la classe C ;
∀ : quantificateur universel, ∀ r.C est la classe des x tel que, pour tout y avec une relation de type r entre x et
y, y est un individu de la classe C ;
Étant donné A, C, D des concepts, r un rôle et n un nombre entier, alors ¬A, C⊔D, C⊓ D, ∀r.C, ∃r.C,
≥n r et ≤n r sont des concepts.
Par convention, les noms des concepts commencent par une majuscule (e.g : Personne, Homme, Plante
et A ) et ceux des rôles et des individus par une minuscule (e.g : estFils, estParent et r sont des rôles ;
neemier est un individu de Plante).
"Homme ⊑ Personne" et "Homme ⊓ Femme ⊑ ⊥ " sont des exemples simples de T-Box ;
3.2.9.2 Interprétation
Un monde particulier est appelé une interprétation. En LP, le sens des formules est uniquement fixé
par les valeurs des variables.
En LPO, le sens des formules dépend aussi du sens des fonctions et des relations. Ce sens est fixé par
une interprétation. Il en est de même pour les LDs.
Une formule est valide (tautologie) si elle est vraie quelque soit l’interprétation (si toute interprétation
est un modèle).
Par exemple : Personne(x) ⇒ Homme(x) ∨
Femme(x) est une tautologie (toujours vraie).
Une formule est consistante (ou satisfiable) s’il existe une interprétation dans laquelle elle est vraie.
Par exemple : Homme(x) avec Homme(Joseph) un élément d’interprétation.
Une formule est insatisfiable (ou inconsistante) s’il n’existe pas d’interprétation dans laquelle elle est
vraie (e.g : Homme(x) ∧ Femme(x) ) dans un domaine de discours d’humains où personne n’est en même
temps femmes et hommes.
3.2.9.3 Signature
La signature S de la LD est définie par le triplet < CON C, ROL, IND > où CON C, ROL, IND sont
des ensembles resp. des concepts, des rôles et des individus (ou instances).
3.2.9.4 Fonction d’interprétation
On définit une interprétation pour Σ notée I = (∆I
,
.I
) où :
– ∆I ̸=ø (un ensemble non vide) est le domaine de l’interprétation (le domaine de discours ou l’univers).
–
.I est une fonction affectant :
– à chaque ai∈ IND ,
.I( ai) = ai
I∈ ∆I
– à chaque Ci ∈ CON C, .I( Ci) = Ci
I ⊆ ∆I
– à chaque relation binaire ri∈ ROL ,
.I( ri) = ri
I ⊆∆I x ∆I
50

--- page 71 ---
–
. I
(⊤) = ⊤ I = ∆I
–
. I
(⊥) = ⊥ I = ø
– Si A ⊑ C alors AI⊆C
I
3.2.10 RDF et Web sémantique
Resource Description Framework (RDF) est un modèle de graphe destiné à décrire de façon formelle les
ressources Web et leurs métadonnées, de façon à permettre le traitement automatique de telles descriptions.
Développé par le W3C, RDF est le langage de base du Web sémantique [39]. RDF représente le cadre de
description des ressources y compris celles contenues dans le web. On entend par ressource toute entité
que l’on veut décrire sur le web mais qui n’est pas nécessairement elle-même accessible sur le web. Comme
l’indique [222], quatre (4) objectifs de RDF sont : (1) améliorer la découverte de ressources sur le Web ;
(2) établir des catalogues de ressources (décrire le contenu et les relations) ; (3) développer des agents
intelligents ; (4) spécifier la sémantique des données d’un document XML.
RDF est conçu pour être lu et être intelligible (compris) par la machine. RDF n’est pas conçu pour être
utilisé par des humains. Un document RDF est un ensemble de triplets de la forme (sujet, prédicat, objet) :
le "sujet" représente la ressource à décrire ; le "prédicat" représente un type de propriété applicable à cette
ressource ; l’ "objet" représente la valeur de la propriété, il s’agit d’une donnée ou d’une autre ressource. Les
ressources (sujet et objet le cas échéant) peuvent être identifiés par une URI ou être des nœuds anonymes.
Le prédicat est nécessairement identifié par une URI.
Les documents RDF peuvent être écrits en différentes syntaxes, y compris en XML. Mais RDF n’impose
pas nécessairement XML. Il est possible d’avoir recours à d’autres syntaxes pour exprimer les triplets.
RDF est simplement une structure de données constituée de nœuds et organisée en graphe. Le langage
XML utilisé par RDF est RDF/XML. Par l’usage de XML les information RDF peuvent facilement être
échangées entre différentes plate-formes aux types différents de systèmes d’exploitation et de machines.
La sémantique de RDF peut être aussi traduite en formule de LPO, positive (sans négation), conjonctive
et existentielle :
(sujet, objet, prédicat) ↔ prédicat(objet, sujet) ↔ ∃ objet, ∃ sujet tel que prédicat(objet, sujet).
RDF définit peu de prédicats intégrés (built-in predicates), principalement la relation de typage
(rdf :type) et le constructeur de propriétés (rdf :Property). Ainsi, il n’est pas considéré comme un langage
d’ontologie.
RDFS (RDF Schema) étend RDF avec un ensemble de prédicats intégrés pour définir une ontologie
légère. Les principaux éléments de RDFS 10 sont les suivants :
– Définition de classe : rdfs :Class et rdfs :subClassOf définissent une hiérarchie de classes ;
– Définition de propriétés : rdfs :domain et rdfs :range définissent le domaine et la portée (range) d’une
propriété RDF. Une hiérarchie de propriétés peut être définie avec rdfs :subPropertyOf ;
– Définition de type de données : rdfs :Datatype définit un type de données. rdfs :Literal correspond
à un littéral ; les type de données disponibles en XML peuvent être utilisés pour les littéraux ;
– Définition d’instances : les instances sont définies en RDF par un triplet (i, rdf :type, C) où i est
l’instance et C est la classe. La définition peut être complétée par des triplets (i, p, v) indiquant la
valeur v d’une propriété p pour l’instance i ;
– Noms et descriptions des entités : ils peuvent être définis avec les propriétés rdfs :label et rdfs :com￾ment, respectivement.
10. https ://www.w3.org/TR/rdf-schema consulté en 2017/
51

--- page 72 ---
3.2.11 Ontologies formelles
3.2.11.1 Définition
En philosophie, l’Ontologie (avec O majuscule) signifie la théorie des objets et leurs liens. Cette théorie
fournit des critères pour distinguer différents types d’objets (concrets et abstraits, existants et inexistants,
réels et idéaux, indépendants et dépendants) et leurs liens (relations, dépendances et prédication) [65].
En informatique, une ontologie définit formellement un ensemble commun de termes et de concepts
qui sont utilisés pour décrire et représenter un domaine. Une ontologie est spécifique au domaine, et
elle est utilisée pour décrire et représenter un domaine de connaissance. Elle contient des termes et les
relations entre ces termes. Il existe un autre niveau de relation exprimé en utilisant un groupe spécial de
termes : propriétés. Ces termes de propriété décrivent diverses caractéristiques et attributs des concepts,
et ils peuvent également être utilisés pour associer différentes classes ensemble. En ayant les termes et
les relations entre ces termes clairement définis, l’ontologie encode la connaissance du domaine de telle
manière que la connaissance puisse être comprise par un ordinateur. C’est l’idée de base de l’ontologie. Une
ontologie est une représentation de propriétés générales de ce qui existe dans un formalisme permettant
un traitement automatique. Les ontologies peuvent avoir plusieurs buts notamment :
– communication entre machines et humains : intégrer du sens dans les informations manipulées par
les machines ;
– communication entre machines : l’interopérabilité ;
– communication entre humains via des machines.
Selon Sassi et al [216], ces buts sont considérés comme des couches communicationnelles portées par
des communautés d’hommes et/ou de machines.
Un terme est un mot ou une expression de la langue naturelle qui désigne un (des) concept(s) :
cat, chat, greffier, miatou sont des termes qui désignent le concept de chat. Plusieurs termes synonymes
dénotent le même concept, et un terme ambigu est un terme qui peut dénoter des concepts différents.
Un concept (parfois appelé classe) est une idée que l’on se fait de quelque chose. La représentation
mentale générale et abstraite d’un objet donne suite à un concept, manifestation de cette idée. Pour un
concept donné, il est possible d’y référer plusieurs instances ou individus distincts.
Une ontologie nous aide à décrire les faits, les croyances, les hypothèses et les prédictions sur le monde
en général, ou dans un domaine donné en vue de satisfaire un certain nombre de besoins. Toute activité
humaine spécialisée développe son propre jargon (langue de spécialité) sous la forme d’une terminologie
et d’une conceptualisation associée spécifiques. L’existence de tels jargons entraîne des problèmes de com￾préhension et des difficultés à partager des connaissances entre les acteurs de l’entreprise, entre les services
d’une entreprise, et aussi entre les entreprises d’une industrie qui font des métiers différents. Ce constat
peut s’étendre à moult industries.
Une ontologie comprend donc tout ce à quoi il faut penser dans un domaine, tous les objets de pensée
d’un domaine. La façon d’y penser ou d’en parler indique le type ontologique de l’objet (ou des objets).
Par exemple, un docteur n’est pas un objet physique, c’est le rôle académique "docteur" tenu par un objet
physique appelé "être humain". Ainsi, il faudra soigneusement décider, d’une part, si l’on retient la notion
de "docteur" dans l’ontologie du domaine et, d’autre part, quelle est la manière d’être de la notion de
"docteur" pour lui donner le type ontologique qui lui revient [27] [58] [75].
Traditionnellement, la logique étudie le discours dans sa capacité à dire le vrai. Elle s’efforce de dégager
les formes ou manières de dire qui permettent de déterminer la vérité du discours indépendamment de sa
matière, c’est-à-dire ce qui est dit. Mais un discours vrai est un discours qui est conforme à ce qui est.
52

--- page 73 ---
C’est ainsi que la logique entretient une forte proximité (connexité) avec l’ontologie où les lois permettant
de dire le vrai reviennent à des lois caractérisant ce qui est. Si bien qu’élaborer une ontologie peut être
compris comme la construction d’une théorie logique du monde.
La plupart du temps, les termes utilisés en langage naturel ont plusieurs significations, et dans une
ontologie nous avons la possibilité de contraindre l’interprétation sémantique de ces termes et de leur
fournir une définition formelle.
Le concept d’ontologie peut avoir plusieurs définitions selon le type de l’ontologie et son utilisation.
Dans notre cas, nous définissons une ontologie comme un quadruplet (C, R, I, A), où C est l’ensemble
des concepts de l’ontologie, R l’ensemble des relations entre les concepts, I l’ensemble des instances et A
l’ensemble des axiomes. Les ontologies s’appuient sur des LDs pour l’expression des axiomes. Le
choix de la LD dépend du niveau d’expressivité utilisés par l’ontologie, c’est à dire des connecteurs utilisés
dans les axiomes de l’ontologie.
Selon N. Guarino [109] [110] et via [104], en intelligence artificielle, une ontologie représente un artefact
d’ingénierie constitué d’un vocabulaire utilisé pour construire une réalité, accompagnée d’un ensemble
d‘hypothèses implicites concernant la signification des mots et du vocabulaire. Selon Tom Gruber, "Une
ontologie est une spécification formelle explicite d’une conceptualisation partagée" [107].
Les ontologies peuvent exprimer des axiomes et des restrictions, avec un niveau d’expressivité impor￾tant. Cette expressivité élevée rend les ontologies difficiles à créer, à entretenir et à gérer.
NB : Trois engagements en matière d’ingénierie ontologique
Définir une ontologie est une tâche de modélisation entreprise à partir de l’expression linguistique des
connaissances. Les ontologies ont souvent une grande et complexe structure, dont le développement et
l’entretien provoquent certains problèmes à la fois conceptuels et sémantiques. Pour cela, lors du cycle
de développement comprenant l’élicitation, la conceptualisation, formalisation et l’opérationnalisation, un
triple engagement est nécessaire au sens de Bachimont [27]. Ainsi, nous notons :
– un engagement sémantique, fixant le sens linguistique des concepts et connaissances,
– un engagement ontologique, fixant leur sens formel (conceptualisation et formalisation),
– et enfin un engagement computationnel, déterminant leur exploitation effective en machine (réalisa￾tion et utilisations).
3.2.11.2 Types d’ontologies
Plusieurs types d’ontologies sont à distinguer [75], selon le degré d’abstraction et de généralité du
domaine conceptuel couvert par leurs descriptions. Ce sont :
1. Les ontologies fondationnelles (top ou upper-level ontologies) : Encore appelées ontologies de
fondement, elles sont le niveau le plus élevé (abstrait) structurant les connaissances avec des caté￾gories dont l’organisation repose sur des réflexions philosophiques, des fondamentaux et l’essentiel.
Elles expriment des conceptualisations valables dans différents domaines. Elles servent de pilier pour
les ontologies noyau et celles de domaine.
Au moins cinq fonctions leur sont généralement attribuées : (a) améliorer l’interopérabilité séman￾tique, (b) fédérer des ontologies de domaines, (c) faciliter le processus de conception des ontologies de
53

--- page 74 ---
domaine, (d) améliorer la qualité, l’utilisabilité et la ré-utilisabilité, la maintenance et l’évolutivité,
(e) aider aux choix implicites de conceptualisation dans les ontologies de domaine avec un cadre de
comparaison (e.g : engagements ontologiques).
Ce type d’ontologie décrit des concepts très généraux comme l’espace, le temps, la substance, la
matière, les objets, les processus, les évènements, les actions, etc, au sens des dix catégories d’Aristote
(384-322 av.JC) [30] [69] [76]. Il traite de concepts ne dépendant pas d’un problème ou d’un domaine
particulier. Ce sont des concepts fondamentaux et ouverts. En théorie, elles doivent trouver consensus
à de vastes communautés d’utilisateurs. Ce type d’ontologies est fondé sur la théorie de la dépendance.
Son sujet est l’étude des catégories des choses qui existent dans le monde, ou encore des choses à partir
desquelles plusieurs autres émergent. A travers [50], [96], [97] et [99], on pourrait traiter des questions
de perdurants (occurrents) propres aux processus et de perdurants (continuants) propres aux objets
matériels et leur propriétés de dépendances temporellles (atemporelles et intemporelles) et spatiales.
A ces traitements, on peut inclure l’ordre de dimensionnalité de la représentation (inversement
d’interprétation) [161]. Exemples d’ontologies fondationnelles (cf Ontobee 11) : GFO (General Formal
Ontology), OBO (Open Biological and Biomedical Ontology), DOLCE (Descriptive Ontology for
Linguistic and Cognitive. Engineering), BFO (Basic Formal Ontology), YAMATO (Yet Another More
Advanced Top-level Ontology) , SUMO (Suggested Upper Merged Ontology), GO (Gene Ontology),
PO (Plant Ontology), PSO (Plant Structure Ontology), PATO (Phenotype And Trait Ontology),
PROTON 12, CYC 13
, ...
2. Les ontologies noyaux (core-domain ontologies) : Aussi appelées ontologies génériques [235], elles
fournissent les concepts structurants du domaine et décrivent les relations entre ces concepts. En
médecine par exemple, on trouve des concepts de diagnostic, de signe, de structure anatomique et
de relations comme celles liées à la localisation d’une pathologie sur une structure anatomique. Ici
les concepts sont les plus généraux et transverses. On peut y trouver des concepts à lois génériques
et pratiques. Entre le concept de base lié au concept universel Top (⊤ ) et les individus du monde
concerné, la hiérarchie peut ne pas être importante (suffisamment creusée) comme l’est celle des
ontologies fondationnelles. Le nombre de concepts ou de classes intermédiaires est faible. Ces deux
dernières affirmations sont à nuancer car un domaine très riche sémantiquement et en concepts
pourrait particulièrement les contrarier.
Voici deux exemples d’ontologie noyau :
– La décomposition d’une discipline en sous-disciplines : la médecine moderne peut être décomposée
en cancérologie, psychiatrie, pédiatrie, pneumologie, épidémiologie, ...
– La médecine en général et les différentes approches : médecine conventionnelle, médecine tradi￾tionnelle africaine, médecine traditionnelle chinoise, médecine alternative. Chaque sous-discipline
peut ensuite être l’objet d’une ontologie de domaine.
En somme, les concepts d’ontologie noyau sont moins généraux que ceux des ontologies de fondement
mais plus généraux que ceux des ontologies de domaine.
3. Les ontologies de domaine : Elles décrivent les concepts d’un domaine précis, tels qu’ils sont
manipulés par les professionnels ou les praticiens dans ce domaine d’activités humaines. Bien entendu,
11. http ://www.ontobee.org/
12. https ://ontotext.com/proton/protontop.html# consulté en 2015
13. http ://www.ontology4.us/Ontologies/Upper-Ontologies/Cyc%20Ontology/index.html consulté en 2015
54

--- page 75 ---
Figure 3.5 – Racines RDF(S) des constructeurs de base pour OWL
les deux premières catégories d’ontologies constituent un support indéniable (en terme de méta
descriptions) pour les ontologies de domaines. Cependant, la distinction entre ontologie noyaux et
ontologie de domaine n’est pas toujours très nette.
4. Les ontologies de bas niveau : C’est un type d’ontologies pour qualifier celles d’application et
celles de tâche.
En général, les trois premiers types sont les plus fréquents [75] [88].
3.2.11.3 Langage OWL
Le langage OWL (Web Ontology Language, standardisé par le W3C, World Wide Web Consortium)
est l’un des plus utilisés pour formaliser les ontologies. OWL peut prendre en charge un grand nombre de
LDs différentes (transformations structurelles). Il existe également de nombreux outils adaptés à OWL,
dont l’éditeur Protégé. OWL peut s’enregistrer sous différent format, dont RDF/XML et OWL/XML.
La syntaxe de OWL est la résultante croisée de transformations structurelles inspirées et héritées des
syntaxes de XML, RDF, RDFS d’une part et d’autre part de celle des LDs comme le démontrent Dave
et al via [74]. Les constructeurs de base de OWL pour l’information de typage tant pour les classes que
pour les propriétés observent le principe de spécialisation inhérente à la subsomption comme le montre la
figure 3.5. Cela permet la compatibilité avec RDFS et RDF.
En terme de comparaison entre RDFS et OWL, provenant des sites 14 et 15, OWL est un langage
plus riche que RDFS. Aux notions définies par RDFS, OWL ajoute les propriétés de classe équivalente,
de propriété équivalente, d’identité de deux ressources, de différence de deux ressources, de contraire, de
symétrie, d’asymétrie, de transitivité, de réflexivité, d’irreflexivité, de cardinalité, de propriété fonctionnelle
ou inversement fonctionnelle, de propriété inverses, permettant ainsi de définir des rapports complexes entre
des ressources.
14. https ://www.w3.org/TR/owl-ref/ consulté en 2017
15. www-igm.univ-mlv.fr/~dr/XPOSE2009/Le Web 3.0/technologies.html consulté en 2017
55

--- page 76 ---
3.3 Construction d’une ontologie
Les méthodologies et méthodes de construction d’une ontologie formelle et quelques principes généraux
fort afférents sont ici abordées.
3.3.1 Méthodologies de construction
La plupart des méthodologies partagent les mêmes grandes étapes : le recueil de données, d’informations
et de connaissances à travers différentes sources (internet, observations, domaine de discours, experts du
domaine, technique d’élicitation), la conceptualisation, la formalisation, l’implémentation, l’évaluation (ou
validation), la maintenance et l’évolution. Ceci est bien corroboré par la littérature sur les méthodologies
de construction d’ontologies [66], [104], [207].
Nous avons tout d’abord étudié la norme IEEE (I3E) 16 de développement d’outils et d’applications
logiciels. De cette norme, nous tirons quelques principes forts sur les aspects axiaux de développement
du logiciel dans lesquels s’inscrit le spectre de méthodologies de la construction d’une ontologie. Nous
ferons ensuite un zoom sur trois méthodologies notamment Diligent [77] [87] [190] [191], NeOn [53] [105]
[223] et OntoForInfoSciences [160]. Ces trois méthodologies étendent On-to-knowledge et Methontology,
deux méthodologies plus fermées aux activités de conceptualisation, de formalisation et d’implémentation.
Enfin, nous arrêterons notre démarche méthodologique de construction pour notre ontologie de la MT
(ontoMEDTRAD).
3.3.1.1 Norme I3E 1074-1995 de développement d’application logicielle, appliquée à la
construction d’une ontologie
La norme I3E 17 1074-1995 [70] est une description du processus et des étapes pour développement de
logiciel très reconnue en terme de choix conceptuel, technique et opérationnel. Cette norme, selon [91],
repose sur quatre (4) éléments que nous notons E1, E2, E3 et E4.
– E1 : Modèle de cycle de vie de développement : Il s’agit du choix des modèles de cycles de vie
appropriés.
– E2 : Gestion globale du processus de développement : Une coordination générale des activités de
développement permet de dégager une vue synoptique de leur déroulement et l’état d’avancement
des travaux afférents depuis l’initiation du projet en passant par le management et le contrôle. C’est
une sorte de tableau de bord avec des indicateurs de performance du déroulement du programme de
développement du logiciel.
– E3 : Stratégie de conduite et d’orientation du développement : Sont ici concernés, le pré-développement,
le développement et le post-développement.
– (a) le pré-développement : c’est l’étude de faisabilité où il est question de la spécification des
besoins et la définition du cahier des charges et des questions de compétences. C’est l’étape de
l’étude préalable (de l’existant). Il faut également s’assurer de la capacité d’expertise et de la
16.
https :www1.in.tum.de/paid.globalse.org/paid1/courseDocs/Readings/SoftwareLifeCycle030398.pdf consulté en 2017
17. http ://arantxa.ii.uam.es/~sacuna/is1/normas/IEEE_Std_1074_1997.pdf consulté en 2017
56

--- page 77 ---
disponibilité de la technologie nécessaire à utiliser. Les moyens économiques et l’environnement
de développement ne sont pas en reste.
S’agissant du cas spécifique de développement d’une ontologie, c’est de préciser, les justifications en
terme de besoins d’une ontologie et le cadre dans lequel cette ontologie future va être développée et
déployée (installée et utilisée). Il y est compris l’examen de sa possible intégration dans d’autres
systèmes. Dans les domaines où il existe une ontologie, il est possible d’exprimer les différents
modèles conceptuels correspondant à différents cahiers de charges applicatifs en termes de sous￾ensembles ou de spécialisation de cette ontologie [187]. Pour un domaine de discours, à l’image
d’une base de données (ontologie légère), il existe toujours un fond de schéma conceptuel de
données à partir duquel une ontologie prend forme.
– (b) le développement : Il vise la production logicielle tel que attendue à travers trois étapes :
définition des moyens nécessaires pour développer l’application attendue partant de la conception
à réalisation du logiciel, ensuite la conception et enfin l’implémentation dans les langages de
programmation prévus à cet effet. Cette étape est très déterminante.
– En la situation d’une ontologie à développer, l’expert ontologiste (ingénierie ontologique), donne
un aperçu des attentes et critères de qualité auxquels doit répondre la future ontologie. Le type
d’ontologie à construire (domaine ou autre) doit être déterminée. Quel en est le degré ou la
possibilité de la réutilisation d’une ou plusieurs ontologies existantes.
– En second, on a la conception de l’ontologie dont la méthodologie de construction n’est pas en
phase fermée ou hermétique à celle de la construction d’un simple logiciel, bien que des éléments
communs existent (conceptualisation, modélisation). Il faut faire appel aux méthodes existantes
parmi lesquelles aucune ne s’impose à ce jour. C’est pourquoi, il n’est pas exclu la possibilité de
simplement s’en inspirer pour arriver au terme de la construction de l’ontologie via des étapes
clairement consignées. La conceptualisation suivie de la formalisation de l’ontologie sont deux
activités indispensables.
– En troisième étape, on a l’implémentation de la formalisation : C’est l’étape d’encodage de
l’ontologie à travers des outils comme protégé. L’ontologie est en phase d’utilisation à travers
de multiples applications directes (SPARQL) ou à travers d’autres applications développées. Le
support (de données) essentiel est bien cette ontologie construite.
– (c) le post-développement ou l’après développement : Avant le déploiement d’envergure du logiciel
ou des outils développés, il y a des essais pilotes d’utilisation avec des formations liminaires des
utilisateurs finaux. Après cela, il faut passer à une plus grande échelle jusqu’à la couverture maxi￾male du champ d’utilisation. Ceci est accompagné de techniques de validation et de maintenance.
Tout ce qui précède est mis en application quand il s’agit d’ontologie développée. Il faut y rajouter
un support de validation et de son évolution consensuel.
– E4 : Processus d’intégration : Ce processus doit assurer la complétude et la qualité des activités
(définition, accomplissement, finition). Il donne le cadre en terme d’action supplémentaire et utile
permettant d’aboutir avec succès au développement de l’application prévue (attendue) avec une
bonne maitrise des effets de bord. Aussi les responsables experts de l’ontologie construite doivent-ils
bénéficier de formation en vue de leur permettre de relever le défi de sa maintenance. Il faut leur
rendre disponible un guide d’utilisation. De façon personnalisable ou prototypée, des spécimens de
57

--- page 78 ---
formation et de guides d’utilisation sont définies selon la typologie des utilisateurs.
Très clairement et de façon pragmatique, dans son application à la construction d’une base de données
applicative, la norme I3E 1074-1995 devient encore plus accommodante qu’à la construction d’une ontologie
en général. Elle peut cependant être appelée dans les méthodologies de construction d’ontologie de domaine.
Seulement en certains points pour la construction d’ontologies fondationnelles et noyau, elle pourrait être
intéressante. Cela est à juste titre, car les ontologies de domaine sont plus promptes à des applications
concrètes que celles de type noyau ou fondationnel. Dans notre travail, nous intègrerons cette norme dans
notre démarche.
3.3.1.2 Méthodologie Diligent
Diligent (DIstributed, Loosely-controlled and evolvInG Engineering of oNTologies ) est une méthodo￾logie de construction d’ontologie comprenant 5 étapes.
L’ontologie idéale est celle émanant des parties prenantes qui seraient à la fois les experts du do￾maine, les experts de l’ingénierie ontologique et les potentiels utilisateurs. Cela assurerait la consistance
et la validation de l’ontologie construite. Hélas, une telle situation où de telles parties prenantes dispose￾raient d’un tel cumul de connaissances et d’expertises distinctes, est rare. Du coup, nous devons envisager
une construction d’ontologie multi-expertise ou pluridisciplinaire (sans volonté d’exagération) autour des
connaissances du domaine de discours circonscrit.
Plus encore, la dispersion géographique des parties prenantes (acteurs) impliquées dans la construction
d’une ontologie peut constituer un écueil ou un obstacle important au déroulement normal du dévelop￾pement de cette ontologie. Et pourtant, il faille minimiser les coûts (en matière de consommation de
ressources de tout ordre) de construction d’une ontologie. Ceci peut passer également par la réduction du
nombre des déplacements des acteurs de construction, et les lourdeurs engendrées par la perte de temps.
Face à ce qui vient d’être décrit (construction centrée utilisateur), la raison d’être de Diligent est
d’apporter une solution idoine à la question de la bonne méthodologie de développement d’ontologie
quelle que soit la localisation des acteurs ou de leur répartition géographique en différents endroits et
lieux. Cette raison d’être de Diligent est donc la prise en compte de la collaboration à distance (en
temps réel via un Chat Room (messagerie) par exemple ou de partage d’espace web où les documents
de travail (en entrée, en cours et en sortie), sont disponibles et accessibles). Bien entendu, quelle que
soit leur typologie et le domaine d’expertise de ces acteurs, il s’agit pour Diligent de leur permettre une
bien meilleure communication dans le but ultime de participer activement à la construction de l’ontologie
(partager, échanger et discuter les points de vue, discuter pour aboutir sur arrêt consensuel). Diligent
décrit les dispositions adéquates relatives à la démarche méthodologique, l’outillage et le langage qui
doivent jalonner tout le cycle processuel de construction de l’ontologie (cf tableau 3.4 et figure 3.6).
La capitalisation des expériences nécessite de corriger les faiblesses relevées et à en dresser en référence
les forces de la méthode, et ce de façon consensuelle et démocratique, suite aux modifications introduites
par les utilisateurs et le management général (conseil central doté d’outils appropriés). Ce conseil endosse
la responsabilité de la qualité et de la maintenance de l’ontologie en construction. Le détail des étapes de
la méthodologie est de mise. L’originalité de la méthodologie est de faire porter le focus par les utilisateurs
sur l’usage de l’ontologie dans son état d’amorçage initial (avec peu de concepts, en général les fonda￾mentaux). Concernant l’ontologie, son enrichissement en concepts nouveaux est fait tout le cours de son
58

--- page 79 ---
5 Étapes Description
1 Construire Ontologie initiale de petite taille (nombre de concepts, ...). ;
Cette première version de l’ontologie est consensuelle. On est conscient de la non
couverture du domaine de discours par cette ontologie. Appelons-la, A.
2 Adapter
localement
A est disponible et est utilisable par les acteurs. Pendant l’utilisation de A, d’autres
propositions allant dans le sens de la couverture du domaine sont engendrées.
Comme le changement est très caractéristique de toute organisation entreprise
(nouvelles directives et exigences, besoins nouveaux, but institutionnel, changement des
utilisateurs, du personnel, évolution des ontologies locales), cette utilisation nous amène
à un travail de comparaison des concepts de notre environnement ou de l’ontologie
locale si elle existe, ou d’autres ressources terminologiques et ontologiques (RTO) avec
A.
Les autorisations de modification passent par des requêtes pilotées par un tableau de
bord de contrôle géré par un conseil d’administration. Ce tableau de contrôle recevant
les demandes de modification de l’ontologie partagée A, il faut ensuite examiner les
modifications ou adaptations possibles pour ne pas mettre en biais la réalité du
domaine de discours et non plus celle de son environnement local.
3 analyser Détecter les similarités entre l’ontologie locale et A ;
Examiner les demandes (argumentées avec des exemples et contre-exemples, classer les
arguments, tracer les discussions) de modifications des utilisateurs.
Procéder à des modifications avec vote démocratique consensuel (acceptées ou rejetées),
appuyées par un autre argumentaire.
Tracer les discussions et mettre à jour structures canoniques et particularités.
Une décision équilibrée qui tient compte des différents besoins des utilisateurs et qui
répond aux exigences évolutives de l’utilisateur doit être trouvée.
4 réviser Réviser régulièrement l’ontologie A par le conseil central de contrôle (dans toute
décentralisation, il y a un minimum de centralisation pour éviter le chaos) ; Ce conseil
révise régulièrement l’ontologie partagée A, de sorte à éviter que les ontologies locales
emmènent l’ontologie partagée en construction hors du domaine de discours objectivé
(objectif initial).
Par conséquent, le conseil devrait avoir une participation équilibrée et représentative
des différents types de participants impliqués dans le processus.
5 mettre à jour
localement
Sortie de la version de l’ontologie et mise à jour des ontologies locales
TABLEAU 3.4 – Description de chacune des 5 étapes de Diligent
59

--- page 80 ---
Figure 3.6 – Illustration des cinq (5) phases de la méthodologie Diligent [77]
développement et de son cycle de vie. Un tableau de bord disponible mais plus utilisé par le conseil central,
donne un aperçu synoptique ou un aperçu à vol d’oiseau (birds-eye View) de l’ensemble du processus des
activités (entrée, déroulement, sortie) de construction de l’ontologie. Diligent n’impose aucun formalisme
de présentation des concepts et relations de l’ontologie. Le processus méthodologique de Diligent est illustré
via la figure 3.6.
3.3.1.3 Méthodologie NeOn
Cette méthodologie NeOn (cf tableau 3.5 et figure 3.7) de construction d’ontologie comprend 9 étapes
(en scénarios). Comme Diligent, Néon étend les On-to-knowledge et Methontology, deux méthodologies
plus fermées aux activités de conceptualisation, de formalisation et d’implémentation.
Nous faisons remarquer que l’activité de conceptualisation est centrale pour l’ensemble des 9 étapes de
Néon, car elle intervient pour chacune des 7 étapes (de la 2ème à la 8ème) de NeOn.
En outre, en fonction du niveau de modélisation à atteindre ou en vue d’obtenir un niveau stable (ou
un niveau dit d’invariabilité suffisante) de nos modèles, une stratégie additionnelle de Neon consiste à
reparcourir les étapes avec le préfixe "Re" (cf figure 3.8). Cela donne pour les principales activités suc￾cessives leurs dénominations Re-spécification, Re-conceptualisation. Re-formalisation, Re-implémentation.
Ceci concourt à mesurer l’invariabilité de nos modèles en comparaison avec ceux du précédent parcours.
La conduite à terme de l’ensemble des activités, permet par exemple au niveau de l’implémentation de
déceler les faiblesses et difficultés rencontrées de sorte qu’au prochain parcours des corrections puissent
être apportées au niveau des modèles avant leur implémentation.
3.3.1.4 Méthodologie ontoForInfoScience
OntoForInfoScience est une méthodologie de construction d’ontologie comprenant 9 étapes. Comme
Diligent et Néon, OntoForInfoScience étend On-to-knowledge et Methontology deux méthodologies plus
60

--- page 81 ---
9 Étapes (Scénarios) Description
1 De la spécification à la mise en
œuvre
Spécifier les besoins de construire une ontologie.
Spécifier les exigences en attente (questions de compétence) de
l’ontologie et les moyens dont il faut disposer en vue de la
construire. Soit il s’agit de construire une ontologie partant « de
rien » ou à partir d’ontologies existantes. ORSD (ontology
requirements specification document) est le document de
spécification des besoins en terme de cahier de charge qui en
résulte principalement.
Il s’agit pour Néon d’une ontologie avec une collaboration en
réseau des acteurs impliqués. Ce qui vaut le dénominatif
d’ontologie de réseau.
2 Réutiliser et réorganiser les
ressources non-ontologiques
Réutiliser et réorganiser (re-ingénierie) les ressources
non-ontologiques de sorte à leur donner un format ontologique.
3 Réutiliser les ressources
ontologiques
Réutiliser totalement ou quelques modules ou encore quelques
déclarations d’une ou plusieurs ontologies existantes (d’ici, il est
possible d’aller aux étapes 5 et 6)
4 Réutiliser et réorganiser les
ressources ontologiques
Réutiliser et réorganiser les ressources ontologiques existantes qui
passe par une profonde structuration avec la technique de reverse
ingéniering. On part ainsi du niveau d’implémentation au niveau
conceptuel et formel avant de redescendre dans l’implémentation
(courbe de soleil).
5 Réutiliser et fusionner les
ressources ontologiques
Réutiliser les ressources ontologiques existantes (étape 3).
Particulièrement cette étape où il est question de fusion,
s’applique lorsqu’on est en présence de la réutilisation de
plusieurs ontologies existantes. Les opérations d’alignement des
ontologies peuvent s’avérer nécessaires.
6 Réutiliser, fusionner et
réorganiser les ressources
ontologiques
En plus de l’étape 5, on fait usage de la technique de reverse
ingéniering pour la restructuration
7 Réutiliser des modèles de patron
de conception de l’ontologie
(ODP)
L’utilisation des patrons de concepts des ontologies existantes
permet un gain de temps de conception et de développement
8 Restructurer les ressources
ontologiques
Cette restructuration de l’ontologie réseau en construction peut se
décliner aux sous activités :
(1) modulariser l’ontologie (différents modules)
(2) élaguer des branches de la taxonomie non nécessaires ;
(3) étendre l’ontologie, y compris (en largeur) de nouveaux
concepts et relations ;
et (4) spécialiser les branches qui exigent plus de granularité et
incluant des concepts et des relations de domaine plus spécialisés
(taxinomie approfondie)
9 Localiser les ressources
ontologiques
Cette phase s’adresse aux différents langages des ontologies
existantes à arrêter et leur traduction possible vers la langue
principale de l’ontologie en construction (multilingue).
ODP : Ontology Design Pattern
TABLEAU 3.5 – Description de chacune des 9 scénarii de Néon
61

--- page 82 ---
Figure 3.7 – Illustration des étapes en 9 scénarios de NEON [53]
X est une étape
Figure 3.8 – Reparcours des étapes pour l’atteinte d’un niveau de stabilité suffisant pour nos modèles
62

--- page 83 ---
9 Phases Description
1 Évaluation des besoins
en ontologie
Définir les besoins.Questions de compétence, critère, cahier de charge, définir ou
faire un inventaire des moyens ou ressources dont on aura besoin
2 Spécification de
l’ontologie
Spécification structurelle de l’ontologie, réutilisation d’ontologie existante ou
construire partir de rien
3 Acquisition et extraction
des connaissances
Collection des informations avec les procédés de recherche de l’information utilisés
4 Conceptualisation Affiner et rendre atomique l’ensemble des concepts et des relations entre concepts
5 Fondement ontologique Ontologie de base
6 Formalisation de
l’ontologie
Développement à proprement dit de l’ontologie au moyen de langage formel (OWL)
7 Évaluation de
l’ontologie
Indicateurs d’évaluation : validation, satisfaisabilité et consistance, respect du cahier
des charges
8 Documentation Une documentation sanctionne chaque étape. En plus, on a le document bilan qui
sanctionne l’ontologie construite (prête à l’emploi).
9 Publication de
l’ontologie
ontologie prête à l’emploi
TABLEAU 3.6 – Illustration des étapes en 9 scénarios de ontoForInfoScience
fermées aux activités de conceptualisation, de formalisation et d’implémentation. Le tableau 3.6 et la figure
3.9 expriment différemment les 9 phases ou étapes de OntoForInfoScience.
Remarque
A travers ces trois méthodologies, spécifiquement pour l’évolution de l’ontologie, il s’agit au minimum de
supprimer, ajouter, déplacer, renommer, fusionner, diviser un concept ou (et) une relation au sens de Sassi
et al [216]. Cette transformation est rythmée par les besoins humains et le but institutionnel, eux-mêmes
tellement influencés par des réseaux complexes de contextes que toute formalisation doit être faite avec
soin et humilité[94].
3.3.2 Principes généraux
Un grand nombre de principes communs se retrouvent dans les ontologies, quelle que soit la méthodo￾logie de construction employée. Nous décrivons ici les principaux.
3.3.2.1 Rejet de l’hypothèse du nom unique (UNA)
L’hypothèse du nom unique UNA (Unique Name Assumption) signifie que deux concepts avec des noms
différents sont nécessairement distincts. Les ontologies ne font pas l’hypothèse du nom unique (UNA).
Cela implique que deux concepts avec des noms différents peuvent malgré tout être considérés comme
équivalents. De notre expérience, l’UNA est plus adaptée à de nombreux problèmes d’ingénierie qui utilisent
des ontologies comme solutions (e.g : le modèle PLIB (Parts LIBrary), GUI (globally unique identifier
traduit en français par identifiant universel globalement unique)[40], [188]). En revanche, sur le Web,
l’UNA est souvent considérée comme moins plausible.
63

--- page 84 ---
Figure 3.9 – Illustration des 9 étapes de ontoForInfoScience [160]
64

--- page 85 ---
3.3.2.2 Hypothèse du monde ouvert (OWA)
L’hypothèse du monde ouvert (Open-World Assumption, OWA) signifie que tout ce qui n’est pas
préalablement spécifié est possible et peut être vrai ou faux [243]. OWA est notamment utilisée dans des
bases de connaissances, soutenue par des axiomes. Le contraire est l’hypothèse du monde fermé (Closed￾World Assumption, CWA) [243] : tout ce qui n’est pas connu comme vrai dans la base de données ou
de connaissances est considéré comme faux. Les ontologies adoptent généralement l’approche OWA. Voici
plusieurs exemples :
1. "Jean est un citoyen d’Israël". Jean est-il américain ?
Avec CWA, la réponse est non.
Avec OWA, la réponse est inconnue. Car, elle peut être vraie ou fausse. Du moment où Jean peut
avoir la double nationalité.
2. "Jean est un citoyen d’Israël". En plus, on dispose de l’axiome : "une personne ne peut seulement
qu’être un citoyen d’un seul pays". Jean est il américain ?
Ici, la réponse est à la fois non, avec CWA et avec OWA.
3.3.2.3 Continuants et occurrents
Le terme changement appliqué au monde n’a de sens qu’avec le constat de changement de son contenu.
Chacun des éléments formant ce contenu constitue bien un système de nature et de complexité variés. Ils
peuplent ainsi ce monde et ne changent pas tous de la même manière. Aussi note-t-on que le monde est
en plus peuplé par les moult échanges ou interactions entre ces systèmes. Aucun de ces systèmes n’est
isolé, c’est à dire, sans connexion à un autre. Cet état de fait nous amène à une description catégorielle
(canonique) prenant en compte les types de changement basiques qui sous-tendent l’ensemble de ces
systèmes ou sujets existants (choses, objets individuels) et leurs interactions. Nous présentons un exemple
traduisant des sujets, acteurs ou participants, et les échanges possibles entre ces derniers (le tout décrivant
des processus). Il s’agit de l’édification d’une maison : La construction d’une maison est un processus
aboutissant au sujet maison. Ce processus est une succession d’interactions et d’échanges entre autres
sujets. Les constituants de la maison connaissent d’autres échanges interactionnels jusqu’à ce que ce sujet
maison habité et maintenu, disparaisse un jour (par exemple 60 ans après).
A l’analyse de ce qui vient d’être décrit, il ressort une projection représentative d’un domaine de
discours pouvant faire l’objet d’un travail d’ingénierie ontologique. Cette ingénierie est foncièrement basée
sur une classification catégorielle des objets individuels à même d’aider à une interprétation de ce domaine.
Pour cela, la compréhension voire l’entendement plus avancé de ce domaine nous amène à une ap￾préhension plus approfondie basée sur quelques concepts catégoriels pour une catégorisation adéquate et
valide. Ces concepts sont : les endurants (ou continuants) et les perdurants (ou occurrents). Notons que
les continuants sont les sujets, les objets, les porteurs ou encore les participants des occurrents.
En parlant d’occurrent, il faut y voir temps, processus et évènement. Les types de dépendances entre
continuants et occurrents ne seront pas en reste dans ce qui va suivre.
Les continuants (choses ou objets) persistent dans le temps ; Par conséquent, on les appelle aussi
les endurants [96] [97]. Un continuant existe dans son ensemble à chaque instant de son existence. Un
continuant peut subir un changement : C’est-à-dire que ses propriétés peuvent être différentes à différents
65

--- page 86 ---
SNAP SPAN
Objects Processes, Events
Continuants (endurants) Occurrents (perdurants)
TABLEAU 3.7 – SNAP et SPAN de BFO
moments, bien que son identité reste fixe. Autrement dit, les propriétés d’un continuant peuvent varier
avec le temps ; En conséquence un continuant, en respectant sa stature dans son ensemble, est une entité
dépendant du temps. Au fil du temps, il peut acquérir ou perdre certaines de ses parties dans le respect
de certaines propriétés de l’ensemble ou de ses parties. Ces composantes ou parties sont plus spatiales que
temporelles (voire totalement spatiales). Par exemple : la chaise, mon crayon, l’ami Doha Dakrome, la
cité, les USA (union de 13 pays en 1776 puis aujourd’hui de 51 pays depuis 1969) [225] ;
Les occurrents sont tout ce qui se passe. Les occurrents se produisent dans le temps ; Ils sont aussi
appelés perdurants [34] [50] [99]. Un occurrent n’est pas présent à tout moment dans son ensemble. Il est
sujet à plus de changements (notables). Il dispose beaucoup plus (voire totalement) de parties temporelles
qui ont des propriétés différentes selon le temps. Il est possible qu’il dispose de parties spatiales également
mais pas toujours. Les propriétés d’un occurrent peuvent être intemporelles. C’est le cas d’un second
occurrent qui a obligatoirement lieu, car impliqué ou déclenché par un premier quoi qu’il en soit. Par
conséquent, certains des occurrents sont des entités indépendantes du temps. Quand il commence, il se
déroule. Par exemple : la vie d’un être, battement du cœur, un voyage, une éruption, fabrication de charbon
de bois. En outre, on a aussi l’existence d’un occurrent dans un continuant à l’instar du battement de
cœur au sein d’une personne qui respire.
Une telle approche du monde constitue le fondement de BFO (Basic Formal Ontology), une ontologie
générale inspirée par une autre, OBO (Open Biomedical Ontologies) d’ordre biomédical. Au plan des
catégories fondationnelles (top-level), BFO est compatible avec l’ontologie DOLCE (Ontology for Linguistic
and Cognitive Engineering). BFO comprend deux principales sous ontologies dénotées par SNAP et SPAN
portant respectivement sur les continuants et les occurrents [99].
Nous donnons à travers le tableau 3.7, les correspondants en SNAP (SNAPshot) et SPAN (SPANning
a period of time) de BFO.
Un occurrent implique nécessairement des continuants [98]. Au premier plan de ces continuants, on a
les objets acteurs ou participants (actifs de l’occurrent). Au second rang, on a les autres continuants non
acteurs (passifs de l’occurrent). Et enfin, on a les continuants qui ne sont pas concernés du tout par un
occurrent donné. Aucun occurrent ne peut exister sans continuants [206].
3.3.2.4 Processus et évènements
Un processus commence et finit (open-ended). En clair, il a un début et une fin. Il n’est pas ponctuel.
Il est homogène. Il peut être expérimenté. Les propriétés d’un processus n’ont pas de fin intrinsèque.
Quelques exemples de processus :
– Les activités humaines comme la marche, la nage, la conduite de charrette, la conduite d’un autocar,
jouer au piano, pousser une brouette, éplucher des pommes de terre, écrire.
– Les phénomènes naturels comme la pluie, la marrée haute, la photosynthèse, la circulation du sang,
l’écoulement d’une rivière, l’érosion, la révolution de la terre.
66

--- page 87 ---
Un évènement est le fait qu’une chose se passe. L’évènement ne change pas. Il est non divisible.
Pour sa bonne compréhension on le définit également par rapport au processus. Pour cela, l’évènement
est également vu comme une seule occurrence d’un processus (a single occurrence of a process). Il est
exhaustif (complet) et ponctuel dans un processus. Chacun des deux affirmations "Achat de voiture" et
"calcination du bois" constitue un processus. "Voiture achetée" et "bois calciné" constituent chacun un
évènement. Deux sortes d’évènements apparaissent, l’un est instantané (Tdebut=Tfin) et l’autre défini
selon un intervalle de temps (Tdebut, Tfin).
Différentes perceptions en classification hiérarchique de processus et évènement sont à noter dans [99] :
– Le premier point de vue défendu par Mourelatos [164] et autres : Processus et Évènement sont des
sous catégories disjointes de Occurrents (occurrence) ;
– Le second groupe du même point de vue que celui de Moens et Steedman [163] et autres) soutient :
Processus est sous catégorie de Évènement ;
– Un troisième groupe stipulant le même point de vue que Sowa, disent : Évènement est sous catégorie
de Processus.
Dans notre modélisation, nous optons pour la classification des catégories disjointes de Processus et
Évènement, sous classes de Occurrent.
3.3.2.5 Objets fluents
Par fluent [225], il faut entendre une chose ou objet qui a un état variable. Il coule, change tout le
temps. Il s’oppose à statique. Par la sublimation de l’espace et du temps en tout objet physique existant, on
arrive à reconsidérer ce dernier comme un évènement généralisé. On peut pour cela considérer USA comme
un évènement ayant débuté en 1776 sous la forme d’une union de 13 états, et qui est toujours en cours, sous
la forme actuelle d’une union de 51 États. On a également des fluents d’états pour décrire les propriétés
qui changent comme population et président assignées à USA, notées respectivement : Population(USA)
et Président (USA). En outre T1(egal(President(USA), Barack Obama), 2010 ApJC ) est une assertion
qui traduit le fait suivant : Le président des États-Unis était Barack Obama en 2010.
3.3.2.6 Homéomères (noms non comptables) et anhoméomères (noms comptables)
Selon Aristote, des parties des animaux, les unes sont "incomposées" ; ce sont celles qui se divisent
en homéomères, comme les chairs en chairs. Les autres sont composées : ce sont celles qui se divisent en
anhoméomères ; la main, par exemple, ne se divise pas en mains, ni le visage en visages. On généralise cette
idée, en parlant d’entités ou d’objets homéomères et ceux qui ne le sont pas, sont les entités anhoméomères
[43] [225].
Nous avons dans la conception des ontologies la question de relation hiérarchique, de relation composi￾tionnelle ou partitive et de relation horizontale souvent observables, avec les axiomatisations possibles, de
classes primitives, de classes définies possibles (classes auxquelles on a donné une définition propre souvent
utilisant une ou des classes primitives).
Nous avons les substances, les éléments et temps/espace. En premier lieu, on a les substances : chair,
fer, bois, ... ainsi que quelques-unes de leurs propriétés comme la couleur. Viennent ensuite les "éléments"
qui ont servi de principes à l’ancienne physique : la terre, l’air, le feu, l’eau ; c’est ce que A. J. Greimas
appelle le "figuratif abstrait" [43]. Enfin, on a en exemple l’espace et le temps. Une partie du temps est
67

--- page 88 ---
Une partie de beurre (Beurre) est du beurre b ⊂ Beurre ∧ partOf (p, b) ⇒ p ⊂ Beurre
Exemples de propriété intrinsèque de Beurre (PInt
ensemble de ce type de propriétés) : ex : saveur,
blancheur
k ∈ PInt ∧ b ⊂ Beurre ∧ partOf (p, b) ⇒ k(p) = k(b)
Exemples de propriété extrinsèque de Beurre (PExt
ensemble de ce type de propriétés) : ex : poids
k ∈ PExt ∧ b ⊂ Beurre ∧ partOf (p, b) ̸⇒ k(p) = k(b)
TABLEAU 3.8 – Propriétés d’une partie d’un objet suite à sa subdivision
un temps. Une partie de l’espace est un espace.
Les propriétés intrinsèques d’un objet appartiennent à la substance même de l’objet plutôt qu’à l’objet
en soi. Lorsqu’on coupe une instance de matière en deux, les deux morceaux obtenus conservent les mêmes
propriétés intrinsèques (densité, saveur, point d’ébullition, couleur, appartenance, odorat,..). A l’inverse les
propriétés extrinsèques, telles que le poids, la longueur, la forme, ... ne sont pas conservées dans les parties
découlant d’une subdivision. Le tableau 3.8 donne une illustration de formalisation de ces propriétés.
La propriété intrinsèque d’une chose est une propriété qui est essentielle à la chose. Cette chose peut perdre
son identité lorsque la propriété change.
Il est bon de noter qu’il est difficile pour moult choses, objets de perdurer identiquement et pareillement
à son état antérieur dans le temps [148]. L’exception est faite sur les objets atemporels (e.g : symbole
mathématique "+"). Cependant, on peut se questionner si ce symbole pourrait-il changer un jour ?
3.3.3 Conclusion sur les méthodologies existantes
Il n’existe à ce jour aucune méthodologie de construction d’ontologie qui soit normalisée, standardisée
ou fortement recommandée par les organismes de normalisation (W3C, ISO, ...). Nous voyons plusieurs
raisons à cela :
1. La base sur laquelle, nous entreprenons nos activités, nous menons nos réflexions (à travers moult
organisations), toute une vie ou via plusieurs cycles de vie, est soutenue par des fondements très
souvent ignorés ou passés sous silence par nous-mêmes. Malgré le bâti considérable, nous avons du mal
à définir les fondements consensuels pour tout existant. La raison d’intérêts divergents favorable (ou
profitant) au profit, tient-elle ? En outre, est-il possible d’avoir une vue d’ensemble consensuelle sur
les découvertes de "nouvelles" planètes, de "nouveaux" individus ? Nous avons encore du mal à définir
ce à partir de quoi l’existence commence. Qu’en est-il du but ultime du monde ? Est-ce préserver la
vie aussi longtemps que possible et particulièrement pour l’homme, inclure le rallongement constant
de l’espérance de vie active suivi de conditions humaines conséquentes ?
2. Jusque-là, il n’existe pas de socle des connaissances et des savoirs qui soit universellement partagé.
3. Au plan des machines, universellement et pour tous, l’on ne dispose pas d’un fond organisationnel
de mémoire suffisant pour stocker et cumuler des connaissances, et qui soit partagé par tous (à la
fois) : agents humains et agent machines.
4. Atteindre zéro ambiguïté en machine est un objectif poursuivi par nos modélisations et formalisations
machine. Cependant, nos formalisations d’une certaine complexité ne sont-elles pas entachées par
cette ambiguïté innée des langages naturels (dans lesquels nous pensons) ?
68

--- page 89 ---
5. L’absence d’un système classificatoire universel fondamental est à noter. En cela, les classifications,
loin d’être fondées sur la logique pure, sont l’expression d’un consensus établi dans des groupes domi￾nants [195]. Elles résultent d’une suite de décisions d’ordre moral, politique et autre, qui contribue à
des moments donnés à valoriser un point de vue et à faire le silence sur un autre. Comme présentées
par Cote [69], on peut noter les dix classes ou catégories 18 et 19 d’Aristote qui ne sont pas adoptées.
Fort de tout ce qui précède, pour toute approche de construction d’ontologies formelles, il nous revient
soit de faire un choix raisonné portant sur une des méthodologies existantes ou à en combiner, soit à
procéder à un choix inspiré des méthodologies existantes. Cependant, un atout capitalisable existe : les
phases spécification des besoins, conceptualisation, formalisation, implémentation, maintenance et évolu￾tion sont présentes dans la plupart des méthodologies de construction de ces d’ontologies. En ce qui nous
concerne nous procéderons à un choix inspiré des méthodologies existantes basée sur diligent, NeOn et
ontoForInfoScience.
3.4 Représentation des connaissances et ontologies existantes dans des
domaines connexes
Des travaux connexes aux nôtres existent, que nous passons en revue. Nous distinguons ceux relevant
de la MT et ceux relevant de la MM. Ceux hors de la médecine sont relatés au chapitre 4.
3.4.1 Travaux relevant de la MT
Les travaux de G. Atemezing [21] [22] sont focalisés sur la validation des connaissances de la MT
gérée par un système d’agents. L’auteur aborde les concepts de rituel, de pratiques traditionnelles de soins
de santé (diagnostique, divination, croyance religieuse), de sorcellerie, de patient, de potion, de maladie,
de symptôme, de plante (concept utilisé en PO 20, une ontologie sur les plantes existante), de traitement
traditionnel. Il a réutilisé des ontologies comme PO, Pathogen Transmission Ontology (TRANS) 21, Human
Disease Ontology (DOID)
22 et Infectious Disease Ontology (IDO) 23. Toutes ces ontologies s’appuient sur
Open Biological Ontologies (OBO), une ontologie de fondement. Il aborde le volet métaphysique avec une
absence de modèle de validation (absence d’une interprétation par individu). Il parle d’un système multi￾agent se référant aux différents types d’acteurs humains et machines. Les concepts d’experts de domaine
et de médecins traditionnels ne sont pas nettement définis. Il n’aborde pas le fait que les PMT (médecins
traditionnels) sont des personnes ne sachant ni lire ni écrire dans une majorité large.
Les travaux de Ayimdji A. constituent un prolongement amélioré de ceux de Atemezing. Au Cameroun,
Ayimdji A et al via [23] et [24], ont réalisé une ontologie sur la MT avec Methontology. Ils ont décrit
le processus de la collecte d’une plante à travers le collecteur (son sexe, jeune ou vieux, son attitude
comportementale comprenant le fait qu’aucune pause n’est admise pendant cette collecte de la plante,
puis après collecte, la plante est directement transportée à la maison pour être utilisée sur le patient). La
18. https ://philosophie.cegeptr.qc.ca/wp-content/documents/Catégories.pdf consulté en 2015
19. substance, quantité, qualité, relation, lieu, temps, position, possession, action, passion
20. http ://www.obofoundry.org/ontology/po.html consulté en 2014
21. http ://www.obofoundry.org/ontology/trans.html consulté en 2015
22. http ://www.informatics.jax.org/disease consulté en 2015
23. http ://www.ontobee.org/ontology/IDO consulté en 2015
69

--- page 90 ---
Figure 3.10 – Icônes de VétoMed
période convenable de cette collecte importe également. Il relève que les guérisseurs ont du mal à accepter
que la MM donne des explications "scientifiques" aux causes des maladies surnaturelles . Les auteurs ont
implémenté l’outil SWI-Prolog (sémantique web interface). Dans sa méthodologie, le caractère verbatim
des connaissances résultant directement du dialogue ou des interview avec les PMT souvent analphabètes,
en plus du caractère tacite du domaine de la MT, n’est pas perceptible. Il n’aborde pas l’approche visuelle
de l’ontologie dans ces travaux.
Kamsu et al [127] ont effectué un certain nombre de travaux sur la MT Africaine en terre Camerounaise.
Ces travaux se rapportent à un graphe conceptuel avec une possibilité de raisonnement. Ils y abordent
les termes d’orientation de pharmacovigilance, d’alertes précoces, et de raisonnement temporel. Dans la
médication, les suppléments de plantes associatifs en terme de repas ne sont nettement définis (obligation de
prendre certaines décoctions après ou avant un repas. Ils utilisent la méthodologie Delphi pour l’élicitation
des connaissances basée sur l’anonymat pour la gestion de plus de consensus. Cependant, cet anonymat
devra pouvoir être dévoilé après validation afin de mieux caractériser les typologies d’experts et d’acteurs,
et de sources. Maintenant, cette technique de collecte ne met pas l’accent sur le fait que les PMT sont pour
la plupart illettrés . Ils définissent un outil collaboratif entre les acteurs de la MT et ceux de la MM. Le
formalisme de représentation des connaissances utilisé, est le graphe conceptuel (GC), dont la sémantique
et la syntaxe entre concept et individu/constante d’objet sont très réductrices voire soumises à l’intuition
de celui qui exploite le graphe. Kamsu n’a pas utilisé le formalisme OWL. Il aborde les concepts de plante,
ses parties utilisées, la maladie traitée, symptôme et signe, diagnostic, les modes d’administration. Ils traite
singulièrement du malaria. La distinction entre signe et symptôme est nette.
En Côte d’Ivoire, Brou [48] a construit VetoMed, un système expert à base d’icônes qui traite des
connaissances de la MT accompagnées par des représentations visuelles notamment des images visuelles.
La base de connaissances comprend 134 faits et 66 règles. L’association d’icônes correspondant à des faits
détermine d’autres faits. Réciproquement, étant donné un fait, il existe la possibilité de lister ses causes.
Par exemple, la conjonction additive d’une icône d’un animal avec celle du feux implique l’icône de la
fièvre. L’icône de l’animal de la figure 3.10 peut être améliorée de sorte à être plus générique et prendre
en compte l’ensemble des animaux. Celle présente sur cette figure exclut une bonne frange des animaux
comme la volaille. Cependant, les icônes sont de conception intuitives et manquent de consistance : il y a
une grande disparité entre celle du poulet et de la vache. De plus, il n’y a pas d’ontologie à proprement
parler : la base de connaissances résulte davantage d’un système expert (règles et faits).
Behou [37] a réalisé des travaux avec une approche d’apprentissage fondée sur une ontologie de la MT.
Aussi bien la définition que la mise en œuvre des aspects visuels et iconiques sont très limitées.
Zulazeze et al [249] ont réalisé des travaux de construction d’ontologie sur la MT hors Africaine. C’est
précisément la MT de la Malaisie sur les plantes. Il a construit une ontologie détaillant les principales
parties de la plante proche de notre vision. Cependant, dans cette ontologie, les fleurs et la sève ne
sont pas décrites dans les parties de plante. Cette description reste toujours limitée quant aux autres
70

--- page 91 ---
Langage naturel (français) Prenez cinq poignées de centella et faites bouillir avec
quatre verres d’eau puis buvez un verre de décoction
le matin, un verre midi et un verre le soir
Langage iconique icOnto
TABLEAU 3.9 – Traduction d’une phrase du langage naturel au langage iconique
ressources notamment minérales et animales utilisées en MT. Il n’aborde pas d’approche visuelle pour la
représentation iconique des connaissances.
Kuicheu N. C et al [138] abordent une ontologie d’icônes, IcOnto en MT au Cameroun, en définissant
l’icône b d’un concept X via X(a, b) , a étant le terme de X. En terminologie, le marquage distinctif entre
X et a est difficile à percevoir. Le langage iconique utilisé est limité en définition. Dans ce système icOnto,
on a la possibilité de passer par la traduction d’une phrase en langage naturel à une phrase iconique dans
le langage iconique. Pour exemple, on a en langage naturel : "Prenez cinq (5) poignées de centella et faites
bouillir avec quatre verres d’eau puis buvez un verre de décoction le matin, un verre à midi et un verre le
soir". Cette phrase a pour équivalent en langage iconique, la phrase iconique comme le montre la figure
dans le tableau 3.9.
Dans cette phrase iconique, une photo réaliste désignant la plante apparait dans les icônes. Du coup,
les constituants de cette phrase ne sont pas au même niveau sémantique et structurel , encore moins en
avoir la même base descriptive. En toute évidence, la sémantique telle que définie laisse la place à une
marge intuitive trop grande pour l’utilisateur en vue d’interpréter les icônes, puis la phrase iconique. Il
manque un alphabet clairement défini. En plus, les règles de traduction du langage naturel au langage
iconique ne sont pas explicites. Dans cette traduction, Kuicheu ne dit pas s’il utilise un interpréteur. De
plus nous relevons que centella est un genre de plantes qui comprend plus d’une cinquantaine d’espèces 24 :
cela n’est pas assez précis pour identifier la plante sans ambiguïté.
Yoruba Traditional Medicine (YTM) au Nigeria , a été l’objet de travaux menés par Omotosho et al
[172]. Une ontologie formelle sur la MT a été réalisée par cette équipe. Cette description ne prend pas
en compte tous les types de ressources médicinales. Celle qui est faite est focalisée sur les plantes mais
partiellement. Les principaux concepts sont plante, parties des plantes, les parties utilisées (écorce, racine,
feuille, tige, fruit et plante entière, ...) symptôme, signe, maladie. Il n’a pas tenu compte du caractère
analphabète des guérisseurs qui auront du mal à utiliser cette ontologie une fois à terme et mature.
L’approche d’ontologie visuelle n’est pas envisagée.
Pratheeba et al [197], ont démarré un projet de système expert sur la MT hors Afrique, au Sri Lanka. Ce
système est fondé sur une ontologie des plantes (indiennes) de la MT. Il ne vise pas un langage iconique.
Plusieurs autres travaux d’ontologie en MT asiatique surtout chinoise (TCM : Traditional Chinese
Medicine) ([184] [226]) existent mais en général ne traitent pas d’ontologie visuelle. Dans les ontologies
24. http ://www.theplantlist.org/1.1/browse/A/Apiaceae/Centella/ , 2017
71

--- page 92 ---
utilisées, la description simultanée des principales ressources constituées par les plantes, les animaux, et les
minéraux des recettes médicales traditionnelles, est très réduite. Les travaux sur les plantes sont dominants.
Les concepts couramment traités sont maladie, plante, partie de plante, signe et symptôme.
Nous avons dans notre étude fait presque abstraction des ressources métaphysiques en les notifiant
simplement sans les aborder en profondeur. Les sorties de terrain et de brousse pour aller en contact avec
les guérisseurs font l’objet de mention dans peu de travaux et dont pour beaucoup d’entre eux, leurs auteurs
se sont contentés des dispositions invariantes dans la description des ethnobotanistes en biosciences sur la
MT. La description tabulaire donne fréquemment les termes de colonnes suivantes : nom scientifique de
la plante, famille scientifique, partie utilisée de la plante, nom local de la plante, maladie traitée, mode de
fabrication, mode d’administration, origine ou pays d’origine. Une telle description des pratiques de la MT
peut en conséquence s’avérer superficielle et réductionniste, loin de révéler l’aspect holiste de traitement
d’un patient. Cet aspect holiste (cf sections 2.4.2 et 2.5.4.1 du chapitre 2) est bien, très caractéristique de
cette MT.
3.4.2 Travaux relevant de la MM
Nous avons plus tiré parti des techniques et méthodes de construction des ontologies existantes en MM
que leur réutilisation, vu la différence marquée entre les pratiques de la MM et celle de la MT. La plupart
des travaux reposent sur des thésauri, des taxinomies ou des ontologies. Cependant, ils ne comprennent
pas d’ontologie visuelle sauf les deux projets hors MT suivants.
Le Projet "VCM" de Lamy est un langage iconique pour l’accès aux connaissances sur le médicament et
aux guides de bonnes pratiques cliniques. Une ontologie visuelle est validée sur la MM. L’objectif principal
est la facilité d’apprentissage et la vitesse de lecture du praticien [140] [144]. La syntaxe iconique se fonde
sur trois bases iconiques notamment décrites dans la figure 3.11. Ces bases sont :
– les formes géométriques rond (absence de pathologie), carré (pathologie ou maladie), carré et triangle
associés.
– les couleurs : marron (antécédent étiologique), orange (risques futurs à encourir), vert (sous traite￾ment), rouge (état actuel) et bleu (test en cours).
– autres icônes : des symboles en termes d’instrument (ex : seringue), de patient, d’estomac, de croix
(médicament), de prélèvement (récipient en tube), ...
Le langage iconique VCM cible principalement les praticiens de la MM. Il est validé par un consortium
de médecins. De plus, la sémantique du langage VCM a été formalisée par une ontologie OWL [143].
Miria et al à travers [67], ont réalisé AGUIA (Autonomous graphical user interface assembly for clinical
trials semantic data services). C’est un système graphique, une application web frontale conçue à l’origine
pour gérer les données cliniques, démographiques et biomoléculaires des patients recueillies lors d’essais
cliniques au centre de cancer MD Anderson au Texas (USA). AGUIA utilise un formalisme web sémantique,
un cadre de description de ressource (RDF) et une base de connaissances de bas en haut. La mise en œuvre
de tous ces aspects a pour outil support, S3DB (Simple Sloppy Semantic Database) en qualité de point
de départ pour l’assemblage d’interface du client. S3DB contient G-box avec 11 éléments graphiques. La
construction des icônes sur la base des onze (11) autres n’est pas clairement définie.
72

--- page 93 ---
Figure 3.11 – Syntaxe de l’alphabet de base du langage iconique VCM
3.5 Synthèse
Les ontologies, presque deux à trois décennies après leur apparition, sont aujourd’hui incontournables
pour l’organisation des connaissances investies d’un ancrage sémantique consensuel. Elles contribuent éga￾lement à la capitalisation évolutive des connaissances. Ces ontologies peuvent répondre à de nombreux
besoins et objectifs, surtout grâce à l’intégration en leur sein de possibilités d’axiomatisation et d’utili￾sation de systèmes raisonneurs inférentiels. Elles sont utilisées relativement à une communauté d’experts
à l’instar de celle des PMT qui nous préoccupe dans ce travail. Plus précisément, nos besoins portent
principalement sur le partage et la pérennisation des connaissances et expériences de la MT. Dans la ligne
de réflexion conduisant nos activités de recherche, nous considérons les ontologies comme des repré￾sentations de connaissances s’insérant dans les systèmes d’information en vue de leur apporter une
dimension sémantique qui leur faisait défaut jusqu’ici. Nous nous intéressons beaucoup plus aux ontolo￾gies de domaine (définies comme une représentation formelle et validée par les experts de ce domaine). Il
importe alors ici l’identification des entités conceptuelles (concepts et relations) pertinentes de ce domaine
et de leur sémantique. Ces ontologies sont bâties sur la base d’un niveau conceptuel intégrant à la fois
les connaissances terminologiques d’un domaine et l’expression de la sémantique de celui-ci. Elles doivent
conserver leur indépendance vis-à-vis des usages opérationnels spécifiques à une application donnée.
Vu les caractéristiques toutes particulières de la MT, et du fait de l’existence dans ce domaine que des
ontologies embryonnaires, il nous semble ne pas être indiquée la réutilisation automatique des ontologies
et RTO existantes. De même, les ontologies et RTO existantes de la MM ne peuvent être réutilisées telles
quelles à cause des différences importantes entre MT et MM. En revanche, les politiques de ces ressources
(ontologies et RTO), leurs stratégies, leurs méthodologies et méthodes de construction nous seront d’une
grande utilité.
L’iconisation de concepts est une partie importante de notre travail. Au regard des solutions à apporter,
cette approche visuelle n’est pas en marge des ontologies formelles. Pour cela, dans le chapitre suivant,
nous abordons des stratégies de représentation visuelles. En outre, l’aspect visuel étant analogique, il est
nécessaire d’y asseoir une sémantique sans ambiguïté et intelligible par la machine, ce que les ontologies
formelles rendent possible.
73

--- page 94 ---
Chapitre 4
Icône et Langage iconique
Sommaire
4.1 Importance de l’icône . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
4.2 Définition et constance de l’icône . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
4.3 Icône et communauté . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.4 Étude et décomposition des icônes . . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.5 Exemples de langages iconiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
4.6 Langages iconiques formalisés . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
4.7 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
74

--- page 95 ---
Par langage, nous comprenons un système de signes permettant la communication. En général, c’est
tout moyen d’expression, de communication et d’instruction à base de signes. On pourrait par exemple
citer le langage humain, le langage animal, le langage informatique, le langage des panneaux de circulations
routières, le langage gestuel, le langage olfactif. En réalité, nous communiquons par nos sens. En la matière,
au cours de son histoire, l’homme a développé certains sens au détriment d’autres, soit volontairement soit
involontairement.
Ici, l’homme est placé au centre de la communication à travers deux communautés d’agents : celle des
agents humains dont il fait partie et celle des machines. Ceci met en relief trois types de communication
comme identifiés en section 3.2.11.1 du chapitre 3.
Basé sur une aire linguistique et sociale, le langage utilisé par l’homme dit langage naturel, est bien la
manière de parler et de s’exprimer. C’est une forme de langage qui n’est pas celle des machines. Depuis
l’apparition de l’ordinateur (environ 1950), au moins cinq (5) générations de langages (1GL, 2GL, 3GL,
4GL, 5GL) existent. Inspirés ou conçus sur le modèle de factorisation modulaire, les quatre (4) dernières
générations de langages (2GL, 3GL, 4GL, 5GL) sont superposables via une transformation structurelle
(translation) au langage machine (binaire), la 1GL.
Tous les langages écrits sont à différentes échelles de formalisme [154].
Dans notre environnement de vie, tout ce qui est de l’entendement humain est décrit sous le triptyque
sujet verbe complément. Ceci traduit bien le fondement des langages du web sémantique s’appuyant sur un
réseau de termes de concepts représentant le sens d’un champ d’informations qui incarne une interprétation.
Pour obtenir un langage visuel, il est difficile de suivre l’ensemble des principes de construction d’un
langage écrit avec un alphabet assujetti à des sons phoniques en correspondance avec les objets du monde,
bien qu’il s’agit des mêmes objets auxquels ce langage visuel fait référence. En conséquence, dans le cadre
du domaine de la thérapie traditionnelle, cible de notre travail, il faut noter l’existence d’un réseau où
collaborent un nombre non défini au préalable et même illimité de concepts et termes référant ces objets.
Alors établir une icône par concept via le langage iconique s’avère non aisé. En plus, cette difficulté croît
quand on doit doter la machine (ordinateur), de l’intelligibilité sémantique des icônes.
Après une présentation de l’icône sous un aspect sémiologique (sémiotique), il s’en suit un état de l’art
des langages iconiques (formalisés et moins formalisés).
4.1 Importance de l’icône
Une grande mutation du texte et de l’oral vers l’image iconique est en cours, et pourrait s’accentuer
au point de devenir une marque caractéristique du XXI siècle. Ce phénomène est presque comparable à
celui au début de l’église romaine. Ceci rejoint la pensée de Tijus et al [228].
Dans la société de l’information, la parole et le texte laissent de plus en plus la place à l’image avec ses
multiples formes. Parmi celles-ci, nous notons l’icône, la photographie (les appareils photo sont à portée
de main à travers les téléphones mobiles), le dessin, le schéma, le pictogramme, l’idéogramme, le logo, la
graphie, le diagramme, ... Ceux-ci sont partout : dans les notices de médicaments de la MM et celles des
appareils électroménagers, la partie externe visible des emballages de toute sorte, les IHM (interface homme
machines) des logiciels d’ordinateurs et de téléphone mobile, les insignes et indications dans les aérogares,
les aéroports, les gares routières [159], les centres de santé de la MM, les affiches (de représentation
de maladies sous forme de dessins, ...) postées aux abords des étalages et des centres du tradipraticien
(PMT) africain, les panneaux de signalisation routière, les panneaux publicitaires, la sécurité, les signes
d’interdiction dans les zones d’industries chimiques, de circuit de production d’électricité (moyenne et haute
tension) et de déchets nucléaires toxiques, les symboles et signes d’autorisation et d’avertissement relatifs
75

--- page 96 ---
aux issues de secours des salles de masse et lieux populaires (amphithéâtre, toilettes publiques, stades,
podiums, ascenseurs, parking), les consignes sur la flore et la faune classées, les réseaux sociaux (Facebook,
Twiter, Instagram) et le web, les bandes dessinées (presse et TV), les vues symboliques et synoptiques via
Googlearth (à l’échelle), les signes de centres et apparats religieux [137], les vitraux d’église, les logos et
ceux accompagnant les marques déposées de fabrique et les sociétés, les fascicules et ouvrages scolaires et
académiques, les véhicules de transport et de déplacement (voiture, camion, car, train, métro, trameway,
bus, bateau, avion, ...) tant pour le conducteur/pilote (tableau de bord) que pour le simple usager passager,
les indications flottantes pour la navigation marine, le monde des peintres, les dessins sur les habillements
et les vêtements (chaussures, pagne et tissu africains, asiatiques, occidentaux), consignes, signes et dessins
dans l’hôtellerie et tourisme, dessins et signes sur les monuments et dans les musées, sur les meubles et
façades d’immeubles, sur les couverts (cuisine, restauration, ..), dans les centres commerciaux (des plus
insignifiants aux hypermarchés), etc.
Les premières apparitions des pictogrammes et des icônes d’information se sont faites de manière
sectorielle à savoir dans le tourisme pour les déplacements humains, et dans l’industrie pour les machines
et les produits. En somme, l’image en général et surtout celle miniaturisée à l’échelle de pictogramme
ou d’icône devient omniprésente. Pendant de longues périodes avant l’époque contemporaine, pour lutter
contre l’analphabétisme et l’isolement, l’image a eu toute son importance pour véhiculer l’information
[159]. A l’époque contemporaine, le texte même quand il est dominant, continue d’être parfois agrémenté
d’images (journaux, livres, ..).
Après la télégraphie, émerge une nouvelle forme de communication à grande vitesse fondée sur les
évolutions des sociétés (au plan démographique, culturel et économique). L’intra exode est augmentée de
l’inter exode. L’usage à grande échelle, de plus en plus croissant de l’image iconique et pictographique se
fonde sur l’impérieuse nécessité de communiquer toujours plus rapidement (les icônes sont lues plus vite
que le texte) et plus largement (les icônes peuvent être comprises au-delà des frontières [28] et barrières
linguistiques).
A cela, il faut rajouter les raisons liées aux mutations sociales : une frange importante des populations
illettrées soit transitoirement, durablement ou à vie, est fortement demandeuse de son intégration dans
la société urbaine. Certaines catégories des personnes handicapées par exemple aphasiques ne sont pas en
reste.
Sortir et même s’éloigner le plus possible de l’analyticité du texte par l’émergence d’un message plus
laconique et plus synthétique inonde notre quotidien. Ce message est présenté comme un pur stimulus
[233] tout en s’inscrivant dans l’obtention de résultats qui satisfont le mieux les objectifs attendus. L’image
iconique peut incarner un tel message également quand elle est établie selon un certain nombre de règles
clé. Ainsi, sa représentation endosserait davantage un caractère de spontanéité sémantique pour un groupe
d’utilisateurs donné (communauté des PMT par exemple). Le rôle joué par l’informatique en particulier
et les TIC en général est crucial : indubitablement, les images et icônes de toute sorte foisonnent sur le
web. En somme, l’informatique et Internet facilitent énormément l’utilisation et la diffusion des icônes
aujourd’hui.
4.2 Définition et constance de l’icône
Nous intéressons à définir une icône et un langage iconique et ensuite à mettre en exergue leur propriété
immanente.
76

--- page 97 ---
4.2.1 Définition de l’icône
Icône se dit d’un signe qui entretient une similitude, une analogie avec ce qu’il désigne. Nous pouvons
définir une icône comme une image simplifiée, stylisée et de petite taille, qui est utilisée pour représenter
un sens précis, par exemple pour identifier une consigne dans un lieu public, une marque sur un produit, un
logiciel sur un ordinateur, ... Klinkerberg 1 dans [233], définit une icône comme étant un signe motivé par
la ressemblance, avec des découpages non correspondants (e.g : maquette d’avion, imitation d’un parfum,
bruitage du générique d’un film, une onomatopée).
4.2.2 Définition d’un langage iconique
Un langage iconique est un langage composé d’un lexique de primitives visuelles (par exemple des
couleurs et/ou des pictogrammes) et d’une grammaire graphique pour assembler les primitives et former
des icônes. Par combinatoire, il est ainsi possible de créer un grand nombre d’icônes à partir d’un jeu de
primitives restreints.
Une icône d’un langage iconique est généralement composée de plusieurs iconèmes. Un iconème est un
morceau d’icône, auquel est associé une partie du sens de l’icône. Un iconème peut correspondre à une
ou plusieurs primitives. Par exemple, dans le panneau routier "interdiction de tourner à gauche", le cercle
rouge et barré, entourant une flèche est un iconème (composé d’une couleur et d’une forme) et signifie
l’interdiction (cf ligne 4 du tableau 4.1). Enfin, un iconème pur est un iconème qui porte sur une et une
seule unité signifiante, marquée sans ambiguïté.
La division en iconèmes permet une sorte de description de l’image iconique par découpage reposant
sur des unités signifiantes préalablement définies. C’est le rôle joué par les iconèmes. Nous estimons que le
découpage iconémique est une source d’enrichissement de la sémantique (graphique), les iconèmes pouvant
être inféodés à des concepts dans une ontologie formelle. Ils constituent un point de départ pour l’uniformité
iconique et sémantique de concepts dans ce domaine de la MT en partant d’une ontologie formelle.
4.2.3 Constance de l’icône
L’icône permet à deux personnes ne pratiquant pas les mêmes langues de communiquer, d’échanger et
même de se comprendre.
A travers la figure 4.1, on a l’unicité iconique qui transcende espace, temps et contexte multilinguiste
(de langues vivantes opposées à celles en extinction ou mortes). Plus que l’immédiateté, l’icône renvoie
spontanément son utilisateur à l’objet dont elle fait référence. L’icône est la même car persistante, atem￾porelle. Comme propriété immanente, elle demeure constante. Ce qui n’est pas le cas de certains langages
terminologiques (naturels (écrit, oral), semi-formels).
Lorsque le langage naturel est appris par deux personnes, puis est utilisé par celles-ci, il donne une
compréhension à caractère immédiat. Il peut en être de même pour la compréhension partagée d’une icône.
Toute perception par la vue est renvoyée en une image ou représentation mentale. C’est à partir de cet
instant que l’interprétation commence. Pour D. Le Breton, la perception 2 n’est pas une coïncidence, mais
une interprétation. Les images iconiques fixes sont celles concernées par nos travaux présents. Les images
1. http ://www.signosemio.com/klinkenberg/index.asp 2017
2. https ://fr.scribd.com/document/348324354/semiologie-vp-pdf consulté en 2015
77

--- page 98 ---
Figure 4.1 – Caractère persistant et inchangé de l’icône
mobiles ou filantes en sont exclues. Ainsi, nous nous limiterons ici aux icônes visuelles, et nous laisserons
de côté les icônes sonores ou gestuelles.
4.2.4 Exemple d’icônes
Quelques exemples d’icônes, d’images iconiques ou de pictogrammes dans notre vécu quotidien, sont
donnés à travers les tableaux 4.1 et 4.2.
4.3 Icône et communauté
L’intérêt premier de l’image en général et en particulier de l’icône est l’atteinte du but sémantique
par ce qu’il y a de vraiment essentiel en matière de représentation. Se rapportant à l’intelligibilité de
l’homme, l’icône par son usage, pousse à l’atteinte de la compréhension par la simplicité. Ainsi, elle donne
la possibilité à l’homme de se connaitre et comprendre son environnement de vie, puis celui du monde et
de l’univers.
"Un dessin ou un bon croquis vaut mieux qu’un long discours" est une pensée de Napoléon Bonaparte 1er 3
,
qui connaît un regain croissant en popularité de nos jours, depuis l’avènement de "l’ère de l’information"
et du web, et mieux actuellement, de "l’ère de l’iconique ou de l’iconicité".
Whiteside [239], a soutenu et montré la supériorité de la communication iconique et pictographique
sur la communication textuelle et orale dans le dialogue homme et machine.
Par exemple, dans sa conception d’un langage iconique pour des personnes malades en vue de rompre
avec l’isolement médical et relationnel du patient, Brangier [46] a retenu 84 icônes les plus régulières parmi
celles réalisées par des sujets malades d’aphasie pour représenter une centaine de phrases qui leur sont
familières dans leur lieu d’hospitalisation. Ces icônes sélectionnées sont remises à la disposition de 38
autres sujets. Ces derniers suite à l’écoute de la centaine de phrases prononcées, doivent faire correspondre
chacune d’elles avec une ou plusieurs icônes. "je voudrais aller au fauteuil.", "merci.", "je voudrais me
brosser les dents." et "j’ai froid." sont entre autres quatre exemples de ces phrases. Les scores obtenus de
l’interprétation des icônes varient entre 0 et 100%. C’est une technique simple qui prouve la possibilité
3. https ://www.histoire-pour-tous.fr/histoire-de-france/3436-napoleon-ier-empereur-1769-1821.html consulté en 2014
78

--- page 99 ---
Concept
Représentation du concept (image, image
iconique, image pictographique)
feuilles, fruits et fleurs de neemiers
(azadirachta indica)
ange Saint Michel
interdiction de tourner à gauche
carrefour giratoire
social media indication
raccourcis accompagnés de texte
(environnement MS Windows)
centre de santé
TABLEAU 4.1 – Exemples, d’images, de pictogrammes et d’icônes
79

--- page 100 ---
Concept
Représentation du concept (image, image
iconique, image pictographique)
configuration de téléphone
portable
soleil brillant à l’aube
restaurant à mets
Homme, homme et femme
danger de mort
interdiction de fumer
toilettes publiques
paludisme
TABLEAU 4.2 – Exemples, d’images, de pictogrammes et d’icônes (suite et fin)
80

--- page 101 ---
Figure 4.2 – Extraction d’un langage iconique pour les personnes handicapées aphasiques
de développer un langage iconique dans une communauté donnée. Pour une idée plus nette des icônes en
rapport de correspondance à une suite de phrases, une extraction de ce langage iconique est donnée en
illustration par la figure 4.2. C’est également une technique simple de validation d’un langage iconique.
L’icône peut revêtir un caractère universel [159]. Elle permet d’atteindre une certaine universalité via
la ressemblance. Cette icône elle-même, éventuellement associée à son apprentissage, nous permettent
d’arriver à une compréhension commune et consensuelle de la réalité dénotée par l’icône. Une même icône
présente partout et accessible de partout permet également de partager la sémantique de l’information
qu’elle véhicule au plan universel. A ce titre, les icônes sont à même de transcender les barrières linguis￾tiques dans une communauté.
Mon expérience personnelle m’a montré qu’un illettré à qui on a appris à utiliser un téléphone portable
(mobile), ou, plus clairement un individu à qui l’on a appris à utiliser les icônes de l’interface d’un téléphone
mobile, arrive par la suite à se les approprier parfaitement (e.g : artisan rural de mon village qui n’a pas
connu l’école). Même en changeant de téléphone, peu importe la marque, il arrive à en faire un bon usage
(s’en servir).
81

--- page 102 ---
Des individus illettrés ou non ayant des aires linguistiques différentes ou même avec des courants
culturels distincts, des milieux et des vécus totalement différents, et qui notoirement n’ont aucune base
commune linguistique, arrivent à communiquer par le biais des icônes, des images, des pictogrammes (e.g :
signes dans les domaines scientifiques surtout en mathématiques et physiques, médecine, botanique, etc).
La standardisation des icônes dans certains domaines est très avancée et obéit à des normes ISO
[233] : signes de panneau de circulation, signes des aéroports, signes des centres hospitaliers, signes de
restaurations et hôteliers, signes agricoles, signe de sécurité, signes des issues de secours dans les bâtiments
et les immeubles etc.
Cette force de l’image en général et de l’icône à travers le (ou un) langage iconique en particulier, peut
devenir également sa faiblesse si elle n’est pas soutenue d’une part par un certain nombre de principes
dans sa construction et dans son utilisation, et d’autre part par l’apprentissage aux fins de préserver sa
sémantique au fil du temps.
4.4 Étude et décomposition des icônes
Dans cette section, nous présenterons rapidement différentes approches pour l’étude des icônes. Nous
insisterons notamment sur ce qu’elles peuvent nous apporter lors de la conception de nouvelles icônes.
4.4.1 Sémiologie des icônes
La sémiologie ou sémiotique est la science qui étudie les signes, leur sens et la manière dont ils fonc￾tionnent. Les icônes sont des signes visuels, et sont donc concernées. Un signe visuel est la réunion d’une
perception rétinienne (œil) et de l’image mentale associée 4
. La perception rétinienne se rapporte en clair à
quelque chose qu’on perçoit par la vue. La chose vue se retrouve (est projeté) sur la rétine puis transmise
au cerveau.
Deux figures emblématiques ont marqué la sémiologie (la sémiotique). Il s’agit de Charles Sanders
Peirce et Ferdinand De Saussure.
Dans le cadre de nos travaux, la sémiologie d’obédience peircienne a plus pesé, quand bien même celle
de Saussure ne nous a pas fait défaut pour fortifier notre compréhension des signes (symptôme, icône,
symbole, indice).
A travers [41], [68] et [233], Peirce présente le signe sous forme d’indice, d’icône ou de symbole (appelé le
trichotome de l’objet) comme le montre plus explicitement le tableau 4.4.
L’analogie de l’icône vise la spontanéité de la reconnaissance (mieux la ressemblance spontanée) du
référent à travers l’icône, puis de l’icône elle-même par les destinataires.
Il faut comprendre que celui à qui l’icône est renvoyée doit également recevoir un stimilus réactif
(effet manifeste mais silencieux, effet visible ou vif dans le changement de comportement). Admettons cela
sous le vocable de réactivité dans une tâche donnée. Cette analogie repose sur une convention apprise
préalablement codant en correspondance associative l’icône et son objet. Le signe a un lien conventionnel
avec son objet ou est reconnu à partir d’une norme apprise. C’est même le cas des langages oraux et écrits.
Les trois types de signes de Peirce ont chacun leurs avantages, mais le signe iconique est préférable lorsque
l’on recherche l’universalité.
4. http ://www.surlimage.info/ecrits/semiologie.html consulté en 2015
82

--- page 103 ---
Types
Peircéens
de signe :
(trichotome)
Fonction Description et exemple Catégorie de signe Relation à priori
entre signifiant
et signifié
indice contiguïté de
faits
L’indice est un signe qui entretient un lien
physique avec l’objet qu’il indique. E.g : la
fumée pour le feu ou encore les nuages pour
la pluie ; montrer le paquet de cigarette
pour demander une cigarette, grattement à
la porte permettant de comprendre que le
chien manifeste d’entrer, signe symptôme
d’une réalité complexe, bouton de furoncle,
percevoir la queue du lion camouflé, le lion
arrêté en face à 50 m de soi.
le signifiant est sur le
même plan de réalité
que son objet
(référent).
identité (totale ou
partielle)
symbole fonctionnent
par
convention
Le symbole entretient avec ce qu’il
représente une relation arbitraire,
conventionnelle. Le signe symbolique rompt
toute ressemblance et toute contiguïté avec
la chose exprimée. E.g : le drapeau d’un
pays africain, deux symboles en MM dont
l’un exprimant la masculinité ou l’autre la
féminité, la langue et le signe linguistique
(syntaxe et lexique), le calcul
mathématique.
le signifiant n’a pas
de rapport autre que
conventionnel avec
son objet (référent).
aucune relation de
ressemblance
(symbole établi
par pure
convention, par loi,
par habitude
culturelle) pour
référer un objet
icône similitude L’image est classée sous cette catégorie du
fait qu’il y a un rapport d’analogie entre le
signifiant et le référent. Les signes iconiques
sont des représentations analogiques
détachées des objets ou phénomènes
représentés. e.g : l’icône d’une plante.
le signifiant ressemble
à son objet (référent).
analogie,
ressemblance
TABLEAU 4.4 – Types peircéens de signe
83

--- page 104 ---
Figure 4.3 – Triangle sémiotique de base selon Peirce
NB : En outre, autour de ces trois types percéens de signe (indice, symbole et icône), il manque un
consensus entre sémioticiens (Peirce, Hegel, Wallon, Jung ...) selon [31]. En lieu et place de ces trois types
peircéen (indice, symbole et icône), certains de ces sémioticiens excepté Peirce lui-même, parlent encore de
signal, indice, icône, symbole, signe et allégorie [31]. Cette contradiction nous réconforte dans notre choix :
icône. Nous admettons ainsi icône pour supplanter l’ensemble de ces termes (signal, indice, icône, symbole,
signe et allégorie). Icône est donc suffisamment acceptable pour le langage iconique envisagé dans le cadre
de nos travaux.
Relativement à son alphabet, les symboles de la langue française (langue parlée et écrite), ne sont
pas des images. Nous parlons de terme quand le symbole est utilisé. Ce sont ces termes, les signifiants
que nous dressons "canoniquement" en classes (concepts axiomes avec consensus) en LDs, inspirés des
symboles logiques et mathématiques.
Selon C. Peirce S., un signe a trois dimensions de compréhension à savoir son objet, son icône et son
interprétant. Saussure en a une perception double : signifiant et signifié. Nous optons pour le signe Peircien
pour son aspect plus pragmatique.
4.4.2 Triangle sémiotique
Nous présentons succinctement le triangle sémiotique (ou sémiologique) au sens de S. C. Peirce, formé
par les concepts clés : signifié, signifiant et référent (voir figures 4.3 et 4.4).
Ces concepts clés sont explicités dans ce qui suit.
– le référent est un objet concret ou imaginaire de la réalité observable. Il a des caractéristiques
propres. Il peut devoir son existence à l’assemblage d’autres objets. Il peut être immatériel comme
un sentiment, une émotion, un concept abstrait (une vitesse, liberté, grandeur, ...). Peuvent être
substitués au terme référent les éléments objet, fait, individu, observable. Ce sont des continuants
84

--- page 105 ---
Figure 4.4 – Triangle sémiotique signifié-signifiant-référent de Peirce inspiré de [118]
(endurants) et occurrents (perdurants). Ils sont des objets abstraits ou concrets (matériels) sous un
autre prisme.
– Le signifié est le sens qu’on donne aux choses. Il est une abstraction qui se rapporte au référent
faisant partie de la réalité. On peut parler du monde mental ou du concept. C’est l’idée qu’on se fait
de quelque chose de tangible ou d’immatériel. Le signifié fait partie de la réalité subjective. Il peut
être remplacé par idée, interprétant, modèle mental. C’est le concept [236], l’image mentale, une
représentation générale et abstraite d’un objet jouant le rôle de relais entre le signifiant et l’objet.
– Le signifiant est une chose de la réalité objective qui a la fonction de représenter, de dénoter un
référent. Dans l’exemple donné sur la figure 4.4, on a le signe graphique (croquis ou icône d’arbre)
ou signe terminologique (arbre) qui représente spécifiquement un arbre et symbolise le concept
"arbre". Mais les signes ne renvoient pas directement à la réalité mais passent par l’intermédiaire
des signifiés. Le signifiant est de même dit representamen.
Pour Peirce, un signe, est "quelque chose qui tient lieu pour quelqu’un de quelque chose sous quelque
rapport ou à quelque titre" ([118]). Nous donnons l’exemple d’une plante avec un signifiant symbolique (ou
terminologique) qui est "arbre" et un signifiant graphique, la "silhouhette arbre" qui est un pictogramme
(cf figure 4.4).
L’analogie poursuivie par Peirce entre le signe iconique et son référent, constitue un support solide
à celle de Carlos [52] qui considère la trilogie de stratégies de représentation dans les icônes. Ces trois
stratégies sont :
– la similarité visuelle ou analogie ;
– l’association sémantique ;
– la convention arbitraire nécessitant un apprentissage préalable (e.g : drapeau d’un pays).
Pour représenter iconiquement des concepts concrets, c’est à dire des objets matériels, la similarité
visuelle (analogie) est la stratégie qui semble la plus appropriée. Pour les concepts abstraits (pensée,
processus, activité, ...), la règle d’association sémantique est plus appropriée à appliquer pour leur repré￾sentation iconique, suivi de la règle de convention arbitraire.
Tout icône ou tout iconème est réalisé par application d’au moins une de ces trois règles.
85

--- page 106 ---
Lois de la théorie du
Gestalt (GestaltThéorie)
Expression élément de connaissance
de forme de base
loi de proximité ou de la
régularité
Des élément proches sont plus facilement
perçus comme appartenant à une forme
commune que des éléments éloignés
loi de similarité (ou
d’égalité)
des éléments de la même forme ou de
même taille sont plus facilement vus
comme appartenant à une même forme
d’ensemble
loi de bonne continuation
on a tendance à naturellement continuer
de façon rationnelle une forme, si elle est
inachevée
loi du destin commun
les choses et les points qui se déplacent
selon une même trajectoire apparaissent
groupés dans une même forme
loi de fermeture
une forme fermée paraît plus prégnante
qu’une forme ouverte qui ne constitue pas
réellement une forme tant qu’elle reste
incomplète
TABLEAU 4.5 – Cinq (5) lois émanant de la Gestalt
4.4.3 Théorie de la Gestalt
Pour mettre en œuvre la similarité visuelle dans les icônes, il est important de pouvoir expliquer
quelles formes globales seront perçues dans l’icône, et le cas échéant dans les iconèmes qui composent
l’icône elle-même.
Cette manière de procéder est inspirée de la Gestalt 5
. Selon [236], la Gestalt signifie "mettre en
forme, donner une structure signifiante". Plus explicitement, en parlant de Gestalt, il s’agit d’un ensemble
structuré où chaque élément, chaque processus ne peut s’envisager que dans son rapport au tout. La théorie
de la Gestalt propose des lois pour expliquer pourquoi certaines formes sont perçus au détriment d’autres
formes. Ces lois ont notamment été appliquées à la perception visuelle. La Gestalt beaucoup utilisée dans
les sciences cognitives comme en psychologie et les arts plastiques (image et dessin) et bien d’autres.
Pour exemple, la même table prend une signification différente selon qu’elle est recouverte de livres et
de papiers, ou d’une nappe et de feuilles séchées de plantes (sa "Gestalt" globale ou d’ensemble a changé).
Cinq lois émanent de la théorie structurale de la Gestalt que nous présentons dans le tableau 4.5.
4.4.4 Propriétés des icônes
Suite aux trois types de signes et aux cinq lois du gestaltisme, nous pouvons ajouter d’autres critères
importants à considérer lors de la conception d’icônes : les cinq normes d’intérêt de l’image iconique.
5. s http ://bounie.polytech-lille.net/multimedia/multimedia.htm
86

--- page 107 ---
Cinq propriétés doivent donc être considérées lors de la conception d’icônes [159] :
– Par simplicité/complexité, il faut entendre la non surcharge de l’icône ;
– Le pragmatisme iconique, consiste à rendre opérationnelle et pratique l’utilisation de l’icône. Ceci est
lié à la propriété précédente mais surtout le long texte iconique est à éviter. Quel est par exemple le
nombre d’iconèmes (d’icônes également) maximal, acceptables dans une icône. Par exemple combien
d’icônes de plantes à admettre dans l’icône d’une recette voire d’un remède traditionnel. Les icônes
de posologies, contre associations (ressources médicinales plantes), contre indications (contre état
patient (jeune, adulte, genre, femme en grossesse)) sont concernées par ce même type de question￾nement. Comment maintenir la spontanéité, l’immédiateté à tout point de vue (degré de modularité
et grain convenable) ;
– Familiarité de l’icône avec l’utilisateur ;
– Le sens donné à l’icône ;
– la distance sémantique. C’est le caractère relationnel et fermé (hermétique) qui lie l’icône à l’objet
représenté par cette icône. Il y a notoirement le degré d’évidence de la reconnaissance de l’objet par
l’intermédiaire de l’icône. Il s’agit simplement de la similarité. C’est une distance qu’on voudrait
faire tendre vers zéro[159].
4.5 Exemples de langages iconiques
Les tentatives de disposer au plan scientifique d’un langage iconique ne sont pas nombreuses et encore
moins d’un langage iconique véritable.
Néanmoins, nous décrivons quelques exemples de langages iconiques dans ce qui suit.
– En 1906, le suisse Ferdinand de Saussure, un linguiste, a initié une sorte de langage iconique dé￾nommée image fonctionnelle ou signe-fonction à but de science générale des signes, avec les apports
concertés du scientifique mathématicien Shannon, et de l’anthropologue Lévi-Strauss et toute la lin￾guistique. La sémiotique prend en considération la manière dont les signes sont utilisés pour désigner
les choses et les états du monde [233].
– Le langage Bliss [147] est une sémantographie [46], composée d’une centaine de symboles pictogra￾phiques et d’idéogrammes (inspirés du chinois) et des symboles arbitraires lors des années 1942 à
1965. Bliss eût la ferme volonté d’aboutir à une langue universelle au sens du rêve d’un symbolisme
également universel de Leibniz. Bliss créa l’iconicité comme l’organisation structurelle de l’expres￾sion reflétant le contenu. Dans cette organisation chaque signe doit ressembler à la chose à laquelle il
renvoie. Contrairement à son prédécesseur Wilkins, Bliss vise un langage qui n’exige aucun appren￾tissage. Cependant, les symboles graphiques ne peuvent pas représenter certains concepts abstraits
(comme la négation) sans faire appel à des conventions qui doivent être apprises. Face au caractère
universel assigné au langage Bliss, l’impasse a pris le dessus. Son utilisation a fortement diminué
d’échelle pour se limiter aux enfants souffrant d’IMC (infirmité moteur cérébrale).
– L’isotype (International System Of Typographic Picture Education, traduit en français par Système
International d’Éducation par les Images Typographiques) [28] [183] fonctionne pareillement au
langage de Bliss, mais les icônes sous forme de pictogrammes sont plus représentatives des objets
représentés. Ces icônes ont des traits caractéristiques des objets qu’elles représentent (voir figure
4.5).
87

--- page 108 ---
Figure 4.5 – Isotype de Neurath (1882-1945), un exemple de symboles et de combinaison symbolique
– Comme mentionné précédemment, Brangier [46] a proposé un langage iconique pour des personnes
aphasiques en vue de rompre avec l’isolement médical et relationnel du patient. Pour une idée plus
nette des icônes en rapport de correspondance à une suite de phrases, une extraction de ce langage
iconique est donnée en illustration en figure 4.2.
– Le langage iconique médical VCM (Visualisation des Connaissances Médicales) de Lamy [141], il
intègre trois types de primitives graphiques : couleurs, formes géométriques (rond, carré, triangle)
et pictogrammes (formes plus complexes). Ce langage iconique permet de représenter les principaux
concepts médicaux : symptôme et diagnostic du patient, antécédents médicaux, risques futurs, trai￾tements, examens, ... VCM a été utilisé dans plusieurs applications médicales : dossiers patients
hospitaliers et en médecine générale, consultations de guides de bonnes pratiques cliniques ou de
documents listant les propriétés des médicaments, moteurs de recherche médicaux, ... Ce langage n’a
pas pour objectif de remplacer le texte (comme le cherchait Bliss), mais plutôt d’enrichir le texte
pour faciliter le repérage et le filtrage visuelle pour faciliter la recherche d’information dans un texte.
Une évaluation sur un petit groupe de médecins a montré que VCM permettait d’accéder deux fois
plus rapidement à l’information, tout en faisant deux fois moins d’erreurs [142].
4.6 Langages iconiques formalisés
Nous abordons ici, la notion de langage et la mise en relief de deux langages iconiques formalisés existants.
Deux langages iconiques formels ont été réalisés avec des niveaux de formalisation différents. L’un est de
Kuicheu moins formalisé que l’autre, celui de Lamy ayant fait l’objet de validation.
S’agissant de Kuicheu [138], il a réalisé IcOnto, une ontologie d’icônes du domaine de la MT au
Cameroun en Afrique centrale. Il se fonde sur une définition algébrique de l’icône X via un couple X(a,
b) dont la première composante est le sens (logique) et la deuxième l’image (physique). Dans ce système
icOnto, on a la possibilité de passer par traduction d’une phrase en langage naturel à une phrase iconique
dans le langage iconique.
Le cheminement d’obtention ou simplement la provenance des images ou icônes n’est pas explicité. Le
choix des icônes est très intuitif. On a en plus des icônes de standing différent : il y a des icônes en image
photo réaliste (plante "centella") et d’autres en dessin ("soleil levant" ou matin).
Relativement aux travaux de Lamy [143], VCM est formalisé et validé. VCM est fondé sur trois types de
primitives (cf figure 4.6) : les pictogrammes, les couleurs et les formes géométriques. La formalisation se fait
à l’aide de trois ontologies : une ontologie des icônes qui décrit les icônes et leurs composants, une ontologie
du domaine avec les concepts représentés par les icônes, et une ontologie de correspondance (la troisième)
qui fait le lien entre les deux précédentes. Cette dernière ontologie ne contient aucune nouvelle entité, mais
uniquement des contraintes portant sur la relation "icône représente concept / concept est-représenté-par
icône".
88

--- page 109 ---
Figure 4.6 – Structure générale de l’ontologie iconique de VCM
4.7 Synthèse
Dans ce chapitre, nous avons présenté les icônes et les langages iconiques à différents stades de for￾malisation. Parmi ces langages, celui de Lamy connait un niveau de formalisation suffisant et est validé
dans le domaine de la MM. Nous avons vu que les icônes ont une dimension "universelle". Elles rendent
possible la communication au-delà des barrières linguistiques et de l’analphabétisme. Cette dimension
universelle serait très utile dans le contexte de la MT, car nous avons montré au chapitre 2 les difficultés
rencontrées dans cette MT : l’insuffisance de formation des PMT, la perte des connaissances à la mort
d’un PMT, l’absence de cadre d’échange sur les connaissances et expériences, tout cela dans un contexte
d’analphabétisme important, de multilinguisme (1127 langues locales) et de transmission orale.
En conséquence, nous nous donnons pour objectif de construire un langage iconique dans le domaine
de la MT. Puisque notre objectif est l’universalité, nous utiliserons au maximum des signes iconiques pour
la définition de notre langage iconique. Notre centre d’intérêt étant principalement le traitement d’un
patient, nous avons jugé utile de démarrer l’amorçage de ce langage iconique par les plantes, ressources les
plus significatives utilisées en MT pour l’offre de soins de santé primaires. Le grand nombre de concepts, et
notamment d’espèces de plante, utilisés en MT justifie que nous nous orientons vers un langage iconique
et non vers une simple collection d’icônes indépendantes.
La complexité de l’image et de la construction du langage iconique d’une part, et la nature même du
domaine de santé humaine (via la MT), une question délicatement sensible d’autre part, imposent une
construction progressive, incrémentale, rigoureuse et consensuelle. De plus, afin de formaliser le
langage iconique à concevoir, nous l’adosserons sur une ontologie formelle de la MT. Ce travail aboutira
donc à une approche d’ontologie visuelle.
89

--- page 110 ---
Chapitre 5
OntoMEDTRAD : vers une ontologie de la
médecine traditionnelle africaine
Sommaire
5.1 Présentation et architecture globale du système envisagé : sysMEDTRAD . . 91
5.2 Notre méthodologie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
5.3 Étapes de construction de notre ontologie . . . . . . . . . . . . . . . . . . . . . 103
5.4 Spécifications des besoins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
5.5 Conceptualisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
5.6 Concepts présents dans des ontologies ou ressources déjà existantes . . . . . . 119
5.7 Formalisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
5.8 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
90

--- page 111 ---
Nous cherchons à construire un cadre idéal pour les praticiens de la MT (PMT), afin de partager,
mutualiser, co-construire et sauvegarder les connaissances, les acquis et expériences de la MT. Nous appel￾lerons ce cadre sysMEDTRAD, pour système de gestion des connaissances de la médecine traditionnelle.
Sa composante principale sera ontoMEDTRAD, une ontologie de la MT. Cette ontologie comprendra une
partie terminologie, ontoCONCEPT-Term, et une partie iconique contenue dans ontoICONE. Le cha￾pitre actuel a pour objet ontoCONCEPT-Term, et la composante iconique fera l’objet principalement du
prochain chapitre.
Cette ontologie constituera l’épine dorsale fournissant la référence des objets et leur sens pour la
communication entre les machines, et également entre ces dernières et les humains (notamment les tradi￾praticiens, PMT). L’adhésion au projet de cet endogroupe de PMT est garantie par leur implication en
amont, au milieu et en aval dans tout le processus. C’est avec tact que cette adhésion a permis également
de faciliter les entretiens en profondeur et de façon étendue malgré la réticence et le caractère réservé très
manifeste dont certains PMT ont du mal à se défaire. A l’instar des bases de données, une fois l’onto￾logie en phase d’utilisation et répondant aux fonctionnalités applicatives initiales pour lesquelles elle est
construite, la possibilité de l’émergence de nouvelles fonctionnalités est grande.
Une ontologie définit les termes et concepts (sens) utilisés pour décrire et représenter un domaine de
connaissance. La compréhension de chaque concept dans une ontologie est d’importance capitale en vue
de le définir rigoureusement et d’en investir la sémantique idoine. Il s’agit par cette nouvelle technique
mettant en avant la sémantique des objets modélisés, de permettre aux machines d’aller au-delà des formes
classiques de comparaison de ces objets dans leur manipulation et recherche, pour prendre désormais
en compte leur sens. Cependant, l’ontologie vue comme une taxonomie ou une terminologie à l’image
d’un dictionnaire intelligible par l’ordinateur, même vraie, peut entrainer des bribes d’incompréhension.
Toute la sémantique du réel ne peut pas être vidée ni en machine ni humainement, elle nécessiterait une
description considérable voire infinie. L’enrichissement sémantique se veut alors continuellement graduel.
Cette étanchéité de la sémantique se fortifie et se complexifie avec des conventions sociales, historiques et
culturelles pesantes. En outre, le niveau sémantique atteignable dite formelle actuellement permet déjà de
répondre à de nombreuses attentes.
Enfin, la MT présente des caractéristiques particulières : il s’agit d’un savoir fortement tacite et gardé
secret par les PMT. Très peu de travaux ont porté sur la modélisation de la MT, en dehors d’ontologies
restées embryonnaires. En comparaison avec la MM (chapitre 2), nous avons deux formes de médecine qui
diffèrent beaucoup dans les concepts qu’elles manipulent. Pour toutes ces raisons, la réutilisation automa￾tique des ontologies et RTO existantes de la MT ou de la MM ne semble pas être indiquée. En revanche,
leurs politiques, leurs stratégies, leurs méthodologies et méthodes de construction peuvent nous être utiles.
Dans la suite du chapitre, nous indiquerons les éventuels concepts réutilisés dans ontoMEDTRAD et les
RTO dont ils sont issus.
5.1 Présentation et architecture globale du système envisagé : sysMED￾TRAD
Les acteurs et les composants modulaires de systMEDTRAD sont mis en évidence. Leurs corrélations
et leurs fonctionnalités s’explicitent aisément en conséquence.
91

--- page 112 ---
5.1.1 Cartographie globale des acteurs et des utilisateurs
Les acteurs principaux sont les PMT et les patients. Les PMT ont un rôle de première ligne. L’objectif
des cas d’utilisation relatifs aux PMT est essentiel. L’acteur patient jouent un rôle secondaire. Selon le
statut du patient (personne âgée, mineur, femme en état de grossesse), ou son état lié à la gravité de la
maladie, le patient peut être accompagné par une personne (accompagnant humain) : le garant. Cet acteur
suppléant est optionnel. Ce dernier peut apporter des réponses en compléments des indices (symptômes,
signes), de la maladie, des soins reçus qui sont propres au patient. Nous nous concentrons véritablement
aux cas d’utilisations de ces principaux acteurs. Bien avant, le tableau 5.1 montre la cartographie des
acteurs et utilisateurs.
Les PMT sont les porteurs des connaissances de la MT dont nous cherchons à construire l’ontologie
ontoMEDTRAD. Les résultats qui découlent des travaux liés aux experts du domaine de la communauté
des PMT devront constituer une base à partir de laquelle doivent émerger plusieurs applications à même
de faire également face aux attentes des acteurs secondaires.
En conséquence, nous nous focalisons sur les PMT et le patient, et principalement sur les PMT, acteurs
avec lesquels nous avons eu plusieurs rencontres physiques et déterminantes.
5.1.2 Quatre composants essentiels de SysMEDTRAD
L’architecturale envisagée pour sysMEDTRAD [19] est présentée via la figure 5.1. C’est un système à
quatre composants :
– L’infrastructure conceptuelle : Elle résulte de la première abstraction (abstraction 1 dans la figure
5.1.). Elle englobe les concepts sur les sources de connaissances partant donc du réel vivant et naturel
relatif à la MT.
– ontoMEDTRAD : Il résulte de la deuxième abstraction (abstraction 2 dans la figure 5.1. ). Il ren￾ferme les ontologies ontoCONCEPT-Term (terminologique) et ontoICONE (mi-terminologique et
mi-iconique), toutes de ontoMEDTRAD. Le DNI, dépôt numérique des iconèmes et des icônes, est
la partie iconique de ontoICONE.
– Le Wiki sémantique : Le déploiement de ontoMEDTRAD dans un wiki sémantique est celui de
ontoCONCEPT-Term suivi de celui de ontoICONE en tenant compte des concepts en partage. Ce
wiki obtenu est extensible à l’intégration d’autres communautés socio-professionnelles à l’image de
SIOC 1
.
– La cartographie des acteurs : Les acteurs principaux (dont les PMT comme utilisateurs avancés,
experts du domaine de la MT), les acteurs secondaires (ceux de type 1 et ceux de type 2). Ils sont
tous de potentiels utilisateurs.
Un aperçu fonctionnel du fond organisationnel continu de la mémoire de la MT supporté par ontoMED￾TRAD, est succinctement illustré via la figure 5.2 au sens de Dieng [80]. Les connaissances de l’expert y
sont décrites comme étant spécifiques au domaine de la MT, idiosyncratiques, organisées en schémas fonc￾tionnels, flexibles et en partie tacites. On a des travaux continus d’élicitation et d’explicitation (de tacite,
1. SIOC : Semantically Interlinked Online Communities
92

--- page 113 ---
Catégories Acteurs Description de la fonction dans sysMEDTRAD
Acteurs principaux
primaires
PMT Dépositaires des connaissances de le MT.
Premiers bénéficiaires du système pour
l’exercice de l’art médical traditionnel ([19]
amélioré en 5.1)
Patient Le patient est interrogé et ausculté par le
PMT, pour déterminer la maladie. Le patient
est bénéficiaire via l’amélioration de l’offre de
soins de santé de la MT.
Garant ou Entourage Patient Selon le degré ou la gravité de la maladie du
patient, ou encore de l’état du patient
(personne âgée, enfant, femme en grossesse en
état critique), il est accompagné par une
personne adulte, responsable.
Expert ontologiste (ingénierie
des connaissances et des
ontologies formelles)
Maintenance de ontoMEDTRAD
Acteurs secondaires
type 1 (Expert en
informatique et TIC)
Expert en web sémantique et
wiki triplestore
Déploiement de ontoMEDTRAD dans un wiki
sémantique
Infographistes expert, designer Amélioration des icônes
Botaniste Connaissances de la botanique (plantes), bien
qu’elle n’en constitue pas la source principale
Acteurs secondaires
type 1 (Experts mais
pas en informatique et
TIC)
Faunisticien Connaissances de la faune physique des
animaux
Médecins de la MM Pour la validation (en plus de celle des PMT)
Enseignants (TIC, Biosciences,
...)
Utilisateurs finaux
Acteurs secondaires
type 2 (simples
utilisateurs)
Apprenants (Étudiants, ...) Utilisateurs finaux
Grand public (usages
populaires, ...)
Utilisateurs finaux
TABLEAU 5.1 – Cartographie des acteurs et utilisateurs
93

--- page 114 ---
Figure 5.1 – Vue synoptique et architecturale de sysMEDTRAD
94

--- page 115 ---
Figure 5.2 – Fond organisationnel des connaissances et des expériences continu de la MT pour les PMT
implicite à explicite), de voting [191], de pré-conceptualisation, de conceptualisation, de formalisation, de
déploiement, d’intégration, d’opérationalisation et d’arrêtés décisionnels.
5.2 Notre méthodologie
Nous avons fait le choix d’une démarche méthodologique inspirée à la fois des trois points suivants :
1. des méthodologies de construction d’ontologies en général et notamment de Diligent, NeOn et On￾toForInfoScience (section 3.3.1 du chapitre 3) ;
2. de notre expérience suite à la lecture des travaux sur les ontologies existantes. Cela nous a permis
de déceler la manière dont elles sont construites quand bien même nous ne les réutilisons que peu
voire pas du tout ;
3. de la mise en œuvre de plusieurs exercices pratiques de construction d’ontologies issus d’auteurs
différents [89], [95], [104], [119], [168], [202], [205], [212], [222], [249].
Les grandes étapes de notre méthodologie sont : la spécification de besoins, la conceptualisation, la for￾malisation, l’implantation/implémentation, la maintenance.
L’étape de conceptualisation d’un point de vue hautement générique comprend la spécification des
besoins. Ainsi, on a les sous-étapes afférentes suivantes :
– l’expression de besoins : cibler et circonscrire le domaine du discours, spécifier les besoins ;
– les questions de compétences (questions pilotes) : définir le but de l’ontologie ;
95

--- page 116 ---
– les procédés de recherche et d’acquisition de données, des informations et des connaissances au￾près des experts. On peut citer entre autres les entretiens et interviews, la revue documentation
et l’exploitation des résultats de travaux de référence (publications et thèses), utilisation ontologies
existantes, séminaires de sensibilisation et ateliers de formation et des techniques d’élicitation ;
– l’énumération des termes et leur assignation aux concepts ou vice versa. Cela va du glossaire des
termes, du diagramme des concepts et des relations au dictionnaire plus détaillé des concepts.
De façon concrète, nous adopterons un processus itératif (avec des aller-retour) pour consolider la
définition de chacun des termes recensés et qui émergent du domaine de discours. Cette définition consiste
à assigner à chaque terme une fonction ou rôle dans l’ontologie future. Ceci motive le centre d’intérêt du
concept portant le terme. A cela, il faut ajouter qu’il s’agit précisément d’assigner à un terme une seule
des quatre (4) catégories considérées dans une ontologie formelle : classe (ou concept), relation, propriété,
individu. Notons cet ensemble TO. On a donc : TO = { classe, relation, propriété, individu }.
De manière progressive et itérative, les aller-retour consistent à combiner ou croiser les avis recueillis
auprès des acteurs (notamment les experts PMT, lettrés ou illettrés) qui sont les dépositaires des connais￾sances de la MT. A ce titre, des interview réalisés ont été repris avec le même PMT sur le même sujet à
des périodes d’intervalle de 4 à 6 mois, puis croisés.
D’autres sources ont été utilisées, nous les donnons dans l’ordre d’utilisation. Nous avons les sources
écrites en médecine et biosciences (publications, thèses, documentation des programmes nationaux de
promotion de la MT, de la documentation des ONG, ouvrages de librairies, ...). Nous avons aussi les
sources web. Nous avons spécifiquement des sources en botanique (physicalité et morphologie des plantes).
L’analyse croisée et le recoupement de plusieurs sources est une façon de s’assurer du bon choix fait d’une
assignation de terme à un concept. Cela concourt à une vérification et aide à déterminer le terme de
préférence ou le plus consacré dans le domaine de discours, puis ceux de second rang, pour un concept
donné. Par exemple en MT, le terme "Plante" (Plant en anglais) est préféré à celui de "Végétal" bien
qu’on s’adresse généralement aux ressources végétales.
Une fois que l’assignation des classes aux termes ou des termes aux classes est faite (en rapport à une
interprétation minimale), nous passons à la pré-représentation à travers un diagramme de classes UML.
Tout ceci permet d’avoir une première vue synoptique des classes et une idée plus nette de la façon dont
se fera leur projection dans l’ontologie à partir de ce diagramme de classes. Il convient de noter que ce
diagramme n’est pas complet, en particulier toutes les propriétés n’y figurent pas. Le plus important
sur ce diagramme, ce sont les classes et leurs noms, puis les relations de classes (subsomption en terme
d’héritage, et association entre classes d’individus).
Après la phase de conceptualisation, vient l’étape de formalisation, qui est réalisée au moyen d’un
éditeur d’ontologies (comme Protégé). Plusieurs sous-étapes sont à noter lors de la formalisation, sans
ordre précis :
– La hiérarchisation des classes sous forme arborescente (structure taxinomique) : Une fois que les assi￾gnations de termes sont faites, ceux qui sont devenus des classes vont subir un rangement hiérarchisé
par la technique combinatoire des approches de top-down et du bottom-up ;
– La hiérarchisation des relations sous forme arborescente : Comme pour la hiérarchie de subsomption
de classes (structure taxinomique), nous faisons de même pour les relations possibles entre classes ;
– La définition des classes définies (abouties) et des classes équivalentes : Nous faisons la distinction
96

--- page 117 ---
Figure 5.3 – Cycle de vie de construction d’ontologies (prototype général)
entre classe primitives, classes définies et classes équivalentes ;
– L’établissement des relations binaires (entre classes) : Il s’agit de vérifier l’effectivité d’accomplisse￾ment de la relation. Ensuite s’il y a lieu, de leur assigner à leur tour, les propriétés structurelles à
deux niveaux notamment (1) et (2) suivants :
– (1) : caractéristiques : réflexive, irreflexive, inverse, symétrique, asymétrique, transitive, fonction￾nelle, inverse fonctionnelle ;
– (2) : classe source et classe image respectivement qui sont domaine et range (domaine et range
sont des propriétés de propriétés ou encore des propriétés de relations) ;
– L’établissement des propriétés de classe : Il faut vérifier la véracité et l’effectivité de la propriété de
classe en assignant à cette propriété le domaine qui est la classe elle-même et le range (type natif
qui peut être un littéral) ;
– La liste des axiomes.
Est un axiome, tout énoncé vrai manifestant un intérêt pour ce qui est décrit dans le domaine de
discours. La liste des axiomes ne peut jamais être exhaustive. Certains sont évidents et ne nécessitent
pas d’être transcrits. Quand il y a lieu de les formaliser, il faut le faire de sorte à soutenir par exemple
la définition d’une classe (classe définie par opposition à une classe atomique ou primitive). Les classes
primitives sont dites évidentes ou atomiques. Elles s’appuient en réalité sur des axiomes dont la notation, la
transcription ou la spécification n’est pas nécessaire (trivial et vrai). Les axiomes à marquer s’apparentent
à des règles de gestion relatives aux entités de l’ontologie. Les axiomes peuvent avoir un but descriptif, et
alors restreindre ou contraindre une classe, une relation, une propriété, un individu, ...
Avec axiome comme une des catégories possibles dans TO, TO déjà défini, devient alors : TO = {
classe, relation, propriété, individu, axiome }.
L’étape de formalisation consiste à transcrire ce qui précède dans un langage plus formel (tel que OWL)
que celui utilisé lors de la conceptualisation (tel que UML).
Notre méthodologie se fonde sur les prototypes de cycle de vie (cf figures 5.3 et 5.4) inspirés de
Methontology et surtout de ses points communs avec NeOn, Diligent et OntoforInfoScience.
Les activités de développement constituent le noyau de la construction de l’ontologie avec la possibilité
de retour et de modification. C’est à dire, à chaque étape de développement, on a la possibilité de revenir sur
97

--- page 118 ---
Figure 5.4 – Cycle de vie de construction d’ontologies (inspiré de Methontology) en phase avec Neon,
Diligent et OntoforInfoScience
les décisions prises ou les résultats issus des activités précédentes. Ceci concourt à maintenir la cohérence et
le consensus. Les activités supports (acquisition des connaissances de multiples sources dont principalement
des experts du domaine, intégration, documentation, évaluation et configuration du management) ont lieu
tout le long de l’exécution des activités de développement.
Récapitulatif des étapes de construction pragmatique d’une ontologie
La figure 5.5 présente un récapitulatif des étapes de construction pragmatique d’une ontologie, qui sont
compatibles avec les figures 5.3 et 5.4. Au regard de cette même figure, excepté l’étape de circonscription
(flexible) du domaine du discours pour l’initialisation du projet de construction d’ontologie, le sens des
symboles à trois têtes de flèches (dont deux plus petites en arrière, et une plus grande en avant), exprime
l’insistance sur les aller-retour, les emboitements cohérents et logiques. L’avancement est important mais
avec cette possibilité de retour en vue de mieux aiguiller ou raffiner les solutions prises à chaque étape
en cours pour entamer la prochaine. Après l’activité de peuplement de la ligne 3 (de la figure 5.5), nous
avons l’exploitation (par la communauté des potentiels acteurs utilisateurs), la maintenance (l’évolution).
Cette approche de développement concourt à assurer un consensus et une consistance certains à notre
modèle. Des sauts sont possibles mais sur la base d’une évidence notoire des éléments de l’étape sautée.
Dans le cadre d’un projet de développement complexe d’ontologie, il y a lieu de respecter méticuleusement
les étapes et même d’y revenir. Dans ce contexte, il n’est pas toujours aisé ou même possible d’enregistrer
l’exhaustivité des actes posés et des activités menées. A ce titre, on est tenu par une traçabilité en les
décrivant succinctement et pour l’essentiel.
98

--- page 119 ---
Figure 5.5 – Schéma récapitulatif des étapes de construction pragmatique d’une ontologie
Pré-conceptualisation
Nous appliquons notre méthodologie de construction à la MT, notre domaine de discours et de connais￾sances, dans le tableau 5.2.
Vu le domaine fortement tacite de la MT, dans le cadre de l’élicitation et de la conceptualisation, nous
avons mis un accent particulier sur la contextualisation pour faciliter une compréhension en profondeur.
Après quoi, nous décontextualisons pour généraliser. Ceci consolide la stabilité de notre modèle conceptuel.
L’information contextuelle est compartimentée en sous contextes ou facteurs. Ici, les termes Class et
SubClass sont à titre pré-conceptualisation et ne correspondent pas nécessairement à ceux de l’étape de
formalisation ultérieure en OWL (cf tableaux 5.3 et 5.4).
Après élicitation, ce principe de contextualisation et de décontextualisation est la base à partir de
laquelle nous obtenons notre modèle conceptuel (UML) dans les sections suivantes. Celle-ci a également
fait l’objet d’une analyse croisée avec les sources multiples mentionnées à la ligne 3 du tableau 5.2.
Avec ce choix inspiré des descriptions faites des méthodologies de construction d’ontologies en général
et spécifiquement de Diligent, NeOn et OntoForInfoScience, des travaux de construction pratique isolément
menés en marge de ceux-ci et suite à notre propre expérience, nous sommes en mesure de construire notre
ontologie OntoMEDTRAD de sysMEDTRAD.
99

--- page 120 ---
Domaine de discours Secteur : Médecine et santé humaine ; Domaine : MT Afrique de l’ouest
Principaux experts de connaissances : PMT
Typologie des acteurs PMT, experts de domaines de la MT, Traducteurs (guide-interprètes).
Patient.
Experts de domaines annexes : botaniste (physiologie et morphologie des plantes)
pour la phase d’amorçage du langage iconique, puis après, faunisticien (physiologie
et morphologie des animaux).
Expert en informatique / TIC et dessin : Ingénierie ontologique et de connaissances,
Infographiste, ingénieur expert en Wiki sémantique.
Enseignant, Étudiant et population.
Sources d’information Ressources Experts de domaines et traducteur
Ouvrages de médecine moderne et de biosciences, publications, thèses traitant de la
MT
Documentation des programmes nationaux de promotion de la MT, des ONG, ...
Sources web, Observation,
Visite de terrain (jardin botanique), sites ou centres de MT (des PMT), étalage de
ressources médicinales au marché, étalage à domicile,
ouvrage de la description flore et faune
Elicitation Réunions de sensibilisation pour adhésion, ateliers de formation et rencontres
d’entretien, traduction par des interprètes entre le français et les langues locales, des
aller-retour chez les experts à chaque niveau de notre construction.
Cycle de vie Spécification, contrôle assurance qualité, management, Elicitation, conceptualisation,
intégration, formalisation, implémentation, maintenance (évaluation peut être
répartie à chaque fin d’étape), évaluation, documentation
Pratique de l’art médical par le PMT Patient - Indice (symptôme et signe) - maladie - Ressources médicinales (Plantes,
Animal, Minéral) - Recettes Remèdes.
Type de collaboration Réparti et distribué avec les outils (téléphones, internet, messagerie, ...)
identification des concepts (classes) UML (Diagramme des classes)
Ontologies existantes fondationnelles
et noyau , et celles (non de référence
en général et au stade d’embryon) de
la MT de quelques auteurs isolés
Ontologies fondationnelles et noyau : OBO, PO, PSO.
Spécificités de la MT sur l’utilisation directe des ressources naturelles (plantes,
animaux, minéraux) pour les soins de santé primaires. Prise en charge du patient se
démarquant de celle de la MM. Difficulté d’utiliser des ontologies de domaine
émanant de la MM (cf Caractéristiques propres à la MT du chapitre 2, Description
détaillée des cas d’utilisations du chapitre 5). ontologies de la MT de différentes
régions du monde au stade d’embryon (Travaux relevant de la MT du chapitre 3).
détermination et définition des
classes
OWL
arrangement taxinomique OWL
Relations Propriétés associatives entre entités
Propriétés Propriétés littérales propres à l’individu lui-même
Taxinomie (Systématisation) Nom scientifique des ressources végétales et animales détectées comme sources
médicamenteuses de la MT
Peuplement de l’ontologie inscription des individus propres à chaque classe
Rencontre des acteurs experts à
certaines étapes pilotes de la
construction
Approche épistémologique en vue d’aiguiller mieux et consensuellement la
construction, partage des résultats
Banc d’essai et évaluation, détection
des erreurs et les corriger
Sélection des attributs-valeurs par l’outil logiciel d’apprentissage et de classification
WEKA (cf section "6.3.4 Sélection des critères" du chapitre 6)
Inventaire et émergence de formes de
plante, des parties de plantes au vu
de la diversité des descriptions
botaniques (physicalité/morphologie),
iconèmes
WEKA (classification supervisée), InkScape (cf section "6.3.5 Dessin des iconèmes et
choix des couleurs" du chapitre 6)
TABLEAU 5.2 – Point d’ancrage pour de la construction de ontoMEDTRAD
100

--- page 121 ---
Class SubClass Description (commentaire ou remarque)
Information
contextuelle
Type de PMT (genre, âge et
habitat)
Ils sont différemment abordés selon le genre, l’âge et le milieu
(urbain-capitale, quartier huppé ou populaire, urbain-simple, rural,
campagne
Profile ou type professionnel Herboriste (les plus nombreux) ; accoucheuse (matrone)
Magico-religieux combinant (animisme, coran, bible, plante, argile
blanche, tissus blanc, noir et rouge, ...)
Expérience du PMT De tous les âges après 16 ans.
Pratiques de l’art de guérir Observation d’une consultation d’un patient (enfant, adulte,
personne de troisième âge, femme, homme), d’une préparation des
médicaments (décoction avec de grosses marmites d’aluminium et
faire des décoctions principalement) ;
Concept de faire un canari : mise des produits ingrédients de
ressources médicinales dans un canari facilement transportable
(taille du canari variant entre 10 à 30 cm)
Renommée du PMT Degré de référence en matière d’offre de soins de santé primaires,
diminution de risques iatrogènes
PMT lettré ou illettré, niveau
scolaire
Selon le niveau scolaire, il y a nécessité de traduction ou pas
(traducteur : langue officielle ↔ langue locale (flèche à deux têtes
montrant le caractère bidirectionnel)
Promptitude et habilité à
prendre en charge le patient
Localisation, niveau d’expertise du PMT, hospitalisation rarissime
PMT exerçant seul ou avec
une équipe
La plupart des PMT exerce seul, des groupements sont rares ou en
famille
Appréciation et niveau
d’acceptation de collaboration
avec d’autres PMT, avec la
MM, avec la recherche
scientifique, avec autres
partenaires de santé
Il arrive que certains PMT de grande renommée soient non
favorables à l’ouverture et donc réticents à la collaboration.
La sensibilisation pour l’ouverture doit être continue.
Environnement d’exposition
des ressources médicinales
(RM) ou des produits MTA
provenant des RM
Air libre, étalage (empaquetage ou attachement par cordon),
magasin de vente, centre médical traditionnel, au marché rural, au
marché urbain ;
MTA (médicaments traditionnels améliorés) : moins de
transformation chimique subie ou à l’état de recette physique avec
les ingrédients empaquetés.
Exercice professionnel
ponctuel (secondaire) ou
continu
Allier l’exercice de l’art médical avec des activités de commerce hors
de la MT, de travaux champêtres. Il existe des PMT qui en font leur
seul métier
Type de traitement Prévenir et/ou traiter la maladie (préventif et curatif)
Détection des symptômes et
des signes de maladie et
acceptation de test cliniques
de la MM
Selon le PMT, les tests cliniques sont effectués en entrée seulement,
seulement en sortie de ou après traitement, en entrée et en sortie,
sont carrément refusés, ou peu importe
Attitude du PMT une fois la
maladie déterminée
Choix possibles du PMT :
-Traiter effectivement la maladie car sûr de son expertise ;
-Tenter le traitement ;
-Avouer son incapacité de traiter la maladie ;
-Faire un référencement médical à un autre PMT ou à la MM.
TABLEAU 5.3 – Principe de contextualisation et de décontextualisation pour l’émergence des concepts/classes
future
101

--- page 122 ---
Class SubClass Description (commentaire ou remarque)
Information
contextuelle
période/temps de collecte de
la RM et administration
directe ou fabrication du
remède pour traiter la
maladie, par administration
Disposition temporelle et attitude comportementale
période de collecte (aube, nuit, midi, jour, points cardinaux, ...) et
état d’esprit (éviter le mensonge).
Cela se rapporte au PMT, au patient et souvent à son entourage
immédiat (amis et famille)
Il existe moult collectes sans disposition particulière de temps et
d’attitude.
En général, les ressources végétales (Plantes) sont collectées et
utilisées en MT à partir de leur état de maturité. Ce qui n’est pas
appliqué pour les animaux ou leurs parties : poule, poussin, coq ,
agneau, bélier, mouton, ...
Aucun critère véritable n’existe pour les minéraux : sable, argile,
eau, ...
NB : Les couleurs sont en nombre restreint en langues locales et en
MT : noir, blanc, rouge,/orange, ...
Etat de maturité de la RM
surtout quand elle est vivante
(Plantes, animaux)
L’état où la plante dispose des principes actifs nécessaires à même de
pouvoir soigner.
Il en est presque similaire pour les ressources animales.
RM populaire ou rare Passer des commandes, plantes en voie de disparition (réchauffement
climatique), RM en abus de consommation. Chercher à avoir un
jardin personnel de plantes rares.
Circuit de collecte et
d’approvisionnement en RM
Circuit généralement court un (1) à deux (2) intermédiaires. En
pleine brousse, jardins botaniques, ventes des ressources brutes au
marché (rural ou urbain).
Temps de réception
d’interview du PMT, visites
de terrain (jardin botanique
ou centre de floristique) avec
reprise
-Prendre un rendez vous
-tenir compte de la durée de la réception
-choisir la période où ils sont plus réceptifs
-Pour le visiteur (que nous sommes) : rencontre gratuite ou imposé à
payer un franc symbolique ou une somme donnée, ou simplement un
pourboire. Tout ceci peut conditionner la prochaine visite.
TABLEAU 5.4 – Principe de contextualisation et de décontextualisation pour l’émergence des concepts/classes
future (suite et fin du Tableau 5.3)
102

--- page 123 ---
5.3 Étapes de construction de notre ontologie
Cette section émerge de la précédente et même pourrait s’y inclure. Cependant, l’intérêt de sa mise en
évidente ici, est de la valoriser davantage.
Nous résumons nos étapes issues de Diligent, de NeOn et de ontoForInfoSciences (Section 3.3.1 du
chapitre 3), au nombre de neuf (9). Ces étapes ou phases sont plus ou moins communes à ces trois (3)
méthodes et compatibles en parties avec la norme I3E 1074-1995 (Section 3.3.1 du chapitre 3). Elles
constituent le socle de notre démarche méthodologique, vu la nature du domaine de notre projet de
recherche.
– Étape 1 : Spécification des besoins
Pour la construction de l’ontologie, sont largement suffisantes les raisons déjà évoquées dans le chapitre
1, introductif, auxquelles se rajoute celle qui suit : il n’existe pas d’ontologie de référence en MT africaine.
Il en existe à l’état embryonnaire (cf chapitre 3) tant au niveau terminologique qu’au niveau iconique
(icOnto de Kuicheu).
– Étape 2 : Questions de compétences
Ces questions se rapportent à la spécification des besoins. L’ontologie ontoMEDTRAD a deux niveaux
de réponse : le premier terminologique et le second iconique. A chaque niveau plusieurs applications
sémantiques peuvent être réalisées : constitution d’un fond organisationnel continu des connaissances, des
pratiques et expériences de la MT. Ces ontologies à travers sysMEDTRAD vont constituer le support
principal d’un cadre d’échange sous forme de plateforme web social et sémantique entre PMT et leur
permettre d’exercer leur art de guérisseur. Ces derniers seront aidés par l’usage du langage iconique une
fois celui-ci à terme.
– Étape 3 : Acquisition de connaissances
Cette phase implique l’acquisition de connaissances. Elle comprend la sélection des matériaux à étudier
(sur le domaine) et la sélection des méthodes pour extraire les connaissances. Ces activités mélangent
souvent différentes méthodes, comme : l’analyse textuelle des livres et des documents, et l’extraction
manuelle et/ou automatique des termes (concept et propriétés). Du point de vue terminologique, nous
avons utilisé les procédés visant les échanges et interviews avec le PMT par des rencontres physiques, des
réunions, une documentation riche en MT relavant des programmes nationaux, ONG (Prometra), travaux
scientifiques en biosciences, le web et des ouvrages. Du point de vue iconique, nous avons utilisé des
techniques de catégorisation afin de mettre en relief les critères-attributs et valeurs permettant d’amorcer
l’ontologie visuelle (langage iconique) par le concept de plante (en justification par les cas d’utilisation).
Chaque concept à iconiser peut constituer un travail considérable. Ainsi par exemple la représentation
iconique visuelle de la plante dépasse le cadre de la MT pour aborder de manière dense la physicalité des
plantes traitée par la morphologie en botanique. Pour l’émergence et la rétention de critères attributs et
valeurs, nous avons fait usage d’un outil automatique d’apprentissage et de classification Weka (cf section
6.3.4 "sélection des critères" du chapitre 6). Ce sont ces attributs qui seront conceptualisés et puis après
formalisés en classes dans ontoMEDTRAD.
– Étape 4 : Conceptualisation
103

--- page 124 ---
Le point de vue d’intérêt majeur de notre travail consistant à traiter un patient, nous a amenés à la
définition de trois cas d’utilisation dominants notamment UC1 : diagnostiquer la maladie sur le patient,
UC2 : déterminer le remède et UC3 : préparer le remède et l’administrer. Ainsi se signale le point de
départ de notre modélisation conceptuelle. La description de ces cas d’utilisation nous conduits à asseoir
les concepts et les relations fondamentaux à partir desquels nous allons étendre (élargir) le champ des
concepts et le spectre relationnel. A ce titre, nous avons fait usage de tableau, de dictionnaire et d’un
modèle conceptuel graphique (diagramme de classes sous UML) décrits succinctement comme suit :
i) un tableau de concepts et de propriétés, contenant des concepts, des définitions, des synonymes, des
valeurs et des propriétés autorisées ;
ii) un dictionnaire de verbes contenant des verbes identifiés candidats à être des relations, ainsi que
leurs définitions textuelles ;
iii) un modèle conceptuel graphique qui représente des relations conceptuelles entre des concepts uti￾lisant des graphiques et des structures similaire au diagramme de classes sous UML.
– Étape 5 : Intégration et importation de concepts depuis des ontologies existantes
La réutilisation de concepts des ontologies de fondement (OBO 2
, BFO), ou core (PO), concerne peu de
concepts ici, vu le mode opératoire de la MT très différent de celui de la MM. C’est pourquoi, nous avons
plus cherché, après la définition des termes de nos concepts, à les confronter aux ontologies existantes. Le
concept de plante dans PO [193] [203] est décrit chimiquement en détail, mais beaucoup plus sommairement
d’un point de vue morphologique. Les principes actifs des plantes médicinales traditionnelles ne sont pas
abordées en MT du point de vue du PMT.
Ces dernières années, les gouvernements cherchent à aider financièrement les PMT à tester cliniquement
les principes actifs des plantes utilisées. Par contre les travaux en biosciences sur l’éthnobotanique sont
déjà bien riches pour la sous région (ex ORSTOM devenu Institut de recherche pour le développement
(IRD), travaux de recherche universitaires et avancés). Il est prévu l’intégration des curricula de formation
en MT africaine dans des écoles et universités comme cela se fait en Chine. Le regain d’intérêt de la MT
amène à permettre aussi l’intégration progressive de centres de MT dans les structures hospitalières de
soins de santé de la MM.
Nous n’abordons pas les principes actifs dans ontoMEDTRAD. Il y a des systèmes universels et in￾ternationaux de classification que nous avons analysés et intégrés en partie. Il s’agit notamment pour les
concepts de maladie et de symptôme de la CIM-10 (ICD-10) 3
et de SNOMED-CT (Systematized Nomen￾clature of Medicine - Clinical Terms) qui est une terminologie internationale de MM. La classification du
règne du vivant nous intéresse à travers les noms scientifiques des plantes (faisant partie des végétaux) et
ceux des animaux utilisés tous en MT. Elle est traitée par le NCBI (National Center for Biotechnology
Information) 4 et 5 organismal classification adossé à OBO. Il est possible d’accéder à moult ontologies de
référence par Ontobee 6 et 7, comme le montre [241]. Ontobee est un puissant outil serveur, point focal de
liaison de termes de concepts d’ontologies formelles existantes et de référence).
Le terme herbe, dans une acception large, est utilisé pour désigner toute plante annuelle ou vivace,
non ligneuse.
2. http ://www.obofoundry.org/ consulté en 2015
3. http ://apps.who.int/classifications/icd10/browse/2015/en consulté en 2015
4. http ://www.obofoundry.org/ontology/ncbitaxon.html consulté en 2017
5. https ://www.ncbi.nlm.nih.gov/pmc/articles/PMC3037419/ consulté en 2015
6. http ://www.ontobee.org/ consulté en 2017
7. http ://www.ontobee.org/sparql consulté en 2017
104

--- page 125 ---
– Étape 6 : Formalisation
La représentation formelle de l’ontologie est créée en utilisant un langage logique (LDs comme OWL).
En partant de la conception (phase 3), les développeurs produisent des descriptions formelles. La connais￾sance du domaine est ensuite organisée en tenant compte des principes ontologiques et formels. Ce qui
implique de raffiner des structures conceptuelles antérieures afin de respecter les contraintes ontologiques
et logiques. Les activités principales de cette phase sont :
i) Construire une taxonomie, l’ontologie de niveau supérieur sélectionnée ; caractériser les types de
relation is_a et part_of ;
ii) Décrire les relations et propriétés (attributs) des classes. Il en est de même pour des noms synonymes,
définitions et annotations, selon la langue ;
iii) Créer des définitions formelles des classes, qui sont dérivées des définitions textuelles relevant du
discours littéraire ;
iv) Décrire les propriétés et attributs en tant que types de données, cardinalités, quantificateurs exis￾tentiels et universels ;
v) Peupler les classes par les individus, les instances ;
vi) Adjonction de règles (Swrl).
– Étape 7 : Formalisation avancée
Cette étape implique une évaluation de l’ontologie. A la fois la validation ontologique (correspondance
entre l’ontologie et le monde réel) et la vérification ontologique (analyse en fonction de l’exactitude et de la
consistance) y sont effectuées. Les exemples de critères de validation sont : la non-récursivité dans les défi￾nitions, la spécification de différents types de parties de relations, la définition des relations, fonctionnelles,
inverses et la création de cardinalités, symétrique, ...
– Étape 8 : Documentation
Toutes les activités du cycle de vie sont documentées et organisées. La documentation est produite
avec la construction de l’ontologie. Elle englobe le document de spécification (phase 2), les documents de
référence relatifs au domaine (phase 3), les modèles conceptuels (phase 4), les ontologies réutilisées (phases
5 et 6), le contenu ontologique et formel (phase 6) et d’autres notes utiles.
– Étape 9 : Disponibilité de l’ontologie et emploi
Enfin, dans la phase 9, le développeur rend l’artefact ontologique disponible pour être téléchargé et
visualisé par une communauté d’utilisateurs. Les étapes de cette phase sont les suivantes :
i) exporter le contenu de l’ontologie de l’éditeur vers le référentiel Web ;
ii) présenter l’ontologie sous forme graphique, qui peut faciliter la compréhension de la structure par
les utilisateurs.
Remarque
Ces étapes n’ont pas les mêmes degrés de description et d’importance. Au stade actuel de notre ontologie
(ontoMEDTRAD) et de notre recherche, d’autres validations sont en vue pour le déploiement web effectif
en environnement wiki sémantique (virtuoso choisi). Ce qui suit en tient compte.
105

--- page 126 ---
( A ) ( B )
Figure 5.6 – Vues synoptiques succinctes de la spécification des besoins à l’implémentation de la solution
en machine
5.4 Spécifications des besoins
Un aperçu des spécifications des besoins avec les exigences et les contraintes, du point de vue de leur
rapport avec les représentations retenues comme solution de mise en œuvre informatique, est décrit à
travers les deux sous figures (A) et (B) de la figure 5.6. Il est inspiré de Kerzazi [130]. Ceci corrobore
bien notre démarche méthodologique. Dans la partie A de cette même figure le chiffre 1 encerclé traduit
un processus chronologique et celui de 2 traduit une validation globale.
5.4.1 MT : Besoins tactiques et stratégiques
Notre proposition sysMEDTRAD [19] se veut un système fédérateur et évolutif. Il constitue proprement
un système de partage de connaissances pour la MT. Il intègre les outils TIC (mobile, ordinateur, wiki
sémantique, ontologies formelles, langage iconique, ...). sysMEDTRAD est un système d’échange et de
partage des connaissances, dont l’élément le plus important est ontoMEDTRAD. En somme, il s’agit de
contribuer à l’amélioration des soins de santé primaires et à l’augmentation du potentiel de leur offres en
matière de MT. Spécifiquement, cet objet se décline en trois composantes essentielles.
– Au plan technique : Disposer d’un langage iconique pour les PMT les affranchissant des barrières
linguistiques et de leur état d’incapacité à lire et à écrire (ou d’analphabète) ; disposer d’un outil
TIC pour la MT.
– Au plan fonctionnel : assister et aider les PMT dans leurs tâches quotidiennes et permettre l’échange
et la collaboration entre eux.
– Au niveau de la portée : pérenniser, capitaliser et mutualiser, partager et réutiliser les connaissances
et expériences dans le domaine de la MT.
La majorité des PMT ont accepté de collaborer à nos enquêtes avec l’appui de facilitateurs (sensibili￾sation, PNPMT et traducteurs). Quasiment 90% des PMT ont un prolongement de leur travail à domicile.
Certains d’entre eux disposent de plusieurs autres lieux fixes pour exercer l’art de guérisseur traditionnel
106

--- page 127 ---
tandis que d’autres sont ambulants. Nous relevons que ces activités sont menées également sur les sites
des marchés tant urbains que ruraux. On note une forte présence de ces activités pour les grands jours de
marchés tenus une fois dans la semaine et à des jours fixes dans les villages et pour certaines petites villes.
Décrire les besoins représente un travail considérable. C’est pourquoi nous partons d’un groupe noyau de
trois cas d’utilisation pour lesquels le langage iconique que nous proposons présente un intérêt particulier.
5.4.2 Besoins pragmatiques pour la construction de ontoMEDTRAD : Trois cas
d’utilisation
Nous avons identifié les trois cas d’utilisation suivants :
UC1 : diagnostiquer la maladie.
Nous partons de la détection des symptômes (indiciels) jusqu’à la détermination de la maladie. L’objectif
est donc de déterminer la maladie et son intitulé (e.g : le paludisme).
UC2 : déterminer le remède.
Ici, suite à la détermination de la maladie dont souffre le patient, le PMT doit prescrire un remède
approprié émanant des ressources médicinales traditionnelles. Quand bien même il existe un remède en
terme de MTA, celui-ci peut ne pas être prêt à l’emploi. Il est souvent au stade d’ingrédients donc de
recette avec un mode de préparation. L’UC2 est une prescription où le PMT pense au traitement qu’il
faut.
NB : Ici, disposer de la recette non physique est obligatoire (liste des ingrédients et le mode de pré￾paration). On passe cette étape en disposant également de la recette physique (composants matériels
ingrédients) et ce souvent par la recherche (visite d’étalages, herboristerie, récolte, ...). Ces deux tâches
sous-tendent la prescription du remède.
UC3 : préparer le remède et l’administrer au patient.
Préparer le remède c’est préparer la recette suivant son mode de préparation. La préparation du remède
repose donc sur une seule recette (recette physique) et un seul mode de préparation. Il a une seule forme
galénique. Il a au moins un mode d’administration.
Dans l’UC1, nous constatons qu’il est difficile de séparer les deux approches diagnostiques en MT [84] :
– l’une est d’ordre somatique [178] en rapport avec la maladie physique ou psychosomatique. C’est
à dire une maladie organique dite naturelle, qui n’est pas liée à l’action maléfique d’un tiers. C’est
la maladie dont il faut reconnaître les symptômes (le médecin traditionnel PMT ou le guérisseur ou
encore la MM peut le faire) ;
– l’autre est d’ordre métaphysique qui implique la recherche de causes non naturelles de la maladie.
Cela requiert des capacités qui permettent au thérapeute de communiquer avec des éléments du
monde invisible. Ici, seuls les devins, magico-religieux et devins-guérisseurs sont capables de le faire.
Cela comprend plusieurs protocoles d’administration de soins, de rituels de collecte. Il faut observer
des dispositions de bonnes pensées, d’attitudes et d’interdits.
Ces deux volets de diagnostics dans les consultations vont de pair, de manière concomitante en réalité.
Cependant, dans notre démarche actuelle, le diagnostic d’ordre métaphysique n’est pas abordé. Nous
relevons également que pour le premier cas de maladie symptomatique, il arrive tout de même qu’un
patient souffre d’un mal dont les symptômes ont du mal à être confirmés en signes suite aux tests cliniques
de précision de la MM.
Les PMT utilisant une seule de ces deux démarches existent également, mais ils sont moins nombreux. Ils
sont efficaces mais souvent de renommée moins importante. Les PMT les plus renommés pratiquent les
107

--- page 128 ---
deux démarches.
Pour l’UC2 et l’UC3, le remède constitue l’essence commune de leur raison d’être.
5.4.3 Description détaillée des cas d’utilisations
Suite aux entretiens avec les PMT et la revue documentaire sur la MT, les descriptions qui en résultent,
posent ici les formes canoniques de la consultation du patient par un PMT avec pour préoccupation
centrale, la détermination de la maladie à partir des symptômes et signes, la définition de la recette et sa
préparation, et enfin, le mode d’administration du remède qui en découle.
En l’absence ou l’inexistence de MTA (médicament traditionnel amélioré), le réflexe de tout PMT est
de lister les ingrédients de la recette et de disposer de la ressource qui servira pour préparer cette recette.
Il pense alors tout de suite à la ressource médicinale (RM) qui conviendrait et dont les parties pourraient
constituer les ingrédients de la recette.
Nous prenons en compte ici la collaboration entre MM et MT. Il s’agit de la collaboration stricto
sensu, consistant à permettre au PMT, s’il y a lieu, de disposer de moyens de preuve plus avérée via les
examens ou analyses cliniques effectués par la MM, relatifs à un symptôme ou une maladie du patient.
Soit à l’initiative du PMT, du patient ou de son entourage, ce type d’examen peut être réalisé avant ou
après tout traitement d’un symptôme ou d’une maladie. Il demeure non obligatoire, car il n’a jamais été
imposé par le PMT.
Notons que UC1, UC2 et UC3 reposent sur l’expertise quasi-exclusive du PMT qui donne consignes et
instructions au patient et à son entourage-accompagnant. La responsabilité du PMT peut être partagée
avec la MM, dans le cas d’examens cliniques effectués sur le patient par la MM et utilisés par le PMT.
Dans la majorité des cas de consultation auprès des PMT, la prise en charge du patient se limite à
la détection des symptômes, des signes et de la maladie, à la prescription de remède via des recettes ou
des MTA puis au traitement effectif décidé par le PMT. Les cas d’hospitalisation du patient par la MT
sont rares, et ce, quelle que soit la gravité de la maladie ou de l’état du patient. Les quelques uns qui
détiennent un ou plus d’un centre de soins de santé traditionnel font des hospitalisations mais toujours
rarement. Nous laisserons cette possibilité de côté.
5.4.3.1 Description de l’UC1
Pour l’UC1, il s’agit d’une consultation par le PMT d’un patient ayant un problème de santé. Il faut
alors détecter les symptômes et signes concourant à identifier la maladie dont souffre le patient (cf figure
5.7).
Remarque
Par ailleurs, le type d’examen clinique peut constituer un point déterminant dans les approches concep￾tuelles de collaboration entre MM et MT surtout du point de vue de la maladie et de la prise en charge
du patient. Ceci vient en renfort à l’association de ces deux médecines comme l’entend Sanou [215].
5.4.3.2 Description de l’UC2
Le PMT doit ensuite passer à la phase de prescription du remède pour traiter et soigner le patient. Il
existe des remèdes MTA soit déjà prêts à l’emploi soit au stade d’ingrédients. Quand le MTA est au stade
108

--- page 129 ---
(**) se référer à la figure 2.1 pour le processus de clarification de symptômes objectifs (signes) et symptômes subjectifs.
Figure 5.7 – Description algorithmique de l’UC1.
d’ingrédients, il nécessite une préparation (mode de préparation) afin d’obtenir le remède prêt à l’emploi.
En conséquence, l’UC2 comprend le choix du remède. Cette détermination du remède comprend la
définition (ou la formulation) de la recette appropriée suivie de son mode de préparation. Concrètement,
cela consiste à lister les ressources médicinales (e.g : les plantes médicinales) et les parties de ces ressources
médicinales (e.g : ingrédients ou parties de plantes précisément l’exemple de feuille de neemier "Azadirachta
indica A. Juss"), puis de préciser le mode de préparation (e.g : décoction, ...). Ici, on n’obtient pas vraiment
le remède mais la recette devant permettre de l’obtenir. On parle de prescription du remède comme déjà
titré.
Les conseils, les contres associations (entre ressources médicinales) et contre indications (en rapport
avec l’état du patient) prodigués par le PMT sont supposés implicites (passés sous silence ici) pour simplifier
le cas d’utilisation. En somme, le premier réflexe du PMT suite à la détermination de la maladie est de
penser au remède. Ici penser au remède conduit à trois types de remède :
– un MTA prêt à l’emploi ;
– un MTA nécessitant une préparation (mode de préparation), car étant au stade d’ingrédients ;
– une absence de MTA qui consiste à une recette (ingrédients listés) avec un mode de préparation
permettant d’obtenir le remède.
La dernière de ces trois situations est la plus courante dans les prescriptions des PMT.
Nous avons ici deux grandes étapes pour l’UC2 :
– La première étape (étape 1) est celle concernant la prescription et donc portant sur le choix du
remède sous forme de recette comme la détermination de la liste des ingrédients de celle-ci. Le mode
de préparation est notifiée. Cette prescription peut viser également un MTA. Cette étape relève d’un
109

--- page 130 ---
Figure 5.8 – Description algorithmique de la première partie de l’UC2
aspect purement immatériel.
NB : Lister les ingrédients revient à la fois à lister les parties des ressources médicinales (RM) et les
RM dont ces parties émanent (e.g : feuille de neemier "Azadirachta indica A. Juss" ; la plante est
sous entendue donc).
– La seconde étape (étape 2) consiste à disposer effectivement des constituants physiques matériels
de la recette ou le MTA. Ces constituants sont essentiellement les parties des ressources médicinales
qu’on a appelées ingrédients.
En conséquence, nous pouvons éclater l’UC2 en deux parties : UC2a et UC2b d’objets respectifs étape
1 et étape 2. UC2a est la véritable prescription (à l’image de l’ordonnance médicale de la MM, Figure 5.8)
et UC2b porte sur la disponibilité physique de la recette et du MTA (figure 5.9).
En général, on note une forte implication voire un engagement certain du PMT pour disposer des
ressources physiques constitutives de la recette et même pour obtenir le remède. Le PMT manifeste la
volonté de suivre le patient tout le long de la maladie.
En cas de rareté ou de manque d’un ingrédient, ou simplement en cas de difficulté pour disposer d’une
110

--- page 131 ---
RM, le PMT effectue une recherche (menée par le PMT lui-même, ou à travers plusieurs canaux : patient
lui-même et son entourage, ou tous se mettent à la recherche, ou encore passer une commande, ...). Cela
peut consommer du temps. Le dynamisme des acteurs à la recherche peut être motivée par la gravité de la
maladie du patient. Au Sénégal, un PMT à Figo, nous confiait qu’il n’a jamais manquer de plantes pour
guérir ou soigner un patient. Il en prend partout où il veut dans le monde même hors du Sénégal (via des
voyages très particuliers).
5.4.3.3 Description de l’UC3
Tout d’abord, il faut enlever les parties toxiques des RM (ingrédients) de la recette physique quand elles
existent, avant sa préparation pour produire le remède. On peut adjoindre, combiner ou associer des RM
mais au delà d’un certain nombre de RM (3 plantes), il faut l’implication forte d’un PMT. La combinaison
des plantes peut s’avérer dangereuse. Également, est souvent opérée une adjonction d’excipients, de liants,
d’apaisants, d’adjuvants, de conservateurs, de colorants, d’arômes, d’épices, . . . à la recette. Le mode de
préparation et/ou celui d’administration appliqué par le PMT sont dits directs. En revanche quand, ils
sont effectués par une tierce personne (une personne autre que le PMT), nous parlons d’indirect. Les
figures 5.10 et 5.11 sont deux parties successives montrant et décrivant l’UC3.
Dans la description algorithmique de l’UC3, quoique le nombre de fois de l’administration du remède
(ou du MTA) sur le patient soit un ou plus d’un, à l’arrêt du traitement (fin de l’administration de remède
sur le patient), à l’initiative soit du PMT, soit du patient ou de l’entourage du patient, le recours à un
examen clinique pourrait permettre de savoir si le patient est guéri ou non. Bien entendu, ce test clinique
n’est pas obligatoire.
Le PMT est l’expert de la connaissance dans le domaine de la MT. En tant que tel, il prescrit et fait la
cueillette pour constituer la recette physique. Puis, il prépare cette recette pour fabriquer le remède qu’il
administre au patient. Le patient ou l’entourage du patient peut réaliser ces mêmes tâches, soit sous les
instructions strictes du PMT ou tout simplement parce qu’ils les ont apprises sans se prétendre être un
PMT. Néanmoins, la prescription est beaucoup plus propre au PMT.
NB : Plus précisément préparer la recette, c’est son inscription puis disposer de la recette physique,
c’est à dire ses constituants physiques. On peut là également parler de prescription du remède (englobant
définition de la recette puis recherche et disposition des constituants de la recette). Fabriquer le remède
signifie sa préparation.
Cependant, on note des dérapages dommageables causés par des personnes qui passent outre les ins￾tructions du PMT. Les programmes nationaux de promotion de la MT (PNPMT) et de sa modernisation,
des ONG dédiées également à des tâches similaires mènent à ce sujet des campagnes de sensibilisation à
l’endroit des populations urbaines et rurales.
Les programmes nationaux publics (comme le PNPMT) à travers les ministères de la santé, en plus
des associations et fédérations de PMT, sanctionnent les PMT qui ne suivent pas les règles et normes de
pratique et d’éthique dans leur art de guérisseur traditionnel ou art médical traditionnel. Ils détectent les
faux PMT.
111

--- page 132 ---
Figure 5.9 – Description algorithmique de la deuxième partie de l’UC2
112

--- page 133 ---
Figure 5.10 – Description algorithmique de première partie de UC3
113

--- page 134 ---
Figure 5.11 – Description algorithmique de la deuxième partie de UC3
114

--- page 135 ---
Figure 5.12 – Concepts de la MT qui découlent de l’UC1
5.5 Conceptualisation
La conceptualisation est la représentation mentale générale et abstraite d’un objet. C’est une idée que
l’on se fait de quelque chose. Le concept, unique dans une ontologie, est la manifestation de cette idée.
La conceptualisation consiste à faire émerger les concepts qui vont constituer la charpente architecturale
de l’ontologie. Le but recherché est de faire émerger les concepts, les abstractions, et de chercher à les saisir
par les signifiants (terminologiques) convenables et les plus représentatifs. Elle consiste à catégoriser les
instances en concepts, c’est-à-dire à mettre en relief les propriétés communes des instances individuelles
d’un même groupe.
En se servant de techniques et de procédés pluriels de recherche de l’information, une place de choix est
faite aux enquêtes et verbatim.
Nous avons effectué des analyses croisées sur les données recueillies lors des échanges avec les PMT par
spécialité et selon le niveau scolaire. La majorité de ces PMT est illettrée et parle des langues locales, nous
avons alors usé de traducteur interprète (guide-interprète). Très peu d’entre eux sont lettrés, le niveau
scolaire est hétérogène allant du primaire au professeur d’université.
Au delà des experts PMT, la bibliographie, l’observation naturelle et plusieurs autres sources notam￾ment (web, publication scientifique en biosciences, pour les plantes et autres, des ouvrages de références,
...), nous ont amenés aux activités clé pour conceptualiser :
– asseoir une stratégie sur le consensus des PMT ;
– importer, désambiguïser, transformer, désincarner (du PMT), contextualiser et décontextualiser ;
– désambiguïser (typologie, topologie, sémantique) ;
– co-modéliser (modélisation consensuelle) ;
– méthode de conception d’un modèle sémi-formel fondée sur une stratégie de comodélisation.
Parmi les sources que nous avons parcourues, nous avons [6], [7], [10], [20], [54], [71], [72], [124], [166],
[171], [170], [176], [185], [198], [246], [247], les sites 8 et 9
.
Les méthodologies NeOn [53], Diligent [77] et ontoForInfoSciences [160] ont été utilisées en partie pour la
modélisation conceptuelle. Concernant l’UC1, les concepts de la MT qui émergent sont mis en exergue à
travers la figure 5.12.
8. http ://www.ethnopharmacologia.org/recherche-dans-prelude/ ? consulté en 2015
9. http ://www.africamuseum.be/collections/external/prelude/view_plant ?pi=00600 consulté en 2015
115

--- page 136 ---
Dans une langue, il n’existe pas toujours un mot unique pour incarner pleinement un concept, surtout si
celui-ci est d’abord décrit dans une autre langue. Pour palier cet état de fait, on procède généralement par
une concaténation (plus explicite) de mots pour exprimer un concept. On a "Winery" en un seul mot en
anglais, dont l’équivalent en français utilise plus d’un mot notamment "Établissement vinicole" ou encore
"Établissement de production de vin". Cependant, "ÉtablissementVinicole", bien que compréhensible, ne
fait pas partie de la langue française. C’est un code, un mnémonique de terme conceptuel. Il peut être une
source de conflit (pitfall en ontologie), aussi il est préférable de trouver un synonyme adapté. Par exemple,
nous remplaçons le subsumant direct de symptôme et de Signe, initialement noté "SymptômeSigne" par
"Indice".
5.5.1 Cinq règles d’or pour initier la conceptualisation de manière compatible avec
Diligent, NeOn et ontoForInfoScience
Fondamentalement, dans notre démarche pour la construction d’une ontologie, nous nous sommes fiés
à cinq (5) règles d’or soutenues par Riichiro M [203] :
– (1) Un vocabulaire commun
La description du monde cible nécessite un vocabulaire adéquat entre les acteurs impliqués dans le
développement de la construction.
– (2) Expliciter ce qui est implicite
Il s’agit de donner les explications suffisantes à ce qui est souvent laissé implicite notamment des
hypothèses, des présuppositions ou les non-dits. Surtout dans le domaine comme celui de la MT, il
existe beaucoup de choses cachées et taboues qui ne sont pas facilement relevables. Il faut des moyens
d’élicitation et de facilitation à la fois doux, coriaces et intelligents dans le questionnement lors des
rencontres pour faire sortir les PMT de leur réserve. Les connaissances conceptuelles du PMT sont
le plus souvent abstraites quand bien même elles portent sur des choses concrètes et matérielles.
Nous avons effectué à plusieurs reprise des interviews et des croisements de points de vue de PMT
sur certaines plantes médicinales et les maladies traitées, pour arrêter les termes. Nous nous sommes
fait accompagnés par des interprètes traducteurs de langues locales également.
– (3) Catégorisation et systématisation des connaissances
Les concepts ne doivent pas rester au stade d’idée ou même de concepts. Il leur faut des objets pour
les saisir et les tenir. Des objets qui traduisent le sens commun. Il faut vérifier ce qu’il représente par
projection dans le réel. Ces objets ici sont les signifiants terminologiques ou les termes. On essaie
de voir si un terme convient pour designer tel concept. Et réciproquement repartant du concept,
de voir si le terme l’incarne bien. En effet dans le parcours discursif oral ou écrit les interlocuteurs
utilisent le "terme" pour décrire les phénomènes, les théories, les attentes et les objectifs visés. Une
ontologie contribue ainsi à fournir une épine dorsale pour la systématisation de la connaissance. Ce
sens commun est incarné dans une catégorisation. Cette dernière est parfois vue comme l’action de
juger le résultat d’une comparaison entre deux structures conceptuelles selon Jackendoff via [55].
– (4) Standardisation
116

--- page 137 ---
La standardisation du terme d’un concept résulte de trois niveaux : Le premier est celui après
contextualisation du terme tel que compris par les différents groupes de PMT pour la généraliser
à l’échelle de la communautaire régionale (Afrique de l’ouest) des PMT. Le second est au plan
des ontologies de la MT déjà réalisées (celles de gabarit embryonnaire à moyen). Les ontologies de
domaines sont embryonnaires. Le troisième niveau est de voir l’emploi du terme à titre de grande
référence, hors domaine dans lequel nous travaillons donnant lieu à d’autres domaines d’ontologies
et si possible les ontologies racines. Tout ce travail nous situe sur le niveau plus ou moins standard
du terme, En même temps, il s’agit d’un terme qui se voit appartenir à un vocabulaire commun
agrandissant son cercle de compréhension dès sa première inscription dans une ontologie.
– (5) Fonctionnalité méta-modèle
Un modèle relevant d’une ontologie est construit dans l’ordinateur comme une abstraction de la cible
dans le réel perçu et vivant. Partant de cette réalité, bien qu’annonçant la machine, nous traversons
plusieurs niveaux d’abstraction (conceptualisation et modélisation) hors machine. Dans la machine,
nous avons également d’autres niveaux d’abstraction (formalisation, implémentation, des réponses
traduites en d’autres objets artefacts suite à des requêtes, ces objets artefacts se projetant dans les
objets de la réalité avec similarité forte ou quelques biais surmontables). Une ontologie met en relief
des concepts et des relations entre eux qui sont utilisés comme blocs de construction du modèle
intégral. Elle spécifie les modèles à construire en fournissant les lignes directrices, les contraintes et
contingences (exceptions) à satisfaire. On a là, une fonctionnalité de méta-modèle et méta-niveau
assurée par une ontologie formelle. Ceci est bien illustré par les blocs d’abstraction et de composition
de sysMEDTRAD à base d’ontologies (cf figure 5.1).
Dans une ontologie bien construite, les termes peuvent avoir des définitions logiques (calculables) et
des définitions textuelles.
Les définitions textuelles précisent les conditions nécessaires et suffisantes pour l’utilisation correcte d’un
terme ; Ainsi, ils nous disent exactement ce qu’il faut retenir d’une entité si elle doit être une instance
d’un type donné, ou, en d’autres termes, si elle doit être membre d’une classe donnée. Alors que les
définitions textuelles sont utilisées par les utilisateurs humains d’une ontologie, les définitions logiques
sont utilisées par les ordinateurs. Ils fournissent la base sémantique pour permettre l’utilisation d’outils
appelés raisonneurs qui classent automatiquement l’ontologie et détectent des incohérences.
5.5.2 Acquisition de connaissances
Les connaissances en MT sont tacites et cachées. Elles sont difficiles à éliciter. En linguistique, l’élicita￾tion est l’incitation d’un locuteur à un autre à statuer sur différentes hypothèses, c’est-à-dire à introduire
chez lui le recours à sa compétence/performance. On recourt à des stratégies pour connaître la réaction
des locuteurs.
Nous avons utilisé de nombreux procédés de recueil de l’information : interview des PMT, sortie
de terrain avec reprise dans les centres de PMT, visite des ONG de promotion de la MT, réunion de
sensibilisation à travers les associations et fédérations de PMT, documents reçus d’ONG de promotion
de la MT et de programme de promotion de la MT (PNMPT), documents scientifiques de biosciences se
rapportant à l’ethnobotanique et la MT, aux ressources médicinales traditionnelles (Plantes, Animales),
publications et thèses sur la MT, visite de jardin botanique (e.g : Centre National de Floristique (CNF)
à l’Université Félix HOUPHOÜET-BOIGNY Abidjan cocody, autres jardins de PMT non nominatifs),
lecture des ouvrages livresques de référence traitant de la MT et des ressources du web traitant des
117

--- page 138 ---
plantes médicinales (PROTA) et sites de référence, passage en revue des ontologies existantes comme PO
(Plant Ontology).
Les difficultés d’élicitation sont aggravées par le fait que les PMT sont souvent illettrés. Afin de disposer
de sources de données, les visites de terrains considérées comme étant indispensables, ont été une charge
de travail importante pour nous. Ces visites ont consisté également à réaliser des entretiens avec des PMT.
Ainsi nous avons pu nous imprégner du comment et du lieu de leur exercice. Il s’agit notamment du cadre
ou du site dans lequel ils exercent. Nous avons été instruit des pratiques médicales de leur art de guérisseur.
Cette phase nécessite plusieurs visites successives : une pré-élicitation avec un ou de multiples retours. Nous
nous sommes servi de moyens de transports (mon véhicule en Côte d’ivoire pour les villes de Abidjan,
de Yamoussoukro et de Bouaké et villages environnants ; au Sénégal au même chapitre on note location
de taxis, utilisation de véhicule de transport commun en dehors de Saint-Louis, de taxis urbains) pour
visiter les PMT dans leurs secteurs, bourgs, villages, campagnes, centres urbains traditionnels, domiciles,
marchés, ... Nous avons eu recours à des interprètes (traducteurs) avec qui nous sommes venus à plusieurs
reprises (2 fois au moins à intervalles de 2, 4, 6 mois à une année) chez des PMT. La seconde visite a
porté sur le même sujet que la première, et l’on a cherché à déterminer ce qui était stable et renforcer les
questionnements sur ce qui avait varié.
Avant la sortie de terrains, sur la MT, s’agissant des travaux réalisés en biosciences, par la médecine
moderne, ou logés sur les sites internet consultés, les sources ont un niveau semi-formels ou formels pour
une élicitation directe. Pour certaines de ces sources comme PROTA 10 [198] et bien d’autres cas de ce type
ou encore livresques, nous avons collecté des données et nous les avons confrontées aux avis de certains
PMT (pré-élicitation).
En revanche, pour l’utilisation des travaux de biosciences, l’élicitation est directe.
L’ambiguïté est très caractéristique des langages naturels. Du fait que le traducteur lui-même est
souvent du même courant culturel que le PMT pour pouvoir interpréter, la continuité de l’empreinte
culturelle reste et, avec elle, les ambiguïtés. Nous avons pour cela adopté l’approche d’interviews avec retour
(ou reprises) afin de réduire le fossé sémantique. Nous avons eu recours à des rencontres de présentations
des travaux avec échange, sans ignorer celles des publications lors des colloques. Ceci évite que cette
sémantique soit dépendante du seul modélisateur.
Au final, nous avons rencontré plus d’une trentaine de PMT en Côte d’Ivoire dans les régions d’Abidjan,
de Yamoussoukro et de Bouaké et plus de 35 PMT au Sénégal à Dakar, et dans les régions de Saint-Louis,
de Richard Toll, Dagana et Podor. Les villages aux environs de celui de Figo sont bien fournis en PMT. Les
entretiens ont duré de 25 minutes à 1 heure. Certains PMT nous ont conduits vers d’autres de plus grande
renommée. Nous avons eu recours à des rencontres de présentations des travaux (au PNPMT à Abidjan).
Demba Mamadou au Sénégal (résidant à Saint-Louis) et Amessan Beugré en Côte d’Ivoire (résidant à
Abidjan), nous ont accompagné en explication et en traduction principalement. Ils nous ont également
servi d’indicateur des PMT, de leurs présidents de fédérations, d’associations.
En somme, les sources d’acquisition des connaissances auxquelles nous avons eu accès sont multiples.
Ces sources en ethnobotanique et en pharmacopée traditionnelle de la MT surtout portant sur l’Afrique
dans sa partie occidentale sont : [6], [3], [9] [10], [20], [54], [72], [78], [124], [171], [170], [176], [185], [198],
[246], [247], et les sites web 11, 12, puis l’annexe 1 (voir Annexe 1).
10. PROTA : Plants Resources Of Tropical Africa
11. http ://www.ethnopharmacologia.org/recherche-dans-prelude/ ? consulté en 2015
12. http ://www.africamuseum.be/collections/external/prelude/view_plant ?pi=00600 consulté en 2015
118

--- page 139 ---
Concept
majeurs :
PMT (Praticien de la Médecine Traditionnelle), Patient, Indices (Signes, Symptômes), Maladies,
Sources ou ressources médicinales (RM) (Plante), Examen clinique, Recette, Ingrédient, Partie de
ressource médicinale (PRM) : Partie de Plante, Partie d’Animal, partie de Minéral), Recette, Mode de
préparation de la Recette, Remède, Forme médicamenteuse ou galénique (forme de fin de préparation)
du Remède, Mode d’administration du Remède, FOrme (ancrage iconique) de ontoICONE (pour
FOrme voir la section 5.7.3 (figure 5.18) et le chapitre 6 (figure 6.12 de la section 6.4)).
Concepts
secondaires :
Centre de soins de santé, Sources ou ressources médicinales (RM), Contre-indications (état du
patient), Contre-association (interaction médicamenteuse dangereuse : de RM ou/et de PRM),
Propriétés (ou vertus thérapeutiques) de RM (Plante, Animal, Minéral), Excipient, Etiologie (de la
maladie), Anamnèse (du patient), Toxicité de la RM (Plante, Animal, Minéral, "Métaphysique"),
Iatrogénie, Anatomie, Croyance, Pays, Région, Localité, Références scientifiques (RM, Recette,
Remède), Systématique du vivant, Systématique de Maladie (CIM-10), Glossaire, Loi-Cadre (normes,
règles, discipline et sanctions) de la MT, ...
TABLEAU 5.5 – Concepts majeurs et concepts secondaires
5.5.3 Modélisation conceptuelle (UML)
La représentation profonde et ontologique d’un objet nécessite de mettre en évidence ses caractéris￾tiques essentielles suite aux préoccupations suivantes :
– de quoi est-il fait ? (matière, corps, énergie ou autre) ;
– quelle est sa provenance ? (causalité transitive) ;
– quelle est sa forme référentielle ? (apparence) ;
– quels autres objets lui ressemblent-ils structurellement au plan des données et à celui du comporte￾ment ? (Tous ces objets sont alors cernables dans un canevas : catégorie ou classe) ;
– quelles relations exprime-t-il avec les autres objets de son environnement proche ou distant (éloigné)
d’une part et d’autre part antérieurement, actuellement et postérieurement ? (relation) ;
– peut-on quantifier ou dénombrer tous les objets le ressemblant ? (cardinal du peuplement ou instan￾ciation) ;
– quels rôles joue-t-il ? (ses finalités).
Nous avons identifié les concepts que nous avons catégorisés en deux classes concepts majeurs et
concepts secondaires comme le montre le tableau 5.5.
5.5.4 Diagramme UML des classes relativement à ontoCONCEPT-Term
Le modèle de classes est présenté par la figure 5.13 dont la suite est l’annexe 2, en vue de la formalisation
de l’ontologie dans protégé. Les classes se trouvant à la fois dans cette figure et dans cette annexe servent
de points de jonction. Il s’agit donc d’un seul diagramme de classes nom complet car les attributs n’y sont
pas tous matérialisés. Seuls les noms des classes importent ici.
5.6 Concepts présents dans des ontologies ou ressources déjà existantes
Nous mettons en relief les concepts fondamentaux d’ontoMEDTRAD qui ont été retrouvés dans des
RTO ou dans des ontologies existantes, en indiquant de manière précise les sources (Url) ou la provenance.
119

--- page 140 ---
Figure 5.13 – Diagramme des classes (partie une)
120

--- page 141 ---
Termes de concept au nombre de 15 RTO existantes : librairies, thésaurus,
ontologies
Remarque
Français anglais
Plante Plant OBO, PSO, TO (Trait Ontology), PO,
NCBI organismal classification,
ontoBee
Animal Animal NCBI, ontoBee
Minéral Mineral ontoBee
Personne Person ontoBee
Patient Patient ontoBee
Anatomie (humaine) Anatomy OBO, FMA (Foundational Model of
Anatomy), ontoBee
Maladie Diseaese, Illness,
Disorder
NCBI, SNOMED-CT, IDO (infection
diseases ontology), CIM-10 (ICD-10),
ontoBee
Symptôme Symptom NCBI, SNOMED-CT, IDO (infection
diseases ontology), CIM-10 (ICD-10),
ontoBee
Remède Remedy NCBI, ontoBee
Recette Recipe NCBI, SIO
(Semanticscience Integrated Ontology)
existence
d’ontologies
culinaires
embryonnaires
[212]
Ingrédient Ingredient SIO, PDRO, FOODON (Food
ontology)
Coordonnée
géographiques
GPRS OGG-Dm ( Ontology of Genes and
Genomes) , PRO (PRotein Ontology)
Etiologie Etiology NCIT (National Cancer Institute
Thesaurus)
Anamnèse Anamnesis MeSH (Medical Subject Headings)
Pays Country FAO Geopolitical ontology
TABLEAU 5.6 – Indication de sources (RTO et ontologies) de concepts utilisés dans ontoMEDTRAD
Le tableau 5.6 liste les concepts retrouvés, et le tableau 5.7 les subsomptions et rôles.
Les ressources ontologiques suivantes FOODON 13, PRO 14 , PDRO 15, SIO 16, OGG-Dm 17, NCIT 18
et 19, TO 20 et 21, FAO Geopolitical ontology 22 sont consultables aux références web en pied de page-ci.
13. http ://www.obofoundry.org/ontology/foodon.html consulté en 2014
14. http ://www.ontobee.org/ontostat/pr consulté en 2017
15. http ://www.obofoundry.org/ontology/pdro.html conculté en 2015
16. http ://www.ontobee.org/ontology/SIO consulté en 2015
17. http ://www.ontobee.org/ontostat/OGG-Dm consulté en 2015
18. http ://www.ontobee.org/ontology/NCIT consulté en 2015
19. https ://bioportal.bioontology.org/ontologies/NCIT consulté en 2015
20. http ://www.ontobee.org/ontology/to consulté en 2015
21. http ://archive.gramene.org/plant_ontology/ontology_browse.html cpnsulté en 2014
22. http ://www.fao.org/countryprofiles/geoinfo/geopolitical/resource/ consulté en 2017
121

--- page 142 ---
Subsomption ou terme du rôle RTO existantes :
Librairies, thesaurus,
Ontologies
Remarque
Français Anglais E1 et E2 deux concepts
est un is_a Toute ontologie, OBO,
PSO, TO, PO, NCBI
organismal
classification, ontoBee
Dans toute ontologie, on a la subsomption au sens de
hyponymie/hyperonymie.
Plus explicitement,
(E1 est une hyponymie de E2) ↔ (E2 est une
hyperonymie de E1) :
E1 ⊑ E2 i.e "hyponymie ⊑ hyperonymie"
est une partie
de
part_Of NCBI organismal
classification, ontoBee
Dans certaines ontologies, on a la relation de partie à
tout (ou tout à partie) au sens de méréologie
(méronymie/holonymie).
Plus explicitement, (E1 est une méronymie de E2) ↔
(E2 est une holonymie de E1) : E1 partOf E2 i.e
"méronymie partOf holonymie"
TABLEAU 5.7 – Indication des sources (RTO et ontologies) pour les rôles et subsomptions utilisés dans onto￾MEDTRAD
5.7 Formalisation
5.7.1 Choix de l’outil de modélisation ontologique
Au regard d’OntoTools 23 et de la littérature, [42], [66], [86], [181], [204] et [227], il existe plusieurs
outils de modélisation et de formalisation qui ont fait l’objet d’une revue analytique et comparative selon
des critères précis. Parmi ces outils, ceux qui ont le plus attiré notre attention sont : Apollo, IsaViz ,
Swoop et Protégé.
Le tableau 5.8 compare ces 4 outils. Nous constatons que Protégé est davantage compatible avec le
cycle de vie méthodologique retenu à compter de la conceptualisation et surtout de la formalisation jusqu’à
la maintenance (cf les figures 5.3 et 5.4 pour le cycle de vie et la figure 5.5 pour le schéma récapitulatif
des étapes de construction d’une ontologie). Nous avons donc retenu l’éditeur Protégé, dans sa version 5.
5.7.2 Typologies des erreurs dans les ontologies de fondement existantes
L’examen des ontologies de haut niveau constitue une clé importante pour l’ingénierie ontologique.
Ces ontologies fournissent des indications sur la manière de construire une ontologie et un aperçu des
concepts et relations de base qui y sont utilisés. Ceci est un capital dont on pourrait se servir en terme
de partage et de réutilisation dans notre domaine de discours cible. Des exemples de ces ontologies sont
OBO, BFO, DOLCE, SUMO, CYC, ...[206]. Elles diffèrent par leur qualité et volume (quantité) s’agissant
de la représentation des concepts, des propriétés et relations. Certaines ontologies (OBO, BFO) vont
plus loin en mettant en évidence la distinction entre continuant et occurrents d’une part, et d’autre part
leur dépendance mutuelle. Plus spécifiquement au sein des occurrents, la distinction entre processus et
évènement est nettement mise en relief.
Lors du développement d’une ontologie, le modélisateur doit s’attaquer à un large éventail de difficultés,
pouvant être liées à l’inclusion ou l’introduction d’anomalies dans la modélisation. Dans ce contexte, OOPS
23. www.hozo.jp/OntoTools consulté en 2014
122

--- page 143 ---
Niveaux de
critères
Caractéristiques Protégé (5) IsaViz Apollo Swoop
Architecture
extensibilité oui via des
extensions
plug-ins
non non non
format de fichier
de stockage
fichiers fichiers fichiers fichiers
Interopérabilité
export/import HTML, Java,
XML, XMLS,
RDF(S), OWL,
OKBC
Protocole
XSLT, RDF(S),
OIL, OWL
OCML,
Okbc￾protocol
RDF(S), OIL,
DAML
fusion oui non non non
Service d’inférence
moteur
d’inférence
Pal, Fact+,
Hermit,
RacerProTG
1.2.0
non non non
contrôle de la
consistance
via plugins
comme Fact, and
pal
à travers
l’héritage
taxinomique et
détection de
cycles
oui contrôle restreint
sur les erreurs
relevant
seulement des
écrits seuls et
non des inférés
collaboration
avec d’autres
outils
oui oui non non
Utilisabilité visualisation plusieurs outils
de visualisation
par plug-in en
général
oui non non
Librairie /
bibliothèque
d’ontologies
oui non non non
Versioning et
support en
collaboration
versioning oui non non non
collaboration des
participants
en partie pas de
collaboration
pas de colla￾boration
en partie
TABLEAU 5.8 – Étude comparative de quelques outils éditeurs d’ontologies formelles
123

--- page 144 ---
Approches d’évaluation
Niveaux Norme d’or
(golden
standard)
A base
d’application
(application
based)
Par pilotage de
données
(Data-driven)
Évaluation
humaine
(assessment by
humans)
Lexicalité,
Vocabulaire,
concept, donnée
x x x x
Hiérarchie
(taxinomie ou
taxonomie)
x x x x
Autre relation
sémantiques
x x x x
Contexte et
application
x x
Syntaxe x x
Structure,
architecture et
conception
x
TABLEAU 5.9 – Quatre approches d’évaluation d’une ontologie (de domaine)
(OntolOgies Pitfalls Scanner), nous relève une trentaine d’erreurs typiques, après avoir analysé plus de
362 ontologies existantes (en utilisation) dont certaines sont mondialement reconnues et d’autres beaucoup
moins [155] [157] [168]. Ces erreurs typiques ont fait l’objet de plusieurs conseils, guides et indications.
L’évaluation de l’ontologie qui en vérifie la qualité technique par rapport à un cadre de référence, et sa
validation (consistance interprétative et faisabilité), jouent un rôle clé lors de tout cycle de développement
d’ontologies. Cette évaluation de l’ontologie peut viser différents niveaux [47]. Différentes approches d’éva￾luation existent. En dehors de l’approche humaine, celles que nous présentons ne couvrent pas l’ensemble
de ces niveaux de critères contenu dans le tableau 5.9.
5.7.2.1 Catalogue de 33 écueils communément rencontrés dans la construction des ontolo￾gies
Cette étude nous permet d’éviter les écueils couramment commis.
Plusieurs auteurs [29] [105] [155] [156] [157] [242] ont listé les types d’écueils retrouvés de manière
régulière dans de nombreuses ontologies (au nombre de plus de 350) de toute nature (fondationnelles
ou de fondement, noyau, domaine, application, tâche). Ces écueils sont notés de P1 à P35. Nous les
regroupons en neuf (9) divisions : de Div1 à Div9 (cf tableau 5.10). Les erreurs P34 (classe non typée)
et P35 (propriété non typée) ne concernent pas notre travail. Chacune des divisions est explicitée par des
points précis impactant directement ou indirectement des éléments devant constituer une ontologie ou
encore toute l’ontologie.
– div1 : Écueils relatifs aux concepts (cf tableau 5.11)
124

--- page 145 ---
Divisions Significations Écueils Nombre d’écueils
Div1 écueils relatifs aux concepts P1, P2, P6, P7, P21 5
Div2 écueils relatifs aux Concepts, relations
et propriétés
P4, P10, P11, P17, P18 P19,P23,
P28, P29, P33
10
Div3 écueils relatifs aux relations P5, P13, P24, P25, P26, P27 6
Div4 écueils relatifs aux propriétés P12 1
Div5 écueils généraux (annotations) P8, P9, P20, P22 4
Div6 écueils relatifs aux concepts, relation,
instances individuelles et valeurs
P3 1
Div7 écueils relatifs aux instances
individuelles et valeurs
P14 1
Div8 écueils relatifs aux axiomes P15, P16 2
Div9 écueil de définition de classe
d’équivalence
P30, P31, P32 3
Total 33
TABLEAU 5.10 – Catalogue des 9 groupes d’erreurs courantes dans les ontologies
Div1 P1 Création d’éléments polysémiques
P2 Création de synonymes en tant que classes
P6 Inclusion de cycles dans la hiérarchie
P7 Fusion de différents concepts dans la même classe
P21 Utilisation d’une classe diverse
TABLEAU 5.11 – Groupe 1 des erreurs relatives aux concepts
Div2 P4 Création d’éléments d’ontologie isolés (non connectés)
P10 Manque ou absence de disjonctions utiles
P11 Manque de domaines et de range
P17 Spécification de spécialisation trop avancée
P18 Spécification trop aigüe de domaine et de range
P19 permutabilité entre intersection et union (swapping)
P23 Utilisation incorrecte d’éléments d’ontologie (classe concept, relation ou
propriété)
P28 Définition de relations symétriques qui n’ont pas le même domaine ni la
même plage de range
P29 Définition de relations transitives qui n’ont pas le même domaine ni la même
plage de range prise deux à deux
P33 Création d’une chaîne de propriété avec une seule propriété
TABLEAU 5.12 – Groupe 2 des erreurs relatives aux concepts, relations et propriétés
125

--- page 146 ---
Div3 P5 Définition de mauvaises relations inverses
P13 Manque de relations inverse
P24 Utilisation de la définition récursive
P25 Définition d’une relation inverse à elle-même :
P26 Définition de relations inverses en lieu et place de relations
symétriques
P27 Définition de mauvaises relations équivalentes
TABLEAU 5.13 – Groupe 3 des erreurs relatives aux relations
Div4 P12 Absence de spécification de domaines de range des propriétés
TABLEAU 5.14 – Groupe 4 des erreurs relatives aux propriétés
– div2 : Écueils relatifs aux Concepts, relations et propriétés (cf tableau 5.12)
– Div3 : Écueils relatifs aux relations (cf tableau 5.13)
– Div4 : Écueils relatifs aux propriétés (cf tableau 5.14)
– Div5 : Écueils généraux (cf tableau 5.15)
– Div6 : Écueils relatifs aux concepts, relation, instances individuelles et valeurs (cf tableau
5.16)
– Div7 : Écueils relatifs aux instances individuelles et valeurs (cf tableau 5.17)
– Div8 : Écueils relatifs aux axiomes (cf tableau 5.18)
– Div9 : Écueils relatifs à la définition de concepts équivalents (cf tableau 5.19)
Div5 P8 Manque d’annotation des propriétés pour la compréhension
P9 Insuffisance d’information de base sur l’ontologie
P20 Permutation ou échange d’étiquettes et commentaires :
P22 Utilisation de différents critères de dénomination dans l’ontologie : absence de règles
de notation des termes
TABLEAU 5.15 – Groupe 5 des erreurs d’ordre général
126

--- page 147 ---
Div6 P3 Création de la relation "est" au lieu d’utiliser l’une des trois primitives
relationnelles suivantes : "sous-classe", "instanceOf" ou "même Individuel"
(notamment et respectivement “is” instead of using ”rdfs :subClassOf”,
”rdf :type” or ”owl :sameAs” )
TABLEAU 5.16 – Groupe 6 des erreurs relatives aux concepts, relation, instances individuelles et valeurs
Div7 P14 Mauvaise utilisation de "allValuesFrom"
TABLEAU 5.17 – Groupe 7 des erreurs relatives aux instances individuelles et valeurs
Div8 P15 Utilisation incorrecte "not some” et "some not"
P16 Utilisation incorrecte des classes primitives et définies
(ou abouties)
TABLEAU 5.18 – Groupe 8 des erreurs relatives aux axiomes
Div9 P30 Manque de classe d’équivalence
P31 Mauvaise définition de classe d’équivalence
P32 Plusieurs classes avec le même label
TABLEAU 5.19 – Groupe 9 des erreurs relatives à la définition de concepts équivalents
Échelle de préoccupation à
laquelle se rapporte le type
d’erreurs
Erreurs
Compréhension humaine P1
, P2
, P7
, P8
, P11, P12, P13, P19, P20, P22, P30, P32.
Consistance logique P5
, P6
, P14, P15, P18, P19, P27, P28, P29, P31, P33.
Représentation du monde réel ou
de la réalité
P5
, P9
, P10, P27, P28, P29.
Modélisation P2
. P3
, P4
, P5
, P6
, P7
, P10, P17, P11, P12, P13, P14, P15, P18,
P19, P21, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33.
TABLEAU 5.20 – Classification des erreurs par cause
127

--- page 148 ---
Notice : flèches en traits resp. discontinus et continus dénotant resp. object proprties et héritage
Figure 5.14 – Principales classes et relations d’ontoMEDTRAD
5.7.2.2 Classification des erreurs par cause
En outre, il existe d’autres typologies de catalogues au regard de l’impact de prise de conscience visé.
Ainsi, nous présentons une cartographie extraites de [157] à travers le tableau 5.20. Ici, nous avons un
catalogue d’erreurs courantes dans les ontologies et à quatre échelles de préoccupation.
5.7.3 Résultat : ontoCONCEPT-Term
La figure 5.14 montre la structure générale de l’ontologie ontoMEDTRAD et de sa couche terminolo￾gique ontoCONCEPT-Term [18].
128

--- page 149 ---
Contenu de ontoCONCEPT-Term de ontoMEDTRAD FIGURE
Aperçu d’ordre général classes 5.15 et 5.16
Propriétés 5.17
Iconisation classes pour iconisation (subsumées par Forme) 5.18
Propriétés pour iconisation (aPourForme) 5.19
TABLEAU 5.21 – Liste des figures des copies d’écran sous Protégé du contenu en partie de ontoMEDTRAD
ontoMEDTRAD 1.0 Nombre RTO existantes : Librairies,
thésaurus, Ontologies
Concepts 144 15 (cf tableau 5.7)
Rôles
Relations associatives (object
properties)
76 2
Propriétés (data properties) 16
Individus 789
Axiomes 2734
Famille de logiques de description : ALCHOIQ(D)
TABLEAU 5.22 – Métrique de ontoMEDTRAD
Les processus et activités en matière de délivrance de soins de santé via la MT sont décrits au sens
de Gaoussou [50] pour prendre en compte le contexte. Les copies d’écran suivantes, issues de Protégé,
montrent la liste des classes et des propriétés. Il s’agit des figures consignées dans le tableau 5.21.
Les sept (7) propriétés associatives (relations) sélectionnées comme le montre la figure 5.19 sont dans la
hiérarchie de racine aPourForme. Elles trouvent leur origine et raison d’être pour l’iconisation du concept
de Plante dans le chapitre 6.
Le tableau 5.22 donne la métrique de notre ontologie.
Voici quelques exemples de définitions que nous avons retenus dans l’ontologie ontoMEDTRAD :
– recette : un procédé pour obtenir une fin désirée ;
– plante : les plantes sont des organismes vivants qui appartiennent au règne végétal et qui possèdent
des racines et une partie aérienne ;
– arbre : plante lignifiée terrestre comportant un tronc sur lequel s’insèrent des branches ramifiées
portant le feuillage dont l’ensemble forme le houppier, appelé aussi couronne ;
– tige : partie axiale d’un végétal ;
– tronc : partie principale de la tige ;
129

--- page 150 ---
Figure 5.15 – Liste des classes sous Protégé de ontoMEDTRAD
130

--- page 151 ---
Figure 5.16 – Liste des classes avec le nombre d’individus ou d’instances par classe de ontoMEDTRAD
131

--- page 152 ---
Figure 5.17 – Liste des propriétés de ontoMEDTRAD
Figure 5.18 – Classes pour iconisation ontoMEDTRAD
132

--- page 153 ---
Figure 5.19 – Mise en relief des propriétés d’iconisation (Plante)
– feuille : organe aérien des végétaux ;
– fleur : partie de certains végétaux contenant les organes reproducteurs, souvent odorante et ornée
de vives couleurs ;
– racine : partie inférieure, le plus souvent souterraine, d’une plante vasculaire, qui permet la fixation
du végétal dans le sol tout en assurant son alimentation en eau et en sels minéraux ;
– sève : milieu intérieur fluide des plantes vasculaires dotées d’un double appareil circulatoire, s’écoulant
dans les différentes parties par les vaisseaux conducteurs des tissus, et assurant leur nutrition et leur
croissance ;
– écorce : enveloppe protectrice du tronc d’un arbre et de ses branches que l’on peut détacher du bois ;
– Maladie : altération (organique ou fonctionnelle) de la santé.
En particulier, nous avons vérifié que notre ontologie comprenait bien chacun des concepts nécessaires
clés pour réaliser l’iconisation des plantes et des recettes à base de plantes (qui feront l’objet du prochain
chapitre) : les types de plante (arbre, arbuste, palme, herbe, liane), et les neuf parties de plantes utilisées
(feuille, fruit, fleur, racine, tronc, écorce de tronc, écorce de racine, sève, plante entière), les ingrédients,
les recettes, les remèdes, les modes d’administration, et les modes de préparation. La maladie exemple est
le paludisme.
Deux indicateurs d’évaluation de l’ontologie ontoMEDTRAD propre à protégé : consistance
via raisonneur et expressivité Nous avons d’une part un niveau d’expressivité moyen (car l’excès
d’expressivité peut diminuer les performances machine), et d’autre part nous n’avons noté aucune incon￾133

--- page 154 ---
Figure 5.20 – Copie écran montrant l’exécution d’Hermit et l’expressivité de ontoMEDTRAD
sistance suite au lancement de plusieurs raisonneurs sous Protégé, notamment Hermit et Pellet (cf figure
5.20).
5.8 Synthèse
L’art de guérir par les plantes est connu et pratiqué en Afrique depuis bien avant l’ère de la MM. Les
PMT ou guérisseurs sont soit initiés à cet art soit exploitent des savoirs transmis oralement de générations
en générations. Nous avons également ceux ayant le don (innéisme) de guérir par les mêmes ressources
médicinales. Les PMT et les ressources médicinales (plantes, ...), les connaissances afférentes, constituent
un patrimoine important du continent africain [214].
Nous avons réutilisé des concepts isolés provenant d’ontologies et RTO existantes (e.g : PO 24, NCBI,
MesH 25, PSO 26, FOODON 27, SNOMED-CT 28, TO 29, OBO 30, CIM-10 31, ...), sans pour autant réutiliser
les ontologies existantes en entier, à cause des nombreuses spécificités propres à la MT. Nous avons pris
connaissances des erreurs (pitfalls) couramment commises dans la construction d’ontologie afin de nous en
prémunir et de les éviter.
24. http ://www.ontobee.org/ontology/po
25. https ://www.ncbi.nlm.nih.gov/mesh/
26. http ://www.sparontologies.net/ontologies/pso
27. http ://www.obofoundry.org/ontology/foodon.html
28. https ://bioportal.bioontology.org/ontologies/SNOMEDCT
29. http ://www.obofoundry.org/ontology/to.html
30. http ://www.obofoundry.org/
31. http ://apps.who.int/classifications/icd10/browse/2015/en
134

--- page 155 ---
Vu le volume considérable des travaux et la richesse de la MT, notre méthodologie globale de construc￾tion procède par étape et de manière incrémentale. C’est pour cela que, lors de la conceptualisation
d’ontoCONCEPT-Term, nous nous sommes appuyés sur les trois (3) cas d’utilisation (UC) amenant à
offrir des soins de santé primaires de MT au patient. Ceci nous a conduit à une description fine de ces
trois (3) UC pour faire émerger les concepts et relations à même de traduire la réalité de l’art médical
traditionnel de la manière la plus fidèle possible. Ceci nous a permis d’asseoir de manière importante
ontoCONCEPT-Term, la partie entièrement terminologique de ontoMEDTRAD.
Pour débuter l’iconisation, qui fera l’objet du chapitre suivant, il ressort que la description de l’UC2
et de l’UC3 se prête bien à une approche visuelle et iconique. Le langage iconique que nous décrirons
comprendra des icônes et des iconèmes pour la représentation des plantes médicinales, des recettes et
des remèdes traditionnels. Il sera rattaché à ontoCONCEPT-Term à travers un lien indispensable entre le
concept à iconiser et le descriptif graphique (visuel) terminologique y compris les couleurs. Il est en relation
entre ce descriptif et les iconèmes. Bien entendu, ce descriptif donne une représentation des iconèmes.
Nous avons décrit ainsi la conception d’ontoMEDTRAD et sa formalisation sous Protégé, à travers
sa couche terminologique, ontoCONCEPT-Term. La validation conceptuelle de l’ontologie pourrait être
réalisée en effectuant une vérification manuelle par des experts, en la comparant à un gold standard, ou
indirectement en évaluant des applications utilisant l’ontologie. Une seconde perspective est l’utilisation
d’ontoMEDTRAD dans des applications, tel que le système sysMEDTRAD dont nous avons présenté
l’architecture.
135

--- page 156 ---
Chapitre 6
Vers une ontologie visuelle : construction
d’un langage iconique pour les plantes
médicinales, les recettes et les remèdes
Sommaire
6.1 Position de ontoICONE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
6.2 Périmètre de notre travail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
6.3 Construction d’un langage iconique pour les plantes . . . . . . . . . . . . . . . 138
6.4 Génération automatique des icônes de plantes à partir de l’ontologie onto￾MEDTRAD (ontoCONCEPT-Term) . . . . . . . . . . . . . . . . . . . . . . . . . 154
6.5 Remarque importante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
6.6 Iconisation de la recette et du remède . . . . . . . . . . . . . . . . . . . . . . . . 157
6.7 Généralisation de l’iconisation des remèdes et recettes pour l’ensemble des
maladies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
6.8 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
6.9 Synthèse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
136

--- page 157 ---
Construire un outil collaboratif de travail pour les PMT qui leur permet de communiquer malgré
l’illettrisme, constitue un défi majeur. C’est pourquoi, nous proposons d’aller vers une ontologie visuelle
intégrant des icônes en plus des termes. Nous l’appelons ontoICONE. Dans ce chapitre, nous amorcerons
ce travail par la conception d’un langage iconique compositionnel pour identifier les plantes médicinales et
pour représenter les recettes des remèdes de la MT. La sémantique de ce langage iconique s’appuiera sur
notre ontologie de la MT (ontoCONCEPT-Term), qui a fait l’objet du chapitre précédent.
6.1 Position de ontoICONE
ontoMEDTRAD est structuré en deux modules sous forme de couches : ontoCONCEPT-Term et ontoI￾CONE. ontoICONE a pour support ontoCONCEPT-Term. ontoICONE partage une partie terminologique
de ontoCONCEPT-Term. Cette partie permet indirectement d’atteindre par la machine l’intelligibilité sé￾mantique iconique d’une part et l’inférence sémantique iconique d’autre part.
L’épine dorsale ou noyau de ontoMEDTRAD est ontoCONCEPT-Term. ontoICONE correspond à l’en￾semble des icônes ou pictogrammes dénotant des concepts de cette ontologie. La figure 1.1 en donne
l’illustration. La couche A de cette figure 1.1 représente l’ontologie de la MT via les termes et des axiomes
logiques. La description des concepts et des relations sémantiques entre ces concepts est d’ordre hiérar￾chique, de relation associatives et compositionnel par iconèmes et icônes. La couche B est associée à
un sous-ensemble des concepts de ontoCONCEPT-Term. La couverture des concepts par les icônes est
progressive.
6.2 Périmètre de notre travail
Le champ de la MT étant étendu, et vu la complexité des aspects de la visualisation, la construction
iconique se veut progressive. En effet, pour un concept donné, créer une icône pour le représenter demande
plus de travail que de le représenter par un terme. Ne pouvant donc pas réaliser la création des icônes
d’un trait pour l’ensemble des concepts de la MT, nous avons focalisé notre travail sur l’UC2 (définir
le remède ie définir la recette via ses ingrédients et son mode de préparation) et l’UC3 (préparer
le remède et l’administrer au patient) pour l’amorçage de l’iconisation. Nous avons choisi le paludisme
comme maladie contre laquelle est dirigée la finalité de UC1. Nous nous limiterons donc aux patients
atteints de paludisme. Nous argumentons ces choix dans les paragraphes suivants.
En général, lorsque la maladie du patient est déterminée (UC1), le premier réflexe cognitif du PMT
porte sur la ressource médicinale à partir de laquelle, il décèlera les parties devant servir à définir et à
composer la recette (UC2). De cette recette, pourra découler alors le remède (UC3).
Relativement à UC1, le paludisme (ou la malaria) a été pris comme maladie exemple. Cette infection
est classée parmi les maladies tropicales les plus morbides et mortelles en Afrique occidentale ([125], [133],
[136]). De plus, comme constatée lors de nos sorties de terrain, cette maladie est inscrite dans l’agenda de
la majorité des PMT pour le traitement des patients. Du coup, les cas d’utilisation UC2 et UC3 porteront
sur les recettes et les remèdes contre le paludisme. Bien entendu recettes et remèdes ont pour base les
ressources médicinales, premier matériel de travail du PMT.
A l’analyse de l’UC2, les ressources médicinales utilisées sont d’ordre végétal, minéral, animal et méta￾physique. Nous rappelons que les éléments métaphysiques (magico-religieux, ...) ne font pas l’objet de notre
présent travail. Parmi les ressources restantes, les plantes sont les plus dominantes dans les prescriptions
137

--- page 158 ---
des PMT. Pour preuve, La plupart des étalages [72] et boutiques des tradipraticiens en Afrique de l’ouest
abondent de plantes. Selon Kroa [136], les végétaux et surtout les plantes constituent de loin le lot le plus
important de l’arsenal thérapeutique traditionnel. C’est pourquoi, nous nous intéressons uniquement aux
remèdes antipaludiques à base de plantes. Sur ces dernières, un inventaire est nécessaire.
Une recette est une composition de parties de plantes (les ingrédients) avec un mode de préparation.
Un remède est l’ensemble constitué de la recette, la forme de fin de préparation (ou forme galénique) et les
modes d’administration. Pour cela, nous retenons comme concepts fondamentaux relevant de la MT, de
l’UC2 et de l’UC3 : Plante, Partie de plante, Mode de préparation, Forme de fin de préparation
et Mode d’administration.
NB : Nous faisons remarquer que conceptuellement préparer un remède au regard du chapitre précédent
à travers l’UC3, repose ou revient pragmatiquement et plus finement à préparer la recette émanant de la
prescription du remède. Ainsi, dans ce qui va suivre précisément en section 6.6 (du présent chapitre 6),
notre modélisation rattache mode de préparation à recette.
Il convient alors, au regard de ce qui précède, d’amorcer l’iconisation avec le concept de Plante de notre
ontologie ontoMEDTRAD (ontoCONCEPT-Term). En MT, il est clairement notifié la préexistence de la
plante à la recette et au remède. Les icônes de plantes qui seront obtenues feront partie d’ontoICONE.
Notons également que le nombre élevé d’espèces de plantes médicinales en Afrique de l’ouest estimé à plus
de 500 [8] [136], constitue une difficulté majeure pour que les PMT les mémorisent, mais aussi pour que
nous puissions les représenter par un jeu d’icônes. Ainsi, créer une icône pour chaque espèce impliquerait
une multiplication d’icônes difficilement maîtrisable par le PMT.
Suite à ce constat, il parait nécessaire de mettre au point un langage iconique combinatoire pour
présenter visuellement les plantes médicinales et permettre leur reconnaissance distinctive. Ce langage
permettra de créer de nombreuses icônes à partir d’un jeu restreint de pictogrammes et d’iconèmes.
6.3 Construction d’un langage iconique pour les plantes
Cette partie porte sur l’extraction d’un jeu de données, la définition de critères valeurs (attributs￾valeurs), leur sélection automatique (via weka), dessin des iconèmes et leur assemblage automatique don￾nant l’icône du concept de plante.
6.3.1 Extraction d’un jeu de données (31 remèdes et 22 plantes)
Nous avons eu recours à un florilège de plantes médicinales antipaludiques collectées en pharmacopée
traditionnelle. Notre anthologie de plantes est constituée d’un échantillon de vingt deux (22) espèces
végétales médicinales utilisées dans trente et un (31) remèdes, suite à nos recherches bibliographiques
basées sur des résultats de travaux botaniques et ethnobotaniques en biosciences concernant la MT. Nous
avons eu également recours à des ressources bibliographiques en ligne (comme PROTA 1, 2). Nous avons
confronté cet échantillon de plantes anti-malaria avec les avis des PMT lors de nos multiples visites de
terrain (en Côte d’Ivoire et au Sénégal). Tous les PMT ont (re)confirmé à 100% les valeurs thérapeutiques
de ces plantes contre le paludisme. Parmi ces plantes ainsi ciblées, certaines comme le neemier (Azadirachta
indica A. Juss. (Meliaceae) ou neem), sont connues de manière populaire tant dans les villes que dans les
villages d’Afrique de l’ouest pour leur efficacité contre le paludisme. Cette plante neemier a une appellation
célèbre "d’arbre à pharmacie".
1. PROTA : Plants Resources of Tropical Africa consulté en 2015
2. http ://uses.plantnet-project.org/fr consulté en 2015
138

--- page 159 ---
En général, les différents travaux analysés présentent leurs résultats sous forme de tableau. Les colonnes
de ces tableaux indiquent la plante médicinale notifiée par son nom botanique, les parties utilisées, les
modes de préparation (en abrégé MP, e.g : décoction), les modes d’administration (en abrégé MA, e.g :
boisson), les indications (maladies ou symptômes). Sont parfois également présents les noms en français
ou en anglais, et les noms locaux des plantes et des maladies. S’agissant de ces noms en langues locales,
les termes de ces noms sont exprimés en utilisant l’alphabet de la langue officielle. La plupart des langues
locales ou dialectes ne sont pas écrits. On parle alors de langage parlé (langue locale) et non écrit. Une
"bonne" langue officielle est un langage parlé et écrit.
L’extraction des 22 plantes pouvant combattre le paludisme est la résultante d’analyse croisée entre les
sources précédentes et celles relatives notamment à la documentation reçue du PNPMT (Côte d’Ivoire)
et celle de l’ONG (Prometra) du Sénégal. Ces sources multiples en ethnobotanique et en pharmacopée
traditionnelle de la MT surtout incluant l’Afrique de l’ouest sont [6], [7], [10], [20], [54], [71], [72], [124],
[166], [170], [171], [176], [185], [198], [246], [247], les sites 3 , 4. Les séminaires et ateliers auxquels nous avons
eu droit de participer, nous ont été très instructifs en matière de thérapie par les plantes médicinales.
A travers les tableaux 6.1 et 6.2, nous donnons respectivement les 22 plantes et les 31 remèdes retenus.
Un travail important a été nécessaire pour rechercher, extraire, recouper, et structurer ce jeu de données,
en particulier à cause de la confusion fréquente entre plantes et remèdes dans les sources. Nous avons
rajouté au tableau 6.2 la colonne de la forme de fin de préparation (ou Forme Galénique) en abrégé FFP
(ou FG). Notons que la plupart des remèdes contiennent une seule plante (mono-spécifiques), mais que
certains en comprennent plusieurs (jusqu’à 5) (multi-spécifiques).
Nous devons à présent trouver des critères sur les aspects visuels pour caractériser chacune des 22
plantes. Pour cela, nous procéderons aux étapes suivantes :
– définir les critères possibles ;
– définir les valeurs possibles des critères ;
– sélectionner les critères à retenir.
6.3.2 Définition des critères
Nous nous sommes intéressés à la partie de la botanique (la science ayant pour objet l’étude des
végétaux) relative aux caractéristiques morphologiques des plantes. De toute évidence, les différentes par￾ties d’une plante feront l’objet de la description visuelle iconique que nous mettons en œuvre. Pour cela,
nous avons passé en revue chacune des 22 espèces végétales antipaludiques. Ainsi pendant cette tâche
d’analyse méticuleuse, difficile et longue, les éléments caractéristiques de la botanique physique relatifs
aux différentes parties de la plante notamment : feuilles, fruits, fleur, tronc (branche, tige, stipe, rameau,
brin, brindille), fleurs, écorces, épines, racines, sève, ..., nous ont été d’un précieux apport. Chaque partie
matérielle de la plante fait l’objet d’une description détaillée. Dans un premier temps, nous avons arrêté
de manière "naïve" 42 critères après le parcours des descriptions botaniques. Le nom botanique ne peut
bien évidemment pas être considéré comme critère car il n’existe pas de manière directe de le traduire en
icônes non textuelle. En outre, sous forme d’une résultante, ce nom botanique de l’espèce est la cible
(classificatoire) sur laquelle devront s’appliquer les autres critères. La liste des 42 critères est donnée dans
les tableaux 6.3 et 6.4.
139

--- page 160 ---
N°PL. Plantes
1 Adenia lobata (Jacq.) Engl. (Passiflore)
2 Ananas comosus (L.) Merr. (Bromeliaceae)
3 Azadirachta indica A. Juss.( Meliaceae)
4 Carica papaya L. (Caricaceae)
5 Chrysophyllum africanum A. DC. (Sapotaceae)
6 Citrus aurantifolia (Christm.) Swingle (Rutaceae)
7 Cochlospermum tinctorium Perr. Ex A. Rich.( Cochlospermaceae)
8 Cocos nucifera L. (Arecaceae)
9 Combretum micranthum G. Don(Combretaceae )
10 Cymbopogon citratus (DC.) Stapf (Poaceae)
11 Enantia polycarpa (DC.) Engl. et Diels (Annonaceae)
12 Eucalyptus camaldulensis Dehnhardt (Myrtaceae )
13 Ficus exasperata Vahl (Moraceae)
14 Hibiscus sabdariffa L. (Malvaceae)
15 Lannea microcarpa Engl. et K. Krause (Anacardaiceae)
16 Manihot esculenta Crantz (Euphorbiaceae)
17 Musa x paradisiaca L. (Musaceae)
18 Nephrolepis biserrata (Sw.) Schott. (Davalliaceae)
19 Scaphopetalum amoenum A. Chev. (Malvaceae)
20 Senna alata (L.) Roxb. (Fabaceae-Caesalpinioideae)
21 Senna occidentalis L. (sfamille Caesalpinaceae )
22 Vernonia colorata (Willd.) Drake (Asteraceae )
TABLEAU 6.1 – Liste des 22 plantes anti-malaria
Il existe des feuilles simples et des feuilles composées de plusieurs folioles. Lorsque nous parlons de
feuille sans précision, alors il s’agit de feuille simple ou de la foliole d’une feuille composée. Lorsque nous
parlons d’une feuille composée nous le préciserons systématiquement.
Nous ne devons pas perdre de vue la minimisation du nombre de critères pour une fin de non surcharge
de l’icône.
6.3.3 Définition des valeurs des critères
Pour chaque critère qualificatif, nous avons défini les valeurs possibles. Nous avons cherché à minimiser
le nombre de valeurs par critères, par souci de simplicité, tout en permettant la reconnaissance individuelle
des 22 espèces végétales. La grande variabilité de la description botanique peut amener à deux constats :
1. Pour une forme de fruit d’une espèce de plante donnée, la même forme peut être désignée différem￾ment selon le botaniste. Par exemple elliptique, obovale ou ovale pour la forme du fruit de neemier
(Azadirachta indica A. Juss) ;
2. Le degré de précision souvent élevé en botanique de la même forme de feuille donnée conduit aux
qualifications suivantes : rectiligne, en aiguillon, en aiguille. C’est souvent une volonté d’affinement
3. http ://www.ethnopharmacologia.org/recherche-dans-prelude/ ? consulté en 2015
4. http ://www.africamuseum.be/collections/external/prelude/view_plant ?pi=00600 consulté en 2015
140

--- page 161 ---
N°Rmd N°PL Partie utilisée (PU) MP MA FFP(FG)
1
3
21
feuille
feuille
décoction fumigation et boisson liquide
2
21
3
feuille
feuille
décoction boisson et bain liquide
3 21 feuille décoction boisson liquide
4 1 feuille décoction boisson liquide
5 1 tige décoction boisson liquide
6 15 écorce- racine- feuille décoction boisson et bain liquide
7
20
4
22
feuille
feuille
feuille
décoction boisson et bain liquide
8 20 feuille infusion boisson liquide
9
22
20
feuille
feuille
décoction boisson et bain liquide
10 4 feuille décoction boisson liquide
11 4 fleur infusion boisson liquide
12 4 fruit pétrissage absorption pâte
13
4
2
6
21
8
fleur
fruit
fruit
feuille
racine
décoction boisson liquide
14
10
14
16
6
feuille
pétiole
feuille
fruit
décoction boisson liquide
15 5 feuille décoction bain de vapeur vapeur
16 5 écorce de tige pétrissage boisson liquide
17 20 feuille décoction bain de vapeur vapeur
18 20 feuille décoction ablution liquide
19
21
11
écorce de racine
écorce de racine
pétrissage purge et badigeonnage pâte
20 21 feuille décoction ablution liquide
21 11 écorce décoction boisson liquide
22 11 écorce macération purge liquide
23 13 écorce de tige macération boisson liquide
24 13 écorce de tige pétrissage (piment) purge liquide
25 9 racine séchées décoction boisson liquide
26
17
6
feuille
fruit
décoction boisson liquide
27 19 feuille décoction bain de vapeur vapeur
28 19 feuille macération alcoolique boisson liquide
29 7 racine séchée décoction boisson liquide
30
18
4
6
feuille fraiche
feuilles sèche
jeune feuille
décoction boisson liquide
31
12
4
21
feuilles
feuille sèche
feuille
décoction
boisson, fumigation et bain de
vapeur
liquide
TABLEAU 6.2 – Liste de trente un (31) remèdes traditionnels
141

--- page 162 ---
Critère Valeurs
1 silhouette de la plante
arbre, arbuste, arbrisseau, sous-arbrisseau, arbuste lianescent,
herbacée, herbacée vivace, arbre fructifère, palmiers, bambou
2 feuillage de la plante caduque, persistant
3 tronc existant booléen
4 longueur du tronc réel
5 largeur du tronc réel
6 longueur du fruit réel
7 largeur du fruit réel
8 longueur de la feuille réel
9 largeur de la feuille réel
10 écorce du tronc lisse, fissurée, cannelée, fibreuse, crevassée
11 écorce du tronc se détachant lanière, plaque, écaille
12
pétiole/pédoncule (fixant la feuille, la
fleur, le fruit)
court : <= 1 cm, ; moyen : > 1 cm et <= 5 cm, long : > 5 cm,
sessile : 0 cm
13 forme de feuille simple ou foliole
elliptique, orbiculaire, peltée, réniforme, cordée, obcordée,
orbiculaire, rhomboïdale, spatulée, triangulaire, conique, sagittée,
hastée, longue, oblongue, panduriforme, acutilobée, lunée, lunulée,
cunéiforme, peltée, deltoïde
14
forme de la feuille simple ou foliole
(pennée, palmée, pédalée)
pennatilobe, pennafide, pennapartite, pennatisequee , palmatilobe,
palmatifide, palmatipartite, palmatisequee, pédatilobe,
pédatifide, pédatipartite, pédatisequée.
15
pénnation nervure de feuille simple ou
foliaire
alterne, opposée, palmée, pédalée, anastomosée, uninervée,
transverse, réticulée, dichotome, parallèle, en éventail, curvinervée,
peltée
16 pénnation feuille composée 1 paripenné, imparipennée
17 pénnation feuille composée 2 pennée, bipennée, tripennée, quadripennée
18 pennation feuille composée 3 trifollée, palmée, pédalée, pectinée
19
disposition de la foliole sur axe feuille
composée
alterne, opposée
20
disposition de feuille sur tige/stipe ou
tronc (Feuille simple ou feuille
composée)
alterne, opposée, touffe, verticille, spirale, générique
21 couleur Feuille vert pur foncé, vert clair, rouge bordeau, jaune
22
épine existant en une partie
quelconque de la plante
booléen
23 épine de tronc tige branche booléen
24 épine de feuille booléen
25 épine de fruit booléen
TABLEAU 6.3 – Liste des critères
142

--- page 163 ---
Critère Valeurs
26 épine de fleur booléen
27 épiné de racine booléen
28 forme de fruit ronde, ovale, allongée, triangulaire
29 de fruit texte
30 fruit très connu (populaire) booléen
31 fruit comestible par homme booléen
32 couleur de fleur texte
33 vrille (plante rampante) booléen
34 stipule (plante non rampante) booléen
35 nombre de pétales de corole fleur entier
36 nombre de pétales de calice fleur entier
37 sève booléen
38 couleur de sève texte
39 organe fruit souterrain booléen
40 forme organe fruit souterrain ronde, ovale, allongée, triangulaire
41 graine ou pépin booléen
42 sexe de la plante mâle, femelle
TABLEAU 6.4 – Liste des critères (suite)
et de précision distinctive affichée par le botaniste (souvent propre à la zone ou au milieu floristique
étudié).
Pour le besoin iconique, nous avons décidé de simplifier et d’effectuer des regroupements pour ne
conserver qu’une seule valeur de forme parmi les trois qualifications : elliptiques, obovales et ovales. Ici
nous retenons elliptique. Nous avons simplifié les formes de feuilles de la même manière en retenant
elliptique.
Dans notre démarche, nous avons considéré des catégories génériques correspondant à des formes géo￾métriques simples (ellipse par exemple). Quand cela s’avère complexe voire impossible de faire correspondre
une forme donnée à une forme générique, nous avons considéré des formes spécifiques, surtout lorsqu’elles
sont soutenues par la connaissance ou la reconnaissance populaire. Ces dernières formes sont également
dites typiques. Par exemple, la feuille du cocotier (cocos nucifera L.) a une forme spécifique très recon￾naissable, et nous avons décidé de la conserver comme telle (voir tableau 6.12). De même pour la forme
du fruit banane. Une forme spécifique (typique ou prototypique) peut être affectée à une autre espèce de
plante moins connue (ou reconnue), à partir du moment où cette forme est la même que l’autre plante
moins célèbre.
En dehors de la silhouette considérée indispensable (une sorte de moment d’unité [43]) pour le concept
de plante, il est possible qu’une espèce de plante donnée, n’ait aucune valeur pour un critère donné. Il ne
s’agit pas d’une valeur manquante ou absente mais de valeur inexistante. Par exemple, on pourra mettre
"pas de fruit" comme valeur au critère forme de fruit, pour les plantes non fructifères. En revanche, il
existe des cas où l’espèce de plante a plus de deux valeurs pour un critère (à multiples valeurs). Cette
propriété est systématiquement remarquée sur les individus.
Certains critères (comme la couleur de fleur) peuvent prendre plusieurs valeurs (par exemple blanc,
jaune, bleu) pour une même plante. Nous autoriserons jusqu’à deux valeurs différentes pour une plante
donnée, mais nous n’irons pas au-delà, afin de ne pas surcharger les icônes. Dans de tels cas, nous devrons
lui associer deux iconèmes dont un par valeur.
143

--- page 164 ---
Figure 6.1 – Impact du moment d’unité dans la reconnaissance d’une image iconique
NB : Dans une icône d’un concept, quand il se dégage un iconème ayant le plus de liens sémantiques
avec les autres parties ou avec les autres unités signifiantes, ce dernier est qualifié de moment d’unité (cf
figure 6.1.). Son absence peut impacter négativement le sens visuel à accorder à l’icône du point de vue de
l’utilisateur final, car simplement, sémantiquement, les liens de ce moment d’unité avec les autres parties
(le tronc en rapport avec un membre supérieur (cf figure 6.1) ne sont pas pris en compte (décrits) par la
machine ici.
6.3.4 Sélection des critères
Nous avons effectué la sélection des critères en deux étapes : pré-sélection manuelle et sélection d’at￾tributs avec Weka (version 3.8).
Étape 1 : pré-sélection manuelle
Ce premier niveau de sélection des critères est fait en se basant sur les éléments suivants :
– le contexte et l’environnement de travail du PMT ;
– la reconnaissance populaire du critère (la forme du fruit est davantage connue que la forme de la
racine par exemple) ;
– la limitation du nombre de critères pour éviter la surcharge iconique ;
– la facilité à présenter visuellement le critère (par exemple une couleur est facile à représenter), selon
l’une au moins des trois règles de la stratégie de représentation (voir chapitre 4) : la similarité visuelle
ou analogie, l’association sémantique, la convention arbitraire.
Le type de plante en terme de classification est diversement décrit par différents auteurs botanistes.
Nous donnons un exemple à travers le tableau 6.5. Au regard de la grande variabilité de la description
144

--- page 165 ---
selon "Classe des plantes, Types
biologiques chez les végétaux
intertropicaux par J. L. Trochain" [229]
selon "Familes des plantes par M.
Adanson" Académie des Sciences [5]
1- Herbes mineures
2- Sous-arbrisseaux
3- Herbes majeures
4- Plantes herbacées
7- Plantes charnues
6- Arbrisseaux
8- Arbustes
9- Palmiers, bambous
10- Arbres (des boisements clairs)
11- Arbres ou grands arbres (des forêts)
1- Arbres
2- Arbres fructifères
3- Arbres et Arbrisseaux. Baccifères
4- Siliques
5- Arbrisseaux
6- Arbrisseaux grimpants
7- Herbes
8- Herbes pommifères et légumineuses
TABLEAU 6.5 – Différentes classifications des types de plantes selon deux botanistes
faite par les botanistes sur ce sujet, nous avons choisi de retenir le terme de silhouette plutôt que "type
de plante".
Ce critère silhouette que nous considérons comme central pour une plante, a cinq valeurs que nous
projetons d’arrêter : arbre, arbuste, palme, liane, herbe. Ce critère a un caractère stable et est indispensable
pour la plante. Les PMT, acteurs principaux et utilisateurs centraux, ont émis des avis favorables pour ces
silhouettes surtout lors de notre présentation au siège du PNPMT en février 2016 au Plateau (Abidjan).
Bien que la majorité des PMT soient analphabètes, on note parmi eux, des universitaires, des enseignants
chercheurs et des botanistes.
Par ailleurs, vu la complexité à représenter les dimensions, c’est à dire à apprécier sur les icônes une
distance ou une longueur, les critères de hauteur, de longueur et de taille (exemple dans la liste de critères
de base : du n°4 au n °9) n’ont pas été retenus (voir tableaux 6.3 et 6.4).
Nous avons retenu un premier lot de 13 critères numérotés de 1 à 13, au terme de cette première étape.
Ce sont :
1. silhouette ;
2. disposition de la feuille ;
3. fixation de la feuille composée ;
4. forme de la feuille ;
5. pennation de la feuille composée ;
6. épine de la branche ;
7. épine de la tige ;
8. épine de feuille ;
9. épine du fruit ;
10. forme du Fruit ;
11. couleur du Fruit ;
145

--- page 166 ---
Figure 6.2 – 13 critères attributs de description des 22 plantes
12. comestible du fruit par l’homme ;
13. couleur de la fleur.
Étape 2 : sélection d’attributs avec Weka (version 3.8)
Dans un second temps, nous avons effectué une sélection d’attributs (features selection) à l’aide d’algo￾rithmes d’apprentissage. Nous avons utilisé WEKA, pour définir le poids de chaque critère au regard des
valeurs prises par espèce de plante. Weka 5
(Waikato Environment for Knowledge Analysis) est une suite
de logiciels d’apprentissage automatique (Machine learning). Weka ne permet d’avoir qu’une seule valeur
pour un critère, pour une espèce donnée. Lorsque nous avions plusieurs valeurs, par exemple des fleurs
jaunes et blanches, nous avons retenu arbitrairement l’une des deux valeurs.
L’usage que nous avons fait de Weka est principalement celui de ses deux modules Ranker et Jrip.
Nous avons utilisé d’abord Ranker pour la sélection des critères. Ces critères sont des attributs (attributes
en anglais) sous Weka et les 22 espèces les instances. Les critères les plus utiles pour distinguer nos 22
plantes ont un poids plus élevé.
Le fichier des 22 plantes avec les 13 critères, au format CSV (noté donc botanique22.csv), une fois
chargé dans Weka pour l’analyse, la liste des attributs y est bien indiquée (voir figure 6.2 ).
Un poids (weight) est affecté par Ranker à chaque critère (voir figure 6.3 ). Cette valeur calculée pour
chaque critère montre sa capacité à distinguer les 22 individus (instances de plantes).
Les critères candidats à l’élagage sont cochés et les autres sont ceux qui sont retenus (voir figure 6.4).
5. https ://www.cs.waikato.ac.nz/ml/weka/ consulté en 2014
Traduit en français : "Environnement Waikato pour l’analyse de connaissances"
146

--- page 167 ---
Figure 6.3 – Poids des attributs des plantes
Figure 6.4 – 6 Critères candidats à l’élagage
147

--- page 168 ---
Figure 6.5 – Paramétrage de JRIP
Jrip est un module d’apprentissage supervisé et de classification automatique. Nous avons modifié les
paramètres usePruning et minNo. usePruning est mis à "false" pour prendre en compte la totalité des
plantes sans élagage des règles concernant un nombre de plantes trop petit. La valeur de minNo mise à 1
signifie qu’une règle peut être créée pour une seule plante (voir figure 6.5).
La classe nominale est ici le nom botanique de la plante. Chacune des 22 espèces a donc un nom
botanique distinct des autres que nous retenons. Nous avons utilisé JRip pour vérifier que les critères
retenus permettaient bien de distinguer de manière univoque à 100% nos 22 plantes par classification.
Dans ce processus on estime que c’est une classification supervisée avec les classes qui sont les 22 espèces
de plantes.
Critères retenus
Le nombre de critères retenus est de sept (7). Ce sont :
1. Silhouette,
2. Forme de fruit (FormeFruit),
3. Disposition de la feuille(DispositFeuille),
4. Forme de la feuille (FormeFoliaireFeuille),
5. Pennation de la feuille (PennationFeuille),
6. Couleur du fruit (CouleurFruit),
7. Couleur de la fleur (CouleurFleur).
Ces critères constituent des attributs ; chacun d’eux a un ensemble de valeurs qui lui est propre. Nous
considérons (hissons) ces critères comme des classes dans notre ontologie (ontoMEDTRAD) et les valeurs
prises comme étant les instances. Les 22 espèces de plantes sont les instances de la classe Plante. Plante
est en relation avec chacun des sept critères (classes). En supprimant les nœuds Fruit, Fleur et Feuille,
148

--- page 169 ---
Figure 6.6 – Illustration de la classification à 100% des 22 espèces de plantes
dans la structure arborescente de la figure 6.7, nous obtenons les relations entre la racine (Plante) et les
nœuds terminaux (les sept (7) critères 6.8 ).
Nous passons à présent à l’élaboration des iconèmes afférents.
6.3.5 Dessin des iconèmes et choix des couleurs
Pour chaque valeur de chaque critère, nous faisons correspondre une couleur ou un iconème que nous
avons dessiné à l’aide d’InkScape. InkScape est un logiciel vectoriel de dessin utilisant le format d’image
SVG. Il est compatible avec XML. Par exemple la figure 6.9 montre les iconèmes réalisés pour le critère
silhouette.
A travers le tableau 6.6, nous donnons quelques exemples relatifs à la pennation, à la forme de feuille
et à la forme de fruit. Nous avons admis une seule couleur de feuille, qui est la couleur verte.
Dans notre démarche d’élaboration des icônes des espèces de plantes, nous avons pris en compte la
possibilité de combiner couleurs et iconèmes pour des critères. Il existe également pour un même critère
la possibilité d’assigner des valeurs multiples (jusqu’à deux). Nous explicitons ces deux situations dans les
deux paragraphes suivants.
149

--- page 170 ---
Figure 6.7 – Mise en relief de la relation entre plante et les sept critères
Figure 6.8 – Relation de la Plante avec chacun des (7) sept critères
arbre arbuste palme liane herbe
Figure 6.9 – Les cinq iconèmes pour le critère silhouette
150

--- page 171 ---
Forme de la feuille
entière oblongue lancéolée
feuille du cocotier
(cocos nucifera)
palmatilobe
Pennation
paripennée imparipennée
Forme de fruit
banane rectiligne elliptique ailée allongée
Notice : La feuille de la plante Nephrolepis biserrata (Sw.) Schott. (Davalliaceae) communément appelée fourgère, est
spécifique (typique) et reconnue comme telle. Bien que prise en compte, elle ne figure pas dans la liste d’exemples de
formes de feuille ici fournie. Pareillement, d’autres typicalités (formes typiques) sont faites pour les formes de fruit :
banane, melon, ananas.
TABLEAU 6.6 – Exemples d’iconèmes relatifs aux formes de feuille, de fruit et à la pennation
Combinaison des couleurs et des iconèmes
Nous avons considéré une classe Couleur dont le nombre d’instances n’est pas limitée. Rouge, vert,
orange, jaune, vert gris, blanc sont quelques instances de couleur. Le caractère couleur est porté par les
parties de la plante ici concernées, nommément les feuilles, les fleurs et les fruits.
Pour les feuilles, la couleur de la feuille ne fait pas partie des sept critères retenus. De ce fait, nous avons
admis une seule couleur de feuille : la verte. Les iconèmes de feuilles (Forme de la feuille) seront donc tous
combinés à la couleur verte.
Pour les fruits, nous combinons la couleur du fruit aux iconèmes représentant les formes de fruit
spécifiques (banane, melon, ananas, ...) ou génériques (allongé, triangulaire, conique, rectiligne, rond).
Pour les fleurs, la couleur de la fleur a été retenue parmi les critères, mais pas la forme. Pour cela,
nous avons dessiné un seul iconème, symbolisant et représentant toutes les fleurs. Cet iconème unique est
combiné à la couleur de la fleur.
Valeurs multiples pour un même critère
Généralement, une espèce donnée de plante est à feuille composée soit paripennée (deux folioles termi￾nales) soit imparipennée (une ou trois folioles terminales). Plus explicitement, si l’espèce est imparipennée
tous les individus émanant de cette espèce le sont également. Il en est de même pour le cas d’espèces à
feuille composée paripennée.
Cependant, il existe des espèces qui ont à la fois des individus à feuille composée imparipennée et d’autres
à feuille composée paripennée. On dira alors que cette espèce est à feuille composée paripennée et impa￾ripennée.
C’est le cas de l’espèce neemier (Azadirachta indica A. Juss). Et lorsque nous cherchons à représenter
l’icône de l’espèce de plante, nous attribuerons deux iconèmes au neemier. On insiste bien qu’un individu
donné n’a pas les deux pennations.
151

--- page 172 ---
TABLEAU 6.7 – Cadre graphique rectangulaire subdivisé en régions spatiales pour la position des iconèmes
de Plante
De ces deux situations, nous admettons la possibilité d’avoir sur l’icône d’une espèce de plante donnée
deux valeurs de pennation en même temps, donc les deux iconèmes de pennation. Également, avoir à la
fois deux couleurs de fleur sur l’icône d’une plante est possible (dans ce cas, nous mettrons deux iconèmes
de fleur, avec une couleur différente pour chacun de ces iconèmes). Le neemier constitue un exemple de
ces deux cas.
6.3.6 Assemblage des iconèmes
Cadre graphique
Nous avons défini un cadre graphique rectangulaire devant contenir l’icône de la plante à l’issue de
l’assemblage des iconèmes. Pour y parvenir, nous avons subdivisé ce cadre en régions spatiales dont chacune
de celles numérotées pourra recevoir un iconème conçu. Le tableau 6.7 présente ce cadre. On peut également
l’appeler canevas graphique.
Dans le tableau 6.8, nous donnons un aperçu du contenu des régions spatiales du cadre graphique selon
le critère. Nous y avons également le nombre de valeurs iconèmes) par critère (entité ou entité canonique).
Nous obtenons un total de 35 (= 5+11+10+6+2+1) iconèmes réalisés pour les icônes de nos 22 plantes.
La combinaison de ces iconèmes et de ces couleurs permet de générer théoriquement 422400 icônes
différentes (5 × 11 × 10 × 6 × 2 × 8 × 1 × 8), sans tenir compte des possibilités de valeurs multiples ou
inexistante pour un critère. "inexistante" ne signifie pas manquante.
Nous donnons un exemple d’assemblage de la silhouette "arbre" et d’une forme de fruit "elliptique".
Ce qui donne (A) sur la figure 6.10. En rajoutant (additionnant) la couleur "verte" du fruit à ce résultat
(A), on obtient (B) de la même figure.
L’exemple donné par cette figure 6.10 montre l’icône du neemier (Azadirachta indica A. Juss) et les
iconèmes correspondants.
Nous avons élaboré également l’ensemble des iconèmes-valeurs prises par les sept (7) critères. Il en
résulte l’exemple de l’icône du neemier que nous donnons en figure 6.11 [16].
152

--- page 173 ---
Entité Critère Existence
d’iconème
Région de position
géographique ou spatiale
(provenant du tableau 6.7)
Couleur
Nombre de
valeurs
possibles
Silhouette oui oui 1 noire 5
Forme de la
feuille
oui oui 2 verte 11
Forme de
fruit
oui oui 3 verte 10
Disposition
de la feuille
oui oui 4 noire 6
Pennation
de la feuille
oui oui 5 noire 2
Couleur du
fruit
oui non 3 couleur variable 8
Fleur non oui 6 1
Couleur de
la fleur
oui non 6 couleur variable 8
TABLEAU 6.8 – Correspondance des critères et des régions spatiales du cadre graphique et nombres
d’iconèmes par critère
Figure 6.10 – Exemple d’assemblage d’iconèmes pour l’icône d’une plante
Figure 6.11 – Icône de la plante Azadirachta indica A. Juss
153

--- page 174 ---
Entité Critère Classes (au nombre de six(6)) Classe (Sous Classe)
Silhouette oui Silhouette
Forme de la
feuille
oui FormeDeFeuille
FormeDeFeuilleGenerique
FormeDeFeuilleSpecifiqueConnue
Forme de fruit oui FormeDeFruit
FormeDeFruitGenerique
FormeDeFruitSpecifiqueConnue
Disposition de
la feuille
oui DispositionDeFeuille
Pennation de la
feuille
oui Pennation
Couleur du fruit oui Couleur
Couleur de la
fleur
oui Couleur
TABLEAU 6.9 – Définition de six classes pour les sept critères
Cette icône de la plante a été obtenue manuellement. Nous aborderons la génération automatique des
icônes à partir de l’ontologie ontoMEDTRAD (ontoCONCEPT-Term) dans la section suivante.
6.4 Génération automatique des icônes de plantes à partir de l’ontologie
ontoMEDTRAD (ontoCONCEPT-Term)
6.4.1 Lien ontologique
Conformément à notre périmètre de travail, pour la construction de ontoICONE qui se veut progressive,
la plante constitue un concept fondamental. Nous optons en conséquence pour la partie de la MT utilisant
les plantes en vue de la satisfaction progressive des cas d’utilisation UC2 et UC3. Pour cela, nous avons
défini six classes que nous avons fait correspondre à chacun des sept critères comme le présente le tableau
6.9.
Pour la représentation graphique, nous avons créé la classe basique de ontoICONE de ontoMEDRAD
que nous appelons Forme. Toutes les classes définies en rapport avec les sept critères, sont dans la hiérarchie
de racine Forme (voir figure 6.12 ).
Nous avons ensuite établi des relations sémantiques entre la classe Plante avec les classes qui viennent
d’être créées (figure 6.13) et découlant des sept critères. Chacune des relations est subsumée par aPour￾Forme.
Au regard de la figure 6.13, nous admettons la propriété fonctionnelle ou non aux relations sémantiques
(object properties) entre la plante et les classes de critères (voir tableau 6.9). Soit C une classe et (rS)
une relation sémantique. Alors C et (rS).C sont respectivement le domaine et le range de (rS). Dire que
(rS) est fonctionnelle signifie qu’aucune instance de C ne peut se prévaloir à travers (rS) au plus qu’une
seule instance de (rS).C. Ainsi une instance de Plante à travers (aPourSilhouette) n’a au plus qu’une seule
instance de (aPourSilhouette).Plante.
154

--- page 175 ---
Figure 6.12 – Extraction de ontoMedtrad montrant la classe Plante et les classes dérivées des critères
pour la représentation iconique des espèces de plantes médicinales
Figure 6.13 – Relations sémantiques entre Plante et les classes pour la représentation iconique
155

--- page 176 ---
Object properties Domaine Range Fonctionnelle : oui/non
aPourSilhouette Plante Silhouette oui
aPourCouleurDeFruit Plante Couleur oui
aPourDispositionDeFeuille Plante DispositionDeFeuille oui
aPourFormeDeFeuille Plante FormeDeFeuille oui
aPourFormeDeFruit Plante FormeDeFruit oui
aPourPennation Plante Pennation non
aPourCouleurDeFleur Plante Couleur non
TABLEAU 6.10 – État du caractère fonctionnel des object properties ou propriétés objet entre plante
(domaine) et classe de critère (range)
data properties Domaine Range
aPourNomBotanique Plante String
aPourCodeHtml Couleur String
aPourSynonyme Plante String
aPourNomEnLangueOfficelle Plante String
aPourNomEnLangueVernaculaire Plante String
TABLEAU 6.11 – Quelques data properties relatives aux Plantes et à leur iconisation
Quelques data properties utilisées relatives à Plante (voir tableau 6.11)
6.4.2 Programme en python (attachement procédural) pour la génération des icônes
de plantes
En cinq étapes, nous donnons un aperçu de l’algorithme de création des icônes des espèces de plantes
à partir des iconèmes, nous ayant amené au programme source en python puis au programme exécutable.
C’est un algorithme admis comme un attachement procédural global.
Dans cet algorithme, nous avons utilisé une librairie appropriée : pour accéder aux connaissances sto￾ckées dans l’ontologie, nous avons utilisé OwlReady [144], un module Python pour la programmation
orientée ontologie, qui permet de charger une ontologie au format OWL/XML comme un module Python.
ALGORITHME DE CRÉATION DE L’ICÔNE D’UNE PLANTE MÉDICINALE :
– Étape 1 : Importer OWLReady, un module en python ;
– Étape 2 : Indiquer le chemin de l’ontologie (ontoMEDTRAD : ontoCONCEPT-Term) et la charger ;
– Étape 3 : Écrire la procédure de création de l’icône : creer_Icone(plante)
indiquer la propriété centrale de la plante : silhouette, puis les autres propriétés : Forme de feuille,
Disposition de la feuille, Pennation, Forme de fruit, Couleur de fruit, Couleur de la fleur ;
– Étape 4 : Écrire la fonction de combinaison : combiner_SVG (X, Y)
Elle permet de combiner ensemble deux fichiers SVG, pour en former un seul. A chacun de ses
appels, on ajoute un icônème à l’icône de plante en cours de génération. creer_Icone(plante) part
de la silhouette de la plante puis ajoute les iconèmes un à un par appel de combiner_SVG (X, Y).
– Étape 5 : Constituer l’icône de la plante et l’enregistrer.
Le code source en python de création des icônes de plantes que nous avons écrit, est donné dans la
figure 6.14.
156

--- page 177 ---
Ce programme a notamment permis la génération des icônes pour les 22 plantes de notre jeu de données.
Nous donnons les 22 icônes des plantes antipaludiques dans le tableau 6.12.
6.5 Remarque importante
Dans notre ontologie, nous nous sommes alignés sur la systématique universelle de Carl von Linné
(1707-1778), plus stable, qui donne une taxinomie (hiérarchie) du règne végétal. Dans cette systématique
(espèce → genre → famille → ordre → classe → embranchement → règne végétal), nous avons utilisé
l’espèce et le genre, quelques rares fois la famille, comme le stipule la littérature sur l’ethnobotanique,
l’ethnopharmacologie et la MT.
Les individus de Plante dans notre ontologie sont formés des espèces. Sur le terrain se trouvent en
réalité les plantes individuelles. La seule espèce neem au nom botanique ou scientifique "Azadirachta
indica A. Juss", existe en des centaines de milliers d’individus de plantes. En exemple : Le neem planté
par Modou, le grand neem juste à côté de la boutique de Koffi, le neem à l’angle de ma cour à Ndjoléfem
(Saint Louis du Sénégal).
Les descriptions faites des plantes correspondent à leur état mature. Pour les plantes fruitières, la
description faite sur la plante porte sur son état d’inflorescence où elle est prête à produire des fruits (état
de maturité). Malgré cette maturité la morphologie de la plante est influencée par le climat (pluviométrie,
type de sol, hauteur de vent, ...) , les saisons, la région d’habitat et le pays.
6.6 Iconisation de la recette et du remède
UC2 et UC3 sont les cas d’utilisation aux finalités respectives "définir le remède" et "préparer le
remède". Prodiguer un soin de santé en MT, à travers un remède, nécessite de définir la recette obligatoi￾rement inhérente à ce remède et de faire suive également le mode préparation. De manière pragmatique
préparer le remède revient à préparer la recette. Le mode de préparation consiste à un processus de
transformation des composant ingrédients de la recette devant permettre d’obtenir le remède.
6.6.1 Parties utilisées de la plante
Définir le remède consiste à spécifier les ingrédients de la recette comprise dans le remède la recette,
notamment la ressource médicinale et les parties de ces ressources utilisées. Comme nous avons opté pour
une recette à base de plante, ses composantes sont en toute évidence des parties de plante. Les parties
couramment utilisées sont : les feuilles, le fruit, la fleur, la racine, l’écorce, la sève, le tronc, la branche, la
tige, le stipe, le rameau, le brin, la brindille.
En pratique, la distinction entre tronc, branche, tige, stipe, rameau, brin, brindille, est aisée. Ce n’est
pas le cas dans la représentation iconique poursuivie ici. Pour cela nous avons décidé au regard des règles
sémiologiques, de les désigner par une seule partie "troncTige". Pour les même raisons, nous regroupons
gomme et sève en une seule entité, noté "sève".
Pour les écorces, on utilise fréquemment celles du tronc et celles des racines de la plante. Nous ferons
donc la distinction entre les deux. Au final, nous retenons neuf parties de la plante : feuille, fruit, fleur,
157

--- page 178 ---
from owlready import *
onto_path.append("D:\\athèses SIG INFO\\limics") # Répertoire contenant les ontologies OWL
OntoMedTrad = get_ontology("http://www.semanticweb.org/hp/ontologies/2015/11/OntoMedTrad.owl")
OntoMedTrad.load()
SVG_DIR = "D:\\athèses SIG INFO\\limics\\icone concu\\" # Répertoire contenant les icônes SVG
def creer_icone(plante):
fichier = SVG_DIR + "Silhouette_" + plante.aPourSilhouette.name + ".svg"
svg = svg_silhouette = open(fichier).read()
x = 0
for couleur in plante.aPourCouleurDeFleur:
fichier = SVG_DIR + "Fleur.svg"
svg_fleur = open(fichier).read()
svg_fleur = svg_fleur.replace("#ff0000", couleur.aPourCodeHtml)
position_debut = svg_fleur.find("</metadata>") + len("</metadata>")#information graphique
position_fin = svg_fleur.find("</svg>")
svg_fleur = svg_fleur[ : position_debut] + ("<g transform=’translate(%s 0)’>" % x)
+ svg_fleur[position_debut : position_fin] + "</g>" + svg_fleur[position_fin : ]
svg = combiner_svg(svg, svg_fleur)
x = x + 80
if plante.aPourFormeDeFruit:
fichier = SVG_DIR + "FormeDeFruit_" + plante.aPourFormeDeFruit.name + ".svg"
svg_forme_de_fruit = open(fichier).read()
svg_forme_de_fruit = svg_forme_de_fruit.replace("#ff0000",
plante.aPourCouleurDeFruit.aPourCodeHtml)
svg = combiner_svg(svg, svg_forme_de_fruit)
if plante.aPourFormeDeFeuille:
fichier = SVG_DIR + "FormeFeuille_" + plante.aPourFormeDeFeuille.name + ".svg"
svg_forme_de_feuille = open(fichier).read()
svg = combiner_svg(svg, svg_forme_de_feuille)
if plante.aPourDispositionDeFeuille:
fichier = (SVG_DIR + "FormeDispositionFeuille_"
+ plante.aPourDispositionDeFeuille.name + ".svg")
svg_disposition_de_feuille = open(fichier).read()
svg = combiner_svg(svg, svg_disposition_de_feuille)
y=0
for pennation in plante.aPourPennation:
fichier = SVG_DIR + "FormePennation_" + pennation.name + ".svg"
svg_pennation = open(fichier).read()
position_debut = svg_pennation.find("</metadata>") + len("</metadata>")
position_fin = svg_pennation.find("</svg>")
svg_pennation = svg_pennation[ : position_debut] + ("<g transform=’translate(%s 0)’>" % y)
+ svg_pennation[position_debut : position_fin]
+ "</g>" + svg_pennation[position_fin : ]
svg = combiner_svg(svg, svg_pennation)
y = y - 90
fichier = SVG_DIR + "Plante_" + plante.name + ".svg"
open(fichier, "w").write(svg)
def combiner_svg(svg1, svg2):
svg1 = svg1.replace("</svg>", "")#y revenir
position_metadata = svg2.find("</metadata>")
svg2 = svg2[position_metadata + len("</metadata>") : ]
return svg1 + svg2
#création des icônes pour toutes les plantes de l’ontologie OntoMedTrad
for plante1 in OntoMedTrad.Plante.instances():
creer_icone(plante1)
Figure 6.14 – Code source en python pour la création des icônes des 22 espèces de plantes médicinales
antipaludiques
158

--- page 179 ---
Plante_Adenia lobata Plante_Ananas
comosus
Plante_Azadirachta
_indica_A._Juss
Plante_Carica_
papaya_L.
Plante_Chrysophyllum
_africanum_A._DC.
Plante_Citrus_aurantif
olia_Christm._Swingle
Plante_Cochlospermu
m_tinctorium_Perr.
Plante_Cocos_nucifera
_L.
Plante_Combretum_mi
cranthum_G._Don
Plante_Cymbopogon_
citratus_DC._Stapf
Plante_Enantia_
polycarpa _DC._Engl.
Plante_Eucalyptus_ca
maldulensis_Dehnhardt
Plante_Ficus_exaspera
ta_Vahl
Plante_Hibiscus_sabd
ariffa_L.
Plante_Lannea_microc
arpa_Engl._et_K._
Plante_Manihot_escul
enta_Crantz
s
Plante_Musa_x_
paradisiaca_L.
Plante_Nephrolepis_
biserrata
Plante_Scaphopetalum_
amoenum_A._Chev.
Plante_Senna_alata
_L._Roxb.
Plante_Senna_
occidentalis_L
Plante_Vernonia_
colorata_Willd._Drake
r
TABLEAU 6.12 – Les 22 icônes des 22 espèces de plantes antipaludiques
159

--- page 180 ---
pp1 : feuille pp2 : fruit pp3 : fleur pp4 :
troncTige
pp5 : écorce de
troncTige
pp6 : écorce de
racine
pp7 : racine pp8 : sève pp9 : plante
entière
TABLEAU 6.13 – les 9 iconèmes des parties de plantes
racine, tronc, écorce de tronc, écorce de racine, sève, plante entière. En général, la plante a une
silhouette herbe quand il s’agit de l’utiliser entièrement.
Il est bon de noter qu’une partie de plante peut faire l’objet de plusieurs recettes. Une fois, la partie
de la plante (e.g : la feuille) est utilisée, elle se trouve dans un autre état. Il ne s’agit pas de cela ici. La
feuille est prise au sens terminologique et conceptuel. Une contrainte majeure est de faire en sorte que
pour une feuille donnée, l’on ne puisse pas avoir de doute sur l’espèce de la plante dont elle provient. On
doit pouvoir lier la partie de la plante à la plante de manière univoque. Relevons également que s’il existe
des plantes comprenant toutes les neuf parties, d’autres ne comprennent que seulement certaines d’entre
elles.
Nous avons dessiné un iconème associé à chacune des neuf parties de plante utilisées (tableau 6.13). Si
on doit faire usage de la feuille de deux plantes, c’est le même iconème de feuille qui paraitra en face de
chaque icône de plante. Dans ce tableau, pp1 représente l’iconème de feuille en couleur verte.
6.6.2 Recette et Ingrédient
La quintessence d’une prescription à base de plante en MT est premièrement l’identification des plantes,
et deuxièmement celle des parties à utiliser de ces plantes. En clair, une association ternaire apparait entre
Recette, Partie de plante et Plante, trois classes de ontoMEDTRAD (ontoCONCEPT-Term). Cette relation
sémantique ternaire est illustrée par (A) de la figure 6.15. Sur cette même figure en (B), étant donné que
les relations dans les ontologies sont binaires, ce cas de relation ternaire constitue une difficulté que nous
résolvons par l’introduction du concept Ingrédient. Un ingrédient est lié à la fois à une partie de plante,
une plante et une recette. Pour garantir l’univocité de l’appartenance d’une partie de la plante à la plante,
les deux relations sémantiques, d’une part de Ingrédient à Partie de plante et d’autre part de Ingrédient
à Plante, sont fonctionnelles.
Un ingrédient porte sur une seule partie utile d’une espèce de plante. Ainsi, une recette est formée d’un
ensemble d’ingrédients. Une recette possède aussi un mode de préparation (en abrégé MP) (voir figure
6.16).
En dénotant Recette, Ingrédient, Partie de plante, Plante et Mode de préparation respectivement par
R, I, PP, P et MP, nous donnons une représentation plus simplifiée mettant en relief les relations, toutes
symbolisées par des flèches. Le début de la flèche est le domaine ontologique de la relation et sa fin pointue
est le range de cette relation. La lettre f signifie que la relation est fonctionnelle. Une forme canonique
de l’ingrédient s’apparente au couple ou doublet : (PP, P). Ainsi deux ingrédients i1(pp1, p1) et i2(pp2,
pp2) sont égaux si et seulement si pp1 = pp2 et p1 = p2. Par ailleurs, la recette dans sa quintessence est
constituée d’un ensemble d’ingrédients et d’un mode de préparation.
160

--- page 181 ---
Figure 6.15 – Relation ternaire entre Recette, Plante et Partie de plante
Figure 6.16 – Modèle de recette exhaustif
Dans sa définition complète, elle est un couple formé d’un ensemble d’ingrédients que nous notons {I}
et d’un seul mode de préparation noté MP (voir figure 6.17). On a alors R = ({I}, MP). Ainsi deux recettes
sont égales si et seulement si elles ont le même ensemble d’ingrédients et le même mode de préparation.
La recette peut comprendre plusieurs parties d’une ou de plusieurs plantes. En conséquence, une recette
est à base d’au moins une plante. Sous Protégé, nous donnons un aperçu de la formalisation de la recette
en vue de son iconisation (voir figure 6.18).
Les relations sémantiques de la recette sont décrites avec ou non leur caractère fonctionnel (voir tableau
6.14).
Figure 6.17 – Représentation diagrammatique de la recette
161

--- page 182 ---
Figure 6.18 – Représentation formelle de la recette en vue de son iconisation
Object properties Domaine Range Fonctionnelle : oui/non
aPourBaseDePlante Ingredient Plante oui
aPourPartieDePlante Ingredient PartieDePlante oui
aPourIngredient Recette Ingredient non
aPourFormeDeModeDePreparation Recette FormeDeModeDePreparation oui
TABLEAU 6.14 – Relations sémantiques de la recette
Cadre graphique de la recette (R) (voir tableau 6.15)
Comme le montre le tableau 6.15, l’icône de la plante se positionne en région 1 et les iconèmes des
parties de cette plante sont horizontalement et successivement placés en région 2.
S’il y a une deuxième plante, on créera une deuxième ligne et on procédera de même pour cette
deuxième ligne. Ainsi en face de chaque icône de plante, se placeront successivement et horizontalement,
les parties de plante possibles utilisées par la recette.
Une fois la liste des plantes de la recette est arrêtée, on ajoutera en dernière ligne le mode de préparation
en région 3.
Nous projetons une recette R à base de deux plantes P1 et P2. Les parties utilisées ne sont pas
explicitées pour P1 et P2. Cependant, chacune de P1 et P2, a au moins un iconème de partie de plante
(pp) dans les cellules en sa face droite. Dans ce contexte, on obtient vraisemblablement le cadre graphique
afférent à R (voir tableau 6.16).
Les deux premiers remèdes de la liste des remèdes traditionnels (voir tableau 6.2 ) sont basés sur
la même recette. Cette recette que nous nommons mTRecipe01 est à base de deux plantes que sont
l’Azadirachta indica A. Juss et le Senna occidentalis L aux numéros de plante (N°PL.) respectifs (3) et
(21) dans chacun des tableaux 6.1 et 6.2. Elle comprend les feuilles de chacune de ces deux plantes dont
il faut faire la décoction dans le cadre du traitement du paludisme (Voir tableau 6.17).
1 2
(plante suivante) (reconduite d’iconème (s) ou autre iconème)
3
TABLEAU 6.15 – Cadre graphique pour l’iconisation de la recette
162

--- page 183 ---
pp1 :
feuille
pp2 :
fruit
pp3 :
fleur
pp4 :
troncTige
pp5 : écorce de
troncTige
pp6 : écorce
de racine
pp7 :
racine
pp8 :
sève
pp9 :
plante
entière
icône de P1 icopp1 icopp2 icopp3 icopp4 icopp5 icopp6 icopp7 icopp8 icopp9
icône de P2 icopp1 icopp2 icopp3 icopp4 icopp5 icopp6 icopp7 icopp8 icopp9
iconème de Mode de préparation
P : plante ; pp : partie de plante ; icopp : iconème de pp.
TABLEAU 6.16 – Projection du cadre graphique pour l’iconisation d’une recette (R) à base de deux
espèces de plantes P1 et P2
Plantes PU (pp1) Ingrédient Recette MP
Azadirachta indica A. Juss.( Meliaceae) fe i1
mTRecipe01 décoction
Senna occidentalis L. (sfamille Caesalpinaceae ) fe i2
PU : partie utilisée ; fe : feuille ; MP : mode de préparation.
TABLEAU 6.17 – mTRecipe01 extrait de ontoMEDTRAD (ontoCONCEPT-Term)
L’icône de cette recette mTRecipe01 de ontoMEDTRAD (ontoCONCEPT-Term) a été réalisée ma￾nuellement en figure 6.19 après assemblage des icônes de ces deux espèces de plantes (notamment la (3)
et la (21) listées dans le tableau 6.1).
Esquisse de l’icône d’une recette (exemple : figure 6.19) [17]
L’icône d’une recette est formée au moins d’une icône de plante et d’au moins d’un iconème de partie
de plante.
6.6.3 Remède
Le remède est structurellement lié à la recette. Il a un mode d’administration et une forme galénique
(présentation médicamenteuse de la plante). Il en résulte la mise en exergue de quatre classes, à savoir :
Figure 6.19 – Esquisse d’icône de mTRecipe01
163

--- page 184 ---
Figure 6.20 – Représentation diagrammatique du remède succincte
Figure 6.21 – Représentation formelle du remède en vue de son iconisation
Remède, Recette, ModeDeAdministration, FormeDeFinDePréparation (forme galénique). Les relations
sémantiques entretenues par Remède avec les autres classes sont définies dans le tableau 6.18 et formalisées
sous protégé (voire figure 6.21). Ainsi, un remède est constitué d’une seule recette R, d’un ensemble de
modes d’administration {MA} et d’une seule forme de fin de préparation (forme galénique), FFP. C’est
donc un triplet d’éléments qui caractérise le remède.
Si on note Rmd le remède, on a alors Rmd = (R, {MA}, FFP). Autrement dit un remède est basé sur
une seule recette (R), un ensemble de modes d’administration {MA} et une seule forme galénique (forme
de fin de préparation ou FFP) (cf figure 6.20). En conséquence, deux remèdes sont égaux si et seulement
s’ils ont la même recette, le même ensemble de modes d’administration et la même forme galénique.
De ce qui précède, à travers la figure 6.20, le cadre rectangulaire rouge nous montre les éléments de
base pour la définition succincte du remède.
Dans notre approche de construction progressive, l’icône de la recette précède celle du remède. Comme
l’icône ultime est celle du remède, pour l’obtenir, il suffit d’y adjoindre le ou les iconèmes correspondants
aux modes d’administration et de la forme médicamenteuse de plante (forme de fin de préparation) ou
164

--- page 185 ---
Object properties Domaine Range Fonctionnelle : oui/non
aPourBasePlante Ingrédient Plante oui
aPourPartieDePlante Ingrédient PartieDePlante oui
aPourIngredient Recette Ingrédient non
aPourModeDePreparation Recette ModeDePreparation oui
aPourRecetteDeBase Remède Recette oui
aPourFormeDeModeDeAdministration Remède FormeDeModeDeAdmnistration non
aPourFormeDeFinDePreparation Remède FormeDeFinDePreparation oui
TABLEAU 6.18 – Relations sémantiques du Remède et des classes associées.
1
2 3
TABLEAU 6.19 – Cadre graphique du remède
encore forme galénique. S’agissant du remède, il est obtenu à partir de la recette préparée. Pour améliorer
la définition du remède, nous lui rajoutons le mode d’administration.
Cadre graphique du remède (voir tableau 6.19)
Sur le cadre graphique à travers le tableau 6.19, la région spatiale 1 héberge l’icône de la recette et la
région 3, les iconèmes de modes d’administration. L’iconème de la forme galénique est en région spatiale
2.
En pratique dans l’art médical en MT, on a régulièrement un seul mode d’administration pour un
remède, même s’il est possible d’en avoir plusieurs.
Esquisse de l’icône d’un remède (exemple : figure 6.22)
Nous donnons une esquisse du remède (rmd01) basé sur la recette mTRecipe01 à travers la figure
6.22. De l’extrait portant sur la décoction de feuilles de Azadirachta indica A. Juss et de celles de Senna
occidentalis L (acacia), on obtient un remède sous forme de liquide (décocté).
6.6.4 Langage diagrammatique pour les recettes et les remèdes
En MT, comme une plante peut être utilisée pour le traitement de plusieurs pathologies, on en déduit
qu’un remède peut également traiter plus d’une maladie. Nous rappelons l’exemple du neemier (plante à
pharmacie) contre le paludisme, qui est également utilisé pour prévenir et traiter les maladies fongiques
(maladies en rapport avec des champignons, gastro-intestinal) et asthénie (faiblesse, diminution des forces,
dépression). Avant toute généralisation, le diagramme de la figure 6.23 relatif au remède et à la recette
s’inscrit dans le contexte d’une seule maladie qui est le paludisme avec lequel nous avons jusque-là travaillé.
De ce fait, l’indication de la maladies traitée n’était alors pas nécessaire.
165

--- page 186 ---
rmd01
mTRecipe01 : Décoction de feuilles de Azadirachta indica A. Juss et de feuilles de Senna occidentalis L
Forme galénique : liquide Mode(s) d’administration : boisson et bain
boisson bain
Figure 6.22 – Esquisse d’icône du remède rmd01 basé sur la recette mTRecipe01
Figure 6.23 – Diagramme pour le langage iconique des remèdes et recettes
166

--- page 187 ---
6.7 Généralisation de l’iconisation des remèdes et recettes pour l’en￾semble des maladies
Cette généralisation suppose la prise en compte de l’ensemble des ressources médicinales (Animal,
Minéral, Plante) utilisées dans les prescriptions des PMT et l’ensemble des maladies traitées par ces
derniers.
Dans le long processus de prise en charge du patient, depuis sa consultation par le PMT, jusqu’à
l’administration d’un remède à ce patient, les éléments essentiels focalisant le point de vue d’intérêt
majeur méritent d’être mis en exergue notamment : celui de traiter la maladie, de soigner le patient pour
le guérir. Suite à la détermination de la maladie sur le patient, deux cas de pratiques courantes sont utilisées
concomitamment. Nous avons le cas où l’on doit préparer le médicament traditionnel (remède) et celui
où le médicament est disponible prêt à l’emploi. Dans le cas de la disponibilité, deux autres possibilités
sont offertes dont l’une porte sur le fait que le médicament est à portée de main (vente ou pas) et l’autre
est relative au médicament se trouvant hors du site de consultation (en vente ou non) dont l’acquisition
nécessite un déplacement ou une recherche.
Nous notons également que plusieurs maladies peuvent être soignées par un seul remède. Aussi pour
une maladie donnée, on a plusieurs recettes ou remèdes pour la traiter. Comme c’est le cas du paludisme
tel que vu plus haut.
Nous avons à travers la figure 6.24, le diagramme générique du médicament traditionnel remède suite à
la détection de la maladie, incluant sa préparation ou son utilisation directe dans la vision de l’iconisation
de ce remède.Ce diagramme en clair, prend en compte le premier cas d’utilisation UC1 dont la finalité est
la détermination de la maladie à partir des signes et symptômes. Il y a une forte nuance entre signe et
symptôme. Le premier est prouvé du côté PMT ou bien plus par un test clinique de la MM et le second
du côté patient.
Dans ce contexte, et au regard de ce qui précède, la définition de la recette et celle du remède sont
respectivement R = ({ I }, MP, { Mal }) et Rmd = (R, { MA }, FFP). Mal signifie Maladie ou
encore Pathologie.
Une forme canonique fondée sur les trois cas d’utilisation UC1, UC2 et UC3 aux finalités respectives
déterminer la maladie, définir le remède et enfin préparer et administrer le remède, est donnée à travers
la figure 6.25.
En vue de couvrir l’ensemble des ressources médicinales d’origine animale et minérale, l’on doit dans la
modélisation représentative faite à travers les deux diagrammes 6.24 et 6.25, y remplacer les termes Partie
de plante (PP) et Plante (P) par respectivement partie de ressource médicinale (PRM) et ressource
médicinale (RM).
NB : En terme de cardinalité, le type de relation entre Maladie (Mal) et Recette (R) est celui entre
entre Maladie et Remède (Rmd).
6.8 Discussion
Vu la complexité des langages iconiques, pour la construction iconique, nous avons procédé par étape.
Nous nous sommes focalisés sur les plantes, ressources médicinales les plus prescrites par les PMT. Nous
167

--- page 188 ---
Figure 6.24 – Diagramme pour le langage iconique intégrant les maladies à partir des remèdes et recettes
Figure 6.25 – Forme canonique répondant aux trois cas d’utilisation pour l’iconisation des recettes et
remèdes partant des Plantes
168

--- page 189 ---
avons alors utilisé les éléments sémiologiques relatifs à un triptyque de règles pour la stratégie de représen￾tation [52]. Aussi avons-nous tenu compte de l’existant contextuel notamment l’environnement des plantes
dans lequel évolue le PMT. Et enfin nous tenons compte de l’environnement lié à l’utilisation future de
l’outil final dont disposeront les PMT. L’usage d’outils TIC (mobile, ordinateur, ...) comme moyen d’accès
à SysMEDTRAD, milite fortement en faveur de l’utilisation de telles approches. Il est démontré la supério￾rité de la communication pictographique sur la communication verbale dans le dialogue homme-ordinateur
[111] [239].
Limites et extensions possibles du langage iconique
Dans l’évolution de l’ontologie, on peut découvrir de nouvelles plantes médicinales, de nouvelles recettes
(remèdes). Du coup, nous n’avons pas l’exhaustivité des valeurs prises par l’ensemble des critères (e.g. :
formes de feuille). Autrement dit, de nouvelles valeurs de formes de feuilles peuvent être nécessaires. Le
critère silhouette est le seul pour lequel nous avons toutes les valeurs possibles (arbre, arbuste, liane, palme,
herbe). Ce critère peut être vu comme une propriété centrale ou principale dans la construction de l’icône
de la plante. S’il est possible qu’une plante ait une valeur inexistante pour un critère (couleur de fleur),
le critère silhouette lui est indispensable. C’est le cas des plantes sans fleurs. Par ailleurs, il arrive pour
certaines espèces de plantes d’avoir plus d’une valeur pour un critère. Le neemier de nom scientifique ou
botanique "Azadirachta indica A. Juss" a deux couleurs jaune et blanche pour le critère de couleur de
fleur. Le même neemier est imparipennée (pour certains individus) et paripennée (pour d’autres individus)
pour le critère pennation. Pour ces deux cas, nous avons pris deux iconèmes pour les deux valeurs au plus
pour une espèce de plante donnée. Nous ne sommes pas allés au delà de deux iconèmes quand bien même
plus de deux valeurs peuvent exister pour un critère sur une espèce de plante donnée.
Nous relevons que, pour cette espèce neemier, d’une part les deux valeurs de couleur de fleur et d’autre
part les deux valeurs de la pennation, ne sont perceptibles pareillement. Nous retenons ici comme instances
les espèces de plantes et non les représentation individuelles (e.g : neemier planté par Lamy, neemier planté
par Moussa). Un individu de neemier possède à la fois des fleurs des deux couleurs (jaune et blanc), tandis
qu’il ne peut avoir qu’une seule des deux valeurs paripennée et imparipennée de la pennation. Nos icônes
présentent les deux valeurs, mais ne font pas la distinction entre variations intra- et inter-individus (Nous
nous en tenons à l’espèce comme instance de plante : elle est notre plus faible granularité en machine en
rapport avec le concept de Plante).
Dans sa version actuelle, notre langage iconique ne couvre que les plantes. Il pourrait être étendu
aux ingrédients d’origine minérale et animale. Concernant les animaux, des distinctions de taille sur leur
morphologie apparaissent : les vers de terre, les mollusques (escargot) et un éléphant sont très distants en
terme de caractérisations similaires. Nous proposons que chaque espèce (genre espèce de la systématique
des animaux) puisse être caractérisée de manière générique avec la possibilité de les distinguer.
Dans les recettes, nous n’avons pas tenu compte des quantités de chaque ingrédient. En conséquence,
les recettes manquent d’une posologie stricte tant au plan temporel que quantitatif. En général les prises
indiquées par le PMT est matin - soir ou matin - midi - soir. Mais cela peut varier selon le degré de
gravité de la maladie (paludisme).
Pour les symptômes et les maladies, nous proposons de suivre le cadre général d’iconisation des concepts
de la MT que nous avons décrit et si possible avec l’alignement à d’autres ontologies de la MM où des
travaux de visualisation et d’iconisation pour décrire les maladies, les signes et symptômes patient existent,
notamment celui de [144].
169

--- page 190 ---
Collisions
Une « collision » correspond à la situation où deux espèces de plantes différentes se verraient attribuer
la même icône dans notre langage iconique. Ce risque est possible car nous avons travaillé sur un échantillon
de 22 plantes et nous avons vérifié l’absence de collision sur ces 22 plantes avec Weka et JRip, mais pas
au-delà. Il existe cependant beaucoup d’autres plantes (médicinales ou non).
Le risque de collision reste cependant faible car notre langage iconique permet un nombre important
d’icônes différentes (422400).
En cas de collisions, nous préconisons d’ajouter d’autres critères d’identification des plantes, tout en
conservant les mêmes règles. Voici une liste de critères possibles :
– présence d’épines ;
– épine sur partie de la plante ;
– présence de fruit souterrain ;
– typologie des fruits : simple ou composée ;
– disposition du fruit ;
– présence de pubescence ;
– pennation 2 : penne, bipennée, tripennée, quadripennée ;
– pennation 3 (nervuration) : nervation feuille simple ou foliole ;
– feuillage : persistant ou caduc ;
– surface de l’écorce : lisse, peu fissurée, cannelée ;
– détachement de l’écorce : en lanière, en plaque, en écaille 6
.
6.9 Synthèse
En partant des ressources médicinales (RM), nous donnons la forme canonique répondant aux trois
cas d’utilisation en vue de l’iconisation des recettes et remèdes.
Nous avons adopté une procédure d’iconisation par étape, et de façon incrémentale, en partant de
plantes antipaludiques. L’iconisation de la plante, la ressource la plus prescrite et dominante des ressources
médicinales de la MT, est achevée. Elle s’appuie sur un langage iconique de plante à sept critères, que
nous avons testé sur 22 espèces de plantes. L’évolution de l’ontologie et la croissance du nombre d’espèces
incluses nous amèneront certainement à intégrer progressivement de nouveaux critères sans perdre de vue
que la discrimination individuelle est une règle d’or à observer.
La plante constitue le fondement des recettes et des remèdes dont des esquisses sont données dans
ce travail. Bien entendu, les remèdes se fondent sur les recettes. Les descriptions botaniques et visuelles
par les botanistes afférentes à la même espèce de plante sont souvent des plus variées. Il n’en demeure
pas moins du discours des PMT sur la même recette traitant la même maladie. La difficulté liée à cette
variabilité descriptive a été surmontée.
Ce système iconique (ontoICONE), amorcé sur les plantes, devra servir d’outil d’assistance décisionnel
pour les PMT afin de transcender les barrières liées à la lecture, l’écriture et les multiples langues. La
validation de nos résultats se fera à deux niveaux, tous deux basés sur le cadre communautaire des PMT
6. http ://www.lesarbres.fr/ecorces2.php consulté en 2015
170

--- page 191 ---
Figure 6.26 – Forme canonique répondant aux trois cas d’utilisation pour l’iconisation des recettes et
remèdes partant des Ressources Médicinales
de l’Afrique de l’ouest. Les deux étapes de ce processus de validation des icônes sont : la première par les
PMT lettrés, et la seconde par l’ensemble réuni des PMT lettrés et non lettrés.
Nous proposons d’établir une relation entre icônes et images photos réalistes afin de pallier à l’insuf￾fisance d’instruction pour des PMT, le temps de la standardisation et de leur appropriation du langage
iconique.
Nous pouvons arrêter le bilan du nombre d’iconèmes à ce stade de notre construction du langage
iconique comme le montre le tableau 6.20.
En application de l’algorithme, les propositions peuvent connaître un nombre variable d’iconèmes. On
a un nombre stable de 44 (35 + 9) iconèmes et 48 (17 + 13 + 15 + 2) autres sont en cours de proposition
(cf tableau 6.20).
En perspective, au terme de cette composition de plante, nous devons asseoir un véritable langage
iconique à but inférentiel pour les PMT. La génération automatique des icônes de recettes et de remèdes
est une autre perspective. Cela pourrait se faire en utilisant les mêmes outils que pour les icônes de plantes.
La composition sémi-formalisée, formalisée et schématisée est une tâche ardue qui doit s’appuyer sur
un minimum de règles (similarité visuelle, association sémantique, convention arbitraire) en vue de son
intégration dans un wiki sémantique, puis permettre d’autres catégorisations et extractions de connais￾sances.
171

--- page 192 ---
Concept Nombre d’iconèmes pour le concept Description commentaire
P 35 RM comprend les plantes, les minerais, et
les animaux. On a les icônes de la classe
Plante que nous notons P (cf tableau 6.8) ;
P
I ⊂ RMI
fait
PP 9 Recette à base de plante fait
FFP 17 Forme médicamenteuse de fin de
préparation des recettes à base de plantes
(forme galénique)
proposition
MP 13 Mode de préparation de la recette à base
de plantes
proposition
MA 15 Mode d’administration du remède
(recettes) à base de plantes
proposition
Température 3 chaud comme à la prise de café, moyen ou
tiède, froid
proposition
TABLEAU 6.20 – Récapitulatif des iconèmes appartenant à l’alphabet du langage iconique
172

--- page 193 ---
Chapitre 7
Discussion, conclusion et perspective
Sommaire
7.1 Discussions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
7.2 Vers des ontologies iconiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
173

--- page 194 ---
Dans ce travail, nous avons tout d’abord identifié deux des problèmes majeurs de la médecine tradi￾tionnelle (MT) d’Afrique de l’ouest : l’absence de communication entre les praticiens (PMT), et l’absence
d’une mémoire permettant aux connaissances des praticiens de perdurer. La cause commune de ces deux
problèmes est l’illettrisme, qui concerne la majorité des PMT, associé à la multiplicité des langues locales.
Afin de rendre possible la structuration des connaissances en MT, nous avons conçu ontoMEDTRAD,
une ontologie formelle de la MT. De plus, pour permettre les échanges entre PMT de langues différentes,
ou la communication écrite avec un PMT non lettré, nous avons intégré dans cette ontologie une couche
iconique. Cette couche ne couvre actuellement qu’une partie de l’ontologie, elle permet notamment d’iden￾tifier les plantes par des icônes et ensuite de présenter les recettes et les remèdes de la MT sous forme
de diagrammes iconiques. Enfin, nous avons proposé l’architecture d’un système informatique, sysMED￾TRAD, permettant aux PMT d’échanger entre eux via Internet et de structurer leur connaissances sur un
wiki sémantique s’appuyant sur l’ontologie ontoMEDTRAD. Ce wiki sémantique (triple store virtuoso)
est simplement entamé mais non achevé.
Jusqu’à présent, nous nous sommes plus particulièrement intéressés aux trois cas d’utilisations suivants :
– UC1 : déterminer la maladie à partir de la détection des symptômes (signes, indices) à la détermi￾nation de la maladie (e.g : le paludisme) ;
– UC2 : prescrire un remède approprié émanant des ressources médicinales traditionnelles. Plus ex￾plicitement et pragmatique, pour la plupart du temps, il s’agit de recette à fournir (recette non
physique et recette physique) et son mode de préparation ;
– UC3 : préparer et administrer le remède obtenu au patient. Toujours de manière pragmatique, il
s’agit de préparer le remède à travers la recette si ce remède n’est pas prêt à l’emploi.
Les principales difficultés que nous avons rencontrées, sont décrites dans ce qui suit :
1. La MT est un domaine très tacite et tabou. De plus, on a noté de multiples langues existantes dont
4 officielles et 1127 locales en Afrique de l’ouest. Nos efforts d’élicitation, de conceptualisation et de
formalisation ont donc été particulièrement difficiles. Ces efforts ont permis de disposer de modèles
verbatim correspondants au mieux au réel perçu.
2. La MT diffère grandement de la MM. Il est donc difficile de réutiliser les ressources (ontologiques)
existantes dans la MM, ou d’adapter les méthodes qui ont été appliquées à la MM.
3. Le langage, écrit ou parlé, reste incontournable malgré ses ambiguïtés. Il est donc presque impossible
de disposer d’un système cent pour cent (100%) iconique. Nous nous sommes pour l’instant limités
à l’iconisation des plantes, des recettes et des remèdes.
4. La conception d’un langage iconique demande de dessiner un nombre important d’icônes et d’icô￾nèmes. Cela a nécessité d’apprendre à utiliser un logiciel de dessin vectoriel (InkScape).
sysMEDTRAD totalement à terme pourrait être un point de départ important pour la modernisation
de la MT tout en préservant sa spécificité vis-à-vis de la MM. Ce travail est d’une grande opportunité déjà
pour la communauté des PMT d’Afrique de l’ouest, et il le sera encore plus dès son implémentation dans
un wiki sémantique comme virtuoso. Cette seconde partie du travail est en cours. Il s’agit précisément de
l’implémentation de sysMEDTRAD. Cet outil permettrait aux acteurs de la MT de faire usage des TIC,
et principalement aux PMT de jouer pleinement leur rôle de guérisseur traditionnel tout en ayant accès à
un corpus large de connaissances, et en étant à même de contribuer à son enrichissement. Cela implique
174

--- page 195 ---
la réduction des complexes de supériorité et d’infériorité, l’acceptation mutuelle entre PMT, le réflexe à la
référence médicale (ou au référencement médical).
7.1 Discussions
7.1.1 Comparaison aux travaux de Kuicheu
Kuicheu N. C et al ont proposé IcOnto, une ontologie d’icônes pour la MT au Cameroun [138]. Les
auteurs présentent un système d’icônes proche du nôtre pour décrire des recettes de remèdes. Cependant,
ils ne proposent pas un langage iconique combinatoire aussi poussé que le nôtre pour l’identification des
plantes médicinales. L’identification des plantes semble davantage reposer sur des photos.
Les auteurs définissent également une sémantique formelle pour les icônes. Une icône est définie comme
l’intersection d’une composante physique (l’image de l’icône) et d’une composante logique (l’ensemble des
caractéristiques ou attributs associés à l’icône). En utilisant un raisonneur sur l’ontologie, il est alors
possible de faire des déductions par subsomption. Cependant, la formalisation des icônes restent limitées
et les raisonnements autre que ceux par subsomption ne sont pas possibles.
7.1.2 Comparaison aux travaux de Lamy
Lamy et al. ont proposé le langage iconique VCM (Visualisation des Connaissances Médicales). Ce
langage comprend environ 150 pictogrammes et une grammaire graphique simple qui permet par com￾position de construire plusieurs milliers d’icônes médicales pour la MM (maladies, symptômes, risques,
antécédents, traitements, surveillances, ...).
Lamy et al. ont également proposé une méthode à base d’ontologie pour formaliser la sémantique d’un
langage iconique [143] ; cette méthode a notamment été appliquée à VCM. Elle considère trois ontologies :
l’ontologie des icônes qui formalise les icônes du langage iconique et leur décomposition en primitives (pic￾togrammes, formes géométriques et couleurs), l’ontologie du domaine qui modélise les concepts représentés
et l’ontologie de correspondances qui relie les deux précédentes. Les auteurs présentent ensuite plusieurs
applications de la formalisation de la sémantique de VCM : vérification de la consistance des icônes, géné￾ration automatique de libellés ou de lexique de pictogramme, établissement de correspondances avec des
terminologies médicales.
Cependant, les applications sémantiques proposées par les auteurs ne sont guère applicables dans notre
contexte. La vérification de la consistance des icônes n’est pas une application pertinente dans le sens où
toutes les combinaisons d’iconèmes sont consistantes : par exemple la forme du fruit n’impose pas de
contrainte sur sa couleur ni sur celle des fleurs. La génération de libellés ou de lexiques textuels est peu
utile dans un contexte d’illettrisme. Enfin, il n’existe pas à proprement parler de terminologie bien établie
dans le domaine de la MT.
Par conséquent, dans ce travail, nous avons donc opté pour une approche d’ontologie visuelle plus simple,
avec une seule ontologie comprenant des concepts associés à des termes textuels (ontoCONCEPT-Term)
et des icônes (ontoICONE).
175

--- page 196 ---
7.1.3 Icônes et photos réalistes
Nous avons utilisé des icônes pour identifier les plantes médicinales de manière visuelle. Une autre
possibilité aurait été d’utiliser des photographies de plantes ou des images très réalistes. Cependant, les
photos sont problématiques lorsqu’il existe une grande variabilité intra- et inter-individus au sein d’une
espèce de plante donnée. Nous avons vu au chapitre précédent l’exemple du Neem, mais de nombreux autres
situations similaires existent. Cette variabilité est liée aux indicateurs climatiques, environnementaux,
pédologiques et agrométéorologiques. Par exemple, nous avons l’influence de la hauteur du vent, du type
de sol, du niveau hydrolique, de la pluviométrie, de la présence d’herbivores voraces, ... Chacun de ces
paramètres peut changer l’aspect de la plante, parfois de manière importante. En revanche, les critères
botaniques sur lesquels reposent notre langage iconique (forme des feuilles et des fruits, pennation, ...)
présentent une certaine constance.
7.2 Vers des ontologies iconiques
Nous avons construit une ontologie de la MT (ontoMEDTRAD) incluant une couche terminologique
(ontoCONCEPT-Term) et une couche iconique (ontoICONE). Une perspective de ce travail serait d’aller
plus loin dans l’intégration des icônes aux ontologies. Pour cela, nous proposons de compléter les deux
parties d’une ontologie formelle (la T-Box, terminologique, et la A-Box, assertionnelle) par une troisième
partie, la G-Box, comprenant les icônes et leur structure.
Dans les ontologies formelles, il existe une distinction entre "concepts définis" et "concepts simples
(ou non définis, ou encore primitifs)". Les concepts définis ont une définition formelle, à l’aide d’axiome :
par exemple le concept "Homme" peut être défini comme un "Etre humain" de sexe "Mâle". De manière
similaire, dans une ontologie iconique, nous pouvons considérer deux niveaux d’iconisation : "l’iconisation
définie" et "l’iconisation simple".
Lors d’une iconisation simple, une icône est simplement associée à un concept. Lors d’une iconisation
définie, l’icône est construite par assemblage de plusieurs iconèmes, ces iconèmes reprenant des éléments
de la définition du concept. L’icône est alors une "définition visuelle" du concept qu’elle représente.
Par exemple, nous avons défini le Neemier au nom botanique Azadirachta indica A. Juss.(Meliaceae)
comme une plante ayant une silhouette d’arbre, des fruits elliptiques verts, des fleurs blanches et jaunes,
des feuilles lancéolées disposées en opposition. L’icône que nous avons construite pour ce Neemier (figure
6.11), reprend chacun de ces éléments sous forme d’iconème. Il s’agit donc d’une iconisation définie. Au
contraire, les icônes que nous avons proposées pour les formes galéniques et les modes de préparation n’ont
pas été créées par assemblage d’iconèmes : il s’agit alors d’une iconisation simple.
La prochaine étape se focalisera sur la validation définitive et globale de ontoMEDTRAD dans sa partie
terminologique et iconique de sorte à déboucher sur l’adoption d’une véritable ontologie visuelle. Cette
étape intègre également le déploiement de ontoMEDTRAD dans un environnement de Wiki sémantique
(amorcé) pour arriver à sysMEDTRAD opérationnel.
En perspective plus proche, nous avons la définition de la G-Box devant compléter effectivement la T￾Box et la A-Box d’une ontologie formelle par une partie graphique comprenant les icônes et leur structure
(plus avancée).
La perspective suivante relève de deux aspects :
– l’alignement de l’ontologie visuelle à d’autres existantes comme celles relatives aux travaux de vi￾sualisation et d’iconisation de la MM de Lamy [144] ;
176

--- page 197 ---
– une ontologie de domaine de la MT africaine qui soit de référence (hissée à un niveau de standardi￾sation plus élevé qu’actuellement).
177

--- page 198 ---
Bibliographie
[1] M ABBASI A, A KHAN M, S MUNIR H, S MAROOF M, P ARSHAD et M AH￾MAD : Ethnobotanical appraisal and cultural values of medicinally important wild edible vege￾tables of Lesser Himalayas-Pakistan ; Journal of Ethnobiology and Ethnomedicine , PMC3853161 ,
http ://www.ethnobiomed.com/content/9/1/66 ; pp 1-13, 2013.
[2] G ABDOLBASET, N FARZANEH et M MOSADDEGH : Ethnobotany, Ethnopharmacology
and Drug Discovery ; Iranian Journal of Pharmaceutical Sciences, Spring 2006, pp 1-10, 2006.
[3] ABDULLAHI A A : Trends and challenges of traditional medicine in Africa ; ăAfr J Tradit Com￾plement Altern Med(AJTCAM). (2011) 8(S) :115-123 ; pp 4-9 , 2011.
[4] ADAM J M : Types de textes ou genres de discours, comment classer les textes qui disent de et
comment faire ? in : Langages, 35e année, no 141,2001, Les discours procéduraux, pp 10-27, doi :
10.3406/lgge.2001.872, persée, 2001.
[5] ADANSON M : Familles des plantes ; Chez VINCENT, académie des Sciences, de la Société Royale
de Londres, Censeur Royal, Imprimeur-Libraire Paris ; P 19, 1894.
[6] L ADOU, D MARIE, A TOURE, K KOMOE et J IPOU : Nephrolepis biserrata, une ptéridophyte
utilisée comme plante médicinale en Côte d’Ivoire ; Journal of Applied Biosciences 81 :7298 - 7306
ISSN 1997-5902 PP 1-9, 2014.
[7] ADU-GYAMFI S : Spiritual and indigenous healing practices among the Asante people of Ghana :
a testimonial from twenty-first century practitioners and recipients in Kumase ; in : Journal of Ba￾sic and Applied Research International ; Kwame Nkrumah University of Science and Technology
(KNUST), Ghana ; pp 1-13, 2014.
[8] AEN et RAE : African ethnobotany network ; Bulletin AJTCAM.v8i5S.5. PMCID ; PP 5-75 , 2000.
[9] R AHLUWALIA et B MECHIN : La médecine traditionnelle au Zaïre : fonctionnement et contri￾bution potentielle aux services de santé ; Centre de recherches pour le développement internatio￾nal(CRDI) ; Canada ; ISBN : 0-88936-222-X ; archiv ; 615.89 A 4F. PP 1-66 , 1979.
[10] AKE A : Abrégé de Médecine et pharmacopée africaines ; Abidjan RCI ; SIPPI-NEI-CEDA ; PP
1-150, volume 1-150. 2011.
[11] ALAN G : Thesauri, taxonomies and ontologies - an etymological note ; emeraldinsight.com/0022-
0418.htm ; vol 59 -1 ; PP. 7 - 18, 2003.
[12] C ALEXANDER P, R PATRICK L, J MARK et D ALEXANDER D : Defining sign and
symptom ; http ://ceur-ws.org/Vol-1309/paper4.pdf ; ICBO-WS 2014. DIKR 2014 - IWOOD 2014 -
OBIB 2014 - Workshops of ICBO 2014 co-located with 5th International ; PP 1-7, 2014.
[13] AMARI A : Adaptabilité des conditions d’enregistrement des médicaments génériques en RCI aux
médicaments traditionnels améliorés ; J. sci., Lab. de galénique et législation pharma Univ Cocody
(UFHB) ; PP 1-4, 2006.
178

--- page 199 ---
[14] ANDERSON C F M A : Contribution à l’étude de la pharmacopée ivoirienne : enquête ethnophar￾macologique dans le district autonome d’Abidjan (Côte d’Ivoire) ; Thèse en pharmarcie à l’Université
Cheikh Anta Diop de Dakar (UCAD), Sénégal ; PP 97-121 , 2015.
[15] ANSAY M : Les animaux médecins d’eux-mêmes ; Institut de la Vie 50, avenue Franklin Roosevelt ;
http ://horizon.documentation.ird.fr/exl-doc/pleinstextes/divers09 − 03/010030480.pdf; P P1 −
4, 2002.
[16] K APPOH, M BROU K, M LO et B LAMY J : Vers un système iconique d’aide à la décision
pour les praticiens de la médecine traditionnelle ; CARI 2016 ; PP 1-12, 2016.
[17] K APPOH, B LAMY J, M BROU K et M LO : Modelization of recipe in african traditional
medicine with visual ontology approach, iconic sketch ; Proceedings of e-Infrastructure and e-Services
for Developing Countries, LNICST, Springer, Africomm 2016 ; PP 304-312, 2016.
[18] K APPOH, M LO, M BROU K et M BABRI : Modélisation conceptuelle d’une ontologie de la
médecine traditionnelle (ontoMEDTRAD) ; CNRIA ; PP 1-5, 2015.
[19] K APPOH, M LO, M KONAN B et M BABRI : Architecture d’un système de gestion des
connaissances de la médecine traditionnelle : sysMEDTRAD ; CARI 2014 ; PP 1-12, 2014.
[20] ARBONNIER M : Arbres arbustes et lianes de zones sèche de l’Afrique de l’Ouest ; 3 ème Edition
QUAE 2009 ; ISBN MNHN 978-2-85653-626-1 ; PP 1-579, 2009.
[21] G ATEMEZING A., L P FOTSO, M TCHOTSOUA et A CARDON : Modélisation multi agent
massif d’un système d’aide à la décision en médecine traditionnelle ; pp 1-12 , 2009.
[22] G ATEMEZING A et P JUAN : An Ontology for African Traditional Medicine ; Springer ; DOI
10.1007/978-3-540-85863-839.ISSN1615 − 3871; pp329 − 337, 2009.
[23] A AYIMDJI, S KOUSSOUBE, L P FOTSO et K BALIRA O : Towards a "Deep" Ontology for
African Traditional Medicine ; Intelligent Information Management Volume 3, Issue 6 ; ISSN Online :
2160-5920 ; PP 244-251, 2011.
[24] A AYIMDJI, S KOUSSOUBE, L P FOTSO et K BALIRA O : Using METHONTOLOGY to
Build a Deep Ontology for African Traditional Medicine, First Steps ; ARIMA ; PP1-12, 2012.
[25] F BAADER et B HOLLUNDER : A Terminological Knowledge Representation System with
Complete Inference Algorithms ; First International Workshop on Processing Declarative Knowledge ;
ISBN :3-540-55033-X ; pp 67-86, 1991.
[26] F BAADER, L MCGUINNESS D, D NARDI, S PETER F P, W NUTT, D CALVANESE et
R MOLITOR : The description logic ; in handbook , Theory, implementation, and applications ;
ISBN : 0-521-78176-0 ; pp 1-138, 184-222, 226-269, 495-504, 2003.
[27] BACHIMONT B : Engagement sémantique et engagement ontolo￾gique : conception et réalisation d’ontologies en Ingénierie des connaissances ;
https ://www.utc.fr/ bachimon/dokuwiki/media/fr/ontologie − icbook.pdf; pp1 − 16, 2000.
[28] BANU I U D : Otto Neurath, ISOTYPE Picture Language and Its Reflections on Recent De￾sign ; ITICAM - International Trend and Issues in Communication and Media, At Dubai, Istanbul
University ,Turkey, pp 1-6, 2014.
[29] BARRY S : The Evaluation of Ontologies :Editorial Review vs. Democratic Ranking ; Proceedings
of InterOntology 2008 , Japan, 26-27 February 2008, pp 127-138. , 2008.
[30] BARTHELEMY S H : L’HERMENEIA, Traité de la proposition Aris￾tote ; Paris : Ladrange ; http ://www.documentacatholicaomnia.eu/03d/-
384−322,A ristoteles,L apropositionHermeneia,F R.pdfconsult2016; ; pp1 − 70, 1866.
179

--- page 200 ---
[31] BARTHES R : Eléments de sémiologie ; Persée ; vol 4, pp. 91-135, 1964.
[32] J BASQUE et B PUDELKO : La modélisation des connaissances à l’aide d’un outil informatisé à
des fins de transfert d’expertise, resencion d’écrits ; Ph.D ; Centre de recherche LICEF ; LICEF ; pp
1-27, 63-82, 2004.
[33] J BASQUE et B PUDELKO : Comodélisation de connaissances par objets typés ? : une stratégie
pour favoriser le transfert d’expertise dans les organisations ; Centre de recherche LICEF ; LICEF ;
pp 1-19, 2010.
[34] R BAUMANN, F LOEBE et H HERRE : Ontology of time in GFO. In M. Donnelly
G. Guizzardi (Eds.), Formal Ontology in Information Systems : Proceedings of the 7th International
Conference, FOIS 2012, Graz, Austria, Jul 24-27 (pp. 293-306). Amsterdam : IOS Press, 2012.
[35] BEAL A : L’ethnopharmacologie à travers l’exemple de l’iboga : la conservation des savoirs thé￾rapeutiques ethniques et leur transfert en médecine occidentale ; Université de Nantes Faculté de
pharmacie ; pp 1-26. Thèse de doctorat, 2014.
[36] S BECHHOFER et C GOBLE : thesaurus construction through knowledge representation ; Elsvier
sciences ; data and knowledge Engineering 37 pp 25-45, 2001.
[37] BEHOU G N : Propositions de méthodologies pour la valorisation de la médecine traditionnelle
fondées sur une ontologie ; Thèse de doctorat UFR-SFA de l’Université Nangui-Abrogoua ; pp 12-50,
2016.
[38] K BENE, D CAMARA, Y FOFIE N B, Y KANGA, B YAPI A, C YAPO Y, A AMBE S
et N ZIRIHI G : Etude ethnobotanique des plantes médicinales utilisées dans le Département de
Transua, District du Zanzan (Côte d’Ivoire) ; Journal of Animal
Plant Sciences, ISSN 2071-7024 , Vol.27, Issue 2 : pp 4230-4250 , 2016.
[39] T BERNERS-LEE, J HENDLER et O LASSILA : The Semantic Web , A New form of
Web content that is meaningful to computers will unleash a revolution of new possibilities ;
http ://www.citeulike.org/user/kajakbent/article/2841498 ; pp 1-4, 2001.
[40] BERY L M : Conception physique des bases de données à base ontologique : le cas des vues
matérialisées ; Thèse de doctorat de l’Ecole Nationale Supérieure de Mécanique et d’Aérotechnique
(ENSMA), LIAS ; France ; pp 12-30, 2014.
[41] BESSE H : Signes iconiques, signes linguistiques ; Persée vol 24 pp. 27-54, 1974.
[42] K BHASKAR et S SAVITA : A comparative study ontology building tools in semantic Web
applications ISSN : 2333-9721 ; journal of software Engineering and applications ; pp 1-13, 2010.
[43] BORDRON JF : Les objets en parties, esquisse d’ontologie matérielle ; Persée ; volume 25, no 103
L’objet, sens et réalité ; 103 pp. 51-65, 1991.
[44] F BOURDARIAS, J P DOZON et F OBRINGER : La médecine chinoise au Mali. Les économies
d’un patrimoine culturel ; Fondation Maison des sciences de l’homme - 190 avenue de France - 75013
Paris - France http ://www.fmsh.fr - FMSH-WP-2014-64 ; pp 1-25, 2014.
[45] R BRACHMAN et J G SCHMOLZE : An Overview of the KL-ONE , Knowledge Representation
System ; Cognitive science 9, pp 171-216, 1985.
[46] E BRANGIER et G GRONIER : Conception d’un langage iconique pour grands handicapés
moteurs aphasiques ; Laboratoire de Psychologie. Equipe Psychologie du Travail et Ergonomie. Uni￾versité de Metz ; pp 1-8, 2001.
180

--- page 201 ---
[47] J BRANK, M GROBELNIK et D MLADENIC : A survey of ontology evaluation techniques ;
Proc. of 8th Int. multi-conf. Information Society, pp 166-169., 2005.
[48] M BROU K, C BOGUI N, B GOORE T et I LOKPO : VetoMed , un système
expert à base d’icônes pour la médecine vétérinaire traditionnelle ; Afrique Science, Vol.10,
http ://www.afriquescience.info/document.php ?id=3105. ISSN 1813-548X. ; pp 39-46, 2014.
[49] CABALION P : Ethnopharmacologie sous les tropiques : l’exemple de Vanuatu ; In Waast Roland
(ed.), Moulin A.M. (ed.) Les sciences hors d’Occident au 20ème siècle ; Paris : ORSTOM, pp 211-221,
1986.
[50] CAMARA G : Conception d’un système de veille épidemiologique à base d’ontologies, Application à
la schistosomiase au Sénégal, Thèse de doctorat Université Gaston berger UGB Saint Louis Sénégal,
UFR SAT ; pp 22-94, 2013.
[51] CARILLON A : Place de la phytothérapie dans les systèmes de santé au 21 siècle ; Conférence
SIPAM -Djerba Mars 2009 ; pp 1-7, 2009.
[52] N CARLOS et Z T QINZ : A Taxonomy of Representation Strategies in Iconic Communication ;
ScienceDirect Volume 70, Issue 8, August 2012, pp 535-551, 2012.
[53] F CARMEN M S, P GOMEZ A et L FERNANDEZ M : The NeOn Methodology for Ontology
Engineering ; Springer Ontology Engineering in a Networked World ; pp 9-34, 2012.
[54] A CAROLINE et B KOFI : An Exploratory Ethnobotanical Study of the Practice of Herbal
Medicine by the Akan Peoples of Ghana ; Alternative Medicine Review , Volume 10, Number 2 ; pp
112-122, 2005.
[55] CARON S : Ancrage symbolique dans des catégorisations sensorimotrices, une simulation ; Présen￾tation du projet de thèse DIC9411, Canada ; pp 1-30, 2006.
[56] CEDEAO-ECOWAS : Les dynamiques démographiques, https ://www.oecd.org/fr/csao/publications/39803778.pdf,
2015.
[57] CHABRIER JY : Plantes médicinales et formes d’utilisation en phytothérapie ; thèse de doctorat
en pharmacie ; Université Henri Poincare - Nancy 1 ; pp1-51, 2010.
[58] CHARLET J : L’ingénierie des connaissances : développements, résultats et perspectives pour la
gestion des connaissances médicales ; thèse ; Hdr de l’Université Pierre et Marie Curie Paris ; pp 1-50,
2002.
[59] J CHIWUZIE, F UKOLI, O OKOJIE, E ISAH et I ERIATOR : Traditional medicine, Traditional
practitioners are here to stay ; USAID ; https ://www.popline.org/node/348606 ; pp 1-5, 1987.
[60] K CHOUDHARY, M SINGH et U PILLAI : Ethnobotanical Survey of Rajasthan - An Update ;
American-Eurasian Journal of Botany, ISSN 1995-8951 IDOSI ; pp 38-45, 2008.
[61] C CIEUR et A CARILLON : La plante médicinale - notion de totum - implication en phytothérapie
clinique intégrative ; Société Internationale de Médecine Endobiogénique et de Physiologie Intégrative
(SEMPI) ; https ://www.simepi.info/spip.php ?article57 ; pp 1-11, 2012.
[62] CLENET J : Le concept de représentation ; http ://dai￾mon.free.fr/mediactrices/representations.html, 2016.
[63] M COLLINS A et E LOFTUS F : A Spreading Activation Theory of Semantic Processing ;
http ://psycnet.apa.org/record/1976-03421-001 ; DOI : 10.1037//0033-295X.82.6.407 ; vol 82 ; 6 ; pp
407-428, 1975.
181

--- page 202 ---
[64] M COLLINS A et R QUILLIAN M : Retrieval time from semantic memory in Journal of Verbal
Learning and Verbal Behavior, 8 : pp. 240-247, 1969.
[65] CORAZZON R : Theory and History of Ontology ;www.ontology.co ; pp 1-12, 48-102, 2016.
[66] O CORCHO, L FERNANDEZ M et P GOMEZ A : Methodologies, tools and languages for
building ontologies. Where is their meeting point ? ; Elsevier Data
Knowledge Engineering 46 (2003) 41-64 ; http ://oa.upm.es/2637/1/JCR02.pdf ; pp 41-64, 2003.
[67] C CORREA M, F DEUS H, T VASCONCELOS A, Y HAYASHI, A AJANI J, P SRI￾KRISHNA V et S ALMEIDA J : AGUIA , autonomous graphical user interface assembly
for clinical trials semantic data services ; PMCID : PMC2987967 ; doi : 10.1186/1472-6947-10-65 ;
https ://www.ncbi.nlm.nih.gov/pmc/articles/PMC2987967/ ; pp1-13, 2010.
[68] COSSETTE C : Vers une grammaire de l’image publicitaire ; In : Communication et langages ; DOI :
10.3406/colan.1973.4035 ; Persée 19 ; www.persee.fr/doc/colan0336 − 15001973num1914035; pp.93 −
105, 1973.
[69] COTE A : Le nombre des catégories aristotéliciennes ; DOI : 10.7202/1020059ar ; ISSN 0023-9054
(imprimé) 1703-8804 (numérique) ; Erudit Université de LAVAL ; pp 1-11, 1964.
[70] CROLL P R : An Overview of IEEE Software Engineering Stan￾dards and Knowledge Products ; IEEE SESC Computer Sciences Corporation ;
http ://www.asq509.org/ht/a/GetDocumentAction/i/490 ; pp 1-46, 2000.
[71] DARKO I N : Ghanaian indigenous health practices : the use of herbs ; Ontario Institute for Studies
in Education of the University of Toronto ; pp 1-97, 2009.
[72] DASYLVA B : Contribution à l’étude de l’herboristerie traditionnelle sénégalaise : Inventaire des
plantes médicinales vendues dans les marchés de Dakar et contrôle de qualité sur 170 échantillons ;
thèse de doctorat à l’Université Cheikh Anta Diop de Dakar (UCAD) ; pp 40-44, 2001.
[73] DAUCOURT V : Genèse de la médecine ; http ://vdaucourt.free.fr/Histmed/ (consulté en 2016).
2001.
[74] R DAVE, C THOMPSON, J MUKERJI et D COLEMAN : An assessment of RDF-OWL mo￾delling ; Digital Media Systems Laboratory Bristol. HPL-2005-189 ; pp 1-24, 2005.
[75] G DECLERCK, A BANEYX, A XAVIER et J CHARLET : A quoi servent les ontologies
fondationnelles ? 23 èmes Journées francophones d’Ingénierie des Connaissances (IC 2012) ; Paris,
France ; pp 67-82, 2012.
[76] DELAPORTE G F : Guide de lecture de la métaphysique d’aristote, commen￾taire de Thomas d’Aquin 1 à 4 du tome 1 ; L’harmattan. http ://www.thomas-d￾aquin.com/documents/files/Metaphysique1.pdf; pp5 − 32, 53 − 58.1 − 481, 2012.
[77] V DENNY, S PINTO, S YORK et C TEMPICH : The DILIGENT Knowledge Processes ; Journal
of Knowledge Management , Vol. 9 Issue : 5, https ://doi.org/10.1108/13673270510622474 ; pp.85-96,
2005.
[78] D DIBONG S, E MPONDO E, A NGOYE, F KWIN M et L BETTI J : Ethnobotanique et
phytomédecine des plantes médicinales de Douala, Cameroun ; Journal of Applied Biosciences 37 :
2496 - 2507 ISSN ; pp 1997-5902 , 2011.
[79] DICK S : The Relationship between Information and Knowledge ; in Proceedings of IRIS 24, Ulvik,
Norway, August 11-14. http ://citeseerx.ist.psu.edu/viewdoc/summary ?doi=10.1.1.21.965, pp 11-14,
2001.
182

--- page 203 ---
[80] DIENG R K : Le web sémantique pour la gestion des connaissances ; Projet ACACIA. INRIA,
Sophia-Antipolis http ://www.inria.fr/acacia. pp 1-75. 2005.
[81] R DOS S J et J FLEURENTIN : L’ethnopharmacologie : une approche pluridisciplinaire ; In : Fleu￾rentin J. et al. (Ed.) Ethnopharmacologie. Sources, méthodes, objectifs, Actes du Premier colloque
européen d’ethnopharmacologie, Metz, 23-25 mars 1990. Paris, ORSTOM, Metz, Société française
d’ethnopharmacologie : 26. Colloques et séminaires. pp 26-39, 1990.
[82] V DOUGNON T, E ATTAKPA, H BANKOLE, G HOUNMANOU Y M, R DEHOU,
J AGBANKPE, M DESOUZA, K FABIYI, F GBAGUIDI et L BABA M : Etude eth￾nobotanique des plantes médicinales utilisées contre une maladie cutanée contagieuse : La
gale humaine au Sud-Bénin ; - Série Pharm. Méd. Trad. Afr., 2016. 18(1) ; http ://publica￾tion.lecames.org/index.php/pharm/article/viewFile/924/626 ; pp 16-22, 2016.
[83] P DOZON J et N SINDZINGRE : Pluralisme thérapeutique et médecine traditionnelle en Afrique
contemporaine ; La base de ressources documentaires de l’IRD ; Horizon ; 056SOCSAN, (12)p ; pp
43-52., 1996.
[84] DOZON J P : Ce que valoriser la médecine traditionnelle veut dire ; In, Politiques de santé. Source,
Politique Africaine, ISSN 0244-7827. Plan de classement, Politiques de la santé [056POLSAN] ; pp
(28)p. 9-20., 1987.
[85] H EKEOPARA C et A UGOHA : The Contributions of African Traditional Medicine to Nige￾ria’s Health Care Delivery System ; IOSR Journal Of Humanities And Social Science (IOSR-JHSS)
Volume 22, Issue 5, Ver. 4 (May 2017) ; e-ISSN : 2279-0837, p-ISSN : 2279-0845 ; pp 32-43, 2017.
[86] EMHIMED A : Comparison some of ontology editors ; Management Information Systems, Vol. 8
(2013), No. 2, ; pp. 018-024 , 2013.
[87] M ENGLER, V DENNY et S YORK : A tool for Diligent argumentation, Experiences, require￾ments and design ; Institute of applied Informatics and formal Description methode (AIFB) ; Uni￾versity of Karlsruhe. Karlsruhe, Germany ; 1st International Workshop on Semantic Technologies in
Collaborative Applications STICA ; Manchester, UK 2006 ; PP 1-6 , 2006.
[88] ESPINASSE B : Introduction aux Ontologies ; http ://www.lsis.org/espinasseb/Supports/ONTOWS/IntroOnto.pdf ;
pp 1-12, 2010.
[89] FARID N : Ontology Development ; https ://users.informatik.haw￾hamburg.de/ schmidt/it/presentations/OntoDev-naimi-06.pdf ; pp 1-24, 2006.
[90] G FAUSTO, D BISWANATH et V MALTESE : From knowledge organization to knowledge
representation ; University of Trento, Trento, Italy ; pp 1-21, 2013.
[91] FERNANDEZ L M : Overview Of Methodologies For Building Ontologies ; Proceedings of the IJ￾CAI99 Workshop on Ontologies and Problem Solving Methods Lessons Learned and Future Trends ;
http ://www.lsi.upc.es/ bejar/aia/aia-web/4-fernandez.pdf ; pp 1-13, 1999.
[92] FLEURENTIN J : L’ethnopharmacologie au service de la thérapeutique ; sources et méthodes ;
DOI : 10.4267/2042/47400 ; Société Française d’Ethnopharmacologie ; Hegel Vol. 2 no 2 - 2012, 2012.
[93] FORTINEAU V : Contribution à une modélisation ontologique des informations tout au long du
cycle de vie du produit ; Thèse de doctorat de l’Ecole Nationale Supérieure des Arts et Métiers ; pp
66-86, 2013.
[94] FRIEDER N : Data, information and knowledge : a semiotic view of phenomena of organization ;
IFIP TC8 / WG8.1 Working Conference on Organizational Semiotics ; volume 94 ; pp 1-10, 2002.
183

--- page 204 ---
[95] C FUCHS, C GIMMLER, G SIMON, L HOLTHOL et R BERG￾MANN : Cooking Cake ; University of Trier, Germany ; http ://www.wi2.uni￾trier.de/shared/publications/2009cookingcake.pdf; doi = 10.1.1.459.7457; pp1 − 10, 2009.
[96] A GALTON et M RIICHIRO : The Water Falls but the Waterfall does not Fall : New perspectives
on Objects, Processes and Events ; IOS Press Amsterdam ; Volume 4 Issue 2, April 2009 ; pp 71-107
, 2009.
[97] GALTON A : On What Goes On : The Ontology of Processes and Events ; IOS Press Amster￾dam, The Netherlands ; Proceedings of the 4e International Conference on on Formal Ontology in
Information Systems (FOIS 2006) ; ISBN :1-58603-685-8 ; pp 4-11 , 2006.
[98] GALTON A : Processes as Continuants (abstract) ; Proceedings of the Thirteenth International
Symposium on Temporal Representation and Reasoning (TIME 06) 1530-1311/06 ; Budapest IEEE ;
DOI : 10.1109/TIME.2006.23 ; p ISSN :1530-1311 ; pp 187-187, 2006.
[99] GALTON A : The Ontology of Time and Process ; Third Interdisciplinary School on Applied
Ontology (ISAO 2016), Bozen-Bolzano, June 27-July 1, 2016 ; pp 15-28, 2016.
[100] GANDON L F : Graphes RDF et leur manipulation pour la gestion de connaissances ; INRIA Sophia
Antipolis - Méditerranée , Université de Nice ; thèse Hdr ; http ://www-sop.inria.fr/dias/Theses/hdr￾gandon.pdf ; pp 33-97, 2008.
[101] GASTON B : Le nouvel esprit scientifique ; Paris , Les Presses universitaires de France ; pp 1-40,
1968.
[102] F GlANNESINI, H KANOUI, R PASERO et M VAN C : Prolog ; Inter Editions , 1985.
[103] GODFRAIND T : A propos des médecines traditionnelles en Afrique Centrale ; Revue des Questions
Scientifiques, 2010, 181 (3) ; pp 341-371 , 2010.
[104] P GOMEZ A, L MARIANO F et O CORCHO : Advanced Information and Knowledge Processing
with examples from the areas of Knowledge Management, e-Commerce and the Semantic Web in :
Ontological engineering ; Springer 2004, ISBN 978-1-85233-551-9, pp. 1-362, 2004.
[105] A GOMEZ P et F CARMEN M S : NeOn Methodology for building ontology Networks , a
scenario based methodology ; Ontology Engineering Group. Departamento de Inteligencia Artificial.
Facultad de. Informtica. Universidad Politécnica de Madrid ; DOI 10.1007/978-3-642-24794-12; http :
//oa.upm.es/5475/1/INV EMEM200964399.pdf; pp1 − 8, 2009.
[106] B N GROSOF, I HORROCKS, R VOLS et S DECKER : Description Logic Programs : Combining
Logic Programs with Description Logic ; WWW2003, May 20-24, 2003, Budapest, Hungary. ACM 1-
58113-680-3/03/0005.xxx. ; Proceeding WWW ’03 Proceedings of the 12th international conference
on World Wide Web ; ISBN :1-58113-680-3. 48-57 , 2003.
[107] GRUBER T R : A Translation Approach to Portable Ontology Specifications. Knowledge Acqui￾sition,vol 5, pp199-220, 1993.
[108] GRUNDSTEIN M : Distinguishing knowledge from information, a prerequisite for Elaborating
KM Initiative Strategy ; Proceedings of the International Conference on Knowledge Management
and Information Sharing ; ISBN 978-989-674-013-9. volume 135-140, 2009.
[109] N GUARINO, D OBERLE et S STAAB : What Is an Ontology ? In : Staab S., Studer R.
(eds) Handbook on Ontologies. International Handbooks on Information Systems. Springer, Berlin,
Heidelberg ; pISBN 978-3-540-70999-2, pp 1-17. 1-17, 2009.
[110] GUARINO N : Formal Ontology and Information Systems ; Proceedings of FOIS’98, Trento, Italy,
6-8 June 1998. Amsterdam, IOS Press, pp 3-15. 3-15, 1998.
184

--- page 205 ---
[111] J GUASTELLO S et M TRAUT : Verbal versus pictorial representation of objects human computer
interface, https ://doi.org/10.1016/0020-7373(89)90034-5, Vol. 31. pp 99-120, 1989.
[112] F GUENTHNER et P SABATIER : Sémantique formelle et représentation des connaissances ; in :
Langages, 22 ? année, no87, 1987, Sémantique et intelligence artificielle ; 87 pp. 103-122, 1987.
[113] L GUISSOU K M, E SANON, P SANKARA et S GUINKO : La mycothérapie au Burkina
Faso : état des lieux et perspectives ; ISSN 1997-5902. ; Jourrnal of Applied Biosciences 79 :68. 96.
-. 6. 908. ; http ://dx.doi.org/10.4314/jab.v79i1.14 ; vol 79 ; pp 1-13. 1-13, 2014.
[114] H HARYANI et M HAMIZ : An Ontological Model for Indigenous Knowledge of Malay Confinement
Dietary ; Journal of software, vol. 9, no. 5, may 2014 ; doi :10.4304/jsw.9.5.1302-1312 ; pp 1302-1312,
2014.
[115] HEATHER H : Taxonomies and controlled vocabularies best practices for metadata ; ISSN 1743-
6559 ; https ://doi.org/10.1057/dam.2010.29 ; Volume 6, Issue 5, pp 279-284. 1-6, 2010.
[116] HEATHER H : The Accidental Taxonomist ; Information Today Inc ; 469p ; ISBN 978-1-57387-
499-1 ; 2nd edition, pp 1-40. Information Today Inc, 2016.
[117] HEATHER H : Taxonomy Types and Definitions, https ://www.hedden￾information.com/taxonomies.htmdefinitions, 2017.
[118] HEON M : Web sémantique et modélisation ontologique (avec G-OWL) ; dition Epsilon ; ISBN
978-2-7460-8955-6 ; pp 53-78. 2014.
[119] HORRIDGE M : A Practical Guide To Building OWL Ontologies Using
Protege 4 and CO-ODE Tools ; The University Of Manchester ; http ://mowl￾power.cs.man.ac.uk/protegeowltutorial/resources/ProtegeOWLTutorialP4v13.pdf; pp1 − 100, 2011.
[120] I HORROCKS et P SCHNEIDER P F : Knowledge Representation and Reasoning on he Seman￾tic Web , OWL ; http ://www.cs.ox.ac.uk/ian.horrocks/Publications/download/2010/HoPa10a.pdf,
2016.
[121] HORROCKS I : Reasoning with Expressive Description Logics : Theory and Practice ; In : Voron￾kov A. (eds) Automated Deduction ?CADE-18. CADE 2002. Lecture Notes in Computer Science,
vol 2392. Springer, Berlin, Heidelberg ; ISBN 978-3-540-43931-8 ; pp 1-15. 1-15, 2002.
[122] HORROCKS I : Description Logic : A Formal Foundation for Ontology Languages and
Tools ; https ://www.cs.ox.ac.uk/ian.horrocks/Seminars/download/HorrocksIanpt1.pdf andhttps :
//www.cs.ox.ac.uk/ian.horrocks/Seminars/download/HorrocksIanpt2.pdf, 2003.
[123] HUFFMAN M A : Animal origins of herbal medicine ; In : Fleuren￾tin J. (ed.), Pelt J.M. (ed.), Mazars G. (ed.), Lejosne J.C. (trad.), Cabalion
Pierre (collab.) ; http ://horizon.documentation.ird.fr/exl-doc/pleinstextes/divers09 −
03/010030476.pdf; IRDEditions; pp31 − 42, 2002.
[124] O IGOLI J, G OGAJI O, A TORANYIIN T et P IGOLI N : Traditional medicinal practices
among the Igede people of Nigeria (part II). AJTCAM (Afri. J. Tradit. Compliment Altern. Med.)
2(2) ; pp 134-152, 2005.
[125] O JANSEN, M FREDERICH, M TITS, L ANGENOT, S COUSINEAU, L BESSOT, C CRU￾NET et P NICOLAS J : Ethnopharmacologie et paludisme au Burkina Faso : sélection de 13
espèces à potentialités antiplasmodiales méconnues, vol 41, Société Française d’ethnopharmacologie,
PP74-81, 2008.
185

--- page 206 ---
[126] D B JUHE et A LAINE : Processus d’acquisition et de transmission des ressources thérapeutiques
africaines dans les sources européennes du XVIIe au XIXe siècle ; In : Outre-mers, tome 92, no346-
347, 1er semestre 2005. La santé et ses pratiques en Afrique, sous la direction de Karine Delaunay.
Outre Mer, 47-78, 2005.
[127] N KAMSU B F A, B GAYO D et C C FOGUEM : Conceptual graph based knowledge representa￾tion for supporting reasoning in African traditional medicine ; Engineering Applications of Artificial
Intelligence ; Volume 26, Issue 4, April 2013, pp 1348-1365. 1348-1365, 2013.
[128] J KERHARO et G ADAM J : La pharmacopée sénégalaise traditionnelle. plantes médicinales et
toxiques ; Ed : Paris, Vigot frères, DL 1973 ; ISBN : 2-7114-0646-6 ; pp 1-200. 1974.
[129] KERHARO J : La médecine et la pharmacopée traditionnelles sénégalaises ; In : Kerharo J., Bouquet
Armand, Debray Maurice ; source : Etudes Médicales ; documentation.ird.fr/hor/fdi :21758 ; pp 7-54.
1975.
[130] KERZAZI N : Exigences et spécifications du logiciel ; Ecole Polytechnique de Montréal ; pp1-30,
2010.
[131] KESRAOUI D : Test et recette dans un projet Logiciel, Evolution des méthodes et outils ; le
CNAM, Chef de projet en ingénierie documentaire" INTD, Promotion 43, pp 1-104, 2014.
[132] K KIGEN G, K RONOH H, K KIPKORE W et K ROTICH J : Current trends of Traditional
Herbal Medicine Practice in Kenya : A review ; African Journal of Pharmacology and Therapeutics
Vol. 2 No. 1 ; pp 32-37, 2013.
[133] KONAN A : La place de la médecine traditionnelle dans les soins de santé primaires à Abidjan
(Côte d’Ivoire) ; Thèse de doctorat en médecine de l’Université de Toulouse (France) : pp 10-47,
59-69, 2012.
[134] B KOUE M T, K YAOKOKORE H B, B KASSE K et K KOUASSI P : Données ethnozoo￾logiques sur l’utilisation des oiseaux dans la médecine traditionnelle chez le peuple Gouro de la
Marahoué de Côte d’Ivoire ; https ://vertigo.hypotheses.org/author/hyaokokore, pp 1-13, 2015.
[135] E KROA, B DIABY, A NIARE, Y TRAORE, E M AHOUSSOU, A YAO G H, S COULI￾BALY G et D KOUASSI : Analyse de la collaboration entre médecines traditionnelle et moderne
dans la région du Sud Bandama (Côte d’Ivoire) ; Revue CAMES - Série Pharm. Méd. Trad. Afr.,
vol 1 : pp 21-27, 2014.
[136] KROA E : Evaluation de l’efficacité du traitement traditionnel de l’accès simple du paludisme à
Plasmodium falciparum à Agnanfoutou, Département d’Agnibilékrou ; Thèse de doctorat en méde￾cine de l’Université Félix Houphouet Boigny Abidjan ; pp 51-68, 2005.
[137] KRUK S : Semiotics of visual iconicity in Leninist ’monumental propaganda ; . Visual Communi￾cation, 7, 27-56., 2008.
[138] N C KUICHEU, N WANG, G N FANZOU T, F SIEWE et D XU : Description Logic Based Icons
Semantics : An Ontology for Icons. In Proceedings of International Conference on Signal Processing
(ICSP), volume pp 1260-1263, 2012.
[139] LAINE A : Médecins africains et français à la Côte d’Afrique. Les raisons d’une non-rencontre
(1815-1874) ; in : Outre-Mers. Revue d’histoire Année 2003 338-339 ; pp. 199-224 , 2003.
[140] J B LAMY, F SOUALMIA L, A VENOT et C DUCLOS : Validation de la sémantique d’un
langage iconique médical à l’aide d’une ontologie : méthodes et applications (OWLready) ; ic2014,
pp 1-12, 2014.
186

--- page 207 ---
[141] B LAMY J, C DUCLOS, H AVNER B, P OUVRARD et A VENOT : An iconic language for
the graphical representation of medical concepts ; BMC Med Inform Decis Mak ; PMID : 18435838
PMCID : PMC2413217 DOI : 10.1186/1472-6947-8-16 ; pp 8-16, 2008.
[142] B LAMY J, C DUCLOS, H AVNER B, P OUVRARD et A VENOT : Design of a graphical and
interactive interface for facilitating access to drug contraindications, cautions for use, interactions
and adverse effects ; BMC Med Inform Decis Makv.8 ; 2008 PMC2442832 ; doi : 10.1186/1472-6947-
8-21, 2008.
[143] B LAMY J et S LINA F : Formalization of the semantics of iconic languages : An ontology-based
method and four semantic-powered applications ; Knowledge-Based Systems, Elsevier, 2017, 135, pp
159 - 179, 2017.
[144] LAMY JB : Ontology-Oriented Programming for Biomedical Informatics. revue SHTI PubMEd,
221:64–68, 2016.
[145] LASSUEUR S A : Les propriétés des remèdes simples selon Avicenne (980-1037), analyse de
quelques passages du Canon ; Gesnerus 69/2 (2012) 207-246, 2012.
[146] LE MOIGNE J L : Qu’est-ce qu’un modèle ? Paris : MCX, Ateliers. Disponible sur
http ://www.mcxapc.org/docs/ateliers/lemoign2.pdf , 1987.
[147] LECOCQ P : Réflexions théoriques sur un moyen de communication substitutif pour IMC, le
septième Bliss ; Persée vol 4, pp. 345-365, 1985.
[148] P LEWIS, S GARY F et D FENNIG C : Ethnologue : Languages of the world ;
https ://www.ethnologue.com/, 19th edition , 2016.
[149] M LOICK et W MENVIE : Le tourisme médical, une nouvelle façon de voyager ; TéOROS, vol.
29, no 1, pp109-119, 2010.
[150] LOLKE J V D V : Maladies, remèdes et langues en Afrique centrale ; ouvrage collectif ; Gênes
(Italie). Chapitres 1 à 3, 5 et 9 (453p), 1996.
[151] LUONG P H : Gestion de l’évolution du web sémantique d’entreprise ; Thèse de doctorat de Mines
de Paris, 2007 ; pp 35-71, 2007.
[152] MAGDELEINE M : Problèmes posés par la structure d’un thésaurus : Exemple d’un système à
facettes ; Bulletin des bibliothèques de France (BBF), 1968, no 5, p. 201-210. Disponible en ligne :
http ://bbf.enssib.fr/consulter/bbf-1968-05-0201-001>. ISSN 1292-8399. , 1968.
[153] MAGDELEINE M : Principe et développement d’un thésaurus Exemple d’application : Le Thé￾saurus pétrole ; in : Bulletin des bibliothèques de France (BBF), vol 10, 1973, ., 1973.
[154] MARCUS S : Mathématique et linguistique, dans mathématique et sciences humaines, Faculté de
mathématique de l’Université de Bucarest (Roumanie), tome 103, pp 7-21, 1988.
[155] K MARIA C, F CARMEN M C S et V MARIA P : The current landscape of pitfalls in onto￾logies ; In Proceedings of the 5th International Conference on Knowledge Engineering and Ontology
Development KEOD 2013, Vilamoura, Portugal, 2013. ; 132-139, 2013.
[156] V MARIA P, F CARMEN M S et P GOMEZ A : A double classification of common pitfalls in
Ontologies ; in Proc. of Workshop on Ontology Quality (OntoQual 2010), Co-located with EKAW
2010, 2014.
[157] V MARIA P et F MARI C S : OOPS OntOlogy Pitfalls Scanner ;
http ://dx.doi.org/10.4018/ijswis.2014040102. Int J Semant Web Inf Syst. 2014 ; 10(2) : pp
7-34. , 2014.
187

--- page 208 ---
[158] K MARKUS, F SIMANCIK et I HORROCKS : A Description Logic Primer ; CoRR
abs/1201.4089. arxiv.org , 2013.
[159] P MCDOUGALL S J, B CURRY M et B OSCAR D : Measuring symbol and icon characteris￾tics : Norms for concreteness, complexity, meaningfulness, familiarity, and semantic distance for 239
symbols ; Behavior Research Methods, Instruments,
Computers (1999). https ://doi.org/10.3758/BF03200730, 31 : 487-519, 1999.
[160] M MENDONCA F et B ALMEIDA M : Ontoforinfoscience : A detailed metho￾dology for construction of ontologies and its application in the blood domain ; DOI :
http ://dx.doi.org/10.5016/brajis.v10i1.5426 , 2016.
[161] MICHEL P : Les trois dimensions de l’espace et les quatre dimensions de l’espace-temps ; In :
Flament, D. (Ed.). Dimensions, dimensions I. Paris : Fondation Maison des Sciences de l’Homme,
1998. pp. 87-112, 2007.
[162] G MIRKO D, B FANTINI et A SHUGAAR : Western Medical Thought from Antiquity to the
Middle Ages (review) ; ISBN-13 : 978-0674007956 , ISBN-10 : 0674007956 ; Published May 3rd 2002
by Harvard University Press ; Bulletin of the History of Medicine (2000), pp 351-352, 2000.
[163] M MOENS et M STEEDMAN : Temporal ontolgy and temporal reference ; Computational Lin￾guistics ; MIT Press Cambridge, MA, USA ; Volume 14 Issue 2, pp 15-28, 1988.
[164] MOURELATOS A P D : Events, processes and states ; Volume 2, Issue 3, pp 415-434 ; DOI
https ://doi.org/10.1007/BF00149015 ; Kluwer Academic Publishers ; pISSN 0165-0157, e1573-0549.
1978.
[165] MSLS : Plan stratégique de développement des ressources humaines du secteur de la santé en Côte
d’Ivoire 2009-2013, Mnistère de la santé et de la lutte contre le sida (MSLS), 2009.
[166] NAKUMA S : Perceptions of the role traditional medical system in national development : the case
study of Ghana ; doi :10.5539/gjhs.v3n2p40 ; p-ISSN 1916-9736 e-ISSN 1916-9744, 1994.
[167] D NARDI et R J BRACHMAN : An Introduction to Description Logics , In the Description Logic
Handbook, edited by F. Baader, D. Calvanese, D.L. McGuinness, D. Nardi, P.F. Patel-Schneider,
Cambridge University Press, pp 5-44. 2002.
[168] N NATALYA F et L MCCGUINNESS D : Ontology Develop￾ment 101 : A Guide to Creating Your First Ontology, Available from
http ://protege.stanford.edu/publications/ontologydevelopment/ontology101 − noy −
mcguinness.html, 2001.
[169] NEBEL B : Reasoning and Revision in Hybrid Representation Systems. Vol. 422 of Lecture Notes
In Artificial Intelligence. Springer-Verlag. Heidelberg, Berlin, New York as LNAI reprinted 1995, PP
10-30, 34-70, 1990.
[170] K NGUESSAN, K BEUGRE, Z GUEDE N., T DASSAHOUA et A L AKE : Screening phy￾tochimique de quelques plantes médicinales ivoiriennes utilisées en pays Krobou (Agboville, Côte￾d’Ivoire) ; Sciences et Nature Vol. 6 no1 : 1 - 15 , pp 1-15, 2009.
[171] K NGUESSAN, H TRA B F et W KONE M : Etude ethnopharmacologique de plantes antipa￾ludiques utilisées en médecine traditionnelle chez les Abbey et Krobou d’Agboville (Côte d’Ivoire) ;
Ethnopharmacologia, vol 44 pp 42-50, 2009.
[172] O OMOTOSHO L, A ADEYEMO O, A AYENI O et O BABALOLA G : Practical application
of an ontology based diagnostic and therapeutic system for Yoruba traditional ; STEAMS 2014 in
Nigeria, 2014.
188

--- page 209 ---
[173] OMS/WHO : Stratégie de l’OMS pour la Médecine traditionnelle pour 2002-2005, pp 1-12, 2002.
[174] OMS/WHO : Une réglementation pharmaceutique efficace ,
http ://apps.who.int/medicinedocs/pdf/s4960f/s4960f.pdf (consulté en 2016), 2003.
[175] OMS/WHO : Stratégie de l’OMS pour la Médecine traditionnelle pour 2014-2023, pp 1-53. 2013.
[176] OOAS : Pharmacopée d’Afrique de l’ouest , Ed KS PrintKraft GH LTD, Ghana ; ISBN : 978-9988-
1-8014-0, pp 1-253, 2013.
[177] H OUMAROU, I DAHIRATOU, B MOUSSA, A BASSIROU et D PABLO P : Utilisations de
quelques espèces de Macromycètes dans la pharmacopée traditionnelle au Niger occidental (Afrique
de l’Ouest) ; J. Appl. Biosci., SSN 1997-5902, vol 57 : pp 4159-4167, 2012.
[178] PANU-MBENDELE C W M : La " membralité" : Clé de compréhension des systèmes thérapeu￾tiques africains, Thèse de doctorat de l’Université de Fribourg, en Suisse, pp 1-100, 2005.
[179] PAQUETTE G : La modélisation par objets typés - une méthode de représentation pour les
systèmes d’apprentissage et d’aide à la tâche ; Sciences et Techniques Educatives, Hermes, 3 (1), pp
9-42, 1996.
[180] PAQUETTE G : Modélisation des connaissances et des compétences ;
http ://inf6070.teluq.ca/teluqDownload.php ?file=2013/07/INF6070M1a3ModelistationConnaissances.pdf ; , pp1−
23, 2002.
[181] PARVEEN, S DHEERAJ K, K DHIRAJ et N RAINU : Ontology development tools and lan￾guages, a review ; International Journal of Enhanced Research in Management
Computer Applications , ISSN : 2319-7471, Vol. 5 Issue 6, pp 92-96, Impact Factor : 1.544, 2016.
[182] PASHTIWAN Q R : Semantic Network and Frame Knowledge Representation Formalisms in
Artificial Intelligence ; Eastern Mediterranean University, Gazima ?usa, North Cyprus ; http ://i￾rep.emu.edu.tr :8080/xmlui/handle/11129/1783 consulté en 2016 ; pp 1-44, 2015.
[183] PATTON P : Neurath, Bliss and the Language of the Pictogram ; https ://www.aiga.org/neurath￾bliss-and-the-language-of-the-pictogram ; pp 1-4, 2009.
[184] G PEIQIN, C HUAJUN et Y TONG : Ontology-Oriented Diagnos￾tic System for Traditional Chinese Medicine Based on Relation Refine￾ment ; doi : 10.1155/2013/317803 ; http ://dx.doi.org/10.1155/2013/317803 ;
https ://www.hindawi.com/journals/cmmm/2013/317803/ consulté en 2016 ; pp 1-11, 2013.
[185] S C PIBA, B F H TRA, D KONAN, B G A BITIGNON et A BAKAYOKO : Inventaire et
disponibilité des plantes médicinales dans la forêt classée de Yapo-abbé, en Côte d’Ivoire ; European
Scientific Journal August 2015 edition vol.11, No.24 ISSN : 1857 - 7881 (Print) e - ISSN 1857- 7431 ;
pp 161-181, 2015.
[186] PIDCOCK W : What are the differences between a vocabulary, a taxonomy, a the￾saurus, an ontology, and a meta-model ? in The Web Graph Database, http ://info￾grid.org/trac/wiki/Reference/PidcockArticle, 2010.
[187] G PIERRA, D HONDJACK, A YAMINE A et B LADJEL : Base de données à base ontologique :
principe et mise en oeuvre ; Journal Ingénierie des systèmes d’information (J ISI) ; hermès, VOL 10/2
- 2005 ; doi :10.3166/isi.10.2.91-115 ; pp 91-115 , 2005.
[188] PIERRA G : Context-Explication in Conceptual Ontologies : The PLIB Approach, in : Proceedings
of CE’2003, Special track on Data Integration in Engineering, Madeira, Portugal, 26-30/07/2003 ;
243-254, 2003.
189

--- page 210 ---
[189] V PIETERSE et G KOURIE D : Lists, Taxonomies, Lattices, Thesauri and Ontologies : Paving
a pathway through a terminological jungle ; Knowledge Organization . 2014, Vol. 41 Issue 3, pp
217-229., 2014.
[190] S PINTO, S STAAB, S YORK et C TAMPICH : OntoEdit Empowering SWAP : a Case Study in
Supporting DIstributed, Loosely-Controlled and evolvInG Engineering of oNTologies (DILIGENT) ;
In : Bussler C.J., Davies J., Fensel D., Studer R. (eds) The Semantic Web : Research and Applications.
ESWS 2004. Lecture Notes in Computer Science, Springer, Berlin, Heidelberg ; DOI : 10.1007/978-
3-540-25956-52, V ol3053, pp16 − 30, 2004.
[191] S PINTO H, C TEMPICH et S STAAB : DILIGENT, Towards a fine-grained methodology for
DIstributed, Loosely-controlled and evolvInG Engingeering of oNTologies ; In R. L. de Mntaras and
L. Saitta, editors, Proceedings of the 16th European Conference on Artificial Intelligence (ECAI
2004), pp 393-397 ; Valencia, Spain, August 2004. IOS Press, Amsterdam, pp 93-397, 2004.
[192] PNPMTB : Manuel d’initiation des professionnels de la santé aux systèmes d’éducation et de
transmission du savoir en Médecine Traditionnelle au Bénin, pp 4-50, 2013.
[193] POC Plant Ontology Consortium : The Plant Ontology Consortium and Plant Ontologies ;
Comp Funct Genom 2002 ; 3 : 137-142. Published online 15 March 2002 in Wiley InterScience
(www.interscience.wiley.com). 10.1002/cfg.154 ; PMC2447263 ; pp 137-142, 2002.
[194] POLANYI M : Personal Knowledge , Towards a Post-Critical Philosophy ; ISBN, 0710076916,
9780710076915, eISBN 0-203-44215-6 , Length, 428 P ; pp 1-150 , 1962.
[195] Y POLITY, G HENNERON et R PALERMITI : L’organisation des connaissances, approches
conceptuelles ; ISBN : 2-7475-8274-4 ? 272P ; pp1-71, 2005.
[196] S PRASAD et T AMIT K : Traditional Medicine : The Goldmine for Modern Drugs ; Adv Tech
Biol Med 3 :e108. doi :10.4172/2379-1764.1000e108 ; ISSN : 2379-1764 ; pp 1-2. volume 1-2, 2015.
[197] J PRATHEEBA, A CHARLES E Y et S ATUKORALE D A : Towards an expert system to Sri
Lankan indigenous medicinal plants ; Poster accepted by Student Workshop on Computer Science
2015 ; of University of Colombo School of Computing ; pp1, 2015.
[198] PROTA : Plant Resources of Tropical Africa (PROTA), World Agroforestry Centre
(ICRAF),Nairobi in Africa, Department of Plant Sciences of Wageningen University in Europe ;
https ://www.prota4u.org/database/, 2000.
[199] N RAJESWARI P V et V PRASAD T : Hybrid Systems for Knowledge Representation in Artificial
Intelligence ; (IJARAI) International Journal of Advanced Research in Artificial Intelligence, Vol. 1,
No. 8 ; pp 31-36, 2012.
[200] RAMEAU : Guide d’indexation RAMEAU, http ://rameau.bnf.fr/formation/pdf/guiderameau2017.pdf, , 2016.
[201] REINBERG O : Des Dieux et des Hommes : approches de la maladie en Afrique et en Europe ,
Académie nationale de chirurgie, vol 13(4), pp 75-84, 2014.
[202] R RIBEIRO, F BASTITA, P PARDAL J, J MAMEDE N et S PINTO H : Cooking an Ontology ;
In : Euzenat J., Domingue J. (eds) Artificial Intelligence : Methodology, Systems, and Applications.
AIMSA 2006. Lecture Notes in Computer Science, vol 4183. Springer, Berlin, Heidelberg ; ISBN
978-3-540-40930-4 ; https ://doi.org/10.1007/1186146123, 2006.
[203] M RIICHIRO, K KOUJI, S TOSHINOBU et K YOSHINOBU : Construction and Deployment
of a Plant Ontology ; EKAW 2000 : Knowledge Engineering and Knowledge Management Methods,
Models, and Tools ; Computer Science„ vol 1937 ; Springer, Berlin, Heidelberg ; pp 113-128, 2002.
190

--- page 211 ---
[204] RIICHIRO M : Part 2 Ontology development, tools and languages ; New Generation Computing
March 2004, Volume 22, Issue 1 ; https ://doi.org/10.1007/BF03037281 ; ISSN 0288-3635 ; pp 61-96,
2004.
[205] RIICHIRO M : Part 3 Advanced course of ontological engineering ; New Generation Computing
June 2004, Volume 22, Issue 2 ; Springer-Verlag ; ISSN 0288-3635 ; pp 193-220, 2004.
[206] RIICHIRO M : YAMATO : Yet Another More Advanced Top-level Ontology ; y. Proceedings of the
Sixth Australasian Ontology Workshop Adelaide (AOW2010) (pp. 1-16). Retrieved July 18, 2013 ;
from http ://www.ei.sanken.osakau.ac.jp/hozo/ontolibrary/Y AMAT O101216.pdf, pp1 − 15, 2010.
[207] I RIZWAN, M MASRAH A A, M AIDA et S NURFADHLINA M : An Analysis of Ontology
Engineering Methodologies, A Literature Review ; Research Journal of Applied Sciences, Engineering
and Technology 6(16) : 2993-3000 ; ISSN : 2040-7459 ; e-ISSN : 2040-7467 ; pp 2993-3000 ;, 2013.
[208] Roger F : Medicine before science, the business of medicine from the middle age to the enlighten￾ment (extrait) ; Cambridge University Press ; https ://doi.org/10.1017/CBO9780511614989 ; eISBN
isbn 0 521 80977 0 ; pISBN 9780511614989, 2003.
[209] ROLAND P : L’ethnobotanique : Place - Objet - Méthode - Philosophie ; in : Journal d’agriculture
traditionnelle et de botanique appliquée , 10.3406/jatba.1961.6902 ; vol 8-4-5 ; pp 102-109, 1961.
[210] RUKANGIRA E : Medicinal plants and traditional medicine in Africa : constraints and challenges,
infohouse.p2ric.org/ref/40/39776.pdf, Conserve Africa International, Nairobi, Kenya. Suitable deve￾lopment international pp 179 -184, 2001.
[211] SADOK G : La phytothérapie, http ://www.planetthalasso.com/annexes/medecinedouce/laphytotherapie.pdf, , 2008.
[212] M SAM, A KRISNADHI A, W CONG, J GALLAHGHER et P HITZLER : An Ontology
Design Pattern for cooking recipes - Classroom Created ; Proceeding WOP’14 of the 5th International
Conference on Ontology and Semantic Web Patterns - Volume 1302 ; pp 49-60 , 2014.
[213] SAMBARE Y P A : Collaboration entre médecine traditionnelle et médecine moderne au Burkina
Faso : entre discours et pratiques ; CODESRIA de Dakar - Bibliothèque ; pp 1-32, 2011.
[214] SANOGO R : Le rôle des plantes médicinales en médecine traditionnelle, Université de Bamako ;
Pharmacognosie, Faculté de Médecine de Pharmacie et d’Odonto-. Stomatologie, Université de Ba￾mako (Mali), 2006.
[215] SANOU M : Développement d’une méthode de communication entre la médecine traditionnelle et
la médecine conventionnelle dans la prise en charge de la douleur en Odontologie ; Thèse de doctorat
faculté des sciences et des techniques, Université de Nantes ; pp 57-62 ;72, 2012.
[216] N SASSI et W JAZIRI : Types de changements et leurs effets sur l’évolution de l’ontologie ; JFO
2007 ; http ://liris.cnrs.fr/gom/JFO2007/5.pdf; 1 − 19, 2007.
[217] U SATTLER, D CALVANESE et R MOLITOR : Relationships with other Formalisms ; In the
Description Logic Handbook, edited by F. Baader, D. Calvanese, D.L. McGuinness, D. Nardi, P.F.
Patel-Schneider, Cambridge University Press, 2002, pp 142-166, 2003.
[218] SOWA J F : Conceptual Structures– Information processing in mind and machine ; Addison- Wesley,
Reading, MA. ISBN 0-201-14472-7 , 1984.
[219] SOWA J F : Conceptual Graphs ; in P. Bernus et al., eds., Handbook on Architectures of Information
Systems, Springer, Berlin, pp. 287-311, 1992.
[220] SOWA J F : Conceptual Graphs For Representing Conceptual Structures ;
http ://www.jfsowa.com/pubs/cg4cs.pdf. ; Conceptual Structures in Practice, pp. 101-136,
2009., 2009.
191

--- page 212 ---
[221] SOWA J F : From existential graphs to conceptual graphs , vol 1 issue 1 in International Journal
of Conceptual Structures and Smart Applications archive, IGI Publishing Hershey, PA, USA, pp
39-72, 2013.
[222] S STAAB, M ERDMANN, A MAEDCHE et S DECKER : An extensible approach for modeling
ontologies ins RDF(S) ; In First ECDL’2000 Semantic Web Workshop, Lisbon, Portugal, 2000.
[223] B STADLHOFER, P SALHOFER et A DURLACHER : An overview of ontology engineering
methodologies in the context of public administration ; SEMAPRO 2013 : The 7th International
Conference on Advances in Semantic Processing ; IARIA, 2013. ISBN : 978-1-61208-293-6 ; pp 36-42,
2013.
[224] J STEYVERS M et B TANENBAUM J : The Large-Scale Structure of Semantic Net￾works : Statistical Analyses and a Model of Semantic Growth ; PMID : 21702767 ; DOI :
10.1207/s15516709cog29013; CognitiveScience; pp41 − 78, 2005.
[225] R STUART et N PETER : Intelligence artificielle ; Pearson Education Edition III ; ISBN-13 :
978-2744074554 ; pp 249-499, 2010.
[226] L SURYANI, H YULAN et C HUI S : Computational methods for Traditional Chinese Medicine,
A survey ; Elsevier ; Volume 88, Issue 3, pp 283-294, 2008.
[227] S SWAPNA et K RAGINI : A comparative study of inference engines ; 2010 7 th International
Conference on Information Technology ; IEEE ; DOI 10.1109/ITNG.2010.198 ; pp 53-57, 2010.
[228] C TIJUS, J BARCENILLA, B CAMBON et G MEUNIER J : The design, understanding and
usage of pictograms ; E-ISBN : 9789004253254 ; DOI : 10.1163/9789004253254003; W orkplace, pp17−
31, 2007.
[229] TROCHAIN J L : Types biologiques chez les végétaux intertropicaux (Angiospermes) ; Bulletin
de la Société Botanique de France ; 113 :sup2, 187-196, DOI : 10.1080/00378941.1966.10838486 ; P
189, 1966.
[230] TSUCHIYA S : Improving knowledge creation ability through organizational learning ; International
Symposium on the Management of Industrial et Corporate Knowledge. Compiègne, France : UTC￾IIIA, ISMICK’93 Proceedings ; pp 87-95, 1993.
[231] UNESCO : Rapport du CIB sur les systèmes de la médecine traditionnelle et leurs implications
éthiques ; http ://unesdoc.unesco.org/images/0021/002174/217457f.pdf, 2013.
[232] Universite Gaston Berger UFR SAT : Projet de Mise en place d’une infrastructure socio￾économique distribuée pour une approche de développement par la connaissance . 2012.
[233] VAILLANT P : Interaction entre modalités sémiotiques : de l’icôone à la langue ; Thèse de doctorat
de l’Université Paris XI Orsay ; pp 9-50, 135-182, 1997.
[234] VALADEAU C : De l’ethnobotanique à l’articulation du soin : une approche anthropologique du
système nosologique chez les Yanesha de Haute Amazonie péruvienne ; Thèse de Doctorat d’Anthro￾pologie
Ethnobotanique ; Université de Toulouse ; pp 8-18,58, 2010.
[235] H VAN G, T SCHREIBER A et J IELINGA B : Using explicit ontologies in KBS development ;
International Journal of Human-Computer Studies Volume 46, Issues 2-3, pp 183-292, 1997.
[236] VANMALDEREN L : Un glossaire de la sémiologie de l’image ; Persée ; In : Communication et
langages, no54, 4ème trimestre 1982. pp 10-24., 1982.
192

--- page 213 ---
[237] VATANT B : Porting library vocabularies to the Semantic Web, and back , A win-win round trip ;
76 th IFLA congress ; pp 1-11, 2010.
[238] L VIDAL, A S FALL et D GADOU : Les professionnels de santé en Afrique de l’Ouest, entre
savoirs et pratiques, Paris : L’Harmattan ; Paris : L’Harmattan ; p 328., 2005.
[239] J WHITESIDE, S JONES, P S LEVY et D WIXON : User performance with command, menu,
and iconic interfaces ; Proceeding CHI ’85 Proceedings of the SIGCHI Conference on Human Factors
in Computing Systems ; ISBN :0-89791-149-0 doi :10.1145/317456.317490 ; pp 185-191 , 1985.
[240] WHO/OMS : Conférence internationale d’Alma-Ata sur les soins de santé primaires : vingt￾cinquième anniversaire ; http ://apps.who.int/gb/archive/pdff iles/W HA56/f a5627.pdf; pp1 −
6.1 − 6, 2003.
[241] Z XIANG, C MUNGAL, A RUTTENBERG et Y HE : ontobee, a linked data server and browser
for ontology terms ; ICBO ; Buffalo ; pp 1-3, 2011.
[242] A YAMINE A, M BARON, B LADJEL et S J E SARDET : Ontologies in engineering : The
OntoDB/OntoQL platform ; springer Volume 21, Issue 2 ; https ://doi.org/10.1007/s00500-015-1633-
5 ; pp 369-389, 2017.
[243] YULIA L : Closed World Reasoning ; in Non-classical Logics and Applications Seminar, Tel Aviv
University, 2008.
[244] YUWANUCH T : Modern science and native knowledge : collaborative process that
opens new perspective for PCST (Public Communication of Science and Technology) ;
http ://www.raco.cat/index.php/quark/article/viewFile/55038/63353 ; Vol 32, pp 70-74. 2004.
[245] YUWANUCH T : Opening dialogue between tradition and science : ?science and society ? in
the traditional asian ways ; 9th International Conference on Public Communication of Science and
Technology (PCST) , Seoul, South Korea ; pp 1-7, 2006.
[246] P ZERBO, J MILLOGO R, O O G NACOULMA et P VAN D : Plantes médicinales et pratiques
médicales au Burkina Faso : cas des Sanan ; Plantes médicinales ; Bois et forêts des tropicales, 2011,
n
o307(1) ; pp 41-53, 2011.
[247] P ZERBO, J MILLOGO R, O NACOULMA O et O VANE D : Contribution à la connaissance
des plantes médicinales utilisées dans les soins infantiles en pays San, au Burkina Faso ; ISSN 1991-
8631 ; Int. J. Biol. Chem. Sci. 1(3) ; pp 262-274, 2007.
[248] T ZOHOUN et J FLENON : La médecine traditionnelle et la pharmacopée africaines peuvent￾elles constituer une alternative de soins face aux coûts prohibitifs actuels de la médecine moderne ? ;
Pharm. Méd. Trad. Afr. 1997, Vo1.9, pp 3-16, 1997.
[249] S ZULAZEZE et H HARYANI : Malaysia Indigenous Herbs Knowledge Representation ; Knowledge
Management International Conference (KMICe) 2012, Johor Bahru, Malaysia, pp 253-259, 2012.
193

--- page 214 ---
Annexe 1

--- page 215 (no text layer) ---

--- page 216 ---
Annexe 2
Diagramme de classes (Suite et fin )
