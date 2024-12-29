file = open("2024/j25/input.txt", 'r').read().split('\n\n')
squares = [square.split('\n') for square in file]

def part1():
    keys = []
    locks = []
    count = 0
    for square in squares:
        if square[0] == "....." :
            keys.append(square)
        else :
            locks.append(square)
    #print(keys)
    #print(locks)
    for lock in locks :
        for key in keys :
            valid = True
            for pin in range(5):
                for height in range(5):
                    if lock[height+1][pin] == "#" and key[height+1][pin] == "#":
                        valid = False
            if valid:
                count += 1
    print(count)

part1()