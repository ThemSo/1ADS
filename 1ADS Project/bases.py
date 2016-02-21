def plateau0 (n) :
    liste1 = []
    liste = []
    i = 0
    #génération des lignes
    while i < n :
        liste1.append(0)
        i += 1
    i = 0
   #génération du tableau
    while i < n :
        liste.append(liste1)
        i += 1
    return (liste)
def affichage_liste (l) :
    #affichage sous forme de tableau
     i = 0
     while i < n :
        print(l[i])
        i +=1

#déroulement du programme
plateau= []
n = input("Nombre de lignes et de colonnes a afficher ?")
n = int(n)
plateau0(n)
affichage_liste(plateau0(n))
