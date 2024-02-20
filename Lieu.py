from define import *

class Lieu:
    # Lieu has 3 attributes : coords and a name
    x = 0
    y = 0
    name = ""

    def __init__(self, xinit=None, yinit=None, nameinit=None):
        """ Create Lieu object
        xinit : x coord to give to the new Lieu
        yinit : y coord to give to the new Lieu
        nameinit : the name to give to the new Lieu
        """
        # x and y are random if no value is given
        if xinit is None: 
            xinit = np.random.randint(DIAMETRE, LARGEUR - DIAMETRE)
        if yinit is None:
            yinit = np.random.randint(DIAMETRE, HAUTEUR - DIAMETRE)
        # default name is noname unless a name is given
        if nameinit is None:
            nameinit = "noname"
        self.x = xinit
        self.y = yinit
        self.name = nameinit
    

    def distance(self, lieu2):
        """ Calcul the distance between two points
        lieu2 : the second point
        """
        dist = ((lieu2.x-self.x)**2 + (lieu2.y-self.y)**2)**(1/2)
        return round(dist,1) # only one decimal
    
    def __repr__(self):
        """ Function to compute informaitons when an object is created
        """
        return f'Lieu(\'{self.name}\', {self.x}, {self.y})'
