from define import *
from Graph import Graph
from Matrice_od import Matrice_od

class Route:

    def __init__(self, graph=Graph(), matrice_phero=Matrice_od(np.ones((NB_LIEUX, NB_LIEUX))).matrice):
        self.dist_total=0
        self.ant_route(graph, matrice_phero)

    def glouton(self, graph):
        """Euristic function, searching for the shortest path between each edge."""
        self.ordre = ["0"]
        voisin = graph.liste_lieux[:]
        while len(self.ordre) != NB_LIEUX:
            lieu_from=[lieu for lieu in graph.liste_lieux if lieu.name == self.ordre[-1]][0]
            voisin.remove(lieu_from)#If we already passed by an edge, we don't need it anymore.
            closest = graph.plus_proche_voisin(lieu_from, voisin)#We fetch the closest neighbor that is still not in the way.
            self.dist_total = graph.calcul_distance_route(self.dist_total, int(self.ordre[-1]), int(closest.name))#We add the distance to the total of the way.
            self.ordre.append(closest.name)
        #We finish our path at the starting point
        self.ordre.append("0")
        self.dist_total = graph.calcul_distance_route(self.dist_total, int(self.ordre[-2]), int(self.ordre[-1]))

    def ant_route(self, graph, matrice_phero):
        """Ant normal path and adding of pheromones to influence the future path choices."""
        self.ordre = ["0"]
        voisin = graph.liste_lieux[:]
        while len(self.ordre) != NB_LIEUX:
            lieu_from=[lieu for lieu in graph.liste_lieux if lieu.name == self.ordre[-1]][0]
            voisin.remove(lieu_from)
            destinations = graph.matrice_cout.matrice[int(lieu_from.name)]
        
            pheromones = matrice_phero[int(lieu_from.name)]
            dest_left, phero_left = [],[]#The pheromones and the eadges that are left to visit
            for i in range(NB_LIEUX):
                if str(i) in self.ordre:
                    continue
                else:
                    dest_left.append(destinations[i])
                    phero_left.append(pheromones[i])

            prob_sum = sum(0 if elem == 0 else 1/elem for elem in dest_left)
            #To prevent dividing by 0 in the normalizations
            if prob_sum == 0:
                prob_sum = 1
            phero_sum = sum(elem for elem in phero_left) # sum every element in the list containing the pheromones for the left routes
            if phero_sum == 0:
                phero_sum = 1
            prob_dest = [(1/d)/prob_sum for d in dest_left] # Normalize the distance 

            #The ant is doing a random choice while knowing the distance and the pheromone in each hub thanks to the two matrix
            prob = random.choices(dest_left, weights=[0.4*d+0.6*p for d,p in zip(prob_dest, phero_left)], k=1)
            chosen_dest = [id for id, val in enumerate(destinations) if val == prob and str(id) not in self.ordre][0]
            self.dist_total = graph.calcul_distance_route(self.dist_total, int(self.ordre[-1]), chosen_dest)
            self.ordre.append(str(chosen_dest))
        self.ordre.append("0")
        self.dist_total = graph.calcul_distance_route(self.dist_total, int(self.ordre[-2]), int(self.ordre[-1]))

        return self.dist_total

    #Fonction pour afficher l'objet route
    def __repr__(self):
        return f'Route(\'{self.ordre}\')'
