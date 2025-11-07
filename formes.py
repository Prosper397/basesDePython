class Rectangle(object) :
    "classe de rectangles"
    def __init__(self, longueur = 0, largeur = 0):
        self.L = longueur
        self.l = largeur
        self.nom = "rectangle"

    def perimetre(self):
        return "({0:d} + {1:d} * 2 = {2:d}".\
        format(self.L, self.l, (self.L*self.l)*2)
    def surface(self):
        return "{0:d} * {1:d} = {2:d}".format(self.L, self.l, self.L*self.L)
    def mesures(self):
        print("Un {0} de {1:d} sur {2:d}".format(self.nom, self.L, self.l))
        print("a une surface de {0}".format(self.surface()))
        print("et un périmètre de {0})\n".format(self.perimetre()))

class Carre(Rectangle) :
    "Classe de carrés"
    def __init__(self, cote):
        Rectangle.__init__(self, cote, cote)
        self.nom = "carré"

if __name__ == "__main__" :
    r1 = Rectangle(15, 30)
    r1.mesures()
    c1 = Carre(13)
    c1.mesures()


### EXERCICES   ###


from math import pi
class Cercle(object) :
    "Classe permettant d'instancier des cercles de tailles variées"
    #Le constructeur
    def __init__(self, rayon):
        self.rayon = rayon
    #La méthode permettant de calcule la surface du cercle
    def surface(self):
        return pi*self.rayon**2

class Cylindre(Cercle) :
    "Classe Cylindre qui dérive de la classe Cercle"
    def __init__(self,rayon, hauteur):
        Cercle.__init__(self, rayon)
        self.hauteur = hauteur
    def volume(self):
        return Cercle.surface(self) * self.hauteur

#Simulation
cyl = Cylindre(5, 7)
print(cyl.surface())
print(cyl.volume())


class Cone(Cylindre) :
    "Classe Cone qui dérive de la classe Cylindre"
    def __init__(self, rayon, hauteur):
        Cylindre.__init__(self, rayon, hauteur)
    def volume(self):
        return Cylindre.volume(self) / 3
co = Cone(5, 7)
print(co.volume())



from random import shuffle
class JeuDeCartes(object):
    "Classe permettant d'instancier des objets dont le comportement soit similaire à celui d'1 vrai jeu de cartes"

    # Méthode constructeur (Une liste de tuples).
    liste = [  # Pique
        (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3),
        # Trèfle
        (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2),
        # Carreau
        (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1),
        # Coeur
        (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0)
    ]

    def __init__(self):
        self.jeu = JeuDeCartes.liste.copy()     #copy est utilisé pr éviter que ts les objets partagent la meme liste

    def nom_carte(self, carte: tuple):
        retour = ""  # Variable de retour initialisée

        if carte in self.jeu:
            indice0 = carte[0]

            if carte[1] == 3:  # Pique
                for i in range(2, 11):
                    if indice0 == i:
                        retour = str(i) + " de pique"
                if indice0 == 11:
                    retour = "valet de pique"
                if indice0 == 12:
                    retour = "dame de pique"
                if indice0 == 13:
                    retour = "roi de pique"
                if indice0 == 14:
                    retour = "as de pique"

            if carte[1] == 2:  # Trèfle
                for i in range(2, 11):
                    if indice0 == i:
                        retour = str(i) + " de trèfle"
                if indice0 == 11:
                    retour = "valet de trèfle"
                if indice0 == 12:
                    retour = "dame de trèfle"
                if indice0 == 13:
                    retour = "roi de trèfle"
                if indice0 == 14:
                    retour = "as de trèfle"

            if carte[1] == 1:  # Carreau
                for i in range(2, 11):
                    if indice0 == i:
                        retour = str(i) + " de carreau"
                if indice0 == 11:
                    retour = "valet de carreau"
                if indice0 == 12:
                    retour = "dame de carreau"
                if indice0 == 13:
                    retour = "roi de carreau"
                if indice0 == 14:
                    retour = "as de carreau"

            if carte[1] == 0:  # Coeur
                for i in range(2, 11):
                    if indice0 == i:
                        retour = str(i) + " de coeur"
                if indice0 == 11:
                    retour = "valet de coeur"
                if indice0 == 12:
                    retour = "dame de coeur"
                if indice0 == 13:
                    retour = "roi de coeur"
                if indice0 == 14:
                    retour = "as de coeur"

        return retour
    #Méthode battre()
    def battre(self):
        shuffle(self.jeu)
    #Méthode tirer()
    def tirer(self):
       if len(self.jeu) == 0 :
           return  None
       else :
           return self.jeu.pop(0)       #pop(3) va permettre de retirer la carte après tirage
#Simulation
j = JeuDeCartes()
#Battons les cartes
j.battre()
for n in range(53) :
    #Tirons une carte
    c = j.tirer()
    if c is None :
        print("Terminé !")
    else:
        print(j.nom_carte(c))


#Instancions 2 objets de la classe JeuDeCartes
A, B = JeuDeCartes(), JeuDeCartes()
#Mélangeons les 2
A.battre()
B.battre()
sum1, sum2 = 0, 0
for n in range(52) :
    a, b = A.tirer(), B.tirer()
    if a is None or b is None :     #Qd le paquet est vide, cassons la boucle
        break
    elif a > b :
        sum1 += 1
    elif a < b :
        sum2 += 1
    else :
        a, b = A.tirer(), B.tirer()
if sum1 > sum2 :
    print("Le joueur A a gagné.")
elif sum2 > sum1 :
    print("Le joueur B a gagné")
else :
    print("Match nul !")




from pooAvecPython import compteBancaire
from math import pow
#Définissons une nvelle classe compteEpargne()

class compteEpargne(compteBancaire) :
    "compteEpargne est une classe qui dérive de la classe compteBancaire"
    #Le constructeur doit permettre d'initialiser 1 taux d'intéret mensuel pr défaut égal à 0.3%
    def __init__(self, nom , solde , t = 3*pow(10, -3)):
        compteBancaire.__init__(self, nom , solde )     #Il ne faut  pas initialiser nom et solde
        self.tauxInteret = t

    def changeTaux(self, valeur):
        "Méthode qui permet de modifier ce taux à volonté"
        self.tauxInteret = valeur
    def capitalisation(self, nombreMois):
        """Cette méthode doit afficher le nbre de mois,
        le taux d'intéret pris en compte,
        """
        print("Capitalisation sur {0} mois de {1} est de {2}%".format(nombreMois, self.nom,round(self.tauxInteret*nombreMois*10, 2)))


#Exemple d'utilisation

c1 = compteEpargne('Duvivier', 600)
c1.depot(350)
c1.affiche()
c1.capitalisation(12)
c1.affiche()











