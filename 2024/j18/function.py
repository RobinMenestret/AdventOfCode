from astar.search import AStar

def dn(corpus):
    return [[int(l[0]), int(l[1].rstrip())] for l in [l.split(",") for l in open('2024/j18/'+ corpus + '.txt', 'r').readlines()]], (7, 12) if corpus == "demo" else (71, 1024)


def part1():
    corpus = "input"
    liste, (size, param) = dn(corpus)
    room = [[0] * size for _ in range(size)]
    begin = (0, 0)
    end = (size-1, size-1)
    for bug in liste[:param] :
        room[bug[1]][bug[0]] = 1
    print(room)
    path = AStar(room).search(begin, end)
    print(len(path))

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

part2()
