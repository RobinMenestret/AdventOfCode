import sys
sys.setrecursionlimit(5000)

text = open('2024/j16/input.txt', 'r').read()

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

def new_value(maze, previous_cell, current_cell, value):
    end = False
    dir  = [current_cell[0]-previous_cell[0], current_cell[1]-previous_cell[1]]
    if maze[current_cell[0]][current_cell[1]] == "E":
        maze[current_cell[0]][current_cell[1]] = str(value + 1)
        print("Trouvé !")
        end = True
    elif maze[current_cell[0]][current_cell[1]] == '#' or maze[current_cell[0]][current_cell[1]] == 'S':
        pass
    elif maze[current_cell[0]][current_cell[1]] == '.' or int(maze[current_cell[0]][current_cell[1]]) > value + 1 :
        maze[current_cell[0]][current_cell[1]] = str(value + 1)
        #print('\n'.join([''.join(x) for x in maze]))
        #input()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if end : 
            return
        for direction in directions:
            if direction == dir :
                new_value(maze, current_cell, [current_cell[0]+direction[0], current_cell[1]+direction[1]], value + 2001)
            if direction[0] == -dir[0] or direction[1] == -dir[1] :
                new_value(maze, current_cell, [current_cell[0]+direction[0], current_cell[1]+direction[1]], value + 1)
            else :
                new_value(maze, current_cell, [current_cell[0]+direction[0], current_cell[1]+direction[1]], value + 1001)
def part1():
    maze = text_to_table(text)
    begin = [len(maze)-2, 1]
    maze[begin[0]][begin[1]] = '0'
    print(maze[begin[0]][begin[1]])
    new_value(maze, begin, [begin[0]-1, begin[1]], 1000)

    # for i in range(len(maze)):
    #     for j in range(len(maze[0])):
    #         if maze[i][j] == "#":
    #             maze[i][j] = "####"

    print('\n'.join([' '.join(x) for x in maze]))
    print(maze[1][len(maze)-2])
    return maze



def find_path(maze, liste, current_cell): 
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    liste.append(current_cell)
    #print(current_cell)
    for direction in directions :
        #print([current_cell[0]+direction[0],current_cell[1]+direction[1]])
        if maze[current_cell[0]+direction[0]][current_cell[1]+direction[1]] not in ["#", "."] :
            if [current_cell[0]+direction[0],current_cell[1]+direction[1]] not in liste :
                if int(maze[current_cell[0]+direction[0]][current_cell[1]+direction[1]]) < int(maze[current_cell[0]][current_cell[1]]) or int(maze[current_cell[0]+direction[0]][current_cell[1]+direction[1]]) == int(maze[current_cell[0]][current_cell[1]])+999 :
                    liste = find_path(maze, liste,[current_cell[0]+direction[0],current_cell[1]+direction[1]])
    return liste
def part2():
    maze = part1()
    begin = [1, len(maze)-2]
    liste = find_path(maze, [], begin)
    print(liste)
    print(len(liste))
    for i in range(len(maze)) :
        for j in range(len(maze[0])):
            maze[i][j] = "+" if [i, j] in liste else "." if maze[i][j] != "#" else "#"
    print('\n'.join([' '.join(x) for x in maze]))



part2()