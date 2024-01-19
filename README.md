# LegumiStar


## Documentation technique 

### Récupération physique des données

Tout d'abord, une onde sinusoïdale est envoyée à travers un légume. A l'aide d'un oscilloscope, un signal sinusoïdal bruité par le légume est récupéré à ses bornes. Celui-ci est ensuite enregistré via une clé USB.

### Utilisation du programme soundProcessing.py

A partir du signal bruité, les 88 notes de piano, que nous avons précédemment récupérées, sont modifiées et mixées avec un certain ratio compris entre **0** et **1**. Plus ce ratio se rapproche de 1 et moins la note de piano est modifiée par le bruit produit par le légume. 
Le signal bruité est tout d'abord récupéré au format *.csv*, avant d'être transformé en fichier *.wav*. Les notes du piano sont ensuite traitées au format *mp3*.

### Utilisation des notes de piano modifiées par le légume

Afin de faire ***"chanter le légume"***, nous avons sélectionné des chansons exclusivement composées de notes de piano, au format *MIDI* (Musical Instrument Digital Interface), qui permet notamment de gérer la musique avec les notes qui la composent. Dans notre programme, nous rassemblons les notes contenues dans la musique souhaitée, et les remplaçons par celles qui ont précédemment été modifiées par le légume. Pour arriver à ce résultat et d'un point de vue technique, les notes modifiées qui composent la musique doivent tout d'abord être rassemblées dans un fichier d'extension *SF2* (SoundFont2), afin d'être par la suite gérées au format *MIDI*.Ce fichier au format *MIDI* constitue alors la nouvelle version de la chanson modifiée, celle ***chantée par le légume!***

### Utilisation d'IA

Afin de suivre le fil conducteur de notre projet, une téléréalité sur des fruits, on a voulu montrer l'aspect superficiel des star systems de téléréalité, leur objectif étant de faire de l'audimat, nous avons décidé que les légumes jugés **"jolis"** produiraient des meilleures chansons que les légumes **"moches"**. En ce sens, nous avons jugé nécessaire l'utilisation de modèles d'apprentissage. 
Le premier modèle permet dans un premier temps de reconnaître le légume "en train de chanter" à partir d'une image. Ensuite, un autre modèle permet quant à lui de déterminer si un légume est pourri, donc considéré comme moche, ou bien s'il est jugé beau, toujours à partir d'une image. 
Nos modèles ont suivi le schéma suivant : 
![Diagramme pour représenter le traavail fait sur les IA](https://github.com/Phoenesis/LegumiStar/assets/102919545/62f1f58c-b7f7-41c4-934e-63f76b76082c).
A la fin du processus décrit dans le diagramme, les modèles sont capables de nous donner une prédiction sur les photos qu'on leur envoie.

### Produit final

Toutes ces différentes parties sont liées par une interface graphique, développée à l'aide de **Tkinter**. Celle-ci permet à l'aide d'un menu déroulant de choisir la musique désirée, parmi celles disponibles. L'interface permet également de gérer et mixer la chanson sélectionnée, en fonction du légume qui "chante". Celui-ci est reconnu et détecté grâce à l'IA précédemment décrite, à l'aide de la caméra d'un smartphone. En effet, via le logiciel **IVCam**, la caméra du smartphone est simulée comme étant la webcam de l'ordinateur. Enfin, grâce au deuxième modèle d'apprentissage, si le légume chanteur est considéré comme "moche", alors le ratio utilisé pour modifier les notes de la chanson sera bas,et donc la musique dégradée.

### Diagrammes

![DiagrammeSetup](https://github.com/Phoenesis/LegumiStar/assets/23200652/a46254ee-77e8-4ab8-b794-7e5b1b49f4ca)


![diagrammeSonore](https://github.com/Phoenesis/LegumiStar/assets/23200652/9f509651-1da8-499e-bfe9-1571f1ab7568)

### Preuve que chaque légume possède sa propre voix!

<img width="1499" alt="image" src="https://github.com/Phoenesis/LegumiStar/assets/23200652/d468e915-1ee5-47cd-980f-0562372c376b">

Ici nous avons fait traverser une même onde sinusoïdale à une fréquence de 440 kHz dans deux légumes différents. En haut l'onde bruitée qui a traversé une pomme de terre, et en dessous celle issue d'un citron! 
C'est à l'aide de ces bruits que nous avons pu par la suite modifier les différentes notes de piano, **et ainsi faire chanter les légumes de manière unique!**

---

### SOURCES

Pour la partie IA de notre projet, nous utilisons FreshCheck, un système intelligent conçu pour identifier les fruits et légumes sur des images et fournir un score de fraîcheur. 


Le code source de notre IA **FreshCheck** est situé ici : [https://github.com/captraj/freshcheck]


https://github.com/AjayK47/image-classification-with-inceptioV3-and-Google-Palm

