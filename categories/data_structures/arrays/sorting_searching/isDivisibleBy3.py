def isDivisibleBy3(inputString):
    res = []
    for i in range(10):
        trans = int(inputString.replace('*', str(i)))
        if trans % 3 == 0:
            res.append(str(trans))
    return res
