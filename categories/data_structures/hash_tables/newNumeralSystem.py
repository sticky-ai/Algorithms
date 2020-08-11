def newNumeralSystem(number):
    dic = {k:v for k, v in enumerate(string.ascii_uppercase)}
    target = string.ascii_uppercase.index(number)
    res = []
    nRange = sorted(list(range(target+1)) + [target // 2])
    try:
        while nRange:
            s, e = nRange.pop(0), nRange.pop()
            if s + e == target:
                res.append([s, e])
    except:
        pass
    
    return [dic[f] +  ' + ' + dic[s] for f, s in res]
