
def compute_next(number):
    new_number = number
    new_number *= 64
    new_number = mix_n_prune(new_number, number)
    number = new_number
    new_number //= 32
    new_number = mix_n_prune(new_number, number)
    number = new_number
    new_number *= 2048
    new_number = mix_n_prune(new_number, number)

    return new_number

def mix_n_prune(n1, n2):
    new_number = n1^n2
    new_number %= 16777216
    return new_number

def part1():
    entree = open("2024/j22/input.txt", 'r').read().split('\n')
    sum = 0
    print(entree)
    for number in entree :
        cur_num = int(number)
        for _ in range(2000):
            cur_num = compute_next(cur_num)
        print(cur_num)
        sum += cur_num
    print(sum)

def part2():
    entree = open("2024/j22/input.txt", 'r').read().split('\n')
    #entree = ["123"]
    print(entree)
    recap = {}
    for number in entree :
        recap_temp = {}
        sum = [int(number[-1])]
        cur_num = int(number)
        for _ in range(2000):
            cur_num = compute_next(cur_num)
            sum.append(cur_num%10)
            if len(sum) >=5 :
                instructs = (sum[-4]-sum[-5], sum[-3]-sum[-4], sum[-2]-sum[-3], sum[-1]-sum[-2])
                if instructs in recap_temp.keys() :
                    pass
                else :
                    recap_temp[instructs] = cur_num%10
                    if instructs in recap.keys():
                        recap[instructs] += cur_num%10
                    else :
                        recap[instructs] = cur_num%10
        
        #print([sum[i+1]-sum[i] for i in range(len(sum)-1)])
        #print(recap_temp[(-1, -1, 0, 2)])
        #print(max(recap_temp, key=recap_temp.get))
        #print('\n')
    #print(recap)
    print(max(recap.values()))
    print(max(recap, key=recap.get))

part2()