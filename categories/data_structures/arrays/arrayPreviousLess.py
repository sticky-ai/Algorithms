def arrayPreviousLess(items):
    res = [0] * len(items)
    for i in range(len(items)):
        temp = items[i]
        t = items[i]
        for j in range(i, -1, -1):
            if items[j] < temp:
                temp = items[j]
                break
        if temp == t:
            res[i] = -1
        else:
            res[i] = temp
    return res

