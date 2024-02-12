"""
Memorisation d'une liste de lieux """

import numpy 
import random
import time
import pandas
import csv
import Lieu

LARGEUR = 800
HAUTEUR = 600
NB_LIEUX = 5

 

class Graph:

    def __init__(self, file):
        if file == None:
            liste_lieux = []
            for i in range(1, NB_LIEUX):
                x = random.randint(0,LARGEUR)
                y = random.randint(0, HAUTEUR)
                Lieu(x,y,i)
                liste_lieux.append(Lieu)

        return liste_lieux
    
   
    def calcul_matrice_cout_od():

        return matrice_od
    
    def plus_proche_voisin():

        return closest_N

    def charger_graph():
        return 
    
    def charger_matrice_od():
        return
    
    def calcul_distance_route():
        return

