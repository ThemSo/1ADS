def rotationgauche(m, liste, maliste90g):
    # cette fonction fait tourner de 90 degres vers la gauche la liste "liste"
    # m = taille de la liste a tourner
    # liste = liste a tourner
    maliste90g = copy.deepcopy(liste)
    # on utilise deep.copy pour désolidariser les listes
    i = 0
    u = 0
    while i < m:
        j = 0
        while j < m:
            u = m - 1 - i
            maliste90g[i][j] = liste[j][u]
            j = j + 1
        i = i + 1
    return maliste90g


def rotationdroite(m, liste, maliste90d):
    # cette fonction fait tourner de 90 degres vers la droite la liste "liste"
    # m = taille de la liste a tourner
    # liste = liste a tourner
    maliste90d = copy.deepcopy(liste)
    # on utilise deep.copy pour désolidariser les listes
    i = 0
    u = 0
    while i < m:
        j = 0
        while j < m:
            u = m - j -1
            maliste90d[i][j] = liste[u][i]
            j = j +1
        i = i +1
    return maliste90d


def rotation_plateau(n, plateau, q, S):
    # Cette fonction fait tourner le quadrant q du plateau "plateau" dans le sens S
    # Plateau = plateau a traiter
    #n : taille du plateau
    #q : numéro du quadrant à tourner
    #S : booléen qui donne le sens (TRUE = droite, FALSE = gauche)
    m = n/2
    m =int(m)
    Q1 = []
    Q2 = []
    Q3 = []
    Q4 = []
    # la variable Qi accueille le quadrant i
    # extraction des quadrants
    liste = []
    maliste90d = []
    maliste90g = []
    for i in range(m):
        print(i)
        Q1.append(plateau[i][0:m])
        Q4.append(plateau[i][m:])
    for i in range(m, n):
        print(i)
        Q2.append(plateau[i][0:m])
        Q3.append(plateau[i][m:])
        # Copie du quadrant a tourner dans la liste de travail "liste"
    if q == 1:
        liste = copy.deepcopy(Q1)
    if q == 2:
        liste = copy.deepcopy(Q2)
    if q == 3:
        liste = copy.deepcopy(Q3)
    if q == 4:
        liste = copy.deepcopy(Q4)
    print(liste)
    # Rotation du quadrant
    if S:
        tmp = rotationdroite(m, liste, maliste90d)
        print("ma liste 90d est ", maliste90d)
    else:
        tmp = rotationgauche(m, liste, maliste90g)
        print("ma liste 90g est ", maliste90g)
        # Reconstitution de la liste
    for y in range(0, n//2):
        for x in range(0, n//2):
            posx = x
            posy = y
            if q == 4 or q == 3:
                posx += n//2
            if q == 2 or q == 3:
                posy += n//2

            plateau[posy][posx] = tmp[y][x]
    print(plateau)
    return plateau

from random import randint
import copy
plateau = [[randint(0,2) for j in range(8)] for i in range(8)]
print("plateau avant rotation : ", plateau)
n = 8
q = 8
while q > 4 or q <1 :
    q = input("Numero du quadrant a tourner : ")
    q = int(q)
S = True
Sens = 4
while Sens > 2 or Sens < 1 :
    Sens = input("Donner le sens de rotation (1 = DROITE , 2 = GAUCHE) ")
    Sens = int(Sens)
    if Sens is 2:
        S = False

rotation_plateau (n,plateau,q,S)

import copy
p = 5
plateau = [[0 for i in range(6)]for i in range(6)]
joueur = 1