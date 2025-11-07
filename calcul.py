"""def heure(min:int, sec:int) :

min, sec= int(input("Entrez la minute")), int(input("Entrez la seconde"))
if sec == 60  :
    min += 1
 print(f"{min} minutes {}")
"""


# Mini Sokoban en Python (console)
"""
import os

# Plateau (niveau simple)
level = [
    "#####",
    "# . #",
    "# $ #",
    "# @ #",
    "#####"
]

# Convertir en liste de listes pour modification
board = [list(row) for row in level]

# Trouver la position initiale du joueur
for y, row in enumerate(board):
    for x, cell in enumerate(row):
        if cell == "@":
            player_pos = (y, x)

def print_board():
    os.system("cls" if os.name == "nt" else "clear")
    for row in board:
        print("".join(row))

def move(dy, dx):
    global player_pos
    y, x = player_pos
    ny, nx = y + dy, x + dx  # nouvelle position

    # Si c’est un mur, rien ne se passe
    if board[ny][nx] == "#":
        return

    # Si c’est une caisse
    if board[ny][nx] == "$":
        ny2, nx2 = ny + dy, nx + dx
        # Vérifier si on peut pousser
        if board[ny2][nx2] in " .":
            board[ny2][nx2] = "$"  # déplacer la caisse
            board[ny][nx] = "@"     # déplacer le joueur
            board[y][x] = " " if level[y][x] == " " else "."
            player_pos = (ny, nx)
    # Si c’est une case vide ozu une cible
    elif board[ny][nx] in " .":
        board[ny][nx] = "@"
        board[y][x] = " " if level[y][x] == " " else "."
        player_pos = (ny, nx)

# Boucle de jeu
while True:
    print_board()
    move_input = input("Déplace-toi (z/q/s/d, x pour quitter) : ")
    if move_input == "x":
        break
    moves = {"z": (-1, 0), "s": (1, 0), "q": (0, -1), "d": (0, 1)}
    if move_input in moves:
        dy, dx = moves[move_input]
        move(dy, dx)

"""

"""
Num =  int(input("Veuillez entrer le numéro de l'employé:"))
Nj = int(input("Veuillez entrer le nombre de jours que l'employé à travaillé:"))
Nkm = float(input("Veuillez entrer la distance entre l'entreprise et la maison de l'employé:"))
while True :
    if Nkm > 5 :
        if Nkm < 15 :
            Ij = 2000 * Nj
            print("L'indemnité est :", Ij)
        elif Nkm > 15 :
            Ij = 3000 * Nj
            print("L'indemnité est:", Ij)
    elif Nkm < 5 :
        Ij = 1000 * Nj
        print("L'indemnité est:", Ij)
    if Num > 0 :
        break
"""


"""
class Application(object) :
    def __init__(self):
    
    
        Construction de la fenêtre principale
        
        self.root = Tk()
        self.root.title('Code des couleurs')
        self.dessineResistance()
        Label(self.root, text ="Entrez la valeur de la résistance, en ohms :").\
            grid(row =2, column =1, columnspan =3)
        Button(self.root, text ='Montrer', command =self.changeCouleurs).\
            grid(row =3, column =1)
        Button(self.root, text ='Quitter', command =self.root.quit).\
            grid(row =3, column =3)
        self.entree = Entry(self.root, width = 14)
        self.entree.grid(row =3, column =2)
        # Code des couleurs pour pour les valeurs de zéro à neuf :
        self.cc = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey', 'white']
        self.root.mainloop()

    def dessineResistance(self):
    
        Canevas avec un modèle de résistance à trois lignes colorées
        
        
        self.can = Canvas(self.root, width =250, height =100, bg ="light blue")
        self.can.grid(row =1, column =1, columnspan =3, pady =5, padx =5)
        self.can.create_line(10, 50, 240, 50, width =5)         # fils
        self.can.create_rectangle(65, 30, 185, 70, fill ='beige', width =2)
        # Dessin des 3 lignes colorées (noires au départ) :
        self.ligne = []     # On mémorisera les 3 lignes dans 1 liste
        for x in range(85, 150, 24) :
            self.ligne.append(self.can.create_rectangle(x, 30, x+12, 70, fill ="black", width =0))

    def changeCouleurs(self):
    
    
        
        Affichage des couleurs correspondant à la valeur entrée
        
        
        self.v1ch = self.entree.get()       # Cette méthode renvoie une chaine
        try :
            v = float(self.v1ch)        # Conversion en valeur numérique
        except :
            err = 1                 # erreur : entrée non numérique
        else :
            err = 0


            if err == 1 or v < 10 or v > 1e11 :
                self.signaleErreur()        # Entrée incorrecte ou hors limites
            else :
                li = [0]*3
                logv = int(log10(v))        # Partie entière du logarithme
                ordgr = 10**logv            # Ordre de grandeur
                # Extraction du premier chiffre significatif :
                li[0] = int(v/ordgr)        # Partie entière
                decim = v/ordgr - li[0]     # Partie décimale
                # Extraction du second chiffre significatif :
                li[1] = int(decim*10 + .5)      # +.5 pour arrondir correctement
                # Nombre de zéros à accoler aux 2 chiffres significatifs :
                li[2] = logv -1
                # Coloration des 3 lignes :
                for n in range(3) :
                    self.can.itemconfigure(self.ligne[n], fill = self.cc[li[n]])

    def signaleErreur(self):
        self.entree.configure(bg = 'red')        # Colorer le fond du champ
        self.root.after(1000, self.videEntree)  # Après une seconde, effacer

    def videEntree(self):
        self.entree.configure(bg = 'white')     # rétablir le fond blanc
        self.entree.delete(0, len(self.v1ch))       # Enlever les car. présents


# Programme principal :
if __name__ == '__main__' :
    from tkinter import *
    from math import log10          # Logarithmes en base 10
    f = Application()               # Instanciation de l'objet application
"""


from tkinter import *
def cercle(can,x, y, r) :
    "Dessin d'un cercle de rayon <r> en <x, y> dans le canevas <can>"
    can.create_oval(x-r, y-r, x+r, y+r)


class Application(Tk) :
    def __int__(self):
        Tk.__init__(self)           # Constructeur de la classe parente
        self.can = Canvas(self, width=475, height=130, bg="white")
        self.can.pack(side=TOP, padx=5, pady=5)
        Button(self, text="Train", command=self.dessine).pack(side=LEFT)
        Button(self, text="Hello", command=self.coucou).pack(side=LEFT)

    def dessine(self):
        "Instanciation de 4 wagons dans le canevas"
        self.w1 = Wagon(self.can, 10, 30)
        self.w2 = Wagon(self.can, 130, 30)
        self.w3 = Wagon(self.can, 260, 30)
        self.w4 = Wagon(self.can, 370, 30)

    def coucou(self):
        "apparition de personnages dans certaines fenêtres"
        self.w1.perso(3)        # 1er wagon, 3 fenêtres
        self.w3.perso(1)        # 3è wagon, 1e fenêtre
        self.w3.perso(2)        # 3è wagon, 2 fenêtres
        self.w4.perso(1)        # 4è wagon, 1e fenêtre

class Wagon(object) :
    def __init__(self, canev, x, y):
        "Dessin d'un petit wagon en <x, y> dans le canevas <canev>"
        # Mémorisation des paramètres dans des variables d'instance :
        self.canev, self.x, self.y = canev, x, y
        # rectangle de base : 95*60 pixels :
        canev.create_rectangle(x, y, x+95, y+60)
        # 3 fenêtres de 25*40 pixels, écartées de 5 pixels :
        for xf in range(x+5, x
                            +90, 30) :
            canev.create_rectangle(xf, y+5, xf+25, y+40)
        # 2 roues de rayon égal à 12 pixels :
        cercle(canev, x+18, y+73, 12)
        cercle(canev, x+77, y+73, 12)

    def perso(self, fen):
        "apparition d'un petit personnage à la fenêtre <fen>"
        # calcul des coordonnées du centre de chaque fenêtre :
        xf = self.x + fen*30 -12
        yf = self.y + 25
        cercle(self.canev, xf, yf, 10)      # Visage
        cercle(self.canev, xf-5, yf-3, 2)   # oeil gauche
        cercle(self.canev, xf+5, yf-3, 2)   # oeil droit
        cercle(self.canev, xf, yf+5, 3)     # bouche

app = Application()
app.mainloop()
