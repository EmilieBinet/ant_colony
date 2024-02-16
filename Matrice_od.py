from define import *

class Matrice_od:
    def __init__(self, matrice):
        
        if matrice == None:
            self.matrice = np.zeros((NB_LIEUX, NB_LIEUX)) # matrice de 0
        else:
            self.matrice = matrice

    def __repr__(self):
        return f'Matrice_od({self.matrice})'