from define import *
from Affichage import Affichage
from Lieu import Lieu
from Matrice_od import Matrice_od
from Graph import Graph
from Route import Route

class TSP_ACO():
    def __init__(self, csv_file = None) -> None:
        graph = Graph(csv_file)
        self.mat_pheromones = Matrice_od(np.ones((NB_LIEUX, NB_LIEUX)))#initialise une matrice avec des 1 pour les phéromones
        # print(f"matrice phéromones initiale: {self.mat_pheromones.matrice}")
        route_glouton = Route()# créé une première route pour qui on va executer l'algorithme glouton 
        route_glouton.glouton(graph)
        self.best_route=route_glouton# route gloutonne gardée en tant que meilleure route 
        glouton_dist = route_glouton.dist_total#récupère la distance de la route gloutonne  
        self.update_mat_pheromones(route_glouton, graph, glouton_dist, 1)# emt à jour les phéromones en en ajoutant sur la route gloutonne 
        # print(glouton_dist)
        min_dist=glouton_dist# distance gloutonne gardée en tant que distance la plus petite  
        self.fenetre = Affichage(graph, self.best_route, HAUTEUR, LARGEUR, NB_LIEUX, self.mat_pheromones)# affichage de la fenêtre

        for i in range(NB_FOURMIS):
            nb_it = i
            extra=None
            route = Route(graph, self.mat_pheromones.matrice)# récupère la route de la fourmi 
            # print(f"route {i}: {route.ordre}")
            dist = route.dist_total# récupère la distance de cette route 
            # print(min_dist, dist)
            if dist<min_dist:# compare la distance à celle de la meilleure route 
                # print("min")
                extra=1# pour ajouter un bonus de phéromones 
                min_dist = dist# la distance devient la meilleure distance 
                self.best_route=route# idem pour la meilleure route 
            else:
                extra=0
            # print(f"dist: {dist}")
            self.update_mat_pheromones(route, graph, dist, extra)
            # print(f"matrice phéromones: {self.mat_pheromones.matrice}\n")
            self.fenetre.update_win(route=self.best_route, liste_lieux=graph.liste_lieux, matrice=self.mat_pheromones, nb_it=nb_it)
            self.fenetre.update_idletasks()
            self.fenetre.update()
        # print(f"glouton_dist: {glouton_dist}")

    def update_mat_pheromones(self, route, graph, dist, extra):
        """"Met à jour la matrice de phéromones en fonction de la route qui vient d'être choisie par la fourmi et de la proximité entre les deux points"""
        extra_phero = extra*20
        self.mat_pheromones.matrice *= 0.999
        for i in range(len(route.ordre)-1):
            self.mat_pheromones.matrice[int(route.ordre[i])][int(route.ordre[i+1])] = (self.mat_pheromones.matrice[int(route.ordre[i])][int(route.ordre[i+1])] / 0.999 + (1000/dist) + extra_phero )
            self.mat_pheromones.matrice[int(route.ordre[i+1])][int(route.ordre[i])] = (self.mat_pheromones.matrice[int(route.ordre[i+1])][int(route.ordre[i])] / 0.999 + (1000/dist) + extra_phero )
    


