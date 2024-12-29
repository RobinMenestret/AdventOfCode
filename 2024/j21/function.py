pave = {'0':[3, 1], 'A':[3, 2], '1':[2, 0], '2':[2, 1], '3':[2, 2], '4':[1, 0], '5':[1, 1], '6':[1, 2], '7':[0, 0], '8':[0, 1], '9':[0, 2]}

arrows = {'<':[1, 0], 'v':[1, 1], '>':[1, 2], '^':[0, 1], 'A':[0, 2]}

# def is_normal(case1, case2):
#     if (case1[0] == 3 or case1[1] == 0) and (case2[0] == 3 or case2[1] == 0):
#         return False

def code_to_move(code):
    begin = 'A'
    prev = begin
    move = ''
    for case in range(len(code)):
        y = pave[code[case]][0]-pave[prev][0]
        x = pave[code[case]][1]-pave[prev][1]
        #print(prev)
        if prev == "0" or prev == "A":
            if code[case] in ["7", "4", "1"] :
                if y<0:
                    move += "^"*-y
                if x>0:
                    move += ">"*x
                if x<0:
                    move +="<"*-x
            else :
                if x>0:
                    move += ">"*x
                if x<0:
                    move +="<"*-x
                if y<0:
                    move += "^"*-y
        elif prev == "7" or prev == "4" or prev == "1" :
            if code[case] == "A" or code[case] == "0" :
                if y<0:
                    move += "^"*-y
                if x>0:
                    move += ">"*x
                if y>0:
                    move += "v"*y
            else :
                if y<0:
                    move += "^"*-y
                if y>0:
                    move += "v"*y
                if x>0:
                    move += ">"*x
        else :
            if y>0:
                move += "v"*y
            if x>0:
                move += ">"*x
            if x<0:
                move +="<"*-x
            if y<0:
                move += "^"*-y

        move += 'A'
        prev = code[case]

    #print(move)
    return move

def code_to_arrows(code):
    begin = 'A'
    prev = begin
    move = ''
    for case in range(len(code)):
        y = arrows[code[case]][0]-arrows[prev][0]
        x = arrows[code[case]][1]-arrows[prev][1]
        if x>0:
            move += ">"*x
        if y<0:
            move += "^"*-y
        if y>0:
            move += "v"*y
        if x<0:
            move +="<"*-x

        move += 'A'
        prev = code[case]
    #print(move)
    return move

def part1():
    liste = open('2024/j21/input.txt', 'r').read().split('\n')
    print(liste)
    count = 0
    for i in liste:
        t1 = len(code_to_arrows(code_to_arrows(code_to_move(i))))
        print(t1)
        t2 = int(i[:3])
        print(t2)
        count += t1*t2
    print(count)

def part2():
    liste = open('2024/j21/input.txt', 'r').read().split('\n')
    print(liste)
    count = 0
    for i in liste:
        t1 = code_to_move(i)
        for j in range(25):
            print(len(t1))
            t1 = code_to_arrows(t1)
        t1 = len(t1)
        print(t1)
        t2 = int(i[:3])
        print(t2)
        count += t1*t2
    print(count)

part2()
# digit = [
#     ['7', '8', '9'],
#     ['4', '5', '6'],
#     ['1', '2', '3'],
#     ['X', '0', 'A']
# ]

# fleches = [
#     ['X', '^', 'A'],
#     ['<', 'v', '>']
# ]
# def manual_move():
#     positions = ((3, 2), (0, 2), (0, 2))
#     entree = input()
#     if entree == '^' :
#         positions[3]
