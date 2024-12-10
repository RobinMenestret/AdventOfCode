def part1():
    text = open('2024/j10/input.txt','r').read()
    table=[[]]
    ligne = 0
    for i in range(len(text)):  
        
        if text[i] == "\n":
            table.append([])
            ligne +=1
        else :
            table[ligne].append(int(text[i]))
    print(table)
    inputs = []
    nb_de_neuf = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 0:
                inputs.append([i,j])
                print("un point de depart!")
                actual_cell = [i,j]
                actual_value = 0
                next_cells = [actual_cell]
                actual_cells = []
                while True :
                    actual_cells = list.copy(next_cells)
                    next_cells = []
                    for cell in actual_cells:
                        for direction in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                            if cell[0]+direction[0]< len(table) and cell[1]+direction[1] < len(table[0]) and cell[0]+direction[0]>=0 and cell[1]+direction[1] >=0 :
                                if table[cell[0]+direction[0]][cell[1]+direction[1]] == actual_value + 1 :
                                    # commented for part 2 XD : 
                                    if [cell[0]+direction[0], cell[1]+direction[1]] not in next_cells:
                                        next_cells.append([cell[0]+direction[0], cell[1]+direction[1]])
                    if actual_value == 9:
                        break
                    
                    if next_cells != []:
                        actual_value +=1
                    else :
                        print("on ne va pas plus loin que : " + str(actual_value))
                        break
                nb_de_neuf += len(actual_cells)
    print(nb_de_neuf)
part1()