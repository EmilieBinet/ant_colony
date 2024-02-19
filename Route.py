from define import *
from Graph import Graph

class Route:

    def __init__(self, graph=Graph()):
        self.ordre = ["0"]
        dist_total = 0
        voisin = graph.liste_lieux[:]
        print(f"Liste_lieux : {graph.liste_lieux}")
        # del voisin[0] # retire 0 des voisins
        while len(self.ordre) != NB_LIEUX:
            lieu_from=[lieu for lieu in graph.liste_lieux if lieu.name == self.ordre[-1]][0]
            #print(f'lieu passé: {lieu_from}')
            voisin.remove(lieu_from)
            #print(f'voisin: {voisin}')
            closest = graph.plus_proche_voisin(lieu_from, voisin)
            dist_total = graph.calcul_distance_route(dist_total, self.ordre[-1], closest)
            print(f"Total : {dist_total}")
            self.ordre.append(closest.name)
            #print(f"ordre petit à petit: {self.ordre}")
        self.ordre.append("0")
        

    def __eq__(self, __value: object) -> bool:
        pass
    
    
    def __repr__(self):
        return f'Route(\'{self.ordre}\')'

    def fourmi_chemin(matrice_a, matrice_b):
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


            # best_proba, best_dest = 0, None
            # for i in range(NB_LIEUX):
            #     if i == lieu_depart:
            #         continue
            #     else:
            #         proba = 0.5*depart_a[i] + 0.5*depart_b[i]
            #         if proba > best_proba:
            #             best_proba, best_dest = proba, i
            self.ordre.append(str(chosen_dest))
        self.ordre.append("0")

# def random_choice(self,lieu, liste_lieux_restant):
#     """Choisi aléatoirement le noeud en fonction des probabilités des matrices de phéromones et de distance"""
#     mat_prob_left = 0.5*self.mat_pheromones[] + 0.5*self.mat_prob_dist #Doit ressortir une liste de probabilités en fonction d'un lieu 
#     choice = random.choices(liste_lieux_restant, weights=mat_prob_left, k=1)
#     return choice

