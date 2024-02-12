class Lieu:
    x = 0
    y = 0
    name = ""

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 549be19a27ab42b26ce11b0027337165364bc2b4
    def __init__(self, xinit, yinit, nameinit):
        self.x = xinit
        self.y = yinit
        self.name = nameinit

    def distance(self, lieu2):
        dist = ((lieu2.x2-self.X)**2 + (lieu2.y2-self.y)**2)**(1/2)
        return dist
    
    def __repr__(self):
        return "('+str(self.x)','+str(self.y)')"
<<<<<<< HEAD
=======
=======
    def distance(self, x2, y2):
        dist = ((x2-self.X)**2 + (y2-self.y)**2)**(1/2)
        return dist
>>>>>>> 0fcb1c4a4daafb030f10d111645cc63f1ba8f1e6
>>>>>>> 549be19a27ab42b26ce11b0027337165364bc2b4
