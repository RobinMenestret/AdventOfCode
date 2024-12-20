from astar.search import AStar

def maze(text):
    map = [[0 if elt == '.' else 1 if elt == '#' else elt for elt in line]for line in [list(line) for line in text.split('\n')]]
    start = 0
    end = 0
    for line in range(len(map)) :
        for elt in range(len(map[line])) :
            if map[line][elt] == 'S':
                start = (line, elt)
                map[line][elt] = 0
            elif map[line][elt] == 'E':
                end = (line, elt)
                map[line][elt] = 0
    return map, start, end


def dn(corpus):
    file = open('2024/j20/'+ corpus + '.txt', 'r').read()
    return maze(file)


def part1_naive():
    corpus = "input"
    maze, start, end = dn(corpus)
    #print("\n".join([''.join([str(x) for x in line]) for line in maze]))
    path = AStar(maze).search(start, end)
    based_len = len(path)-1
    saves = {}
    count = 0
    for line in range(len(maze))[1:-1]:
        for elt in range(len(maze[line]))[1:-1]:
            if maze[elt][line] == 1 and ((maze[elt-1][line], maze[elt+1][line]) == (0, 0) or (maze[elt][line-1], maze[elt][line+1]) == (0, 0)):
                maze[elt][line] = 0
                path = AStar(maze).search(start, end)
                maze[elt][line] = 1
                cheat = based_len-len(path)+1
                if cheat >= 100:
                    count +=1
                    if cheat in saves.keys():
                        saves[cheat] += 1
                    else :
                        saves[cheat] = 1
                        
        print(saves)    
        print("ligne {} : raccourcis > 100 trouvés : {}".format(line,count))      
    
def part1():
    corpus = "input"
    maze, start, end = dn(corpus)
    print("\n".join([''.join([str(x) for x in line]) for line in maze])) 
    path = AStar(maze).search(start, end)
    print(path)
    for cell in range(len(path)):
        maze[path[cell][0]][path[cell][1]] = cell+2
    print("\n".join(['\t'.join([str(x) for x in line]) for line in maze]))
    saves = {}
    count = 0
    for line in range(len(maze))[1:-1]:
        for elt in range(len(maze[line]))[1:-1]:
            if maze[elt][line] == 1:
                if maze[elt-1][line]>1 and maze[elt+1][line]>1 and abs(maze[elt-1][line]-maze[elt+1][line])>100:
                    count +=1
                if maze[elt][line-1]>1 and maze[elt][line+1]>1 and abs(maze[elt][line-1]-maze[elt][line+1])>100:
                    count +=1
    print(count)

def part2():
    corpus = "input"
    maze, start, end = dn(corpus)
    print("\n".join([''.join([str(x) for x in line]) for line in maze])) 
    path = AStar(maze).search(start, end)
    print(path)
    for cell in range(len(path)):
        maze[path[cell][0]][path[cell][1]] = cell+2
    print("\n".join(['\t'.join([str(x) for x in line]) for line in maze]))
    saves = {}
    count = 0
    max = 100
    for cell1 in path :
        for cell2 in path:
            cheat = maze[cell2[0]][cell2[1]]-maze[cell1[0]][cell1[1]]-(abs(cell1[0]-cell2[0])+abs(cell1[1]-cell2[1]))
            if cheat >= max and (abs(cell1[0]-cell2[0])+abs(cell1[1]-cell2[1])) <= 20:
                count+=1
                if cheat in saves.keys():
                    saves[cheat] += 1
                else :
                    saves[cheat] = 1
    print(count)
    print(saves)
part2()

