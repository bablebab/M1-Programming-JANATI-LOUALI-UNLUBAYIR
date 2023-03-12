import seaborn as sns
import sys
import numpy as np 
import pandas as pd
from scipy.spatial.distance import euclidean
from tkinter import *
import matplotlib.pyplot as plt
from collections import Counter
import requests
import zipfile
import io

url = "https://storage.googleapis.com/kaggle-data-sets/1617785/2767201/compressed/players_22.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230312%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230312T165056Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=9ea3cbff04eb5a9e57f29bcf14a79ec01e99febce2c595fc458933e7ecb73e83f8fe48f294a918a791b21469a97264a9dd77bbecf8e65506841c6c6ace944e989eb8cb2e2639603fba40e3493c33ccaf4da280fe30948aa7944a8282c75fa2cb238110fcb4d02995fab4470b8414bd6c0508dd645100573ff0021309d335ff66138b93815a6b71650e0bd03de3293df7651b5c63d0179a91e6a7363e868405d656f57018a794c0de0bf07f60260ba56e5df9f668f32a5309028edc4fd9ea73e64b33f33c9a32675e9e43e224bf500828aee04021534c0559372eebdae874c867ddfd86c72c8f30a74c4110f91ea8712c415c3819366cb1bc473ba18a7f99426b"
response = requests.get(url)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))
csv_file = zip_file.extract("players_22.csv")
df = pd.read_csv(csv_file, sep=',')
print(df.head())

data = df.iloc[:, [2,3,11,12,27,28,29,37,38,39,40,41,42]]
data.dropna(inplace=True)
data2 = data.loc[:,['weight_kg','height_cm','pace','shooting','passing','defending','physic','dribbling','weak_foot','skill_moves']]
df = data2.apply(pd.to_numeric)

####################

def joueur():
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
    
    print(data.loc[index_min])