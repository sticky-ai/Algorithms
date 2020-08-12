def champernowneDigit(n):
    s = ''
    i = 1
    while True:
        s += str(i)
        i += 1
        if len(s) > n+1:
            break
    return int(s[n-1])
