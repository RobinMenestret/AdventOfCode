
links = [sorted(link.split('-')) for link in open('2024/j23/input.txt', 'r').read().split('\n')]
pcs = []
for link in links :
    for i in range(2):
        if link[i] not in pcs :
            pcs.append(link[i])



def find_maximale_clique(cur_pc, pcs, links):
    clique = [cur_pc]
    for pc in pcs :
        is_in = True
        for clique_pc in clique :
            if sorted([clique_pc, pc]) not in links :
                is_in = False
        if is_in :
            clique.append(pc)
    return clique  
      
def bronKerbosch(R,P,X):
    if (P,X) == ([], []):
        print(len(R))
        print(str(R).lstrip("'"))
        input()
        return
    for v in P :
        next_R = sorted(R+[v])
        next_P = P.copy()
        for pc in range(len(next_P)) :
            if sorted([next_P[pc], v]) not in links:
                next_P[pc] = 'None'
        next_P = list(filter(lambda x : x!="None", next_P))
        next_X = X.copy()
        for pc in range(len(next_X)) :
            if sorted([next_X[pc], v]) not in links:
                next_X[pc] = 'None'
        next_X = list(filter(lambda x : x!="None", next_X))
        bronKerbosch(next_R, next_P, next_X) 
        try :
            P.remove(v)
        except :
            pass
        if v not in X :
            X.append(v) 

def part2():
    bronKerbosch([], pcs, [])
    

part2()


def part1():
    triplets = []
    count = 0
    c = 0
    for link in links :
        c+=1
        for pc in pcs :
            if sorted([pc, link[0]]) in links and sorted([pc, link[1]]) in links :
                triplet = [pc, link[0], link[1]]
                triplet.sort()
                #print(triplet)
                
                if triplet not in triplets :
                    triplets.append(triplet)
                    if pc[0] == 't'or link[0][0] == 't' or link[1][0] == 't':
                        count +=1
        #input()
        print('{} t sur {}'.format(count, c))
        
