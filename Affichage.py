from Graph import Graph
from Route import Route
import tkinter as tk
from tkinter import ttk

class Affichage (tk.Tk):
    def __init__(self, hauteur, largeur, NB_LIEUX) -> None:
        g = Graph()
        liste_lieux = g.liste_lieux
        tk.Tk.__init__(self)
        nb_it = 0
        best_dist = 0
        self.title("G2 - Algo fourmis")
        self.draw_lieu(liste_lieux, largeur, hauteur)
        self.draw_route(liste_lieux[0])
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
            name = lieu.name
            self.canvas.create_text(x+15, y+15, text=name, font=("Arial", 15))
            self.canvas.create_oval(x, y, x+30, y+30)


    def draw_route(self, lieu):
        x = lieu.x
        y = lieu.y
        self.canvas.create_line(x+30, y+30, 623, 25, width=2)
        pass

    def draw_matrix(self, NB_LIEUX, hauteur):
        for i in range(NB_LIEUX):
            y = i*(hauteur/(NB_LIEUX))
            for j in range(NB_LIEUX):
                x = j*(hauteur/(NB_LIEUX))
                self.win.canvas.create_text(x+200, y+100, text=self.matrix[i][j], tags=self.matrix[i][j])
                #self.win.canvas.create_rectangle(x+200,y, x+(hauteur/(NB_LIEUX)), y+(hauteur/(NB_LIEUX)))
        # for row in self.matrix:
        #     line = " | ".join(map(str, row))
        #     self.matrix_text.insert(tk.END, line + '\n')


    def d_matrix(self, event):
        largeur = 800
        hauteur = 600
        self.matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.win = tk.Toplevel(self)
        self.win.title("Matrix of cost")
        self.win.canvas = tk.Canvas(self.win, width=800, height=600, bg="white")
        self.win.canvas.pack(anchor=tk.CENTER)
        # self.matrix_text = tk.Text(self.win, wrap=tk.NONE)
        # self.matrix_text.pack()
        
        self.draw_matrix(3, hauteur)
        


    def close_f(self, event):
        self.destroy()
