# from Graph import Graph
# from Route import Route

from define import *

class Affichage (tk.Tk):
    def __init__(self, graph, route, hauteur, largeur, NB_LIEUX, matrice) -> None:
        liste_lieux = graph.liste_lieux
        lst_route = route.ordre
        print(lst_route)
        tk.Tk.__init__(self)
        nb_it = 0
        best_dist = 0
        self.title("G2 - Algo fourmis")
        self.draw_lieu(liste_lieux, largeur, hauteur)
        # self.draw_route_init(lst_route, liste_lieux)
        self.d_evolution(nb_it, best_dist)
        self.bind("<space>", lambda event: self.d_mat_cout(liste_lieux, matrice, lst_route))
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


    def draw_best_route(self, route, liste_lieux):
        route = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] # à enlever et mettre la route obtenue avec l'algo
        for i in range(len(route)-1):
            for lieu in liste_lieux:
                if lieu.name == route[i]:
                    lieu_dep= lieu
                if lieu.name == route[i+1]:
                    lieu_arr = lieu
            self.canvas.create_line(lieu_dep.x, lieu_dep.y+15, lieu_arr.x, lieu_arr.y+15, width=5, fill="blue", dash=30)


    def d_mat_cout(self, liste_lieux, matrice, route):
        for i in range(NB_LIEUX):
            for j in range(i, NB_LIEUX):
                pt_a = liste_lieux[i]
                pt_b = liste_lieux[j]
                width = matrice.matrice[i][j]
                self.canvas.create_line(pt_a.x, pt_a.y+15, pt_b.x, pt_b.y+15, width=width, fill="black")
        self.draw_best_route(route, liste_lieux)

    
    def update_win(self): #finir fonction
        self.update()
        self.update_idletasks()


    def close_f(self, event):
        self.destroy()
