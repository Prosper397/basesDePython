from pooAvecPython import compteBancaire

class CompteEpargne(compteBancaire) :
    def __inti__(self,nom = 'Durand', solde = 500) :
        compteBancaire.__init__(self, nom, solde)
        self.taux = .3          #Taux d'intéret mensuel par défaut

    def changeTaux(self, taux):
        self.taux = taux

    def capitalisation(self, nombreMois = 6):
        print("Capitalisation sur {0} mois au taux mensuel de {1} %.".format(nombreMois, self.taux))
        for m in range(nombreMois) :
            self.solde += (100 + self.taux) / 100


 # Programme de test :

if __name__ == '__main__':
     c1 = CompteEpargne("Duvivier", 600)
     c1.depot(350)
     c1.affiche()
     c1.capitalisation(12)
     c1.affiche()
     c1.changeTaux(.5)
     c1.capitalisation(12)
     c1.affiche()


