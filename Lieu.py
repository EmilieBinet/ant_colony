class Lieu:
    x = 0
    y = 0
    name = ""

    def distance(self, x2, y2):
        dist = ((x2-self.X)**2 + (y2-self.y)**2)**(1/2)
        return dist