"""Script qui crée 1 mini-système de base de données fonctionnant à l'aide d'1 dictionnaire.
Ds le dictionnaire, on mémorisera les noms d'1e série de copains, leur age et leur taille.
Le script devra comporter 2 fcts:La 1ère pr le remplissage et la seconde pr sa consultation.Ds la fct de remplissage(la 1ère),
on doit utiliser 1e boucle pr accepter les données entrées pr l'utilisateur.
Ds le dictionnaire, le nom de l'élève servira  de clé d'accès, et les valeurs seront constituées de tuples(age, taille).L'age
 sera exprimé en années(entier), et la taille en mètres(réel).
La fct de consultation comportera elle aussi 1e boucle, ds laquelle l'utilisateur pourra fournir 1 nom quelconque pr obtenir
en retour le couple "age, taille" correspondant.Le résultat de la requete devra etre 1e ligne de texte bien formatée, telle
par exemple : "Nom: Jean Dhoute -age:15 ans -taille:1.74 m".Il ft se servir du formatage des chaines de caractères"""



#1ère fct(remplissage du dictionnaire)
def remplissage():
    dico = {}
    while True :
        nom = input("Veuillez entrer le nom du copain:")
        if nom == "" :      #C'est le nom seul qu'on vérifie
            break
        age, taille = int(input("Veuillez entrer l'age du copain:")), float(input("Veuillez entrer la taille du copain:"))
        print()         #On crée 1 espace entre les infos de 2 copains
        dico[nom] = (age, taille)
    return dico
#print(remplissage())


#2è fct(Consultation)
def consultation(name:str, dico:dict) :
    for cle, valeur in dico.items() :
        if cle == name :
            print("Nom:{} -age:{} ans -taille:{} m".format(name, valeur[0], valeur[-1]))

#copains = remplissage()

#print("Dictionnaire remplie:", copains)

#nom_du_copain_a_consulter = input("Entrez le nom du copain à consulter:")
#consultation(nom_du_copain_a_consulter, copains)


"""
def changerCleValeur(dictionnaire:dict) :
    nouveauDict = {}
    for cle, valeur in dictionnaire.items() :
        nouveauDict[valeur] = cle
    return nouveauDict

print(changerCleValeur({"Français":"Anglais", "Anglais":"Français"}))
"""

"""Complétons le 1er exo(mini-système de base de données) en lui ajoutant 2 fcts :l'1e pr enregistrer le dictionnaire résultant ds 1 fichier texte, et l'autre 
pr reconstituer ce dictionnaire à partir du fichier correspondant.
Détails: Chq ligne du fichier texte correspondra à 1 élt du dictionnaire(cle, valeur).Elle sera formatée de manière à bien séparer :
-la clé et la valeur(ie, le nom de la personne, d'1e part, et l'ensemble:"age + taille", d'autre part
-ds l'ensemble "age+taille", ces 2 données numériques"""

#from pickle import dump, load
def enregistrer(dicti:dict) :
    with open("fichierTest.txt", "w") as file :
        for cle, valeur in dicti.items():
            ligne = cle+"@"+valeur[0]+"#"+valeur[1] + "\n"
            file.write(ligne)

def reconstituer() :
    with open("fichierTest.txt", "r") as file :
        dico = {}
        for l in file :
            a = l.strip().split("@")    # "Prosper@19#1.70" va devenir ["Prosper", "19#1.70"]
            b = a[-1].split("#")        # On prend le dernier élt de cette liste(a) et on le transforme en liste en prenant
            #pr séparateur #.On aura dc pr exple ["19", "1.70"]
            dico[a[0]] = (b[0], b[1])   #On reconstitue notre liste
        return dico


# Exemple de dictionnaire à enregistrer
mon_dico = {
    "Prosper": ("19", "1.70"),
    "Afi": ("25", "1.65"),
    "Kodjo": ("30", "1.80")
}

# Enregistrement dans le fichier
enregistrer(mon_dico)

# Reconstitution depuis le fichier
nouveau_dico = reconstituer()

print(nouveau_dico)

#from os import getcwd
#print(getcwd())


"""Controle de flux d'exécution en python"""
from sys import exit
menu = input("Choisissez le menu de voltre choix: ")

dico = {'R':reconstituer,
     'A': remplissage,
     'C':consultation,
     'S':enregistrer,
     'T': exit}
dico[menu] ()


