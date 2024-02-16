from define import *
import Graph
class Route:

    def __init__(self):
        self.ordre = [0]
        voisin = Graph.liste_lieux
        del voisin[0] # retire 0 des voisins
        while len(self.ordre) != NB_LIEUX:
            closest = Graph.plus_proche_voisin(self.ordre[-1], voisin)
            voisin.remove(closest)
            self.ordre.append(closest)
        self.ordre.append(0)
        print(self.ordre)
        

    def __eq__(self, __value: object) -> bool:
        pass
