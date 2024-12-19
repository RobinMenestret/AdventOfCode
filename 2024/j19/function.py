def parser():
    file = open("2024/j19/input.txt").read().split("\n")
    return file[0].split(", "), file[2:]

def rec(model, available_towels):
    matches = []
    for i in range(len(model)+1):
        if model[:i] in available_towels :
            #print(model[:i])
            matches.append(i)
    for i in matches :
        if model[i:]=="":
            return True
        valid = rec(model[i:], available_towels)
        if valid:
            return True

    

def part1():
    available_towels, models_todo = parser()
    count = 0
    for model in models_todo:
        if rec(model, available_towels):
            print(model)
            count +=1
        #quit() if input() == "q" else True
        
    print(count)

def part1_man():
    available_towels, models_todo = parser()
    count = 0
    for model in models_todo :
        if model[:2] == "ur":
            print(model)
            # if model[3:5] not in ["ug", "br", "gr"]:
            #     print(model)
            # else :
            #     print("a test")
        else :
            count += 1
    print(count)

part1()