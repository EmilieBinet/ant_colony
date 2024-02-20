from define import *
from Affichage import Affichage
from Lieu import Lieu
from Matrice_od import Matrice_od
from Graph import Graph
from Route import Route

class TSP_ACO():
    def __init__(self, csv_file = None) -> None:
        graph = Graph(csv_file)
        self.mat_pheromones = Matrice_od(np.ones((NB_LIEUX, NB_LIEUX)))#Problème ici  : tente de créer une matrice_od, or la classe veut en argument une matrice = None
        print(f"matrice phéromones initiale: {self.mat_pheromones.matrice}")
        route_glouton = Route()
        route_glouton.glouton(graph)
        self.best_route=route_glouton
        glouton_dist = route_glouton.dist_total
        self.update_mat_pheromones(route_glouton, graph, glouton_dist, 1)
        print(glouton_dist)
        min_dist=glouton_dist
        self.fenetre = Affichage(graph, self.best_route, HAUTEUR, LARGEUR, NB_LIEUX, self.mat_pheromones)#fonctionne pour ce test unitaire

        for i in range(NB_FOURMIS):
            nb_it = i
            extra=None
            route = Route(graph, self.mat_pheromones.matrice)
            print(f"route {i}: {route.ordre}")
            dist = route.dist_total
            # print(min_dist, dist)
            if dist<min_dist:
                # print("min")
                extra=1
                min_dist = dist
                self.best_route=route
            else:
                extra=0
            # print(f"dist: {dist}")
            self.update_mat_pheromones(route, graph, dist, extra)
            print(f"matrice phéromones: {self.mat_pheromones.matrice}\n")
            self.fenetre.update_win(route=self.best_route, liste_lieux=graph.liste_lieux, matrice=self.mat_pheromones, nb_it=nb_it)
            self.fenetre.update_idletasks()
            self.fenetre.update()
        print(f"glouton_dist: {glouton_dist}")

    def update_mat_pheromones(self, route, graph, dist, extra):
        """"Met à jour la matrice de phéromones en fonction de la route qui vient d'être choisie par la fourmi et de la proximité entre les deux points"""
        extra_phero = extra*20
        self.mat_pheromones.matrice *= 0.999
        for i in range(len(route.ordre)-1):
            self.mat_pheromones.matrice[int(route.ordre[i])][int(route.ordre[i+1])] = (self.mat_pheromones.matrice[int(route.ordre[i])][int(route.ordre[i+1])] / 0.999 + (1000/dist) + extra_phero )
            self.mat_pheromones.matrice[int(route.ordre[i+1])][int(route.ordre[i])] = (self.mat_pheromones.matrice[int(route.ordre[i+1])][int(route.ordre[i])] / 0.999 + (1000/dist) + extra_phero )
    


