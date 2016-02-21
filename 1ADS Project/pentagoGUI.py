import pygame, sys
from pygame.locals import *
import copy
pygame.init()


maSurface = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('PentagoGui')

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 50, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)


p = 5
plateau = [[0 for i in range(6)]for i in range(6)]
joueur = 1
fleche = pygame.image.load('rotation.png').convert_alpha()


def rotationgauche(m, liste, maliste90g):
    maliste90g = copy.deepcopy(liste)
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
    maliste90d = copy.deepcopy(liste)
    print("entrée dans rotation droite")
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
    global joueur
    #n : taille du plateau
    #q : numéro du quadrant à tourner
    #S : booléen qui donne le sens (TRUE = droite, FALSE = gauche)
    m = n/2
    m =int(m)
    print("la valeur de m est : ", m)
    Q1 = []
    Q2 = []
    Q3 = []
    Q4 = []
    liste = []
    maliste90d = []
    maliste90g = []
    for i in range(m):
        print(i)
        Q1.append(plateau[i][0:m])
        Q4.append(plateau[i][m:])
    #print(Q1)
    #print(Q4)
    for i in range(m, n):
        print(i)
        Q2.append(plateau[i][0:m])
        Q3.append(plateau[i][m:])
    #print(Q2)
    #print(Q3)
    if q == 1:
        liste = copy.deepcopy(Q1)
    if q == 2:
        liste = copy.deepcopy(Q2)
    if q == 3:
        liste = copy.deepcopy(Q3)
    if q == 4:
        liste = copy.deepcopy(Q4)
    print(liste)

        #1 4
        #2 3
    if S:
        tmp = rotationdroite(m, liste, maliste90d)
        print("ma liste 90d est ", maliste90d)
    else:
        tmp = rotationgauche(m, liste, maliste90g)
        print("ma liste 90g est ", maliste90g)
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
    if joueur == 1:    #tour joueur
        joueur = 2
    elif joueur == 2:
        joueur = 1    #joueur = 1 if joueur == 2 else 2
    if victoire(len(plateau), plateau, p, joueur):
        etape = 3
    return plateau


def rotation_g_d_cadre(position_souris):
    x = position_souris[0]
    y = position_souris[1]
    print(x,y)
    if 700 < x < 748 and 30 < y < 78: #zone cliquable pour rotation
        return True, 4
    elif 700 < x < 748 and 740 < y < 788: #
        return False, 3
    elif 70 < x < 118 and 30 < y < 78: #
        return False, 1
    elif 30 < x < 78 and 72 < y < 120: #
        return True, 1
    elif 30 < x < 78 and 700 < y < 748: #
        return False, 2
    elif 70 < x < 118 and 740 < y < 788:
        return True, 2
    elif 740 < x < 788 and 72 < y < 120:
        return False, 4
    elif 740 < x < 788 and 700 < y < 748:
        return True, 3


#position des fleches
def position_fleche():
    maSurface.blit(fleche, (700, 30)) #droite
    maSurface.blit(pygame.transform.flip(fleche, False, True), (700, 740)) #gauche
    maSurface.blit(pygame.transform.flip(fleche, True, False), (70, 30)) #gauche
    maSurface.blit(pygame.transform.flip((pygame.transform.rotate(fleche, 90)), False, False), (30, 72)) #droite
    maSurface.blit(pygame.transform.flip((pygame.transform.rotate(fleche, 90)), False, True), (30, 700)) #gauche
    maSurface.blit(pygame.transform.flip(fleche, True, True), (70, 740)) #droite
    maSurface.blit(pygame.transform.flip((pygame.transform.rotate(fleche, 90)), True, False), (740, 72)) #gauche
    maSurface.blit(pygame.transform.flip((pygame.transform.rotate(fleche, 90)), True, True), (740, 700)) #droite


def dessin_plateau():
    pygame.draw.rect(maSurface, BLACK, ((0, 0, 1000, 800)))

    #cadrant
    pygame.draw.rect(maSurface, RED, ((75, 75, 325, 325)))
    pygame.draw.rect(maSurface, RED, ((420, 75, 325, 325)))
    pygame.draw.rect(maSurface, RED, ((420, 420, 325, 325)))
    pygame.draw.rect(maSurface, RED, ((75, 420, 325, 325)))

    #definir position cercle
    for iy, y in enumerate(plateau):
        height_cadrant = 325
        ecart_cadrant = 20
        posy = round(75+((height_cadrant//3)*(iy+0.5)))
        if iy >= len(plateau)//2:
            posy += ecart_cadrant
        for ix, x in enumerate(y):
            posx = round(75+((height_cadrant//3)*(ix+0.5)))
            if ix >= len(plateau)//2:
                posx += ecart_cadrant
            if plateau[iy][ix] == 0:
                pygame.draw.circle(maSurface, WHITE, (posx, posy), 35, 1)
            elif plateau[iy][ix] == 1:
                pygame.draw.circle(maSurface, BLACK, (posx, posy), 35, 0)
            else:
                pygame.draw.circle(maSurface, BLUE, (posx, posy), 35, 0)


#partage cadrant
def position_pion(x, y):
    global plateau
    x, y = (x-75), (y-75)
    if x < 0 or y < 0 or x > 670 or y > 670:
        return False
    if 325 < x < 345 or 325 < y < 345:
        return False
    case = 650 // 6
    if x > 325:
        x -= 20
    if y > 325:
        y -= 20
    x, y = x//case, y//case
    if plateau[y][x] != 0:   #vérif si case prise
        return False
    return x, y


def pose_pion(position):
    global joueur
    global etape
    if not position:
        return False
    plateau[position[1]][position[0]] = joueur
    etape = 2
    if victoire(len(plateau), plateau, p, joueur):
        etape = 3


def verification_horizontale(n, plateau, p, joueur):

# cette fonction retourne vrai si on trouve p valeurs successives de j
# n = taille du plateau
# plateau = plateau à vérifier
# p = nombre de répétitions à trouver
# joueur = indice du joueur

    victoire = False
    for i in range(n):
        compteur = 0
        print("La ligne est ", i)
        for j in range(n):
            if plateau[i][j] == joueur:
                compteur += 1
                print("compteur", compteur)
                if compteur >= p:
                    victoire = True
                    print("Le joueur", joueur, "a gagne")
            else:
                compteur = 0
        # print("Compteur vaut", compteur)
    return victoire


def verification_verticale(n, plateau, p, joueur):

# cette fonction retourne vrai si on trouve p valeurs successives de j
# n = taille du plateau
# plateau = plateau à vérifier
# p = nombre de répétitions à trouver
# joueur = indice du joueur

    victoire = False
    for j in range(n):
        compteur = 0
        print("La colone est ", j)
        for i in range(n):
            if plateau[i][j] == joueur:
                compteur += 1
                print("compteur", compteur)
                if compteur >= p:
                    victoire = True
                    print("Le joueur", joueur, "a gagne")
            else:
                compteur = 0
        print("Compteur vaut", compteur)
    return victoire


def verification_diagonaleGD(n, plateau, p, joueur):

# cette fonction retourne vrai si on trouve p valeurs successives de j
# n = taille du plateau
# plateau = plateau à vérifier
# p = nombre de répétitions à trouver
# joueur = indice du joueur

    victoire = False
    for i in range(-n, n):
        compteur = 0
        j = 0
        print("La ligne est ", i)
        while i < n and j < n:
            if i >= 0 and plateau [i][j] == joueur:
                compteur += 1
                if compteur >= p:
                    print("Le joueur", joueur, "a gagne")
                    return True
            else:
                compteur = 0

            i += 1
            j += 1
            print("compteur", compteur)

    return False


def verification_diagonaleDG(n, plateau, p, joueur):

# cette fonction retourne vrai si on trouve p valeurs successives de j
# n = taille du plateau
# plateau = plateau à vérifier
# p = nombre de répétitions à trouver
# joueur = indice du joueur

    for i in range(n*2):
        compteur = 0
        t = i
        j = 0
        print("La ligne est ", i)
        while 0 <= t < n and j < n:
            if t >= 0 and plateau[t][j] == joueur:
                compteur += 1
            if compteur >= p:
                print("Le joueur", joueur, "a gagne")
                return True
            else:
                compteur = 0

            t -= 1
            j += 1
            print("compteur", compteur)

    return False

def victoire(n, plateau, p, joueur):
    # n = taille du plateau
    # plateau = plateau à vérifier
    # p = nombre de répétitions à trouver
    # joueur = indice du joueur
    if verification_diagonaleDG(n, plateau, p, joueur) or verification_horizontale(n, plateau, p, joueur) or verification_verticale(n, plateau, p, joueur) or verification_diagonaleGD(n, plateau, p, joueur):
        return True
    return False

dessin_plateau()

etape = 1

#action
inProgress = True
while inProgress:

    action = []
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if etape == 2:
                fuf = rotation_g_d_cadre(event.pos)
                if fuf:
                    plateau = rotation_plateau(6, plateau, fuf[1], fuf[0])
                    global etape
                    etape = 1
            elif etape == 1:
                pose_pion(position_pion(x, y))
    
    dessin_plateau()
    if etape == 2:
        position_fleche()

    pygame.display.update()
pygame.quit()

