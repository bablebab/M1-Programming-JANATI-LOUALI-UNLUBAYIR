import numpy as np 
import pandas as pd
from scipy.spatial.distance import euclidean
from  utils_scrap import *
import pandas as pd
from tkinter import *

caracteristiques = ['poids', 'taille', 'vitesse', 'tir', 'qualité de passe', 'niveau en défense', 'force physique', 'qualité de dribble']

# Créer une série vide pour stocker les valeurs entrées
valeurs = pd.Series(index=caracteristiques)

# Créer une fenêtre tkinter
fenetre = Tk()
fenetre.title("Entrez vos caractéristiques")

# Boucle pour créer une entry box pour chaque caractéristique
for i in range(len(caracteristiques)):
    # Créer un label pour la caractéristique
    label_caract = Label(fenetre, text=f"{caracteristiques[i]} (entre 0 et 100): ")
    label_caract.grid(row=i, column=0)
    # Créer une entry box pour la valeur de la caractéristique
    entree_caract = Entry(fenetre)
    entree_caract.grid(row=i, column=1)
    # Stocker la valeur entrée dans la série "valeurs"
    valeurs[caracteristiques[i]] = entree_caract

# Fonction appelée lors du clic sur le bouton "Valider"
def valider():
    # Récupérer les valeurs entrées dans les entry boxes et les stocker dans la série "valeurs"
    for caract in caracteristiques:
        valeur = int(valeurs[caract].get())
        valeurs[caract] = valeur
    # Fermer la fenêtre tkinter
    fenetre.destroy()

# Créer un bouton pour valider les valeurs entrées
bouton_valider = Button(fenetre, text="Valider", command=valider)
bouton_valider.grid(row=len(caracteristiques), column=1)

# Lancer la boucle principale de la fenêtre tkinter
fenetre.mainloop()

print("Vos caractéristiques sont :")
print(valeurs)

# Série de valeurs cible
valeur_cible = valeurs

# Calculer la distance entre chaque ligne du data frame et la série de valeurs cible
distances = df.apply(lambda row: euclidean(row, valeur_cible), axis=1)

# Trouver l'indice de la ligne ayant la distance minimale
index_min = distances.idxmin()

print(data.loc[index_min])
data = pd.read_csv(r'/Users/zac/Downloads/base_finale2.csv', sep = ";")
data.head()

data2 = data.loc[:,['weight_kg','height_cm','pace','shooting','passing','defending','physic','dribbling']]
df = data2.apply(pd.to_numeric)

####################

caracteristiques = ['poids', 'taille', 'vitesse', 'tir', 'qualité de passe', 'niveau en défense', 'force physique', 'qualité de dribble']
valeurs = []

for caracteristique in caracteristiques:
    print(f"Entrez votre {caracteristique} (entre 0 et 100) : ")
    valeur = int(input())
    valeurs.append(valeur)

print("Vos caractéristiques sont :")
for i in range(len(caracteristiques)):
    print(f"{caracteristiques[i]} : {valeurs[i]}")

valeur_cible = valeurs

distances = df.apply(lambda row: euclidean(row, valeur_cible), axis=1)

index_min = distances.idxmin()

print(data.loc[index_min])


caracteristiques = ['poids', 'taille', 'vitesse', 'tir', 'qualité de passe', 'niveau en défense', 'force physique', 'qualité de dribble']

# Créer une série vide pour stocker les valeurs entrées
valeurs = pd.Series(index=caracteristiques)

# Créer une fenêtre tkinter
fenetre = Tk()
fenetre.title("Entrez vos caractéristiques")

# Boucle pour créer une entry box pour chaque caractéristique
for i in range(len(caracteristiques)):
    # Créer un label pour la caractéristique
    label_caract = Label(fenetre, text=f"{caracteristiques[i]} (entre 0 et 100): ")
    label_caract.grid(row=i, column=0)
    # Créer une entry box pour la valeur de la caractéristique
    entree_caract = Entry(fenetre)
    entree_caract.grid(row=i, column=1)
    # Stocker la valeur entrée dans la série "valeurs"
    valeurs[caracteristiques[i]] = entree_caract

# Fonction appelée lors du clic sur le bouton "Valider"
def valider():
    # Récupérer les valeurs entrées dans les entry boxes et les stocker dans la série "valeurs"
    for caract in caracteristiques:
        valeur = int(valeurs[caract].get())
        valeurs[caract] = valeur
    # Fermer la fenêtre tkinter
    fenetre.destroy()

# Créer un bouton pour valider les valeurs entrées
bouton_valider = Button(fenetre, text="Valider", command=valider)
bouton_valider.grid(row=len(caracteristiques), column=1)

# Lancer la boucle principale de la fenêtre tkinter
fenetre.mainloop()

print("Vos caractéristiques sont :")
print(valeurs)

# Série de valeurs cible
valeur_cible = valeurs

# Calculer la distance entre chaque ligne du data frame et la série de valeurs cible
distances = df.apply(lambda row: euclidean(row, valeur_cible), axis=1)

# Trouver l'indice de la ligne ayant la distance minimale
index_min = distances.idxmin()

print(data.loc[index_min])