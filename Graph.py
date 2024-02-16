"""
Memorisation d'une liste de lieux """

from define import *
from Lieu import Lieu

class matrice_od:
    def __init__(self, matrice=None):
        if matrice == None:
            self.matrice = np.matrix([np.zeros(NB_LIEUX), np.zeros(NB_LIEUX)])
        else:
            self.matrice = matrice

class Graph:

    def __init__(self, csv_lieux=None, csv_matrice=None):
        self.liste_lieux = []
        if csv_lieux == None:
            for i in range(NB_LIEUX):
                lieu = Lieu(None, None,str(i))
                self.liste_lieux.append(lieu)
        else:
            self.charger_graph(csv_lieux)
        if csv_matrice == None:
            self.matrice_cout = matrice_od()
        else:
            self.charger_matrice_od(csv_matrice)
    
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
    
    def charger_graph(self, csv_file):
        with open(csv_file, 'r') as f:
            graph = csv.reader(f)
        self.liste_lieux = graph
    
    def charger_matrice_od(self, csv_file):
        with open(csv_file, 'r') as f:
            matrice = csv.reader(f)
        self.matrice_cout = matrice_od(matrice)

