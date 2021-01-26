def financialCrisis(roadRegister):
    l = len(roadRegister)
    ans = []
    for n in range(l):
        
        temp = []
        for i in range(l):
            if i != n:
                temp.append(roadRegister[i])
        
        cols = list(zip(*temp))
        
        temp2 = []
        for j in range(l):
            if j != n:
                temp2.append(cols[j])
        
        ans.append(list(map(list, temp2)))
    
    return ans
