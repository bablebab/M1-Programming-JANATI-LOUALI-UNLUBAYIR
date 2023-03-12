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

Nous avons pour se faire utiliser la base de données FIFA 22, disponible à travers un utilisateur Kaggle, en utilisant une méthode de webscrapping pour télécharger directement la database à travers le site Kaggle.
Les différents codes permettent de calculer la distance euclidienne entre les valeurs entrées et celles de chaque joueur dans la base de données, puis trouve l'indice du joueur ayant la distance minimale. 
Les informations sur ce joueur sont alors affichées à l'écran.

Pour diversifier le contenu que nous souhaitons proposer, nous avons préférés utiliser deux moyens différents : à travers des dataframes et des matrices.
Les données sont entrées par le biais d'une fenêtre tkinter pour le joueur en plus du résultat, après calcul.

Il convient de noter que ce code ne traite pas les erreurs de saisie de l'utilisateur et ne prend pas en compte les interactions possibles entre les différentes caractéristiques d'un joueur. De plus, il utilise la distance euclidienne comme métrique de similarité, ce qui peut ne pas être la meilleure mesure pour ce type de problème.

Le code permet une totale automatisation. En effet, on peut lancer projet_final.py de n'importe où sans posséder la moindre librairie annexe étant directement sur le repository GitHub.
Les données ont été traitées de la même façon et il n'est pas nécessaire de posséder le moindre .csv.

Les difficultés rencontrées ont été les suivantes :

- Trouver une base de données FIFA, régulièrement mise à jour. Cela aurait été sympa d'actualiser constamment la base de données mais cela est apparemment impossible. En effet, FIFA garde ses serveurs de données privés.
- Maîtriser tkinter, du moins du niveau de notre projet, a été très difficile et les bugs rencontrés ont été vastes. Vis à vis des matrices, cela était compliqué niveau temps d'organiser une fenêtre d'input et d'output contrairement au fichier joueur.py, où cela fonctionnait totalement.
- Ordonner le code avec les fonctions était pas forcément facile de mise en place.
- Permettre au code d'être lié à GitHub et de pouvoir lancer projet_final.py de n'importe où. Le soucis a été réglé et le code permet donc de le lancer, de manière individuelle, sans avoir ni données et ni tout autre code.
