# M1-Programming-JANATI-LOUALI-UNLUBAYIR

M1 DS2E - Dossier lié au travail de programmation dans le cadre de l'UE Techniques de programmation.
Sous la responsabilité de M. Pierre Pelletier, doctorant au Bureau d'Économie Théorique et Appliquée.

Vous trouverez ci-dessous le nom et prénom de chaque membre du groupe :

- Zachary JANATI, M1 DS2E
- Rodi UNLUBAYIR, M1 DS2E
- Salmane LOUALI, M1 DS2E

Le projet est divisé en deux parties :

- Trouver le joueur qui vous correspond le plus
- Trouver le poste qui vous correspond le plus

Le code permet une totale automatisation. En effet, on peut lancer projet_final.py de n'importe où sans posséder la moindre librairie annexe étant directement sur le repository GitHub.
Les données ont été traitées de la même façon et il n'est pas nécessaire de posséder le moindre .csv.

###################################### EN QUOI CONSISTE LE PROJET ? ###############################

Si vous avez toujours voulu savoir quel est le joueur professionnel vous ressemblant le plus et quel est le poste qui serait adéquat pour vous, vous vous trouvez au bon endroit.
Notre projet consiste en le calcul, grâce à la base de données du jeu vidéo FIFA 22, du joueur et du poste vous correspondant le plus.
On se base sur la Méthode des k plus proches voisins, nous laissons Wikipédia vous l'expliquer.

"En intelligence artificielle, plus précisément en apprentissage automatique, la méthode des k plus proches voisins est une méthode d’apprentissage supervisé. En abrégé KPPV ou k-PPV en français, ou plus fréquemment k-NN ou KNN, de l'anglais k-nearest neighbors.

Dans ce cadre, on dispose d’une base de données d'apprentissage constituée de N couples « entrée-sortie ». Pour estimer la sortie associée à une nouvelle entrée x, la méthode des k plus proches voisins consiste à prendre en compte (de façon identique) les k échantillons d'apprentissage dont l’entrée est la plus proche de la nouvelle entrée x, selon une distance à définir. Puisque cet algorithme est basé sur la distance, la normalisation peut améliorer sa précision.1,2

Par exemple, dans un problème de classification, on retiendra la classe la plus représentée parmi les k sorties associées aux k entrées les plus proches de la nouvelle entrée x."

Sur la base de ce principe, nous avons appliquer la même méthode afin de rester en lien avec la data science. Le seul problème est que nous aurions aimé faire travailler nos données dans un cadre d'apprentissage, chose sans doûte compliquée étant donné que les serveurs sont privés MAIS, pas impossible et cela ferait sans doute l'objet d'une belle ouverture sur un futur projet.

###################################### DÉROULEMENT DU PROJET ######################################

Nous avons pour se faire utiliser la base de données FIFA 22, disponible à travers un utilisateur Kaggle, en utilisant une méthode de webscrapping pour télécharger directement la database à travers le site Kaggle.
Les différents codes permettent de calculer la distance euclidienne entre les valeurs entrées et celles de chaque joueur dans la base de données, puis trouve l'indice du joueur ayant la distance minimale. 
Les informations sur ce joueur sont alors affichées à l'écran.

Pour diversifier le contenu que nous souhaitons proposer, nous avons préférés utiliser deux moyens différents : à travers des dataframes et des matrices.
Les données sont entrées par le biais d'une fenêtre tkinter pour le joueur en plus du résultat, après calcul.

Il convient de noter que ce code ne traite pas les erreurs de saisie de l'utilisateur et ne prend pas en compte les interactions possibles entre les différentes caractéristiques d'un joueur. De plus, il utilise la distance euclidienne comme métrique de similarité, ce qui peut ne pas être la meilleure mesure pour ce type de problème.

Les difficultés rencontrées ont été les suivantes :

- Trouver une base de données FIFA, régulièrement mise à jour. Cela aurait été sympa d'actualiser constamment la base de données mais cela est apparemment impossible. En effet, FIFA garde ses serveurs de données privés.
- Maîtriser tkinter, du moins du niveau de notre projet, a été très difficile et les bugs rencontrés ont été vastes. Vis à vis des matrices, cela était compliqué niveau temps d'organiser une fenêtre d'input et d'output contrairement au fichier joueur.py, où cela fonctionnait totalement.
- Ordonner le code avec les fonctions était pas forcément facile de mise en place.
- Permettre au code d'être lié à GitHub et de pouvoir lancer projet_final.py de n'importe où. Le soucis a été réglé et le code permet donc de le lancer, de manière individuelle, sans avoir ni données et ni tout autre code.
