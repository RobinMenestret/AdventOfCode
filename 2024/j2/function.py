from copy import copy

def convertir_en_listes(fichier_path):
    listes = []

    with open(fichier_path, 'r') as fichier:

        for ligne in fichier:
            sequence = ligne.strip().split()
            sequence = [int(nombre) for nombre in sequence]
            listes.append(sequence)

    return listes


def j2():
    listes = convertir_en_listes("liste2.txt")
    count = 0
    for liste in listes :
        for i in range(len(liste)+1):
            listec = copy(liste)
            if i != len(liste) :
                listec.pop(i)
            safe = True
            if listec[0]<listec[1]:
                increase = True
            else :
                increase = False
            previous_number = -1
            for number in listec :
                if (previous_number != -1):
                    if (previous_number < number and not increase) or (previous_number > number and increase) or (abs(previous_number-number)<1) or (abs(previous_number-number)>3):
                        safe = False
                previous_number = number
            if safe :
                count +=1
                print(listec)
                break
    print(count)

        


j2()