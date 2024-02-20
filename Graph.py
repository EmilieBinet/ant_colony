from define import *
from Lieu import Lieu
from Matrice_od import Matrice_od

class Graph:

    def __init__(self, csv_lieux=None, csv_matrice=None):
        self.liste_lieux = []
        if csv_lieux == None:
            for i in range(NB_LIEUX): # create NB_LIEUX points, and their name is i as a string
                lieu = Lieu(None, None, str(i))
                self.liste_lieux.append(lieu) # add the lieu to the list of lieux
        else:
            self.charger_graph(csv_lieux)
        if csv_matrice == None:
            self.matrice_cout = Matrice_od()
            self.calcul_matrice_cout_od()
        else:
            self.charger_matrice_od(csv_matrice)

    
    def calcul_matrice_cout_od(self):
        """Create a matrix origine - destination containing the distance between each points of the complete graph"""
        for i in range(0, NB_LIEUX):
            for j in range(i, NB_LIEUX):
                lieu_i, lieu_j = self.liste_lieux[i], self.liste_lieux[j]
                dist = lieu_i.distance(lieu_j)
                self.matrice_cout.matrice[i][j] = dist
                self.matrice_cout.matrice[j][i] = dist
                
    
    def plus_proche_voisin(self, lieu, pot_voisins):
        '''
        lieu = Lieu class : (x,y,name)
        pot_voisins = Lieu class's list: [(x,y,name),(x,y,name)]
        '''
        min = float('inf')
        ligne = list(self.matrice_cout.matrice[int(lieu.name)]) # list containing the distance between actual edge and all the other edges (including with itself)
        to_del = []
        for i in range(NB_LIEUX):
            if not any(voisin.name == str(i) for voisin in pot_voisins): # if no neighbor has the same id
                to_del.append(ligne[i]) # save the element tht need to be remove
        for elem in to_del:
            ligne.remove(elem) # Remove each element
        for i in range(len(ligne)):
            if ligne[i] < min:
                #Keep and compare the minimum 
                min = ligne[i]
                knn = i
        return pot_voisins[knn]#Return the closest neighbor that hasn't been visited
    
    def calcul_distance_route(self, dist_total, lieuA, lieuB):
        """"Search for the distance between two edges inside the cost matrix"""
        dist_total += self.matrice_cout.matrice[lieuA][lieuB]
        return dist_total
    
    def charger_graph(self, csv_file):
        """Open and fetch the postions x and y of each edges in a .csv file."""
        with open(csv_file, 'r') as f:
            i=0
            graph = csv.reader(f)
            for ligne in graph:
                if i!=0:#Except the first line
                    lieu = Lieu(float(ligne[0]), float(ligne[1]), str(i-1))
                    self.liste_lieux.append(lieu)
                i+=1
    
    def charger_matrice_od(self, csv_file):
        """Open and fetch the distance of each path in a .csv file containing a matrix."""
        with open(csv_file, 'r') as f:
            i=0
            self.matrice_od = Matrice_od()
            matrice = csv.reader(f)
            for ligne in matrice:
                if i!=0:#Except the first line
                    for j in len(ligne):
                        matrice[i][j] = ligne[j]                    
                i+=1

    def __repr__(self):
            return f'Graph(\'{self.liste_lieux}\', {self.matrice_cout})'
