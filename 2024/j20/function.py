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


def part1():
    corpus = "input"
    maze, start, end = dn(corpus)
    #print("\n".join([''.join([str(x) for x in line]) for line in maze]))
    path = AStar(maze).search(start, end)
    based_len = len(path)-1
    saves = {}
    count = 0
    for line in range(len(maze))[1:-1]:
        for elt in range(len(maze[line]))[1:-1]:
            if maze[elt][line] == 1 and ((maze[elt-1][line], maze[elt+1][line]) == (0, 0) or (maze[elt][line-1], maze[elt+1][line+1]) == (0, 0)):
                maze[elt][line] = 0
                path = AStar(maze).search(start, end)
                maze[elt][line] = 1
                cheat = based_len-len(path)+1
                if cheat >= 100:
                    count +=1
                    # if cheat in saves.keys():
                    #     saves[cheat] += 1
                    # else :
                    #     saves[cheat] = 1
                        
        print(saves)    
        print(count)      
    
    



def part2():
    corpus = "input"
    liste, (size, _) = dn(corpus)
    room = [[0] * size for _ in range(size)]
    begin = (0, 0)
    end = (size-1, size-1)
    start = 2600
    for i in range(len(liste)):
        for bug in liste[:i+start] :
            room[bug[1]][bug[0]] = 1
        path = AStar(room).search(begin, end)
        #print(path)
        if path == None:
            print(liste[i-1+start])
            return

part1()

