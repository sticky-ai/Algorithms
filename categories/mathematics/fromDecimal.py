def fromDecimal(b, n):
    s = ''
    while n >= 1:
        s += str(n % b)
        n = n // b
    return s[::-1]
