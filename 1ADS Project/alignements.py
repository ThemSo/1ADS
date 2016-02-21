def verification_horizontale(n, plateau, p, joueur) :

# cette fonction retourne vrai si on trouve p valeurs successives de j
# n = taille du plateau
# plateau = plateau à vérifier
# p = nombre de répétitions à trouver
# joueur = indice du joueur

    victoire = False
    for i in range (n) :
        compteur = 0
        for j in range (n) :
            if plateau [i][j] == joueur :
                compteur += 1
                if compteur >= p :
                    victoire = True
                    print("Le joueur", joueur, "a gagne")
            else :
                compteur = 0
        # print("Compteur vaut", compteur)
    return victoire

def verification_verticale(n, plateau, p, joueur) :

# cette fonction retourne vrai si on trouve p valeurs successives de j
# n = taille du plateau
# plateau = plateau à vérifier
# p = nombre de répétitions à trouver
# joueur = indice du joueur

    victoire = False
    for j in range (n) :
        compteur = 0
        for i in range (n) :
            if plateau [i][j] == joueur :
                compteur += 1
                if compteur >= p :
                    victoire = True
                    print("Le joueur", joueur, "a gagne")
            else :
                compteur = 0
        # print("Compteur vaut", compteur)
    return victoire

def verification_diagonaleGD(n, plateau, p, joueur) :

# cette fonction retourne vrai si on trouve p valeurs successives de j
# n = taille du plateau
# plateau = plateau à vérifier
# p = nombre de répétitions à trouver
# joueur = indice du joueur*
# j'ai trouvé un pion du joueur
# je parcours les P cases de la diagonale GD à partir de ce pion pour voir si il y a P pions alignés
# les indices de parcours sont : l = incrément de ligne et c = incrément de colonne


    victoire = False
    for i in range (n-p +1) :
        compteur = 0
        for j in range (n-p +1) :
            if plateau [i][j] == joueur :
                compteur = 1
                for l in range (p -1) :
                    l += 1
                    if plateau [i+l][j+l] == joueur :
                            compteur += 1
                if compteur == p :
                    victoire = True
                    print("Le joueur", joueur, "a gagne")
        break
    return victoire

def verification_diagonaleDG(n, plateau, p, joueur) :

# cette fonction retourne vrai si on trouve p valeurs successives de j
# n = taille du plateau
# plateau = plateau à vérifier
# p = nombre de répétitions à trouver
# joueur = indice du joueur*
# j'ai trouvé un pion du joueur
# je parcours les P cases de la diagonale GD à partir de ce pion pour voir si il y a P pions alignés
# les indices de parcours sont : l = incrément de ligne et c = incrément de colonne


    victoire = False
    for i in range (n-p) :
        compteur = 0
        for j in range (n-p) :
            if plateau [n-i-1][n-j-1] == joueur :
                compteur = 1
                for l in range (p -1) :
                    l += 1
                    if plateau [n-i-l][n-j-l] == joueur :
                            compteur += 1
                if compteur == p :
                    victoire = True
                    print("Le joueur", joueur, "a gagne")
        break
    return victoire

plateau = [
[0, 0, 1, 0, 0, 1],
[0, 0, 0, 1, 1, 0],
[0, 1, 0, 1, 1, 0],
[0, 0, 1, 1, 0, 1],
[0, 0, 0, 1, 0, 1],
[1, 1, 0, 0, 1, 0] ]
n = 6
p = 4
joueur = 0
#P = input("La valeur de p ?")
# p = int(p)
joueur = input("La valeur du joueur ?")
joueur = int(joueur)
victoire = False
victoire = verification_diagonaleGD(n, plateau, p, joueur)

