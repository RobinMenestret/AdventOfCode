def part1() :
    text = open("2024/j9/input.txt", 'r').read()

    new_format = []
    compteur = 0
    for i in range(len(text)):
        if i%2 == 0 :
            for j in range(int(text[i])):
                new_format.append(compteur)
        else :
            compteur += 1
            for j in range(int(text[i])):
                new_format.append(".")
    decompte = 0
    while True:
        decompte +=1
        if new_format[-1] == "." :
            new_format.pop(-1)
        else :
            for j in range(len(new_format)):
                try :
                    if new_format[j] == ".":
                        new_format[j]=new_format[-1]
                        new_format.pop(-1)
                        break
                except :
                    pass
        #print("decompte : " +str(decompte)+ " length : " + str(len(new_format)))

        if decompte >= len(new_format):
            break
    count = 0
    for i in range(len(new_format)):
        try :
            count += i*int(new_format[i])
        except :
            pass
    print(count)

def part2() :
    text = open("2024/j9/input.txt", 'r').read()

    new_format = []
    compteur = 0
    for i in range(len(text)):
        if i%2 == 0 :
            for j in range(int(text[i])):
                new_format.append(compteur)
        else :
            compteur += 1
            for j in range(int(text[i])):
                new_format.append(".")
    #new_format = list("00...111...2...333.44.5555.6666.777.888899")
    print(new_format)
    # new_format nous donne la liste avec les . et les ids
    decompte = 0
    actual_number = "&"
    current_last_pos = 1
    while True:
        decompte += 1
        if new_format[-current_last_pos] in [".", actual_number] :
            current_last_pos += 1        
        else :
            actual_number = new_format[-current_last_pos]
            findall = 1
            while new_format[-findall-current_last_pos] == actual_number: # determine la taille de la séquence
                findall += 1
            
            length = len(new_format)
            for j in range(length-current_last_pos):
                if new_format[j:j+findall] == ['.']*findall :
                    new_format[j:j+findall] = [actual_number]*findall
                    if current_last_pos == 1:
                        new_format[-findall-current_last_pos+1:] = ["."]*len(new_format[-findall-current_last_pos+1:])
                    else :
                        new_format[-findall-current_last_pos+1:-current_last_pos+1] = ["."]*len(new_format[-findall-current_last_pos+1:-current_last_pos+1])
                    
                    # print(''.join(new_format))
                    break
        # print("decompte : " +str(decompte)+ " length : " + str(len(new_format)))
        #print(new_format[:100])
        #print(new_format[-100:])
        #print("decompte : " +str(decompte)+ " length : " + str(len(new_format)))
        if decompte >= len(new_format) or len(new_format)== 67795:
            break
    count = 0
    for i in range(len(new_format)):
        try :
            count += i*int(new_format[i])
        except :
            pass
    
    print(count)


def part2_better():
    text = [int(x) for x in list(open("2024/j9/input.txt", 'r').read())]
    text = [int(x) for x in list('2333133121414131402')]
    fullfill = text[::2]
    revert_fullfill = list.copy(fullfill)
    revert_fullfill.reverse()
    empty = text[1::2]
    #print(revert_fullfill)
    count = 0
    compteur = len(text)//2
    for nombre in range(len(revert_fullfill)):
        done = False
        for espace in range(len(empty)):
            if revert_fullfill[nombre] <= empty[espace]:
                empty[espace] -= revert_fullfill[nombre]
                id = sum(text[:espace])
                count += compteur*revert_fullfill[nombre]*(id+((revert_fullfill[nombre]-1)/2)) # ajout de tous les termes d'un coup
                done = True
                break
        if not done :
            id = sum(text[:-nombre])
            count += compteur*revert_fullfill[nombre]*(id+((revert_fullfill[nombre]-1)/2))
    print(count)

def part2_better_bis():
    text = [int(x) for x in list('2333133121414131402')]
    fullfill = text[::2]
    revert_fullfill = list.copy(fullfill)
    revert_fullfill.reverse()
    empty = text[1::2]
    #print(revert_fullfill)
    count = 0
    compteur = len(text)//2
    for nombre in range(len(revert_fullfill)):
        done = False
        for espace in range(len(empty)):
            if revert_fullfill[nombre] <= empty[espace]:
                empty[espace] -= revert_fullfill[nombre]
                id = sum(text[:espace])
                count += compteur*revert_fullfill[nombre]*(id+((revert_fullfill[nombre]-1)/2)) # ajout de tous les termes d'un coup
                done = True
                break
        if not done :
            id = sum(text[:-nombre])
            count += compteur*revert_fullfill[nombre]*(id+((revert_fullfill[nombre]-1)/2))
    print(count)


part2_better_bis()