
def compute_combo(x, A, B, C):
    if x == 4 :
        return A
    elif x == 5 :
        return B
    elif x == 6 :
        return C
    elif x == 7 :
        return KeyError
    else :
        return x

def adv(x, i, A, B, C):
    x = compute_combo(x, A, B, C)
    A = A//(2**x)
    return i + 2, A, B, C

def bxl(x, i, A, B, C):
    B = x^B
    return i+2, A, B, C

def bst(x, i, A, B, C):
    B = compute_combo(x, A, B, C)%8
    return i+2, A, B, C

def jnz(x, i, A, B, C):
    if A != 0 :
        if i <= len(program)-1:
            return program[i+1], A, B, C
        else :
            return i+10, A, B, C
    else :
        return i+2, A, B, C

def bxc(x, i, A, B, C):
    B = B^C
    return i+2, A, B, C

def out(x, i, A, B, C):
    x = compute_combo(x, A, B, C)%8
    print(x)
    return i+2, A, B, C

def outbis(x, i, A, B, C):
    x = compute_combo(x, A, B, C)%8
    return x, i+2, A, B, C



def bdv(x, i, A, B, C):
    x = compute_combo(x, A, B, C)
    B = A//(2**x)
    return i+2, A, B, C

def cdv(x, i, A, B, C):
    x = compute_combo(x, A, B, C)
    C = A//(2**x)
    return i+2, A, B, C

#program = [0,1,5,4,3,0]
#program = [0,3,5,4,3,0]
program = [2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0]

def main(program):
    demo = True
    if demo :
        A = 729
        B = 0
        C = 0
    else :
        A = 1332
        B = 0
        C = 0
        
    program = program
    i=0
    while i in range(len(program)) :
        if program[i] == 0 :
            i, A, B, C = adv(program[i+1], i, A, B, C)
        elif program[i] == 1 :
            i, A, B, C = bxl(program[i+1], i, A, B, C)
        elif program[i] == 2 :
            i, A, B, C = bst(program[i+1], i, A, B, C)
        elif program[i] == 3 :
            i, A, B, C = jnz(program[i+1], i, A, B, C)
        elif program[i] == 4 :
            i, A, B, C = bxc(program[i+1], i, A, B, C)
        elif program[i] == 5 :
            i, A, B, C = out(program[i+1], i, A, B, C)
        elif program[i] == 6 :
            i, A, B, C = bdv(program[i+1], i, A, B, C)
        elif program[i] == 7 :
            i, A, B, C = cdv(program[i+1], i, A, B, C)

def main2(A, program):
    demo = True
    if demo :
        B = 0
        C = 0
    else :
        B = 0
        C = 0
    program = program
    i=0
    liste = []
    while i in range(len(program)) :
        if program[i] == 0 :
            i, A, B, C = adv(program[i+1], i, A, B, C)
        elif program[i] == 1 :
            i, A, B, C = bxl(program[i+1], i, A, B, C)
        elif program[i] == 2 :
            i, A, B, C = bst(program[i+1], i, A, B, C)
        elif program[i] == 3 :
            i, A, B, C = jnz(program[i+1], i, A, B, C)
        elif program[i] == 4 :
            i, A, B, C = bxc(program[i+1], i, A, B, C)
        elif program[i] == 5 :
            x, i, A, B, C = outbis(program[i+1], i, A, B, C)
            liste.append(x)
            if liste != program[:len(liste)]:
                pass
                #break
        elif program[i] == 6 :
            i, A, B, C = bdv(program[i+1], i, A, B, C)
        elif program[i] == 7 :
            i, A, B, C = cdv(program[i+1], i, A, B, C)
    print(liste)
    return liste

def rec(program, liste, iterate, list_i):
    for i in range(10):
        liste[iterate] = i
        A = int("".join(map(str, liste)))
        output = main2(A, program)
        if program[-iterate:] == output[-iterate:] and len(output)==16:
            print("gagné")
            print(iterate)
            list_i.append(i)
            print("i : {}".format(list_i))
            
            if program == output :
                print(A)
            ok = rec(program, liste, iterate+1, list_i)
            if not ok :
                list_i.pop()
    return False
        

def part2(program):
    while True :
        iterate = 2
        list_i = []
        for i in range(10):
                liste = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                liste[iterate] = i
                A = int("".join(map(str, liste)))
                output = main2(A, program)
                if program[-iterate:] == output[-iterate:] and len(output)==16:
                    print("gagné")
                    print("i : {}".format(i))
                    list_i.append(i)
                    ok = rec(program, liste, iterate+1, list_i)
                    if not ok :
                        list_i.pop()
                    #return
        # if program == main2(A, program):
        #     print(A)
        #     return
        # #print(A)
        return
#part2(program)
def part2_bis(program):
    for i in range(10000):
        A = 109019476330624+i
        if program == main2(A, program):
            print(A)
            return

part2_bis(program)

#program = [2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0]

