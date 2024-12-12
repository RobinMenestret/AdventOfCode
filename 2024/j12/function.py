text = open("2024/j12/input.txt").read()
input=[[]]
ligne = 0
for i in range(len(text)):  
    
    if text[i] == "\n":
        input.append([])
        ligne +=1
    else :
        input[ligne].append(text[i])

def next_cells(previous_cell, visited_cells, perimeter):
    directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
    value = input[previous_cell[0]][previous_cell[1]]
    for direction in directions:
        next_cell = [previous_cell[0]+direction[0],previous_cell[1]+direction[1]]
        if next_cell not in visited_cells :
            if (next_cell[0]<len(input) 
                and next_cell[1] <len(input[0]) 
                and next_cell[0]>=0 
                and next_cell[1] >=0
                and input[next_cell[0]][next_cell[1]] == value 
                ):

                    visited_cells.append(next_cell)
                    visited_cells, perimeter = next_cells(next_cell, visited_cells, perimeter)
            else:
                perimeter.append((next_cell, direction))

    return visited_cells, perimeter
            
def p1():   
    zones = []
    count = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            already_done = False
            for zone in zones :
                if [i, j] in zone[0] :
                    already_done = True
            if not already_done :
                current_zone = [[i, j]]
                perimeter = []
                current_zone, perimeter = next_cells([i,j], current_zone, perimeter)
                #print("area : {} et perimeter : {}".format(len(current_zone), len(perimeter)))
                count += len(current_zone)*len(perimeter)
                zones.append([current_zone, perimeter])
    return zones


def p2():
    directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
    zones = p1()
    count = 0
    for zone in zones :
        sides = 0
        barriere_done = []
        for barriere in zone[1]:
            found = 0
            for direction in directions:
                if ([barriere[0][0]+direction[0],barriere[0][1]+direction[1]], barriere[1]) in barriere_done :
                    found += 1 
            if found == 0 :    
                sides += 1
                #print(barriere)
            elif found == 2 :
                sides -= 1
            barriere_done.append(barriere)
        count += sides*len(zone[0])     
        print("le nombre de coté est {} x {} = {} pour le groupe des {}".format(len(zone[0]), sides, len(zone[0])*sides, input[zone[0][0][0]][zone[0][0][1]]))
    print(count)

p2()