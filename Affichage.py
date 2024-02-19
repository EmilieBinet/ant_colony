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
        #self.draw_route_init(lst_route, liste_lieux)
        self.d_evolution(nb_it, best_dist)
        self.bind("<space>", lambda event: self.d_mat_cout(liste_lieux, matrice))
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


    def draw_route_init(self, route, liste_lieux):
        for i in range(len(route)-1):
            for lieu in liste_lieux:
                if lieu.name == route[i]:
                    lieu_dep= lieu
                if lieu.name == route[i+1]:
                    lieu_arr = lieu
            self.canvas.create_line(lieu_dep.x, lieu_dep.y, lieu_arr.x, lieu_arr.y, width=2)


    def draw_the_route(self, pt_a, pt_b, width):
        self.canvas.create_line(pt_a.x, pt_a.y, pt_b.x, pt_b.y, width=width)


    def d_mat_cout(self, liste_lieux, matrice):
        for i in range(NB_LIEUX):
            for j in range(i, NB_LIEUX):
                pt_a = liste_lieux[i]
                pt_b = liste_lieux[j]
                width = matrice.matrice[i][j]
                self.draw_the_route(pt_a, pt_b, width)


    def d_best_way(self):
        pass 

    # def draw_matrix(self, matrice, NB_LIEUX, hauteur):
    #     for i in range(NB_LIEUX+1):
    #         y = i*(hauteur/(NB_LIEUX+1))
    #         for j in range(NB_LIEUX+1):
    #             x = j*(hauteur/(NB_LIEUX+1))

    #             # Dessiner le contour
    #             cell_width = hauteur / (NB_LIEUX+1)
    #             self.win.canvas.create_rectangle(x , y, x + cell_width, y + cell_width, outline="black")

    #             # Trouver le centre du rectangle
    #             center_x = x + cell_width / 2
    #             center_y = y + cell_width / 2

    #             if i == 0 or j == 0:
    #                 if i == 0 and j == 0:
    #                     self.win.canvas.create_text(center_x, center_y, text=" ", font=("bold"))
    #                 elif i == 0:
    #                     self.win.canvas.create_text(center_x, center_y, text=str(j-1), font=("bold"))
    #                 elif j == 0:
    #                     self.win.canvas.create_text(center_x, center_y, text=str(i-1), font=("bold"))
    #             else: 
    #                 self.win.canvas.create_text(center_x, center_y, text=matrice.matrice[i-1][j-1])


    # def d_matrix(self, matrice):
    #     dimension = 800
    #     self.win = tk.Toplevel(self)
    #     self.win.title("Matrix of cost")
    #     self.win.canvas = tk.Canvas(self.win, width=dimension, height=dimension, bg="white")
    #     self.win.canvas.pack(anchor=tk.CENTER)      
    #     self.draw_matrix(matrice, len(matrice.matrice), dimension)
        

    def close_f(self, event):
        self.destroy()
