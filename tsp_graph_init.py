# -*- coding: utf-8 -*-

from define import *

#Import Class
from Graph import Graph
from Lieu import Lieu
from Route import Route
from Affichage import Affichage
from tsp_aco import TSP_ACO


def main():
    """To use with a .csv file already containing points coordinates: add r'YOUR_CSV_PATH' as an argument of TSP_ACO()"""
    app = TSP_ACO()

main()