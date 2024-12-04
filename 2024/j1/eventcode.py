
def separer_listes():
    liste_1 = []
    liste_2 = []
    fichier_path = 'liste.txt' 

    with open(fichier_path, 'r') as fichier:
        for ligne in fichier:
            nombres = ligne.split()
            if len(nombres) == 2: 
                liste_1.append(nombres[0])
                liste_2.append(nombres[1])

    return liste_1, liste_2


def j1_1():
    liste_1, liste_2 = separer_listes()

    liste_1.sort()
    liste_2.sort()

    print("Liste 1:", liste_1)
    print("Liste 2:", liste_2)

    compteur = 0

    for i in range(1000):
        compteur += abs(int(liste_1[i])-int(liste_2[i]))

    print(compteur)

def j1_2():
    liste_1, liste_2 = separer_listes()
    similarity = 0
    for i in liste_1 :
        occurs = 0
        for j in liste_2 :
            if i == j :
                occurs += 1
        similarity += int(i)*occurs
    print(similarity)

