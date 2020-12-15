def magicalWell(a, b, n):
    s = 0
    for _ in range(n):
        s += a * b
        a += 1
        b += 1
    return s
