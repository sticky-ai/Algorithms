def constructSquare(s):
    _min = int((10 ** (len(s) - 1)) ** 0.5)
    _max = int((10 ** (len(s))) ** 0.5)

    for i in range(_max, _min, -1):
        num = str(i * i)
        if sorted(s.count(n) for n in set(s)) == sorted(num.count(n) for n in set(num)):
            return int(num)
    return -1
    
