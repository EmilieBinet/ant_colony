from define import *
from Graph import Graph
from Matrice_od import Matrice_od

class Route:

    def __init__(self, graph=Graph(), matrice_phero=Matrice_od(np.ones((NB_LIEUX, NB_LIEUX))).matrice):
        # self.glouton(graph)
        self.dist_total=0
        self.ant_route(graph, matrice_phero)

        
    #Fonctions de comparaison des routes:
    # def __eq__(self, other):
    #     #==
    #     if self.dist_total == other.dist_total:
    #         pass

    # def __lt__(self, other):
    #     #<
    #     if self.dist_total < other.dist_total:
    #         return 
        
    def glouton(self, graph):
        self.ordre = ["0"]
        voisin = graph.liste_lieux[:]
        while len(self.ordre) != NB_LIEUX:
            lieu_from=[lieu for lieu in graph.liste_lieux if lieu.name == self.ordre[-1]][0]
            voisin.remove(lieu_from)
            closest = graph.plus_proche_voisin(lieu_from, voisin)
            self.dist_total = graph.calcul_distance_route(self.dist_total, int(self.ordre[-1]), int(closest.name))
            self.ordre.append(closest.name)
        self.ordre.append("0")
        self.dist_total = graph.calcul_distance_route(self.dist_total, int(self.ordre[-2]), int(self.ordre[-1]))
        # print(f"Glouton {self.ordre}")

    def ant_route(self, graph, matrice_phero):
        self.ordre = ["0"]
        voisin = graph.liste_lieux[:]
        while len(self.ordre) != NB_LIEUX:
            lieu_from=[lieu for lieu in graph.liste_lieux if lieu.name == self.ordre[-1]][0]
            # print(lieu_from)
            voisin.remove(lieu_from)
            # print(f"matrice_cout: {graph.matrice_cout.matrice}")
            destinations = graph.matrice_cout.matrice[int(lieu_from.name)]#cout_od
            # print(f"destinations: {destinations}")
            pheromones = matrice_phero[int(lieu_from.name)]#prob_phero
            dest_left, phero_left = [],[]
            for i in range(NB_LIEUX):
                if str(i) in self.ordre:
                    continue
                else:
                    dest_left.append(destinations[i])
                    phero_left.append(pheromones[i])

            # print(f"dest_left: {dest_left}")
            prob_sum = sum(0 if elem == 0 else 1/elem for elem in dest_left)
            if prob_sum == 0:
                prob_sum = 1
            phero_sum = sum(elem for elem in phero_left)
            if phero_sum == 0:
                phero_sum = 1
            prob_dest = [(1/d)/prob_sum for d in dest_left]
            phero_dest = [p/phero_sum for p in phero_left]
            # print(f"prob_dest: {prob_dest}")

            prob = random.choices(dest_left, weights=[0.4*d+0.6*p for d,p in zip(prob_dest, phero_left)], k=1)
            chosen_dest = [id for id, val in enumerate(destinations) if val == prob and str(id) not in self.ordre][0]
            # print(f"Prochain noeud : {chosen_dest}")
            self.dist_total = graph.calcul_distance_route(self.dist_total, int(self.ordre[-1]), chosen_dest)
            # print(f"Total : {self.dist_total}")
            self.ordre.append(str(chosen_dest))
        self.ordre.append("0")
        self.dist_total = graph.calcul_distance_route(self.dist_total, int(self.ordre[-2]), int(self.ordre[-1]))

        return self.dist_total

    #Fonction pour afficher l'objet route
    def __repr__(self):
        return f'Route(\'{self.ordre}\')'
