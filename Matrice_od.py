from define import *

class Matrice_od:
    # Matrice_od has one attribute : matrice
    def __init__(self, matrice=[]):
        """ Initialize the object
        matrice : the matrix to add to the attribute of the object
        """
        
        if len(matrice) == 0: # if the matrix is empty (no matrix given to create the object)
            self.matrice = np.zeros((NB_LIEUX, NB_LIEUX)) # create a matrix filled with 0 with the size of number of points on the graph
        else:
            self.matrice = matrice

    def __repr__(self):
        """ Function to compute informaitons when an object is created
        """
        return f'Matrice_od({self.matrice})'