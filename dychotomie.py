# l'erreur "wrong logique" (quand la fonction réponds plus et que l'opérateur donne une valeur plus petite ou l'inverse) est bugger
#probablement a cause des variables interne des cellules qui sont vidé et donc inutilisable d'une fonction sur l'autre, check capture d'ecran9 pour solver le pb

import random
nmList = [0]
nombre_game = 1
l100=(range(1,101))
print("J'ai choisi un nombre entre 1 et 100, par dychotomie tu dois le trouver, je ne répondrai que par plus ou moins")
continuer = True
while continuer:
    wincond=0
    def randomi():
        nm = random.randint(1, 100)
        while nm in nmList:
            nm1 = random.randint(1, 100)
            nm = nm1
        nmList.append(nm)
        #print(nmList)
        return int(nm)
    nm=randomi()

    l100 = (range(1, 101))


    tour = True
#    indice=0
    awnserList=[0]
    def var():
            my_var = int(input("choisissez un nombre : "))
            tempVar = my_var
#            def wrongLogik(K):
#                if (K<=awnserList(-1)) and (indice>=0):
#                    print(f"j'ai dis que le nombre est PLUS grand que {tempVar}")
#                    return 1
#                if (K>=awnserList(-1)) and (indice<=0):
#                    print(f"J'ai dis que le nombre est MOINS grand que {tempVar}")
#                    return 1
#                elif ((K<=awnserList(-1)) and (indice<=0)) or ((K>=awnserList(-1)) and (indice>=0)):
#                    return 0
#                return wrongLogik(K)
            def wrongKey(K):
                for i in K:
                    if tempVar == K[i]:
                        return 0
                    elif tempVar not in K:
                        return 1
                return wrongKey
            l100 = (range(1, 101))
            if wrongKey(l100)==1:
                print("Votre entrée n'est pas un entier compris entre 1 et 100")
                return 0
#            elif (wrongKey(l100)==0) and (wrongLogik(tempVar)==0):
#                awnserList.append(my_var)
#                print(awnserList)########################################" à retirer
            if (my_var < nm) ==1:
                print("plus")
#                indice = 2
                return 0#, indice
            if (my_var > nm) ==1:
                print("moins")
#                indice = -2
                return 0#, indice
            elif my_var==nm:
                print(f"Bien joué mon nombre était bien {nm}!")
            return 1


    while tour:
        variable=var()
        if variable:
            tour = False

    def nbgame(nombre_game):
        if variable==1:
            nombre_game = nombre_game +1
            return nombre_game
    nbG = nbgame(nombre_game)

    if nbG == 99:
        continuer = False
    if variable==1:
        awnser = input("voulez-vous rejouer ? (oui/non) : ")
        if awnser not in ('oui'):
            continuer = False


