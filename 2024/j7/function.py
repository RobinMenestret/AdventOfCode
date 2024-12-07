def part():
    equations = open("j7/input.txt", 'r').readlines()
    for i in range(len(equations)) :
        equations[i] = equations[i][:-1]
        equations[i] = equations[i].split(':')
        equations[i][1] = equations[i][1].split(' ')
        equations[i][1] = equations[i][1][1:]
    valide = 0
    for equation in equations :
        value = int(equation[0])            
        quant_nombre = len(equation[1])
        operators = 2**(quant_nombre-1)-1 # 0 : + , 1 : x
        while True :
            count = int(equation[1][0])
            operators +=1
            bin_op = bin(operators)
            
            for nombre in range(quant_nombre-1):
                #print(bin_op[nombre+3])
                if count > value :
                    break
                if bin_op[nombre+3] == "0" :
                    count += int(equation[1][nombre+1])
                else :
                    count *= int(equation[1][nombre+1])
            if count == value :
                valide += value
                print(value)
                break
            

            if operators == 2*2**len(equation[1]):
                break
    print(valide)
            


#part()

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def part2():
    equations = open("j7/input.txt", 'r').readlines()
    for i in range(len(equations)) :
        equations[i] = equations[i][:-1]
        equations[i] = equations[i].split(':')
        equations[i][1] = equations[i][1].split(' ')
        equations[i][1] = equations[i][1][1:]
    valide = 0
    for equation in equations :
        value = int(equation[0])            
        quant_nombre = len(equation[1])
        operators = 3**(quant_nombre-1)-1 # 0 : + , 1 : x
        while True :
            count = int(equation[1][0])
            operators +=1
            ter_op = ternary(operators)
            
            for nombre in range(quant_nombre-1):
                if count > value :
                    break
                if ter_op[nombre+1] == "0" :
                    count += int(equation[1][nombre+1])
                elif ter_op[nombre+1] == "1" :
                    count *= int(equation[1][nombre+1])
                else :
                    count = int(str(count)+equation[1][nombre+1])
            if count == value :
                valide += value
                print(value)
                break
            

            if operators == 3*3**quant_nombre:
                break
            #print(count)
    print(valide)
            
part2()