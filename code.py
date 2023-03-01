import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean

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

# Série de valeurs cible
valeur_cible = valeurs

# Calculer la distance entre chaque ligne du data frame et la série de valeurs cible
distances = df.apply(lambda row: euclidean(row, valeur_cible), axis=1)

# Trouver l'indice de la ligne ayant la distance minimale
index_min = distances.idxmin()

print(data.loc[index_min])


import tkinter as tk # OR from tkinter import *
from tkinter import filedialog
import subprocess

# Fonction pour obtenir les valeurs saisies par l'utilisateur
def obtenir_valeurs():
    poids = int(poids_entry.get())
    taille = int(taille_entry.get())
    vitesse = int(vitesse_entry.get())
    tir = int(tir_entry.get())
    passe = int(passe_entry.get())
    defense = int(defense_entry.get())
    force = int(force_entry.get())
    dribble = int(dribble_entry.get())

    # Affichage des valeurs saisies
    print(f"Poids : {poids}")
    print(f"Taille : {taille}")
    print(f"Vitesse : {vitesse}")
    print(f"Tir : {tir}")
    print(f"Qualité de passe : {passe}")
    print(f"Niveau en défense : {defense}")
    print(f"Force physique : {force}")
    print(f"Qualité de dribble : {dribble}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Saisie des caractéristiques")

# Création des labels et des champs de saisie pour chaque caractéristique
poids_label = tk.Label(fenetre, text="Poids (entre 0 et 100) :")
poids_entry = tk.Entry(fenetre)
poids_label.pack()
poids_entry.pack()

taille_label = tk.Label(fenetre, text="Taille (entre 0 et 100) :")
taille_entry = tk.Entry(fenetre)
taille_label.pack()
taille_entry.pack()

vitesse_label = tk.Label(fenetre, text="Vitesse (entre 0 et 100) :")
vitesse_entry = tk.Entry(fenetre)
vitesse_label.pack()
vitesse_entry.pack()

tir_label = tk.Label(fenetre, text="Tir (entre 0 et 100) :")
tir_entry = tk.Entry(fenetre)
tir_label.pack()
tir_entry.pack()

passe_label = tk.Label(fenetre, text="Qualité de passe (entre 0 et 100) :")
passe_entry = tk.Entry(fenetre)
passe_label.pack()
passe_entry.pack()

defense_label = tk.Label(fenetre, text="Niveau en défense (entre 0 et 100) :")
defense_entry = tk.Entry(fenetre)
defense_label.pack()
defense_entry.pack()

force_label = tk.Label(fenetre, text="Force physique (entre 0 et 100) :")
force_entry = tk.Entry(fenetre)
force_label.pack()
force_entry.pack()

dribble_label = tk.Label(fenetre, text="Qualité de dribble (entre 0 et 100) :")
dribble_entry = tk.Entry(fenetre)
dribble_label.pack()
dribble_entry.pack()

# Bouton pour valider la saisie et obtenir les valeurs
valider_bouton = tk.Button(fenetre, text="Valider", command=obtenir_valeurs)
valider_bouton.pack()

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
