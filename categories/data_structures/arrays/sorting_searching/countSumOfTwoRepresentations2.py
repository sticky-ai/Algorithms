def countSumOfTwoRepresentations2(n, l, r):
    s = set()
    for i in range(l, r+1):
        if n - i in range(l, r+1):
            s.add(tuple(sorted([i, n - i])))
    return len(s)
