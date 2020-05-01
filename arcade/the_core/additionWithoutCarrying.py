def additionWithoutCarrying(param1, param2):
    param1, param2 = map(str, [param1, param2])
    max_len = max(len(param1), len(param2))
    
    if len(param1) == max_len:
        param2 = param2.zfill(max_len)
    else:
        param1 = param1.zfill(max_len)

    return int(''.join(map(str, [sum(map(int, i)) % 10 for i in zip(param1, param2)])))
        
