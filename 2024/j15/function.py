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

map = text_to_table(open("2024/j15/map-demo1.txt", 'r').read())
moves = open ("2024/j15/moves-demo1.txt", 'r').read()

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
        #print('\n'.join([''.join(x) for x in map]))
        #a = input()
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

def move_bloc_bis(bloc, dir, map):
    horiz = True if dir[0] == 0 else False
    next_bloc = [bloc[0]+dir[0], bloc[1]+dir[1]]
    print(map[next_bloc[0]][next_bloc[1]])
    if map[next_bloc[0]][next_bloc[1]] == '[':
        if move_bloc_bis(next_bloc, dir, map) and (horiz or move_bloc_bis([next_bloc[0], next_bloc[1]+1], dir, map)):
            map[next_bloc[0]][next_bloc[1]] = map[bloc[0]][bloc[1]]
            map[bloc[0]][bloc[1]] = "."
            return True
        else :
            return False
    elif map[next_bloc[0]][next_bloc[1]] == ']':
        if move_bloc_bis(next_bloc, dir, map) and (horiz or move_bloc_bis([next_bloc[0], next_bloc[1]-1], dir, map)):
            if move_bloc_bis([bloc[0], bloc[1]-1], dir, map):
                map[next_bloc[0]][next_bloc[1]] = map[bloc[0]][bloc[1]]
                map[bloc[0]][bloc[1]] = "."
                return True
            else :
                return False
        else :
            return False
    elif map[next_bloc[0]][next_bloc[1]] == '#':
        return False
    elif map[next_bloc[0]][next_bloc[1]] == '.':
        map[next_bloc[0]][next_bloc[1]] = map[bloc[0]][bloc[1]]
        map[bloc[0]][bloc[1]] = "."
        return True
     
def part2():
    map = new_map()
    current_pos = find_init(map)
    print('\n'.join([''.join(x) for x in map]))
    
    for i in range(len(moves)):
        map_m1 = list.copy(map)
        arrow = moves[i] 
        arrow = input()
        print(arrow)
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
        horiz = True if dir[0] == 0 else False
        #input()
        next_pos = [current_pos[0]+dir[0], current_pos[1]+dir[1]]
        move = False
        if horiz :
            if map[next_pos[0]][next_pos[1]]== ".":
                move = True
            print(map[next_pos[0]][next_pos[1]]in ['[', ']'])
            if map[next_pos[0]][next_pos[1]]in ['[', ']'] and move_bloc_bis(next_pos, dir, map):
                move = True
            elif map[next_pos[0]][next_pos[1]]== "#":
                move = False
            if move :
                map[current_pos[0]][current_pos[1]] = '.'
                map[next_pos[0]][next_pos[1]] = '@'
                current_pos = next_pos
        else :
            if map[next_pos[0]][next_pos[1]]== ".":
                move = True
            elif map[next_pos[0]][next_pos[1]] == "[" and move_bloc_bis(next_pos , dir, map) and move_bloc_bis([next_pos[0], next_pos[1]+1], dir, map):
                move = True
            elif map[next_pos[0]][next_pos[1]] == "]" and move_bloc_bis(next_pos , dir, map) and move_bloc_bis([next_pos[0], next_pos[1]-1], dir, map):
                move = True
            elif map[next_pos[0]][next_pos[1]]== "#":
                move = False
            if move :
                map[current_pos[0]][current_pos[1]] = '.'
                map[next_pos[0]][next_pos[1]] = '@'
                current_pos = next_pos
        print('\n'.join([''.join(x) for x in map]))
    count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "[":
                count += 100*i + j
    return count

print(part2())