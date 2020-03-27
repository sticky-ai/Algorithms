def calcFinalScore(scores, n):
    gen = (i**2 for i in sorted(scores)[::-1])

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res

