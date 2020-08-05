def findSubarrayBySum(s, a):
    x = y = 0
    for n in a:
        y += 1
        s -= n
        while s < 0:
            s += a[x]
            x += 1
        if s == 0:
            return [x+1, y]
    return -1,
