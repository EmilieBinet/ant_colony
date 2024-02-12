import tsp_graph_init as init

class Affichage (init.tk.Tk):
    def __init__(self, hauteur, largeur, NB_LIEUX) -> None:
        init.tk.Tk.__init__(self)
        nb_it = 0
        best_dist = 0
        self.title("G2 - Algo fourmis")
        self.draw_lieu(NB_LIEUX, largeur, hauteur)
        self.d_evolution(nb_it, best_dist)
        self.bind("<Escape>", self.close_f)
        self.mainloop()


    def d_evolution(self, nb_it, best_dist):
        evolution = init.tk.Label(self, text=f"nombre d'itérations: {nb_it}, meilleure distance: {best_dist}")
        evolution.pack()

    def draw_lieu(self, NB_LIEUX, largeur, hauteur):
        self.canvas = init.tk.Canvas(self, width=largeur, height=hauteur, bg='white')
        self.canvas.pack(anchor=init.tk.CENTER, expand=True)
        for i in range(NB_LIEUX):
            x_max = init.random.randint(0, largeur)
            y_max = init.random.randint(0, hauteur)
            self.canvas.create_oval(x_max-30,y_max, x_max, y_max-30)


    def close_f(self, event):
        self.destroy()


def main():
    fenetre = Affichage(init.HAUTEUR, init.LARGEUR, 5)

main()