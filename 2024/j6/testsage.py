from sage import *

MM = []
with open('j6/truc.txt' , 'r', encoding='iso-8859-1') as truc:
    for l in truc.readlines():
        MM.append(l[:-1])


def Path(M,i = 43,j = 96, drc = 'up'):
    LD = set()
    s = 0
    while True:
        if drc == 'up':
            if i>0:
                if M[i-1][j]!='#':
                    if M[i][j]!='X':
                        s += 1
                        M[i] = ''.join([M[i][:j],'X',M[i][j+1:]])
                    i -= 1
                else:
                    drc = 'right'
            else:
                s += 1
                break
        elif drc == 'left':
            if j>0:
                if M[i][j-1]!='#':
                    if M[i][j]!='X':
                        s += 1
                        M[i] = ''.join([M[i][:j],'X',M[i][j+1:]])
                    j -= 1
                else:
                    drc = 'up'
            else:
                s += 1
                break
        elif drc == 'down':
            if i<129:
                if M[i+1][j]!='#':
                    if M[i][j]!='X':
                        s += 1
                        M[i] = ''.join([M[i][:j],'X',M[i][j+1:]])
                    i += 1
                else:
                    drc = 'left'
            else:
                s += 1
                break
        elif drc == 'right':
            if j<129:
                if M[i][j+1]!='#':
                    if M[i][j]!='X':
                        s += 1
                        M[i] = ''.join([M[i][:j],'X',M[i][j+1:]])
                    j += 1
                else:
                    drc = 'down'
            else:
                s += 1
                break
        if (i,j,drc) in LD:
            return False
        else:
            LD.add((i,j,drc))
    return s

nloop = 0
for a in range(130):
    for b in range(130):
        if MM[a][b]=='.':
            M2 = MM.copy()
            M2[a] = ''.join([M2[a][:b],'#',M2[a][b+1:]])
            if Path(M2)==False:
                nloop += 1
                print(nloop)
