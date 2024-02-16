"""
Memorisation d'une liste de lieux """

import define
from define import *
import Lieu

class matrice_od:
    def __init__(self):
        self.matrice = np.matrix([np.zeros(NB_LIEUX), np.zeros(NB_LIEUX)])

class Graph:

    def __init__(self):
        self.liste_lieux = []
        for i in range(NB_LIEUX):
            Lieu(None, None,str(i))
            self.liste_lieux.append(Lieu)
        self.matrice_cout = matrice_od()
    
    def calcul_matrice_cout_od(self):
        for i in range(1, NB_LIEUX):
            for j in range(i, NB_LIEUX):
                lieu_i, lieu_j = self.list_lieux[i], self.list_lieux[j]
                dist = lieu_i.distance(lieu_j)
                self.matrice_cout[i][j] = dist
                self.matrice_cout[j][i] = dist
                
    
    def plus_proche_voisin(self, lieu, voisin):
        ligne = self.matrice_od[lieu, voisin]
        closest_N = np.argmin(ligne)
        return closest_N
    
    def calcul_distance_route():
        return

