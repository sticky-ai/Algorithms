def eulersTotientFunction(n):
    res = 1
    for i in range(2, n):
        if math.gcd(i, n) == 1:
            res += 1
    return res
