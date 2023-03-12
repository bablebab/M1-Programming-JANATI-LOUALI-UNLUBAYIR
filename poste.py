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

def poste():
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