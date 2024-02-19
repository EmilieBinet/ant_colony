from define import *
from Affichage import Affichage
from Lieu import Lieu
from Matrice_od import Matrice_od
from Graph import Graph
from Route import Route

class TSP_ACO():
    def __init__(self) -> None:
        graph = Graph()
        route = Route()
        self.mat_pheromones = Matrice_od(np.ones((NB_LIEUX, NB_LIEUX)))#Problème ici  : tente de créer une matrice_od, or la classe veut en argument une matrice = None
        #mat_pheromones = mat_pheromones()
        self.mat_prob_dist= Matrice_od()
        fenetre = Affichage(graph, route, HAUTEUR, LARGEUR, NB_LIEUX, self.mat_pheromones)#fonctionne pour ce test unitaire

    def init_prob_dist(self, matrice_cout):
        # calcul de la matrice de prob dist: (1/dist)/(sum(1/autres_dist))
        for i in range(NB_LIEUX):
            sum_norm = sum(0 if elem == 0 else 1/elem for elem in matrice_cout[i])
            for j in range(i, NB_LIEUX):
                if matrice_cout[i][j] == 0:
                    self.mat_prob_dist[i][j] = 0
                    self.mat_prob_dist[j][i] = 0
                else:
                    self.mat_prob_dist[i][j] = (1/matrice_cout[i][j])/sum_norm
                    self.mat_prob_dist[j][i] = (1/matrice_cout[i][j])/sum_norm

    def update_mat_pheromone(self, route):
        """"Met à jour la matrice de phéromones en fonction de la route qui vient d'être choisie par la fourmi et de la proximité entre les deux points"""
        self.mat_pheromones -= 0.1
        for i in len(range(route.ordre))-1:
            self.mat_pheromones[int(route.ordre[i])][int(route.ordre[i+1])] += (0.1 + 0.1)
            self.mat_pheromones[int(route.ordre[i+1])][int(route.ordre[i])] += (0.1 + 0.1)
    


def main():
    app = TSP_ACO()

main()