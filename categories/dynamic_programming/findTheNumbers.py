def findTheNumbers(a):
    d = set()
    for n in a:
        d ^= {n}
    return sorted(d)
