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

#tests unitaires
graph = Graph()
print(graph)
matrice = graph.calcul_matrice_cout_od()
print(graph)

route = Route(graph)
print(route)

fenetre = Affichage(graph, route, HAUTEUR, LARGEUR, NB_LIEUX, matrice)#fonctionne pour ce test unitaire