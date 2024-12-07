def part():
    equations = open("input.txt", 'r').readlines()
    for i in range(len(equations)) :
        equations[i] = equations[i][:-1]
        equations[i] = equations[i].split(':')
        equations[i][1] = equations[i][1].split(' ')
        equations[i][1] = equations[i][1][1:]
    print(equations)

part()