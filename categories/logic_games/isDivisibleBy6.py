def isDivisibleBy6(inputString):
    res = []
    for i in range(0, 10):
        if int(inputString.replace('*', str(i))) % 6 == 0:
            res.append(inputString.replace('*', str(i)))
    return res
