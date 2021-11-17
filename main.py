tableau = ["","","","","","","","",""]
complet = False
victoire = False
tour = 0

while complet == False and victoire == False :
    if tour > 8 :
        complet = True
    for i in range(len(tableau)) :
        if (tableau[0] == tableau[4] and tableau[0] == tableau[8]) or (tableau[2] == tableau[4] and tableau[2] == tableau[6]) and tableau[4] !="" or (tableau[i*3] == tableau[i*3+3] and tableau[i*3] == tableau[i*3+6] and tableau[i] !="") or (tableau[i*3] == tableau[i*3+1] and tableau[i*3] == tableau[i*3+2] and tableau[i] !="") :
            victoire = True
    for i in range(9):
        for j in range(2):
            print(tableau[j],"|")
            i=i+1
        print(tableau[i],"\n")
        for k in range(3):
            print("_")
        print("","\n")
        for j in range(2):
            print(tableau[j+3],"|")
            i=i+1
        print(tableau[i],"\n")
        for k in range(3):
            print("_")
        print("","\n")
        for j in range(2):
            print(tableau[j+6],"|")
            i=i+1
        print(tableau[i],"\n")
        for k in range(3):
            print("_")
        print("","\n")


        
