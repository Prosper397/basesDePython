class Point(object) :
    "Définition de la classe Point"

P9 = Point()
print(P9)
print(P9.__doc__)

P9.x = 4.0
P9.y = 3.0
print(P9.x)
print(P9.x**2 + P9.y**2)


def affcihe_point(p) :
    print("Cood. horizontale=", p.x, " Coord. Verticale=", p.y)

affcihe_point(P9)

from math import sqrt, pow
def distance(p1, p2) :
    return sqrt(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2))

p1, p2 = Point(), Point()
p1.x, p1.y, p2.x, p2.y = 1.5, -5.8, -8.5, 6.0
print("Distance P1P2 = ", distance(p1, p2))

p1, p2 = Point(), Point()
p1.x, p1.y, p2.x, p2.y = 3, 4, 3, 4
print(p1 == p2)     #False
print(p1)
print(p2)
p1 = p2
print(p1 == p2)         #True

p1.x = 7
print(p2.x)     #Donne 7
print(p1)
print(p2)

#La fct hash256()
import hashlib

message = "Bonjour le monde"
hash_object = hashlib.sha256(message.encode())
print(hash_object.hexdigest())
print(hash_object)


#Objets composés d'objets
class Rectangle(object) :
    "définition d'une classe de rectangles"

#Objet boite de la classe Rectangle
boite = Rectangle()
boite.largeur = 50.0
boite.hauteur = 35.0
boite.coin = Point()
boite.coin.x, boite.coin.y = 12.0, 27.0


#Objets comme valeur de retour d'1e fct
def trouveCentre(box) :
    p = Point()     #Objet p de la classe Point()
    #Modification des attributs de p
    p.x = box.coin.x + box.largeur/2.0
    p.y = box.coin.y + box.hauteur/2.0
    return p

centre = trouveCentre(boite)
print(centre.x, centre.y)

#Modification des objets

boite.hauteur = boite.hauteur + 20      #On augmente la hauteur de la boite de 20
boite.largeur = boite.largeur -5        #On a diminué la largeur de la boite de 5

print(boite.hauteur, boite.largeur)         #On aura hauteur = 30 et largeur = 45



class Time(object) :
    "Définition d'objets temporels"

instant = Time()
instant.heure, instant.minute, instant.seconde = 11, 34, 25

def affiche_heure(Heure) :
    print(Heure.heure,":",Heure.minute,":",Heure.seconde)

affiche_heure(instant)


def affiche_heure(t) :
    print(str(t.heure) +":" + str(t.minute) +":" + str(t.seconde))

affiche_heure(instant)

def affiche_point(t) :
    print("{0}:{1}:{2}".format(t.heure, t.minute, t.seconde))

affiche_point(instant)


deuxPoint = ":"
def affiche_point(Heure) :
    print("{0}{1}{2}{3}{4}".format(Heure.heure, deuxPoint, Heure.minute, deuxPoint, Heure.seconde))

affiche_point(instant)


class Time(object) :
    "Nouvelle classe temporelle"
    #Méthode affiche_heure
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))

#Objet maintenant
maintenant = Time()
#Les attributs de l'instance maintenant
maintenant.heure = 13
maintenant.minute = 34
maintenant.seconde = 21
#APpliquons mtn la méthode affiche_heure à l'objet maintenant
maintenant.affiche_heure()



#La méthode constructeur
class Time(object) :
    "Encore une nvelle classe temporelle"
    #Le constructeur de la classe
    def __init__(self):
        self.heure = 12
        self.minute = 0
        self.seconde = 0
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))

#Objet tstart
tstart = Time()
tstart.affiche_heure()


class Temps(object) :
    "Encore une nouvelle classe temporelle"
    #Le constructeur
    def __init__(self, hh = 12, mm = 0, ss = 0):
        self.heure = hh
        self.minute = mm
        self.seconde = ss
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))

recreation = Temps(10, 15, 18)
recreation.affiche_heure()
rentree = Temps(10, 30)
rentree.affiche_heure()
rendezVous = Temps(hh = 18)
rendezVous.affiche_heure()

#--EXERCICES--

#--EXO 12.1 --
class Domino(object) :
    "Classe permettant d'instancier des objets simulant les pièces d'1 jeu de dominos."
    #Le constructeur de la classe
    def __init__(self, A = 0, B = 0):
        self.faceA, self.faceB = A, B
    def affiche_points(self):
        print("face A :", self.faceA, "face B :", self.faceB)
    def valeur(self):
        return self.faceA + self.faceB

#Exple d'utilisation
d1, d2 = Domino(2, 6), Domino(4, 3)
d1.affiche_points()
d2.affiche_points()
print("total des points :", d1.valeur() + d2.valeur())

liste_dominos = []
for i in range(7) :
    liste_dominos.append(Domino(6, i))
print(liste_dominos[3])     #Liste d'objets de la classe Domino

#EXO 12.2

class compteBancaire(object) :
    "Classe permettant d'instancier des objets tels que compte1, compte2..."
    #Le constructeur
    def __init__(self, nom = "Dupond", solde = 1000):
        self.nom, self.solde = nom, solde
    #Méthode qui permet de déposer une somme
    def depot(self, somme:float):
        self.solde += somme
    #Méthode qui permet de retirer une certaine somme
    def retrait(self, somme:float):
        self.solde -= somme
    #Méthode qui permet d'afficher le titulaire du compte et le solde
    def affiche(self):
        print("Le solde du compte de", self.nom, "est de ", self.solde, "euros")

#Simulation
compte1 = compteBancaire('Duchmol', 800)
compte2 = compteBancaire()
compte1.depot(350)     #800+350 = 1150
compte1.retrait(200)    # 1150-200 = 950
compte1.affiche()
compte2.depot(25)
compte2.affiche()


#--EXO 12.3 --
class Voiture(object) :
    "Classe permettant d'instancier des objets reproduidant le comportement des voitures automobiles"
    #Le constructeur
    def __init__(self, marque = 'Ford', couleur = 'rouge', pilote = 'personne', vitesse = 0):
        self.marque, self.couleur, self.pilote, self.vitesse = marque, couleur, pilote, vitesse
    #Méthode permettant de changer ou de changer le nom du conducteur
    def choix_conducteur(self, nom):
        self.pilote = nom
    #Méthode permettant de faire varier la vitesse de la voiture
    def accelerer(self, taux, duree):
        if self.pilote == 'personne':
            print("Cette voiture n'a pas de conducteur !")
        else :
            self.vitesse += taux*duree          #Pr modifier la vitesse(accéléraion ou décélération)
    #Méthode affiche_tout permettant de faire apparaitre les propriétés présentes de la voiture
    def affiche_tout(self):
        print(self.marque,self.couleur, "pilotée par", self.pilote, ", vitesse =", self.vitesse, "m/s")

#Simulation
a1 = Voiture("Peugeot", 'bleue')
a2 = Voiture(couleur = "verte")
a3 = Voiture('Mercedez')
a1.choix_conducteur('Roméo')
a2.choix_conducteur('Juliette')
a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11)
a2.affiche_tout()
a3.affiche_tout()



from math import pow

class Satellite(object) :
    "Classe permettant d'instancier des objets simulant des satellites artificiels lancés dans l'espace, autour de la terre"
    def __init__(self, nom:str, masse = 100, vitesse = 0):
        self.nom, self.masse, self.vitesse = nom, masse, vitesse
    #Méthode permettant de faire varier la vitesse du satellite
    def impulsion(self, force, duree):
        self.vitesse += (force*duree) / self.masse
    #Méthode permettant d'afficher le nom du satellite et sa vitesse courante
    def affiche_vitesse(self):
        print("Vitesse du satellite", self.nom, "=", self.vitesse, "m/s")
    #Méthode qui renverra au programme appelant la valeur de l'énergie cinétique
    def energie(self):
        return (self.masse * pow(self.vitesse, 2)) / 2

#Simulation
s1 = Satellite('Zoé', masse = 250, vitesse = 10)
s1.impulsion(500, 15)
s1.affiche_vitesse()
print(s1.energie())
s1.impulsion(500, 15)
s1.affiche_vitesse()
print(s1.energie())


#Notion d'espaces de noms des classes et des instances
class Espaces(object) :
    aa = 33
    def affiche(self):
        print(aa, Espaces.aa, self.aa)

aa = 12
essai = Espaces()
essai.aa = 67
essai.affiche()

#Notion d'Héritage

class Mammifere(object) :
    carac1 = "Il allaite ses petits ;"

class Carnivore(Mammifere) :
    carac2 = "Il se nourrit de la chair de ses proies ;"

class Chien(Carnivore) :
    carac3 = "Son cri s'appelle aboiement ;"

#Objet chien
mirza = Chien()
print(mirza.carac1, mirza.carac2, mirza.carac3)

#L'instance mirza peut accéder à ses attributs mais pas les modifier
mirza.carac2 = "Son corps est couvert de poils;"
print(mirza.carac2)
#Instance fido
fido = Chien()
print(fido.carac2)


#Notion de polymorphisme

class Atome(object) :
    "atomes simplifiés, choisis parmi les 10 premiers éléments du TP"
    table = [None, ('hydrogène', 0), ('hélium', 2), ('lithium', 4),
             ('beryllium', 5), ('bore', 6), ('carbone', 6), ('azote', 7),
             ('oxygène', 8), ('fluor', 10), ('néon', 10)]
    #le construcuteur de la classe
    def __init__(self, nat):
        "le n° atomique détermine le n. de protons, d'éléctrons et de neutrons"
        self.np, self.ne = nat, nat         # nat = numéro atomique
        self.nn = Atome.table[nat][1]

    def affiche(self):
        #1e ligne vide(séparatrice)
        print()
        print("Nom de l'élément :", Atome.table[self.np][0])
        print("{0} protons, {1} éléctrons, {2} neutrons".format(self.np, self.ne, self.nn))


class Ion(Atome) :  #La classe Ion hérite de la classe Atome
    """Les ions sont des atomes qui ont gagné ou qui ont perdu des éléctrons"""

    #Le constructeur de la classe
    def __init__(self, nat, charge):
        "Le n° atomique et la charge détermine l'ion"
        Atome.__init__(self, nat)
        self.ne -= charge
        self.charge = charge

    def affiche(self):
        Atome.affiche(self)
        print("Particule électrisée. Charge =", self.charge)

### Progamme principal :###
a1 = Atome(5)
a2 = Ion(3, 1)
a3 = Ion(8, -2)
a1.affiche()
a2.affiche()
a3.affiche()

"""
Le fait qu'il y a une ligne une ligne supplémentaire
dans la méthode affiche de la classe
 Ion fait intervenir la notion de polymorphisme.
 L'héritage ne concerne que les classes et non les instances de ces classes."""




class Point(object) :
    "point géométrique"
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Rectangle(object) :
    "rectangle"
    def __init__(self, ang, lar, hau):
        self.ang = ang
        self.lar = lar
        self.hau = hau
    def trouveCentre(self):
        xc = self.ang.x + self.lar/2
        yc = self.ang.y + self.hau/2
        return  Point(xc, yc)
class Carre(Rectangle) :
    """carre = Rectangle particulier"""
    def __init__(self, coin, cote):
        Rectangle.__init__(self, coin, cote, cote)
        self.cote = cote
    def surface(self):
        return  self.cote**2

#PROGRAMME PRINCIPAL

csgR = Point(40, 30)
csgC = Point(10, 25)

boiteR = Rectangle(csgR, 100, 50)
boiteC = Carre(csgC, 40)


cR = boiteR.trouveCentre()
cC = boiteC.trouveCentre()

print("Centre du rectangle:", cR.x, cR.y)
print("Centre du carré:", cC.x, cC.y)

print("Surface du carré:", end="")      #Ça va permettre d'afficher ceci et ce qui va suivre sur la meme ligne
print(boiteC.surface())





























