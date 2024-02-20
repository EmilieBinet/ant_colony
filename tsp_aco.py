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
        route_glouton = Route()
        route_glouton.glouton(graph)
        self.fenetre = Affichage(graph, route_glouton, HAUTEUR, LARGEUR, NB_LIEUX, self.mat_pheromones)#fonctionne pour ce test unitaire
        min_dist = route_glouton.dist_total
        print(min_dist)
        for i in range(NB_FOURMIS):
            route = Route(graph, self.mat_pheromones.matrice)
            # print(f"route {i}: {route.ordre}")
            dist = route.dist_total
            if dist<min_dist:
                extra=True
                min_dist = dist
            else:
                extra=False
            # print(f"dist: {dist}")
            self.update_mat_pheromones(route, graph, dist, extra)
            print(f"matrice phéromones: {self.mat_pheromones.matrice}\n")
            self.fenetre.update_win(route=route.ordre, liste_lieux=graph.liste_lieux, matrice=self.mat_pheromones)
            self.fenetre.update_idletasks()
            self.fenetre.update()
        # route.glouton(graph)
        # print(f"dist: {dist}")

    def update_mat_pheromones(self, route, graph, dist, extra=False):
        """"Met à jour la matrice de phéromones en fonction de la route qui vient d'être choisie par la fourmi et de la proximité entre les deux points"""
        extra_phero = int(extra)*10
        if extra: 
            print(f'extra: {extra_phero}') 
        for i in range(NB_LIEUX):
            for j in range(i, NB_LIEUX):
                self.mat_pheromones.matrice[i][j] = self.mat_pheromones.matrice[i][j] * 0.999
                self.mat_pheromones.matrice[j][i] = self.mat_pheromones.matrice[j][i] * 0.999
        for i in range(len(route.ordre)-1):
            self.mat_pheromones.matrice[int(route.ordre[i])][int(route.ordre[i+1])] = (self.mat_pheromones.matrice[int(route.ordre[i])][int(route.ordre[i+1])] / 0.999 + (1/dist) + extra_phero )
            self.mat_pheromones.matrice[int(route.ordre[i+1])][int(route.ordre[i])] = (self.mat_pheromones.matrice[int(route.ordre[i+1])][int(route.ordre[i])] / 0.999 + (1/dist) + extra_phero )
    


def main():
    app = TSP_ACO()

main()