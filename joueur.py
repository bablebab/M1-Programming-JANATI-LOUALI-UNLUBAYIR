import seaborn as sns
import sys

import numpy as np 
import pandas as pd
from scipy.spatial.distance import euclidean
from tkinter import *
import matplotlib.pyplot as plt
from collections import Counter


data = pd.read_csv(r'/Users/zac/Downloads/base_finale2.csv', sep = ";")
data2 = data.loc[:,['weight_kg','height_cm','pace','shooting','passing','defending','physic','dribbling','weak_foot','skill_moves']]
df = data2.apply(pd.to_numeric)

####################

def joueur():
    data = pd.read_csv(r'/Users/zac/Downloads/base_finale2.csv', sep = ";")
    data2 = data.loc[:,['weight_kg','height_cm','pace','shooting','passing','defending','physic','dribbling','weak_foot','skill_moves']]
    df = data2.apply(pd.to_numeric)

    ####################

    caracteristiques = ['Poids', 'Taille', 'Vitesse', 'Tir', 'Qualité de passe', 'Niveau en défense', 'Force physique', 'Qualité de dribble', 'Pied faible', 'Geste technique']

    # Créer une série vide pour stocker les valeurs entrées
    valeurs = pd.Series(index=caracteristiques)

    # Créer une fenêtre tkinter
    fenetre = Tk()
    fenetre.title("Entrez vos caractéristiques")

    # Créer un widget Text pour afficher le résultat final
    output_box = Text(fenetre)
    output_box.grid(row=len(caracteristiques)+1, column=0, columnspan=2)

    # Boucle pour créer une entry box pour chaque caractéristique
    for i in range(len(caracteristiques)):
        # Créer un label pour la caractéristique
        label_caract = Label(fenetre, text=f"{caracteristiques[i]}")
        label_caract.grid(row=i, column=0)
        # Si la caractéristique est une des 8 premières, créer une entry box avec une échelle de 0 à 100
        if i < 8:
            entree_caract = Entry(fenetre)
            entree_caract.grid(row=i, column=1)
            # Stocker la valeur entrée dans la série "valeurs"
            valeurs[caracteristiques[i]] = entree_caract
        # Si la caractéristique est l'une des deux dernières, créer une Scale de 1 à 5
        else:
            scale_caract = Scale(fenetre, from_=1, to=5, orient=HORIZONTAL)
            scale_caract.grid(row=i, column=1)
            # Stocker la valeur de la Scale dans la série "valeurs"
            valeurs[caracteristiques[i]] = scale_caract

    def fermer_fenetre():
        fenetre.destroy()

    # Fonction appelée lors du clic sur le bouton "Valider"
    def valider():
        # Récupérer les valeurs entrées dans les entry boxes et les stocker dans la série "valeurs"
        for caract in caracteristiques:
            valeur = int(valeurs[caract].get())
            valeurs[caract] = valeur
        # Fermer la fenêtre tkinter
        fermer_fenetre()

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
    
    print(data.loc[index_min]
        
data_mat = pd.read_csv(r'/Users/zac/Downloads/base_finale.xls', sep = ";")

data_matrice = np.array(data_mat)

matrice4 = ([[ligne[1]] for ligne in data_matrice])
matrice2 = [[ligne[5], ligne[4], ligne[10], ligne[11], ligne[12], ligne[14], ligne[15], ligne[13]] for ligne in data_matrice]
matrice3 = np.array(matrice2)
matrice1 = np.array(matrice4)
matrice21 = np.array(matrice3)

liste2 = []
questions = ['Commencez par donnez par votre poids : ',             
             'Donnez votre taille en centimètres : ',             
             'Sur une échelle de 1 à 100, estimez votre vitesse : ',             
             'Sur une échelle de 1 à 100, estimez vos qualités de buteur (puissance, précision, ...) : ', 
             'Sur une échelle de 1 à 100, estimez votre qualité de passe : ', 
             'Sur une échelle de 1 à 100, estimez votre niveau en défense : ',            
             'Sur une échelle de 1 à 100, estimez votre force physique : ',             
             'Sur une échelle de 1 à 100, estimez votre qualité de dribble : ']

for question in questions:
    reponse = input('Veuillez entrer vos caractéristiques : ' + question)
    liste2.append(int(reponse))

distances = np.sqrt(np.sum(np.square(matrice21 - liste2), axis=1))

indices_tries = np.argsort(distances)

indices_proches = indices_tries[:10]

valeurs1 = [matrice1[i][0] for i in indices_proches]

liste = [val.split(", ") for val in valeurs1]

freq = Counter([item for sublist in liste for item in sublist])

noms = list(freq.keys())

valeurs = list(freq.values())

plt.bar(noms, valeurs)

plt.show()

poste_le_plus_courant = max(liste, key = liste.count)

print("ton poste de prédilection est :",poste_le_plus_courant)




