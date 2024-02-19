from define import *
from Affichage import Affichage
from Lieu import Lieu
from Matrice_od import Matrice_od
from Graph import Graph
from Route import Route

class TSP_ACO():
    def __init__(self) -> None:
        graph = Graph()
        self.mat_pheromones = Matrice_od(np.ones((NB_LIEUX, NB_LIEUX)))#Problème ici  : tente de créer une matrice_od, or la classe veut en argument une matrice = None
        print(f"matrice phéromones initiale: {self.mat_pheromones.matrice}")
        # fenetre = Affichage(graph, route, HAUTEUR, LARGEUR, NB_LIEUX, self.mat_pheromones)#fonctionne pour ce test unitaire
        for i in range(NB_FOURMIS):
            route = Route(graph, self.mat_pheromones.matrice)
            print(f"route {i}: {route.ordre}")
            dist = route.dist_total
            # print(f"dist: {dist}")
            self.update_mat_pheromones(route, graph, dist)
            # print(f"matrice phéromones: {self.mat_pheromones.matrice}")
        route.glouton(graph)

    def update_mat_pheromones(self, route, graph, dist):
        """"Met à jour la matrice de phéromones en fonction de la route qui vient d'être choisie par la fourmi et de la proximité entre les deux points"""
        for i in range(NB_LIEUX):
            for j in range(i, NB_LIEUX):
                self.mat_pheromones.matrice[i][j] *= 0.1
                self.mat_pheromones.matrice[j][i] *= 0.1
        for i in range(len(route.ordre)-1):
            self.mat_pheromones.matrice[int(route.ordre[i])][int(route.ordre[i+1])] += (0.1 + (1/dist) )
            self.mat_pheromones.matrice[int(route.ordre[i+1])][int(route.ordre[i])] += (0.1 +  (1/dist) )
    


def main():
    app = TSP_ACO()

main()