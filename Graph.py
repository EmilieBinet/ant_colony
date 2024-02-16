"""
Memorisation d'une liste de lieux """

from define import *
from Lieu import Lieu
from Matrice_od import Matrice_od

class Graph:

    def __init__(self, csv_lieux=None, csv_matrice=None):
        self.liste_lieux = []
        if csv_lieux == None:
            for i in range(NB_LIEUX):
                lieu = Lieu(None, None, str(i))
                self.liste_lieux.append(lieu)
        else:
            self.charger_graph(csv_lieux)
        if csv_matrice == None:
            self.matrice_cout = Matrice_od(None)
        else:
            self.charger_matrice_od(csv_matrice)
    
    def calcul_matrice_cout_od(self):
        print(self.matrice_cout)
        for i in range(0, NB_LIEUX):
            for j in range(i, NB_LIEUX):
                lieu_i, lieu_j = self.liste_lieux[i], self.liste_lieux[j]
                dist = lieu_i.distance(lieu_j)
                self.matrice_cout.matrice[i][j] = dist
                self.matrice_cout.matrice[j][i] = dist
                
    
    def plus_proche_voisin(self, lieu, pot_voisins):
        '''
        lieu = classe Lieu : (x,y,name)
        pot_voisins = liste de classes Lieu : [(x,y,name),(x,y,name)]
        '''
        min = float('inf') # tres grande valeur
        ligne = list(self.matrice_cout.matrice[int(lieu.name)]) # liste avec distance entre lieu et chaque autre lieu (comprend aussi sa distance avec lui même)
        to_del = []
        for i in range(NB_LIEUX):
            if not any(voisin.name == str(i) for voisin in pot_voisins): # si aucun lieu dans la liste de potentiels voisins n'a le nom de l'indice
                to_del.append(ligne[i]) # retiens l'element a supprimer
        for elem in to_del:
            ligne.remove(elem) # supprime chaque element
        print(f'ligne: {ligne}')
        for i in range(len(ligne)):
            if ligne[i] < min:
                min = ligne[i]
                closest_N = i
        print(f'closestN: {closest_N}')
        return pot_voisins[closest_N]
    
    def calcul_distance_route(self, dist_total, lieuA, lieuB):
        print(lieuA, type(lieuA))
        print(lieuB,type(lieuB))
    
        dist_total += self.matrice_cout.matrice[int(lieuA)] [int(lieuB.name)]# va chercher la distance entre les deux lieu dans la matrice 
        return dist_total
    
    def charger_graph(self, csv_file):
        with open(csv_file, 'r') as f:
            graph = csv.reader(f)
        self.liste_lieux = graph
    
    def charger_matrice_od(self, csv_file):
        with open(csv_file, 'r') as f:
            
            matrice = csv.reader(f)
        self.matrice_cout = Matrice_od(matrice)



    def __repr__(self):
            return f'Graph(\'{self.liste_lieux}\', {self.matrice_cout})'
