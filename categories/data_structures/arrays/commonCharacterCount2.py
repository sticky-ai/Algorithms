def commonCharacterCount2(s):
    char = set(s[0])
    
    res = []
    for i in s:
        temp = []
        for c in char:
            temp.append(i.count(c))
        res.append(temp)
    
    cnt = 0
    for z in zip(*res):
        if 0 in z:
            continue
        
        cnt += min(z)
    
    return cnt
