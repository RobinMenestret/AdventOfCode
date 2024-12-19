def parser():
    file = open("2024/j19/input.txt").read().split("\n")
    return file[0].split(", "), file[2:]

def rec(current_letter, model, computed_values, available_towels):
    model_temp = model[current_letter:]
    matches = []
    for last_letter in range(len(model_temp)):
        if model_temp[:last_letter+1] in available_towels : 
            matches.append(last_letter+1)
    for last_letter in matches :
        if computed_values[current_letter+last_letter] != 0 :
            computed_values[current_letter] += computed_values[current_letter+last_letter]
        elif len(model_temp) == last_letter :
            computed_values[current_letter] += 1
        else :
            computed_values = rec(current_letter+last_letter, model, computed_values, available_towels)
            computed_values[current_letter]+=computed_values[current_letter+last_letter]
    return computed_values

    

def part1():
    available_towels, models_todo = parser()
    count = 0
    for model in models_todo:
        computed_values = [0]*(len(model)+1)
        computed_values = rec(0, model, computed_values, available_towels)
        count += computed_values[0]
        #print(model)
        #quit() if input() == "q" else True
        
    print(count)

part1()