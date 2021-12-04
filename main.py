tab = ["","","","","","","","",""]
nbTour = 0
victoire = False

def afficheGrille(tab) :
    iteration = False
    i = 0
    while i < 9 :
        if iteration == False :
            for j in range(2) :
                print(tab[i], end="|")
                i=i+1
            print(tab[i], end="\n")
            i=i+1
            iteration = True
        else :
            for k in range(3) :
                print("_", end=" ")
            print("\n")
            iteration = False

def symbole(tab, nbTour) :
    saisie = 1
    caseValable = False
    if nbTour % 2 > 0 :
        while not caseValable :
            saisie = int(input("Veuillez saisir votre case, 1 étant la première en haut à gauche et 9 la dernière en bas à droite : "))
            if tab[saisie-1] == "" and saisie < 10 and saisie >= 0 :
                caseValable = True
        tab[saisie-1] = "X"
    else :
        while not caseValable :
            saisie = int(input("Veuillez saisir votre case, 1 étant la première en haut à gauche et 9 la dernière en bas à droite : "))
            if tab[saisie-1] == "" and saisie < 10 and saisie >= 0 :
                caseValable = True
        tab[saisie-1] = "O"

def testeVictoireHorizontale(tab, victoire) :
    for i in range(3) :
        if tab[i*3] == tab[i*3+1] and tab[i*3] == tab[i*3+2] and tab[i*3] != "" :
            victoire = True
    return victoire

def testeVictoireVerticale(tab, victoire) :
    for i in range(3) :
        if tab[i] == tab[i+3] and tab[i] == tab[i+6] and tab[i] != "" :
            victoire = True
    return victoire

def testeVictoireDiagonale(tab, victoire) :
    if ((tab[0] == tab[4] and tab[0] == tab[8]) or (tab[2] == tab[4] and tab[4] == tab[6])) and tab[4] != "" :
        victoire = True
    return victoire
    

while nbTour < 9 and victoire == False:
    testeVictoireDiagonale(tab, victoire) or testeVictoireHorizontale(tab, victoire) or testeVictoireVerticale(tab, victoire)
    if testeVictoireDiagonale(tab, victoire) == True or testeVictoireHorizontale(tab, victoire) == True or testeVictoireVerticale(tab, victoire) == True :
        victoire = True
    if victoire == False :
        print("Tour numéro : ", nbTour)
        afficheGrille(tab)
        symbole(tab, nbTour)
        nbTour = nbTour+1
        

afficheGrille(tab)
if victoire == True and nbTour%2 == 0 :
    print("Fin de la partie, félicitations X a gagné")
elif victoire == True and nbTour%2 > 0 :
    print("Fin de la partie, félicitations O a gagné")
else :
    print("Fin de la partie, égalité")