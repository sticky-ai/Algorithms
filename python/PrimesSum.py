def primesSum(a, b):
    return sum([i for i in range(a, b+1) if i > 1 and all([i % j for j in range(2, int(i ** 0.5) + 1)])])

