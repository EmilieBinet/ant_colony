from define import *
from Affichage import Affichage
from Lieu import Lieu
from Matrice_od import Matrice_od
from Graph import Graph
from Route import Route

class TSP_ACO():
    def __init__(self, csv_file = None) -> None:
        """ Initialize the object
        csv_file : path of the file to get the info for the graph creation
        """
        graph = Graph(csv_file) # create a graph object
        self.mat_pheromones = Matrice_od(np.ones((NB_LIEUX, NB_LIEUX)))#initialize matrix with 1s for pheromones
        route_glouton = Route() # create a first route to execute glouton algorithme 
        route_glouton.glouton(graph)
        self.best_route=route_glouton # route glouton kept as the best route 
        glouton_dist = route_glouton.dist_total # get distance of route glouton   
        self.update_mat_pheromones(route_glouton, glouton_dist, 1) # update pheromones matrix by adding some on the route glouton
        min_dist=glouton_dist # distance of glouton is kept as the best one  
        self.fenetre = Affichage(graph, self.best_route, HAUTEUR, LARGEUR, NB_LIEUX, self.mat_pheromones) # display window

        for i in range(NB_FOURMIS): # loop over the number of ants
            nb_it = i
            extra=None # to give extra pheromones if the new route is the best
            route = Route(graph, self.mat_pheromones.matrice) # get the route found by the ant
            dist = route.dist_total # get the route's distance 
            if dist<min_dist: # compare to thebest distance 
                extra=1 # to add extra pheromones 
                min_dist = dist # the distance becomes the new best distance
                self.best_route=route # same for best route
            else:
                extra=0 # no extra pheromones
            self.update_mat_pheromones(route, dist, extra)
            self.fenetre.update_win(route=self.best_route, liste_lieux=graph.liste_lieux, matrice=self.mat_pheromones, nb_it=nb_it)
            self.fenetre.update_idletasks()
            self.fenetre.update()

    def update_mat_pheromones(self, route, dist, extra):
        """"
        Update the pheromones matrix depending on the route the ant chose. The pheromones added depend on the distance between the two points.
        route : route object to access to the attribute ordre
        dist :  total distance of the route
        extra : get 0 or 1 value, 1 means extra pheromones will be added
        """
        extra_phero = extra*20 # if extra = 1, 20 pheromones are added
        self.mat_pheromones.matrice *= 0.999 # reduce the pheromones of every path 
        for i in range(len(route.ordre)-1): # add pheromones for every path the ant ran through
            # divide by 0.999 to cancel the reduction made before
            # add 1000/dist so it is proportional to the distance of the route (if route is small, pheromones added is big)
            # add the extra pheromones if there is some
            self.mat_pheromones.matrice[int(route.ordre[i])][int(route.ordre[i+1])] = (self.mat_pheromones.matrice[int(route.ordre[i])][int(route.ordre[i+1])] / 0.999 + (1000/dist) + extra_phero )
            self.mat_pheromones.matrice[int(route.ordre[i+1])][int(route.ordre[i])] = (self.mat_pheromones.matrice[int(route.ordre[i+1])][int(route.ordre[i])] / 0.999 + (1000/dist) + extra_phero )
    


