def firstNotDivisible(divisors, start):
    while True:
        if any([start % d == 0 for d in divisors]):
            start += 1
        else:
            return start
