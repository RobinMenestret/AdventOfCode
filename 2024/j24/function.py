text = [line.split('\n') for line in open('2024/j24/input.txt', 'r').read().split('\n\n')]
begin = [(line[0], int(line[1])) for line in [op.split(': ') for op in [line for line in text[0]]]]
ops = [(nb[0].split(' '), nb[1]) for nb in [op.split(' -> ') for op in [line for line in text[1]]]]

print(begin)
print(ops)

def rec(input_1, input_2, op):
    out = [-1, -1]
    for entree in begin :
        if input_1 == entree[0]:
            out[0] = entree[1]
    for entree in begin :
        if input_2 == entree[0]:
            out[1] = entree[1]
    if out[0] == -1 :
        for operation in ops :
            if input_1 == operation[1] :
                out[0] = rec(operation[0][0], operation[0][2], operation[0][1])
    if out[1] == -1 :
        for operation in ops :
            if input_2 == operation[1] :
                out[1] = rec(operation[0][0], operation[0][2], operation[0][1])

    if op == 'AND':
        return out[0] and out[1]
    if op == 'OR':
        return out[0] or out[1]
    if op == 'XOR':
        return out[0] ^ out[1]

x, y = map(lambda indice : sum([list(filter(lambda line : line[0][0] == indice, begin))[i][1]*2**i for i in range(len(list(filter(lambda line : line[0][0] == indice, begin))))]), ['x', 'y'])
xpy = x+y
    

def part1():
    zs = {}
    count = 0
    for op in ops :
        if op[1][0] == 'z': 
            zs[op[1]] = rec(op[0][0], op[0][2], op[0][1])
            print("{} vaut {}".format(op[1], zs[op[1]]))
    for key in zs.keys():
        count += zs[key] * 2** int(key[1:])

    return count


def part2():
    print(x)
    print(y)
    
#list(filter(lambda line : line[0][0] == indice, begin))
