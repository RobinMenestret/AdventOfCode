import keyboard
import time

def manual():
    time.sleep(0.1)
    while True :
        if keyboard.is_pressed('up'):
            return "^"
        elif keyboard.is_pressed('down'):
            return "v"
        elif keyboard.is_pressed('left'):
            return "<"
        elif keyboard.is_pressed('right'):
            return ">"
        elif keyboard.is_pressed('q'):
            quit()
            break



def text_to_table(text):
    table=[[]]
    ligne = 0
    for i in range(len(text)):    
        if text[i] == "\n":
            table.append([])
            ligne +=1
        else :
            table[ligne].append(text[i])
    return table

map = text_to_table(open("2024/j15/map.txt", 'r').read())
moves = open ("2024/j15/moves.txt", 'r').read()

def find_init(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                return [i, j]

def move_bloc(bloc, dir):
    next_bloc = [bloc[0]+dir[0], bloc[1]+dir[1]]
    if map[next_bloc[0]][next_bloc[1]] == 'O':
        if move_bloc(next_bloc, dir):
            map[next_bloc[0]][next_bloc[1]] = 'O'
            return True
        else :
            return False
    elif map[next_bloc[0]][next_bloc[1]] == '#':
        return False
    elif map[next_bloc[0]][next_bloc[1]] == '.':
        map[next_bloc[0]][next_bloc[1]] = 'O'
        return True

def part1():
    current_pos = find_init(map)
    for i in range(len(moves)):
        #print(moves[i])
        if moves[i] == "<":
            dir = [0, -1]
        elif moves[i] == "^":
            dir = [-1, 0]
        elif moves[i] == ">":
            dir = [0, 1]
        elif moves[i] == "v":
            dir = [1, 0]
        else :
            continue
        next_pos = [current_pos[0]+dir[0], current_pos[1]+dir[1]]
        move = False
        if map[next_pos[0]][next_pos[1]] == ".":
            move = True
        elif map[next_pos[0]][next_pos[1]]== "O" and move_bloc(next_pos, dir):
            move = True
        elif map[next_pos[0]][next_pos[1]]== "#":
            move = False
        if move :
            map[current_pos[0]][current_pos[1]] = '.'
            map[next_pos[0]][next_pos[1]] = '@'
            current_pos = next_pos
        print('\n'.join([''.join(x) for x in map]))
        a = input()
    count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O":
                count += 100*i + j
    return count

def new_map():
    new_map = [['.'] * 2 * len(map[0]) for _ in range(len(map))]
    print(new_map)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "#":
                new_map[i][2*j] = "#"
                new_map[i][2*j+1] = "#"
            if map[i][j] == "O":
                new_map[i][2*j] = "["
                new_map[i][2*j+1] = "]"
            if map[i][j] == "@":
                new_map[i][2*j] = "@"
                new_map[i][2*j+1] = "."
            if map[i][j] == ".":
                new_map[i][2*j] = "."
                new_map[i][2*j+1] = "."
    #print('\n'.join([''.join(x) for x in new_map]))
    return new_map

def move_bloc_bis(couple, bloc, dir, map):
    list_to_move = [bloc]
    move = True
    next_bloc = [bloc[0]+dir[0], bloc[1]+dir[1]]
    if map[bloc[0]][bloc[1]] == '[':
        if not couple :
            move, liste = move_bloc_bis(True, [bloc[0], bloc[1]+1], dir, map)
            list_to_move.extend(liste)
    else :
        if not couple :
            move, liste = move_bloc_bis(True, [bloc[0], bloc[1]-1], dir, map)
            list_to_move.extend(liste)
    if not move :
        return False, []
    
    if map[next_bloc[0]][next_bloc[1]] in ['[', ']'] and next_bloc not in list_to_move:
        move, liste = move_bloc_bis(False, next_bloc, dir, map)
        list_to_move.extend(liste)
        if move :
            return True, list_to_move
        else :
            return False, []
    elif map[next_bloc[0]][next_bloc[1]] == '#':
        return False, []
    elif map[next_bloc[0]][next_bloc[1]] == '.':
        list_to_move.append(bloc)
        return True, list_to_move
    else :
        return True, list_to_move
 

def part2():
    map = new_map()
    current_pos = find_init(map)
    print('\n'.join([''.join(x) for x in map]))
    
    for i in range(len(moves)):
        arrow = moves[i] 
        arrow = manual()
        #time.sleep(50)
        #print(arrow)
        if arrow == "<":
            dir = [0, -1]
        elif arrow == ">":
            dir = [0, 1]
        elif arrow == "^":
            dir = [-1, 0]
        elif arrow == "v":
            dir = [1, 0]
        else :
            continue
        #input()
        next_pos = [current_pos[0]+dir[0], current_pos[1]+dir[1]]
        move = False
        if map[next_pos[0]][next_pos[1]]== ".":
            move, list_to_move = True, []
        elif map[next_pos[0]][next_pos[1]] == "[" :
            move, list_to_move = move_bloc_bis(False, next_pos , dir, map)
        elif map[next_pos[0]][next_pos[1]] == "]" :
            move, list_to_move = move_bloc_bis(False, next_pos , dir, map)
        elif map[next_pos[0]][next_pos[1]]== "#":
            move, list_to_move = False, []
        if move :
            list_to_move.append(current_pos)
            temp_map = []
            for i in range(len(map)):
                temp_map.append([])
                for j in map[i]:
                    temp_map[i].append(j) 
            passed_elt = []
            for elt in list_to_move : 
                map[elt[0]][elt[1]] = '.'
            for elt in list_to_move : 
                if elt not in passed_elt :
                    passed_elt.append(elt)
                    map[elt[0]+dir[0]][elt[1]+dir[1]] = temp_map[elt[0]][elt[1]]
            current_pos = next_pos
        print('\n'.join([''.join(x) for x in map]))
    count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "[":
                count += 100*i + j
    return count

print(part2())