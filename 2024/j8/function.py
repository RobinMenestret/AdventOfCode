
def text2table():
    text = open("j8/input.txt", 'r').read()
    table=[[]]
    ligne = 0
    for i in range(len(text)):  
        
        if text[i] == "\n":
            table.append([])
            ligne +=1
        else :
            table[ligne].append(text[i])
    return table


def part1():
    table = text2table()
    nb_line = len(table)
    nb_column = len(table[0])
    count = []
    letters_done = []
    for i in range(nb_line):
        for j in range(nb_column):
            if table[i][j] != "." and table[i][j] not in letters_done: # on prend une nouvelle lettre pas déjà faite
                current_letter = table[i][j]
                letters = []
                for a in range(nb_line):
                    for b in range(nb_column):
                        if current_letter == table[a][b]:
                            letters.append([a, b])
                for point in letters:
                    x1 = point[0]
                    y1 = point[1]
                    for second_point in letters :
                        if point != second_point :
                            x2 = second_point[0]
                            y2 = second_point[1]
                            for scal in range(50):
                                if (scal+1)*x2-scal*x1 >= 0 and (scal+1)*x2-scal*x1 <nb_line and (scal+1)*y2-scal*y1 >= 0 and (scal+1)*y2-scal*y1 <nb_column : 
                                    if [(scal+1)*x2-scal*x1, (scal+1)*y2-scal*y1] not in count :
                                        print("point in : " + str((scal+1)*x2-scal*x1) + ", " + str((scal+1)*y2-scal*y1))
                                        count.append([(scal+1)*x2-scal*x1, (scal+1)*y2-scal*y1])
    print(len(count))

part1()