from define import *


from tsp_graph_init import HAUTEUR, LARGEUR, DIAMETRE, np

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
        print(self.x)

    def distance(self, lieu2):
        dist = ((lieu2.x2-self.X)**2 + (lieu2.y2-self.y)**2)**(1/2)
        return dist
    
    def __repr__(self):
        return "('+str(self.x)','+str(self.y)')"
