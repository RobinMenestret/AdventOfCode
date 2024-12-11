import time
import math

def part1():
    list_of_number = [554735, 45401, 8434, 0, 188, 7487525, 77, 7]
    count = 0
    for i in range(15):
        count += 1
        new_list = []
        for number in list_of_number:
            if number == 0:
                new_list.append(1)
            elif int(math.log10(number))%2 == 1:
                new_list.append(int(number//(10**(math.log10(number)//2+1))))
                new_list.append(int(number%(10**(math.log10(number)//2+1))))
            else :
                new_list.append(number*2024)
        list_of_number = list.copy(new_list)
    return list_of_number 


def step1(number):
    new_list = {}
    if number == 0:
        new_list[1] = 1
    elif int(math.log10(number))%2 == 1:
        new_list[int(number//(10**(math.log10(number)//2+1)))] = 1
        second = int(number%(10**(math.log10(number)//2+1)))
        if second not in new_list.keys() :
            new_list[second] = 1
        else :
            new_list[second] = 2 
    else :
        new_list[number*2024] = 1
    return new_list

def other_way(blinks):
    list_of_number = {45401:1, 8434:1, 0:1, 188:1, 7487525:1, 77:1, 7:1}
    dictionnaire = {}
    for i in range(blinks):
        new_list = {}
        for number in list_of_number.keys():
            if number not in dictionnaire.keys() :
                dictionnaire[number] = step1(number)
            for key in dictionnaire[number].keys():
                    if key in new_list.keys():
                        new_list[key] += dictionnaire[number][key]*list_of_number[number]
                    else :
                        new_list[key] = dictionnaire[number][key]*list_of_number[number]
        list_of_number = dict.copy(new_list)
    count = 0
    for key in list_of_number.keys():
        count += list_of_number[key]
    return len(dictionnaire.keys())
t0 = time.time()
y = []
for blinks in range(100):
    y.append(other_way(blinks))
print("computation time : {} ms".format(int((time.time()-t0)*1000)))


import matplotlib.pyplot as plt
import numpy as np

# Liste des valeurs de x allant de 1 à 100
x_values = list(range(1, 101))

# Exemple de fonction : y = x^2
def function(x):
    return x ** 2


# Tracer la courbe
plt.figure(figsize=(10, 6))
plt.plot(x_values, y, color="blue")

# Ajouter des labels et un titre
plt.xlabel("nb de blinks")
plt.ylabel("nb de valeurs possible sur une pierre")
plt.legend()

# Afficher la grille
plt.grid(True)

# Afficher le graphique
plt.show()
