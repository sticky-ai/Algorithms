def leastFactorial(n):
    s = i = 1
    while s < n:
        s *= i
        i += 1
    return s
