from define import *

class Affichage (tk.Tk):
    def __init__(self, graph, route, hauteur, largeur, NB_IT, matrice) -> None:
        liste_lieux = graph.liste_lieux #get the list of place
        lst_route = route.ordre #get the glouton route 
        tk.Tk.__init__(self) #initialization of the tk.TK object
        nb_it = NB_IT #initialization of the iterations number
        self.display = 0 #tell to do not display cout matrix
        self.title("G2 - Algo fourmis") #write the window title
        self.canvas = tk.Canvas(self, width=largeur, height=hauteur, bg='white') #create the canvas
        self.canvas.pack(anchor=tk.CENTER, expand=True) #add the canvas to the window
        #call functions to initialize the first window
        self.draw_lieu(liste_lieux) 
        self.d_evolution(nb_it)
        self.draw_best_route(lst_route, liste_lieux)
        self.d_mat_cout(liste_lieux, matrice)
        self.bind("<Escape>", self.close_f) #close the window and exit the program when escape


    def d_evolution(self, nb_it):
        #function that write the number of iterations
        self.evolution = tk.Label(self, text=f"nombre d'itérations: {nb_it}") #create a label to write the information
        self.evolution.pack()


    def draw_lieu(self, liste_lieux):
        #function to draw the places on the window
        for lieu in liste_lieux:
            x = lieu.x
            y = lieu.y
            name = lieu.name
            self.canvas.create_text(x+15, y+15, text=name, font=("Arial", 15)) #create a text to write the place name
            self.canvas.create_oval(x, y, x+30, y+30) #create an oval to mark the place


    def draw_best_route(self, route, liste_lieux):
        #function to draw the best route
        for i in range(len(route)-1):
            for lieu in liste_lieux:
                if lieu.name == route[i]:
                    lieu_dep= lieu
                if lieu.name == route[i+1]:
                    lieu_arr = lieu
            self.canvas.create_text(lieu_dep.x+15, lieu_dep.y-15, text=str(i), font=("Arial", 10), fill="blue") #write the passage order
            self.canvas.create_line(lieu_dep.x, lieu_dep.y+15, lieu_arr.x, lieu_arr.y+15, width=5, fill="blue", dash=30) #draw the line between place


    def d_mat_cout(self, liste_lieux, matrice):
        #function to draw the way in function of the pheromon rate
        self.canvas.delete("all") #clean all routes
        for i in range(NB_LIEUX):
            for j in range(i, NB_LIEUX): 
                pt_a = liste_lieux[i]
                pt_b = liste_lieux[j]
                width = matrice.matrice[i][j]
                #create line to display way in function of pheromon rate
                if width > MAX:
                    width = MAX
                    self.canvas.create_line(pt_a.x, pt_a.y+15, pt_b.x, pt_b.y+15, width=width/50, fill="grey")
                elif width < MIN:
                    continue
                else:
                    self.canvas.create_line(pt_a.x, pt_a.y+15, pt_b.x, pt_b.y+15, width=width/50, fill="grey")

    def incr(self):
        self.display += 1

    def update_win(self, liste_lieux, matrice, route, nb_it):
        #function to update the window
        self.canvas.delete("all")
        self.bind("<space>", lambda event: self.incr()) #display or not the way in function of pheromon rate
        if self.display % 2 == 1:
            self.d_mat_cout(liste_lieux, matrice)
        self.draw_lieu(liste_lieux)
        self.draw_best_route(route.ordre, liste_lieux)
        self.evolution.config(text=f"nombre d'itérations: {nb_it}, dist: {route.dist_total}")
        self.bind("<Escape>", self.close_f)


    def close_f(self, event):
        #function to close program
        self.destroy()
        exit(0)

