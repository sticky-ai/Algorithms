def checkFactorial(n):
    m, i = 1, 1
    while m < n:
        m *= i
        i += 1
    return m == n
