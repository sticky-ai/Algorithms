def numberOfClans(divisors, k):
    d = set(divisors)
    s = set()

    for i in range(1, k + 1):
        t = tuple(x for x in d if i % x == 0)
        s.add(t)

    return len(s)
