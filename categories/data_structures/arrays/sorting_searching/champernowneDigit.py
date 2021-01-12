def champernowneDigit(n):
    s = ''
    for i in range(1, n+1):
        s += str(i)
    return int(list(s)[n-1])
