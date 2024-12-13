input = open("2024/j13/input.txt", 'r').read()
print(type(input))
machines = []


for char in range(len(input)) :
    if input[char] == "A":
        x = input[char:].find("X=")+2
        y = input[char:].find("Y=")+2
        term = input[char + y:].find("\n")
        machines.append({
            "A":[int(input[char+5:char+7]), int(input[char+11:char+13])],
            "B":[int(input[char+26:char+28]), int(input[char+32:char+34])],
            "P":[int(input[char + x: char+y-4]), int(input[char + y: char + y + term])]
            })

def p1():
    price = 0
    count = 0
    for machine in machines:
        for clickA in range(100):
            for clickB in range(100):
                if machine["A"][0]*clickA + machine["B"][0]*clickB == machine["P"][0]:
                    if machine["A"][1]*clickA + machine["B"][1]*clickB == machine["P"][1] :
                        print("A : {} et B : {}".format(clickA, clickB))
                        price += 3*clickA + clickB
                        count += 1
    return price, count

def p2():
    price = 0
    count = 0
    add = 10000000000000
    #add = 0
    for machine in machines:
        machine["P"][0] += add
        machine["P"][1] += add
        B = (machine["P"][1]-(machine["A"][1]*machine["P"][0]/machine["A"][0]))/(machine["B"][1]-(machine["A"][1]*machine["B"][0]/machine["A"][0]))

        A = (machine["P"][0]-(machine["B"][0]*B))/machine["A"][0]
        
        print("A : {} et B : {}".format(A, B))
        if (abs(B - int(B))<0.01 or abs(B - int(B)-1)<0.01)and (abs(A - int(A))<0.01 or abs(A - int(A)-1)<0.01):
            price += 3*A + B
            print("A : {} et B : {}".format(A, B))
    return price

print(p2())
