def deleteDigit(n):
    res = []
    for i in range(len(str(n))):
        temp = list(str(n))
        temp.pop(i)
        res.append(int(''.join(temp)))
    return max(res)
