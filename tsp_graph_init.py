# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:36:13 2024

@author: maelb
"""
from define import *

#Import Class
from Graph import Graph
from Lieu import Lieu
from Route import Route
from Affichage import Affichage
from tsp_aco import TSP_ACO

# #tests unitaires
# graph = Graph()
# print(graph)
# matrice = graph.calcul_matrice_cout_od()
# print(graph)

# route = Route(graph)
# print(route)

# fenetre = Affichage(graph, route, HAUTEUR, LARGEUR, NB_LIEUX, matrice)#fonctionne pour ce test unitaire

def main():
    app = TSP_ACO("csv/graph_30.csv")

main()