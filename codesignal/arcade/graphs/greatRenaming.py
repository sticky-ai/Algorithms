from collections import defaultdict

def greatRenaming(roadRegister):
    d = defaultdict(list)
    l = len(roadRegister)
       
    for i in range(l):
        for j in range(l):
            if roadRegister[i][j]:
                d[i].append(j)
    
    new_d = dict()
    for k, v in d.items():
        if k == l - 1:
            new_d[0] = [0 if n == l-1 else n+1 for n in v]
        else:
            new_d[k+1] = [0 if n == l-1 else n+1 for n in v]
    
    for k, v in sorted(new_d.items()):
        for n in v:
            roadRegister[k][n] = '1'
    
    for i in range(l):
        for j in range(l):
            if roadRegister[i][j] == '1':
                roadRegister[i][j] = True
            else:
                roadRegister[i][j] = False
    
    return roadRegister


# def greatRenaming(roadRegister):
#     swap = lambda x: [x[-1]] + x[:-1]
#     return swap([swap(i) for i in roadRegister])
