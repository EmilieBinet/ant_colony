from define import *
from Graph import Graph

class Route:

    def __init__(self, graph=Graph()):
        self.ordre=[]
        
    #Fonctions de comparaison des routes:
    def __eq__(self, __value: object) -> bool:
        pass
    
    def __ne__(self, __value: object) -> bool:
        pass

    def __lt__(self, __value: object) -> bool:
        pass

    def __gt__(self, __value: object) -> bool:
        pass

    def __ge__(self, __value: object) -> bool:
        pass
    
    def __le__(self, __value: object) -> bool:
        pass



    #Fonction pour afficher l'objet route
    def __repr__(self):
        return f'Route(\'{self.ordre}\')'


    def glouton(self, graph):
        self.ordre = ["0"]
        dist_toal = 0
        voisin = graph.list_lieux[:]
        while len(self.ordre) != NB_LIEUX:
            lieu_from=[lieu for lieu in graph.liste_lieux if lieu.name == self.ordre[-1]][0]
            voisin.remove(lieu_from)
            closest = graph.plus_proche_voisin(lieu_from, voisin)
            dist_total = graph.calcul_distance_route(dist_total, self.ordre[-1], closest)
            print(f"Total : {dist_total}")
            self.ordre.append(closest.name)
        self.ordre.append("0")

    def ant_route(self, matrice_a, matrice_b):
        self.ordre = ["0"]
        while len(self.ordre) != NB_LIEUX:
            lieu_depart = int(self.ordre[-1])
            destinations = matrice_a[lieu_depart]#prob_dist
            pheromones = matrice_b[lieu_depart]#prob_phero
            dest_left, phero_left = [],[]
            for i in range(NB_LIEUX):
                if str(i) in self.ordre:
                    continue
                else:
                    dest_left.append(destinations[i])
                    phero_left.append(pheromones[i])
            prob = random.choices(dest_left, weights=[0.5*d+0.5*p for d,p in zip(dest_left, phero_left)], k=1)
            chosen_dest = [id for id, val in enumerate(destinations) if val == prob and id not in self.ordre][0]
            print(f"Prochain noeud : {chosen_dest}")
            self.ordre.append(str(chosen_dest))
        self.ordre.append("0")
