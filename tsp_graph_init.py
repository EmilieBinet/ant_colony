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

for i in range(0,N_ITERATION):
    #tests unitaires
    lieu = Lieu()
    lieu2 = Lieu(1,1,"0")
    print(lieu)
    print(lieu2)

    graph = Graph()
    print(graph)
    graph.calcul_matrice_cout_od()
    print(graph)

    route = Route(graph)
    print(route)


