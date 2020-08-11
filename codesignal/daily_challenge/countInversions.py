s = []
def countInversions(a):
    c = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            c += 1
    s.append(c)
    if sorted(a) == a:
        return sum(s) % (10 ** 9 + 7)
    else:
        return countInversions(a)
