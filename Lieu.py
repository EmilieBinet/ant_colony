from define import *

class Lieu:
    x = 0
    y = 0
    name = ""

    def __init__(self, xinit=None, yinit=None, nameinit=None):
        if xinit is None:
            xinit = np.random.randint(DIAMETRE, LARGEUR - DIAMETRE)
        if yinit is None:
            yinit = np.random.randint(DIAMETRE, HAUTEUR - DIAMETRE)
        if nameinit is None:
            nameinit = "noname"
        self.x = xinit
        self.y = yinit
        self.name = nameinit
    

    def distance(self, lieu2):
        dist = ((lieu2.x-self.x)**2 + (lieu2.y-self.y)**2)**(1/2)
        return round(dist,1)
    
    def __repr__(self):
        return f'Lieu(\'{self.name}\', {self.x}, {self.y})'
