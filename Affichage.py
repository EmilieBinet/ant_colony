from Graph import Graph
from Route import Route
import tkinter as tk

class Affichage (tk.Tk):
    def __init__(self, hauteur, largeur, NB_LIEUX) -> None:
        g = Graph()
        liste_lieux = g.liste_lieux
        tk.Tk.__init__(self)
        nb_it = 0
        best_dist = 0
        self.title("G2 - Algo fourmis")
        self.draw_lieu(liste_lieux, largeur, hauteur)
        self.d_evolution(nb_it, best_dist)
        self.bind("<space>", self.d_matrix)
        self.bind("<Escape>", self.close_f)
        self.mainloop()


    def d_evolution(self, nb_it, best_dist):
        evolution = tk.Label(self, text=f"nombre d'itérations: {nb_it}, meilleure distance: {best_dist}")
        evolution.pack()


    def draw_lieu(self, liste_lieux, largeur, hauteur):
        self.canvas = tk.Canvas(self, width=largeur, height=hauteur, bg='white')
        self.canvas.pack(anchor=tk.CENTER, expand=True)
        for lieu in liste_lieux:
            x = lieu.x
            y = lieu.y
            self.canvas.create_oval(x, y, x+30, y+30)


    def d_route():
        pass


    def d_matrix(self, event):
        win = tk.Toplevel(self)
        win.title("Matrix of cost")


    def close_f(self, event):
        self.destroy()


def main():
    fenetre = Affichage(600, 800, 5)

main()