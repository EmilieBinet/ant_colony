from define import *
from Graph import Graph
class Route:

    def __init__(self, graph=Graph()):
        self.ordre = ["0"]
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
            self.ordre.append(closest.name)
            #print(f"ordre petit à petit: {self.ordre}")
        self.ordre.append("0")
        

    def __eq__(self, __value: object) -> bool:
        pass
    
    def __repr__(self):
        return f'Route(\'{self.ordre}\')'
